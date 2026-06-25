# Market Read

## Question

Across the store's 5 marketplace/commission entities (airbnb, etsy, doordash, uber,
upwork), does the universal `offering_category` / `business_model` / price-visibility
frame express what a reader needs about a two-sided platform — take rate, GMV, supply
vs demand side — or is it a run-035-style gap where the industry holds the entity but
the schema cannot carry its economics?

`store-only` calibration. n=5, the full marketplace cohort in the store (not a sample).

## Result

**Split verdict. The schema's entity-shape fields fit marketplaces *well* — better than
they fit investors (run-035). But the schema has no structured home for marketplace
*economics* (take rate, GMV, supply-vs-demand-side fee split), which live entirely in
body prose. The headline is a schema *win* on classification with a narrow, bounded
field gap on quantitative economics — not a run-035 "no positive shape" failure.**

Three findings, State / Signal / Judgment kept distinct.

**1. The classification fields are a clean, designed-for fit (State).**
All 5 carry `business_model: Marketplace / Commission` and `Marketplace / Platform` in
`offering_category` (doordash pairs it with `Software / SaaS` for its merchant-tooling
side; the other 4 are single-value `[Marketplace / Platform]`). Both are real closed-set
values
(TAXONOMIES `Marketplace / Platform` :47, `Marketplace / Commission` :83), and the
schema's own example companies for those values are literally **Airbnb and Uber**
(TAXONOMIES:47). So these two fields were *designed with marketplaces in mind* — they
are not telehealth-overfit. This is the first non-telehealth entity shape the lab has
read where the schema names the shape **positively and accurately** out of the box.
Contrast run-035: investors got an *empty* `business_model` (a subtractive gate);
marketplaces get a *populated, designed-for* one.

**2. The economics have no structured home — they're prose-only (State + Gap).**
What a marketplace reader actually wants — take rate, GMV, which side pays — is captured
**richly but only as body prose / `unverified_fields`**, never as a greppable field:

| Brand | Take rate (verbatim, from prose) | GMV/scale | Side that pays | On-site? |
|---|---|---|---|---|
| etsy | 6.5% transaction + $0.20 listing + 3%+$0.25 payment + 15% offsite-ads | $11.9B GMS (2025, **consolidated** — Etsy + Reverb + Depop, *not* Etsy.com alone; not unit-comparable to a single-brand GMV) | seller (supply) | **yes** — full schedule on /sell |
| doordash | 15% / 25% / 30% delivery commission tiers, 6% pickup | — | merchant (supply) + consumer fees | **yes** — /about FAQ |
| upwork | 3–5% (Basic) / 8–10% (Business Plus) client service fee | >$4B client spend, >$750M rev | client (demand) + supply memberships | **yes** — /pricing/client |
| airbnb | host + guest service fees, **% not disclosed on site** | "8M listings" (marketing copy) | both sides | **no** — explicit `unverified_fields` |
| uber | "takes a commission"; % not disclosed; Uber One $9.99/mo | off-site (IR only) | both sides | **no** — IR/10-K scope |

The structured fields touch this only obliquely: `target_market` (B2C/B2B/B2B2C) gestures
at two-sidedness but does not encode *which side is monetized*; `portfolio_shape`
(Multi-product/Catalog) is orthogonal. There is no `take_rate`, `gmv`, or
`monetized_side` field, and on the evidence of this cohort that is the only real gap.

