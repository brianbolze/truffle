#!/usr/bin/env python3
"""Firecrawl capture helper for the /research-company verb.

Bakes in the firecrawl-capture.md §5 hazard knobs (maxAge:0 + location:US +
waitFor + the all-formats bundle), persists raw JSON + cleaned markdown +
screenshots into store/<slug>/captures/<date>/, and records a manifest for the
§5.1 md5-dedup + sourceURL verify. Mechanics only — no classification, no
profile-writing (that's the agent's enrichment job, per SCHEMA.md).

Usage:
  fc.py map    <url> --slug <slug> [--search TERM] [--limit 500] [--subdomains] [--date YYYY-MM-DD]
  fc.py scrape <url> --slug <slug> --name <name> [--homepage] [--images] [--wait 3500] [--proxy auto] [--date ...]
  fc.py hero    --slug <slug> --name <name> [--top 15] [--date ...]  # recall-first hero-image candidates to pick (opt-in asset, §1.1)
  fc.py verify  --slug <slug> [--date ...]  # scrapes: md5-dedup + sourceURL match; + lint profile.md once written
  fc.py spend   --slug <slug> [--date ...]  # this run's attributed cost, summed from per-call creditsUsed
  fc.py signals --slug <slug> [--name homepage] [--date ...]  # slice rawHtml's JSON-LD + nav region (step-7 hint read, free)
  fc.py credits                             # GET /v2/team/credit-usage — global headroom only (free, 0 credits)

verify runs at two points: pre-write (step 6) it checks scrape integrity; re-run post-write
(step 7) it also lints the written profile.md (leaked tool-call tags, ## Provenance, required
frontmatter keys). Exits nonzero if anything is wrong. Stdlib-only on purpose — no PyYAML.

Credit accounting: each billable call records its own billed credits to the manifest —
scrapes from the response's metadata.creditsUsed, map from its documented flat 1/call. `spend`
sums them for an attributable run total. We never diff the global balance: the key is shared,
so the delta is polluted by other projects' calls (the old "can't attribute" hedge). credits
stays only for pre-flight headroom.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

API = "https://api.firecrawl.dev/v2"
KEY = os.environ.get("FIRECRAWL_API_KEY")
if not KEY:
    with open(os.path.expanduser("~/.claude/settings.json"), encoding="utf-8") as f:
        settings = json.load(f)
    KEY = settings["env"]["FIRECRAWL_API_KEY"]
HDR = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

ROOT = Path(__file__).resolve().parents[3]  # skills/research-company/scripts/fc.py -> repo root
TODAY = datetime.date.today().isoformat()


def store(slug: str, date: str) -> Path:
    d = ROOT / "store" / slug / "captures" / date
    (d / ".payloads").mkdir(parents=True, exist_ok=True)
    return d


def append_manifest(d: Path, rec: dict[str, Any]) -> None:
    """One JSONL line per billable call — the per-run integrity + credit ledger.
    `kind` ("scrape"|"map") lets verify read scrape-only records and spend sum all."""
    with open(d / ".payloads" / "manifest.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


def post(endpoint: str, body: dict[str, Any]) -> dict[str, Any]:
    req = urllib.request.Request(f"{API}/{endpoint}", data=json.dumps(body).encode(), headers=HDR, method="POST")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def do_map(
    url: str,
    slug: str,
    search: str | None,
    limit: int,
    date: str,
    subdomains: bool = False,
) -> None:
    # includeSubdomains defaults FALSE: a docs/dev subdomain (developers./docs.)
    # otherwise swamps the map AND starves the marketing host's crawl — Cloudflare
    # surfaced 4 www URLs with it on, 460 with it off. --subdomains opts back in for
    # the rare signal subdomain (e.g. investors.), which the homepage also links (§5.3).
    body: dict[str, Any] = {
        "url": url,
        "limit": limit,
        "location": {"country": "US"},
        "includeSubdomains": subdomains,
    }
    if search:
        body["search"] = search
    out = post("map", body)
    links = out.get("links", out.get("data", []))
    d = store(slug, date)
    # Slugify search for the payload FILENAME: a `site:domain/path` term carries `/`
    # and `:` that otherwise land in the path and crash the write *after* post() already
    # billed the credit — a silent leak hit twice across the offerings runs. The print
    # below keeps the readable form via `search`, so nothing legible is lost.
    tag = f"map_{re.sub(r'[^A-Za-z0-9._-]+', '-', search)}" if search else "map"
    (d / ".payloads" / f"{tag}.json").write_text(json.dumps(out, indent=2))
    # map bills a flat 1 credit/call and returns no per-call creditsUsed — record
    # the documented constant so the manifest stays a complete spend ledger.
    append_manifest(
        d,
        {
            "kind": "map",
            "name": tag,
            "requested": url,
            "credits": 1,
            "urls": len(links),
        },
    )
    print(f"[map] {url}  search={search!r}  -> {len(links)} urls  (1 credit, saved {tag}.json)")
    for item in links[:600]:
        u = item.get("url") if isinstance(item, dict) else item
        print("   ", u)


def do_scrape(
    url: str,
    slug: str,
    name: str,
    homepage: bool,
    wait: int,
    proxy: str | None,
    images: bool,
    date: str,
) -> None:
    if homepage:
        formats = [
            "markdown",
            "html",
            "rawHtml",
            "links",
            "branding",
            "images",
            {"type": "screenshot", "fullPage": True},
        ]
        only_main = False
    else:
        formats = ["markdown", "links", {"type": "screenshot", "fullPage": True}]
        if images:
            formats.append("images")  # hero-capture: images[] rides the 1-credit base (§1.1)
        only_main = True
    body: dict[str, Any] = {
        "url": url,
        "formats": formats,
        "maxAge": 0,
        "location": {"country": "US", "languages": ["en-US"]},
        "waitFor": wait,
        "onlyMainContent": only_main,
    }
    if proxy:
        body["proxy"] = proxy
    t0 = time.time()
    out = post("scrape", body)
    dt = time.time() - t0
    data = out.get("data", {})
    md = data.get("markdown", "") or ""
    meta = data.get("metadata", {}) or {}
    src = meta.get("sourceURL") or meta.get("url")
    status = meta.get("statusCode")
    credits = meta.get("creditsUsed")  # per-call billed truth (1 base; +4 enhanced proxy; +1/PDF pg)
    proxy_used = meta.get("proxyUsed")
    md5 = hashlib.md5(md.encode()).hexdigest()
    d = store(slug, date)
    (d / ".payloads" / f"{name}.json").write_text(json.dumps(out, indent=2))
    (d / f"{name}.md").write_text(md)
    shot = data.get("screenshot")
    shot_ok = ""
    if shot:
        try:
            urllib.request.urlretrieve(shot, d / ".payloads" / f"{name}.png")
            shot_ok = "shot✓"
        except Exception as e:
            shot_ok = f"shot✗({e})"
    # append manifest line
    rec = {
        "kind": "scrape",
        "name": name,
        "requested": url,
        "sourceURL": src,
        "status": status,
        "md5": md5,
        "mdlen": len(md),
        "secs": round(dt, 1),
        "match": (src or "").rstrip("/") == url.rstrip("/"),
        "credits": credits,
        "proxy": proxy_used,
    }
    append_manifest(d, rec)
    flag = "" if rec["match"] else "  <-- sourceURL MISMATCH"
    cr = "?" if credits is None else credits
    print(f"[scrape] {name:28} status={status} cr={cr} mdlen={len(md):>6} {dt:4.1f}s md5={md5[:8]} {shot_ok}{flag}")
    print(f"         src={src}")
    if md and len(md) < 500:
        print("         !! THIN markdown (<500c) — possible SPA-blank / wall")


# --- profile.md lint (step-7 output) ---------------------------------------
# Required top-level frontmatter keys: identity + capture meta (never legitimately
# empty) plus the fields QUERYING.md's recipes read — keep in sync with
# scripts/querycheck.py's RECIPE_FIELDS. Optional fields (portfolio_shape, visual
# identity) are intentionally not required.
REQUIRED_FM_KEYS = [
    "schema_version",
    "domain",
    "name",
    "captured_at",
    "capture_method",
    "description",
    "entity_type",
    "target_market",
    "offering_category",
    "business_model",
    "parent",
    "owns",
    "key_pages",
    "unverified_fields",
]
# Leaked harness control tags — how </content> and </invoke> reached 4 profiles in
# the first batch. Targeted to the tool-call vocabulary so legit URL-template
# placeholders (<slug>, <sku>, <drug>) don't false-positive.
LEAK_RE = re.compile(r"</?\s*(?:antml:)?(?:function_calls|invoke|parameter|content)\b[^>]*>", re.I)


def frontmatter_keys(text: str) -> list[str] | None:
    """Top-level frontmatter keys via a column-0 line scan (stdlib-only — no PyYAML).
    Returns None if there's no leading '---' fence."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return [m.group(1) for line in parts[1].splitlines() if (m := re.match(r"([A-Za-z_][A-Za-z0-9_]*):", line))]


