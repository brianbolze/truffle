#!/usr/bin/env python3
"""Signal audit over existing Firecrawl payloads. $0 — reads store/*/captures/*/.payloads/ only.

Per format (html, rawHtml, links, images, branding, metadata) characterize what UNIQUE
signal it adds beyond markdown + screenshot. Output is descriptive stats + concrete examples;
the keep/cut call is made by hand in FINDINGS.md.
"""
import json, re, os, glob, collections, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
ROOT = os.path.dirname(ROOT)  # up from experiments/
STORE = os.path.join(ROOT, "store")

def load(p):
    try:
        d = json.load(open(p))
    except Exception as e:
        return None
    return d.get("data", d) if isinstance(d, dict) else None

def h(v):
    """coerce to hashable for Counter keys"""
    if isinstance(v, list): return tuple(h(x) for x in v)
    if isinstance(v, dict): return tuple(sorted((k, h(x)) for k,x in v.items()))
    return v

def latest_capture_dir(store_dir):
    caps = sorted(glob.glob(os.path.join(store_dir, "captures", "*", ".payloads")))
    # pick the latest non-empty
    for d in reversed(caps):
        if glob.glob(os.path.join(d, "*.json")):
            return d
    return None

stores = sorted(glob.glob(os.path.join(STORE, "*")))
homepages = []   # (slug, dir, data)
allpages = []    # (slug, name, data)
for s in stores:
    if not os.path.isdir(s): continue
    slug = os.path.basename(s)
    pd = latest_capture_dir(s)
    if not pd: continue
    hp = os.path.join(pd, "homepage.json")
    if os.path.exists(hp):
        d = load(hp)
        if d: homepages.append((slug, pd, d))
    for jf in glob.glob(os.path.join(pd, "*.json")):
        nm = os.path.basename(jf)
        if nm in ("manifest.jsonl", "map.json"): continue
        d = load(jf)
        if d: allpages.append((slug, nm, d))

print(f"# corpus: {len(homepages)} homepages, {len(allpages)} total page payloads\n")

def section(t): print(f"\n{'='*70}\n{t}\n{'='*70}")

# ---------------------------------------------------------------------------
section("1. FORMAT PRESENCE & SIZE (homepage rich pass)")
fmts = ["markdown","html","rawHtml","links","branding","images","screenshot","metadata"]
print(f"{'slug':28} " + " ".join(f"{f[:8]:>9}" for f in fmts))
size_ratios = collections.defaultdict(list)
for slug, pd, d in homepages:
    cells=[]
    md_len = len(d.get("markdown","") or "")
    for f in fmts:
        v = d.get(f)
        if v is None: cells.append(f"{'-':>9}"); continue
        if isinstance(v,str): n=len(v)
        elif isinstance(v,(list,dict)): n=len(v)
        else: n=1
        cells.append(f"{n:>9}")
        if f in ("html","rawHtml") and md_len:
            size_ratios[f].append(n/md_len)
    print(f"{slug:28} " + " ".join(cells))
print("\nbyte ratio vs markdown (homepage):")
for f,rs in size_ratios.items():
    rs=sorted(rs); print(f"  {f}: median {rs[len(rs)//2]:.0f}x  (range {rs[0]:.0f}–{rs[-1]:.0f}x)")

# ---------------------------------------------------------------------------
section("2. METADATA — content signal vs capture-meta")
# which keys appear, and classify
key_freq = collections.Counter()
for slug, nm, d in allpages:
    m = d.get("metadata",{}) or {}
    for k in m: key_freq[k]+=1
print("metadata key frequency across ALL pages (n=%d):" % len(allpages))
for k,c in key_freq.most_common():
    print(f"  {c:4} {k}")

CAPTURE_META = {"scrapeId","sourceURL","url","statusCode","contentType","timezone",
    "proxyUsed","indexId","creditsUsed","concurrencyLimited","cacheState","cachedAt","numPages"}
print("\n-- generator field (CMS/framework self-report) --")
gen = collections.Counter()
for slug,pd,d in homepages:
    g = (d.get("metadata",{}) or {}).get("generator")
    gen[g and g[:60]] += 1
for g,c in gen.most_common(): print(f"  {c:3} {g!r}")

print("\n-- og:site_name vs domain (canonical-name signal) --")
for slug,pd,d in homepages[:50]:
    m=d.get("metadata",{}) or {}
    sn = m.get("og:site_name") or m.get("ogSiteName")
    print(f"  {slug:26} site_name={sn!r}")

print("\n-- language / og:locale presence --")
loc = collections.Counter()
for slug,pd,d in homepages:
    m=d.get("metadata",{}) or {}
    loc[(h(m.get("language")), h(m.get("og:locale") or m.get("ogLocale")))] += 1
for v,c in loc.most_common(): print(f"  {c:3} {v}")

print("\n-- favicon present? type? --")
fav = collections.Counter()
for slug,pd,d in homepages:
    f=(d.get("metadata",{}) or {}).get("favicon")
    if not f: fav["(none)"]+=1
    elif f.startswith("data:"): fav["data-uri"]+=1
    elif f.endswith(".svg"): fav["svg"]+=1
    elif ".ico" in f: fav["ico"]+=1
    else: fav["other-img"]+=1
for v,c in fav.most_common(): print(f"  {c:3} {v}")

