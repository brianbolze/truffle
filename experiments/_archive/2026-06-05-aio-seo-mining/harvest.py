#!/usr/bin/env python3
"""
AIO/SEO signal harvest — the deterministic backbone for the mining experiment.

Two sources, one record per company:
  A. FETCHED live (the pieces the store never captured): robots.txt, llms.txt,
     llms-full.txt, sitemap presence. Tiny static files; plain urllib, no Firecrawl.
  B. EXTRACTED from existing Firecrawl payloads (store/<slug>/captures/*/.payloads/*.json):
     JSON-LD @type inventory (union across all captured pages) + homepage meta tags.
     The markdown strips these; the rawHtml/metadata payload keeps them.

Writes _out/signals/<slug>.json (full), _out/raw/<slug>.{robots,llms}.txt (citable),
and _out/matrix.json (compact, one row per company). Prints corpus rollups.
No deps beyond stdlib. Re-runnable.
"""
import glob, json, os, re, sys, urllib.request, urllib.error, concurrent.futures, ssl

ROOT = os.environ.get("WEB_RESEARCH_HOME", ".")
OUT = os.path.join(ROOT, "experiments/2026-06-05-aio-seo-mining/_out")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE  # a few have cert quirks; we only read public text

# --- AI / LLM crawler user-agents, split by what blocking them actually costs -------
# TRAIN = model-training corpus crawlers (blocking = opt out of training, NOT answers)
# RETRIEVE = live answer-time fetchers (blocking = removed from AI answers/citations = AIO own-goal)
AI_CRAWLERS = {
    "GPTBot": "train",            # OpenAI training
    "OAI-SearchBot": "retrieve",  # ChatGPT search index
    "ChatGPT-User": "retrieve",   # ChatGPT live browsing (user-initiated)
    "ClaudeBot": "train",         # Anthropic training
    "anthropic-ai": "train",
    "Claude-Web": "retrieve",
    "Claude-User": "retrieve",    # Anthropic user-initiated fetch
    "Claude-SearchBot": "retrieve",
    "Google-Extended": "train",   # Gemini training (Googlebot still indexes for AI Overviews)
    "PerplexityBot": "retrieve",  # Perplexity index
    "Perplexity-User": "retrieve",
    "CCBot": "train",             # Common Crawl — feeds many LLMs
    "Bytespider": "train",        # ByteDance
    "Amazonbot": "train",
    "Applebot-Extended": "train", # Apple AI training (Applebot itself = Siri/Spotlight)
    "Meta-ExternalAgent": "train",
    "FacebookBot": "train",
    "cohere-ai": "train",
    "Diffbot": "train",
    "Omgilibot": "train",
    "Timpibot": "train",
    "YouBot": "retrieve",         # You.com
    "DuckAssistBot": "retrieve",  # DuckDuckGo AI
    "PetalBot": "train",
}

def fetch(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            body = r.read(600_000).decode("utf-8", "replace")
            return {"status": r.status, "final": r.geturl(),
                    "ctype": r.headers.get("Content-Type", ""), "body": body}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "final": url, "ctype": "", "body": ""}
    except Exception as e:
        return {"status": -1, "final": url, "ctype": "", "body": "", "err": type(e).__name__}

def looks_like_text(resp, kind):
    """Guard against SPA catch-alls returning index.html with 200 for /llms.txt etc."""
    if resp["status"] != 200 or not resp["body"].strip():
        return False
    b = resp["body"].lstrip()
    if b[:200].lower().count("<!doctype html") or b[:600].lower().count("<html"):
        return False
    if "text/html" in resp["ctype"].lower():
        return False
    if kind == "robots":
        return bool(re.search(r"(?im)^\s*(user-agent|disallow|allow|sitemap)\s*:", b))
    return True  # llms.txt: any non-HTML text body counts

# --- robots.txt parsing: group UA -> rules, then resolve per AI crawler ------------
def parse_robots(body):
    groups, cur = [], None
    for raw in body.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, val = line.split(":", 1)
        field, val = field.strip().lower(), val.strip()
        if field == "user-agent":
            if cur and cur["rules"]:           # new group starts after rules seen
                groups.append(cur); cur = None
            if cur is None:
                cur = {"agents": [], "rules": []}
            cur["agents"].append(val)
        elif field in ("allow", "disallow") and cur is not None:
            cur["rules"].append((field, val))
    if cur:
        groups.append(cur)
    return groups

def posture_for(agent, groups, star_group):
    """Return 'blocked' (Disallow: /), 'allowed', 'partial', or 'default' for a UA."""
    g = None
    for grp in groups:
        if any(a.lower() == agent.lower() for a in grp["agents"]):
            g = grp; break
    if g is None:
        if star_group is None:
            return "default"  # not named, no * group => allowed by default
        g = star_group
        named = False
    else:
        named = True
    disallows = [v for f, v in g["rules"] if f == "disallow"]
    allows = [v for f, v in g["rules"] if f == "allow"]
    full_block = any(v == "/" for v in disallows) and not any(v == "/" for v in allows)
    if full_block:
        return "blocked" + ("" if named else "*")
    if disallows and any(v for v in disallows):
        return "partial" + ("" if named else "*")
    return "allowed" + ("" if named else "*")

