#!/usr/bin/env python3
"""Firecrawl capture helper for the /research-company verb.

Bakes in the firecrawl-capture.md §5 hazard knobs (maxAge:0 + location:US +
waitFor + the all-formats bundle), persists raw JSON + cleaned markdown +
screenshots into store/<slug>/captures/<date>/, and records a manifest for the
§5.1 md5-dedup + sourceURL verify. Mechanics only — no classification, no
profile-writing (that's the agent's enrichment job, per SCHEMA.md).

Usage:
  fc.py map    <url> --slug <slug> [--search TERM] [--limit 500] [--subdomains] [--date YYYY-MM-DD]
  fc.py scrape <url> --slug <slug> --name <name> [--homepage] [--images] [--wait 3500] [--actions-json FILE] [--mobile] [--headers-json FILE] [--proxy auto] [--date ...]
  fc.py hero    --slug <slug> --name <name> [--top 15] [--date ...]  # recall-first hero-image candidates to pick (opt-in asset, §1.1)
  fc.py logos   --slug <slug> [--name homepage] [--wordmark URL|PATH] [--date ...]  # measure the multi-ratio mark set (opt-in, §1.2)
  fc.py verify  --slug <slug> [--date ...]  # scrapes: md5-dedup + sourceURL match + junk soft-404 gate; + lint profile.md once written (incl. logos:{} measurements)
  fc.py spend   --slug <slug> [--date ...]  # this run's attributed cost, summed from per-call creditsUsed
  fc.py signals --slug <slug> [--name homepage] [--date ...]  # slice rawHtml's JSON-LD + nav region (step-7 hint read, free)
  fc.py credits                             # GET /v2/team/credit-usage — global headroom only (free, 0 credits)

verify runs at two points: pre-write (step 6) it checks scrape integrity; re-run post-write
(step 7) it also lints the written profile.md (leaked tool-call tags, ## Provenance, required
frontmatter keys, and logos:{} slot measurements). Exits nonzero if anything is wrong. Stdlib-only
on purpose — no PyYAML.

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
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

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


# --- junk soft-404 guard (firecrawl-capture.md §5.6) ------------------------
# A page whose TITLE (or first heading) is *essentially* a "not found" message is a
# dead/guessed path — discard it. Deliberately STATUS-INDEPENDENT: a junk stub and a
# REAL §5.6 soft-404 (TeloLife /pricing renders full content at HTTP 404) are BOTH 404,
# so the status can't tell them apart — the page's own headline can (TeloLife's title is
# "Pricing — TeloLife", the stub's is "Not Found"/"404"). Anchored to the headline, NEVER
# a body scan: "...patients who have not found success..." (nurx) is legit mid-sentence
# copy a full-text grep would false-positive on. The dangerous case is a real-SIZED stub
# — ivyrx /pdp-glp1-oral-melts is 9.4 KB with a unique body, so it slips BOTH the thin
# guard and the md5-dedup; only its title gives it away. Validated across the corpus:
# 6/6 true-positive (incl. the 9 KB ivyrx/joinamble shells), 0 false-positive in ~1000 pages.
NOT_FOUND_RE = re.compile(
    r"^\s*(?:404\b"
    r"|(?:page|content)?\s*not\s+found\b"
    r"|page\s+(?:not\s+available|unavailable|does(?:n['’]| no)t\s+exist|can['’]?t\s+be\s+found)"
    r"|this\s+page\s+(?:does(?:n['’]| no)t\s+exist|is(?:n['’]t| not)\s+(?:available|found)|could\s+not\s+be\s+found)"
    r"|oops[!,. ])",
    re.I,
)


def first_heading(md: str) -> str | None:
    """The first markdown ATX heading's text — where a stub's '# Page not found' lands when
    the <title> is generic (goodlifemeds/granola). None if the body opens with no heading."""
    for line in md.splitlines():
        if m := re.match(r"#{1,6}\s+(.*)", line.strip()):
            return m.group(1).strip()
    return None


def is_not_found(title: str | None, md: str) -> bool:
    """True when the page ANNOUNCES itself as not-found in its title or first heading — the
    junk-stub signature. Keeps a real §5.6 soft-404 (a real title served at HTTP 404), which
    is the whole reason this anchors on the headline and not the status code."""
    if title and NOT_FOUND_RE.match(title.strip()):
        return True
    head = first_heading(md)
    return bool(head and NOT_FOUND_RE.match(head))


def do_scrape(
    url: str,
    slug: str,
    name: str,
    homepage: bool,
    wait: int,
    proxy: str | None,
    images: bool,
    date: str,
    actions_json: str | None = None,
    mobile: bool = False,
    headers_json: str | None = None,
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
    if actions_json:
        with open(actions_json, encoding="utf-8") as f:
            actions = json.load(f)
        if not isinstance(actions, list):
            raise SystemExit("--actions-json must point to a JSON array of Firecrawl scrape actions")
        body["actions"] = actions
    if mobile:
        body["mobile"] = True
    if headers_json:
        with open(headers_json, encoding="utf-8") as f:
            headers = json.load(f)
        if not isinstance(headers, dict):
            raise SystemExit("--headers-json must point to a JSON object of request headers")
        body["headers"] = headers
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
    title = meta.get("title")
    not_found = is_not_found(title, md)
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
        "not_found": not_found,
        "credits": credits,
        "proxy": proxy_used,
        "actions": bool(actions_json),
        "mobile": mobile,
        "headers": bool(headers_json),
    }
    append_manifest(d, rec)
    flag = "" if rec["match"] else "  <-- sourceURL MISMATCH"
    cr = "?" if credits is None else credits
    print(f"[scrape] {name:28} status={status} cr={cr} mdlen={len(md):>6} {dt:4.1f}s md5={md5[:8]} {shot_ok}{flag}")
    print(f"         src={src}")
    if md and len(md) < 500:
        print("         !! THIN markdown (<500c) — possible SPA-blank / wall")
    if not_found:
        print(f"         !! NOT-FOUND stub — title={title!r} at HTTP {status}: a dead/guessed path,")
        print(f"            NOT page content (§5.6 junk soft-404). Drop {name}.md — verify gates on it.")


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
# placeholders (<slug>, <sku>, <drug>) don't false-positive. MIRROR of
# scripts/storelint.py's LEAK_RE (duplicated across the skill boundary so fc.py
# stays self-contained + stdlib-only) — change both together.
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


# Per-slot measurement requirements for the opt-in logos:{} module (SCHEMA §Logos-lint).
# The measurement IS the fact a slide/Notion consumer gates on, so a RECORDED slot must carry it —
# a sizeless mark is decoration, not state. A slot may be omitted (true absence); an absent or
# empty (`logos: {}`) block means the module didn't run (predates 2.5), so the check stays silent.
LOGO_SLOT_KEYS = {"wordmark": ("w", "h"), "logomark": ("px", "transparent"), "og": ("w", "h")}


def logo_issues(frontmatter: str) -> list[str]:
    """Slots present in a `logos:{}` block must carry their measurements. Returns one string
    per sizeless slot; [] when there's no block, an empty block, or every recorded slot is measured.

    Fires only on a slot LINE that's actually present (`wordmark: { ... }`) — omitting a slot is
    legal. Body is a single-line inline dict, so a `[^}]*` span + a per-key `\\b<key>:` scan suffices
    (the `src` URL's `?w=1200` uses `=`, never `:`, so it can't satisfy a `w:`/`h:` requirement)."""
    issues: list[str] = []
    for slot, required in LOGO_SLOT_KEYS.items():
        m = re.search(rf"^\s{{2,}}{slot}:\s*\{{([^}}]*)\}}", frontmatter, re.M)
        if not m:
            continue
        body = m.group(1)
        missing = [k for k in required if not re.search(rf"\b{k}:", body)]
        if missing:
            issues.append(f"logos.{slot} recorded without {', '.join(missing)} — the measurement is the fact (SCHEMA §Logos-lint)")
    return issues


def lint_profile(slug: str) -> bool:
    """Lint the written store/<slug>/profile.md: no leaked tool-call tags, a
    ## Provenance section, the required frontmatter keys, and — when a logos:{} block is
    present — its per-slot measurements (§Logos-lint). Returns True on issues.
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
        for issue in logo_issues(text.split("---", 2)[1]):
            print(f"  LOGOS: {issue}")
            bad = True
    print("  profile.md OK — no leaked tags, Provenance present, required keys + logo measurements present" if not bad else "  ^^ profile.md ISSUES above")
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
        # --- junk soft-404 stubs (§5.6): the page declared itself not-found in its
        # title/heading. The LATEST record per name wins (a re-scrape that resolved to
        # real content clears it); a still-flagged page whose .md is on disk is unresolved
        # junk poisoning the capture — the 404 fact lives in `status` + the screenshot +
        # prose, never the nav-shell body, so the fix is to drop the .md (true for a
        # deliberate "dead SKU" finding too: roster it in prose, don't keep the stub file).
        latest: dict[str, dict[str, Any]] = {}
        for r in scrapes:
            latest[r["name"]] = r  # append-ordered manifest -> last write per name wins
        for name, r in latest.items():
            if r.get("not_found") and (d / f"{name}.md").exists():
                print(
                    f"  JUNK SOFT-404: {name}  (HTTP {r.get('status')}, title declares not-found)  <-- §5.6 dead/guessed path; rm {name}.md"
                )
                scrape_bad = True
        print("  scrapes OK — all sourceURLs match, all bodies unique, no junk soft-404s" if not scrape_bad else "  ^^ scrape ISSUES above")
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
    if isinstance(og, list):  # og:image can repeat — fetch_image wants one URL string
        og = next((u for u in og if isinstance(u, str) and u.startswith("http")), None)
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


