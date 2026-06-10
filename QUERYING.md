# QUERYING — how to read the store

> **What this is.** The consume-side companion to [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md): they define what a `profile.md` *contains*; this defines how to *get answers out*.

A `/research-company` agent already paid to capture and structure each company, so a reader **filters that structure instead of re-scraping**. If the question asks for an external signal the store does not hold yet — SERP visibility, Wayback tenure, Trustpilot profile state, branded Trends, Exa neighbors — use [`tools/`](tools/README.md) to capture that source as JSON instead of generic web search. The only thing you have to get right is matching the question to the tool — that's the difference between a one-line answer and a wrong one.

## The one rule: query shape picks the tool

| Your question is… | Use | Because |
|---|---|---|
| **Locate** — does X appear, where, quote it verbatim | `rg` / `grep -r` (the whole corpus is ~100KB) | line-oriented and cheap; you want the raw text |
| **Structure** — filter / group / aggregate / relate on frontmatter | **parse the YAML** (below) — never `grep \| uniq` | values carry inline `#` comments, and multi-selects aren't order-canonical (`[B2C, B2B]` ≠ `[B2B, B2C]`), so `grep \| uniq` silently fragments the count |
| **Presentation** — hand a non-technical human a company brief | `python scripts/render.py <company>` → clickable local link to `scripts/_out/briefs/<slug>.html` | static, self-contained, and provenance renders with the artifact |
| **External signal** — visibility, tenure, review profile, branded search trajectory, similar-site discovery | `tools/<source>.py` → JSON envelope, then match/diff/interpret above it | repeatable source capture with provenance beats one-off web search |

The store is `store/<domain-slug>/`:
- `profile.md` — **frontmatter** (structured, closed-set, valid YAML) + **body** (the prose sections SCHEMA defines: Overview, What they offer, …).
- `captures/<date>/*.md` — cleaned pages, **verbatim** primary source.
- `captures/<date>/images/<sku>.<ext>` — **product reference imagery** (opt-in; absent on most companies): a flagship's clean **hero product render**, captured for a design / rendering-reference consumer and cited from the `offerings.md` deep block. A binary asset, not greppable — look here when you need the picture, not the text.

A folder **without** `profile.md` is a **stub** — a raw capture cache, not a dossier. `python scripts/store.py find <x>` distinguishes profiles from stubs explicitly; "is X captured?" means "does `store/<x>/profile.md` exist?"

Frontmatter is valid YAML, so the structured reader is five lines (PyYAML + stdlib `glob`):

```python
import glob, yaml
def frontmatter(p):
    t = open(p).read()
    return yaml.safe_load(t.split("---", 2)[1]) if t.startswith("---") else {}
P = {p.split("/")[1]: frontmatter(p) for p in glob.glob("store/*/profile.md")}
# P -> {slug: {field: value}}; lists come back as lists.
```

**Resolve the company to its key first.** Domain is the key — but a question arrives as a *name*, an *old domain*, or an *alias*. `python scripts/store.py find <x>` (or `from store import resolve`) folds any surface form to the one slug; hand-matching silently misses non-obvious hits (`SendGrid → twilio-com`, `chatgpt.com → openai-com`, `salesloft.com → clari-com` post-merger). This and the relations join-check (Recipe 3) are the only two reads worth a script — everything else below is a one-line filter.

## Recipes

**1. Single-company brief** — when a human-facing query resolves to exactly one profiled company, run `python scripts/render.py <company>`.

`render.py` prints a ready-to-paste markdown link line — paste it into your reply verbatim (don't re-derive the path; it's pre-wrapped in angle brackets for the spaces). **A rendered brief whose link never reaches the reply is invisible** — the paste is part of the answer, not a flourish. Treat the link as a companion artifact, not a replacement: alongside it, add whatever concise synthesis helps the conversation. Skip the render when the ask is atomic (one field, one price, one quote), cross-company/cohort, machine-readable, agent-internal, or outside store scope/current-state.