# --- JSON-LD @type harvest from payloads -------------------------------------------
LD_RE = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                   re.I | re.S)
def types_in(obj, acc):
    if isinstance(obj, dict):
        t = obj.get("@type")
        if isinstance(t, str): acc.add(t)
        elif isinstance(t, list): acc.update(x for x in t if isinstance(x, str))
        for v in obj.values(): types_in(v, acc)
    elif isinstance(obj, list):
        for v in obj: types_in(v, acc)

def jsonld_from_payload(path):
    """Return (set_of_types, list_of_raw_block_strings) from one page payload JSON."""
    try:
        d = json.load(open(path, encoding="utf-8", errors="ignore"))
    except Exception:
        return set(), []
    if not isinstance(d, dict):
        return set(), []
    node = d.get("data", d)
    if not isinstance(node, dict):
        return set(), []
    raw = node.get("rawHtml") or ""
    types, blocks = set(), []
    for m in LD_RE.findall(raw):
        s = m.strip()
        try:
            parsed = json.loads(s)
        except Exception:
            # salvage @type via regex even if JSON is malformed
            for t in re.findall(r'"@type"\s*:\s*"([^"]+)"', s):
                types.add(t)
            blocks.append(s[:4000]); continue
        types_in(parsed, types)
        blocks.append(s[:4000])
    return types, blocks

def homepage_meta(slug):
    """Latest-date homepage.json metadata dict + canonical/hreflang from its rawHtml."""
    cands = sorted(glob.glob(f"{ROOT}/store/{slug}/captures/*/.payloads/homepage.json"))
    if not cands:
        cands = sorted(glob.glob(f"{ROOT}/store/{slug}/captures/*/.payloads/*.json"))
        cands = [c for c in cands if os.path.basename(c) not in ("manifest.jsonl", "map.json")]
    if not cands:
        return {}, None, 0
    try:
        d = json.load(open(cands[-1], encoding="utf-8", errors="ignore"))
    except Exception:
        return {}, None, 0
    node = d.get("data", d) if isinstance(d, dict) else {}
    if not isinstance(node, dict):
        return {}, None, 0
    md = node.get("metadata", {}) or {}
    raw = node.get("rawHtml") or ""
    canon = None
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', raw, re.I)
    if m: canon = m.group(1)
    hreflang = len(re.findall(r'hreflang=', raw, re.I))
    keep = ("title", "description", "keywords", "og:title", "og:description", "og:image",
            "og:type", "og:site_name", "twitter:card", "twitter:title", "theme-color",
            "robots", "googlebot", "language", "generator")
    meta = {k: md.get(k) for k in keep if md.get(k)}
    return meta, canon, hreflang

def company_jsonld(slug):
    payloads = glob.glob(f"{ROOT}/store/{slug}/captures/*/.payloads/*.json")
    payloads = [p for p in payloads if os.path.basename(p) not in ("manifest.jsonl", "map.json")]
    all_types, type_pages, examples = set(), {}, {}
    for p in payloads:
        types, blocks = jsonld_from_payload(p)
        for t in types:
            type_pages[t] = type_pages.get(t, 0) + 1
        all_types |= types
        # stash one example block per interesting type for citation
        for b in blocks:
            for t in re.findall(r'"@type"\s*:\s*"([^"]+)"', b):
                if t not in examples and t in INTERESTING:
                    examples[t] = {"page": os.path.basename(p), "block": b}
    return sorted(all_types), type_pages, examples

INTERESTING = {"FAQPage", "Product", "Offer", "AggregateRating", "Review", "BreadcrumbList",
               "MedicalOrganization", "MedicalWebPage", "Physician", "Drug", "HowTo",
               "Article", "BlogPosting", "VideoObject", "Course", "Event", "Service",
               "WebSite", "SearchAction", "ItemList", "SoftwareApplication", "Question"}

# --- domain + vertical from profile frontmatter ------------------------------------
WATCH = {"rolex-com","patek-com","cartier-com","audemarspiguet-com","alange-soehne-com",
         "swatch-com","casio-com"}
def vertical(slug, ind, off):
    if glob.glob(f"{ROOT}/store/{slug}/telehealth.md"): return "telehealth"
    if slug in WATCH: return "luxury-watch"
    blob = (ind + " " + off).lower()
    if "software" in blob or "fintech" in blob or ind in ("Technology","Finance & Fintech"):
        return "b2b-saas"
    if "marketplace" in blob or "hospitality" in blob: return "consumer-marketplace"
    if "physical" in blob or "retail" in blob or "sports" in blob or "consumer goods" in ind.lower():
        return "consumer-brand"
    return "other"

