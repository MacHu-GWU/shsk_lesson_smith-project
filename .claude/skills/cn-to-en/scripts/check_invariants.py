#!/usr/bin/env python3
"""Check structural invariants of an English rewrite against its Chinese Markdown source."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})\s*(\S*)")
HEADER_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
TABLE_ROW_RE = re.compile(r"^\s{0,3}\|")
TABLE_SEP_RE = re.compile(r"^\s{0,3}\|[\s:|\-]+\|?\s*$")
QUOTE_RE = re.compile(r"^\s{0,3}>")
CJK_RE = re.compile(r"[㐀-䶿一-鿿豈-﫿]")
DASH_RE = re.compile(r"[‒–—―−]|\s--\s|\w--\w")
FULLWIDTH_RE = re.compile(r"[　-〿！-･‘’“”…]")


def _scan(text: str) -> dict:
    """Extract the structural skeleton of a Markdown document.

    Returns headers, fenced code blocks, tables, quote blocks, and the
    line numbers of prose lines that sit outside fenced code.
    """
    headers: list[tuple[int, str]] = []
    fences: list[tuple[int, str, int]] = []
    tables: list[tuple[int, int, int]] = []
    quotes: list[int] = []
    prose: list[tuple[int, str]] = []
    code: list[tuple[int, str]] = []

    fence_marker: str | None = None
    fence_start = 0
    fence_info = ""
    fence_body = 0
    table_block: list[tuple[int, str]] = []
    in_quote = False

    def flush_table() -> None:
        if len(table_block) >= 2 and TABLE_SEP_RE.match(table_block[1][1]):
            head = table_block[0][1].strip().strip("|")
            cols = len([c for c in head.split("|")])
            tables.append((table_block[0][0], len(table_block), cols))
        table_block.clear()

    for lineno, line in enumerate(text.splitlines(), 1):
        marker = FENCE_RE.match(line)
        if fence_marker is None:
            if marker:
                flush_table()
                in_quote = False
                fence_marker = marker.group(1)
                fence_start = lineno
                fence_info = marker.group(2)
                fence_body = 0
                continue
        else:
            closes = (
                marker is not None
                and not marker.group(2)
                and marker.group(1)[0] == fence_marker[0]
                and len(marker.group(1)) >= len(fence_marker)
            )
            if closes:
                fences.append((fence_start, fence_info, fence_body))
                fence_marker = None
                continue
            fence_body += 1
            code.append((lineno, line))
            continue

        prose.append((lineno, line))

        header = HEADER_RE.match(line)
        if header:
            flush_table()
            in_quote = False
            headers.append((len(header.group(1)), header.group(2)))
            continue

        if TABLE_ROW_RE.match(line):
            table_block.append((lineno, line))
        else:
            flush_table()

        if QUOTE_RE.match(line):
            if not in_quote:
                quotes.append(lineno)
                in_quote = True
        elif line.strip():
            in_quote = False

    flush_table()
    if fence_marker is not None:
        fences.append((fence_start, fence_info, fence_body))

    return {
        "headers": headers,
        "fences": fences,
        "tables": tables,
        "quotes": quotes,
        "prose": prose,
        "code": code,
        "unclosed_fence": fence_marker is not None,
    }


def _compare_counts(name: str, src: int, dst: int, out: list[str]) -> bool:
    if src == dst:
        out.append(f"  PASS  {name}: {dst}")
        return True
    out.append(f"  FAIL  {name}: source has {src}, draft has {dst}")
    return False


def _main(draft: Path, source: Path | None = None, quiet: bool = False) -> int:
    """Report every structural invariant the draft breaks.

    Draft-only checks always run: no em dash, no CJK characters, no
    full width punctuation, no unclosed code fence. When ``source`` is
    given, the header level sequence, code fence count and info strings,
    table shapes, and quote block count are compared against it.

    Returns 0 when every check passes, 1 when any check fails.
    """
    if not draft.exists():
        print(f"ERROR: draft not found: {draft}", file=sys.stderr)
        return 1
    if source is not None and not source.exists():
        print(f"ERROR: source not found: {source}", file=sys.stderr)
        return 1

    d = _scan(draft.read_text(encoding="utf-8"))
    report: list[str] = [f"draft:  {draft}"]
    failures = 0
    warnings = 0

    if source is not None:
        s = _scan(source.read_text(encoding="utf-8"))
        report.insert(0, f"source: {source}")
        report.append("")
        report.append("[structure vs source]")

        s_levels = [lv for lv, _ in s["headers"]]
        d_levels = [lv for lv, _ in d["headers"]]
        if s_levels == d_levels:
            report.append(f"  PASS  header level sequence: {len(d_levels)} headers")
        else:
            failures += 1
            report.append(
                f"  FAIL  header level sequence differs "
                f"(source {len(s_levels)} headers, draft {len(d_levels)})"
            )
            for i in range(max(len(s_levels), len(d_levels))):
                sh = s["headers"][i] if i < len(s["headers"]) else None
                dh = d["headers"][i] if i < len(d["headers"]) else None
                mark = " " if sh and dh and sh[0] == dh[0] else "*"
                left = f"h{sh[0]} {sh[1]}" if sh else "(missing)"
                right = f"h{dh[0]} {dh[1]}" if dh else "(missing)"
                report.append(f"      {mark} [{i}] cn: {left}")
                report.append(f"      {mark}      en: {right}")

        if not _compare_counts("code fence count", len(s["fences"]), len(d["fences"]), report):
            failures += 1
        else:
            for i, (sf, df) in enumerate(zip(s["fences"], d["fences"])):
                if sf[1] != df[1]:
                    failures += 1
                    report.append(
                        f"  FAIL  code fence [{i}] info string: "
                        f"cn `{sf[1]}` (line {sf[0]}) vs en `{df[1]}` (line {df[0]})"
                    )
                elif sf[2] != df[2]:
                    warnings += 1
                    report.append(
                        f"  WARN  code fence [{i}] body length: "
                        f"cn {sf[2]} lines vs en {df[2]} lines (line {df[0]})"
                    )

        if not _compare_counts("table count", len(s["tables"]), len(d["tables"]), report):
            failures += 1
        else:
            for i, (st, dt) in enumerate(zip(s["tables"], d["tables"])):
                if st[1] != dt[1] or st[2] != dt[2]:
                    failures += 1
                    report.append(
                        f"  FAIL  table [{i}] shape: cn {st[1]}x{st[2]} "
                        f"vs en {dt[1]}x{dt[2]} (line {dt[0]})"
                    )

        if not _compare_counts("quote block count", len(s["quotes"]), len(d["quotes"]), report):
            failures += 1

    report.append("")
    report.append("[draft only]")

    if d["unclosed_fence"]:
        failures += 1
        report.append("  FAIL  unclosed code fence at end of draft")
    else:
        report.append("  PASS  all code fences closed")

    for label, pattern, lines, fatal in (
        ("em dash or double hyphen", DASH_RE, d["prose"], True),
        ("CJK character in prose", CJK_RE, d["prose"], True),
        ("full width punctuation", FULLWIDTH_RE, d["prose"], True),
        ("CJK character in code block", CJK_RE, d["code"], False),
    ):
        hits = [(n, ln) for n, ln in lines if pattern.search(ln)]
        if not hits:
            report.append(f"  PASS  no {label}")
            continue
        if fatal:
            failures += 1
            tag = "FAIL"
        else:
            warnings += 1
            tag = "WARN"
        report.append(f"  {tag}  {len(hits)} line(s) with {label}:")
        for n, ln in hits[:20]:
            report.append(f"      line {n}: {ln.strip()[:110]}")
        if len(hits) > 20:
            report.append(f"      ... and {len(hits) - 20} more")

    report.append("")
    report.append(f"RESULT: {failures} failure(s), {warnings} warning(s)")

    if not quiet or failures:
        print("\n".join(report))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="check_invariants",
        description="Check structural invariants of an English Markdown rewrite.",
    )
    parser.add_argument("--draft", type=Path, required=True, help="path to the English draft")
    parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help="path to the Chinese source; omit to run draft only checks",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="print the report only when a check fails",
    )
    args = parser.parse_args(argv)
    return _main(draft=args.draft, source=args.source, quiet=args.quiet)


if __name__ == "__main__":
    sys.exit(main())
