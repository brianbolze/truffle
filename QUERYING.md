# QUERYING — how to read the store

> **What this is.** The consume-side companion to [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md). Those define what a `profile.md` *contains* (capture side); this defines how to *get answers out* (query side). **SCHEMA/TAXONOMIES are authoritative** — this doc names *fields and mechanics*, never the value lists. If a recipe here ever disagrees with the contract, trust the contract and re-derive the recipe. Written against **`schema_version: 1`**; a schema_version bump means the recipes need a re-check (`scripts/querycheck.py`).

The store is `store/<domain-slug>/`:
- `profile.md` — **frontmatter** (structured, closed-set, valid YAML) + **body** (prose sections defined in SCHEMA: Overview, What they offer, How it works, …).
- `captures/<date>/*.md` — cleaned pages, **verbatim** primary source.

## The one rule: query shape picks the tool

| Want to… | Use | 
|---|---|
| **Locate** — does X appear, where, quote it verbatim | `rg` / `grep -r` (line-oriented, cheap — the whole corpus is ~100KB) |
| **Structure** — filter / group / aggregate / relate on frontmatter | **parse the YAML** — do *not* `grep \| uniq` |

**Why not `grep \| uniq` for grouping:** frontmatter values carry inline `# …` comments with trailing padding, and multi-selects aren't order-canonical (`[B2C, B2B]` ≠ `[B2B, B2C]`) — so `grep \| uniq` fragments the count. The frontmatter is valid YAML; parse it. The reader is five lines (PyYAML, stdlib `glob`):

```python
import glob, yaml
def frontmatter(p):
    t = open(p).read()
    return yaml.safe_load(t.split("---", 2)[1]) if t.startswith("---") else {}
P = {p.split("/")[1]: frontmatter(p) for p in glob.glob("store/*/profile.md")}
# P -> {slug: {field: value}}; lists come back as lists.
```

## Recipes

**1. Point read** — *"tell me about <company>"* → `read store/<slug>/profile.md`. One ~10KB file; the SCHEMA body sections map to most asks. Works for every entity type. No tooling.

**2. Filter / group** — *"all B2C subscription brands", "group by business_model"* → parse, then query the dict. (Values are defined in TAXONOMIES — read them there; don't hardcode.)
```python
from collections import Counter
Counter(p.get("business_model") for p in P.values())          # group-by single-select
[s for s,p in P.items() if "B2C" in (p.get("target_market") or [])]   # membership on multi-select
```
Traps: multi-selects are **ranked** — position 1 is *primary* (`tm[0]=="B2B"` = "primarily B2B"; membership = "sells B2C at all"). Never equality-match a multi-select; never `grep|uniq` a closed-set field.

**3. Relations** — *"who owns X", "all brands of Y"* → `parent` / `owns` hold a **domain slug** (joinable to another profile) or a **quoted name** (no domain → not joinable, flagged per SCHEMA Rule B).
```python
{s: p.get("owns") for s,p in P.items() if p.get("owns")}
```
A quoted name has no profile to join to — expected. No SQLite index exists or is needed at this scale.

**4. Cross-brand pricing** — *"compare GLP-1 prices across the cohort"* → the hard path; respect the ceiling:
- **Intra-cohort only.** "Price" isn't comparable across business types (`$/mo` vs take-rate `%` vs AUM fee vs per-night). Compare within one like cohort.
- **Locate, reconcile by hand.** Prices live in body prose (What they offer / How it works), not frontmatter:
  `rg -n '\$[0-9]|/mo|per month' store/<slug>/profile.md`
  Units fragment even within a cohort (membership-stacked, first-month, billing cadence) — normalize manually.
- **Cannot** do numeric/range ("under $200/mo") — needs a structured price (`offerings.md`, not built). Say so; don't fake a table.

**5. Primary source** — *verbatim claims / disclaimers / taglines* → `profile.md` paraphrases; the captures preserve exact wording:
`rg -n '<phrase or variant>' store/<slug>/captures/*/*.md` — guess variants for regulated language ("not approved" / "not evaluated" / "does not verify").

## Before you trust a negative result
*"Company X doesn't do Y"* can mean **not offered** or **not captured**. Every profile carries three signals to tell them apart — check before reporting a negative:
- `key_pages` — what the capturer treated as signal-bearing,
- `unverified_fields` — what it explicitly couldn't get,
- the **Provenance** body section — pages analyzed + what was missed.

## What the store cannot answer yet
- **Numeric/range price** queries — no structured price (`offerings.md` deferred).
- **Cross-type price** comparison — not meaningful.
- **Relational JOINs at scale** — no derived index; fine at this N, a rung-3 concern.
- **Events** (news/funding/M&A), **judgments** (threat/fit/relevance), **financials** (revenue/headcount) — out of scope by design. The store holds durable *state*; these are a deep-research job that reads the store as priors (see the Frame).
