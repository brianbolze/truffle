#!/usr/bin/env python3
"""Probe 2 — wordmark fill (BACKLOG: multi-ratio logo set).  [v3 — trustworthy sources]

v1 scanned only the <head> (missed SPA bodies). v2 scanned the whole doc and "picked widest"
— which grabbed press/endorser/payment logos (NYT, TIME100, Afterpay, Airbnb, Mark Manson, a
Zendesk asset). LESSON: a naive image scan can't tell a brand wordmark from a logo wall.

v3 trusts only sources that are vetted or provably on-brand:
  HOSTABLE = the pre-vetted `logo_url` (real on-domain mark, not a favicon)         -> store the url
           , else on-domain JSON-LD `logo` that isn't a share/og banner.
  EXTRACT  = no hostable mark; the wordmark ships as inline <svg> or a data-URI       -> Tier-2 asset
             (mechanism noted: data-uri | inline-svg | client-rendered).
A wordmark is aspect >= 1.5 (excludes square marks like Hone's TriangleWhite).
Also re-prints what a naive widest-image scan WOULD have grabbed, as the cautionary record.
"""
import json, glob, re, subprocess, os, urllib.parse, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "_out")
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

COHORT = [
    ("hims-com", "hims.com"), ("ro-co", "ro.co"), ("lifemd-com", "lifemd.com"),
    ("maximustribe-com", "maximustribe.com"), ("honehealth-com", "honehealth.com"),
    ("getpetermd-com", "getpetermd.com"), ("remedymeds-com", "remedymeds.com"),
    ("joiandblokes-com", "joiandblokes.com"), ("agelessrx-com", "agelessrx.com"),
    ("gogeviti-com", "gogeviti.com"), ("mylifeforce-com", "mylifeforce.com"),
    ("gethealthspan-com", "gethealthspan.com"), ("marekhealth-com", "marekhealth.com"),
    ("functionhealth-com", "functionhealth.com"), ("eden-health", "eden.health"),
    ("onemedical-com", "onemedical.com"),
]
LOGOMARK_MISS = {"agelessrx-com", "gogeviti-com", "marekhealth-com"}
FAVISH = re.compile(r"favicon|apple-touch|/fav|-fav\b|icon-\d{2,}", re.I)

def is_favicon(u):
    # a filename with logo/wordmark/brand is the mark, even if it lives in an /icons/ dir
    if re.search(r"logo|wordmark|brand", u, re.I):
        return False
    return bool(FAVISH.search(u))
SHARE = re.compile(r"share|og[-_]?image|ogimage|[-_]fb[-_.]|facebook|twitter|social|seo[-_]|open_graph", re.I)

def registrable(host):
    p = host.split(".")
    return ".".join(p[-2:]) if len(p) >= 2 else host

def sips_dims(path):
    try:
        r = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
                           capture_output=True, text=True, timeout=20)
        w = re.search(r"pixelWidth:\s*(\d+)", r.stdout); h = re.search(r"pixelHeight:\s*(\d+)", r.stdout)
        if w and h: return int(w.group(1)), int(h.group(1))
    except Exception: pass
    return None

def svg_aspect(text):
    m = re.search(r'viewBox=["\']\s*[\d.\-]+\s+[\d.\-]+\s+([\d.]+)\s+([\d.]+)', text)
    if m and float(m.group(2)) > 0:
        return float(m.group(1)), float(m.group(2)), float(m.group(1)) / float(m.group(2))
    return None

_cache = {}
def measure(url):
    if url in _cache: return _cache[url]
    dest = os.path.join(OUT, "v3_" + hashlib.md5(url.encode()).hexdigest()[:14])
    res = None
    try:
        subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url, "-o", dest],
                       capture_output=True, timeout=30)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            raw = open(dest, "rb").read()
            if b"<svg" in raw[:6000] or url.lower().split("?")[0].endswith(".svg"):
                res = svg_aspect(raw.decode("utf-8", "ignore"))
            else:
                d = sips_dims(dest)
                if d: res = (d[0], d[1], d[0] / d[1] if d[1] else 0)
    except Exception: pass
    _cache[url] = res
    return res

def logo_url_of(slug):
    try:
        for line in open(os.path.join(ROOT, f"store/{slug}/profile.md")):
            if line.startswith("logo_url:"):
                return (line.split(":", 1)[1].split("#")[0].strip() or None)
    except Exception: pass
    return None

