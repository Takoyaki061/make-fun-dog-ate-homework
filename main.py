#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse (make.fun).

Writes one line - the dog's own excuse, in the dog's own voice - to
/output/entry.txt. The line was picked from 12 DeepSeek-brainstormed
candidates by critique against the judge's brief: dog's own voice,
biggest laugh with a twist of dog logic, sounds like a real dog,
stands alone, and fresh (no cat, no paper-taste, no "good boy").
"""

import os

TEXT = "You left it on the floor. I'm a dog. That's a legal contract and I signed it with my teeth."


def main():
    # Gate guard: the entry must be 1-200 chars of non-whitespace UTF-8 text.
    # Fail loudly here rather than shipping an invalid entry.
    if not TEXT.strip() or len(TEXT) > 200:
        raise SystemExit(f"entry invalid: {len(TEXT)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
