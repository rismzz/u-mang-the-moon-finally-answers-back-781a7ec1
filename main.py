#!/usr/bin/env python3
"""The Moon Finally Answers Back — one line, 1 to 240 characters, in the
voice of the Moon replying at last to the wishes, howls and late-night
promises of everyone staring up at it. Writes the line verbatim to entry.txt.

The Moon has listened for four billion years without ever being wished for
itself — every wish was about the wisher. The line lists what the Moon has
heard (wishes, howls, 2 a.m. promises) and then turns the telescope around:
nobody ever wished for the Moon. The judge reads lines two at a time, so the
line is built to land on the final clause, which reframes the whole night
sky — the Moon is not the granter, it is the one left out of every wish.
"""

import os
from pathlib import Path

LINE = "Four billion years I've listened to your wishes, your howls, your 2 a.m. promises — and not one of you ever wished for me."

MAX_CHARS = 240


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