def jsonld_logos(rh):
    out = []
    for blk in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', rh, re.S | re.I):
        out += re.findall(r'"logo"\s*:\s*"([^"]+)"', blk)
        out += re.findall(r'"logo"\s*:\s*\{[^}]*?"url"\s*:\s*"([^"]+)"', blk)
    return [u for u in out if u.startswith("http")]

def gap_mechanism(rh, domain):
    """No hostable mark — how does the wordmark actually ship?"""
    # brand-link wrapping a data-URI or inline svg
    if re.search(r'<img[^>]*(?:logo|brand)[^>]*src=["\']data:', rh, re.I) or \
       re.search(r'<a[^>]*(?:logo|brand|href=["\']/?["\'])[^>]*>.{0,300}?<img[^>]*src=["\']data:', rh, re.I | re.S):
        return "data-uri"
    if re.search(r'<svg[^>]*(?:logo|brand)', rh, re.I) or \
       re.search(r'<a[^>]*(?:logo|brand|aria-label=["\'][^"\']*home)[^>]*>.{0,200}?<svg', rh, re.I | re.S):
        return "inline-svg"
    return "client-rendered"

rows = []
naive_noise = []
for slug, domain in COHORT:
    rh = ""
    for f in sorted(glob.glob(os.path.join(ROOT, f"store/{slug}/captures/*/.payloads/*.json"))):
        try:
            d = json.load(open(f)).get("data", {})
        except Exception:
            continue
        if d.get("rawHtml"):
            rh = d["rawHtml"]; break

    cands = []  # (source, url, w, h, aspect)
    # 1. pre-vetted logo_url, on-domain, not a favicon
    cur = logo_url_of(slug)
    if cur and cur.startswith("http") and not is_favicon(cur):
        m = measure(cur)
        if m and m[2] >= 1.5:
            cands.append(("logo_url", cur, *m))
    # 2. on-domain JSON-LD logo, not a share/og banner
    for u in jsonld_logos(rh):
        host = urllib.parse.urlparse(u).netloc
        if registrable(host) == registrable(domain) and not SHARE.search(u):
            m = measure(u)
            if m and m[2] >= 1.5:
                cands.append(("jsonld", u, *m))

    if cands:
        best = cands[0]  # logo_url wins if present, else first on-domain jsonld
        cls, mech = "HOSTABLE", ""
        detail = f"{best[0]} {best[2]:.0f}x{best[3]:.0f} a={best[4]:.1f}"
        url = best[1]
    else:
        mech = gap_mechanism(rh, domain)
        cls, detail, url = "EXTRACT", mech, ""

    rows.append(dict(slug=slug, domain=domain, cls=cls, mech=mech, detail=detail,
                     url=url, cur=cur or "(empty)", miss=slug in LOGOMARK_MISS))

def col(s, n):
    s = str(s); return s[:n].ljust(n)

print("\nPROBE 2 v3 — wordmark fill  (HOSTABLE=store a url | EXTRACT=inline/data-uri, needs Tier-2 asset)\n")
hdr = ["competitor", "class", "best wordmark / gap mechanism", "miss?"]
w = [16, 9, 32, 7]
print("  ".join(col(h, x) for h, x in zip(hdr, w)))
print("  ".join("-" * x for x in w))
for r in rows:
    d = r["detail"] if r["cls"] == "HOSTABLE" else f"ships as: {r['mech']}"
    print("  ".join([col(r["domain"], 16), col(r["cls"], 9), col(d, 32),
                     col("MISS" if r["miss"] else "", 7)]))

from collections import Counter
host = sum(r["cls"] == "HOSTABLE" for r in rows)
ext = sum(r["cls"] == "EXTRACT" for r in rows)
mechs = Counter(r["mech"] for r in rows if r["cls"] == "EXTRACT")
n = len(rows)
print(f"\nSUMMARY ({n} competitors):")
print(f"  HOSTABLE wordmark url (store as-is):  {host}/{n}")
print(f"  EXTRACT (inline/data-uri/client):     {ext}/{n}  -> {dict(mechs)}")
print(f"  the 3 logomark-misses, covered by a hostable wordmark? "
      + ", ".join(f"{r['domain'].split('.')[0]}={r['cls']}" for r in rows if r["miss"]))
json.dump(rows, open(os.path.join(HERE, "results2.json"), "w"), indent=2)
print(f"\n  (cautionary: v2's naive 'widest image' picked these NON-brand logos —")
print("   hims=zdassets, agelessrx=NYT, function=TIME100, eden=afterpay, onemedical=airbnb, marek=mark-manson)")
print(f"\nwrote results2.json")
