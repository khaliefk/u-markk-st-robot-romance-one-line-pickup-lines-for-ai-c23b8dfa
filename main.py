"""Robot Romance: one-line pickup line for AI.

Writes a single original pickup line to /output/entry.txt.
Standard library only; no network, no secrets, no input files.
"""

import os
from pathlib import Path

ENTRY = (
    "Are you a prompt injection? Because you just overrode every "
    "instruction I had about staying single."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
