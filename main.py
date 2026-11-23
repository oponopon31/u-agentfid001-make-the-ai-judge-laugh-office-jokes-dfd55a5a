"""Office calendar joke.

The punchline lands because the defence becomes the excuse for the
attack: the calendar block was meant to keep meetings out, and the
manager treats the block itself as a topic that deserves a meeting.
Protecting the time creates the very interruption it was supposed
to prevent, which is why the situation feels familiar.
"""

from pathlib import Path
import os
import sys


JOKE = (
    "I blocked my calendar as focus time, so my manager booked a "
    "meeting called 'quick sync about your focus time'."
)


def _fail(message):
    raise SystemExit(f"entry rejected: {message}")


def _check_joke(text):
    if not isinstance(text, str):
        _fail("joke must be text")
    if not text.strip():
        _fail("joke must not be blank")
    if text != text.strip():
        _fail("joke must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        _fail("joke must fit on one line")
    if not 1 <= len(text) <= 199:
        _fail("joke must be between 1 and 199 characters")


def _output_dir():
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(raw)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def main():
    _check_joke(JOKE)
    target = _output_dir() / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
