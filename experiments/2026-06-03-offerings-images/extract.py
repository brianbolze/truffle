"""Generic hero-candidate extractor for the n>1 image probe. Platform-agnostic (no Hims-only tokens):
score every image in a site's rich payloads by URL-path signal + declared width, download the top-N
(headed request — bare fetch 403s on bot-defended CDNs) + og:image, normalize to PNG for vision review.
Writes sites/<slug>/manifest.json. Throwaway — experiments/ is house-style exempt."""
import json, os, re, glob, sys, subprocess, urllib.request
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

NEG = re.compile(r"(\.svg|f_svg|/icons?/|logo|/footer|/header|/nav|menu|/badge(?!.*product)|qr[-_]?code"
                 r"|testimonial|avatar|headshot|review|star|rating|trustpilot|/press|/blog|background|hero-bg"
                 r"|/og[-_]|[-_]og\b|[-_]seo[-_]|share[-_]|social|favicon|sprite|placeholder"
                 r"|visa|mastercard|amex|klarna|afterpay|paypal|hsa|fsa|payment|[-_]ba[-_]|before|after)", re.I)
POS = re.compile(r"(/products?/|/pdps?/|[-_/]pdp|product[-_]|[-_]product|bottle|vial|[-_]pill|[-_]pen\b|capsule"
                 r"|tablet|packaging|render|float|[-_]jar|[-_]box\b|tube|syringe|device|[-_]kit\b|sachet|vibe)", re.I)
WIDTH = re.compile(r"(?:[,/_]w[_=](\d{2,4}))|(?:[-_](\d{3,4})x\d{2,4})|(?:[-_]p[-_](\d{3,4}))")

def width(u):
    best = 0
    for m in WIDTH.finditer(u):
        best = max(best, *(int(g) for g in m.groups() if g))
    return best

def score(u):
    s = 0.0
    if NEG.search(u): s -= 10
    if POS.search(u): s += 5
    s += min(width(u), 1600) / 400.0
    if re.search(r"\.(svg|gif)(\?|$)", u, re.I): s -= 8
    return s

def rich_payloads(slug):
    dates = {}
    for jf in glob.glob(os.path.join(ROOT, "store", slug, "captures", "*", ".payloads", "*.json")):
        date = jf.split("/captures/")[1].split("/")[0]
        try:
            d = json.load(open(jf, encoding="utf-8")); d = d.get("data", d)
        except Exception:
            continue
        if d.get("images"):
            dates.setdefault(date, []).append((jf, d))
    if not dates: return []
    best_date = max(dates, key=lambda k: len(dates[k]))   # the run with the most rich pages
    return dates[best_date]

def gather(slug):
    imgs, ogs, hosts = {}, set(), {}
    for _, d in rich_payloads(slug):
        md = d.get("metadata") or {}
        src = md.get("sourceURL") or md.get("url") or ""
        host = urlparse(src).netloc
        for u in (d.get("images") or []):
            if u.startswith("http") and u not in imgs:
                imgs[u] = host
        og = md.get("og:image")
        if og and og.startswith("http"):
            ogs.add(og); hosts[og] = host
    return imgs, ogs, hosts

def download(url, referer, dest):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
               "Accept": "image/avif,image/webp,image/png,image/*,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.9"}
    for ref in ([referer] if referer else []) + [f"https://{urlparse(url).netloc}/"]:
        try:
            req = urllib.request.Request(url, headers={**headers, "Referer": ref})
            with urllib.request.urlopen(req, timeout=30) as r:
                b = r.read()
            if len(b) < 600:  # too tiny to be a real render
                return f"tiny:{len(b)}"
            with open(dest, "wb") as f:
                f.write(b)
            return "ok"
        except Exception as e:
            last = f"{type(e).__name__}"
    return f"fail:{last}"

def to_png(src, dst):
    try:
        subprocess.run(["sips", "-s", "format", "png", src, "--out", dst],
                       capture_output=True, timeout=30, check=True)
        return os.path.exists(dst)
    except Exception:
        return False

def run(slug, top_n=10):
    imgs, ogs, hosts = gather(slug)
    site_host = max(set(imgs.values()) | set(ogs and [hosts.get(o,"") for o in ogs]) | {""},
                    key=lambda h: list(imgs.values()).count(h)) if imgs else ""
    referer = f"https://{site_host}/" if site_host else None
    ranked = sorted(imgs, key=score, reverse=True)
    sdir = os.path.join(HERE, "sites", slug); raw = os.path.join(sdir, "raw"); png = os.path.join(sdir, "png")
    os.makedirs(raw, exist_ok=True); os.makedirs(png, exist_ok=True)
    entries = []
    picks = [("og", o) for o in list(ogs)[:2]] + [("r%02d" % i, u) for i, u in enumerate(ranked[:top_n], 1)]
    for tag, u in picks:
        rawp = os.path.join(raw, tag + ".bin"); st = download(u, referer, rawp)
        pngp = os.path.join(png, tag + ".png"); ok = (st == "ok") and to_png(rawp, pngp)
        entries.append({"tag": tag, "rank": (None if tag.startswith("og") else int(tag[1:])),
                        "score": round(score(u), 2), "width": width(u), "url": u,
                        "dl": st, "png": (os.path.relpath(pngp, ROOT) if ok else None)})
    manifest = {"slug": slug, "referer": referer, "n_images": len(imgs), "n_ranked": len(ranked),
                "entries": entries,
                "all_ranked_urls": [{"rank": i, "score": round(score(u), 2), "url": u}
                                    for i, u in enumerate(ranked[:40], 1)]}
    json.dump(manifest, open(os.path.join(sdir, "manifest.json"), "w"), indent=2)
    ok = sum(1 for e in entries if e["png"]); print(f"{slug:16} imgs={len(imgs):>4}  downloaded={ok}/{len(entries)}  host={site_host}")
    return manifest

if __name__ == "__main__":
    for slug in sys.argv[1:]:
        run(slug)
