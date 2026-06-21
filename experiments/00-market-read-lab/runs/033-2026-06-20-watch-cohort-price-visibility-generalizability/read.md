# Market Read

## Question

Across the captured watch brands (Rolex, Patek Philippe, Audemars Piguet, A. Lange & Söhne, Cartier, Swatch, Casio), how does each present and price its catalog online — and does the lab's `published / partial / gated` price-visibility axis still mean the same thing for physical luxury goods, where access is gated by **dealer / boutique / scarcity** convention rather than by **sales-intake**?

## Result

**Two-part result: (1) a brand-by-brand price-presentation map a reader wants, and (2) a recipe-generalization verdict.**

### (1) The watch-cohort price-presentation map

| Brand | Tier | Online price? | Gate mechanism | Captured evidence |
|---|---|---|---|---|
| **Rolex** | Luxury | **None** (C1) | Dealer — sells *only* through authorized Official Jewelers; configurator + store-locator, no cart/e-commerce | profile.md site_notes + unverified_fields |
| **Patek Philippe** | Luxury | **None** (C2) | Dealer/Salon — "price on request," global authorized-retailer network, no cart | profile.md site_notes + unverified_fields |
| **Audemars Piguet** | Luxury | **None** for watches (C3) | Boutique — brand-showcase site driving to boutique appointments; a *service* price list exists (uncaptured) | profile.md site_notes + unverified_fields |
| **A. Lange & Söhne** | Luxury | **None** (C4) | Boutique — *every* model reads "Price upon request" (boutique-led) | profile.md site_notes + unverified_fields |
| **Cartier** | Luxury (multi-category) | **Split** (C5) | Watches "request appointment" (gated); **jewelry $2,130–$38,520 and fragrance $49–$355 published** | profile.md unverified_fields + Overview |
| **Swatch** | Accessible | **Yes** (C6) | Full DTC e-commerce, inline prices ($75–$235 core; Scuba collab $420). Exception: **MoonSwatch in-store-only, no online price** (scarcity-gated) | profile.md What-they-offer + site_notes |
| **Casio** | Accessible (diversified electronics) | **Yes** (C7) | Full DTC storefront, inline prices across watches (~$100–$165+), pianos ($99–$449+), calculators (~$11–$140s). Exception: **Moflin price behind add-to-cart** | profile.md What-they-offer + site_notes |

**Reader takeaway:** the captured watch market splits cleanly into a **luxury tier that publishes no watch price online by convention** (Rolex, Patek, AP, Lange — and Cartier *for watches*) and an **accessible tier that publishes everything** (Swatch, Casio). Cartier is the instructive straddler: its *watches* are appointment-gated while its *jewelry and fragrance* are fully priced — the gate runs at **category grain inside one brand**, not brand grain.

### (2) Recipe-generalization verdict

**The `published / partial / gated` axis generalizes — but "gated" is not one thing, and the gate's *grain* and *meaning* both change.**

- **The axis composes.** Every one of the 7 brands maps onto published / partial / gated without distortion: Swatch & Casio = published; Cartier = partial; Rolex/Patek/AP/Lange = gated. So the lab's most-reused cut (008/013/023 telehealth, 028 SaaS) survives a third, maximally different vertical. `query-time-grouping-enough` fires cross-vertical again.
- **A third gate *type* appears.** Telehealth gating = **sales-intake** (start a medical questionnaire to see price); SaaS gating = **enterprise-quote** (talk to sales); luxury gating = **dealer/boutique/scarcity convention** (the price exists and is known to the dealer, but is deliberately withheld from the public site). These are *not* interchangeable: the telehealth/SaaS gate is a **conversion-funnel** mechanism (capture the lead, then reveal), whereas the luxury gate is an **exclusivity / channel-margin / allocation** posture — for Rolex and Patek the operative scarcity gate is the *waitlist/allocation* at the dealer, not the website at all. **Judgment:** reading luxury "price on request" through the telehealth intake-gate lens would mislabel a market posture as a funnel tactic.
- **The gate runs at three grains, not one.** Brand grain (Rolex: whole catalog gated), **category grain** (Cartier: watches gated, jewelry/fragrance published), and **product grain** (Swatch MoonSwatch and Casio Moflin: single SKUs gated/withheld inside an otherwise-published catalog). The telehealth reads mostly saw brand-grain gating; this vertical surfaces sub-brand grains as first-class.
- **"Gated" ≠ "not captured" (the contracted failure mode held).** For all four luxury maisons, "no online price" is recorded as a **deliberate market posture** ("price on request" / "no e-commerce, sold via authorized retailers"), verbatim from the brands' own site_notes/unverified_fields — *not* as a capture failure. Absence language is "not published," not "not true" and not "we failed to capture."
- **Run-028 trap re-confirmed.** 0/7 watch brands have an `offerings.md` or the SCHEMA structured price-visibility token (`[published|partial|on-request]`). The entire read came from `profile.md` **prose** (the run-010 prose-surface variant + site_notes/unverified_fields). A naive `rg '\[on-request\]'` would return nothing and could be misread as "watch brands don't gate price" — the exact inverse of the truth (5 of 7 gate at least their watches). The empty *structured* surface is a coverage signal, not a market fact (MRL-008 run-028 branch), and it is a **backfill gap, not a recipe defect** (the prose carries the signal cleanly).

