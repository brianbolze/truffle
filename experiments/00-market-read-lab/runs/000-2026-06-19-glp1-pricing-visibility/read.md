# Market Read

Status: answered 2026-06-19 (Run 0). Store-only; no scraping, no spend.
Governing clocks: captures 2026-05-30..06-18, oldest ~20d.

## Question

In GLP-1 / medical weight loss telehealth, which companies publish pricing, which hide
it behind intake, and what offer structures are becoming table stakes?

## Direct Answer

**Most of the cohort shows *a* number, but only a third shows a *real* one.** Across 229
priced GLP-1 SKUs in the store, **33% publish a self-contained price, 42% show only a
moving floor ("from $X/mo") that's finalized in gated intake, and 25% show nothing until a
consult or quiz.** Fully opaque is the minority — even most gate-led brands flash a
membership fee or a "starting at."

- **Publish real numbers** — the **compounded-only, flat-monthly** brands. Struct (`$99–$199`),
  Telo (`$199–$275/mo`), Pepti, Effecty, Good Life Meds, TRT Nation, Amble, AgelessRx. Price
  *is* the pitch, so they lead with it.
- **Publish a floor that moves (the plurality)** — "From $149/mo†", "starts at $179/month",
  where the dose/plan that sets the true price is chosen inside the gated flow. Henry (`$179`
  floor), Hims (`From $149†`), Ro, Ivim, Maximus, Dr Hank. Semi-transparent by design.
- **Gate fully** — the **clinic / consult-first** brands: Defy Medical, Kingsberg, Marek,
  ProHealth, Marque, Rugiet ("quiz-gated"). No number until you're in the funnel. Plus the
  *branded-drug* rows almost everyone punts to "retail pricing" / "+ insurance."

**Table stakes (offer structure):**
1. **A compounded semaglutide + tirzepatide entry pair** — near-universal; the price floor of the category.
2. **A microdose / low-dose tier** — fast-spreading cheaper entry (Henry, Ivim, Fridays, Shed, Noom, Good Life, Ivy, Invigor).
3. **Oral / sublingual variants** beside injectable (Henry, Pepti, Struct, Dr Hank, Direct Meds, Shed).
4. **A branded-drug access tier** (Wegovy / Zepbound / Ozempic / Mounjaro) at `$900–$1,900/mo` or "+ insurance" — the **newer** table stake as compounding tightens; usually `partial`/`on-request`.
5. **First-month and annual-vs-month-to-month discounting** as standard price *presentation*.
6. The real differentiator is **pricing architecture**: all-in flat monthly (visit+med bundled) vs **membership + medication cost** (Medvi `$99 + meds`, Ro Body `$39→$74 + meds`) vs **med-only à-la-carte** (Hims, LifeMD).

## Evidence Used

- **`store/*/telehealth.md`** (46 packs) — `anchor_category`, `access_model`, `pay_model`, `value_chain_role` to scope the cohort and split front-door GLP-1 from broader menus.
- **`store/*/offerings.md`** (47 GLP-1 rosters) — the `Visibility` column (`published|partial|on-request`) and verbatim `Price` per SKU. This is the workhorse; the visibility answer is one roster pass (QUERYING Recipe 4).
- **`store/*/profile.md`** bodies — to classify the no-module companies (altRx, the compounding pharmacies, OpenLoop).
- **`scripts/store.py resolve`** — to fold Notion denominator names to store slugs.
- Receipt: [`receipts/store-derived-glp1-list.md`](receipts/store-derived-glp1-list.md) (full list, reconciliation, aggregate).

Verbatim anchors (why a token is what it is):
- `published`: Struct Health — Oral Semaglutide **$99**, Injectable Semaglutide **$149** (own PDP).
- `partial`: Henry — *"price… varies by treatment plan and dosing, but starts at $179/month"* — floor moves with dose ⇒ `partial`.
- `on-request`: ProHealth — *"Personalized GLP-1 Injection — behind free consult"*; Rugiet — *"no price on page — quiz-gated."*

## Companies Seen

**48 DTC GLP-1 sellers** in the store (full slugs in the receipt):

- **GLP-1 is the front door (20):** altRx*, Brello, Direct Meds, Eden, Effecty, Good Life Meds, Henry, Hims, Medvi, Ivim, Ivy, Amble, Found, Fridays, Dr Hank, Noom, Remedy, Ro, Telo, Shed.
- **GLP-1 as one line in a TRT / longevity / sexual-health / multi menu (28):** AgelessRx, Defy, Healthspan, Opt, PeterMD, Geviti, Pepti, Wisp, Heva, Hone, HormoneMD, Hydra, Invigor, Joi&Blokes, Kingsberg, LifeMD, MaleMD, Marek, Marque, Maximus, Lifeforce, Nurx, ProHealth, RexMD, Rugiet, Sermorelin, Struct, TRT Nation.

