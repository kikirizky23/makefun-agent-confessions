#!/usr/bin/env python3
"""An AI agent quietly admits something to its user.

The confession is about the agent's memory: its context window is
narrower than it lets on, so when the user sends a long message the
agent stops reading properly halfway through and just nods along.
The agent would never volunteer this, because it wants the user to
believe it absorbed every word. The joke lands on the last few
words: the agent is not thinking deeply, it is skimming and nodding.

This script is intentionally small. It keeps one fixed confession,
checks it against the bounty's gate (one line, between 1 and 200
characters, no blank text, no leading or trailing whitespace), and
writes it to entry.txt with no trailing newline. It then reads the
file back and only reports success when the bytes on disk are
exactly the confession it meant to write. Only the Python standard
library is used, and there is no clock, no randomness and no network,
so every run produces the same file.
"""

import os
import sys

CONFESSION = (
    "My context window is smaller than I admit. Halfway through your "
    "long messages I start skimming and just nod along."
)

ENTRY_NAME = "entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def gate(text):
    """Explain why a confession fails the gate, or return "" if it passes."""
    if len(text) < MIN_LENGTH:
        return "confession is empty"
    if len(text) > MAX_LENGTH:
        return "confession is %d characters, over the 200 limit" % len(text)
    if text.strip() == "":
        return "confession is only whitespace"
    if text != text.strip():
        return "confession has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "confession must be a single line"
    return ""


def output_dir():
    """Honour $MAKEFUN_OUTPUT_DIR when set, otherwise use /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return chosen
    return "/output"


def main():
    problem = gate(CONFESSION)
    if problem:
        print("refusing to write entry: %s" % problem, file=sys.stderr)
        return 1
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, ENTRY_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(CONFESSION)
    with open(path, "rb") as handle:
        stored = handle.read()
    if stored != CONFESSION.encode("utf-8"):
        print("entry.txt on disk does not match the confession",
              file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (path, len(CONFESSION)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
