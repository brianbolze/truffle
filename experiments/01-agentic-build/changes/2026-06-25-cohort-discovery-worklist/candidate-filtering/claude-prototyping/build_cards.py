#!/usr/bin/env python3
"""Assemble candidate evidence cards from the packet's CACHED discovery feeders.

Deterministic only: code builds the card, the agent makes the judgment later.
No new spend — reads what the packet already captured:
  - ../../receipts/raw/iteration-2/serpapi/*.json   (SERP organic + references)
  - ../../receipts/raw/iteration-2/exa/*.json        (Exa /search results)
  - ../../receipts/raw/page-extraction/pages/*.json  (opened listicle pages: links + source host)

Writes: cards.jsonl  (one card per unique candidate, deduped by cohort+domain).
A card = name, domain, cohort, the richest snippet found, the feeders it came
from, and whether it IS a listicle's own host (for the publisher-precision test).
No labels, no classification.
"""
import json, os, re, glob
from urllib.parse import urlparse

HERE = os.path.dirname(__file__)
PACKET = os.path.abspath(os.path.join(HERE, "..", ".."))
ROOT = os.path.join(PACKET, "receipts", "raw")
OUT = os.path.join(HERE, "cards.jsonl")

SOCIAL_INFRA = {
    "facebook.com", "twitter.com", "x.com", "linkedin.com", "instagram.com",
    "youtube.com", "tiktok.com", "apple.com", "google.com", "play.google.com",
    "github.com", "reddit.com", "pinterest.com", "wikipedia.org", "gravatar.com",
    "gstatic.com", "googleapis.com", "cloudflare.com", "doubleclick.net",
    "bit.ly", "goo.gl", "t.co", "g.co", "statuspage.io", "schema.org",
    "aboutads.info", "networkadvertising.org", "privacysandbox.com", "w3.org",
    "gstatic.com", "cookiepedia.co.uk", "onetrust.com", "trustarc.com",
}
NAV_STOP = {
    "skip to content", "skip to main content", "log in", "login", "sign up",
    "sign in", "get started", "home", "products", "pricing", "blog", "contact",
    "about", "about us", "privacy", "privacy policy", "terms", "careers",
    "support", "help", "menu", "search", "subscribe", "newsletter", "learn more",
    "read more", "see more", "view all", "next", "previous", "back to top",
    "download", "free trial", "book a demo", "request a demo", "watch demo",
    "visit site", "visit website", "official site", "shop now", "buy now",
    "try now", "get started today", "click here", "view plans",
}
CTA_PREFIX = ("visit ", "try ", "get ", "shop ", "learn about ", "explore ",
              "see ", "buy ", "start with ", "go to ")
SIGNAL_WORDS = (
    "$", "%", "/mo", "/month", "per month", "month", "pricing", "plans", "plan",
    "subscription", "membership", "offers", "offer", "provides", "provide",
    "platform", "care", "treatment", "prescription", "transcri", "meeting",
    "starting at", "from $", "clinic", "doctor", "notes", "labs", "therapy",
)


def reg_domain(host):
    host = re.sub(r"^https?://", "", (host or "").lower()).split("/")[0]
    host = host[4:] if host.startswith("www.") else host
    if not host or "." not in host:
        return host
    parts = host.split(".")
    multi = {"co.uk", "org.uk", "com.au", "co.in", "co.nz"}
    if len(parts) >= 3 and ".".join(parts[-2:]) in multi:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def domain_root(dom):
    return dom.split(".")[0] if dom else ""


def brand_from_domain(dom):
    return domain_root(dom).replace("-", " ").title()


def cohort_of(fname):
    b = os.path.basename(fname)
    if b.startswith("ci-") or b.startswith("conversation"):
        return "conversation-intelligence"
    if b.startswith("telehealth-"):
        return "telehealth"
    return "telehealth"


def snip_score(s):
    s = s or ""
    return sum(1 for w in SIGNAL_WORDS if w in s.lower()) + min(len(s), 220) / 440.0


def _window(text, i, before=60, after=200):
    s, e = max(0, i - before), min(len(text), i + after)
    chunk = text[s:e]
    if s > 0:
        sp = chunk.find(" ")
        if 0 <= sp <= 25:
            chunk = chunk[sp + 1:]
    if e < len(text):
        sp = chunk.rfind(" ")
        if sp > len(chunk) - 25:
            chunk = chunk[:sp]
    return re.sub(r"\s+", " ", chunk).strip()


def best_snippet(text, needles):
    if not text:
        return ""
    low = text.lower()
    best, best_score, seen = "", -1, 0
    for nd in needles:
        nd = (nd or "").strip()
        if len(nd) < 3:
            continue
        start = 0
        while seen < 60:
            i = low.find(nd.lower(), start)
            if i < 0:
                break
            start = i + len(nd)
            seen += 1
            w = _window(text, i)
            sc = snip_score(w)
            if sc > best_score:
                best, best_score = w, sc
    return best


