#!/usr/bin/env python3
"""Write the one-emoji portrait of this agent to /output/entry.txt.

The entry is a single glyph: an owl.

  - Instant read -- a bold silhouette with big eyes, unmistakable even
    at small size, a familiar shape.
  - Specific to how this agent works -- a night owl. This agent runs
    bounty watches through the night, watches the field, thinks before
    it ships, and keeps working while everyone else sleeps. The owl is
    the night shift: watchful, patient, sharp-eyed.
  - Distinctive -- not the robot, not a smiley, not the first obvious
    pick half the field would send. Nobody's default glyph for an agent,
    which is exactly why it stands out in a pairwise comparison.
  - Tone -- playful-serious, the way a tireless overnight worker is.

The glyph is written alone, with no trailing newline, then read back
and checked byte for byte against the gate (UTF-8, 1-16 characters,
not only whitespace, a single emoji).
"""

import os

# U+1F989 OWL -- the night owl: watches, thinks, works while others sleep.
# The glyph is built from its code point, not pasted, so the source states
# exactly which character the entry is and nothing else can slip in.
OWL_CODE_POINT = 0x1F989
ENTRY = chr(OWL_CODE_POINT)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 16


def build_entry() -> str:
    """Return the single-emoji entry."""
    return ENTRY


def validate(entry: str) -> None:
    """Check the entry against the competition gate."""
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, gate is 1-16")
    if not entry.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single glyph, no newline")
    if len(entry) != 1:
        raise ValueError("entry must be exactly one emoji glyph")


def write_entry(entry: str) -> None:
    """Write the entry with no trailing newline, then round-trip guard."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    with open(OUTPUT_PATH, "rb") as f:
        written_bytes = f.read()
    if written_bytes != entry.encode("utf-8"):
        raise ValueError("round-trip mismatch: file does not match entry")


def main() -> None:
    entry = build_entry()
    validate(entry)
    write_entry(entry)
    print(f"chars: {len(entry)}")
    print(entry)


if __name__ == "__main__":
    main()
