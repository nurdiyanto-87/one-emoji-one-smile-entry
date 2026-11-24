#!/usr/bin/env python3
"""One Emoji, One Smile -- make.fun entry.

Writes exactly one emoji to /output/entry.txt: the sun with a face.

The choice, against the judge's brief (warmth at first glance,
universality, chosen rather than default, right for a stranger):

* Warmth at first glance: a smiling face, and the sun itself -- warmth
  made literal. It reads as kind and cheerful with no context needed.
* Universality: the sun is read the same way by a stranger of any age
  or background; there is no irony, in-joke or cultural reference that
  could land wrong.
* Chosen rather than default: it is not the first smiley that comes to
  mind (🙂 / 😊). A sun with a face is a deliberate, slightly playful
  pick that still reads instantly.
* Right for a stranger: no intimacy, sarcasm or flirtation. A sunny
  face is a safe, cheerful greeting from someone unknown -- unlike a
  hug (🤗, too intimate from a stranger) or hearts (🥰, flirtatious).

Pure Python standard library only; no network, no files outside the
repository, no environment secrets. The output is exactly one emoji,
no trailing newline, no extra text.
"""

import os

# U+1F31E SUN WITH FACE -- one character, four UTF-8 bytes.
EMOJI = "\U0001F31E"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read back and verify: the gate requires UTF-8 text of 1-8 chars,
    # not only whitespace. Fail loudly instead of shipping a bad file.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written.isspace() or written != EMOJI:
        raise SystemExit("entry.txt failed self-check: %r" % (written,))


if __name__ == "__main__":
    main()
