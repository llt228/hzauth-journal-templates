#!/usr/bin/env python3
"""Verify that every included journal directory is complete and has a PDF.

Checks:
  * required files exist;
  * main.pdf is a non-trivial PDF;
  * official class files are byte-identical to the copies in assets/;
  * main.tex references the journal title and a document class.

Exit code is non-zero if any journal fails a check.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "main.tex",
    "main.pdf",
    "references.bib",
    ".latexmkrc",
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "meta.json",
    "figures/example-figure.pdf",
]


def main() -> int:
    data = json.loads((ROOT / "catalog" / "journals.json").read_text(encoding="utf-8"))
    included = [j for j in data["journals"] if j["status"] == "included"]
    errors: list[str] = []

    for journal in included:
        slug = journal["slug"]
        directory = ROOT / "journals" / slug
        if not directory.is_dir():
            errors.append(f"{slug}: missing directory")
            continue
        for name in REQUIRED:
            if not (directory / name).exists():
                errors.append(f"{slug}: missing {name}")
        pdf = directory / "main.pdf"
        if pdf.exists() and pdf.stat().st_size < 20_000:
            errors.append(f"{slug}: main.pdf is suspiciously small ({pdf.stat().st_size} bytes)")
        classes = list(directory.glob("*.cls"))
        styles = list(directory.glob("*.bst"))
        if not classes:
            errors.append(f"{slug}: no .cls file")
        if not styles:
            errors.append(f"{slug}: no .bst file")
        tex = (directory / "main.tex").read_text(encoding="utf-8")
        if "\\documentclass" not in tex:
            errors.append(f"{slug}: main.tex has no \\documentclass")
        plain = tex.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_")
        if journal["title"] not in plain:
            errors.append(f"{slug}: main.tex does not mention the journal title")

        # Official files must match the vendored originals.
        template = journal["template"]
        asset_dir = ROOT / "assets" / template
        for asset in asset_dir.iterdir():
            target = directory / asset.name
            if asset.is_file() and target.exists():
                if asset.read_bytes() != target.read_bytes():
                    errors.append(f"{slug}: {asset.name} differs from assets/{template}/{asset.name}")

    if errors:
        print(f"{len(errors)} problem(s) found:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"verified {len(included)} journal template(s): all required files present, PDFs built, class files unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
