#!/usr/bin/env python3
"""querycheck — assert QUERYING.md's structural assumptions still hold against the live store.

QUERYING.md names *fields and mechanics* (never value lists), so it drifts only if a field is
renamed/removed, the frontmatter stops parsing as YAML, a referenced body section disappears, or
the capture layout changes. This script checks exactly those. Run it after any SCHEMA / TAXONOMIES
/ verb change and in the BACKLOG retro.

Exit 0 = the query recipes still work. Nonzero = QUERYING.md may have drifted; the failures say how.
Stdlib + PyYAML only.
"""
import glob
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")

# Fields the QUERYING.md recipes reference by name — a rename/removal breaks a recipe.
RECIPE_FIELDS = [
    "schema_version", "domain", "entity_type", "target_market", "offering_category",
    "business_model", "parent", "owns", "key_pages", "unverified_fields",
]
# Recipes test these by list-membership, so they must parse as lists when present.
MULTISELECT = ["target_market", "offering_category"]

fails, warns = [], []

try:
    import yaml
except ImportError:
    sys.exit("FAIL: PyYAML not importable — the structured-query recipe in QUERYING.md cannot run.")

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
        fails.append(f"{slug}: frontmatter is not valid YAML ({type(e).__name__}: {e}).")
        continue
    if not isinstance(fm, dict):
        fails.append(f"{slug}: frontmatter did not parse to a mapping.")
        continue
    seen_fields |= set(fm)
    for f in MULTISELECT:
        if fm.get(f) is not None and not isinstance(fm[f], list):
            fails.append(f"{slug}: '{f}' parsed as {type(fm[f]).__name__}, not a list — membership recipe breaks.")
    if "## Provenance" in text:
        n_prov += 1
    if os.path.isdir(os.path.join(os.path.dirname(p), "captures")):
        n_caps += 1

for f in RECIPE_FIELDS:
    if f not in seen_fields:
        fails.append(f"field '{f}' is named in QUERYING.md but absent from every profile — renamed/removed?")

if n_prov == 0:
    fails.append("no profile has a '## Provenance' section — the 'trust a negative' recipe breaks.")
if n_caps == 0:
    warns.append("no profile has a captures/ dir — the primary-source recipe has nothing to grep.")
if shutil.which("rg") is None:
    warns.append("ripgrep (rg) not on PATH — recipes fall back to grep -r.")

n = len(profiles)
print(f"querycheck: {n} profile(s); {n_prov}/{n} with Provenance; {n_caps}/{n} with captures/.")
for w in warns:
    print("WARN:", w)
if fails:
    for f in fails:
        print("FAIL:", f)
    sys.exit(f"\n{len(fails)} failure(s) — QUERYING.md may have drifted from the contract/verb.")
print("OK — QUERYING.md's structural assumptions hold.")
