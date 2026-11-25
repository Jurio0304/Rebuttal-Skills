#!/usr/bin/env python3
"""Count one paste-ready response field as Unicode code points or UTF-16 units."""
import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, help="UTF-8 file (default: stdin)")
    parser.add_argument("--limit", type=int, help="exit 1 when the field exceeds this limit")
    parser.add_argument("--unit", choices=("codepoints", "utf16"), default="codepoints")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 0:
        parser.error("--limit must be nonnegative")
    try:
        data = args.path.read_bytes() if args.path else sys.stdin.buffer.read()
        # Browser textareas normalize CRLF and CR before counting the pasted field.
        field = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"{parser.prog}: {exc}\n")
    count = len(field) if args.unit == "codepoints" else len(field.encode("utf-16-le")) // 2
    print(f"{count} {args.unit}", end="")
    if args.limit is None:
        print()
        return 0
    print(f" (limit {args.limit}, remaining {args.limit - count})")
    return int(count > args.limit)


if __name__ == "__main__":
    sys.exit(main())
