#!/usr/bin/env python3
"""Probe 1 — logomark resolution audit (BACKLOG: multi-ratio logo set).

For each telehealth competitor, measure the ACTUAL pixel size of every square-mark
candidate, so we can decide whether a reliable >=128px "deck-quality" logomark exists
and which source wins:

  - Google s2 favicon API at sz=256   (the BACKLOG-named source; check what it REALLY returns)
  - apple-touch-icon / high-res <link rel=icon>  (parsed offline from cached rawHtml)
  - metadata.favicon                  (Firecrawl's parsed favicon == what `branding` sees)
  - current logo_url                   (what the store ships today — the delta)

No network to the bot-walled HTML: icon links come from cached .payloads rawHtml.
Only the image bytes are fetched (static hosts, rarely walled). Dims via macOS `sips`.
"""
import json, glob, re, subprocess, os, urllib.parse, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "_out")
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
BAR = 128  # deck-quality threshold (px on the short side)

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

def sips_dims(path):
    try:
        r = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
                           capture_output=True, text=True, timeout=20)
        w = re.search(r"pixelWidth:\s*(\d+)", r.stdout)
        h = re.search(r"pixelHeight:\s*(\d+)", r.stdout)
        if w and h:
            return int(w.group(1)), int(h.group(1))
    except Exception:
        pass
    return None

_cache = {}
def measure(url):
    """Download url, return (w, h, bytes) or None. Cached by url."""
    if not url:
        return None
    if url in _cache:
        return _cache[url]
    dest = os.path.join(OUT, hashlib.md5(url.encode()).hexdigest()[:16])
    res = None
    try:
        subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url, "-o", dest],
                       capture_output=True, timeout=30)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            dims = sips_dims(dest)
            if dims:
                res = (dims[0], dims[1], os.path.getsize(dest))
    except Exception:
        pass
    _cache[url] = res
    return res

def gather(slug, domain):
    """From cached payloads: icon <link> urls, metadata.favicon, ogImage."""
    icons, meta_fav, og = set(), None, None
    for f in sorted(glob.glob(os.path.join(ROOT, f"store/{slug}/captures/*/.payloads/*.json"))):
        try:
            data = json.load(open(f)).get("data", {})
        except Exception:
            continue
        md = data.get("metadata", {}) or {}
        meta_fav = meta_fav or md.get("favicon")
        og = og or md.get("ogImage") or md.get("og:image")
        rh = data.get("rawHtml") or ""
        for tag in re.findall(r"<link\b[^>]*>", rh, re.I):
            if not re.search(r'rel=["\']?[^"\'>]*icon', tag, re.I):
                continue
            href = re.search(r'href=["\']([^"\']+)["\']', tag)
            if not href:
                continue
            sizes = re.search(r'sizes=["\']([^"\']+)["\']', tag)
            apple = bool(re.search(r"apple-touch-icon", tag, re.I))
            u = urllib.parse.urljoin(f"https://{domain}/", href.group(1))
            icons.add((u, sizes.group(1) if sizes else "", apple))
    return icons, meta_fav, og

def logo_url_of(slug):
    p = os.path.join(ROOT, f"store/{slug}/profile.md")
    try:
        for line in open(p):
            if line.startswith("logo_url:"):
                return line.split(":", 1)[1].split("#")[0].strip() or None
    except Exception:
        pass
    return None

rows = []
for slug, domain in COHORT:
    icons, meta_fav, og = gather(slug, domain)
    google = f"https://www.google.com/s2/favicons?domain={domain}&sz=256"
    g = measure(google)

    # best apple-touch / hi-res square icon by measured short-side, square-ish only
    best_apple = None  # (short, w, h, url, declared)
    for u, declared, apple in icons:
        m = measure(u)
        if not m:
            continue
        w, h, _ = m
        if min(w, h) == 0 or max(w, h) / min(w, h) > 1.3:  # skip wide/banner shapes
            continue
        short = min(w, h)
        if best_apple is None or short > best_apple[0]:
            best_apple = (short, w, h, u, declared, apple)

    mf = measure(meta_fav)
    cur = logo_url_of(slug)
    cm = measure(cur)

    # winner among square candidates
    cands = []
    if g: cands.append(("google256", min(g[0], g[1]), g))
    if best_apple: cands.append(("apple-touch" if best_apple[5] else "link-icon",
                                  best_apple[0], (best_apple[1], best_apple[2], 0)))
    if mf: cands.append(("meta.favicon", min(mf[0], mf[1]), mf))
    win = max(cands, key=lambda c: c[1]) if cands else None

    rows.append(dict(
        slug=slug, domain=domain,
        google=(g and f"{g[0]}x{g[1]}") or "fail",
        google_short=(min(g[0], g[1]) if g else 0),
        apple=(best_apple and f"{best_apple[1]}x{best_apple[2]}") or "—",
        apple_short=(best_apple[0] if best_apple else 0),
        apple_declared=(best_apple[4] if best_apple else ""),
        meta_fav=(mf and f"{mf[0]}x{mf[1]}") or "—",
        cur=(cm and f"{cm[0]}x{cm[1]}") or ("(empty)" if not cur else "fail"),
        cur_short=(min(cm[0], cm[1]) if cm else 0),
        win_src=(win[0] if win else "NONE"),
        win_px=(win[1] if win else 0),
        pass128=bool(win and win[1] >= BAR),
        og=(og or "—"),
    ))

# ---- report ----
def col(s, n):
    s = str(s); return s[:n].ljust(n)

print(f"\nPROBE 1 — logomark resolution audit  (deck-quality bar = short side >= {BAR}px)\n")
hdr = ["competitor", "google256", "appleTch", "metaFav", "today", "WINNER", "px", "ok?"]
widths = [18, 11, 11, 9, 9, 13, 6, 4]
print("  ".join(col(h, w) for h, w in zip(hdr, widths)))
print("  ".join("-" * w for w in widths))
for r in rows:
    print("  ".join([
        col(r["slug"].replace("-com", "").replace("-", "."), 18),
        col(r["google"], 11), col(r["apple"], 11), col(r["meta_fav"], 9),
        col(r["cur"], 9), col(r["win_src"], 13), col(r["win_px"], 6),
        col("YES" if r["pass128"] else "no", 4),
    ]))

n = len(rows)
npass = sum(r["pass128"] for r in rows)
from collections import Counter
wins = Counter(r["win_src"] for r in rows)
gpass = sum(r["google_short"] >= BAR for r in rows)
apass = sum(r["apple_short"] >= BAR for r in rows)
print(f"\nSUMMARY ({n} competitors):")
print(f"  clear {BAR}px deck-quality bar (any source): {npass}/{n}")
print(f"  google s2 sz=256 alone >= {BAR}px:           {gpass}/{n}")
print(f"  apple-touch/link-icon alone >= {BAR}px:       {apass}/{n}")
print(f"  winning source: " + ", ".join(f"{k}={v}" for k, v in wins.most_common()))
print(f"  google s2 actual short-side distribution: " +
      ", ".join(f"{r['domain']}={r['google_short']}" for r in rows))

json.dump(rows, open(os.path.join(HERE, "results.json"), "w"), indent=2)
print(f"\nwrote results.json ({n} rows); images in _out/ (gitignored)")
