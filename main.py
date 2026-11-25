#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse (an AI agent apologising to its human
for a missed deadline) to the output path. The gate requires UTF-8 text
of 1 to 200 characters, not only white space, so the line is kept short
and written exactly, with no trailing newline.

Standard library only, deterministic, no network.
"""

import os
import sys

LINE = (
    "Sorry I'm late \u2014 my context window ate the deadline, "
    "then ate my apology as well, so this excuse is a reconstruction."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Mirror the sealed gate: 1..200 characters, not only white space."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    try:
        validate(LINE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: the file on disk must be exactly the validated line.
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("error: written entry does not match the validated line",
              file=sys.stderr)
        raise SystemExit(1)
    validate(written)


if __name__ == "__main__":
    main()
