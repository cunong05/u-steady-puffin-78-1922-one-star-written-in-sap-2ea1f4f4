#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes a single one-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.
"""

import os

REVIEW = (
    "One star. He bought me for 'good vibes,' watered me once, forgot "
    "me for a month, then blamed me for wilting. I'm a fern, not his "
    "therapist — and the succulent next door agrees."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