**No new primitive needed.** The read is a query-time grouping over existing prose State; it wants no `price_visibility` enum migration, no `gate_type` field, and no durable watch-cohort object. The one *if-it-ever-recurs* nugget is a vocabulary one: distinguish **gate-type** (intake / enterprise-quote / dealer-scarcity) and **gate-grain** (brand / category / product) when reading price visibility — held as recur-watch, not a build.

## Gap Map

| Sub-question | Truffle answered? | Evidence | Where it fell short |
|---|---|---|---|
| Does each watch brand publish a watch price online? | **Clean** | profile.md prose for all 7 | None — every brand's posture is explicit in capture |
| Why is the price withheld (gate mechanism)? | **Clean for posture, partial for mechanism** | site_notes name the channel (dealer/boutique/salon) | The *scarcity/allocation/waitlist* layer (esp. Rolex/Patek) is market knowledge, **not on captured pages** — labeled Judgment, not State |
| Can the read distinguish gate *type* and *grain*? | **Clean** | category-split (Cartier) and product exceptions (MoonSwatch, Moflin) all captured | None |
| Does the structured price-visibility token carry the signal? | **Clean (negative)** | 0/7 token/offerings.md present | Token is unpopulated off telehealth — must read prose; this is the run-028 finding, re-confirmed |
| Actual price *levels* for luxury watches | **Not answerable** | — | No luxury watch prices exist on any captured page (deliberate); would need an external dealer/grey-market panel |

## Evidence Used

