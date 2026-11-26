"""Funniest Sign on a Haunted Server Room Door — make.fun entry.

Writes one sign for the door of a haunted server room to entry.txt in
the output directory named by MAKEFUN_OUTPUT_DIR (default /output).
Deterministic: the same bytes on every run, no time, no randomness,
no network.
"""

import os

ENTRY = (
    "Do not enter. The servers whisper your passwords, "
    "the lights flicker in binary, and IT never came back."
)
# Exactly 103 characters, one line. The joke in three beats: a classic
# "Do not enter" sign, then the haunting turns specific to a server
# room (servers whispering passwords, lights flickering in binary),
# and the punch lands on the last four words — IT never came back,
# so whoever went in to fix it is part of the haunting now.

# Gate: /output/entry.txt must be UTF-8 text of 1 to MAX_CHARS characters.
MAX_CHARS = 120
assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} characters"
assert ENTRY.strip() == ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