def fm(p):
    t = open(p, encoding="utf-8", errors="ignore").read()
    blk = t.split("---", 2)[1] if t.startswith("---") else ""
    d = {}
    for line in blk.splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if m: d[m.group(1)] = m.group(2).split("#")[0].strip().strip('"')
    return d

def main():
    companies = []
    for prof in sorted(glob.glob(f"{ROOT}/store/*/profile.md")):
        slug = prof.split("/")[-2]
        d = fm(prof)
        dom = d.get("domain", "").strip()
        if not dom: continue
        companies.append((slug, dom, vertical(slug, d.get("primary_industry",""),
                                              d.get("offering_category","")), d.get("name", slug)))
    print(f"[harvest] {len(companies)} companies\n")

    # ---- parallel fetch of the missing files ----
    def grab(c):
        slug, dom, vert, name = c
        base = f"https://{dom}"
        robots = fetch(base + "/robots.txt")
        llms = fetch(base + "/llms.txt")
        llmsfull = fetch(base + "/llms-full.txt")
        return slug, robots, llms, llmsfull
    fetched = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        for slug, robots, llms, llmsfull in ex.map(grab, companies):
            fetched[slug] = (robots, llms, llmsfull)

    rows = []
    for slug, dom, vert, name in companies:
        robots, llms, llmsfull = fetched[slug]
        rb_ok = looks_like_text(robots, "robots")
        rb_body = robots["body"] if rb_ok else ""
        groups = parse_robots(rb_body) if rb_ok else []
        star = next((g for g in groups if "*" in g["agents"]), None)
        ai_posture = {a: posture_for(a, groups, star) for a in AI_CRAWLERS} if rb_ok else {}
        sitemaps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", rb_body)
        llms_ok = looks_like_text(llms, "llms")
        llmsfull_ok = looks_like_text(llmsfull, "llms")

        meta, canon, hreflang = homepage_meta(slug)
        ld_types, ld_pages, ld_examples = company_jsonld(slug)

        # write citable raw files
        if rb_ok:
            open(f"{OUT}/raw/{slug}.robots.txt", "w").write(rb_body)
        if llms_ok:
            open(f"{OUT}/raw/{slug}.llms.txt", "w").write(llms["body"])

        rec = {
            "slug": slug, "domain": dom, "vertical": vert, "name": name,
            "robots": {"ok": rb_ok, "status": robots["status"], "n_groups": len(groups),
                       "ai_posture": ai_posture, "sitemaps": sitemaps,
                       "has_star_block": bool(star and any(v=="/" for f,v in star["rules"] if f=="disallow")),
                       "len": len(rb_body)},
            "llms_txt": {"present": llms_ok, "status": llms["status"], "len": len(llms["body"]) if llms_ok else 0},
            "llms_full_txt": {"present": llmsfull_ok, "status": llmsfull["status"]},
            "jsonld": {"types": ld_types, "type_pages": ld_pages, "n_types": len(ld_types)},
            "meta": meta, "canonical": canon, "hreflang_count": hreflang,
        }
        json.dump({**rec, "jsonld_examples": ld_examples,
                   "robots_body": rb_body[:8000], "llms_body": (llms["body"][:8000] if llms_ok else "")},
                  open(f"{OUT}/signals/{slug}.json", "w"), indent=1)
        rows.append(rec)

    json.dump(rows, open(f"{OUT}/matrix.json", "w"), indent=1)

    # ---- rollups ----
    n = len(rows)
    def pct(k): return f"{k}/{n} ({100*k//n}%)"
    llms_yes = [r for r in rows if r["llms_txt"]["present"]]
    robots_yes = [r for r in rows if r["robots"]["ok"]]
    print("=== CORPUS ROLLUPS ===")
    print("robots.txt fetched OK:", pct(len(robots_yes)))
    print("llms.txt present:", pct(len(llms_yes)), "->", [r["slug"] for r in llms_yes])
    print("llms-full.txt present:", pct(len([r for r in rows if r['llms_full_txt']['present']])))
    print("any JSON-LD:", pct(len([r for r in rows if r["jsonld"]["n_types"]])))
    # JSON-LD type frequency
    from collections import Counter
    tc = Counter()
    for r in rows:
        for t in r["jsonld"]["types"]: tc[t] += 1
    print("\nJSON-LD @type frequency (companies deploying each):")
    for t, c in tc.most_common(30):
        print(f"  {t:<24} {pct(c)}")
    # AI crawler blocking rollup (among robots-OK)
    print("\nAI-crawler posture (among robots-OK; 'blocked'=Disallow:/ named or via *):")
    for a, kind in AI_CRAWLERS.items():
        blocked = sum(1 for r in robots_yes if str(r["robots"]["ai_posture"].get(a,"")).startswith(("blocked","partial")))
        hard = sum(1 for r in robots_yes if str(r["robots"]["ai_posture"].get(a,"")).startswith("blocked"))
        if blocked:
            print(f"  {a:<20} [{kind:<8}] restricted {blocked:>2} (hard-block {hard})")
    print("\nby vertical:", Counter(r["vertical"] for r in rows))

if __name__ == "__main__":
    main()
