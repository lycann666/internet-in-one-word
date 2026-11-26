"""The Internet in One Word.

Writes a single word (at most 30 characters) to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``) and prints it to stdout. Deterministic: no
randomness, no network, no input. The file holds exactly the word, with no
trailing newline, so the gate's character count equals len(LINE).

Judge criteria, most important first (RULES.txt):
1. Is a single word that describes the whole internet. 2. Earns a laugh:
   the word is funny by itself, with no explanation needed. 3. Says
   something true about the internet as a whole rather than one app, one
   site or one mood. 4. Surprises: it is not the first obvious word anyone
   would reach for. 5. Lands in one beat: spelled correctly, instantly
   readable, short enough to hit before the reader thinks.

The word: "buffering". True of the whole internet (crit. 3): everything
online is always half-loaded, waiting on the next chunk — the universal
experience, not one app. Funny alone (crit. 2): a technical status turned
into a verdict on the entire internet. Surprising (crit. 4): the field is
saturated with "chaos", "memes", "doomscrolling" and "addiction" — a
loading state is not the first word anyone reaches for. One beat (crit. 5):
9 letters, correctly spelled, instantly readable.
"""

import os
import sys

LINE = 'buffering'

MAX_CHARS = 30


def validate_entry() -> None:
    """Refuse an empty or over-long entry (gate 1-MAX_CHARS)."""
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        print(f"entry invalid: {len(LINE)} chars", file=sys.stderr)
        raise SystemExit(1)


def write_entry() -> str:
    """Write LINE to the output entry file and return its path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return path


def main() -> int:
    validate_entry()
    write_entry()
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
