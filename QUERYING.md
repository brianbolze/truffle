# QUERYING — how to read the store

> **What this is.** The consume-side companion to [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md): they define what a `profile.md` *contains*; this defines how to *get answers out*.

A `/research-company` agent already paid to capture and structure each company, so a reader **filters that structure instead of re-scraping**. The only thing you have to get right is matching the question to the tool — that's the difference between a one-line answer and a wrong one.

## The one rule: query shape picks the tool

| Your question is… | Use | Because |
|---|---|---|
| **Locate** — does X appear, where, quote it verbatim | `rg` / `grep -r` (the whole corpus is ~100KB) | line-oriented and cheap; you want the raw text |
| **Structure** — filter / group / aggregate / relate on frontmatter | **parse the YAML** (below) — never `grep \| uniq` | values carry inline `#` comments, and multi-selects aren't order-canonical (`[B2C, B2B]` ≠ `[B2B, B2C]`), so `grep \| uniq` silently fragments the count |

The store is `store/<domain-slug>/`:
- `profile.md` — **frontmatter** (structured, closed-set, valid YAML) + **body** (the prose sections SCHEMA defines: Overview, What they offer, …).
- `captures/<date>/*.md` — cleaned pages, **verbatim** primary source.

Frontmatter is valid YAML, so the structured reader is five lines (PyYAML + stdlib `glob`):

```python
import glob, yaml
def frontmatter(p):
    t = open(p).read()
    return yaml.safe_load(t.split("---", 2)[1]) if t.startswith("---") else {}
P = {p.split("/")[1]: frontmatter(p) for p in glob.glob("store/*/profile.md")}
# P -> {slug: {field: value}}; lists come back as lists.
```

## Recipes

**1. Point read** — *"tell me about <company>"* → read `store/<slug>/profile.md`. One ~10KB file; the body sections answer most asks. No tooling, every entity type.

**2. Filter / group** — *"all B2C subscription brands", "group by business_model"* → parse, then query the dict. (Value strings live in TAXONOMIES — read them there, don't hardcode.)
```python
from collections import Counter
Counter(p.get("business_model") for p in P.values())                 # group-by single-select
[s for s,p in P.items() if "B2C" in (p.get("target_market") or [])]  # membership on multi-select
```
Multi-selects are **ranked** — position 1 is *primary*. `tm[0]=="B2B"` means "primarily B2B"; membership means "sells B2C at all." Test membership, never equality.

**3. Relations** — *"who owns X", "all brands of Y"* → `parent` / `owns` hold a **domain slug** (joinable to another profile) or a **quoted name** (no domain, so not joinable — expected).
```python
{s: p.get("owns") for s,p in P.items() if p.get("owns")}
```

**4. Cross-brand pricing** — *"compare GLP-1 prices across the cohort"* → the hard path, with a real ceiling:
- **Intra-cohort only.** "Price" isn't comparable across business types (`$/mo` vs take-rate `%` vs AUM fee vs per-night) — compare within one like cohort.
- **Locate, then reconcile by hand.** Prices live in body prose (What they offer / How it works), not frontmatter — but enumerable lines follow the SCHEMA **leaf shape** (`- **name** — … — verbatim price`), so `rg -n '^- \*\*.*\$[0-9]' store/<slug>/profile.md` enumerates priced lines. Units still fragment even within a cohort (first-month, membership-stacked, billing cadence) — normalize manually.

**5. Primary source** — *verbatim claims / disclaimers / taglines* → `profile.md` paraphrases; the captures keep exact wording: `rg -n '<phrase or variant>' store/<slug>/captures/*/*.md`. Guess variants for regulated language ("not approved" / "not evaluated").

## Gotchas & limits

**Before trusting a negative.** *"Company X doesn't do Y"* can mean **not offered** or **not captured**. Three signals tell them apart — check before reporting: `key_pages` (what the capturer treated as signal), `unverified_fields` (what it explicitly couldn't get), and the **Provenance** body section (pages analyzed + what was missed).

**Can't answer yet:**
- **Numeric / range price** ("under $200/mo") — no structured price field (`offerings.md` deferred). Say so; don't fake a table.
- **Cross-type price** comparison — not meaningful (see Recipe 4).
- **Relational JOINs at scale** — no derived index; fine at this N, a rung-3 concern.
- **Events** (news/funding/M&A), **judgments** (threat/fit/relevance), **financials** (revenue/headcount) — out of scope by design. The store holds durable *state*; these are a deep-research job that reads the store as priors (see the Frame).

---

*Authority + drift: SCHEMA / TAXONOMIES are the contract — this doc names fields and mechanics, never value lists. If a recipe here disagrees with them, trust the contract and re-derive the recipe. Written against `schema_version: 1`; a **major** bump means re-check the recipes with `scripts/querycheck.py` (a minor/additive bump can't break an existing recipe).*
