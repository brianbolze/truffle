#!/usr/bin/env python3
"""Firecrawl capture helper for the /research-company verb.

Bakes in the firecrawl-capture.md §5 hazard knobs (maxAge:0 + location:US +
waitFor + the all-formats bundle), persists raw JSON + cleaned markdown +
screenshots into store/<slug>/captures/<date>/, and records a manifest for the
§5.1 md5-dedup + sourceURL verify. Mechanics only — no classification, no
profile-writing (that's the agent's enrichment job, per SCHEMA.md).

Usage:
  fc.py map    <url> --slug <slug> [--search TERM] [--limit 500] [--subdomains] [--date YYYY-MM-DD]
  fc.py scrape <url> --slug <slug> --name <name> [--homepage] [--wait 3500] [--proxy auto] [--date ...]
  fc.py verify --slug <slug> [--date ...]   # scrapes: md5-dedup + sourceURL match; + lint profile.md once written
  fc.py spend  --slug <slug> [--date ...]   # this run's attributed cost, summed from per-call creditsUsed
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

import argparse, datetime, hashlib, json, os, re, sys, time, urllib.request
from pathlib import Path

API = "https://api.firecrawl.dev/v2"
KEY = os.environ.get("FIRECRAWL_API_KEY")
if not KEY:
    settings = json.load(open(os.path.expanduser("~/.claude/settings.json")))
    KEY = settings["env"]["FIRECRAWL_API_KEY"]
HDR = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

ROOT = (
    Path(__file__).resolve().parents[3]
)  # skills/research-company/scripts/fc.py -> repo root
TODAY = datetime.date.today().isoformat()


def store(slug, date):
    d = ROOT / "store" / slug / "captures" / date
    (d / ".payloads").mkdir(parents=True, exist_ok=True)
    return d


def append_manifest(d, rec):
    """One JSONL line per billable call — the per-run integrity + credit ledger.
    `kind` ("scrape"|"map") lets verify read scrape-only records and spend sum all."""
    with open(d / ".payloads" / "manifest.jsonl", "a") as f:
        f.write(json.dumps(rec) + "\n")


def post(endpoint, body):
    req = urllib.request.Request(
        f"{API}/{endpoint}", data=json.dumps(body).encode(), headers=HDR, method="POST"
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def do_map(url, slug, search, limit, date, subdomains=False):
    # includeSubdomains defaults FALSE: a docs/dev subdomain (developers./docs.)
    # otherwise swamps the map AND starves the marketing host's crawl — Cloudflare
    # surfaced 4 www URLs with it on, 460 with it off. --subdomains opts back in for
    # the rare signal subdomain (e.g. investors.), which the homepage also links (§5.3).
    body = {
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
    tag = f"map_{search}" if search else "map"
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
    print(
        f"[map] {url}  search={search!r}  -> {len(links)} urls  (1 credit, saved {tag}.json)"
    )
    for item in links[:600]:
        u = item.get("url") if isinstance(item, dict) else item
        print("   ", u)


def do_scrape(url, slug, name, homepage, wait, proxy, date):
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
        only_main = True
    body = {
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
    credits = meta.get(
        "creditsUsed"
    )  # per-call billed truth (1 base; +4 enhanced proxy; +1/PDF pg)
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
    print(
        f"[scrape] {name:28} status={status} cr={cr} mdlen={len(md):>6} {dt:4.1f}s "
        f"md5={md5[:8]} {shot_ok}{flag}"
    )
    print(f"         src={src}")
    if md and len(md) < 500:
        print(f"         !! THIN markdown (<500c) — possible SPA-blank / wall")


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
LEAK_RE = re.compile(
    r"</?\s*(?:antml:)?(?:function_calls|invoke|parameter|content)\b[^>]*>", re.I
)


def frontmatter_keys(text):
    """Top-level frontmatter keys via a column-0 line scan (stdlib-only — no PyYAML).
    Returns None if there's no leading '---' fence."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return [
        m.group(1)
        for line in parts[1].splitlines()
        if (m := re.match(r"([A-Za-z_][A-Za-z0-9_]*):", line))
    ]