**3. The economics gap splits two ways — schema-can't vs firm-didn't (Judgment, the
contracted trap).** Applying the run-035 two-stacked-absence discipline:
- **schema-can't:** no structured take-rate / GMV / fee-side field exists — true for all 5.
- **firm-didn't-on-site:** airbnb and uber don't publish fee % on their *marketing* site
  (it's in 10-Ks, out of capture scope); etsy, doordash, upwork **do** publish on-site,
  and the store **captured it verbatim in prose**.

So the store is **not blind to take rate** — for 3/5 it already holds decision-grade,
verbatim fee schedules. The honest gap is narrow: the economics are **prose, not
field**. Whether they *should* be a field is the L005 question (does a cross-marketplace
reader cut — "all marketplaces with take rate >20%" — exist that prose can't serve?). At
n=5, heterogeneous (travel / crafts / food / rides / work), and with the numbers mostly
incomparable in unit (per-listing vs per-delivery-tier vs per-contract), the prose
already answers it; a structured field would be sparse and unit-mismatched. Reads as
**"no new primitive needed,"** with at most a documented prose/query convention — the
same anti-sprawl landing as run-035 W1.

## Gap Map

**Answered cleanly (store-only):**
- Marketplace *classification* — both shape fields fit all 5 perfectly; the schema is
  not overfit here.
- Take rate / fee structure for the 3 brands that disclose on-site (etsy, doordash,
  upwork) — verbatim in prose.
- The two-sided *narrative* (who supplies, who pays) for all 5 — clearly in body prose.

**Fell short (store-only):**
- No structured economics fields → no cross-marketplace quantitative cut at query time
  (can't `grep` "take rate >20%"; must read prose).
- airbnb + uber fee % **not captured** — marketing sites don't show it; would need a
  filings source family (10-K / IR), out of this run's scope. Say *not captured*, not
  *not charged*.
- The price-visibility token has a **grain mismatch** on marketplaces: it tags the
  *consumer offering* price (airbnb tags Homes `[published]`, Trip services `[partial]`),
  but a marketplace's own "price" as a product is its **take rate**, which the token
  does not address. The token answers "can a buyer get a price," not "what does the
  platform charge."

**What would change the answer:** a real downstream consumer who needs a *structured*
cross-marketplace economics cut (not prose), plus a 2nd, larger, more homogeneous
marketplace cohort to show the numbers are comparable enough to structure. Absent both,
prose wins.

## Evidence Used

All store-only; capture clocks from each `profile.md` frontmatter. No external/live
sources, no spend.

- **C1 — cohort denominator:** `grep -rl '^business_model: Marketplace / Commission'
  store/*/profile.md` → 5 (airbnb-com, etsy-com, doordash-com, uber-com, upwork-com).
  Full cohort, not a sample.
- **C2 — classification fit:** each profile's `offering_category` + `business_model`
  frontmatter (all 5 identical); closed-set values at TAXONOMIES.md:47 and :83 (example
  cos = Airbnb, Uber).
- **C3 — take-rate prose:** etsy profile.md:67–72 (verbatim fee schedule, /sell);
  doordash profile.md:65–67 (commission tiers, /about FAQ); upwork profile.md:59–60
  (service fees, /pricing/client).
- **C4 — undisclosed-on-site:** airbnb profile.md:28 + :73 + :131 (fee % not on captured
  pages); uber profile.md:71 + :106 ("takes a commission"; financials IR-only).
- **C5 — GMV/scale prose:** etsy profile.md:120 ($11.9B GMS); upwork profile.md:103
  (>$4B client spend).
- **C6 — price-visibility token grain:** airbnb profile.md:62/65/68 (consumer-offering
  tokens); SCHEMA.md:142 (token defines "can I get a price?", per-offering, consumer-side).

Capture clocks: airbnb 2026-06-04; etsy / doordash / uber / upwork 2026-05-31. No
market-sensitive claim here turns on freshness (this is a schema-fit read, not a
pricing read); fee figures are quoted as *captured*, not asserted as *current*.

## Companies Seen

5/5: airbnb-com, etsy-com, doordash-com, uber-com, upwork-com. Spread across 5
`primary_industry` values (Hospitality, Retail/E-Commerce, Logistics, Automotive,
Technology) — the marketplace shape is **industry-orthogonal**, which is exactly why
`business_model` (not `primary_industry`) is the field that recovers the cohort. A
naive industry-based draw would never assemble this cohort; `business_model` is the
right key, and it worked.

## Missing / Stale Coverage

- `offerings.md`: only **1/5** (airbnb) carries one — consistent with the schema
  default ("first enabled set: telehealth; default elsewhere is don't write the file,"
  SCHEMA.md:215). Not a gap, a contracted default.
- airbnb + uber on-site fee % genuinely absent (firm-didn't-on-site); not stale, just
  off-surface.
- No capture is stale for this question — all 2026-05-31/06-04, and the schema-fit
  verdict doesn't depend on point-in-time economics.

## Source Gaps

- **Filings / IR source family** (10-K, investor relations) is the missing panel for the
  take rate of marketplaces that don't disclose on-site (airbnb, uber). The store has no
  filings-derived economics layer; the SEC tool (`tools/`) captures *existence/funding
  footprint*, not take-rate/GMV. This is the marketplace analogue of L003 (decision-grade
  bodies uncaptured) — here the uncaptured ingredient is *platform economics from
  filings*. Spend/approval-gated; out of this run's store-only scope.

## Raw Learning to Preserve

See `run-notes.md` Observations: O1 (classification fits — first positive non-telehealth
schema fit), O2 (economics are prose-not-field), S1 (two-stacked-absence resolved: store
holds 3/5 take rates in prose), G1 (price-visibility token grain mismatch on
marketplaces), G2 (filings source family missing for off-site economics), W1
(anti-sprawl: convention not field). One row per sighting for Loop 2 to append.

## External Completeness Check

Not run — completeness is not load-bearing for a calibration read of a 5/5 internal
cohort, and the contract is store-only. The denominator (5) is the full set of
`Marketplace / Commission` profiles, verified by grep, not an estimate. (Noted as a
deliberate skip, not an oversight — cf. run-035 G2 where a Scout denominator estimate
missed; here the denominator is grep-exact.)

## Market Pattern

1. **`business_model` is the load-bearing field for the marketplace shape, and it
   works.** The cohort is industry-scattered; only `business_model: Marketplace /
   Commission` recovers it. This is positive evidence that the closed set's marketplace
   value earns its place (unlike the empty-investor case, run-035 O1).
2. **The schema captures marketplace *shape* but not marketplace *economics*.** Shape =
   structured + designed-for; economics (take rate, GMV, monetized side) = prose-only.
   That's a cleaner, narrower gap than run-035's "no positive field set at all."
3. **The real marketplace "price" is the take rate, and the price-visibility token
   doesn't reach it.** The token is consumer-offering-grained; a platform's monetization
   price is the fee on the *other* side. A genuine grain insight, not a defect to fix at
   n=5.

## What Would Change This Answer

- A downstream consumer who needs a **structured** cross-marketplace economics cut
  (filterable take rate / GMV), not prose — would move W1 from "convention" toward a
  field candidate.
- A **2nd, larger, more homogeneous** marketplace cohort (e.g. 8–10 food-delivery or
  e-commerce marketplaces) showing the take-rate numbers are unit-comparable enough to
  structure — the n=5 heterogeneity is the main reason prose wins today.
- A **filings/IR source family** capture for airbnb + uber take rate — would close the
  firm-didn't-on-site half of the economics absence (spend/approval-gated).

"No new primitive needed" remains the honest landing: the schema fits the marketplace
shape, the economics are prose-carried and mostly disclosed, and a structured economics
field would be sparse, unit-mismatched, and consumer-less at n=5.
