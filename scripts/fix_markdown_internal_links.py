#!/usr/bin/env python3
"""Fix internal markdown references converted from PDF.

Rules implemented:
- Skip `rmm-contents.md` unchanged.
- Preserve existing markdown links unchanged.
- Convert plain bullets like:
  - `- A2.1 Realm`
  - `- Chapter B4 Realm Management Interface`
  into links using local file/anchor resolution.
- If no target can be resolved, keep the original line and report it.

Output is written to new folders (input copied/rewritten file-by-file).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

# Section IDs in this spec family are A..E with non-leading-zero numeric parts.
SECTION_ID_RE = r"[A-E](?:0|[1-9]\d*)(?:\.(?:0|[1-9]\d*))*"
HEADING_SECTION_RE = re.compile(
    rf"^(?:Chapter\s+)?(?P<section>{SECTION_ID_RE})(?:\s+|$)"
)
BULLET_REF_RE = re.compile(
    rf"^(?P<prefix>\s*-\s+)(?P<label>(?P<chapter>Chapter\s+)?(?P<section>{SECTION_ID_RE})\s+.+?)\s*$"
)
EXISTING_MD_LINK_RE = re.compile(r"\[[^\]]+\]\([^\)]+\)")
HEADING_RE = re.compile(r"^##\s+(?P<text>.+?)\s*$")


@dataclass(frozen=True)
class HeadingTarget:
    file_name: str
    anchor: str
    heading_text: str


@dataclass
class FileChange:
    file_name: str
    changed_lines: int


@dataclass
class UnresolvedRef:
    file_name: str
    line: int
    section: str
    label: str


def github_slug(text: str) -> str:
    """Best-effort GitHub-like slug generation for ASCII-heavy headings."""
    # Handle escaped markdown punctuation from docling output, e.g. RMI\_FOO.
    text = re.sub(r"\\([\\`*_{}\[\]()#+\-.!])", r"\1", text)
    text = text.strip().lower()
    # Keep word chars (includes underscore), spaces, and '-'.
    text = re.sub(r"[^\w\- ]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def parse_pairs(pairs: Sequence[str]) -> List[Tuple[Path, Path]]:
    parsed: List[Tuple[Path, Path]] = []
    for raw in pairs:
        if ":" not in raw:
            raise ValueError(f"Invalid --pair '{raw}'. Expected format input_dir:output_dir")
        inp, out = raw.split(":", 1)
        parsed.append((Path(inp), Path(out)))
    return parsed


def build_heading_index(input_dir: Path) -> Tuple[Dict[str, HeadingTarget], Dict[str, int]]:
    section_to_target: Dict[str, HeadingTarget] = {}
    duplicates: Dict[str, int] = {}

    for md_path in sorted(input_dir.glob("*.md")):
        with md_path.open("r", encoding="utf-8") as f:
            lines = f.readlines()

        slug_counts: Dict[str, int] = {}

        for line in lines:
            m = HEADING_RE.match(line)
            if not m:
                continue

            heading_text = m.group("text").strip()
            base_slug = github_slug(heading_text)
            if not base_slug:
                continue

            # GitHub-style duplicate disambiguation per file: -1, -2, ...
            n = slug_counts.get(base_slug, 0)
            slug_counts[base_slug] = n + 1
            anchor = base_slug if n == 0 else f"{base_slug}-{n}"

            sm = HEADING_SECTION_RE.match(heading_text)
            if not sm:
                continue

            section = sm.group("section")
            if section in section_to_target:
                duplicates[section] = duplicates.get(section, 1) + 1
                continue

            section_to_target[section] = HeadingTarget(
                file_name=md_path.name,
                anchor=anchor,
                heading_text=heading_text,
            )

    return section_to_target, duplicates


def resolve_link(section: str, section_to_target: Dict[str, HeadingTarget], file_set: set[str]) -> Optional[str]:
    direct = f"rmm-{section}.md"
    if direct in file_set:
        return direct

    target = section_to_target.get(section)
    if not target:
        return None

    return f"{target.file_name}#{target.anchor}"


def rewrite_file(
    input_path: Path,
    output_path: Path,
    section_to_target: Dict[str, HeadingTarget],
    file_set: set[str],
) -> Tuple[int, List[UnresolvedRef]]:
    with input_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    changed = 0
    unresolved: List[UnresolvedRef] = []
    out_lines: List[str] = []
    in_see_also = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip().lower()
        if stripped in {"see also:", "## see also:"}:
            in_see_also = True
            out_lines.append(line)
            continue

        if in_see_also and stripped and not line.lstrip().startswith("- "):
            in_see_also = False

        if not in_see_also:
            out_lines.append(line)
            continue

        if EXISTING_MD_LINK_RE.search(line):
            out_lines.append(line)
            continue

        m = BULLET_REF_RE.match(line)
        if not m:
            out_lines.append(line)
            continue

        label = m.group("label")
        section = m.group("section")
        prefix = m.group("prefix")

        target = resolve_link(section=section, section_to_target=section_to_target, file_set=file_set)
        if target is None:
            unresolved.append(
                UnresolvedRef(
                    file_name=input_path.name,
                    line=i,
                    section=section,
                    label=label,
                )
            )
            out_lines.append(line)
            continue

        newline = "\n" if line.endswith("\n") else ""
        new_line = f"{prefix}[{label}]({target}){newline}"
        if new_line != line:
            changed += 1
        out_lines.append(new_line)

    output_path.write_text("".join(out_lines), encoding="utf-8")
    return changed, unresolved


def process_pair(input_dir: Path, output_dir: Path) -> Dict[str, object]:
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    if output_dir.exists():
        raise FileExistsError(f"Output directory already exists: {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=False)

    md_files = sorted(input_dir.glob("*.md"))
    file_set = {p.name for p in md_files}

    section_to_target, duplicates = build_heading_index(input_dir)

    changes: List[FileChange] = []
    unresolved: List[UnresolvedRef] = []

    for in_path in md_files:
        out_path = output_dir / in_path.name

        # Explicit user requirement: keep this file untouched.
        if in_path.name == "rmm-contents.md":
            out_path.write_text(in_path.read_text(encoding="utf-8"), encoding="utf-8")
            changes.append(FileChange(file_name=in_path.name, changed_lines=0))
            continue

        changed_lines, unresolved_refs = rewrite_file(
            input_path=in_path,
            output_path=out_path,
            section_to_target=section_to_target,
            file_set=file_set,
        )
        changes.append(FileChange(file_name=in_path.name, changed_lines=changed_lines))
        unresolved.extend(unresolved_refs)

    changed_files = sum(1 for c in changes if c.changed_lines > 0)
    changed_lines = sum(c.changed_lines for c in changes)

    return {
        "input_dir": str(input_dir),
        "output_dir": str(output_dir),
        "files_total": len(md_files),
        "files_changed": changed_files,
        "lines_changed": changed_lines,
        "duplicate_section_ids": duplicates,
        "unresolved_count": len(unresolved),
        "unresolved": [u.__dict__ for u in unresolved],
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Fix internal markdown references for RMM docs")
    parser.add_argument(
        "--pair",
        action="append",
        default=[],
        help="Input/output pair in format input_dir:output_dir. Can be repeated.",
    )
    parser.add_argument(
        "--report",
        default="link-fix-report.json",
        help="Path to write JSON report",
    )

    args = parser.parse_args(argv)

    pairs = args.pair or [
        "orig-rmm-v1:fixed-rmm-v1-auto",
        "orig-rmm-v2:fixed-rmm-v2-auto",
    ]

    try:
        parsed_pairs = parse_pairs(pairs)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    report: Dict[str, object] = {"runs": []}

    try:
        for input_dir, output_dir in parsed_pairs:
            run_result = process_pair(input_dir=input_dir, output_dir=output_dir)
            report["runs"].append(run_result)
    except Exception as e:  # noqa: BLE001 - CLI tool should surface clean errors.
        print(f"error: {e}", file=sys.stderr)
        return 1

    report_path = Path(args.report)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    total_files_changed = sum(r["files_changed"] for r in report["runs"])  # type: ignore[index]
    total_lines_changed = sum(r["lines_changed"] for r in report["runs"])  # type: ignore[index]
    total_unresolved = sum(r["unresolved_count"] for r in report["runs"])  # type: ignore[index]

    print(f"Wrote report: {report_path}")
    print(f"Changed files: {total_files_changed}")
    print(f"Changed lines: {total_lines_changed}")
    print(f"Unresolved references: {total_unresolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
