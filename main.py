"""Entry for make.fun's "Unsent: The Micro-Confession Sprint".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

TO_LINE = "To: my brother"
CONFESSION = "I sold the boat Dad left us. I told everyone it was falling apart. It wasn't. "
REASON = "I just couldn't afford the slip fees, and I couldn't afford you knowing that either."

ENTRY = TO_LINE + "\n" + CONFESSION + REASON

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
