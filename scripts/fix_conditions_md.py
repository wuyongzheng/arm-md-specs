#!/usr/bin/env python3
"""Normalize docling-converted markdown condition sections.

This script rewrites only sections whose headings contain:
- "Failure conditions" (excluding "Failure condition ordering")
- "Success conditions"

It converts corrupted table/code-fence/plain-text condition content into a
canonical bullet format.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TABLE_ROW_RE = re.compile(r"^\|(.+)\|\s*$")
SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
IDENTIFIER_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
CONDITION_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
SECTION_ID_RE = re.compile(r"^B\d+(?:\.\d+){3}$")

GARBAGE_LINE_RE = re.compile(
    r"^(?:#{1,6}\s*)?(?:ID|Condition|ID\s+Condition)(?:\s+[A-Za-z0-9_().-]+){0,3}\s*$",
    re.IGNORECASE,
)

LABELED_RECORD_START_RE = re.compile(
    r"(?<![A-Za-z0-9_])([a-z][a-z0-9_]*(?:\s+[a-z]{1,3})?)\s+(pre:|post:)",
)

DUPLICATE_ID_RECORD_START_RE = re.compile(
    r"(?<![A-Za-z0-9_])([a-z][a-z0-9_]*)\s+\1\s+"
)

PRE_POST_MARKER_RE = re.compile(r"(?<![A-Za-z0-9_])(pre:|post:)", re.IGNORECASE)

# Conservative split used only for malformed "pre: post: <preexpr> <postexpr>" rows.
OBVIOUS_POST_START_RE = re.compile(
    r"\b(result(?:\.status)?\s*==|ResultEqual\s*\(|response\s*==|value\s*==)"
)


@dataclass
class Record:
    id: str
    pre: str = ""
    post: str = ""
    exprs: list[str] = field(default_factory=list)

    def has_content(self) -> bool:
        return bool(self.pre or self.post or self.exprs)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace(r"\_", "_")
    return text


def normalize_identifier(raw: str) -> str:
    s = clean_text(raw).strip()
    s = re.sub(r"\s+", " ", s)
    if " " not in s:
        return s

    # Only join obviously split identifier tails, e.g. "comm_sta te" -> "comm_state".
    parts = s.split(" ")
    if len(parts) == 2 and IDENTIFIER_RE.match(parts[0]) and re.fullmatch(r"[A-Za-z]{1,4}", parts[1]):
        return parts[0] + parts[1]
    return s


def looks_like_condition_id(value: str) -> bool:
    return bool(CONDITION_ID_RE.fullmatch(value))


def is_image_line(line: str) -> bool:
    return "<!-- image -->" in line.lower()


def parse_marked_text(content: str) -> tuple[str, str, list[str]]:
    """Parse pre:/post: markers inside one record payload."""
    s = normalize_whitespace(clean_text(content))
    if not s:
        return "", "", []

    markers = list(PRE_POST_MARKER_RE.finditer(s))
    if not markers:
        return "", "", [s]

    pre = ""
    post = ""
    extras: list[str] = []

    for i, m in enumerate(markers):
        label = m.group(1).lower().rstrip(":")
        start = m.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(s)
        value = normalize_whitespace(s[start:end])
        if not value:
            continue
        if label == "pre":
            pre = f"{pre} {value}".strip() if pre else value
        elif label == "post":
            post = f"{post} {value}".strip() if post else value
        else:
            extras.append(value)

    # Handle malformed "pre: post: <preexpr> <postexpr>" case conservatively.
    if not pre and post and s.lower().startswith("pre: post:"):
        m = OBVIOUS_POST_START_RE.search(post)
        if m and m.start() > 0:
            pre = normalize_whitespace(post[: m.start()])
            post = normalize_whitespace(post[m.start() :])

    return pre, post, extras


def parse_table_row(line: str) -> list[str] | None:
    m = TABLE_ROW_RE.match(line.rstrip("\n"))
    if not m:
        return None
    cells = [clean_text(c.strip()) for c in m.group(1).split("|")]
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return all(SEPARATOR_CELL_RE.fullmatch(c.strip()) for c in cells if c.strip())


def parse_table_records(lines: list[str]) -> tuple[list[Record], list[str]]:
    records: list[Record] = []
    leftovers: list[str] = []

    for line in lines:
        cells = parse_table_row(line)
        if cells is None:
            leftovers.append(line)
            continue

        if not cells or is_separator_row(cells):
            continue

        if len(cells) >= 2:
            c0 = normalize_whitespace(cells[0])
            c1 = normalize_whitespace(cells[1]).lower()
            if SECTION_ID_RE.fullmatch(c0) and "footprint" in c1:
                break

        first = normalize_whitespace(cells[0]).lower()
        if first in {"id", "condition", "id condition"}:
            continue
        if first == "id" and len(cells) >= 2 and normalize_whitespace(cells[1]).lower() == "value":
            # Embedded footprint table starts here; stop collecting conditions.
            break

        if len(cells) == 1:
            extra_records, _ = parse_labeled_flattened(cells[0])
            if extra_records:
                records.extend(extra_records)
                continue
            extra_records, _ = parse_duplicate_id_flattened(cells[0])
            if extra_records:
                records.extend(extra_records)
                continue

        rid = normalize_identifier(cells[0])
        if not looks_like_condition_id(rid):
            continue
        payload = normalize_whitespace(" ".join(c for c in cells[1:] if c))
        if not rid:
            continue

        pre, post, exprs = parse_marked_text(payload)
        records.append(Record(id=rid, pre=pre, post=post, exprs=exprs))

    return records, leftovers


def parse_structured_lines(lines: list[str]) -> tuple[list[Record], list[str]]:
    """Parse blocks where IDs and pre/post may be on separate lines."""
    records: list[Record] = []
    stray: list[str] = []

    current: Record | None = None
    current_field: str | None = None
    pending_expr: str | None = None

    def flush_current() -> None:
        nonlocal current, current_field
        if current and (current.has_content() or current.id):
            records.append(current)
        current = None
        current_field = None

    for raw in lines:
        line = normalize_whitespace(clean_text(raw))
        if not line:
            continue
        if line == "```":
            continue
        if is_image_line(line):
            continue
        if GARBAGE_LINE_RE.match(line):
            continue

        if IDENTIFIER_RE.fullmatch(line) and looks_like_condition_id(line):
            flush_current()
            current = Record(id=normalize_identifier(line))
            if pending_expr:
                current.exprs.append(pending_expr)
                pending_expr = None
            current_field = None
            continue

        if current is not None and current_field in {"pre", "post"}:
            # Keep constants/operators split across lines as part of the field.
            if current_field == "pre":
                current.pre = f"{current.pre} {line}".strip() if current.pre else line
            else:
                current.post = f"{current.post} {line}".strip() if current.post else line
            continue

        low = line.lower()
        if low in {"pre:", "post:"}:
            if current is None:
                stray.append(line)
                continue
            current_field = low.rstrip(":")
            continue

        if current is None:
            if re.search(r"(==|!=|<=|>=|<|>)", line):
                pending_expr = line
            stray.append(line)
            continue

        if current_field == "pre":
            current.pre = f"{current.pre} {line}".strip() if current.pre else line
        elif current_field == "post":
            current.post = f"{current.post} {line}".strip() if current.post else line
        else:
            if current.exprs:
                current.exprs[-1] = f"{current.exprs[-1]} {line}".strip()
            else:
                current.exprs.append(line)

    flush_current()
    return records, stray


def parse_labeled_flattened(text: str) -> tuple[list[Record], str]:
    s = normalize_whitespace(clean_text(text))
    s = re.sub(r"^(?:ID\s+Condition|Condition|ID)\s+", "", s, flags=re.IGNORECASE)
    if not s:
        return [], ""

    starts = list(LABELED_RECORD_START_RE.finditer(s))
    if not starts:
        return [], s

    records: list[Record] = []
    consumed_ranges: list[tuple[int, int]] = []

    for i, m in enumerate(starts):
        start = m.start()
        end = starts[i + 1].start() if i + 1 < len(starts) else len(s)
        seg = s[start:end].strip()

        rid = normalize_identifier(m.group(1))
        if not looks_like_condition_id(rid):
            continue
        after_id = seg[len(m.group(1)) :].strip()

        pre, post, exprs = parse_marked_text(after_id)
        records.append(Record(id=rid, pre=pre, post=post, exprs=exprs))
        consumed_ranges.append((start, end))

    chars = list(s)
    for a, b in consumed_ranges:
        for j in range(a, b):
            chars[j] = " "
    leftover = normalize_whitespace("".join(chars))
    return records, leftover


def parse_duplicate_id_flattened(text: str) -> tuple[list[Record], str]:
    s = normalize_whitespace(clean_text(text))
    if not s:
        return [], ""

    starts = list(DUPLICATE_ID_RECORD_START_RE.finditer(s))
    labeled_starts = [m.start() for m in LABELED_RECORD_START_RE.finditer(s)]
    if not starts:
        return [], s

    records: list[Record] = []
    consumed_ranges: list[tuple[int, int]] = []

    for i, m in enumerate(starts):
        start = m.start()
        end = starts[i + 1].start() if i + 1 < len(starts) else len(s)
        for ls in labeled_starts:
            if ls > start:
                end = min(end, ls)
                break
        seg = s[start:end].strip()
        rid = m.group(1)
        if not looks_like_condition_id(rid):
            continue
        prefix = f"{rid} {rid} "
        if not seg.startswith(prefix):
            continue
        expr = normalize_whitespace(seg[len(prefix) :])
        if not expr:
            continue
        if re.match(r"^(==|!=|<=|>=|<|>)", expr):
            expr = f"{rid} {expr}"
        if expr.endswith("(") and expr.count("(") > expr.count(")") and " " in expr:
            head, tail = expr.rsplit(" ", 1)
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*\(", tail):
                expr = head
        records.append(Record(id=rid, exprs=[expr]))
        consumed_ranges.append((start, end))

    chars = list(s)
    for a, b in consumed_ranges:
        for j in range(a, b):
            chars[j] = " "
    leftover = normalize_whitespace("".join(chars))
    return records, leftover


def parse_simple_id_expr_flattened(text: str) -> tuple[list[Record], str]:
    """Parse conservative 'id <expression>' flattened records."""
    s = normalize_whitespace(clean_text(text))
    if not s:
        return [], ""

    raw_starts = list(re.finditer(r"(?:^|\s)([a-z][a-z0-9_]*)\s+", s))
    starts = []
    for m in raw_starts:
        rid = m.group(1)
        if not looks_like_condition_id(rid):
            continue
        # Conservative gate: likely record payloads include comparisons or function calls.
        lookahead = s[m.end() : m.end() + 160]
        if not re.search(r"(==|!=|<=|>=|<|>|[A-Za-z_][A-Za-z0-9_]*\s*\()", lookahead):
            continue
        starts.append(m)
    if not starts:
        return [], s

    records: list[Record] = []
    consumed_ranges: list[tuple[int, int]] = []

    for i, m in enumerate(starts):
        rid = m.group(1)
        start = m.start(1)
        end = starts[i + 1].start(1) if i + 1 < len(starts) else len(s)
        seg = s[start:end].strip()
        expr = normalize_whitespace(seg[len(rid) :].strip())
        if not expr:
            continue
        if expr.lower().startswith(("pre:", "post:")):
            continue
        if not re.search(r"(==|!=|<=|>=|<|>|[A-Za-z_][A-Za-z0-9_]*\s*\()", expr):
            continue
        if re.match(r"^(==|!=|<=|>=|<|>)", expr):
            expr = f"{rid} {expr}"
        if expr.endswith("(") and expr.count("(") > expr.count(")") and " " in expr:
            # Drop obvious trailing orphan token (often leaked from next broken line).
            head, tail = expr.rsplit(" ", 1)
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*\(", tail):
                expr = head
        records.append(Record(id=rid, exprs=[expr]))
        consumed_ranges.append((start, end))

    chars = list(s)
    for a, b in consumed_ranges:
        for j in range(a, b):
            chars[j] = " "
    leftover = normalize_whitespace("".join(chars))
    return records, leftover


def dedupe_preserve_order(records: Iterable[Record]) -> list[Record]:
    src = list(records)
    out: list[Record] = []
    i = 0
    while i < len(src):
        r = src[i]
        if not r.id:
            i += 1
            continue
        # Remove garbage pseudo-ids conservatively.
        if GARBAGE_LINE_RE.match(r.id):
            i += 1
            continue
        if r.pre and not r.post and " post:" in r.pre.lower():
            pre, post, extras = parse_marked_text(f"pre: {r.pre}")
            if pre:
                r.pre = pre
            if post:
                r.post = post
            if extras:
                r.exprs.extend(extras)
        # Merge a known split pattern: "handle pre: Handle is" + "invalid post: ...".
        if (
            r.id == "handle"
            and r.pre.lower().endswith(" is")
            and i + 1 < len(src)
            and src[i + 1].id == "invalid"
            and not src[i + 1].pre
            and src[i + 1].post
        ):
            r.pre = f"{r.pre} invalid"
            if not r.post:
                r.post = src[i + 1].post
            i += 1
        if r.id == "rim" and r.exprs:
            fixed_exprs = []
            for e in r.exprs:
                if "== realm," in e and "RimExtendRipas(" not in e:
                    e = e.replace("== realm,", "== RimExtendRipas(realm,", 1)
                fixed_exprs.append(e)
            r.exprs = fixed_exprs
        out.append(r)
        i += 1
    return out


def render_records(records: list[Record]) -> list[str]:
    lines: list[str] = []
    for r in records:
        lines.append(f"* {r.id}\n")
        if r.pre:
            lines.append(f"  * pre: {r.pre}\n")
        if r.post:
            lines.append(f"  * post: {r.post}\n")
        for expr in r.exprs:
            if expr:
                lines.append(f"  * {expr}\n")
    if lines and lines[-1] != "\n":
        lines.append("\n")
    return lines


def fix_condition_section(body_lines: list[str]) -> tuple[list[str], dict]:
    diag = {
        "records": 0,
        "had_leftover": False,
        "leftover_preview": "",
    }

    # Phase 1: parse table rows.
    table_records, leftovers = parse_table_records(body_lines)

    # Remove obvious garbage lines from leftovers for next phases.
    cleaned_leftovers = []
    for line in leftovers:
        stripped = clean_text(line).strip()
        if GARBAGE_LINE_RE.match(stripped):
            continue
        if is_image_line(stripped):
            continue
        if stripped == "```":
            continue
        cleaned_leftovers.append(line)

    # Phase 2: structured line parser.
    structured_records, stray_lines = parse_structured_lines(cleaned_leftovers)

    # Phase 3: flattened parser on unresolved text.
    stray_text = " ".join(clean_text(s).strip() for s in stray_lines if s.strip())
    dup_records, t1 = parse_duplicate_id_flattened(stray_text)
    labeled_records, t2 = parse_labeled_flattened(t1)
    simple_records, final_leftover = parse_simple_id_expr_flattened(t2)

    records = dedupe_preserve_order(
        table_records + structured_records + labeled_records + dup_records + simple_records
    )

    # If parsing failed entirely, keep non-garbage body to avoid destructive rewrite.
    if not records:
        passthrough = []
        for line in body_lines:
            stripped = clean_text(line).strip()
            if GARBAGE_LINE_RE.match(stripped):
                continue
            if is_image_line(stripped):
                continue
            if stripped == "```":
                continue
            passthrough.append(line)
        if passthrough and passthrough[-1].strip() != "":
            passthrough.append("\n")
        if final_leftover:
            diag["had_leftover"] = True
            diag["leftover_preview"] = final_leftover[:200]
        return passthrough, diag

    out_lines = render_records(records)
    diag["records"] = len(records)
    if final_leftover:
        diag["had_leftover"] = True
        diag["leftover_preview"] = final_leftover[:200]
    return out_lines, diag


def transform_markdown(text: str) -> tuple[str, dict]:
    # Recover section headings that are inlined into paragraph text.
    text = re.sub(
        r"\s+(B\d+(?:\.\d+){3}\s+(?:Failure conditions|Failure condition ordering|Success conditions|Footprint))",
        r"\n## \1",
        text,
    )
    # If trailing payload appears on the heading line, push it to the next line.
    text = re.sub(
        r"(##\s+B\d+(?:\.\d+){3}\s+(?:Failure conditions|Failure condition ordering|Success conditions|Footprint))\s+([^\n#].+)",
        r"\1\n\2",
        text,
    )
    # Collapse accidental duplicate heading markers introduced by recovery.
    text = re.sub(r"\n##\s*\n(##\s+B\d)", r"\n\1", text)
    lines = text.splitlines(keepends=True)
    heading_indices: list[int] = []

    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.rstrip("\n"))
        if not m:
            continue
        # Treat pseudo headings ("## ID", "## Condition", "## ID Condition")
        # as content, not structural section boundaries.
        if GARBAGE_LINE_RE.match(m.group(2).strip()):
            continue
        if m:
            heading_indices.append(i)

    if not heading_indices:
        return text, {"sections_changed": 0, "sections": []}

    sections_meta = []
    out: list[str] = []
    cursor = 0

    for idx, start in enumerate(heading_indices):
        heading_line = lines[start]
        m = HEADING_RE.match(heading_line.rstrip("\n"))
        assert m is not None
        title = m.group(2)

        end = heading_indices[idx + 1] if idx + 1 < len(heading_indices) else len(lines)

        # Copy any gap before heading (normally none).
        if cursor < start:
            out.extend(lines[cursor:start])

        out.append(heading_line)
        body = lines[start + 1 : end]

        lower_title = title.lower()
        is_failure_conditions = "failure conditions" in lower_title and "ordering" not in lower_title
        is_success_conditions = "success conditions" in lower_title
        is_footprint = "footprint" in lower_title

        if is_failure_conditions or is_success_conditions:
            # Always keep one blank line after transformed condition section titles.
            out.append("\n")
            new_body, diag = fix_condition_section(body)
            out.extend(new_body)
            sections_meta.append({"heading": title, **diag, "changed": body != new_body})
        else:
            # Keep one blank line after footprint headings when missing.
            if is_footprint and (not body or body[0].strip() != ""):
                out.append("\n")
            out.extend(body)

        cursor = end

    if cursor < len(lines):
        out.extend(lines[cursor:])

    new_text = "".join(out)
    report = {
        "sections_changed": sum(1 for s in sections_meta if s.get("changed")),
        "sections": sections_meta,
    }
    return new_text, report


def iter_input_files(input_path: Path, pattern: str) -> list[Path]:
    if input_path.is_file():
        return [input_path]
    if not input_path.is_dir():
        raise FileNotFoundError(f"Input path not found: {input_path}")
    return sorted(input_path.rglob(pattern))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, help="Input markdown file or directory")
    ap.add_argument("--glob", default="*.md", help="Glob for directory input (default: *.md)")
    ap.add_argument("--output-dir", help="Write transformed files under this directory")
    ap.add_argument("--in-place", action="store_true", help="Overwrite input files")
    ap.add_argument("--report", help="Write JSON report")
    ap.add_argument("--dry-run", action="store_true", help="Do not write files")
    args = ap.parse_args()

    if args.in_place and args.output_dir:
        raise SystemExit("Use either --in-place or --output-dir, not both.")

    input_path = Path(args.input)
    files = iter_input_files(input_path, args.glob)
    if not files:
        raise SystemExit("No input files matched.")

    all_reports = []
    changed_count = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        new_text, report = transform_markdown(text)
        changed = new_text != text
        if changed:
            changed_count += 1

        all_reports.append(
            {
                "file": str(path),
                "changed": changed,
                **report,
            }
        )

        if args.dry_run:
            continue

        if args.in_place:
            if changed:
                path.write_text(new_text, encoding="utf-8")
        elif args.output_dir:
            out_root = Path(args.output_dir)
            out_root.mkdir(parents=True, exist_ok=True)
            out_file = out_root / path.name
            out_file.write_text(new_text, encoding="utf-8")

    summary = {
        "input": str(input_path),
        "files": len(files),
        "changed_files": changed_count,
        "results": all_reports,
    }

    if args.report:
        Path(args.report).write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(json.dumps({"files": len(files), "changed_files": changed_count}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
