# Design: activate `offerings.md` — roster-first, store-only

> **What this is.** The activation decision for the Tier-1 `offerings.md` module, grounded in the
> [2026-06-03 tournament](../experiments/2026-06-03-offerings-tournament/FINDINGS.md) (3 designs × 4
> telehealth companies, produced → adversarially verified → answered cold). It **resolves the "§Activation
> — open"** left by the [2026-06-01 design](2026-06-01-offerings.md) and **revises that draft's body
> shape**: lead with the roster, demote deep blocks to earned, reject the molecule-pivot. Companion to the
> [frame](2026-05-29-frame.md) (scope) + [architecture](2026-05-30-architecture.md) ("Modules: recipes,
> not just schemas"). **Codified 2026-06-03** — §Activation steps 1–6 landed (SCHEMA Tier-1 stub,
> the [§1.1 capture recipe](../skills/research-company/firecrawl-capture.md), `scripts/offeringscheck.py`
> lint, the QUERYING molecule-grouping recipe); settled on [`store/hims-com/offerings.md`](../store/hims-com/offerings.md),
> fanning out the rest of the telehealth cohort. Notion promotion (step 7) stays propose-only.*

## Verdict

**Build it — and the baseline loses decisively.** For the live per-SKU/molecule consumer (the
Teleprescribe Venture's Products/SKUs), a roster-first `offerings.md` beat "extend `profile.md`" on the
decisive molecule-grouped price query — **8.3 vs 5.5**, **35 vs 14** molecule×form rows — and was the
only contestant that prices *all four* brands' GLP-1s (the family line leaves Ro's lineup gated). This is
**not** a "narrow win → extend `profile.md`": the gap is the grain itself. A `profile.md` family line
collapses six GLP-1 SKUs into one bullet and has no room for six prices; forcing them in would bloat the
cross-corpus point-read for a per-SKU consumer that is cohort-specific. The module is the right
**separation of concerns** — and crucially it is **free over the baseline capture** (same pages, zero
marginal Firecrawl).

But build it **leaner than the 2026-06-01 draft**: the win is the **roster**, not the rich blocks.

## The record — roster-first

A separate opt-in doc, own `captured_at` (pricing goes stale fast — the reason it is its own module).
Frontmatter is doc-meta only; the offerings live in the body. **Body order is inverted from the draft:
the roster is the load-bearing core; the overview is brief; deep blocks are *earned*, not a default top-N.**

```markdown
---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: ro.co               # company key; each offering's slug (its relative url) is its key *within* the company
captured_at: 2026-06-03     # own freshness; captures/<date>/ holds the source pages
---

## Portfolio overview
<brief: how the lines relate + the breadth-first hierarchy + the "shape" finding (e.g. "Ro's
'testosterone' is an OTC supplement, not TRT"). For a `Catalog` company this IS the main content.>

## Roster   ← the load-bearing core; complete at the indexed level
| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Wegovy pill | buyable | Ro Body | /weight-loss/wegovy-pill/ | `$149 first month` · `$199-$299 thereafter` | [partial] | semaglutide · oral · cash-only; dose ladder + membership gate cost |
| …one row per offering at the indexed level… |

## Deep blocks   ← EARNED, not default
<a rich block ONLY where a verbatim H1 / exact price footnote / positioning resolves a real ambiguity a
roster row can't — e.g. a gated line whose only price is an FAQ figure ("$99/mo, 10-month prepaid"), or a
"this isn't actually TRT" disambiguation. Spine then verbatim gold. NOT a top-N-by-default.>
```

