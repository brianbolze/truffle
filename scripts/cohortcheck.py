#!/usr/bin/env python3
"""cohortcheck — lint an opt-in cohort pack (store/<domain>/<cohort>.md) against its contract.

A *cohort pack* (contract: `modules/cohort-packs/<COHORT>.md`, e.g. modules/cohort-packs/TELEHEALTH.md; species note: SCHEMA → Tier-1 modules) is the
vertical-specific classification layer the universal `profile.md` can't carry — its load-bearing invariant is
that every cut is a declared closed-set value, so the cohort stays queryable. This is **one generic linter for
every cohort pack**, not one script per cohort: it reads the cohort's own machine-readable closed-set block out
of the contract file and validates each instance against it. The next cohort ships a contract, not a script.

It asserts:
  1. closed-set conformance — every non-empty cut is one of that field's declared values.
  2. single-select          — each cut is a scalar, never a list (a parallel nuance goes in a body note).
  3. doc-meta present        — the frontmatter fence + schema_version / domain / captured_at.
  4. empty over guessed      — an undetermined field may be empty/absent; only a value OFF the list fails.
  5. no stray keys           — a frontmatter key that's neither doc-meta nor a declared cut (a typo, or a
                               universal profile.md field leaking in) trips the lint.

Stdlib + PyYAML (matches store.py). Exit 0 = the pack conforms; nonzero prints how it broke.

CLI:  python scripts/cohortcheck.py --cohort telehealth [--slug <slug>]
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from typing import Any

from storelint import leaked_tags  # shared, schema-independent guard (also called by offeringscheck)

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not importable — cohortcheck needs it to parse the contract + frontmatter.")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")

_FENCE_RE = re.compile(r"```ya?ml\n(.*?)```", re.S)


def load_contract(cohort: str) -> dict[str, Any]:
    """The cohort's machine-readable spec, sliced from `modules/cohort-packs/<COHORT>.md` — `{cohort, doc_meta, fields:{name:[...]}}`.

    Scans the contract's fenced yaml blocks and returns the first that declares both `cohort` and `fields` (so
    the human file-shape *template* block, which has neither, is skipped). This indirection is the whole point:
    the contract owns its closed sets, so one linter serves every cohort.
    """
    path = os.path.join(ROOT, "modules", "cohort-packs", f"{cohort.upper()}.md")
    if not os.path.isfile(path):
        sys.exit(f"cohortcheck: no contract modules/cohort-packs/{cohort.upper()}.md — is '{cohort}' a real cohort?")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for block in _FENCE_RE.findall(text):
        try:
            spec = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if isinstance(spec, dict) and "cohort" in spec and "fields" in spec:
            return spec
    sys.exit(f"cohortcheck: {cohort.upper()}.md has no machine-readable block (a ```yaml block with `cohort` + `fields`).")


def frontmatter(path: str) -> dict[str, Any] | None:
    """Top-level frontmatter dict, or None if the file has no leading '---' fence."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    return yaml.safe_load(parts[1]) if len(parts) >= 3 else None


def check(slug: str, cohort: str, spec: dict[str, Any]) -> list[str]:
    """Lint one company's `<cohort>.md` against the contract spec. Returns failure strings ([] = clean)."""
    path = os.path.join(STORE, slug, f"{cohort}.md")
    if not os.path.isfile(path):
        return [f"{slug}: no {cohort}.md (pack not active here)"]

    fails: list[str] = []
    # --- leaked harness tags: schema-independent, so shared with offeringscheck via storelint ---
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for ln, tag in leaked_tags(text):
        fails.append(f"{slug}: leaked harness tag {tag!r} on line {ln} — strip it (generation artifact, not content).")

    fm = frontmatter(path)
    if fm is None:
        fails.append(f"{slug}: no leading '---' frontmatter fence.")
        return fails

    doc_meta = spec.get("doc_meta") or ["schema_version", "domain", "captured_at"]
    fields = spec["fields"]

    for required in doc_meta:
        if required not in fm:
            fails.append(f"{slug}: frontmatter missing doc-meta '{required}'.")

    allowed = set(doc_meta) | set(fields)
    for key, val in fm.items():
        if key not in allowed:
            fails.append(
                f"{slug}: stray frontmatter key '{key}' — not doc-meta, not a declared cut (typo? a profile.md field leaking in?)."
            )
        elif key in fields:
            if isinstance(val, (list, dict)):
                fails.append(f"{slug}: cut '{key}' is multi-valued ({val!r}) — cohort cuts are single-select.")
            elif val is not None and str(val).strip() and str(val).strip() not in fields[key]:
                fails.append(f"{slug}: cut '{key}' = {val!r} is not in the closed set {fields[key]}.")
    return fails


def main() -> None:
    ap = argparse.ArgumentParser(description="lint a cohort pack against its modules/<COHORT>.md contract")
    ap.add_argument("--cohort", required=True, help="cohort name, e.g. telehealth (resolves to modules/cohort-packs/TELEHEALTH.md)")
    ap.add_argument("--slug", help="lint one company (default: every store/*/<cohort>.md)")
    args = ap.parse_args()

    cohort = args.cohort.lower()
    spec = load_contract(cohort)

    if args.slug:
        slugs = [args.slug]
    else:
        slugs = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(STORE, "*", f"{cohort}.md")))
        if not slugs:
            print(f"cohortcheck: no store/*/{cohort}.md found ('{cohort}' pack not active anywhere yet).")
            return

    all_fails: list[str] = []
    for slug in slugs:
        fails = check(slug, cohort, spec)
        all_fails += fails
        print(f"cohortcheck {slug} [{cohort}]: {'OK' if not fails else str(len(fails)) + ' issue(s)'}")
        for f in fails:
            print("  FAIL:", f)
    if all_fails:
        sys.exit(f"\n{len(all_fails)} failure(s) across {len(slugs)} file(s).")
    print(f"\nOK — {len(slugs)} {cohort}.md file(s) conform to the cohort-pack contract.")


if __name__ == "__main__":
    main()
