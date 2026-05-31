#!/usr/bin/env python3
"""Firecrawl capture helper for the telehealth-cohort experiment.

Bakes in the firecrawl-capture.md §5 hazard knobs (maxAge:0 + location:US +
waitFor + the all-formats bundle), persists raw JSON + cleaned markdown +
screenshots, and records a manifest for the §5.1 md5-dedup + sourceURL verify.
Mechanics only — no classification, no profile-writing.

Usage:
  fc.py map  <url> --slug <slug> [--search TERM] [--limit 500]
  fc.py scrape <url> --slug <slug> --name <name> [--homepage] [--wait 3500] [--proxy auto]
  fc.py verify --slug <slug>          # md5-dedup + sourceURL match across the run
  fc.py credits                       # GET /v2/team/credit-usage (free)
"""
import argparse, hashlib, json, os, sys, time, urllib.request
from pathlib import Path

API = "https://api.firecrawl.dev/v2"
KEY = os.environ.get("FIRECRAWL_API_KEY")
if not KEY:
    settings = json.load(open(os.path.expanduser("~/.claude/settings.json")))
    KEY = settings["env"]["FIRECRAWL_API_KEY"]
HDR = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

ROOT = Path(__file__).resolve().parents[2]          # .../Web Research
DATE = "2026-05-30"

def store(slug):
    d = ROOT / "store" / slug / "captures" / DATE
    (d / ".payloads").mkdir(parents=True, exist_ok=True)
    return d

def post(endpoint, body):
    req = urllib.request.Request(f"{API}/{endpoint}",
        data=json.dumps(body).encode(), headers=HDR, method="POST")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)

def do_map(url, slug, search, limit):
    body = {"url": url, "limit": limit, "location": {"country": "US"}}
    if search:
        body["search"] = search
    out = post("map", body)
    links = out.get("links", out.get("data", []))
    d = store(slug)
    tag = f"map_{search}" if search else "map"
    (d / ".payloads" / f"{tag}.json").write_text(json.dumps(out, indent=2))
    print(f"[map] {url}  search={search!r}  -> {len(links)} urls  (saved {tag}.json)")
    for item in links[:600]:
        u = item.get("url") if isinstance(item, dict) else item
        print("   ", u)

def do_scrape(url, slug, name, homepage, wait, proxy):
    if homepage:
        formats = ["markdown", "html", "rawHtml", "links", "branding", "images",
                   {"type": "screenshot", "fullPage": True}]
        only_main = False
    else:
        formats = ["markdown", "links", {"type": "screenshot", "fullPage": True}]
        only_main = True
    body = {"url": url, "formats": formats, "maxAge": 0,
            "location": {"country": "US", "languages": ["en-US"]},
            "waitFor": wait, "onlyMainContent": only_main}
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
    md5 = hashlib.md5(md.encode()).hexdigest()
    d = store(slug)
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
    rec = {"name": name, "requested": url, "sourceURL": src, "status": status,
           "md5": md5, "mdlen": len(md), "secs": round(dt, 1),
           "match": (src or "").rstrip("/") == url.rstrip("/")}
    with open(d / ".payloads" / "manifest.jsonl", "a") as f:
        f.write(json.dumps(rec) + "\n")
    flag = "" if rec["match"] else "  <-- sourceURL MISMATCH"
    print(f"[scrape] {name:28} status={status} mdlen={len(md):>6} {dt:4.1f}s "
          f"md5={md5[:8]} {shot_ok}{flag}")
    print(f"         src={src}")
    if md and len(md) < 500:
        print(f"         !! THIN markdown (<500c) — possible SPA-blank / wall")

def do_verify(slug):
    d = store(slug)
    mf = d / ".payloads" / "manifest.jsonl"
    if not mf.exists():
        print("no manifest"); return
    recs = [json.loads(l) for l in mf.read_text().splitlines() if l.strip()]
    by_md5 = {}
    print(f"=== verify {slug} ({len(recs)} pages) ===")
    bad = False
    for r in recs:
        by_md5.setdefault(r["md5"], []).append(r["name"])
        if not r["match"]:
            print(f"  sourceURL MISMATCH: {r['name']}  requested={r['requested']} got={r['sourceURL']}")
            bad = True
    for md5, names in by_md5.items():
        if len(names) > 1:
            print(f"  DUP BODY md5={md5[:8]} across: {names}  <-- §5.1 contamination")
            bad = True
    print("  OK — all sourceURLs match, all bodies unique" if not bad else "  ^^ ISSUES above")

def do_credits():
    req = urllib.request.Request(f"{API}/team/credit-usage", headers=HDR)
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.load(r)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("map");    m.add_argument("url"); m.add_argument("--slug", required=True); m.add_argument("--search"); m.add_argument("--limit", type=int, default=500)
    s = sub.add_parser("scrape"); s.add_argument("url"); s.add_argument("--slug", required=True); s.add_argument("--name", required=True); s.add_argument("--homepage", action="store_true"); s.add_argument("--wait", type=int, default=3500); s.add_argument("--proxy")
    v = sub.add_parser("verify"); v.add_argument("--slug", required=True)
    sub.add_parser("credits")
    a = ap.parse_args()
    if a.cmd == "map":     do_map(a.url, a.slug, a.search, a.limit)
    elif a.cmd == "scrape":do_scrape(a.url, a.slug, a.name, a.homepage, a.wait, a.proxy)
    elif a.cmd == "verify":do_verify(a.slug)
    elif a.cmd == "credits":do_credits()