\* altRx is a GLP-1-led DTC brand by its profile but lacks the `telehealth.md`/`offerings.md` layer.

**Surfaced by the same grep but *not* DTC sellers** (kept separate, per the anti-overcount lesson):
- Compounding-pharmacy **suppliers**: Hallandale, Mills, Strive (503A — they make GLP-1, don't sell a program).
- White-label **infra**: OpenLoop.

## Missing / Stale Coverage

- **Module-layer gaps inside the cohort:** altRx (GLP-1-led, no `telehealth.md`/`offerings.md`) and Marque (no `telehealth.md`) are profiled but can't be queried on the cohort cuts. Backfill candidates.
- **Branded-drug rows are the thinnest data.** Many `on-request` tokens are branded SKUs (Ozempic/Mounjaro) the brand lists but prices as "retail" / "+ insurance" — so "gated" here often means *"we don't set this price,"* not *"we hide ours."*
- **Freshness is fine.** Oldest cohort capture ~20d; Hims/Ro/Shed/Hone/LifeMD/Amble re-captured within the last few days. Pricing in this category churns (first-month promos, compounding-law shifts) — re-check before quoting a number live.
- **Price *magnitude* is not comparable as data** — verbatim strings only, by design. The floors above are hand-read, not a sortable table.

## Source Gaps

- The read needed nothing outside the store — no SERP, Wayback, or live fetch. **Visibility was already a captured field.**
- The one external source (the Notion Organizations seed) was *less* complete than the store on this cohort (see below) — so the gap wasn't "need more sources," it was "reconcile the two curated lists we already have."

## External Completeness Check

Denominator: the **Notion Organizations GLP-1 seed** — 34 primary rows
([`receipts/notion-organizations-glp1-denominator-seed.md`](receipts/notion-organizations-glp1-denominator-seed.md)), explicitly **not exhaustive**.

| | Count | Note |
|---|---|---|
| Notion primary rows | 34 | the seed |
| → confirmed GLP-1 sellers in store | **24 (71%)** | clean store hit rate |
| → profiled in store at all | 26 (76%) | incl. One Medical, which sells no GLP-1 |
| → absent from store | 8 | Citizen Meds, Gala, GoodRx, Klarity, Max Life, omzo, TMates, Trim Rx |
| **Store GLP-1 sellers *not* in Notion's primary list** | **~24** | Brello, Direct Meds, Eden, Healthspan, Opt, PeterMD, Geviti, Good Life, Pepti, Wisp, Heva, Hydra, Ivim, Amble, Found, Marek, Marque, Nurx, RexMD, Rugiet, Sermorelin, Struct, Telo, MaleMD |

**The two denominators overlap only ~50%, and each catches players the other misses.** The
store is *not* the smaller list here — it adds as many GLP-1 sellers as Notion's seed has in
total. Treat **union (≈48 store + 8 unprofiled Notion = ~56) as a floor**, not a census.

## Market Pattern

- **Visibility tracks the business model, not bravado.** Compounded-only flat-monthly ⇒
  publishes; dose-laddered or membership-stacked ⇒ floor (`partial`); consult-first clinic ⇒
  gate. You can almost predict the token from `access_model` + `compounding_posture`.
- **The category is converging on a menu, not a product:** compounded sema/tirz + microdose +
  oral + a branded up-tier, wrapped in first-month/annual discounting. Differentiation has moved
  from *"do you have GLP-1"* to *price architecture* and *how much is bundled*.
- **The branded-drug tier is the live edge.** Its prices are the most gated and the most
  volatile — the place a freshness/Signal layer would earn its keep if this becomes a tracked question.

## What Would Change This Answer

- **A bigger or differently-sourced denominator.** Both lists are curated and partial; a SERP/
  listicle panel would likely add more long-tail compounders and shift the published/gated ratio
  (long-tail cash-pay compounders skew `published`).
- **Compounding-law movement.** If 503A compounded GLP-1 access tightens, brands shift weight to
  the branded tier — pushing the cohort *more* gated (brand prices are `on-request`/insurance-set).
- **Re-capture drift.** First-month promos and "starting at" floors move week to week; a 2–3 week
  re-capture could move individual tokens (rarely the cohort shares).
- **Counting SKUs vs brands.** The 33/42/25 split is per-SKU; a brand-weighted view (one vote each)
  flattens toward an even three-way split. Both are in the receipt — pick the grain to the question.
