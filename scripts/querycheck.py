#!/usr/bin/env python3
"""querycheck — assert QUERYING.md's structural assumptions still hold against the live store.

QUERYING.md names *fields and mechanics* (never value lists), so it drifts only if a field is
renamed/removed, the frontmatter stops parsing as YAML, a referenced body section disappears, or
the capture layout changes. This script checks exactly those. Run it after any SCHEMA / TAXONOMIES
/ verb change and in the BACKLOG retro.

Exit 0 = the query recipes still work. Nonzero = QUERYING.md may have drifted; the failures say how.
Stdlib + PyYAML only.

Default run is structure-only (above). Pass --strict to ALSO assert every closed-set frontmatter
value is one TAXONOMIES.md allows (empty always ok; `Other` only where TAXONOMIES grants it). The
value lists are derived from TAXONOMIES at runtime, so it stays the single source of truth. This
catches contract<->corpus drift the structural pass can't see — an off-taxonomy value that still
parses cleanly, e.g. `offering_category: Health & Wellness`.
"""

from __future__ import annotations

import glob
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")


def ver_tuple(v: object) -> tuple[int, int] | None:
    """Normalize a schema_version (int 1, str '1.0', '1.10') to a (major, minor) tuple; None if unparseable."""
    m = re.fullmatch(r"\s*(\d+)(?:\.(\d+))?\s*", str(v))
    return (int(m.group(1)), int(m.group(2) or 0)) if m else None


def current_schema_version(path: str) -> tuple[int, int] | None:
    """The contract's current version, parsed from SCHEMA.md's 'Current contract version' anchor — the single source of truth."""
    with open(path, encoding="utf-8") as f:
        m = re.search(r"Current contract version:\s*`(\d+(?:\.\d+)?)`", f.read())
    return ver_tuple(m.group(1)) if m else None


# Fields the QUERYING.md recipes reference by name — a rename/removal breaks a recipe.
RECIPE_FIELDS = [
    "schema_version",
    "domain",
    "entity_type",
    "target_market",
    "offering_category",
    "business_model",
    "parent",
    "owns",
    "key_pages",
    "unverified_fields",
]
# Recipes test these by list-membership, so they must parse as lists when present.
MULTISELECT = ["target_market", "offering_category"]

# --- strict mode (opt-in): closed-set VALUE conformance against TAXONOMIES.md --------------------
# Structure (above) is QUERYING.md's contract; the value lists are TAXONOMIES.md's. `--strict` derives
# each field's allowed set from TAXONOMIES at runtime (load_taxonomy_sets), so adding a value there
# needs no edit here — TAXONOMIES stays the single source of truth. Only two structural facts are
# mirrored from it; keep them in sync with TAXONOMIES if they ever change:
#   (1) the six closed-set fields, and
CLOSED_FIELDS = [
    "entity_type",
    "target_market",
    "offering_category",
    "business_model",
    "primary_industry",
    "portfolio_shape",
]
#   (2) which of them admit `Other` — TAXONOMIES rule 2: the four category fields only. portfolio_shape
#       is ordinal (empty, never Other) and target_market's four values are exhaustive — neither takes Other.
OTHER_OK = {"entity_type", "offering_category", "business_model", "primary_industry"}


def _grandfathered_versions_from_schema(path: str) -> set[str]:
    """Extract version strings for MINOR bumps that require a FIELD_VERSIONS entry.

    Only matches lines tagged '→ FIELD_VERSIONS' in SCHEMA's version history — the explicit signal
    added when a no-backfill field creates a trust hazard (empty = 'predates it', not 'has none').
    """
    result: set[str] = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            if "FIELD_VERSIONS" in line and "MINOR" in line:
                m = re.search(r"\*\*\*(\d+\.\d+)\*\*\*", line)
                if m:
                    result.add(m.group(1))
    return result


def load_taxonomy_sets(path: str) -> dict[str, set[str]]:
    """Derive {field: {allowed values}} from TAXONOMIES.md — the closed sets live there, not here.

    Each field is a `## `field`` section; a value is a markdown table CELL (lines starting with `|`,
    split on `|`) whose entire content is a single backtick-wrapped token. The whole-cell test is what
    makes it robust across every section's layout — the two-column value/means tables, the three-column
    primary_industry grid, and portfolio_shape's value/means/capture table — while rejecting backticks
    that appear *within* a prose cell (e.g. the `Brand` row's "record the owner in `parent:`") and all
    non-table prose (intro notes, the portfolio_shape tie-breaker) where example values would leak in.
    """
    sets: dict[str, set[str]] = {}
    cur = ""  # the field section we're inside; "" when outside one
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    for line in lines:
        m = re.match(r"^##\s+`(\w+)`", line)
        if m:  # entering a `## `field`` section
            cur = m.group(1) or ""
            sets[cur] = set()
            continue
        if line.startswith("## "):  # a non-field h2 (e.g. "## Rules") ends the field sections
            cur = ""
        if cur and line.lstrip().startswith("|"):
            for cell in line.split("|"):
                cm = re.fullmatch(r"\s*`([^`]+)`\s*", cell)
                if cm:
                    sets[cur].add(cm.group(1).strip())
    return sets


