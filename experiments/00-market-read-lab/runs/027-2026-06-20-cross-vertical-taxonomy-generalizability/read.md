# Market Read

## Question

Is Truffle's universal classification taxonomy telehealth-overfit? Read the
non-telehealth slice of the store (~54 operating companies + 7 investor/holding entities,
across Technology, Finance/VC, Consumer Goods/watches, Energy, Automotive, Industrial)
and map where the closed-set classification fields (`offering_category`,
`primary_industry`, `business_model`, `portfolio_shape`, `entity_type`) strain,
improvise per-row rules, or go empty — and where they carry cleanly.

This is a calibration / system-test run. The value is mapping where the engine's central
"universal fields + reusable cuts" claim holds vs strains beyond its one design vertical.

## Result

**Verdict: the universal taxonomy is *not* broadly telehealth-overfit. It carries the
non-telehealth slice cleanly for any operating company that sells a product or service.
It has exactly one structural break — and that break is not telehealth-shaped at all:
capital allocators (VC / PE / asset managers).**

**Where it carries cleanly (the large majority):**

- **Luxury watches (7 brands).** Uniform and correct: all `offering_category:
  [Physical Products / Hardware]`, all `business_model: Transactional / One-time`, all
  `primary_industry: Consumer Goods` (except Casio → `Technology`, defensible — it's an
  electronics maker). The maker-vs-reseller rule held (no brand mislabeled
  `Retail / E-Commerce`). `portfolio_shape` varied appropriately — `Catalog` for
  Rolex/Patek/Cartier/Swatch/Casio, `Flagship + companions` for AP (Royal Oak hero),
  `Multi-product` for A. Lange. (C2)
- **Tech / SaaS (~22).** Clean and well-differentiated: `Usage-based / Consumption` for
  the metered players (Datadog, Snowflake, AWS, Stripe) vs `Subscription` for seat/plan
  players (Linear, Notion, OpenAI); `portfolio_shape` spread `Single → Catalog`
  sensibly. No `Other`, no forced empties. (C3)
- **Consumer Goods, Automotive, Marketplace, Energy** rows classify without escape
  hatches. Store-wide, `Other` appears in a category field exactly **once** (see below),
  and `entity_type` is `Other`-free.

**The one structural break — capital allocators (7 `Investor / Holding` entities):**

- `offering_category` resolves **four different ways across the 7 firms** for what is
  essentially the same business (allocating capital): (C4)
  - `[]` empty — spero-vc, thrivecap, standishspring (3, per the Investor/Holding
    gating rule)
  - `[Financial / Fintech Products, Services / Consulting]` — firstround, sequoiacap (2)
  - `[Financial / Fintech Products]` — blueowl (1)
  - `[Services / Consulting]` — lsvp (1)
  The gating rule ("Investor/Holding → leave `offering_category` empty") is followed by
  only **3 of 7**. Four of the seven inline-flag the strain themselves:
  *"a capital-allocating VC firm has no sellable product/service in the taxonomy"* and
  *"no dedicated VC/asset-management value in the set."*
- `business_model`: 6 of 7 empty; blueowl forced `Other` — *"management +
  performance/incentive fees on AUM; no taxonomy value fits asset-management fee
  economics."* This is the store's **only** `business_model: Other` (and the only
  category-field `Other` store-wide). (C5)
- **Net effect:** the closed-set grouping promise breaks here. You cannot filter
  `offering_category = X` to retrieve "all capital allocators" — they are scattered
  across `[]`, `[Financial]`, `[Financial, Services]`, `[Services]`. The taxonomy has no
  value for *investing / asset management / capital allocation* as an offering, and none
  for *fees on managed capital* as a model. `entity_type: Investor / Holding` correctly
  flags the entity, but it is the **only** field carrying the read, and the gating rule
  meant to compensate is applied inconsistently.

**Why this is the honest result, not telehealth bias:** the break has nothing to do with
telehealth. It is a *non-offering entity type* — a firm whose "product" is capital. The
taxonomy's `Scope` line says it up front: *"commercial companies + products."* Capital
allocators sit at the edge of that scope, and the slice exposed it because the slice is
where they live.

