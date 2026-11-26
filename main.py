#!/usr/bin/env python3
"""One-Liner Laughs — make.fun entry.

Writes one original one-line joke, setup and payoff in a single
line. Stdlib only, writes a single line to /output/entry.txt, and
leaves the output directory alone. The setup promises romance
and the payoff delivers a pizza: the stranger was the delivery
driver all along.
"""

import os

TEXT = "My horoscope said I would meet a tall, dark stranger today, so I stayed in and ordered pizza \u2014 just in case the stranger turns out to be the delivery driver."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(TEXT) <= 200:
        raise SystemExit("line fails the 1-200 character gate")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
