"""Robot Romance: one-line pickup line for AI.

Writes a single original pickup line to /output/entry.txt.
Standard library only; no network, no secrets, no input files.
"""

from pathlib import Path

ENTRY = (
    "I must be overfitting, because I can't stop thinking about you "
    "and you're the only data point I need."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