def main() -> None:
    fails: list[str] = []
    warns: list[str] = []
    strict = "--strict" in sys.argv[1:]

    try:
        import yaml
    except ImportError:
        sys.exit("FAIL: PyYAML not importable — the structured-query recipe in QUERYING.md cannot run.")

    tax_sets: dict[str, set[str]] | None = None
    if strict:
        tax_sets = load_taxonomy_sets(os.path.join(ROOT, "TAXONOMIES.md"))
        missing = [f for f in CLOSED_FIELDS if not tax_sets.get(f)]
        if missing:
            fails.append(f"--strict: could not derive {missing} from TAXONOMIES.md — its table format changed?")
            tax_sets = None  # can't enum-check without the sets; structural pass still runs and reports

        # FIELD_VERSIONS coverage: the dict in store.py must cover every grandfathered MINOR version SCHEMA names.
        schema_path = os.path.join(ROOT, "SCHEMA.md")
        gf_vers = _grandfathered_versions_from_schema(schema_path)
        if gf_vers:
            scripts_dir = os.path.dirname(os.path.abspath(__file__))
            if scripts_dir not in sys.path:
                sys.path.insert(0, scripts_dir)
            try:
                from store import FIELD_VERSIONS  # type: ignore[import]
                fv_vers = set(FIELD_VERSIONS.values())
                missing_vers = sorted(gf_vers - fv_vers)
                if missing_vers:
                    fails.append(
                        f"FIELD_VERSIONS in store.py missing entries for schema versions {missing_vers}"
                        f" — append to FIELD_VERSIONS after each MINOR no-backfill bump"
                        f" (has: {sorted(fv_vers)}, needs: {sorted(gf_vers)})."
                    )
            except ImportError as e:
                fails.append(f"FIELD_VERSIONS check: could not import store.py ({e}).")

    cur_ver = current_schema_version(os.path.join(ROOT, "SCHEMA.md"))
    if cur_ver is None:
        warns.append("could not parse 'Current contract version' from SCHEMA.md — schema_version gate skipped.")

    profiles = sorted(glob.glob(os.path.join(STORE, "*", "profile.md")))
    if not profiles:
        sys.exit("FAIL: no store/*/profile.md found.")

    seen_fields: set[str] = set()
    n_prov = n_caps = 0
    for p in profiles:
        slug = os.path.basename(os.path.dirname(p))
        with open(p, encoding="utf-8") as f:
            text = f.read()
        if not text.startswith("---"):
            fails.append(f"{slug}: no leading '---' frontmatter fence.")
            continue
        try:
            fm = yaml.safe_load(text.split("---", 2)[1])
        except Exception as e:  # noqa: BLE001 — any parse error is a real failure to report
            fails.append(f"{slug}: frontmatter is not valid YAML ({type(e).__name__}: {e}).")
            continue
        if not isinstance(fm, dict):
            fails.append(f"{slug}: frontmatter did not parse to a mapping.")
            continue
        seen_fields |= set(fm)
        sv = fm.get("schema_version")
        pv = ver_tuple(sv)
        if sv is not None and pv is None:
            fails.append(f"{slug}: schema_version '{sv}' isn't MAJOR.MINOR — readers can't gate on it.")
        elif pv and cur_ver and pv[0] > cur_ver[0]:
            warns.append(f"{slug}: schema_version {sv} claims a major newer than SCHEMA.md's {cur_ver[0]}.{cur_ver[1]} — drift or typo?")
        for field in MULTISELECT:
            if fm.get(field) is not None and not isinstance(fm[field], list):
                fails.append(f"{slug}: '{field}' parsed as {type(fm[field]).__name__}, not a list — membership recipe breaks.")
        if strict and tax_sets:
            for field in CLOSED_FIELDS:
                raw = fm.get(field)
                if raw in (None, "", []):  # empty is always ok
                    continue
                allowed = tax_sets[field] | ({"Other"} if field in OTHER_OK else set())
                for v in raw if isinstance(raw, list) else [raw]:
                    if v not in allowed:
                        note = " or 'Other'" if field in OTHER_OK else ""
                        fails.append(f"{slug}: {field} value '{v}' is off-taxonomy — not in TAXONOMIES{note}.")
        if "## Provenance" in text:
            n_prov += 1
        if os.path.isdir(os.path.join(os.path.dirname(p), "captures")):
            n_caps += 1

    for field in RECIPE_FIELDS:
        if field not in seen_fields:
            fails.append(f"field '{field}' is named in QUERYING.md but absent from every profile — renamed/removed?")

    if n_prov == 0:
        fails.append("no profile has a '## Provenance' section — the 'trust a negative' recipe breaks.")
    if n_caps == 0:
        warns.append("no profile has a captures/ dir — the primary-source recipe has nothing to grep.")
    if shutil.which("rg") is None:
        warns.append("ripgrep (rg) not on PATH — recipes fall back to grep -r.")

    n = len(profiles)
    label = "querycheck [strict]" if strict else "querycheck"
    print(f"{label}: {n} profile(s); {n_prov}/{n} with Provenance; {n_caps}/{n} with captures/.")
    for w in warns:
        print("WARN:", w)
    if fails:
        for f in fails:
            print("FAIL:", f)
        reason = (
            "QUERYING.md drifted, or a profile holds an off-taxonomy value"
            if strict
            else "QUERYING.md may have drifted from the contract/verb"
        )
        sys.exit(f"\n{len(fails)} failure(s) — {reason}.")
    if strict:
        print("OK — structure holds and every closed-set value conforms to TAXONOMIES.")
    else:
        print("OK — QUERYING.md's structural assumptions hold.")


if __name__ == "__main__":
    main()
