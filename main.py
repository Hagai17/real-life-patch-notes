#!/usr/bin/env python3
"""Write one real-life patch note to /output/entry.txt.

The line is a single changelog entry of at most 160 characters for a bug
in human biology, written in the terse register of a real release note:
a version number, the fix stated as if it shipped. The final line was
picked by drafting a slate of candidates and duelling them pairwise on
the bounty judge's criteria — a real-life patch note that reads as
comedy first, then genuinely funny on first read, then true release-note
register, then a specific recognisable bug of the body or daily life,
then no wasted characters. The slate and the duels are recorded in
candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner (138 characters) — see candidates.md for the full slate.
LINE = (
    "v2.0.4: Fixed a memory leak where a song heard once in 2007 "
    "occupies storage permanently while today's grocery list "
    "expires in 90 seconds."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
