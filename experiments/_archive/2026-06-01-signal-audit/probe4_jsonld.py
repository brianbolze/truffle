#!/usr/bin/env python3
"""Probe: what would reading rawHtml's JSON-LD actually ADD to each profile?

For a spread of profiles, extract the JSON-LD identity graph + a quick <header> check,
normalize the fields, and mark each value NET-NEW vs already-in-profile. The output is
the per-profile enrichment delta — the thing that decides the field-scope boundary.
$0: reads persisted payloads + committed profile.md only.
"""
import json, re, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORE = os.path.join(ROOT, "store")

SET = ["honehealth-com","hims-com","marekhealth-com","clari-com","datadoghq-com","usertesting-com"]

def load(p): d=json.load(open(p)); return d.get("data",d)
def homepage(slug):
    c=sorted(glob.glob(os.path.join(STORE,slug,"captures","*",".payloads","homepage.json")))
    return load(c[-1]) if c else None
def profile_text(slug):
    p=os.path.join(STORE,slug,"profile.md")
    return open(p).read() if os.path.exists(p) else ""

def walk(obj, types):
    """collect all dicts that have @type, flattening @graph/lists."""
    if isinstance(obj, list):
        for x in obj: walk(x, types)
    elif isinstance(obj, dict):
        if "@graph" in obj: walk(obj["@graph"], types)
        t = obj.get("@type")
        if t: types.setdefault(t if isinstance(t,str) else t[0], []).append(obj)
        for v in obj.values(): walk(v, types)

def jsonld(slug):
    raw = homepage(slug)["rawHtml"]
    blocks = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', raw, re.S|re.I)
    types={}
    for b in blocks:
        try: walk(json.loads(b.strip()), types)
        except Exception: pass
    return types

def flat(v):
    """render a JSON-LD value compactly"""
    if v is None: return None
    if isinstance(v,str): return v.strip()
    if isinstance(v,list):
        parts=[flat(x) for x in v]; parts=[p for p in parts if p]
        return ", ".join(parts) if parts else None
    if isinstance(v,dict):
        for k in ("name","url","ratingValue","streetAddress","email","telephone"):
            if k in v: return flat(v[k])
        return json.dumps(v)[:80]
    return str(v)

def org_of(types):
    for t in ("Organization","Corporation","MedicalOrganization","LocalBusiness"):
        if t in types: return t, types[t][0]
    return None, {}
def sw_of(types):
    return types.get("SoftwareApplication",[{}])[0] if "SoftwareApplication" in types else {}
def rating_of(types):
    if "AggregateRating" in types: return types["AggregateRating"][0]
    return {}

# fields to surface: (label, extractor)
def extract(types):
    t, org = org_of(types)
    sw = sw_of(types)
    rating = rating_of(types) or org.get("aggregateRating") or sw.get("aggregateRating") or {}
    addr = org.get("address") or {}
    contact = org.get("contactPoint")
    if isinstance(contact, list): contact = contact[0] if contact else {}
    contact = contact or {}
    founders = org.get("founder") or org.get("founders")
    return t, {
        "name":            flat(org.get("name") or sw.get("name")),
        "legalName":       flat(org.get("legalName")),
        "alternateName":   flat(org.get("alternateName")),
        "description":     (flat(org.get("description") or sw.get("description")) or "")[:90] or None,
        "foundingDate":    flat(org.get("foundingDate")),
        "founders":        flat(founders),
        "HQ address":      flat(addr) if addr else None,
        "contact":         flat(contact.get("email") or contact.get("telephone") or org.get("email") or org.get("telephone")),
        "specialty/category": flat(org.get("medicalSpecialty") or sw.get("applicationCategory")),
        "aggregateRating": (f"{flat(rating.get('ratingValue'))} ({flat(rating.get('reviewCount') or rating.get('ratingCount'))} reviews)" if rating else None),
        "sameAs (socials)": flat(org.get("sameAs")),
        "logo":            flat(org.get("logo")),
    }

def in_profile(slug, value):
    """already in profile.md? Test the MOST DISTINCTIVE token (longest >=5 chars),
    else the full normalized value — avoids false 'already' on common short tokens
    like 'Time'/'hims'/'2017'."""
    if not value: return "—"
    txt = profile_text(slug).lower()
    val = str(value)
    toks = sorted({w for w in re.findall(r"[A-Za-z][A-Za-z'&.\-/]{4,}", val)}, key=len, reverse=True)
    probes = toks[:3] if toks else [val]
    hit = any(p.lower() in txt for p in probes)
    return "already" if hit else "NET-NEW"

print("# JSON-LD enrichment delta — what reading rawHtml would add per profile\n")
netnew_tally = {}
for slug in SET:
    types = jsonld(slug)
    t, fields = extract(types)
    print(f"\n=== {slug}  (@type: {t or '?'}; all: {sorted(types)}) ===")
    for label, val in fields.items():
        if val is None:
            continue
        status = in_profile(slug, val)
        if status == "NET-NEW": netnew_tally[label] = netnew_tally.get(label,0)+1
        sval = (val[:95] + "…") if len(str(val)) > 96 else val
        print(f"  {label:20} [{status:8}] {sval}")

print("\n\n# NET-NEW tally across the set (how often each field would add something)")
for label,n in sorted(netnew_tally.items(), key=lambda x:-x[1]):
    print(f"  {n}/{len(SET)}  {label}")

# --- quick <header> sanity check: does the nav slice extract cleanly? ---
print("\n\n# <header> region extraction sanity (the nav slice)")
for slug in SET:
    raw = homepage(slug)["rawHtml"]
    m = re.search(r'<header\b.*?</header>', raw, re.S|re.I)
    seg = m.group(0) if m else ""
    nseg = ""
    if not seg:  # fallback: first <nav>...</nav>
        mn = re.search(r'<nav\b.*?</nav>', raw, re.S|re.I)
        nseg = mn.group(0) if mn else ""
    use = seg or nseg
    links = len(re.findall(r'<a\b', use))
    print(f"  {slug:18} <header>={bool(seg)} <nav-fallback>={bool(nseg)} bytes={len(use):6} <a>={links:3}")

# --- exact re-verification of the specific claims in FINDINGS.md / BACKLOG.md ---
print("\n\n# EXACT claim checks (the headline 'left on the table' examples)")
checks = [
    ("honehealth-com", "Time Therapeutics", "honehealth legalName"),
    ("honehealth-com", "Endocrinology",     "honehealth medicalSpecialty"),
    ("hims-com",       "hims & hers",        "hims alias #1"),
    ("hims-com",       "forhims",            "hims alias #2"),
    ("clari-com",      "5602",               "clari rating count"),
    ("usertesting-com","1034",               "usertesting rating count"),
]
for slug, needle, label in checks:
    present = needle.lower() in profile_text(slug).lower()
    print(f"  {'in profile' if present else 'ABSENT    '}  {label:34} ({needle!r})")