# --- logos module (opt-in: the multi-ratio brand-mark set, §1.2) ------------
# Measures the deterministic source chains so the agent never hand-counts pixels:
#   logomark = the larger MEASURED short side of {google s2/favicons sz=256, apple-touch-icon}
#   og       = the DECLARED og:image, gated at >=600px actual width (the meta size lies — Probe 3)
#   wordmark = the SVG/raster the AGENT chose (--wordmark) — vision picks it; a blind scan grabs
#              press logos (Probe 2). fc.py only MEASURES what it's handed, never selects it.
# sips reads raster px (stdlib subprocess — never PIL, the design's no-image-dep line); an SVG's box
# is parsed from its text (sips can't read vector). `transparent` stays the agent's eyes on a checker
# tile (hasAlpha lies — Probe 3). Candidates land in .payloads/logos/ for that eyeball; only an
# extracted-SVG wordmark is COMMITTED (to store/<slug>/assets/). Rationale: _design/2026-06-03-logos.md.
SVG_SNIFF = re.compile(rb"<svg\b|<\?xml", re.I)


def fetch_bytes(url: str, referer: str | None) -> bytes | None:
    """Headed GET (browser UA + Referer) — like fetch_image but format-agnostic: logos fetches
    SPECIFIC known URLs (google-s2, apple-touch, og, the chosen wordmark), not a blind scan, so no
    magic-byte/pixel gate — an SVG body must pass through too. Bare fetch 403s on bot CDNs (§5.2)."""
    headers = {
        "User-Agent": HERO_UA,
        "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    for ref in [r for r in (referer, f"https://{urlparse(url).netloc}/") if r]:
        try:
            req = urllib.request.Request(url, headers={**headers, "Referer": ref})
            with urllib.request.urlopen(req, timeout=30) as r:
                blob = r.read()
            if len(blob) >= 100:  # reject an empty / error-stub body, not a real small icon
                return blob
        except Exception:
            continue
    return None


def sips_dims(path: Path) -> tuple[int, int] | None:
    """(width, height) px via macOS `sips` — stdlib subprocess, never PIL (the design's no-image-dep
    line). None when sips can't read it (a vector SVG, or a non-image body)."""
    try:
        out = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
        ).stdout
    except Exception:
        return None
    wm = re.search(r"pixelWidth:\s*(\d+)", out)
    hm = re.search(r"pixelHeight:\s*(\d+)", out)
    return (int(wm.group(1)), int(hm.group(1))) if wm and hm else None


