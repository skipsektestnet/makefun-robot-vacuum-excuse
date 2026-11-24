"""The Robot Vacuum's Best Excuse: writes the entry text to /output/entry.txt.

Why this line: Rooted in the vacuum's own world (sensors, classification); the excuse reframes missing the spot as politeness.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'I did not miss that spot: my sensors found a sock, classified it as a pet, and I have been respecting its privacy ever since.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