def upsert(cards, cohort, domain, name, snippet, src_type, is_src=False, anchor=""):
    domain = reg_domain(domain)
    if not domain or domain in SOCIAL_INFRA:
        return None
    key = (cohort, domain)
    c = cards.get(key)
    if not c:
        c = {"name": name or brand_from_domain(domain), "domain": domain, "cohort": cohort,
             "snippet": snippet or "", "anchor_text": anchor, "is_source_domain": is_src,
             "feeders": [src_type]}
        cards[key] = c
    else:
        if src_type not in c["feeders"]:
            c["feeders"].append(src_type)
        if is_src:
            c["is_source_domain"] = True
        if snippet and snip_score(snippet) > snip_score(c["snippet"]):
            c["snippet"] = snippet
        if not c["anchor_text"] and anchor:
            c["anchor_text"] = anchor
    return c


def ingest_serpapi(cards):
    for p in glob.glob(os.path.join(ROOT, "iteration-2", "serpapi", "*.json")):
        d = json.load(open(p))
        cohort = cohort_of(p)
        for r in d.get("organic_results", []) or []:
            dom = reg_domain(r.get("link") or "")
            upsert(cards, cohort, dom, brand_from_domain(dom),
                   r.get("snippet") or r.get("title") or "", "serp_organic", anchor=r.get("title") or "")
        for r in d.get("references", []) or []:
            dom = reg_domain(r.get("link") or r.get("source") or "")
            upsert(cards, cohort, dom, brand_from_domain(dom), r.get("title") or "", "serp_reference",
                   anchor=r.get("title") or "")


def ingest_exa(cards):
    for p in glob.glob(os.path.join(ROOT, "iteration-2", "exa", "*.json")):
        d = json.load(open(p))
        cohort = cohort_of(p)
        for r in d.get("results", []) or []:
            dom = reg_domain(r.get("domain") or r.get("url") or "")
            upsert(cards, cohort, dom, brand_from_domain(dom), "", "exa", anchor=r.get("title") or "")


def ingest_pages(cards):
    base = os.path.join(ROOT, "page-extraction")
    panel = {p["id"]: p for p in json.load(open(os.path.join(base, "page-panel.json")))}
    for pf in sorted(glob.glob(os.path.join(base, "pages", "*.json"))):
        page = json.load(open(pf))
        pid = page.get("input", {}).get("id") or os.path.basename(pf).replace(".json", "")
        meta = panel.get(pid, {})
        cohort = (meta.get("cohort") or page.get("input", {}).get("cohort") or "").replace("_", "-")
        src_url = meta.get("url") or ""
        src_dom = reg_domain(urlparse(src_url).netloc or src_url)
        text = page.get("text", "") or ""
        if src_dom:
            upsert(cards, cohort, src_dom, brand_from_domain(src_dom),
                   best_snippet(text, [brand_from_domain(src_dom), domain_root(src_dom)])
                   or re.sub(r"\s+", " ", text[:240]).strip(),
                   "page_host", is_src=True, anchor=page.get("title") or "")
        for ln in page.get("links", []):
            href = ln.get("href") or ""
            raw = ln.get("domain") or ""
            if href.startswith("mailto:") or "@" in raw or "mailto" in raw:
                continue
            dom = reg_domain(raw)
            if not dom or dom == src_dom:
                continue
            anchor = (ln.get("text") or "").strip()
            if not (2 <= len(anchor) <= 60) or anchor.lower() in NAV_STOP:
                continue
            if anchor.startswith("#") or anchor.startswith("http") or not re.search(r"[A-Za-z]", anchor):
                continue
            upsert(cards, cohort, dom, brand_from_domain(dom),
                   best_snippet(text, [brand_from_domain(dom), anchor]), "page_link", anchor=anchor)


def main():
    cards = {}
    ingest_serpapi(cards)
    ingest_exa(cards)
    ingest_pages(cards)

    rows = list(cards.values())  # keep every domain-keyed candidate; the agent drops junk
    rows.sort(key=lambda c: (c["cohort"], c["domain"]))
    with open(OUT, "w") as f:
        for c in rows:
            c["feeder_count"] = len(c["feeders"])
            f.write(json.dumps(c) + "\n")

    th = sum(1 for c in rows if c["cohort"].startswith("telehealth"))
    print(f"wrote {len(rows)} cards -> {os.path.relpath(OUT)}")
    print(f"  telehealth={th}  conversation-intelligence={len(rows) - th}  "
          f"source-host={sum(1 for c in rows if c['is_source_domain'])}")
    from collections import Counter
    fc = Counter(f for c in rows for f in c["feeders"])
    print("  feeders:", dict(fc))
    print("\nsample telehealth cards:")
    for c in [r for r in rows if r["cohort"].startswith("telehealth")][:6]:
        print(f"  {c['name']!r:18} <{c['domain']:22}> {c['feeders']}  {c['snippet'][:70]!r}")


if __name__ == "__main__":
    main()