def svg_dims(text: str) -> tuple[int, int] | None:
    """(width, height) scoped to the OPENING <svg> tag — its numeric width/height, else its viewBox
    (`min-x min-y W H`). Tag-scoped + numeric-only on purpose: a whole-text scan pairs the root's
    `width` with a CHILD's `height`, and `width="100%"` is a layout hint, not a pixel size — both
    are why eden's `width="100%" viewBox="0 0 74 31"` must fall through to the box (74x31)."""
    head = m.group(0) if (m := re.search(r"<svg\b[^>]*>", text, re.I)) else text[:1000]

    def attr(name: str) -> float | None:
        a = re.search(rf'\b{name}="(\d+(?:\.\d+)?)(?:px)?"', head)  # bare number (+optional px), not "100%"
        return float(a.group(1)) if a else None

    wm, hm = attr("width"), attr("height")
    if wm and hm:
        return (round(wm), round(hm))
    vb = re.search(r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+(\d+(?:\.\d+)?)[\s,]+(\d+(?:\.\d+)?)', head)
    if vb:
        return (round(float(vb.group(1))), round(float(vb.group(2))))
    return None


def do_logos(slug: str, name: str, date: str, wordmark: str | None) -> None:
    p, used = latest_payload(slug, name, date)
    if p is None:
        sys.exit(f"logos: no {name}.json under store/{slug}/captures/* — capture the homepage first (--homepage)")
    data = json.loads(p.read_text())
    data = data.get("data", data)
    meta = data.get("metadata") or {}
    raw = data.get("rawHtml") or ""
    src = meta.get("sourceURL") or meta.get("url") or ""
    netloc = urlparse(src).netloc or slug.replace("-", ".")
    domain = netloc[4:] if netloc.startswith("www.") else netloc
    referer = f"https://{netloc}/" if netloc else None
    outdir = store(slug, date) / ".payloads" / "logos"
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"=== logos {slug} ({name}.json, {used}) ===")
    print(
        "  sips MEASURES; the AGENT looks — confirm the wordmark is the real brand mark (a blind scan\n"
        "  grabs press logos, Probe 2) and judge `transparent` on a checker tile (hasAlpha lies, Probe 3).\n"
        "  Omit a slot only on TRUE absence; RECORD a small/weak mark with its measurement, never drop it."
    )

    def measure(tag: str, ref: str, *, local: bool = False) -> tuple[int, int] | None:
        """Fetch (or read a local file) + measure one source; saves a viewable copy to .payloads/logos/."""
        if local:
            fp = Path(ref) if Path(ref).is_absolute() else ROOT / ref
            if not fp.exists():
                print(f"  {tag:15} MISSING FILE  {ref}")
                return None
            blob = fp.read_bytes()
        else:
            blob = fetch_bytes(ref, referer)
            if not blob:
                print(f"  {tag:15} FETCH-FAIL    {ref}")
                return None
        is_svg = bool(SVG_SNIFF.search(blob[:300]))
        if local:
            target = fp
        else:
            target = outdir / f"{tag}.{'svg' if is_svg else (hero_ext(blob) or 'img')}"
            target.write_bytes(blob)
        dims = svg_dims(blob.decode("utf-8", "ignore")) if is_svg else sips_dims(target)
        size = f"{dims[0]}x{dims[1]}" if dims else "??x?? unmeasured"
        print(f"  {tag:15} {'svg' if is_svg else 'raster':6} {size:>14}  {ref}")
        return dims

    # --- logomark: the larger MEASURED of the two deterministic square sources ---
    print("\n## logomark  (square; >=128px short side is the deck bar — the CONSUMER applies it)")
    cands = [("logomark-s2", f"https://www.google.com/s2/favicons?domain={domain}&sz=256")]
    for lm in re.finditer(r"<link\b[^>]*apple-touch-icon[^>]*>", raw, re.I):
        href = re.search(r'href="([^"]+)"', lm.group(0))
        if href:
            cands.append(("logomark-apple", urljoin(src or f"https://{netloc}/", href.group(1))))
    best: tuple[int, str] | None = None  # (short_side_px, winning_src)
    for tag, url in cands:
        dims = measure(tag, url)
        if dims and (best is None or min(dims) > best[0]):
            best = (min(dims), url)
    if best:
        flag = "" if best[0] >= 128 else "   <-- under 128px (record it anyway; the consumer's call)"
        print(f"  -> winner px={best[0]}  src={best[1]}{flag}")
    else:
        print("  -> no measurable logomark — omit the slot (true absence)")

    # --- og: the DECLARED og:image, gated at >=600px actual width ---
    print("\n## og  (wide cover; gate: a DECLARED og:image at >=600px ACTUAL width — the meta size lies, Probe 3)")
    og = meta.get("og:image") or meta.get("ogImage")
    if isinstance(og, list):  # Firecrawl returns a list when a page declares multiple og:image tags
        og = next((u for u in og if u), None)
    og_dims = None
    if not og:
        print("  no og:image declared — omit the og slot (true absence)")
    else:
        og = urljoin(src or f"https://{netloc}/", og)
        og_dims = measure("og", og)
        if og_dims and og_dims[0] < 600:
            print(f"  -> og width {og_dims[0]}px < 600 — best-effort gate FAILS; omit unless a small-cover consumer wants it")

    # --- wordmark: the agent's pick (vision); fc.py only measures what it's handed ---
    print("\n## wordmark  (rectangle, mark+name — the PRIMARY slot; YOU pick it by looking, fc.py measures)")
    wm_dims = None
    if not wordmark:
        print("  no --wordmark given. Pick it by LOOKING: the hostable logo_url if it's a real wordmark, else")
        print("  extract the inline <svg> (commit the text to store/<slug>/assets/wordmark.svg), then re-run")
        print("  with --wordmark <url|path> to measure it. NEVER let a blind scan pick it (press-logo trap).")
    else:
        wm_dims = measure("wordmark", wordmark, local=not wordmark.startswith("http"))

    # --- draft block — the agent CONFIRMS by looking, sets `transparent`, then writes it ---
    print("\n## Draft logos:{} — confirm by looking, set `transparent`, then write into profile.md frontmatter:")
    wm_src = wordmark or "assets/wordmark.svg | <hostable-url>"
    wm_wh = f"w: {wm_dims[0]}, h: {wm_dims[1]}" if wm_dims else "w: ?, h: ?"
    print(f"  logo_url: {wm_src}        # new captures canonicalize logo_url to the wordmark")
    print("  logos:")
    print(f"    wordmark: {{ src: {wm_src}, {wm_wh} }}")
    if best:
        print(f'    logomark: {{ src: "{best[1]}", px: {best[0]}, transparent: <true|false — YOU judge> }}')
    if og_dims:
        print(f'    og:       {{ src: "{og}", w: {og_dims[0]}, h: {og_dims[1]} }}')
    print(f"\n  candidates saved to {outdir.relative_to(ROOT)}/ — Read them to confirm the mark + judge `transparent`.")


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
    s.add_argument("--actions-json", help="JSON array of Firecrawl scrape actions to run before capture")
    s.add_argument("--mobile", action="store_true", help="enable Firecrawl mobile emulation for this scrape")
    s.add_argument("--headers-json", help="JSON object of extra request headers for this scrape")
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
    lg = sub.add_parser("logos")
    lg.add_argument("--slug", required=True)
    lg.add_argument("--name", default="homepage", help="homepage payload to source og:image + apple-touch + domain (default: homepage)")
    lg.add_argument(
        "--wordmark",
        help="the wordmark YOU picked (a hostable URL or a committed assets/ path) — fc.py measures it, vision picks it (§1.2)",
    )
    lg.add_argument("--date", default=TODAY)
    sub.add_parser("credits")
    a = ap.parse_args()
    if a.cmd == "map":
        do_map(a.url, a.slug, a.search, a.limit, a.date, a.subdomains)
    elif a.cmd == "scrape":
        do_scrape(
            a.url,
            a.slug,
            a.name,
            a.homepage,
            a.wait,
            a.proxy,
            a.images,
            a.date,
            a.actions_json,
            a.mobile,
            a.headers_json,
        )
    elif a.cmd == "verify":
        do_verify(a.slug, a.date)
    elif a.cmd == "spend":
        do_spend(a.slug, a.date)
    elif a.cmd == "signals":
        do_signals(a.slug, a.name, a.date)
    elif a.cmd == "hero":
        do_hero(a.slug, a.name, a.date, a.top)
    elif a.cmd == "logos":
        do_logos(a.slug, a.name, a.date, a.wordmark)
    elif a.cmd == "credits":
        do_credits()


if __name__ == "__main__":
    main()