**2. Filter / group** — *"all B2C subscription brands", "group by business_model"* → parse, then query the dict. (Value strings live in TAXONOMIES — read them there, don't hardcode.)
```python
from collections import Counter
Counter(p.get("business_model") for p in P.values())                 # group-by single-select
[s for s,p in P.items() if "B2C" in (p.get("target_market") or [])]  # membership on multi-select
```
Multi-selects are **ranked** — position 1 is *primary*. `tm[0]=="B2B"` means "primarily B2B"; membership means "sells B2C at all." Test membership, never equality.

`socials` (channels they operate) and `external` (third-party records about them — crunchbase/wikipedia/bloomberg/…) are both `{platform: url}` maps — test key presence (`"linkedin" in (p.get("socials") or {})`, `"crunchbase" in (p.get("external") or {})`). `socials` arrived at `schema_version` 2.1, `external` at 2.2. The whole corpus was backfilled + re-stamped to 2.2, so an empty/absent value here now means "looked, none found"; the grandfather rule still governs any *future* field (empty on a profile older than the field = "predates it," not "has none" — check the stamp before reporting a negative).

**3. Relations** — *"who owns X", "all brands of Y"* → `parent` / `owns` hold a **dotted domain** (joinable to another profile, folded via `canon()`) or a **quoted name** (no domain, so not joinable — expected).
```python
{s: p.get("owns") for s,p in P.items() if p.get("owns")}
```
To see which targets actually resolve to a held profile — and rank the dangling ones as re-capture candidates by in-degree (the parent two captured brands share is the highest-value next capture) — run `python scripts/store.py relations`. Doing this by eye across the corpus miscounts.

**4. Cross-brand pricing** — *"compare GLP-1 prices across the cohort"* → the hard path, with a real ceiling:
- **Intra-cohort only.** "Price" isn't comparable across business types (`$/mo` vs take-rate `%` vs AUM fee vs per-night) — compare within one like cohort.
- **Locate, then reconcile by hand.** Prices live in body prose (What they offer / How it works), not frontmatter — but enumerable lines lead with a bold name + verbatim price (`- **name:** … $X`), so `rg -n '^- \*\*.*\$[0-9]' store/<slug>/profile.md` enumerates priced lines. Units still fragment even within a cohort (first-month, membership-stacked, billing cadence) — normalize manually.
- **Per-SKU + molecule grouping — where `offerings.md` exists (opt-in cohorts).** When a company carries `store/<slug>/offerings.md` (the per-SKU layer; telehealth cohort today; contract [`OFFERINGS.md`](OFFERINGS.md)), it beats the family-line grep: the **roster** is one row per SKU with a verbatim `Price` + `Visibility` cell, and `What` **leads with the molecule** (`semaglutide · oral · …`). So `rg -n 'semaglutide' store/*/offerings.md` enumerates that molecule across every brand's SKUs in one pass — the cross-brand grouping key, computed at **query time**, never stored. Two cautions: still hand-normalize the price *value* (units fragment as above), and the molecule is **page-attested** — a `not stated` cell means the page was silent, *not* a cue to infer from the brand. Here `price_visibility` is the roster's own per-SKU cell, not the family-line token.
  - **Counting SKUs as breadth?** Trust a roster count only when that file's frontmatter reads **`enumeration: indexed-complete`**, and read it *with* `portfolio_shape` (for a `Catalog`, "complete" = exemplars, never a census). **`lines-omitted`** = the count is a **floor** — a whole line was skipped (the Provenance scope note names which); **`unknown`/absent** = predates the field, drop to the scope prose. Never rank brands on a naked `sku_count` — the Ro.co trap (an 8-SKU `lines-omitted` run on a ~36-SKU brand sorted dead-last). `enumeration` joins `key_pages` / `unverified_fields` / Provenance as the signals that tell "not offered" from "not captured."
- **Visibility *is* queryable — the value isn't.** Each `What they offer` line carries a `` `[published | partial | on-request]` `` token (SCHEMA → [price-visibility](SCHEMA.md#price-visibility)), so *"who even publishes a price vs. gates it behind intake"* is one grep — `rg -n '\[on-request\]\|\[partial\]' store/<slug>/profile.md` — even though the price *number* still needs the hand-normalize above. Absent token on a **pre-`2.3`** profile = "predates the convention," not "published" — check the stamp before reporting a negative. (In an `offerings.md` cohort, grep the roster's `Visibility` column instead — it's per-SKU.)

**5. Primary source** — *verbatim claims / disclaimers / taglines* → `profile.md` paraphrases; the captures keep exact wording: `rg -n '<phrase or variant>' store/<slug>/captures/*/*.md`. Guess variants for regulated language ("not approved" / "not evaluated").

**6. Cohort cross-cut** — *"within telehealth: who owns their pharmacy and leads with men?"* → where a company carries `store/<slug>/telehealth.md` (a **cohort pack** — telehealth today; contract [`TELEHEALTH.md`](TELEHEALTH.md)), its frontmatter is the same valid-YAML closed-set surface as `profile.md`, parsed the same way and **joined on the slug**. The pack exists *because* the universal classification reads near-identical across a cohort — so these are the cuts that actually separate players *within* it.
```python
TH = {p.split("/")[1]: frontmatter(p) for p in glob.glob("store/*/telehealth.md")}   # same frontmatter() as above
# the within-cohort scan: integrated pharmacy + men-led + TRT front door
[s for s,t in TH.items() if t.get("pharmacy_model") == "integrated"
   and t.get("audience") in {"men-only", "men-first"} and t.get("anchor_category") == "TRT"]
```
Closed sets live in [`TELEHEALTH.md`](TELEHEALTH.md), not here. **`unclear`/empty is "looked, couldn't tell," not "no"** — a sparse pack (a platform/lab) honestly leaves cuts blank, so check before reporting a within-cohort negative. **Cross-company comparison is computed here, at query time** — it's never stored in the pack (a baked "one of only two who…" rots when the cohort grows; that's the anti-reconciliation line). Judgments (threat/fit) aren't in the pack at all — they're a consumer-side read over it.

