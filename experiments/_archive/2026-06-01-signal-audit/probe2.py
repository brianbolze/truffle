#!/usr/bin/env python3
"""Targeted deep-dives: concrete examples behind the stats."""
import json, re, os, glob, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORE = os.path.join(ROOT, "store")

def load(p):
    d = json.load(open(p)); return d.get("data", d)
def hp(slug):
    cands = sorted(glob.glob(os.path.join(STORE, slug, "captures","*",".payloads","homepage.json")))
    return load(cands[-1]) if cands else None
def page(slug, name):
    cands = sorted(glob.glob(os.path.join(STORE, slug, "captures","*",".payloads",name)))
    return load(cands[-1]) if cands else None

def sec(t): print(f"\n{'#'*60}\n# {t}\n{'#'*60}")

# --- 1. html price recovery: functionhealth $42 / $499 ---
sec("html price recovery — functionhealth")
d = hp("functionhealth-com")
md, html = d["markdown"], d["html"]
for tok in ["$42","$499"]:
    print(f"\n--- token {tok} ---")
    print("in markdown?", tok in md, " | in html?", tok in html)
    i = html.find(tok)
    if i>=0:
        ctx = re.sub(r'<[^>]+>',' ', html[max(0,i-220):i+80])
        ctx = re.sub(r'\s+',' ',ctx).strip()
        print("  html ctx:", ctx[:260])
# what does markdown say near 'month' price area
print("\n--- markdown $ tokens ---", re.findall(r'\$\s?\d[\d,]*', md))

# --- 2. JSON-LD content examples ---
sec("JSON-LD payloads — what structured signal")
def first_ld(slug):
    raw = hp(slug)["rawHtml"]
    blocks = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', raw, re.S|re.I)
    out=[]
    for b in blocks:
        try: out.append(json.loads(b.strip()))
        except: pass
    return out
for slug in ["clari-com","hims-com","honehealth-com","usertesting-com","datadoghq-com","marekhealth-com"]:
    print(f"\n--- {slug} ---")
    for obj in first_ld(slug):
        s = json.dumps(obj)[:600]
        print(" ", s)

# --- 3. metadata price microdata ---
sec("metadata price/currency microdata — which pages")
for s in sorted(glob.glob(os.path.join(STORE,"*","captures","*",".payloads","*.json"))):
    if os.path.basename(s) in ("map.json","manifest.jsonl"): continue
    try: d=load(s)
    except: continue
    m=d.get("metadata",{}) or {}
    if any(k in m for k in ("price","priceCurrency","eligibleQuantity")):
        slug=s.split("/store/")[1].split("/")[0]; nm=os.path.basename(s)
        print(f"  {slug}/{nm}: price={m.get('price')} cur={m.get('priceCurrency')} qty={m.get('eligibleQuantity')}")

# --- 4. metadata keywords ---
sec("metadata keywords (self-declared)")
for slug in ["functionhealth-com","gethealthspan-com","casio-com","swatch-com","rolex-com","alpha-sense-com"]:
    d=hp(slug)
    if not d: continue
    kw=(d.get("metadata",{}) or {}).get("keywords")
    print(f"  {slug}: {str(kw)[:200]}")

# --- 5. branding personality + typography ---
sec("branding.personality / typography / components — brand.md feedstock")
for slug in ["agelessrx-com","stripe-com","rolex-com"]:
    b=hp(slug)["branding"]
    print(f"\n--- {slug} ---")
    print("  personality:", json.dumps(b.get("personality"))[:500])
    print("  typography:", json.dumps(b.get("typography"))[:400])
    print("  fonts:", json.dumps(b.get("fonts"))[:200])
    print("  colors:", json.dumps(b.get("colors"))[:300])
    print("  images:", json.dumps(b.get("images"))[:300])

# --- 6. images: logo candidates + og:logo ---
sec("images[] logo candidates + og:logo / og:image")
for slug in ["delighted-com","upwork-com","granola-ai","apple-com"]:
    d=hp(slug); imgs=d.get("images",[]) or []; m=d.get("metadata",{}) or {}
    logos=[i for i in imgs if isinstance(i,str) and "logo" in i.lower()][:6]
    print(f"\n--- {slug} ---")
    print("  og:logo:", m.get("og:logo"))
    print("  og:image:", m.get("og:image"))
    print("  branding.images.logo:", (d.get('branding',{}) or {}).get('images',{}).get('logo'))
    for l in logos: print("   logo-named:", l[:140])

# --- 7. links unique to links[] on a JS site (airbnb) vs redundant (cloudflare) ---
sec("links[] unique vs markdown — JS site vs static")
for slug in ["airbnb-com","cloudflare-com"]:
    d=hp(slug); links=d.get("links",[]) or []; md=d["markdown"]
    md_abs=set(re.findall(r'\]\((https?://[^)]+)\)', md))
    def paths(urls):
        ps=set()
        for u in urls:
            mm=re.match(r'https?://[^/]+(/[^?#]*)',u)
            if mm: ps.add(mm.group(1))
        return ps
    lp, mp = paths(links), paths(md_abs)
    only=sorted(lp-mp)[:15]
    print(f"\n--- {slug} --- links[]={len(links)} only-in-links[] sample:")
    for o in only: print("   ", o)
