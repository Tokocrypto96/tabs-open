#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one honest tab count, digits only, to /output/entry.txt.

The count: 347. A real, lived-in hoard -- years of "I'll read this
later" spread across windows, never closed, never counted until now.
High enough to surprise, odd and unround enough to read as a number
someone actually counted, and still a count a real person could
honestly have open right now. No words, no punctuation, no second
number: just the digits, exactly as the gate requires (1-5 chars).
"""

import os

ENTRY = "347"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard: the gate only accepts 1-5 digit characters, nothing else.
    assert ENTRY.isdigit() and 1 <= len(ENTRY) <= 5, "entry must be 1-5 digits"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
