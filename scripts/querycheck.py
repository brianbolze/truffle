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

import glob
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")

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


def load_taxonomy_sets(path):
    """Derive {field: {allowed values}} from TAXONOMIES.md — the closed sets live there, not here.

    Each field is a `## `field`` section; a value is a markdown table CELL (lines starting with `|`,
    split on `|`) whose entire content is a single backtick-wrapped token. The whole-cell test is what
    makes it robust across every section's layout — the two-column value/means tables, the three-column
    primary_industry grid, and portfolio_shape's value/means/capture table — while rejecting backticks
    that appear *within* a prose cell (e.g. the `Brand` row's "record the owner in `parent:`") and all
    non-table prose (intro notes, the portfolio_shape tie-breaker) where example values would leak in.
    """
    sets, cur = {}, None
    for line in open(path, encoding="utf-8").read().splitlines():
        m = re.match(r"^##\s+`(\w+)`", line)
        if m:  # entering a `## `field`` section
            cur = m.group(1)
            sets[cur] = set()
            continue
        if line.startswith(
            "## "
        ):  # a non-field h2 (e.g. "## Rules") ends the field sections
            cur = None
        if cur and line.lstrip().startswith("|"):
            for cell in line.split("|"):
                cm = re.fullmatch(r"\s*`([^`]+)`\s*", cell)
                if cm:
                    sets[cur].add(cm.group(1).strip())
    return sets


fails, warns = [], []
strict = "--strict" in sys.argv[1:]

try:
    import yaml
except ImportError:
    sys.exit(
        "FAIL: PyYAML not importable — the structured-query recipe in QUERYING.md cannot run."
    )

tax_sets = None
if strict:
    tax_sets = load_taxonomy_sets(os.path.join(ROOT, "TAXONOMIES.md"))
    missing = [f for f in CLOSED_FIELDS if not tax_sets.get(f)]
    if missing:
        fails.append(
            f"--strict: could not derive {missing} from TAXONOMIES.md — its table format changed?"
        )
        tax_sets = None  # can't enum-check without the sets; structural pass still runs and reports

profiles = sorted(glob.glob(os.path.join(STORE, "*", "profile.md")))
if not profiles:
    sys.exit("FAIL: no store/*/profile.md found.")

seen_fields = set()
n_prov = n_caps = 0
for p in profiles:
    slug = os.path.basename(os.path.dirname(p))
    text = open(p).read()
    if not text.startswith("---"):
        fails.append(f"{slug}: no leading '---' frontmatter fence.")
        continue
    try:
        fm = yaml.safe_load(text.split("---", 2)[1])
    except Exception as e:  # noqa: BLE001 — any parse error is a real failure to report
        fails.append(
            f"{slug}: frontmatter is not valid YAML ({type(e).__name__}: {e})."
        )
        continue
    if not isinstance(fm, dict):
        fails.append(f"{slug}: frontmatter did not parse to a mapping.")
        continue
    seen_fields |= set(fm)
    for f in MULTISELECT:
        if fm.get(f) is not None and not isinstance(fm[f], list):
            fails.append(
                f"{slug}: '{f}' parsed as {type(fm[f]).__name__}, not a list — membership recipe breaks."
            )
    if strict and tax_sets:
        for field in CLOSED_FIELDS:
            raw = fm.get(field)
            if raw in (None, "", []):  # empty is always ok
                continue
            allowed = tax_sets[field] | ({"Other"} if field in OTHER_OK else set())
            for v in (raw if isinstance(raw, list) else [raw]):
                if v not in allowed:
                    note = " or 'Other'" if field in OTHER_OK else ""
                    fails.append(
                        f"{slug}: {field} value '{v}' is off-taxonomy — not in TAXONOMIES{note}."
                    )
    if "## Provenance" in text:
        n_prov += 1
    if os.path.isdir(os.path.join(os.path.dirname(p), "captures")):
        n_caps += 1

for f in RECIPE_FIELDS:
    if f not in seen_fields:
        fails.append(
            f"field '{f}' is named in QUERYING.md but absent from every profile — renamed/removed?"
        )

if n_prov == 0:
    fails.append(
        "no profile has a '## Provenance' section — the 'trust a negative' recipe breaks."
    )
if n_caps == 0:
    warns.append(
        "no profile has a captures/ dir — the primary-source recipe has nothing to grep."
    )
if shutil.which("rg") is None:
    warns.append("ripgrep (rg) not on PATH — recipes fall back to grep -r.")

n = len(profiles)
label = "querycheck [strict]" if strict else "querycheck"
print(
    f"{label}: {n} profile(s); {n_prov}/{n} with Provenance; {n_caps}/{n} with captures/."
)
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