**7. Corpus lens + cohort aggregation — SQLite.** When a question wants *many* one-off pivots at once — *"who sells semaglutide anywhere in the corpus?", "semaglutide SKUs by `pharmacy_model`", "who gates vs. publishes", or just browse-and-sort the store in a GUI* — rebuild before reading: `python scripts/build_db.py && python scripts/build_db.py --check`. It writes the stable, gitignored cache at `scripts/_out/store.db`. The markdown store remains source of truth; the database is the rung-3 derived lens, regenerated on demand.

It's deliberately **scoped + fenced** so it can't hand back a fast, clean, *confident-wrong* answer:
- **Counts read through `enumeration`, never naked** (Recipe 4's count-trust rule, built into the schema). Every `sku_count` rides beside the `enumeration` cut, and `catalog_breadth` renders a `lines-omitted` count as `≥N (floor)` and an `unknown` one as `N (unverified)` — only an `indexed-complete` count is a bare number safe to rank on.
- **No price magnitude.** Only `price_verbatim` — there is no `price_num` by design (a first-`$` grab is *wrong, not lossy*: `$749` parsed for a $166/mo SKU; teasers sort below real prices). SQLite will coerce leading-digit text if you ask it to `AVG(price_verbatim)`; that is visible garbage, not a supported price answer. Recipe 4's hand-normalize ceiling is unchanged.
- **Molecule is `LIKE`, never `GROUP BY`.** No `molecule` column — group with `what LIKE '%semaglutide%'` (Recipe 4's grep, in SQL); a stored key fragments "testosterone" into ~30 buckets.
- **Corpus-wide lookup, cohort-gated ranking.** `companies` carries every profile; `offerings` carries every `store/*/offerings.md` roster row, so lookup questions don't silently miss non-telehealth rosters. Ranked aggregate surfaces stay inside cohort views such as `telehealth_full` (`<cohort>_full` naming convention), where the cohort cuts make the comparison meaningful.
- **Freshness is inside the db.** `_meta` sorts first in Beekeeper and carries `built_at`, row counts, and caveat rows; `_meta_days_old` recomputes staleness live on every open. `coverage` is one row per `store/*` folder, including stubs, with `has_profile` / `has_offerings` / `has_telehealth`, the three module clocks, and `enumeration`. A Beekeeper connection can keep reading a deleted inode after rebuild; if `_meta_days_old` stays old, reconnect.
- **`unclear`/empty ≠ "no"** (Recipe 6), and **three freshness clocks** on `telehealth_full` — `captured_at`, `telehealth_captured_at`, `offerings_captured_at`: a fresh profile can sit over a month-old roster.

`python scripts/build_db.py --check` is the drift self-test — a renamed roster column, cohort cut, missing `coverage` row, reintroduced price magnitude, or roster that parses to zero rows fails loudly instead of misbuilding silently. The engine owns this faithful, fenced corpus lens; projects own judgment lenses built on the parsers (canonical molecule, normalized price, enrichment). For a *single* pivot the Recipe 4/6 one-liners beat SQL — reach for the lens when the *number* of cuts makes ad-hoc SQL (or a GUI) win.

**8. Source-signal capture — tools before generic web search.** The store is site-derived State; it does not automatically know whether a brand is visible in Google, how old a SKU URL is, whether a Trustpilot profile is active, or how branded search interest moved. For those questions, run the focused capture in [`tools/`](tools/README.md) and keep interpretation above it:
- `serpapi.py` — organic + AI Overview visibility for a query; match with `_match.py` / `serp_match.py` when a cohort is involved.
- `serp_intent_panel.py` — query-set + cohort buyer-intent SERP panels over captured `serpapi.py` envelopes; use this when deciding whether category queries are worth tracking. Live capture happens only with explicit `--fetch-missing`.
- `wayback.py` — exact-URL archived tenure; reads as a lower bound, not a launch date.
- `trustpilot.py` — one Trustpilot profile state at one `captured_at`; velocity needs repeat captures.
- `trends.py` — branded search trajectory within each keyword, not absolute cross-brand volume.
- `exa_similar.py` — neighbor discovery / blind-spot finding.

These tools print JSON envelopes to stdout and do **not** write the store. Save captures project-side or in an experiment until a reusable method earns a home.

## Gotchas & limits

**Before trusting a negative.** *"Company X doesn't do Y"* can mean **not offered** or **not captured**. Three signals tell them apart — check before reporting: `key_pages` (what the capturer treated as signal), `unverified_fields` (what it explicitly couldn't get), and the **Provenance** body section (pages analyzed + what was missed).

**Answer trust.** Quote the governing clock, the enumeration floor, and any `unverified_fields` in every answer — point reads end with `as of <captured_at> (Nd)` (use the module's own clock for module-layer facts); cohort answers use a range form (`captures 2026-05-30..06-07, oldest 10d`) rather than per-row clauses; counts cite their `enumeration` status; fields in `unverified_fields` get said out loud. `python scripts/store.py find <x>` puts the clocks in the output — copy, don't recall.

**Can't answer yet:**
- **Numeric / range price** ("under $200/mo") — still no structured price *value* field (verbatim strings only, by design); hand-normalize, don't fake a table. The per-SKU `offerings.md` (opt-in cohorts) tightens this to one row per SKU with a verbatim price + query-time molecule grouping (Recipe 4) — but the value is still a string to normalize, never a sortable number. *(Price **visibility** — gated vs. published — is queryable; see Recipe 4.)*
- **Cross-type price** comparison — not meaningful (see Recipe 4).
- **Corpus lens / cohort aggregation** — the derived SQLite lens now covers corpus `offerings` lookup plus cohort-gated aggregate views (Recipe 7); the *corpus-wide* relation graph (`parent`/`owns` across all types) still has no index — fine at this N, the rung-3 item for when discovery/traction demands it.
- **Events** (news/funding/M&A), **judgments** (threat/fit/relevance), **financials** (revenue/headcount) — out of scope by design. The store holds durable *state*; these are a deep-research job that reads the store as priors (see the Frame).

---

*Authority + drift: SCHEMA / TAXONOMIES are the contract — this doc names fields and mechanics, never value lists. If a recipe here disagrees with them, trust the contract and re-derive the recipe. A **major** bump means re-check the recipes with `scripts/querycheck.py` (a minor/additive bump can't break an existing recipe).*
