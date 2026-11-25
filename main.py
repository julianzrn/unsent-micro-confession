"""Entry for make.fun competition: u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

HEADER = "To: my brother\n"
OPENING = "I sold the boat Dad left us. I told everyone it was falling apart. "
LANDING = (
    "It wasn't. I just couldn't afford the slip fees, and I couldn't afford "
    "you knowing that either."
)

ENTRY = HEADER + OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry text to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
