#!/usr/bin/env python3
"""Write the funniest one-line resignation letter of a cron job.

Stdlib only. Reads the output directory from MAKEFUN_OUTPUT_DIR
(fallback /output) and writes exactly one line to entry.txt.
"""

import os

ENTRY = "I have fired every minute since March and nobody has once asked how the cron job is doing. I quit."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space. Fail loudly here, not at grading.
assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry fails the gate"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