**The roster is the spine.** Columns are the [2026-06-01 draft's](2026-06-01-offerings.md) six spine
fields, reordered for this consumer: `Offering`(name) · `Kind`(family|buyable, an annotation) · `Parent` ·
`Slug`(the within-company key) · `Price`(verbatim, footnotes quoted) · `price_visibility` · `What`. The
one change: **`What` leads with `molecule · form · access`** — page-attested, the greppable grouping
attribute. The draft's three *earned* fields (`includes` / `audience` / `notes`) stay earned and live in
deep-block prose / footnotes, never as roster columns.

**Molecule is a descriptive attribute, never a pivot or a key.** It rides the front of `What` so
`rg semaglutide store/*/offerings.md` enumerates it cross-brand at query time — but it is **page-attested
only** (where a page doesn't state the molecule, write "not stated"; never infer it from the brand name)
and it is **not** a sort/lead column and **not** a stored canonical entity. This is the anti-Doro line the
probe *proved* load-bearing: the molecule-pivoted contestant (B2) gained zero resolution over baseline yet
tagged Mounjaro "tirzepatide" with no page support and botched its own declared slugs. Within-company key
stays the slug; cross-company grouping stays query-time.

**Prominence lives in the overview's *emphasis narrative*, not a per-SKU field.** What the company leads
with vs. buries is a key Portfolio-overview signal — but a per-row `prominence` column is a fill-the-box
hallucination trap (the molecule-pivot's mistake). So it stays a holistic, **calibrated** read in
`## Portfolio overview`, confidence tied to signal stability:

- **HIGH** — the company's *own* label (a `"Best seller"` / `"Most Popular"` badge) or an explicit hero,
  corroborated across ≥2 signals. **MED** — section order / nav depth / CTA repetition / relative visual
  weight. **LOW** — a single weak cue, a rotating or A/B-tested hero, or carousel SKU order. Tag every
  claim inline; honest subjectivity beats false precision.
- Four rules the prominence probe (2026-06-03; 2 readers each on Hims + Ro, strong agreement) surfaced:
  **(1)** popularity badges are emphasis, stock tags (`"In stock"`, `"New dose"`) are *not*;
  **(2)** scope badge detection to *rendered text*, not a raw `rawHtml` grep (Hims's 59 "Featured" hits
  were all the `FeaturedTile` CSS class); **(3)** exclude alphabetically-sorted index pages (Ro's
  `/pricing`) from order inference; **(4)** a rotating hero still gives the *category* lead even when the
  exact creative is LOW.

## The recipe — how to gather

The module's gathering recipe (the half the draft underweighted) — a **two-pass** method: map the
portfolio + its prominence (breadth), then deepen the flagships (depth). `portfolio_shape` is the depth
dial (`Single` / `Flagship + companions` / `Multi-product` → enumerate the set; `Catalog` → shape +
exemplars only, per the [draft's table](2026-06-01-offerings.md#granularity-breadth-completeness-vs-depth)).

**Enumerate the roster with the cheapest tool that works — not `/scrape`-everything** (probed live,
2026-06-03):

| Tool | Job | Cost | Caveat |
|---|---|---|---|
| Scrape the category/index page | the **backbone** — the company's *own* product-card links + labels + order | 1 cr/page | authoritative, structure-independent; doubles as the prominence read |
| `site:domain/<category-path>` search | **accelerant** — a labeled SKU list, catches unlinked PDPs | 2 cr / 10 | clean **only where products & content live in separate URL paths** (Hims `/weight-loss/<sku>` → 7/7 SKUs clean; Ro nests articles under `/weight-loss/` → ~20%, noisy). Cross-check, don't trust blindly |
| `/map` | a flat slug **census** across categories | ~1 cr (per call) | under-returns on big sites; mixes content |

Decision rule: glance at the map — products & content in separate paths → `site:domain/path` search ~nails
the roster cheaply; else fall back to the index scrape. **Never** enumerate with keyword/brand search
(returns SEO noise — the generic query found 1 of 7 SKUs), and **never** read prominence from a search
`position` (Google rank ≠ the company's emphasis). `/crawl` (scrapes everything) and `/extract`
(token-billed, Beta-flaky) stay off the roster path.

**Then deepen, with the capture rules:**
- **Verbatim is mandatory** on every price string **with its footnotes** (the `†`/`*` membership +
  dose-ladder notes decide `[partial]` vs `[published]`); quote the page H1 in any deep block.
- **Gating is a finding** — a quiz/app/membership-gated price still gets a row (`[on-request]`/`[partial]`
  + the floor that *is* shown).
- **Molecule and form from the page only** — never inferred from a brand name (the B2 lesson).
- **Prominence capture flags are load-bearing:** `fullPage` screenshot (the default is above-the-fold
  only — full-page is the *only* way to read what's demoted/absent), `rawHtml` + `onlyMainContent: false`
  (where the company's own badges + section order live), and **persist the `.png`** (its URL expires in
  24h). Do the prominence read **at capture time** — those payloads prune on a curve and can't be
  re-derived later.

**Cost:** ~**10–20** Firecrawl credits for a ~20-SKU `Multi-product` company (`Single` ~4–6; `Catalog` =
map census + index scrapes only). Most of the roster reads off 1–2 index pages + a `/pricing` page;
per-PDP scrapes are reserved for the flagships — so marginal cost over the core capture stays small.

## Destination — store-only (B), with the baseline verdict

- **Where it lands: the `web-research` store**, `store/<domain>/offerings.md`. It is durable **State** (what
  the company sells, from its own pages), opt-in per project/cohort, own freshness TTL.
- **`profile.md` keeps the family lines + price-visibility token** (SCHEMA 2.3). That is the **cross-corpus
  point-read** for all ~45 companies and the 80% case; `offerings.md` is the **opt-in per-SKU layer** for
  the cohort with a live per-SKU consumer (telehealth first). The two are not redundant — they are two
  grains at two costs. When `offerings.md` is active for a company, it **owns `price_visibility` per-SKU**
  (as SCHEMA already anticipates); the `profile.md` token remains the convention everywhere else.
- **The explicit baseline verdict:** *extend `profile.md` was carried as a full contestant and lost
  decisively for this consumer* — but it **wins** for the family-grain point-read, which is why it stays.
  The module earns its existence **only** for the per-SKU/molecule grain, **only** where that consumer is
  live. Default elsewhere remains: don't write the file.
- **Promotion to Notion = sketched, not designed (propose-only, later).** A roster row maps cleanly to the
  venture's **Products/SKUs** (Offering→Product, slug→SKU key, Price/Visibility→fields), molecule→a query-time
  **Categories** grouping. Per your call this round, we **do not** design that mapping now — the store
  artifact is the deliverable; promotion is a separate propose-don't-write step against the co-authored
  Notion.

## What changed from the 2026-06-01 draft (the simplification pass)

Every edit earns a cut — the probe retired three things the draft carried:

| Draft (2026-06-01) | This proposal | Why (probe evidence) |
|---|---|---|
| Body order: overview → **deep blocks** → roster ("rich content first, the long list last") | **Roster first**; deep blocks **earned**, not default top-N | Cold agents answered from the roster; deep blocks earned ~3 correctness-guard cells, else "merely restated roster prices" |
| Molecule → `notes`; pivot left open | Molecule **leads `What`**, page-attested; **no** pivot, **no** canonical molecule column | B2's molecule-pivot gained 0 rows over baseline **and** induced hallucinated canon + key errors |
| Deep blocks justified partly on rich per-SKU detail (incl. dose) | **Don't chase dose** — capture verbatim where shown, "not stated" otherwise | Dose absent for ~20/SKUs (provider-titrated, gated); not a fillable axis here |
| 9-field core | **Same core, reordered**; `includes`/`audience`/`notes` stay earned (deep-block only) | Spine fields filled 100%; earned fields lightly used — kept, not promoted |

## Activation checklist

> **Build status (2026-06-03):** ✓ **1** (SCHEMA stub rewritten) · ✓ **2** (recipe → [`firecrawl-capture.md` §1.1](../skills/research-company/firecrawl-capture.md)) · ✓ **3** (lint = **`scripts/offeringscheck.py`**, a dedicated per-file linter rather than folding into `querycheck.py`/`fc.py` — the fan-out's verifiers run it on one draft) · ✓ **4** (opt-in = *the file exists*; telehealth is the enabled set — no config mechanism) · ✓ **5** (QUERYING Recipe 4 molecule grep) · ✓ **6** (`schema_version: "1.0"`, `profile.md` untouched; seeded from the probe artifacts) · ⊘ **7** (Notion promotion — propose-only, deferred as designed). Settled on `store/hims-com/offerings.md`; remaining tournament companies fan out next.

1. **SCHEMA Tier-1 stub** → point `offerings.md` to this doc; update the stub one-liner to *roster-first
   (overview → roster → earned deep blocks), molecule leads `What`, deep blocks earned*.
2. **Recipe into the verb** → add the offerings gathering recipe to [`firecrawl-capture.md`](../skills/research-company/firecrawl-capture.md)
   / `/research-company`: the **enumeration ladder** (index-scrape backbone → `site:domain/path` search on
   clean-taxonomy sites → `/map` census), the `portfolio_shape` depth dial, verbatim+footnotes,
   gating→still-write-the-row, molecule-from-page-only, and the **prominence capture flags** (`fullPage`
   screenshot + `rawHtml` + `onlyMainContent:false`, persist the `.png`; read prominence at capture time).
3. **Lint** → add `offerings.md` checks to `querycheck.py` / `fc.py`: roster column presence, `price_visibility`
   closed-set, every row slug-keyed, **grep-verifiable price** (every price findable in a cited capture),
   **no cross-company canonical key**.
4. **Config** → opt-in per project/cohort; enable for the telehealth cohort first (the live consumer).
5. **QUERYING.md** → add a recipe: `rg` the `What` molecule token across `offerings.md` files for
   cross-brand molecule grouping (the rung-2 digest path; revisit a derived column only if a digest/
   aggregation consumer is actually built).
6. **No backfill** → new module doc carries its own `schema_version: "1.0"`; `profile.md`'s contract is
   untouched (the family-line token stays). Seed from the 4 probe artifacts already under
   [`experiments/2026-06-03-offerings-tournament/artifacts/`](../experiments/2026-06-03-offerings-tournament/artifacts/).
7. **Promotion (later, propose-only)** → design the roster→Notion Products/SKUs mapping when promotion is
   the live task; not now.

## Deferred / non-goals (unchanged + reaffirmed)

- **No `{value,unit,cadence}` price struct, no canonical molecule key, no per-SKU depth for `Catalog`
   companies** — all reaffirmed by the probe (heavy normalization stays project-side; molecule grouping
   stays query-time).
- **Dose-level comparison** — unserved by design; the sites don't publish it. Re-open only if a dose
  consumer appears *and* a vertical publishes dose.
- **A derived molecule column / digest helper** — deferred until a real cross-company aggregation consumer
  (rung-2/3) exists; the `What`-embedded molecule serves query-time grep today.

---

<sub>**Sources** — the [2026-06-03 tournament](../experiments/2026-06-03-offerings-tournament/FINDINGS.md)
(verdict, scorecards, cold answers, 12 artifacts, 15-credit captures), extended by the **recipe + prominence
probes** (2026-06-03 — live Firecrawl `/search` vs `/map` tests + a 4-reader prominence read on Hims & Ro);
supersedes "§Activation — open" and
revises the body shape of [2026-06-01-offerings.md](2026-06-01-offerings.md); grounded upstream in
[Probe 0](../experiments/2026-06-01-profile-enrichment/FINDINGS.md) (why the family grain stays with
`profile.md`). Authored 2026-06-03.</sub>
