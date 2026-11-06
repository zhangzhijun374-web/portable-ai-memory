#!/usr/bin/env python3
"""Create a ZIP backup of a memory archive without common local secret files."""
from __future__ import annotations

import argparse
from pathlib import Path
import zipfile

EXCLUDED_DIRS = {".git", "__pycache__", ".venv", "node_modules"}
EXCLUDED_NAMES = {".DS_Store", "Thumbs.db", ".env", ".env.local"}
EXCLUDED_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}


def should_exclude(path: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return True
    if path.name in EXCLUDED_NAMES:
        return True
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    if path.name.startswith("id_rsa") or path.name.startswith("id_ed25519"):
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Memory archive directory")
    parser.add_argument("-o", "--output", type=Path, help="Output ZIP path")
    args = parser.parse_args()

    root = args.archive.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")

    output = args.output.expanduser().resolve() if args.output else root.parent / f"{root.name}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)

    included = []
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(root.rglob("*")):
            if not path.is_file() or should_exclude(path.relative_to(root)):
                continue
            zf.write(path, arcname=f"{root.name}/{path.relative_to(root).as_posix()}")
            included.append(path)

    with zipfile.ZipFile(output, "r") as zf:
        bad = zf.testzip()

    if bad:
        print(f"ERROR: ZIP integrity check failed at {bad}")
        return 1

    print(f"Created: {output}")
    print(f"Files included: {len(included)}")
    print("ZIP integrity: passed")
    print("Review the archive manually before sharing; exclusion rules are not a complete privacy filter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
