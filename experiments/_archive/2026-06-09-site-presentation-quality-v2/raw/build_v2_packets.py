#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "experiments/2026-06-09-site-presentation-quality-v2/packets"

COMPANIES = [
    ("Function Health", "functionhealth.com", "functionhealth-com"),
    ("Hone Health", "honehealth.com", "honehealth-com"),
    ("Ro", "ro.co", "ro-co"),
    ("Nurx", "nurx.com", "nurx-com"),
    ("Geviti", "gogeviti.com", "gogeviti-com"),
    ("Amble", "joinamble.com", "joinamble-com"),
    ("Hallandale", "hallandalerx.com", "hallandalerx-com"),
    ("Belmar Pharma Solutions", "belmarpharmasolutions.com", "belmarpharmasolutions-com"),
    ("Pepti", "hellopepti.com", "hellopepti-com"),
]

KEY_PAGE_LIMIT = 3


def load_payload(path: Path):
    with path.open() as f:
        return json.load(f).get("data", {})


def screenshot_dims(path: Path):
    if not path.exists():
        return "missing"
    try:
        out = subprocess.check_output(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return "unknown"
    vals = {}
    for line in out.splitlines():
        line = line.strip()
        if ":" in line:
            k, v = line.split(":", 1)
            vals[k.strip()] = v.strip()
    if "pixelWidth" in vals and "pixelHeight" in vals:
        return f"{vals['pixelWidth']} x {vals['pixelHeight']}"
    return "unknown"


def latest_home_capture(slug):
    base = ROOT / "store" / slug / "captures"
    candidates = []
    for path in base.iterdir():
        if not path.is_dir() or path.name.startswith("_"):
            continue
        if (path / ".payloads/homepage.json").exists():
            candidates.append(path)
    if not candidates:
        raise FileNotFoundError(f"No homepage payload for {slug}")
    return sorted(candidates, key=lambda p: p.name)[-1]


def page_payloads(capture_dir):
    payloads = []
    for json_path in sorted((capture_dir / ".payloads").glob("*.json")):
        if json_path.name.startswith("map") or json_path.name == "manifest.json":
            continue
        png_path = json_path.with_suffix(".png")
        if png_path.exists():
            payloads.append((json_path.stem, json_path, png_path))
    payloads.sort(key=lambda row: (row[0] != "homepage", row[0]))
    return payloads


def pick_key_pages(payloads):
    preferred = [
        "pricing",
        "membership",
        "membership-pricing",
        "our_services",
        "products",
        "weight-loss",
        "weight_management",
        "how-it-works",
        "how_it_works",
        "about",
        "team",
        "clinicians",
        "providers",
        "quality",
        "faq",
    ]
    by_name = {name: row for name, *row in payloads if name != "homepage"}
    picked = []
    for name in preferred:
        if name in by_name:
            picked.append((name, *by_name[name]))
        if len(picked) >= KEY_PAGE_LIMIT:
            return picked
    for name, json_path, png_path in payloads:
        if name != "homepage" and name not in {p[0] for p in picked}:
            picked.append((name, json_path, png_path))
        if len(picked) >= KEY_PAGE_LIMIT:
            break
    return picked


def meta_value(meta, *keys):
    for key in keys:
        val = meta.get(key)
        if val:
            return val
    return ""


def metadata_summary(data):
    meta = data.get("metadata") or {}
    return {
        "title": meta_value(meta, "title", "ogTitle", "og:title"),
        "description": meta_value(meta, "description", "ogDescription", "og:description"),
        "og_title": meta_value(meta, "ogTitle", "og:title"),
        "og_description": meta_value(meta, "ogDescription", "og:description"),
        "og_image": meta_value(meta, "ogImage", "og:image", "twitter:image"),
        "canonical": meta_value(meta, "canonical", "ogUrl", "og:url", "url", "sourceURL"),
        "source_url": meta.get("sourceURL") or "",
        "status_code": meta.get("statusCode", ""),
        "favicon": meta.get("favicon") or "",
    }


def stack_hints(raw):
    checks = [
        ("Next.js", ["__NEXT_DATA__", "/_next/"]),
        ("Gatsby", ["___gatsby", "/page-data/", "gatsby-"]),
        ("Webflow", ["data-wf-", "website-files.com"]),
        ("WordPress", ["wp-content", "wp-json", "woocommerce", "elementor"]),
        ("Shopify", ["cdn.shopify.com", "Shopify.theme", "myshopify.com"]),
        ("Drupal", ["Drupal.settings", "data-drupal-", "/sites/default/files/", "/themes/custom/", "/modules/custom/"]),
        ("React/Vite SPA", ["/assets/index-", "vite", "data-reactroot", "__vite"]),
    ]
    hits = []
    lowered = raw.lower()
    for label, needles in checks:
        if any(n.lower() in lowered for n in needles):
            hits.append(label)
    return hits or ["none detected cheaply"]


def route_hints(home_data, page_rows):
    urls = []
    for _, json_path, _ in page_rows:
        data = load_payload(json_path)
        meta = data.get("metadata") or {}
        url = meta.get("sourceURL") or meta.get("url")
        if url:
            urls.append(url)
    links = home_data.get("links") or []
    parsed_links = []
    for link in links:
        href = link.get("href") if isinstance(link, dict) else link
        text = (link.get("text") if isinstance(link, dict) else "") or ""
        if not href:
            continue
        parsed_links.append((href, text))
    structural_words = [
        "pricing",
        "membership",
        "services",
        "products",
        "treatments",
        "about",
        "team",
        "clinicians",
        "providers",
        "how",
        "faq",
        "quality",
        "contact",
    ]
    structural = []
    noisy = []
    for href, text in parsed_links[:500]:
        hay = f"{href} {text}".lower()
        if any(word in hay for word in structural_words):
            structural.append(href)
        if any(word in hay for word in ["blog", "article", "learn", "press", "campaign", "lp", "utm"]):
            noisy.append(href)
    def compact(items, limit=12):
        seen = []
        for item in items:
            parsed = urlparse(item)
            path = parsed.path or item
            if parsed.netloc and parsed.netloc not in {"", urlparse(home_data.get("metadata", {}).get("sourceURL", "")).netloc}:
                path = item
            if path not in seen:
                seen.append(path)
            if len(seen) >= limit:
                break
        return seen
    return {
        "captured_urls": urls,
        "structural_link_hints": compact(structural),
        "noise_link_hints": compact(noisy, 8),
        "homepage_link_count": len(parsed_links),
    }


def branding_summary(data):
    branding = data.get("branding")
    if not branding:
        return "branding payload unavailable/null"
    colors = branding.get("colors") or {}
    fonts = branding.get("fonts") or []
    font_names = []
    for f in fonts[:8]:
        if isinstance(f, dict) and f.get("family"):
            font_names.append(f["family"])
    bits = []
    if branding.get("colorScheme"):
        bits.append(f"color scheme {branding['colorScheme']}")
    if colors:
        bits.append("colors " + ", ".join(f"{k}={v}" for k, v in colors.items() if v))
    if font_names:
        bits.append("fonts " + ", ".join(font_names))
    images = branding.get("images") or {}
    if images:
        bits.append("branding image hints " + ", ".join(k for k, v in images.items() if v))
    return "; ".join(bits) if bits else "branding payload present but thin"


def write_packet(name, domain, slug):
    capture = latest_home_capture(slug)
    payloads = page_payloads(capture)
    home_json = capture / ".payloads/homepage.json"
    home_png = capture / ".payloads/homepage.png"
    home_data = load_payload(home_json)
    home_meta = metadata_summary(home_data)
    raw = home_data.get("rawHtml") or ""
    key_pages = pick_key_pages(payloads)
    all_pages = [row for row in payloads if row[0] != "homepage"]
    routes = route_hints(home_data, payloads)

    def page_line(row):
        page_name, json_path, png_path = row
        data = load_payload(json_path)
        meta = metadata_summary(data)
        return (
            f"- `{page_name}` screenshot: `{png_path.relative_to(ROOT)}` "
            f"({screenshot_dims(png_path)}); source: `{meta['source_url'] or meta['canonical']}`; "
            f"status: `{meta['status_code']}`; title: `{meta['title'] or 'missing'}`"
        )

    lines = []
    lines.append(f"# V2 blind packet: {name}")
    lines.append("")
    lines.append("Do not use `profile.md`, Notion, Brian's rating, or prior evaluator output. Rate observable marketing-site presentation only.")
    lines.append("")
    lines.append("## Identity")
    lines.append("")
    lines.append(f"- Domain: `{domain}`")
    lines.append(f"- Store slug: `store/{slug}`")
    lines.append(f"- Primary cached capture: `{capture.relative_to(ROOT)}`")
    lines.append("")
    lines.append("## Screenshot Inputs")
    lines.append("")
    lines.append(f"- Homepage screenshot: `{home_png.relative_to(ROOT)}`")
    lines.append(f"- Homepage dimensions: `{screenshot_dims(home_png)}`")
    lines.append("- Key-page screenshots:")
    for row in key_pages:
        lines.append(page_line(row))
    lines.append("")
    lines.append("## Homepage Metadata")
    lines.append("")
    lines.append(f"- Title: `{home_meta['title'] or 'missing'}`")
    lines.append(f"- Meta description: `{home_meta['description'] or 'missing'}`")
    lines.append(f"- OG title present: `{'yes' if home_meta['og_title'] else 'no'}`")
    lines.append(f"- OG description present: `{'yes' if home_meta['og_description'] else 'no'}`")
    lines.append(f"- OG image present: `{'yes' if home_meta['og_image'] else 'no'}`")
    lines.append(f"- Canonical/source URL: `{home_meta['canonical'] or home_meta['source_url'] or 'missing'}`")
    lines.append(f"- HTTP status: `{home_meta['status_code'] or 'missing'}`")
    lines.append(f"- Favicon hint: `{home_meta['favicon'] or 'missing'}`")
    lines.append("")
    lines.append("## Key-Page Metadata Snapshot")
    lines.append("")
    for row in key_pages:
        page_name, json_path, _ = row
        data = load_payload(json_path)
        meta = metadata_summary(data)
        lines.append(
            f"- `{page_name}`: title=`{meta['title'] or 'missing'}`; "
            f"description=`{meta['description'] or 'missing'}`; "
            f"ogImage=`{'yes' if meta['og_image'] else 'no'}`; "
            f"canonical/source=`{meta['canonical'] or meta['source_url'] or 'missing'}`; "
            f"status=`{meta['status_code'] or 'missing'}`"
        )
    lines.append("")
    lines.append("## Stack / Web Operation Hints")
    lines.append("")
    lines.append("- Detected from cached homepage `rawHtml`; treat as a hint, not source-of-truth.")
    lines.append(f"- Framework/CMS hints: `{', '.join(stack_hints(raw))}`")
    lines.append(f"- Branding payload: {branding_summary(home_data)}")
    lines.append("")
    lines.append("## Route / Page-Structure Hints")
    lines.append("")
    lines.append(f"- Homepage link count in cached payload: `{routes['homepage_link_count']}`")
    lines.append("- Captured page source URLs:")
    for url in routes["captured_urls"]:
        lines.append(f"  - `{url}`")
    if routes["structural_link_hints"]:
        lines.append("- Structural route/link hints from homepage payload:")
        for item in routes["structural_link_hints"]:
            lines.append(f"  - `{item}`")
    if routes["noise_link_hints"]:
        lines.append("- Content/campaign/noise route hints from homepage payload:")
        for item in routes["noise_link_hints"]:
            lines.append(f"  - `{item}`")
    lines.append("- Other cached page screenshots in same capture:")
    others = [name for name, _, png in all_pages if png.exists() and name not in {p[0] for p in key_pages}]
    lines.append(f"  - `{', '.join(others) if others else 'none beyond selected key pages'}`")
    lines.append("")
    lines.append("## Media / Render / Design Cues To Check Visually")
    lines.append("")
    lines.append("- Media asset sophistication: inspect screenshots for commissioned photography/video, product renders, app screenshots, clinician/team imagery, generic stock imagery, icon-only/text-heavy pages, or AI/placeholder-looking assets.")
    lines.append("- Design-system consistency: inspect typography hierarchy, CTA/card/form polish, iconography consistency, spacing rhythm, and cross-page reuse.")
    lines.append("- Information architecture: inspect whether a visitor can quickly tell what is sold, for whom, and what the next action is.")
    lines.append("- Cross-page consistency: use key-page screenshots to check whether the homepage system holds beyond the homepage.")
    lines.append("- Render/capture caveats: inspect for cookie/consent overlays, sticky widgets, empty media blocks, broken image panels, clipped text/marquees, repeated overlays, or blank sections.")
    lines.append("")
    lines.append("## V2 Excellent Cap Reminder")
    lines.append("")
    lines.append("Only rate `excellent` when the site has both distinctiveness and execution discipline. Major placeholder blocks, low-contrast sections, broken media panels, repeated overlays, generic stock-template execution, or visibly unfinished sections usually cap at `strong`.")
    lines.append("")
    (OUT / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, domain, slug in COMPANIES:
        write_packet(name, domain, slug)


if __name__ == "__main__":
    main()