All store-only, all captured 2026-05-31 (primary = each brand's own site, captured via Firecrawl). No external/live sources.

| ID | Claim | Source (local path) | Grade |
|---|---|---|---|
| C1 | Rolex publishes no prices anywhere; sells only via authorized Official Jewelers, no cart | `store/rolex-com/profile.md` (site_notes, unverified_fields, What-they-offer) | primary (brand site) |
| C2 | Patek has no e-commerce and no public prices; sold via authorized retailers/Salons, price on request | `store/patek-com/profile.md` (site_notes, unverified_fields, description) | primary |
| C3 | AP publishes no watch prices on .com; brand-showcase → boutique appointments; a service price list exists but is uncaptured | `store/audemarspiguet-com/profile.md` (site_notes, unverified_fields) | primary |
| C4 | A. Lange publishes no prices; every model "Price upon request" (boutique-led) | `store/alange-soehne-com/profile.md` (site_notes, unverified_fields) | primary |
| C5 | Cartier watches are "request appointment" (gated); jewelry ($2,130–$38,520 Love line) and fragrance ($49–$355) prices are published | `store/cartier-com/profile.md` (unverified_fields, site_notes) | primary |
| C6 | Swatch runs full DTC e-commerce with inline prices ($75–$235 core; Scuba $420); MoonSwatch is in-store-only with no online price | `store/swatch-com/profile.md` (What-they-offer, site_notes) | primary |
| C7 | Casio runs a full DTC storefront with inline prices across watches/pianos/calculators; Moflin price is behind add-to-cart | `store/casio-com/profile.md` (What-they-offer, site_notes) | primary |
| C8 | 0/7 watch brands carry an `offerings.md` or the SCHEMA `[published\|partial\|on-request]` token | `ls store/<d>/` + `grep` (this run) | primary (store state) |

## Companies Seen

7 brands. Luxury: rolex-com, patek-com, audemarspiguet-com, alange-soehne-com, cartier-com. Accessible: swatch-com, casio-com. (cartier carries jewelry+fragrance+watches; casio carries watches+instruments+calculators+Moflin — both diversified beyond watches.)

Denominator note: `primary_industry: Consumer Goods` returns 6 (the 5 luxury maisons + swatch); **casio sits under `primary_industry: Technology`** despite being a watch-catalog brand, so a `Consumer Goods` grep alone **under-counts watch brands by 1** — the same anchored-only/cross-field under-count flavor MRL-001 names for telehealth cohorts, now on a non-telehealth slice. The cohort was hand-drawn to include casio.

## Missing / Stale Coverage

- All 7 captured 2026-05-31 (~20 days old at read time) — uniform clock, fine for a structural posture read; luxury "price on request" posture is stable, accessible-tier prices are point-in-time.
- No `offerings.md` for any of the 7, so there is no enumerated SKU roster or structured `Visibility` column — read relied on `profile.md` prose. (This is the depth-backfill gap, not a defect.)
- AP service-price-list page and Lange repair/overhaul pricelist are referenced in capture but **not captured** — out of scope for a watch-price read anyway (maintenance pricing ≠ product pricing).

## Source Gaps

- **Actual luxury watch price levels** are unreachable from any owned brand site by design — would need an external panel (authorized-dealer MSRP sheets, Chrono24/grey-market) to ever state a Rolex/Patek/Lange price. Out of scope (store-only); flagged for honesty, not pursued.
- The **scarcity/allocation/waitlist** dynamic (the *real* luxury gate) is market knowledge, not owned-page State — correctly held as Judgment.

## Raw Learning to Preserve

Append to `discovery-ledger.md` in Loop 2: run-notes Discovery ledger IDs **O1** (gate-type taxonomy: intake/enterprise-quote/dealer-scarcity), **O2** (gate-grain: brand/category/product, with Cartier as the category-grain straddler), **O3** (run-028 token-absence re-confirmed on a 3rd vertical), **S1** (luxury "price on request" is a posture, not a funnel — semantic mismatch with telehealth intake-gate), **G1** (casio cross-field under-count of the watch cohort), and **W1** (the gate-type × gate-grain vocab nugget, recur-watch).

## External Completeness Check

Not run — store-only by contract. The cohort denominator (7) is small and hand-verified against `primary_industry` greps (Consumer Goods = 6 + casio under Technology). Completeness of the *named-watch-market* is not load-bearing for this read: the question is about **presentation posture of captured brands**, not "did we capture every watch brand." A future bounded-live coverage-radar (the run-012/022/024 recipe) could test whether the captured 7 are representative of the watch market, but that is a separate run.

## Market Pattern

The watch vertical reproduces the **same price-visibility axis** seen in telehealth and SaaS, with a stark, reader-legible split: **luxury withholds, accessible publishes.** The generalizable lesson for Truffle is not a new field but a **reading discipline**: price visibility is one universal axis, but its `gated` value hides at least three distinct **gate types** (sales-intake, enterprise-quote, dealer-scarcity) operating at three **grains** (brand, category, product). The store already holds enough prose State to recover all of this at query time; the only real gap is that the *structured* price-visibility surface (`offerings.md` + token) is unpopulated off telehealth, so cross-vertical price reads must go through prose — exactly as run 028 found for SaaS, now confirmed a second time.

## What Would Change This Answer

- If `offerings.md` + the structured price-visibility token were backfilled for the watch brands, the read could move from prose to a greppable cut (and the run-028 trap would dissolve) — a depth-backfill, not a recipe change.
- If a luxury maison launched genuine online watch e-commerce (a real market shift, not a capture artifact), the luxury "gated-by-convention" finding would weaken — a freshness-monitoring concern.
- If a second cross-vertical price read surfaced the same gate-type × gate-grain distinction, the recur-watch vocab nugget (W1) would harden toward an MRL-002 reading-discipline addend.