# ---------------------------------------------------------------------------
section("3. rawHtml — structured signal not in markdown")
print("-- JSON-LD (schema.org) blocks per homepage + @types --")
type_freq = collections.Counter()
ld_pages=0
for slug,pd,d in homepages:
    raw = d.get("rawHtml","") or ""
    blocks = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', raw, re.S|re.I)
    types=[]
    for b in blocks:
        for m in re.findall(r'"@type"\s*:\s*"([^"]+)"', b):
            types.append(m)
    if types: ld_pages+=1
    for t in set(types): type_freq[t]+=1
    if blocks:
        print(f"  {slug:26} {len(blocks)} block(s): {sorted(set(types))}")
print(f"  -> {ld_pages}/{len(homepages)} homepages carry JSON-LD")
print("  @type frequency:", dict(type_freq.most_common()))

print("\n-- hreflang alternates (locale/geo IA, invisible in markdown) --")
for slug,pd,d in homepages:
    raw = d.get("rawHtml","") or ""
    hl = re.findall(r'hreflang=["\']([^"\']+)["\']', raw, re.I)
    if hl:
        print(f"  {slug:26} {len(hl)} alternates  e.g. {sorted(set(hl))[:8]}")

print("\n-- canonical link --")
canon=0
for slug,pd,d in homepages:
    raw=d.get("rawHtml","") or ""
    if re.search(r'rel=["\']canonical["\']', raw, re.I): canon+=1
print(f"  {canon}/{len(homepages)} have <link rel=canonical>")

print("\n-- nav/header region: aria-controls (flyout targets) + <nav> count --")
for slug,pd,d in homepages:
    raw=d.get("rawHtml","") or ""
    navs=len(re.findall(r'<nav\b', raw, re.I))
    aria=len(re.findall(r'aria-controls=', raw, re.I))
    haspop=len(re.findall(r'aria-haspopup=', raw, re.I))
    print(f"  {slug:26} <nav>={navs:3}  aria-controls={aria:3}  aria-haspopup={haspop:3}")

# ---------------------------------------------------------------------------
section("4. html vs markdown — value recovery (price garbling)")
PRICE = re.compile(r'[$£€]\s?\d[\d,]*(?:\.\d{2})?')
for slug,pd,d in homepages:
    md=d.get("markdown","") or ""
    html=d.get("html","") or ""
    if not html: continue
    md_p = set(PRICE.findall(md))
    html_p = set(PRICE.findall(html))
    only_html = html_p - md_p
    if only_html and len(only_html)>=2:
        print(f"  {slug:26} prices in html-not-md: {sorted(only_html)[:10]}")
# also: pages where markdown is near-empty but html has content
print("\n-- pages where markdown thin (<500 chars) but html rich --")
for slug,nm,d in allpages:
    md=len(d.get("markdown","") or "")
    h=len(d.get("html","") or "")
    if h and md<500 and h>5000:
        print(f"  {slug}/{nm}: md={md} html={h}")

# ---------------------------------------------------------------------------
section("5. links — IA inventory vs markdown")
print("-- link count per page; homepage links vs internal --")
for slug,pd,d in homepages:
    links=d.get("links",[]) or []
    host = None
    m=d.get("metadata",{}) or {}
    su=m.get("sourceURL") or m.get("url") or ""
    mm=re.match(r'https?://([^/]+)', su)
    host = mm.group(1) if mm else slug.replace("-",".")
    internal=[l for l in links if host.split(".")[-2] in l] if host else links
    print(f"  {slug:26} links={len(links):4} internal≈{len(internal):4}")
# how many distinct paths only in links[] not markdown link syntax
print("\n-- nav completeness: distinct internal paths in links[] vs in markdown --")
for slug,pd,d in homepages[:12]:
    links=d.get("links",[]) or []
    md=d.get("markdown","") or ""
    md_links=set(re.findall(r'\]\((https?://[^)]+)\)', md))
    paths=set()
    for l in links:
        mm=re.match(r'https?://[^/]+(/[^?#]*)', l)
        if mm: paths.add(mm.group(1))
    md_paths=set()
    for l in md_links:
        mm=re.match(r'https?://[^/]+(/[^?#]*)', l)
        if mm: md_paths.add(mm.group(1))
    print(f"  {slug:26} links[] paths={len(paths):4}  md-link paths={len(md_paths):4}  only-in-links={len(paths-md_paths):4}")

# ---------------------------------------------------------------------------
section("6. images — logo set feasibility")
for slug,pd,d in homepages:
    imgs=d.get("images",[]) or []
    svg=[i for i in imgs if isinstance(i,str) and ".svg" in i.lower()]
    logo=[i for i in imgs if isinstance(i,str) and "logo" in i.lower()]
    data=[i for i in imgs if isinstance(i,str) and i.startswith("data:")]
    print(f"  {slug:26} imgs={len(imgs):3} svg={len(svg):3} logo-named={len(logo):2} data-uri={len(data):2}")

# ---------------------------------------------------------------------------
section("7. branding — fields beyond colors/fonts/scheme (already used)")
for slug,pd,d in homepages:
    b=d.get("branding",{}) or {}
    if not b: print(f"  {slug:26} (no branding)"); continue
    fonts=b.get("fonts",[]) or []
    colors=b.get("colors",[]) or []
    pers=b.get("personality")
    typo=b.get("typography")
    spac=b.get("spacing")
    comps=b.get("components")
    conf=b.get("confidence")
    print(f"  {slug:26} fonts={len(fonts)} colors={len(colors)} personality={'Y' if pers else '-'} "
          f"typo={'Y' if typo else '-'} spacing={'Y' if spac else '-'} components={'Y' if comps else '-'} conf={conf}")