## Gap Map

| Field | Carries cleanly | Strains gracefully (designed escape, honest note) | Breaks (no fitting value / inconsistent) |
|---|---|---|---|
| `entity_type` | All 126 profiled rows (119 `Company`, 7 `Investor / Holding`); `Other`-free | — | — |
| `offering_category` | Watches, SaaS, Consumer, Auto, Marketplace | doordash maker-disambiguation note; firstround/sequoia chose `[Financial, Services]` | **Investor/Holding: 4 encodings across 7 firms**; gating rule honored 3/7 |
| `business_model` | Watches (`Transactional`), SaaS (`Usage-based`/`Subscription`) | telehealth à-la-carte rows (defymedical, marekhealth, hydramed) flag the model honestly | **blueowl `Other`** — no AUM/fee value; 6/7 allocators leave it empty |
| `portfolio_shape` | SaaS + watches; tie-breaker worked (AP, A. Lange) | AP `Flagship + companions` despite catalog-scale (noted); investor empties per gating rule | — (the empties are correct, not breaks) |
| `primary_industry` | Tech, Consumer Goods, Auto, Finance | doordash `Logistics` (operating-core call), runway `Finance & Fintech` for an FP&A SaaS (noted) | — (graceful; `Finance & Fintech` absorbs both the firms and their fintech tooling) |

**Secondary gap (denominator / hygiene, not taxonomy):** 9 of 135 store directories are
**capture-only stubs with no `profile.md`** — belmarpharmasolutions, ddpmedical,
dewittpharma, exaveyra, mdpep, medsupplysolutions, norexi, pfizerpro, stemnova (all
pharma/supply-adjacent). They have raw `captures/` but no synthesized profile, so they
carry **none** of the classification fields. Any "135 captured companies" denominator
over-counts *profiled* companies by ~7% (true profiled N = 126). (C6) This is an
MRL-001-flavored denominator caveat, surfaced incidentally.

## Evidence Used

All evidence is store-local frontmatter (already-captured State); no external or current
claims, so no URL/date receipts are required. Store clock = each profile's `captured_at`
(2026-05-31 era for the watch/tech slice). Claim IDs:

- **C1** — Slice definition: 126 profiled companies carry `entity_type` (119 `Company`,
  7 `Investor / Holding`); ~54 are non-Healthcare operating companies by
  `primary_industry`. Source: `grep ^entity_type:`, `grep ^primary_industry:` over
  `store/*/profile.md`. (receipt R1)
- **C2** — Watch slice uniformity. Source: 7 watch `profile.md` frontmatter. (receipt R1)
- **C3** — SaaS slice clean differentiation. Source: 6-row Tech sample frontmatter. (R1)
- **C4** — 7 `Investor / Holding` firms; `offering_category` resolves 4 distinct ways;
  gating rule honored 3/7. Source: per-firm frontmatter + inline `# STRAIN` comments
  (spero-vc:38, thrivecap:34, firstround:44, sequoiacap:40). (receipt R1)
- **C5** — `business_model: Other` appears exactly once store-wide (blueowl), for AUM fee
  economics. Source: `grep "business_model: Other" store/*/profile.md` → 1 hit. (R1)
- **C6** — 9 capture-only stubs lack `profile.md`. Source: `ls store/<stub>/` → `captures`
  only. (receipt R1)

## Companies Seen

- **Investor / Holding (7):** blueowl, firstround, sequoiacap, spero-vc, thrivecap,
  standishspring, lsvp.
- **Watches (7):** rolex, patek, audemarspiguet, alange-soehne, cartier, swatch, casio.
- **Tech/SaaS sample:** datadoghq, snowflake, linear, notion, aws-amazon, openai, stripe,
  runway (+ ~15 more in the Technology industry bucket).
- **Other non-telehealth verticals touched:** doordash (Logistics), uber/ford/electra
  (Automotive), nike/peloton/hyperice (Sports), etsy/warbyparker (Retail), airbnb
  (Hospitality), 5 Energy, 2 Industrial.
