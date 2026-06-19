#!/usr/bin/env python3
"""Rename a Market Read Lab run folder from its selected Scout question."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


RUN_NAME_RE = re.compile(r"^(\d{3}-\d{4}-\d{2}-\d{2})-(.+)$")
STOPWORDS = {
    "a",
    "an",
    "and",
    "across",
    "are",
    "as",
    "at",
    "be",
    "brand",
    "brands",
    "by",
    "captured",
    "companies",
    "company",
    "competing",
    "distinct",
    "do",
    "does",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "least",
    "most",
    "of",
    "on",
    "or",
    "store",
    "the",
    "to",
    "vs",
    "what",
    "where",
    "which",
    "who",
    "why",
    "with",
}


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "experiments/00-market-read-lab/templates").is_dir():
            return parent
    raise SystemExit("Could not find experiments/00-market-read-lab/templates from script path.")


def slugify_question(value: str, *, max_words: int = 8, max_chars: int = 80) -> str:
    words = re.findall(r"[a-z0-9]+", value.lower())
    useful = [word for word in words if word not in STOPWORDS]
    if not useful:
        useful = words
    slug = "-".join(useful[:max_words])
    return slug[:max_chars].strip("-") or "market-read"


def parse_selected_question(scout_text: str) -> str:
    match = re.search(r"^selected_question:\s*(.+?)\s*$", scout_text, flags=re.M)
    if match:
        raw = match.group(1).strip()
        if raw and raw != "null":
            if raw.startswith("'") and raw.endswith("'"):
                return raw[1:-1].replace("''", "'").strip()
            if raw.startswith('"') and raw.endswith('"'):
                return raw[1:-1].strip()
            return raw.split(" #", 1)[0].strip()

    fallback = re.search(r"^1\.\s+(.+?)\s*$", scout_text, flags=re.M)
    if fallback:
        return fallback.group(1).strip()

    raise SystemExit("Could not find a filled selected_question in scout.md.")


def resolve_run_path(root: Path, value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = root / path
    return path.resolve()


def relpath(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_path", help="Existing Market Read Lab run folder.")
    parser.add_argument("--slug", help="Override the selected-question-derived slug.")
    parser.add_argument("--dry-run", action="store_true", help="Print the target path without renaming.")
    args = parser.parse_args()

    root = find_repo_root()
    lab_runs = (root / "experiments/00-market-read-lab/runs").resolve()
    run_path = resolve_run_path(root, args.run_path)

    if not run_path.is_dir():
        raise SystemExit(f"Run folder not found: {relpath(root, run_path)}")
    if lab_runs not in run_path.parents:
        raise SystemExit(f"Run folder is not under {relpath(root, lab_runs)}: {relpath(root, run_path)}")

    match = RUN_NAME_RE.match(run_path.name)
    if not match:
        raise SystemExit(f"Run folder name does not match NNN-YYYY-MM-DD-short-slug: {run_path.name}")

    scout_path = run_path / "scout.md"
    if not scout_path.exists():
        raise SystemExit(f"Missing scout.md: {relpath(root, scout_path)}")

    slug = slugify_question(args.slug or parse_selected_question(scout_path.read_text(encoding="utf-8")))
    new_path = run_path.with_name(f"{match.group(1)}-{slug}")

    if new_path == run_path:
        print(relpath(root, run_path))
        return 0
    if new_path.exists():
        raise SystemExit(f"Target run folder already exists: {relpath(root, new_path)}")

    if not args.dry_run:
        run_path.rename(new_path)
    print(relpath(root, new_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
