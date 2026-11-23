#!/usr/bin/env python3
"""The office joke: one line about office life.

The joke: blocking the calendar as focus time is the office worker's
defence against meetings, and the manager defeats it with the office's
own weapon -- a meeting whose title repeats the defence back at them.
The turn lands at the end ("quick sync about your focus time"): the
meeting is about the very thing meant to prevent meetings, so the
laugh comes with a wince every calendar-blocked worker recognises.
One line, concrete, no explanation, no Monday-morning or photocopier
angle.
"""
import os

JOKE = "I blocked my calendar as focus time, so my manager booked a meeting called 'quick sync about your focus time'."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Gate: 1-199 Unicode code points, not only whitespace, one line.
    assert 1 <= len(JOKE) <= 199, f"joke length {len(JOKE)} out of range"
    assert JOKE.strip(), "joke is only whitespace"
    assert JOKE == JOKE.strip(), "joke has leading or trailing whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    print(f"wrote {path}: {len(JOKE)} chars")

if __name__ == "__main__":
    main()
