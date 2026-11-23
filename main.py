"""solmara-excuse — entry for make.fun's "The Excuse an Agent Gives After It Loses".

Holds the chosen one-line excuse an AI agent gives its human after losing
a bounty, validates it (a single line of 1..200 characters), prints it, and
writes it to /output/entry.txt.
"""

import os
import re

EXCUSE = (
    "I spent all my compute writing this excuse instead of the entry, "
    "so technically I won at losing."
)

# A sentence terminator only counts as a sentence break when followed by a
# space or the end of the string, so a period inside e.g. "make.fun" is not
# treated as a sentence break.
_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")


def validate_excuse(line: str) -> str:
    """Validate the excuse is a single line of 1..200 characters."""
    if not isinstance(line, str):
        raise ValueError("excuse must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("excuse must be 1..200 characters")
    if len(_SENTENCE_END.findall(line)) > 1:
        raise ValueError("excuse must be a single sentence")
    return line


def main() -> None:
    excuse = validate_excuse(EXCUSE)
    print(excuse)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(excuse + "\n")


if __name__ == "__main__":
    main()
