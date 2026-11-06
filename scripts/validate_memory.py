#!/usr/bin/env python3
"""Basic local checks for a Portable AI Memory archive.

This is a heuristic helper, not a privacy certification tool.
It makes no network requests and does not modify the archive.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SECRET_PATTERNS = {
    "OpenAI-like key": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    "GitHub token": re.compile(r"\b(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{15,}\b"),
    "AWS access key ID": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Private key header": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}

REQUIRED_HINTS = ("README.md", "CHANGELOG.md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Path to a memory archive directory")
    parser.add_argument("--no-secret-scan", action="store_true", help="Skip heuristic secret scanning")
    args = parser.parse_args()

    root = args.archive.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}")
        return 2

    md_files = sorted(root.rglob("*.md"))
    if not md_files:
        print("ERROR: no Markdown files found")
        return 2

    print(f"Archive: {root}")
    print(f"Markdown files: {len(md_files)}")
    errors = []
    warnings = []

    for hint in REQUIRED_HINTS:
        if not (root / hint).exists():
            warnings.append(f"Missing recommended file: {hint}")

    for path in md_files:
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Not UTF-8 text: {path.relative_to(root)}")
            continue
        if not content.strip():
            warnings.append(f"Empty Markdown file: {path.relative_to(root)}")

        if not args.no_secret_scan:
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(content):
                    errors.append(
                        f"Possible {label} in {path.relative_to(root)} "
                        "(value intentionally not displayed)"
                    )

    manifest = root / "manifest.json"
    if manifest.exists():
        import json
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            listed = data.get("files", [])
            for item in listed:
                rel = item.get("path")
                if rel and not (root / rel).exists():
                    warnings.append(f"Manifest path does not exist: {rel}")
        except Exception as exc:
            errors.append(f"Invalid manifest.json: {type(exc).__name__}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"PASSED with {len(warnings)} warning(s).")
    print("Reminder: automated checks cannot identify every sensitive or inaccurate item.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
