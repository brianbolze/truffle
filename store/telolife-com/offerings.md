---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: telolife.com        # company key; each offering's slug (its relative url) is its key *within* TeloLife
captured_at: 2026-06-04     # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "No per-plan PDPs — every plan lives on the single /packages page behind two toggles (Cash↔Financing, Semaglutide↔Tirzepatide); the only attested plan-param is /apply?plan=sema-6mo (homepage CTA). Monthly per-molecule rates are on /pricing ($199 sema / $275 tirz); bundle TOTALS are on /packages and were captured only for the Semaglutide toggle state (Tirzepatide bundle totals need the toggle flipped). Cherry 'As low as $X/mo' figures are FINANCING estimates, not the plan price — the bundle TOTAL is the price. Pricing is fully PUBLISHED (no quiz wall) — unusual for compounded-GLP-1 telehealth."
---

## Portfolio overview

TeloLife is **`Single`** — one offering, **compounded GLP-1 weight-loss therapy**, sold in **two molecules (semaglutide, tirzepatide) × five durations (month-to-month + 3/6/9/12-month bundles)**. There are no separately-positioned product lines; the SKU grid is molecule × commitment length, all at one all-inclusive cash rate per molecule.

**The shape finding: the bundles don't discount the monthly rate — they prepay it.** Every Semaglutide bundle total divides to exactly **$199/mo** (3-mo $597, 6-mo $1,194, 9-mo $1,791, 12-mo $2,388), the same as the month-to-month rate on /pricing. The advertised savings live elsewhere: an **automatic card/wallet discount** ("DISCOUNTS PROVIDED AUTOMATICALLY WHEN UTILIZING CARD/WALLET PURCHASE") and the homepage's "save up to 15% when you pay by credit/debit card." The **"As low as $26/mo"** style figures on each bundle are **Cherry financing estimates** ("*Based on Cherry approval"), not the plan price. Pricing is **`published`** across the board — the full all-in is shown without an intake wall, which is notable for this cohort.

**Prominence (calibrated).**
- **12-month Semaglutide bundle is the lead SKU [HIGH]** — the company's own **"Most popular"** badge on /packages.
- **Semaglutide over Tirzepatide [MED]** — Semaglutide is the default molecule toggle and the homepage CTA (`?plan=sema-6mo`); Tirzepatide is the pricier alternate ($275 vs $199).
- **Financing-first framing [MED]** — "Get started with Cherry →" is the repeated per-bundle CTA; the Cells lead with the financed "As low as $X/mo," not the total.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Semaglutide — monthly | buyable | Semaglutide | /pricing (no PDP — shared toggled page) | `Semaglutide $199/mo` | published | semaglutide · compounded, vial · all-inclusive monthly; Rx-gated by async questionnaire → Provider Group |
| Semaglutide — 3-month bundle | buyable | Semaglutide | /packages (no PDP — toggled) | `$597 total` (Cherry "As low as $26/mo") | published | semaglutide · compounded, vial · prepaid 3 mo; "3 months of compounded Semaglutide, Clinician-guided dose titration, Free monthly shipping" |
| Semaglutide — 6-month bundle | buyable | Semaglutide | /apply?plan=sema-6mo (attested param; no PDP) | `$1,194 total` (Cherry "As low as $53/mo") | published | semaglutide · compounded, vial · prepaid 6 mo |
| Semaglutide — 9-month bundle | buyable | Semaglutide | /packages (no PDP — toggled) | `$1,791 total` (Cherry "As low as $79/mo") | published | semaglutide · compounded, vial · prepaid 9 mo |
| Semaglutide — 12-month bundle | buyable | Semaglutide | /packages (no PDP — toggled) | `$2,388 total` (Cherry "As low as $106/mo") | published | semaglutide · compounded, vial · prepaid 12 mo · **"Most popular"** |
| Tirzepatide — monthly | buyable | Tirzepatide | /pricing (no PDP — shared toggled page) | `Tirzepatide $275/mo` | published | tirzepatide · compounded, vial · all-inclusive monthly; Rx-gated by async questionnaire → Provider Group |
| Tirzepatide — bundles (3/6/9/12-mo) | buyable | Tirzepatide | /packages (no PDP — toggled) | `—` (totals not captured — Semaglutide toggle was active) | published | tirzepatide · compounded, vial · prepaid 3/6/9/12 mo; bundle totals exist on-site but were not in-capture |

*"family" rows omitted — both molecules are buyable leaves of the one `Single` offering; the molecule is the family.*

### Verbatim anchors

- **All-inclusive pricing claim** (/pricing): *"TeloLife Pricing is ALL-INCLUSIVE REGARDLESS OF DOSAGE. No consultation fees, No shipping fees, No membership fees, and absolutely No hidden charges."* — this is why every line is `published` (the shown number is the full, self-contained price; no stacked membership/consult/shipping cost).
- **Per-molecule monthly rates** (/pricing): *"Semaglutide $199/mo"* · *"Tirzepatide $275/mo"* · *"\*DISCOUNTS PROVIDED AUTOMATICALLY WHEN UTILIZING CARD/WALLET PURCHASE."*
- **Bundle inclusions** (/packages, each bundle card): *"3 months of compounded Semaglutide · Clinician-guided dose titration · Free monthly shipping"* (scales per duration).
- **Cherry footnote** (/packages): *"As low as $26/mo … \*Based on Cherry approval"* — a financing estimate, **not** the plan price; the **$597 total** is the price. Financing is *"offered through Cherry — TeloLife's healthcare financing partner. Estimated monthly payments shown are illustrative."*
- **Molecule/form audit:** molecule **semaglutide / tirzepatide** is page-attested (/pricing labels, /packages bundle copy). **Form = "vial"** is attested via the hero image alt *"TeloLife compounded Semaglutide and Tirzepatide vials"* (homepage) — injectable is the obvious read but the pages say "vials," so form is recorded as `vial`, not asserted as "injection." No oral/tablet SKU appears.

## Deep blocks

**None earned** — the roster + Verbatim anchors carry this company. The only would-be ambiguities (bundle totals = prepaid monthly rate, not a discount; Cherry "as low as" = financing not price) are resolved inline in the overview and anchors, not deep enough to merit a block. No PDP-template anatomy (there are no PDPs — every SKU shares one toggled /packages page).

## Provenance

- **Pages read:** /pricing (per-molecule monthly rates), /packages (bundle totals + inclusions + FAQ), homepage (plan framing, hero, `?plan=sema-6mo` CTA) — captured 2026-06-04, Firecrawl. /packages & /pricing are SPA soft-404s (HTTP 404, full content — §5.6); bodies confirmed against screenshots.
- **Scope enumerated:** all 5 Semaglutide duration tiers (monthly + 3/6/9/12-mo) with totals; Tirzepatide monthly rate. **Noted but not enumerated:** Tirzepatide bundle totals (on-site behind the molecule toggle, not in-capture).
- **Gated/unreachable:** nothing price-gated (pricing is published); the Rx itself is gated by the /apply questionnaire (clinician approval), but the plan prices are not.
- **Point-in-time snapshot:** prices are a 2026-06-04 snapshot; /packages renders state-dependent on its Cash↔Financing and Semaglutide↔Tirzepatide toggles — re-check the Tirzepatide toggle next run.
- **Run profile:** vanilla offerings capture (no added columns, no opt-in PDP-anatomy or hero-image block — there are no PDPs/product renders to pull).
