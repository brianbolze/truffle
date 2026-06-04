"""Probe: can we extract a usable HERO PRODUCT RENDER from a persisted offerings capture,
with zero new Firecrawl spend? Tests (1) candidate sourcing, (2) a path-heuristic selector,
(3) the download step against the Hims CDN. Throwaway — experiments/ is house-style exempt."""
import json, os, re, sys, urllib.request

P = "store/hims-com/captures/2026-06-03/.payloads"

# path tokens that mark NOISE (icons, chrome, social cards, before/after)
NEG = re.compile(r"(f_svg|\.svg|/footer/|navigation|nav-|qr-code|/testimonials/|-BA-|-Before|-After"
                 r"|-SEO-|-Share|/logo|logo-|/icons?/)", re.I)
# path tokens that mark a real PRODUCT RENDER
POS = re.compile(r"(/products?/|/pdps?/|/storefront/|Float|-product|-pill|-pen|vial|bottle|device|kit)", re.I)
WIDTH = re.compile(r"[/_]w_(\d{2,4})")

def width(u):
    m = WIDTH.search(u); return int(m.group(1)) if m else 0

def score(u):
    s = 0.0
    if NEG.search(u): s -= 10
    if POS.search(u): s += 5
    w = width(u)
    s += min(w, 1200) / 400.0          # bigger = more hero-like, capped
    if "f_svg" in u: s -= 5            # belt-and-suspenders on icons
    return s

def candidates(data):
    imgs = list(data.get("images") or [])
    og = (data.get("metadata") or {}).get("og:image")
    return imgs, og

def rank(name):
    data = json.load(open(os.path.join(P, name), encoding="utf-8"))
    data = data.get("data", data)
    imgs, og = candidates(data)
    print(f"\n===== {name} =====  images[]={len(imgs)}  og:image={'yes' if og else 'no'}")
    ranked = sorted({u for u in imgs}, key=score, reverse=True)
    for u in ranked[:6]:
        print(f"  {score(u):+5.1f}  w={width(u):>4}  {u[-90:]}")
    if og:
        print(f"  [og:image fallback]  {og[-90:]}")
    return ranked[0] if ranked else og

def try_download(url, dest):
    # recipe §5.5 uses urllib; test whether the CDN serves us without browser headers
    try:
        urllib.request.urlretrieve(url, dest)
        return f"OK {os.path.getsize(dest)} bytes -> {dest}"
    except Exception as e:
        # retry with a UA header (the lean fallback if the bare fetch is blocked)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
                f.write(r.read())
            return f"OK-with-UA {os.path.getsize(dest)} bytes -> {dest}"
        except Exception as e2:
            return f"FAIL bare={type(e).__name__}:{e} | UA={type(e2).__name__}:{e2}"

if __name__ == "__main__":
    top_cat = rank("weight-loss-category.json")          # rich --homepage page (98 imgs)
    top_pdp = rank("ed-sildenafil.json")                 # lean PDP (og:image only)
    print("\n--- download test (top pick from the rich category page) ---")
    os.makedirs("experiments/2026-06-03-offerings-images/out", exist_ok=True)
    print(try_download(top_cat, "experiments/2026-06-03-offerings-images/out/hero-cat.png"))
