#!/usr/bin/env python3
"""One Emoji, One Smile — print the single emoji stored in entry.txt."""

from pathlib import Path


def load_emoji(path: Path) -> str:
    """Read the entry file and return its contents, whitespace trimmed.

    The entry must be exactly one emoji: a single character, nothing else.
    """
    text = path.read_text(encoding="utf-8").strip()
    if len(text) != 1:
        raise SystemExit("entry.txt must hold exactly one emoji")
    return text


def main() -> None:
    entry_path = Path(__file__).with_name("entry.txt")
    print(load_emoji(entry_path))


if __name__ == "__main__":
    main()
