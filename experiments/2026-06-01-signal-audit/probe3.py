#!/usr/bin/env python3
"""Verification: is the JSON-LD / html signal GENUINELY absent from markdown+metadata?"""
import json, re, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORE = os.path.join(ROOT, "store")
def load(p): d=json.load(open(p)); return d.get("data",d)
def page(slug,name):
    c=sorted(glob.glob(os.path.join(STORE,slug,"captures","*",".payloads",name)))
    return load(c[-1]) if c else None

def sec(t): print(f"\n{'#'*60}\n# {t}\n{'#'*60}")

# 1. functionhealth html prices — honest context
sec("functionhealth: $42 / $499 real or artifact?")
d=page("functionhealth-com","homepage.json")
html=d["html"]
for tok in ["$42","$499"]:
    i=html.find(tok)
    raw=html[max(0,i-120):i+120]
    print(f"\n{tok} raw html slice:\n  {raw}")

# 2. JSON-LD fields absent from markdown? (the unique-signal test)
sec("JSON-LD identity fields: present in markdown? metadata?")
checks = {
 "hims-com": ["forhims","hims & hers","2017","Andrew Dudum","Jack Abraham"],
 "honehealth-com": ["Time Therapeutics","Endocrinology","Andrology","2021"],
 "marekhealth-com": ["Marek Health LLC","Pontiac","48342"],
 "datadoghq-com": ["2010","info@datadoghq.com","+1-866"],
 "clari-com": ["9.2","5602"],
 "usertesting-com": ["4.25","1034"],
}
for slug,toks in checks.items():
    d=page(slug,"homepage.json")
    md=d.get("markdown","") or ""
    meta=json.dumps(d.get("metadata",{}) or {})
    print(f"\n--- {slug} ---")
    for t in toks:
        print(f"  {t!r:30} in md={t in md!s:5} in metadata={t in meta!s:5}")

# 3. Does metadata already flatten JSON-LD org fields? sample full metadata keys for a JSON-LD-rich page
sec("Is JSON-LD reachable via metadata, or only rawHtml? (honehealth/clari metadata keys)")
for slug in ["honehealth-com","clari-com","datadoghq-com"]:
    d=page(slug,"homepage.json"); m=d.get("metadata",{}) or {}
    interesting={k:v for k,v in m.items() if any(s in k.lower() for s in
        ("name","found","rating","legal","price","logo","author","email","tel","special"))}
    print(f"\n--- {slug} metadata (identity-ish keys) ---")
    for k,v in interesting.items(): print(f"  {k}: {str(v)[:80]}")

# 4. aliases in frontmatter today vs JSON-LD alternateName — does profile capture them?
sec("Does current profile.md capture what JSON-LD offered? (hims aliases / honehealth legalName)")
for slug,grep in [("hims-com","alias"),("honehealth-com","legal"),("honehealth-com","Time Therapeutics")]:
    pf=os.path.join(STORE,slug,"profile.md")
    if os.path.exists(pf):
        txt=open(pf).read()
        hits=[l for l in txt.splitlines() if grep.lower() in l.lower()]
        print(f"  {slug} grep {grep!r}: {hits[:3] if hits else 'NONE'}")