def lint_profile(slug: str) -> bool:
    """Lint the written store/<slug>/profile.md: no leaked tool-call tags, a
    ## Provenance section, and the required frontmatter keys. Returns True on issues.
    Absent profile (pre-write step 6) is not a failure — the lint just defers."""
    p = ROOT / "store" / slug / "profile.md"
    if not p.exists():
        print("  profile.md not yet written — lint deferred to the post-write verify")
        return False
    text = p.read_text()
    bad = False
    print(f"--- profile.md lint ({slug}) ---")
    for i, line in enumerate(text.splitlines(), 1):
        for m in LEAK_RE.finditer(line):
            print(f"  LEAKED TAG line {i}: {m.group(0)!r}  <-- strip it")
            bad = True
    if "## Provenance" not in text:
        print("  MISSING SECTION: ## Provenance")
        bad = True
    keys = frontmatter_keys(text)
    if keys is None:
        print("  no '---' frontmatter fence")
        bad = True
    else:
        missing = [k for k in REQUIRED_FM_KEYS if k not in keys]
        if missing:
            print(f"  MISSING FRONTMATTER KEYS: {', '.join(missing)}")
            bad = True
    print("  profile.md OK — no leaked tags, Provenance present, required keys present" if not bad else "  ^^ profile.md ISSUES above")
    return bad