def lint_profile(slug):
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
    print(
        "  profile.md OK — no leaked tags, Provenance present, required keys present"
        if not bad
        else "  ^^ profile.md ISSUES above"
    )
    return bad


def do_verify(slug, date):
    d = store(slug, date)
    bad = False
    # --- scrapes: sourceURL match + md5-uniqueness across the run ---
    mf = d / ".payloads" / "manifest.jsonl"
    if not mf.exists():
        print(f"=== verify {slug} ===")
        print("  no manifest — run scrapes first (skipping scrape checks)")
    else:
        recs = [json.loads(l) for l in mf.read_text().splitlines() if l.strip()]
        scrapes = [r for r in recs if r.get("kind", "scrape") == "scrape"]
        by_md5 = {}
        print(f"=== verify {slug} ({len(scrapes)} pages) ===")
        scrape_bad = False
        for r in scrapes:
            by_md5.setdefault(r["md5"], []).append(r["name"])
            if not r["match"]:
                print(
                    f"  sourceURL MISMATCH: {r['name']}  requested={r['requested']} got={r['sourceURL']}"
                )
                scrape_bad = True
        for md5, names in by_md5.items():
            if len(names) > 1:
                print(
                    f"  DUP BODY md5={md5[:8]} across: {names}  <-- §5.1 contamination"
                )
                scrape_bad = True
        print(
            "  scrapes OK — all sourceURLs match, all bodies unique"
            if not scrape_bad
            else "  ^^ scrape ISSUES above"
        )
        bad |= scrape_bad
    # --- the written dossier ---
    bad |= lint_profile(slug)
    if bad:
        sys.exit("verify: issues found (see above)")


def do_spend(slug, date):
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
    recs = [json.loads(l) for l in mf.read_text().splitlines() if l.strip()]
    total, unknown = 0, 0
    for r in recs:
        c = r.get("credits")
        proxy = r.get("proxy")
        extra = f"  ({proxy} proxy)" if proxy and proxy != "basic" else ""
        if c is None:
            mark, unknown = "?", unknown + 1
        else:
            mark, total = str(c), total + c
        print(f"  {r.get('kind','scrape'):7} {r.get('name',''):26} {mark:>3}{extra}")
    note = (
        ""
        if not unknown
        else f"   ({unknown} call(s) w/o reported credits — total is a floor)"
    )
    print(f"  {'':7} {'TOTAL':26} {total:>3} credits{note}")


def do_credits():
    req = urllib.request.Request(f"{API}/team/credit-usage", headers=HDR)
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.load(r)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("map")
    m.add_argument("url")
    m.add_argument("--slug", required=True)
    m.add_argument("--search")
    m.add_argument("--limit", type=int, default=500)
    m.add_argument("--subdomains", action="store_true",
                   help="include subdomains (default: off — drops the docs/dev swamp, §5.3)")
    m.add_argument("--date", default=TODAY)
    s = sub.add_parser("scrape")
    s.add_argument("url")
    s.add_argument("--slug", required=True)
    s.add_argument("--name", required=True)
    s.add_argument("--homepage", action="store_true")
    s.add_argument("--wait", type=int, default=3500)
    s.add_argument("--proxy")
    s.add_argument("--date", default=TODAY)
    v = sub.add_parser("verify")
    v.add_argument("--slug", required=True)
    v.add_argument("--date", default=TODAY)
    sp = sub.add_parser("spend")
    sp.add_argument("--slug", required=True)
    sp.add_argument("--date", default=TODAY)
    sub.add_parser("credits")
    a = ap.parse_args()
    if a.cmd == "map":
        do_map(a.url, a.slug, a.search, a.limit, a.date, a.subdomains)
    elif a.cmd == "scrape":
        do_scrape(a.url, a.slug, a.name, a.homepage, a.wait, a.proxy, a.date)
    elif a.cmd == "verify":
        do_verify(a.slug, a.date)
    elif a.cmd == "spend":
        do_spend(a.slug, a.date)
    elif a.cmd == "credits":
        do_credits()
