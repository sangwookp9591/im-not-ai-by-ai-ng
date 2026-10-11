#!/usr/bin/env python3
"""Measure a UTF-8 answer body; this does not validate meaning or naturalness."""
import argparse
import json
from pathlib import Path


def measure(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return {
        "codepoints": len(text),
        "nonwhitespace": sum(not char.isspace() for char in text),
        "utf16": len(text.encode("utf-16-le")) // 2,
        "utf8_bytes": len(text.encode("utf-8")),
        "line_breaks": text.count("\n"),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--count-mode", choices=("codepoints", "nonwhitespace", "utf16"), default="codepoints")
    parser.add_argument("--max-chars", type=int)
    args = parser.parse_args()
    if args.max_chars is not None and args.max_chars < 0:
        parser.error("--max-chars must be nonnegative")
    try:
        counts = measure(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as error:
        parser.exit(2, f"Cannot read UTF-8 input: {error}\n")
    count = counts[args.count_mode]
    exceeded = args.max_chars is not None and count > args.max_chars
    print(json.dumps({
        "counts": counts,
        "count_mode": args.count_mode,
        "selected_count": count,
        "limit": args.max_chars,
        "length_status": "over_limit" if exceeded else ("within_limit" if args.max_chars is not None else "not_checked"),
        "normalization": "CRLF/CR to LF; trailing newline counted; no Unicode normalization",
        "semantic_check": "not_performed",
    }, ensure_ascii=False, indent=2))
    return int(exceeded)


if __name__ == "__main__":
    raise SystemExit(main())