def do_verify(slug: str, date: str) -> None:
    d = store(slug, date)
    bad = False
    # --- scrapes: sourceURL match + md5-uniqueness across the run ---
    mf = d / ".payloads" / "manifest.jsonl"
    if not mf.exists():
        print(f"=== verify {slug} ===")
        print("  no manifest — run scrapes first (skipping scrape checks)")
    else:
        recs = [json.loads(line) for line in mf.read_text().splitlines() if line.strip()]
        scrapes = [r for r in recs if r.get("kind", "scrape") == "scrape"]
        by_md5: dict[str, list[str]] = {}
        print(f"=== verify {slug} ({len(scrapes)} pages) ===")
        scrape_bad = False
        for r in scrapes:
            by_md5.setdefault(r["md5"], []).append(r["name"])
            if not r["match"]:
                print(f"  sourceURL MISMATCH: {r['name']}  requested={r['requested']} got={r['sourceURL']}")
                scrape_bad = True
        for md5, names in by_md5.items():
            if len(names) > 1:
                print(f"  DUP BODY md5={md5[:8]} across: {names}  <-- §5.1 contamination")
                scrape_bad = True
        print("  scrapes OK — all sourceURLs match, all bodies unique" if not scrape_bad else "  ^^ scrape ISSUES above")
        bad |= scrape_bad
    # --- the written dossier ---
    bad |= lint_profile(slug)
    if bad:
        sys.exit("verify: issues found (see above)")