- **Capture-only stubs (9, no profile):** belmarpharmasolutions, ddpmedical, dewittpharma,
  exaveyra, mdpep, medsupplysolutions, norexi, pfizerpro, stemnova.

## Missing / Stale Coverage

- No external denominator was needed (the read is about the schema's behavior on what's
  captured, not about market completeness).
- The 9 stubs are a coverage gap but not a staleness one; they were never profiled.
- Captures are 2026-05/06 era; no field here is freshness-sensitive (classification is
  durable State).

## Source Gaps

None for this question — it is a pure intrinsic read of captured State and the two
contract docs (SCHEMA/TAXONOMIES). The only "source" that would change the answer is a
*decision*, not data: whether the engine wants to represent capital allocators as a
first-class shape (see What Would Change).

## Raw Learning to Preserve

`run-notes.md` Discovery ledger IDs to append to `discovery-ledger.md` in Loop 2:
O1 (taxonomy not telehealth-overfit — carries Tech/Consumer/Auto cleanly), O2 (the one
break is capital allocators), S1 (4-way offering_category split on one entity_type),
S2 (blueowl is the lone store-wide `Other`), G1 (no investing/asset-management value),
G2 (9 capture-only stubs / denominator caveat), O3 (brand_color STRAIN markers dominate
the `# STRAIN` grep but are a Firecrawl-payload issue, not a taxonomy issue —
don't conflate), W1 (if anything graduates, an entity-type-gated convention beats a new
offering value).

## External Completeness Check

Not load-bearing here — completeness is intrinsic (every profiled `store/` row was
scanned for the 5 fields; the slice is the whole non-Healthcare set, not a sample for the
headline counts). The Tech "sample" rows are illustrative; the Investor/Holding (7),
watch (7), and stub (9) sets are complete enumerations.

## Market Pattern

1. **The universal layer is genuinely universal for *sellers*.** Across watches, SaaS,
   consumer, auto, and marketplace, the closed sets fit without escape hatches. The
   telehealth design did not overfit the *operating-company* case — a reassuring result
   for the "reusable across verticals" claim.

2. **The taxonomy's edge is the *non-offering entity*, not a vertical.** The single
   structural break (capital allocators) is an `entity_type` story, not an industry
   story. The schema already anticipated it (`Investor / Holding` exists; the gating rule
   exists) — but the rule is under-specified enough that 7 firms produced 4 encodings.
   The escape hatches worked *as safety valves* (nothing was forced into a wrong value),
   but they did **not** preserve groupability — the whole point of closing the sets.

3. **"Strain" ≠ "break."** ~Two dozen inline `# STRAIN` markers exist store-wide, but the
   overwhelming majority are `brand_colors` / `logo` / `design_framework` notes —
   Firecrawl branding-payload corrections, a *capture-fidelity* issue orthogonal to the
   classification taxonomy. Only ~6 strain markers touch a classification field, and 5 of
   those are the capital-allocator cluster. Reading the brand-color strains as taxonomy
   defects would badly overstate the problem (the contracted failure-mode trap — avoided).

## What Would Change This Answer

- **A decision to make capital allocators first-class.** The minimal fix is *not* a new
  `offering_category` value (which would re-import the "is investing a service?" debate);
  it is an **`entity_type: Investor / Holding`-gated convention** that pins one encoding
  (e.g. always `offering_category: []` + a `business_model` value for fee/AUM economics,
  or a dedicated `Investor / Holding` non-offering note field). The recurrence is real
  (7 firms, 4 encodings), which is exactly the "promote only when the gap recurs"
  threshold TAXONOMIES.md names. This is a triage candidate, not a Loop-1 action.
- **Profiling the 9 stubs** would move the true denominator from 126 → up to 135 and
  remove the over-count caveat; until then, count *profiled* rows, not directories.
- A larger non-telehealth capture pass (more allocators, more industrials) would test
  whether the allocator break is the *only* one or just the first found.
