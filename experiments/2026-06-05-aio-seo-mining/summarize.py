#!/usr/bin/env python3
"""Reprocess _out/signals/*.json into a clean matrix.md + correct rollups.

Fixes the harvest's over-count: a bot that merely falls through to a normal
`User-agent: *` group (which disallows /cart, /admin, ...) is NOT a deliberate
AI stance. The signals that matter: (a) is the bot NAMED in its own group, and
(b) is it HARD-blocked (Disallow: /), site-wide or by name.
"""
import json, glob, os
from collections import Counter, defaultdict

OUT = os.path.join(os.environ.get("WEB_RESEARCH_HOME", "."),
                   "experiments/2026-06-05-aio-seo-mining/_out")
rows = [json.load(open(p)) for p in sorted(glob.glob(f"{OUT}/signals/*.json"))]
n = len(rows)
RETRIEVE = {"OAI-SearchBot","ChatGPT-User","Claude-Web","Claude-User","Claude-SearchBot",
            "PerplexityBot","Perplexity-User","YouBot","DuckAssistBot"}

def named(posture):   # named group (deliberate) = no '*' suffix and not 'default'
    return posture in ("allowed","partial","blocked")
def blocked(posture): # hard Disallow:/ — named or site-wide via *
    return posture in ("blocked","blocked*")

for r in rows:
    ap = r["robots"]["ai_posture"]
    r["_named"] = sorted(a for a,p in ap.items() if named(p))
    r["_named_block"] = sorted(a for a,p in ap.items() if p == "blocked")
    r["_named_allow"] = sorted(a for a,p in ap.items() if p == "allowed")
    r["_blocks_retrieve"] = sorted(a for a,p in ap.items() if a in RETRIEVE and blocked(p))
    r["_sitewide_block"] = r["robots"].get("has_star_block", False)

def pct(k): return f"{k}/{n} ({round(100*k/n)}%)"

# ---------- matrix.md ----------
KEYTYPES = ["Organization","FAQPage","Product","Offer","BreadcrumbList","AggregateRating",
            "SoftwareApplication","MedicalBusiness","Article","VideoObject"]
lines = ["# AIO/SEO signal matrix — 88 companies", "",
         "Deterministic harvest (harvest.py). `llms`=llms.txt present · `LD#`=distinct JSON-LD @types · "
         "`schema`=notable types deployed · `AInamed`=AI crawlers given their own robots group · "
         "`AIblock`=hard-blocked (Disallow:/) · `hl`=hreflang locale count.", "",
         "| company | vertical | llms | LD# | notable schema | AI named | AI hard-block | hl |",
         "|---|---|:--:|:--:|---|---|---|:--:|"]
for r in sorted(rows, key=lambda x:(x["vertical"], x["slug"])):
    schema = ",".join(t for t in KEYTYPES if t in r["jsonld"]["types"]) or "—"
    nm = ",".join(a.replace("Bot","").replace("-Extended","-Ext") for a in r["_named"]) or "—"
    bl = ",".join(a.replace("Bot","").replace("-Extended","-Ext") for a in r["_named_block"])
    if r["_sitewide_block"]: bl = "ALL(*)" + ("," + bl if bl else "")
    bl = bl or "—"
    llms = "✓" if r["llms_txt"]["present"] else ("—" if r["robots"]["ok"] else "?")
    lines.append(f"| {r['slug']} | {r['vertical']} | {llms} | {r['jsonld']['n_types']} | "
                 f"{schema} | {nm} | {bl} | {r['hreflang_count'] or ''} |")
open(f"{OUT}/matrix.md","w").write("\n".join(lines)+"\n")

# ---------- rollups ----------
print("=== CLEAN ROLLUPS (n=88) ===\n")
print("llms.txt present:", pct(sum(1 for r in rows if r["llms_txt"]["present"])))
print("llms-full.txt present:", pct(sum(1 for r in rows if r["llms_full_txt"]["present"])))
print("any JSON-LD:", pct(sum(1 for r in rows if r["jsonld"]["n_types"])))
print("names >=1 AI crawler in robots:", pct(sum(1 for r in rows if r["_named"])))
print("blocks >=1 RETRIEVAL bot (AIO own-goal):", pct(sum(1 for r in rows if r["_blocks_retrieve"])),
      "->", [r["slug"] for r in rows if r["_blocks_retrieve"]])
print("site-wide block of all bots:", pct(sum(1 for r in rows if r["_sitewide_block"])),
      "->", [r["slug"] for r in rows if r["_sitewide_block"]])

print("\n--- llms.txt by vertical ---")
by = defaultdict(lambda:[0,0])
for r in rows:
    by[r["vertical"]][0]+=1; by[r["vertical"]][1]+= 1 if r["llms_txt"]["present"] else 0
for v,(tot,has) in sorted(by.items(), key=lambda x:-x[1][1]):
    print(f"  {v:<20} {has}/{tot}")

print("\n--- JSON-LD @type x vertical (companies deploying) ---")
verts = sorted(set(r["vertical"] for r in rows))
print(f"  {'type':<20}" + "".join(f"{v[:9]:>11}" for v in verts))
tc = Counter()
for r in rows:
    for t in r["jsonld"]["types"]: tc[t]+=1
for t,_ in tc.most_common():
    if t not in KEYTYPES and t not in ("WebSite","SearchAction","WebPage"): continue
    cells = []
    for v in verts:
        c = sum(1 for r in rows if r["vertical"]==v and t in r["jsonld"]["types"])
        tot = sum(1 for r in rows if r["vertical"]==v)
        cells.append(f"{c}/{tot}")
    print(f"  {t:<20}" + "".join(f"{c:>11}" for c in cells))

print("\n--- AI crawler: NAMED (deliberate) / of which hard-block / of which allow ---")
from harvest import AI_CRAWLERS
for a,kind in AI_CRAWLERS.items():
    nm = sum(1 for r in rows if a in r["_named"])
    bk = sum(1 for r in rows if a in r["_named_block"])
    al = sum(1 for r in rows if a in r["_named_allow"])
    if nm: print(f"  {a:<20} [{kind:<8}] named {nm:>2}  block {bk:>2}  allow {al:>2}")

print("\n--- sitemaps declared in robots ---")
print("  sites declaring >=1 Sitemap:", pct(sum(1 for r in rows if r['robots'].get('sitemaps'))))
print("\nmatrix.md written.")