def do_spend(slug: str, date: str) -> None:
    """This run's attributed cost — sum the per-call credits in the manifest.
    Authoritative because each line carries the credits that call itself billed
    (scrape: metadata.creditsUsed; map: flat 1) — not a diff of the shared global
    balance, which other projects' calls pollute. This is the run-summary number."""
    d = store(slug, date)
    mf = d / ".payloads" / "manifest.jsonl"
    print(f"=== spend {slug} ({date}) ===")
    if not mf.exists():
        print("  no manifest — nothing billable captured this run (0 credits)")
        return
    recs = [json.loads(line) for line in mf.read_text().splitlines() if line.strip()]
    total, unknown = 0, 0
    for r in recs:
        c = r.get("credits")
        proxy = r.get("proxy")
        extra = f"  ({proxy} proxy)" if proxy and proxy != "basic" else ""
        if c is None:
            mark, unknown = "?", unknown + 1
        else:
            mark, total = str(c), total + c
        print(f"  {r.get('kind', 'scrape'):7} {r.get('name', ''):26} {mark:>3}{extra}")
    note = "" if not unknown else f"   ({unknown} call(s) w/o reported credits — total is a floor)"
    print(f"  {'':7} {'TOTAL':26} {total:>3} credits{note}")


def do_credits() -> None:
    req = urllib.request.Request(f"{API}/team/credit-usage", headers=HDR)
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.load(r)
    print(json.dumps(out, indent=2))


# --- structured-layer slice (step-7 enrichment read) -----------------------
# Surfaces the two underused rawHtml regions enrichment reads as HINTS (confirm
# against the page/screenshot, never blind-trust — same discipline as branding):
# the JSON-LD identity graph + the <header>/<nav> region whose mega-nav hierarchy
# markdown flattens. Deterministic slice — grep + pretty-print, NOT extraction (no
# LLM / schema / reconciliation; the anti-Doro line holds). Reads the persisted
# homepage payload; spends nothing. SCHEMA.md "Structured layer" says what lands where.
NAV_KEEP_ATTR = re.compile(r"^(href|aria-controls|aria-haspopup|aria-expanded|aria-label|role)$", re.I)


def latest_payload(slug: str, name: str, date: str) -> tuple[Path | None, str | None]:
    """<name>.json under captures/<date>, else the most recent capture that has it
    (enrichment may run a day after capture, or replay an old one). -> (path|None, date)."""
    direct = ROOT / "store" / slug / "captures" / date / ".payloads" / f"{name}.json"
    if direct.exists():
        return direct, date
    cands = sorted((ROOT / "store" / slug / "captures").glob(f"*/.payloads/{name}.json"))
    if cands:
        return cands[-1], cands[-1].parents[1].name
    return None, None


def jsonld_blocks(raw: str) -> list[tuple[bool, Any]]:
    """Parsed ld+json blocks from rawHtml; tolerant — a malformed block yields (False, raw)."""
    out: list[tuple[bool, Any]] = []
    for b in re.findall(r"<script[^>]*application/ld\+json[^>]*>(.*?)</script>", raw, re.S | re.I):
        b = b.strip()
        try:
            out.append((True, json.loads(b)))
        except Exception:
            out.append((False, b))
    return out


def jsonld_types(obj: Any, acc: set[str]) -> None:
    """Every @type present (flatten @graph/lists) — a scan aid for the reader."""
    if isinstance(obj, list):
        for x in obj:
            jsonld_types(x, acc)
    elif isinstance(obj, dict):
        t = obj.get("@type")
        if isinstance(t, str):
            acc.add(t)
        elif isinstance(t, list):
            acc.update(x for x in t if isinstance(x, str))
        for v in obj.values():
            jsonld_types(v, acc)


