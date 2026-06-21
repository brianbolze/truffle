#!/usr/bin/env python3
"""Cross-anchor analysis of Exa /findSimilar captures for run 030.

The capture tool is match-free by design (see tools/exa_similar.md); this is the
*caller* orchestration it leaves out: apex-fold mirrors, dedupe across anchors,
score cross-anchor recurrence (hubs), and match neighbors against the captured store.
Reads receipts/exa/*.json; prints a report to stdout.
"""
from __future__ import annotations
import json, glob, os, re
from collections import defaultdict

RUN = os.path.dirname(os.path.abspath(__file__))
EXA = os.path.join(RUN, "exa")
STORE = os.path.abspath(os.path.join(RUN, "../../../../../store"))

TELEHEALTH = {  # anchor dir -> anchor_category (the spread we ran)
    "honehealth-com": "longevity/NAD", "mylifeforce-com": "longevity/NAD",
    "gethealthspan-com": "longevity/NAD", "gogeviti-com": "longevity/NAD",
    "agelessrx-com": "longevity/NAD", "defymedical-com": "TRT",
    "marekhealth-com": "TRT", "maximustribe-com": "TRT", "hormonemd-com": "TRT",
    "functionhealth-com": "labs", "ro-co": "GLP-1", "hims-com": "GLP-1",
    "henrymeds-com": "GLP-1", "remedymeds-com": "GLP-1", "rexmd-com": "sexual-health",
    "bluechew-com": "sexual-health", "lifemd-com": "multi/none", "nurx-com": "multi/none",
}
SAAS = {"posthog-com", "notion-com", "linear-app", "airtable-com", "snowflake-com"}

# run 017's store-only Hone neighbor tiering (the calibration baseline)
R017 = {
    "mylifeforce.com": "T1", "gogeviti.com": "T1", "gethealthspan.com": "T1", "defymedical.com": "T1",
    "getopt.com": "T2", "marekhealth.com": "T2", "maximustribe.com": "T2", "getpetermd.com": "T2",
    "hormonemd.com": "T2", "trtnation.com": "T2",
    "functionhealth.com": "T3", "vitalityrx.com": "T3", "agelessrx.com": "T3",
    "prohealth.com": "T3", "niagenplus.com": "T3", "truniagen.com": "T3",
}

def norm(host: str) -> str:
    h = host.strip().lower()
    h = re.sub(r"^https?://", "", h).split("/")[0]
    return h[4:] if h.startswith("www.") else h

# build store domain set
store_doms = set()
for pf in glob.glob(os.path.join(STORE, "*/profile.md")):
    with open(pf, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("domain:"):
                store_doms.add(norm(line.split(":", 1)[1]))
                break
print(f"store profiled domains: {len(store_doms)}\n")

# load captures
anchors = {}  # dir -> [norm domains]
for jf in sorted(glob.glob(os.path.join(EXA, "*.json"))):
    d = os.path.basename(jf)[:-5]
    with open(jf, encoding="utf-8") as fh:
        env = json.load(fh)
    anchors[d] = [norm(n["domain"]) for n in env.get("neighbors", [])]

anchor_doms = {norm(({**{k: k for k in []}}.get(d) or "")) for d in anchors}  # placeholder

def fold(d):  # registrable-ish fold: last 2 labels (mirrors like forhims.co.uk won't fold; eyeball those)
    p = d.split(".")
    return ".".join(p[-2:]) if len(p) >= 2 else d

# cross-anchor frequency, scoped to telehealth vs saas
def hubs(anchor_set, label):
    freq = defaultdict(set)
    for a in anchor_set:
        for nb in anchors.get(a, []):
            freq[nb].add(a)
    rows = []
    for nb, aset in freq.items():
        rows.append((len(aset), nb, nb in store_doms, sorted(aset)))
    rows.sort(key=lambda r: (-r[0], r[1]))
    print(f"\n===== {label}: cross-anchor hubs (neighbors shared by >=2 anchors) =====")
    print(f"{'#anc':>4}  {'in_store':>8}  neighbor                         anchors")
    for cnt, nb, ins, aset in rows:
        if cnt < 2:
            continue
        tag = "STORE" if ins else "absent"
        print(f"{cnt:>4}  {tag:>8}  {nb:<32} {','.join(a.replace('-com','').replace('-','') for a in aset)}")
    # store-absent hubs = the worklist
    absent = [(c, nb, a) for c, nb, ins, a in rows if c >= 2 and not ins]
    print(f"\n  {label} store-ABSENT hubs (>=2 anchors, not captured): {len(absent)}")
    return rows

th_rows = hubs(list(TELEHEALTH), "TELEHEALTH")
saas_rows = hubs(list(SAAS), "SAAS")

# per-anchor store-hit rate (selection-bias quantification)
print("\n\n===== per-anchor neighbor store-coverage (of 25 Exa neighbors, how many captured) =====")
print(f"{'anchor':<20} {'cat':<14} {'in_store':>8} {'absent':>7}")
for a in list(TELEHEALTH) + sorted(SAAS):
    nbs = anchors.get(a, [])
    ins = sum(1 for n in nbs if n in store_doms and n != norm(a.replace("-com",".com")))
    cat = TELEHEALTH.get(a, "SAAS")
    print(f"{a:<20} {cat:<14} {ins:>8} {len(nbs)-ins:>7}")

# Hone calibration vs run 017
print("\n\n===== HONE calibration: Exa neighbors vs run-017 store-only tiering =====")
hone = anchors.get("honehealth-com", [])
print(f"Hone Exa neighbors (25): {hone}\n")
hits = [(n, R017[n]) for n in hone if n in R017]
print(f"017 brands that ALSO appear in Hone's Exa list ({len(hits)}/16):")
for n, t in hits:
    print(f"   {t}  {n}")
missed = [n for n in R017 if n not in hone]
print(f"\n017 brands NOT in Hone's Exa top-25 ({len(missed)}): {missed}")
new_in_store = [n for n in hone if n not in R017 and n in store_doms]
new_absent = [n for n in hone if n not in R017 and n not in store_doms]
print(f"\nNEW Hone neighbors Exa surfaced that 017 did NOT have:")
print(f"   in store ({len(new_in_store)}): {new_in_store}")
print(f"   store-absent ({len(new_absent)}): {new_absent}")
