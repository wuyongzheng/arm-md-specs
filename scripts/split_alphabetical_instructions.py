#!/usr/bin/env python3
"""Split a monolithic alphabetical instruction list into per-instruction files.

Example:
    python scripts/split_alphabetical_instructions.py arm/arm-C6.2.md

Reads a file whose first line is `## C<x>.<y> <title>` and which contains one
`## C<x>.<y>.<n> <mnemonic>` heading per instruction. Writes each instruction
to a sibling subdirectory `<dir>/C<x>.<y>/arm-C<x>.<y>.<n>.md` and overwrites
the input file with an index that links to every per-instruction file.

Refuses to run if no per-instruction headings are found, so re-invoking on an
already-split file is safe.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SECTION_RE = re.compile(r"^## (?P<sid>[A-Z]\d+(?:\.\d+)+)(?:\s+(?P<title>.+))?\s*$")


def split_file(input_path: Path) -> int:
    text = input_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        print(f"error: empty file: {input_path}", file=sys.stderr)
        return 2

    m = SECTION_RE.match(lines[0])
    if not m:
        print(
            f"error: first line is not a section heading: {lines[0]!r}",
            file=sys.stderr,
        )
        return 2

    section_id = m.group("sid")
    instr_re = re.compile(
        rf"^## (?P<iid>{re.escape(section_id)}\.\d+)\s+(?P<name>.+?)\s*$"
    )

    starts: list[tuple[int, str, str]] = []
    for i, line in enumerate(lines):
        im = instr_re.match(line)
        if im:
            starts.append((i, im.group("iid"), im.group("name").strip()))

    if not starts:
        print(
            f"error: no '## {section_id}.<n> ...' headings in {input_path}; "
            "refusing to run (already split?)",
            file=sys.stderr,
        )
        return 2

    out_dir = input_path.parent / section_id
    out_dir.mkdir(parents=True, exist_ok=True)

    for idx, (line_no, iid, _name) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        body = lines[line_no:end]
        while body and body[-1].strip() == "":
            body.pop()
        body.append("")
        out_path = out_dir / f"arm-{iid}.md"
        out_path.write_text("\n".join(body), encoding="utf-8")

    intro = lines[1 : starts[0][0]]
    while intro and intro[0].strip() == "":
        intro.pop(0)
    while intro and intro[-1].strip() == "":
        intro.pop()

    out_lines: list[str] = [lines[0]]
    if intro:
        out_lines.append("")
        out_lines.extend(intro)
    out_lines.append("")
    for _, iid, name in starts:
        out_lines.append(f"* [{iid} {name}]({section_id}/arm-{iid}.md)")
    out_lines.append("")
    input_path.write_text("\n".join(out_lines), encoding="utf-8")

    print(
        f"{section_id}: wrote {len(starts)} files to {out_dir}/, "
        f"rewrote index {input_path}"
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Split a monolithic instruction list into per-instruction files."
    )
    ap.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="Monolithic .md files to split (e.g. arm/arm-C6.2.md arm/arm-C7.2.md)",
    )
    args = ap.parse_args()

    rc = 0
    for path in args.inputs:
        if not path.is_file():
            print(f"error: not a file: {path}", file=sys.stderr)
            rc = 2
            continue
        rc = split_file(path) or rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