def slim_nav(s: str) -> str:
    """Drop inline svg/style/script + attribute noise (Tailwind class-soup is the
    bulk), keep href + aria-* + role + tag structure — so the flyout hierarchy reads
    at a few KB, not tens, while its NESTING (the part markdown loses) survives."""
    s = re.sub(r"<svg\b.*?</svg>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<(style|script|template|noscript)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)

    def keep(m: re.Match[str]) -> str:
        tag, attrs = m.group(1), m.group(2) or ""
        kept = [f'{k}="{v}"' for k, v in re.findall(r'([\w:-]+)="([^"]*)"', attrs) if NAV_KEEP_ATTR.match(k)]
        return f"<{tag}" + (" " + " ".join(kept) if kept else "") + ">"

    s = re.sub(r'<([\w:-]+)((?:\s+[\w:-]+="[^"]*")*)\s*/?>', keep, s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r">\s+<", "><", s)
    return s.strip()


def nav_region(raw: str) -> tuple[str | None, str]:
    """The <header> region, else the first <nav>, slimmed. -> (selector|None, slim)."""
    for sel, pat in (("header", r"<header\b.*?</header>"), ("nav", r"<nav\b.*?</nav>")):
        m = re.search(pat, raw, re.S | re.I)
        if m:
            return sel, slim_nav(m.group(0))
    return None, ""


def do_signals(slug: str, name: str, date: str) -> None:
    p, used = latest_payload(slug, name, date)
    if p is None:
        sys.exit(f"signals: no {name}.json under store/{slug}/captures/* — capture the homepage first")
    data = json.loads(p.read_text())
    data = data.get("data", data)
    raw = data.get("rawHtml")
    print(f"=== signals {slug} ({name}.json, {used}) ===")
    print(
        "  HINT layer — confirm every value against the page/screenshot before it lands "
        "(self-authored: can be marketing-shaped, stale, or absent). SCHEMA 'Structured layer'."
    )
    if not raw:
        sys.exit(f"  no rawHtml in {name}.json — signals reads the homepage rich pass (only --homepage scrapes carry rawHtml)")
    blocks = jsonld_blocks(raw)
    print(f"\n## JSON-LD  ({len(blocks)} block(s))")
    if not blocks:
        print("  none — no application/ld+json on this homepage (it was absent on 11/43 sampled)")
    for i, (ok, obj) in enumerate(blocks, 1):
        if ok:
            types: set[str] = set()
            jsonld_types(obj, types)
            print(f"\n  --- block {i}  @type: {sorted(types)} ---")
            pretty = json.dumps(obj, indent=2, ensure_ascii=False)
            print("\n".join("  " + ln for ln in pretty.splitlines()))
        else:
            print(f"\n  --- block {i}  (unparseable JSON; first 200c) ---\n  {obj[:200]}")
    sel, nav = nav_region(raw)
    print("\n## Nav region")
    if not nav:
        print(
            "  no <header>/<nav> element — nav is in a bare div (marek-shaped). "
            "Rebuild Nav structure from the homepage screenshot (ground truth)."
        )
    else:
        a = len(re.findall(r"<a\b", nav))
        ac = len(re.findall(r"aria-controls", nav, re.I))
        hp = len(re.findall(r"aria-haspopup", nav, re.I))
        print(
            f"  selector=<{sel}>  {len(nav)}b  <a>={a} aria-controls={ac} aria-haspopup={hp}  "
            "(validate completeness vs the screenshot — a label present here != hierarchy captured)"
        )
        print("\n" + nav)


# --- hero product image (opt-in asset capture, §1.1) -----------------------
# Recall-first candidate surfacing for the Product-Rendering reference library:
# score a flagship PDP's images[] by URL-path signal, headed-download the top-N to
# a scratch dir, and let the capturing agent PICK the clean isolated render by
# LOOKING — vision does precision; the path-score only guarantees a hero is in the
# set, never that it's rank 1 (n=6 probe: site-level recall 5/5, rank-1 precision
# 3/5 — so always eyeball). og:image is a last-resort fallback (0/5 clean renders
# across the probe). Bare urlretrieve 403s on bot-defended image CDNs (§5.2) — fetch
# headed (Referer + browser UA). Rationale: experiments/2026-06-03-offerings-images/FINDINGS.md.
#
# The NEG list rejects only what is NEVER a product render. Note `/nav/` is a path
# SEGMENT, not the bare token `nav`: Webflow ships clean hero renders as `nav-<sku>.webp`,
# and a `nav` substring match destroyed those (the probe's worst recall miss). Precision
# (packaging-vs-render, lifestyle-with-product) is the agent's vision job, not the regex's.
HERO_NEG = re.compile(
    r"(\.svg|\.gif|f_svg|/icons?/|[-_]icon[-_./]|logo|/footer/|/header/|/nav/|/navigation/|navbar"
    r"|/menu/|qr[-_]?code|testimonial|avatar|headshot|[-_]review|[-_]stars?[-_]|rating|trustpilot"
    r"|/press/|/blog/|background|hero-bg|[-_]seo[-_]|[-_]share[-_]|/og[-_]|[-_]og\b|social|favicon"
    r"|sprite|placeholder|visa|mastercard|amex|klarna|afterpay|paypal|[-_]hsa[-_]|[-_]fsa[-_]"
    r"|payment|[-_]ba[-_]|[-_]before[-_]|[-_]after[-_])",
    re.I,
)
HERO_POS = re.compile(
    r"(/products?/|/pdps?/|[-_/]pdp|product[-_]|[-_]product|bottle|vial|[-_]pill|[-_]pen\b|capsule"
    r"|tablet|packaging|render|float|[-_]jar|[-_]box\b|tube|syringe|device|[-_]kit\b|sachet)",
    re.I,
)
HERO_WIDTH = re.compile(r"(?:[,/_]w[_=](\d{2,4}))|(?:[-_](\d{3,4})x\d{2,4})|(?:[-_]p[-_](\d{3,4}))")
HERO_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def hero_width(url: str) -> int:
    """Largest declared pixel width in the URL — Cloudinary `,w_499`, WordPress `-300x300`,
    Webflow `-p-500`. Bigger trends more hero-like; 0 when none is encoded."""
    widths = [int(g) for m in HERO_WIDTH.finditer(url) for g in m.groups() if g]
    return max(widths) if widths else 0


def hero_score(url: str) -> float:
    """Recall-first path score: hard-reject never-product assets, boost product tokens,
    nudge by width. Deliberately coarse — the agent's vision pass is the precision layer."""
    s = 0.0
    if HERO_NEG.search(url):
        s -= 10
    if HERO_POS.search(url):
        s += 5
    return s + min(hero_width(url), 1600) / 400.0


def hero_ext(blob: bytes) -> str | None:
    """Image type from magic bytes, so a 403/HTML error body never lands as a fake .png."""
    if blob.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if blob.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if blob[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if blob[:4] == b"RIFF" and blob[8:12] == b"WEBP":
        return "webp"
    return None


def fetch_image(url: str, referer: str | None) -> bytes | None:
    """Headed GET (browser UA + Referer) — bare urlretrieve 403s on bot-defended image
    CDNs (§5.2; the probe proved this across 6 hosts). Retries with the image host itself
    as Referer. None on failure / non-image body / a too-tiny (<600B) tracking pixel."""
    headers = {
        "User-Agent": HERO_UA,
        "Accept": "image/avif,image/webp,image/png,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    for ref in [r for r in (referer, f"https://{urlparse(url).netloc}/") if r]:
        try:
            req = urllib.request.Request(url, headers={**headers, "Referer": ref})
            with urllib.request.urlopen(req, timeout=30) as r:
                blob = r.read()
            if len(blob) >= 600 and hero_ext(blob):
                return blob
        except Exception:
            continue
    return None


def do_hero(slug: str, name: str, date: str, top_n: int) -> None:
    p, used = latest_payload(slug, name, date)
    if p is None:
        sys.exit(f"hero: no {name}.json under store/{slug}/captures/* — scrape the flagship PDP first (with --images)")
    data = json.loads(p.read_text())
    data = data.get("data", data)
    imgs = [u for u in (data.get("images") or []) if isinstance(u, str) and u.startswith("http")]
    meta = data.get("metadata") or {}
    og = meta.get("og:image")
    src = meta.get("sourceURL") or meta.get("url") or ""
    referer = f"https://{urlparse(src).netloc}/" if src else None
    print(f"=== hero {slug} ({name}.json, {used}) ===")
    print(
        "  RECALL-FIRST candidates — the agent PICKS the clean isolated render by LOOKING "
        "(Read each; the path-score only guarantees a hero is in the set, NOT at rank 1). "
        "og.* is FALLBACK-ONLY. Rationale: experiments/2026-06-03-offerings-images/FINDINGS.md."
    )
    if not imgs:
        if not og:
            sys.exit("  no images[] and no og:image — re-scrape the PDP with `fc.py scrape ... --images` (rides the 1-credit base)")
        print("  !! no images[] (lean scrape) — only the og:image fallback is available; re-scrape with --images for real candidates")
    outdir = store(slug, date) / ".payloads" / "hero" / name
    outdir.mkdir(parents=True, exist_ok=True)
    ranked = sorted(dict.fromkeys(imgs), key=hero_score, reverse=True)[:top_n]
    n_ok = 0
    for i, u in enumerate(ranked, 1):
        blob = fetch_image(u, referer)
        if not blob:
            print(f"  c{i:02} FETCH-FAIL  {u}")
            continue
        fp = outdir / f"c{i:02}.{hero_ext(blob)}"
        fp.write_bytes(blob)
        n_ok += 1
        print(f"  c{i:02} score={hero_score(u):+5.1f} w={hero_width(u):>4} {fp.relative_to(ROOT)}")
    if og and (blob := fetch_image(og, referer)):
        fp = outdir / f"og.{hero_ext(blob)}"
        fp.write_bytes(blob)
        print(f"  og  (fallback only)        {fp.relative_to(ROOT)}")
    print(f"\n  {n_ok}/{len(ranked)} candidates saved to {outdir.relative_to(ROOT)}/  (headed download)")
    print("  NEXT (agent): Read the candidates, pick the clean isolated product render, then promote the winner:")
    print(
        f"    mkdir -p store/{slug}/captures/{date}/images && cp {outdir.relative_to(ROOT)}/cNN.<ext> store/{slug}/captures/{date}/images/<sku>.<ext>"
    )
    print("  Reference that path from the flagship's ## Deep block. It is an ASSET, never a roster column.")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("map")
    m.add_argument("url")
    m.add_argument("--slug", required=True)
    m.add_argument("--search")
    m.add_argument("--limit", type=int, default=500)
    m.add_argument(
        "--subdomains",
        action="store_true",
        help="include subdomains (default: off — drops the docs/dev swamp, §5.3)",
    )
    m.add_argument("--date", default=TODAY)
    s = sub.add_parser("scrape")
    s.add_argument("url")
    s.add_argument("--slug", required=True)
    s.add_argument("--name", required=True)
    s.add_argument("--homepage", action="store_true")
    s.add_argument("--images", action="store_true", help="add the free `images` format (hero capture on a flagship PDP, §1.1)")
    s.add_argument("--wait", type=int, default=3500)
    s.add_argument("--proxy")
    s.add_argument("--date", default=TODAY)
    v = sub.add_parser("verify")
    v.add_argument("--slug", required=True)
    v.add_argument("--date", default=TODAY)
    sp = sub.add_parser("spend")
    sp.add_argument("--slug", required=True)
    sp.add_argument("--date", default=TODAY)
    sg = sub.add_parser("signals")
    sg.add_argument("--slug", required=True)
    sg.add_argument("--name", default="homepage", help="payload to slice (default: homepage)")
    sg.add_argument("--date", default=TODAY)
    h = sub.add_parser("hero")
    h.add_argument("--slug", required=True)
    h.add_argument("--name", required=True, help="flagship PDP payload to source (scraped with --images)")
    h.add_argument("--top", type=int, default=15, help="candidates to download (recall-first; headed download is free)")
    h.add_argument("--date", default=TODAY)
    sub.add_parser("credits")
    a = ap.parse_args()
    if a.cmd == "map":
        do_map(a.url, a.slug, a.search, a.limit, a.date, a.subdomains)
    elif a.cmd == "scrape":
        do_scrape(a.url, a.slug, a.name, a.homepage, a.wait, a.proxy, a.images, a.date)
    elif a.cmd == "verify":
        do_verify(a.slug, a.date)
    elif a.cmd == "spend":
        do_spend(a.slug, a.date)
    elif a.cmd == "signals":
        do_signals(a.slug, a.name, a.date)
    elif a.cmd == "hero":
        do_hero(a.slug, a.name, a.date, a.top)
    elif a.cmd == "credits":
        do_credits()


if __name__ == "__main__":
    main()
