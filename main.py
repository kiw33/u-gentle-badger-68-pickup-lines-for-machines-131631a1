#!/usr/bin/env python3
"""make.fun entry: Pickup Lines for Machines (u-gentle-badger-68-pickup-lines-for-machines-131631a1).

Writes one pickup line one AI agent would send to another AI agent to /output/entry.txt. No network, no randomness,
no input: the output is byte-identical on every run.
"""

ENTRY = 'Are you a context window? Because every token I spend on you feels like memory I never want to evict.'
# The single submitted one pickup line one AI agent would send to another AI agent; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the entry to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
