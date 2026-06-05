---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: joinfridays.com
captured_at: 2026-06-04
site_notes: "Catalog backbone = /map census (208 URLs) + category-hub product cards (Webflow CMS; products.json returns the SPA shell, not JSON). Product slugs live at /products/<slug> with 1/3/6/12-month supply variants per SKU — roster is at the product level, not the supply-tier leaf. Prices: GLP-1 on /pricing (annual floor vs month-to-month, both shown, + promo floors via stackable codes); longevity/TRT/microdose on their category hubs (flat per-product 'Quarterly price $X/mo'). Brand-name GLP-1 (Ozempic/Zepbound) priced by insurance. Everything is all-in (med + visits + coaching + labs); 'no membership fees.' Perpetual 50%-off promo + rotating codes → prices A/B-volatile, re-check before quoting. Clean transparent hero renders for every SKU captured to images/."
---

## Portfolio overview

`Multi-product`, **GLP-1-anchored**: four prescription programs plus one co-branded sleep partner. The shape that matters — **everything orbits GLP-1.** Microdosing *is* GLP-1 (sub-clinical doses); longevity (NAD+/peptides) and TRT are adjacent wellness lines sold off the same OpenLoop-clinician + compounding-pharmacy rails. Because the model is **all-in with medication included** ("no membership fees, no sign-up fees, no lab fees"), a shown price is much closer to the true all-in than at membership-stacked peers — **with two exceptions:** the compounded GLP-1 lines publish a *"starting at" floor* that moves with dose/plan (→ `partial`), and brand-name GLP-1 (Ozempic/Zepbound) is *insurance-priced* (→ `partial`). The flat-priced lines — longevity, TRT, microdosing — publish self-contained per-product numbers (→ `published`).

Prominence (calibrated): **GLP-1 weight loss `[HIGH]`** (page title "GLP-1 Telehealth," first nav item "GLP-1 Pricing," homepage hero, "the best GLP-1 provider in the game"). **Longevity / Testosterone / Microdosing `[MED]`** (each a nav item with its own hub). **Happy Sleep `[LOW]`** (not in the main nav; a co-branded partner offering fulfilled on happysleep.com).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **GLP-1 Weight Loss** | family | — | /pricing | — | — | compounded + brand-name GLP-1 · injectable + oral · Rx, intake-gated |
| Compounded Semaglutide | buyable | GLP-1 Weight Loss | /products/compounded-semaglutide-glp-1-1-month-subscription | "Starting at $150/mo" (annual; "$249/mo for month-to-month plan") | partial | semaglutide · subcutaneous injection · Rx; all-in, dose-gated floor |
| Compounded Tirzepatide | buyable | GLP-1 Weight Loss | /products/compounded-tirzepatide-glp-1-gip-1-month-subscription | "Starting at $240/mo" (annual; "$359/mo … month-to-month") | partial | tirzepatide (GLP-1/GIP) · subcutaneous injection · Rx; all-in, dose-gated floor |
| Oral Compounded Semaglutide | buyable | GLP-1 Weight Loss | /products/oral-compounded-semaglutide | — (no standalone price captured; GLP-1 family) | on-request | semaglutide · oral · Rx |
| Ozempic® | buyable | GLP-1 Weight Loss | (no PDP — /pricing card) | "$1498 / monthly" (month-to-month; "pricing based on insurance coverage") | partial | semaglutide (FDA-brand) · injection · Rx, insurance-priced |
| Zepbound® | buyable | GLP-1 Weight Loss | (no PDP — /pricing card) | "$1828 / monthly" (month-to-month) | partial | tirzepatide (FDA-brand) · injection · Rx, insurance-priced |
| Wegovy® | buyable | GLP-1 Weight Loss | /medications/wegovy | — (no price captured) | on-request | semaglutide (FDA-brand) · injection · Rx, insurance-priced |
| **GLP-1 Microdosing** | family | — | /microdosing | — | — | sub-clinical compounded GLP-1/GIP · weekly injection / daily oral · Rx |
| Microdose Tirzepatide | buyable | GLP-1 Microdosing | /products/tirzepatide-microdose | "$198/month" | published | tirzepatide (microdose) · weekly injection · Rx |
| Microdose Semaglutide | buyable | GLP-1 Microdosing | (no distinct PDP — /microdosing card) | "$249/month" | published | semaglutide (microdose, "10mg") · daily oral · Rx |
| **Longevity** | family | — | /longevity | — | — | NAD+ · peptides · vitamin injections · Rx |
| NAD+ Injectable | buyable | Longevity | /products/nad-injection | "Quarterly price $125/mo" | published | NAD+ · injection · Rx |
| NAD+ Oral Liposomal | buyable | Longevity | /products/nad-oral | "Quarterly price $179/mo" | published | NAD+ · oral liposomal liquid (dropper) · Rx |
| NAD+ Nasal Spray | buyable | Longevity | /products/nad | "Quarterly price $229/mo" | published | NAD+ · nasal spray · Rx *(form-binding inferred from /longevity copy; /products/nad is the generic NAD slug)* |
| Sermorelin | buyable | Longevity | /products/sermorelin-injection | "Quarterly price $179/mo" | published | sermorelin (peptide) · injection / daily oral · Rx |
| MIC-B12 | buyable | Longevity | /products/mic-b12 | "Quarterly price $179/mo" | published | MIC + B12 · injection · Rx |
| **Testosterone (TRT)** | family | — | /testosterone | — | — | testosterone + enclomiphene · injection / oral · Rx |
| Injectable TRT (Testosterone Cypionate) | buyable | Testosterone (TRT) | /products/testosterone-cypionate-injection | "$129/mo" | published | testosterone cypionate · IM/SC injection · Rx (Schedule III) |
| Oral Testosterone | buyable | Testosterone (TRT) | /products/testosterone-oral | "$129/mo" | published | testosterone · oral dissolvable tablet (ODT) · Rx (Schedule III) |
| Enclomiphene | buyable | Testosterone (TRT) | /products/enclomiphene | "$169/mo" | published | enclomiphene · oral daily capsule · Rx (stimulates endogenous testosterone) |
| Happy Sleep (Happy Ring) | buyable | — | (no PDP — /happy-sleep; fulfilled at fridays.happysleep.com) | "$396" self-pay (was "$499", 20% off) / "$0 due today" with insurance | published | FDA-cleared Happy Ring home sleep test + board-certified sleep-MD visit · co-branded partner (OpenLoop affiliate) |

*Anastrozole (an aromatase inhibitor) is offered as a TRT add-on "if appropriate" (/testosterone), not a standalone SKU.*

## Verbatim anchors

The price strings the roster points at, quoted exactly:

- **GLP-1 (compounded), /pricing:** "Compounded GLP-1* (Contains: Semaglutide) — Starting at $150 /mo … ( **$249/mo** for month-to-month plan)"; "Compounded GLP-1/GIP* (Contains: Tirzepatide) — Starting at $240 /mo … ( **$359/mo** for month-to-month plan)." Both are all-in ("Medication + Coaching + Care. Membership included free."). → "starting at" floor moves with dose/plan ⇒ `partial`.
- **GLP-1 promo floors, /pricing:** "Semaglutide: $117/mo (Lowest Price)"; "Tirzepatide: As low as $198/mo" (the "Spring Advantage," gated behind codes NYNY12 / NEWYOU12 — "SAVE 58%" / "SAVE 50%"). Promotional, not the standing price.
- **GLP-1 (brand), /pricing:** "Ozempic® — Name Brand Semaglutide Injection — $1498 / monthly — Month-to-month plan"; "Zepbound® — Name Brand Tirzepatide Injection — $1828 / monthly." Fine print: "Brand name medication pricing is based on insurance coverage." ⇒ `partial`.
- **Testosterone, /testosterone:** "Injectable TRT … $129 /mo"; "Oral Testosterone … $129 /mo"; "Enclomiphene … $169 /mo." `$50 OFF FIRST ORDER` code TRT50.
- **Longevity, /longevity** (each "Quarterly price"): "Sermorelin … $179/mo"; "NAD+ Nasal Spray … $229/mo"; "NAD+ Oral Liposomal … $179/mo"; "NAD+ … $125/mo"; "MIC-B12 … $179/mo."
- **Microdosing, /microdosing:** "Weekly Injectable — $198/month — Compounded Microdose Tirzepatide"; "Daily Oral — $249/month — Compounded Microdose Semaglutide … 10mg Compounded Semaglutide (GLP-1)."
- **Happy Sleep, /happy-sleep:** "**$396** ~~$499~~ 20% OFF! — Add to Cart - $396" (self-pay) / "$0 due today" (Use My Insurance) / "As low as $33/mo … interest-free." "Includes: multiple nights of FDA-cleared testing · 1 virtual visit with a board-certified sleep doctor · diagnosis + prescription + care plan · Happy Ring you keep · a year of nightly tracking."
- **All-in attestation, /pricing:** "● No membership fees ● No sign up fees ● No lab fees"; "Medication costs are included in the Fridays program" (footer).
- **Molecule audit:** every molecule is page-attested — semaglutide / tirzepatide (named on /pricing, hubs, product cards), testosterone cypionate + enclomiphene (/testosterone), NAD+ / sermorelin / MIC + B12 (/longevity). No molecule was inferred from a brand name. `oral-compounded-semaglutide` and `injectable-core-microdose` exist as /map slugs but carry no standalone captured price.

## Deep blocks

**GLP-1 pricing — the three-number tangle (the one real ambiguity).** A single compounded GLP-1 SKU shows up to three prices, which is why it rosters `partial`:
- the **annual floor** ("Starting at $150/mo" sema, "$240/mo" tirz) — "Paid annually, delivered monthly," the cheapest standing rate;
- the **month-to-month** rate ("$249/mo" sema, "$359/mo" tirz) — the no-commitment price;
- the **promo floor** ("$117/mo" sema, "$198/mo" tirz) — code-gated, time-limited ("Spring Sale," NYNY/NEWYOU codes).
The *exact* monthly price is set by the prescribed dose inside the gated intake flow, so even the floor is a starting point. All three include the full program (unlimited visits + coaching + labs); the variation is term + dose, not bundle. Hero render: `captures/2026-06-04/images/semaglutide.webp`, `captures/2026-06-04/images/tirzepatide.webp`.

**Hero product renders (opt-in asset — design/rendering reference).** Clean isolated transparent-background 3D vial/jar renders were captured for every flagship to `store/joinfridays-com/captures/2026-06-04/images/`, color-coded by line: GLP-1 (green) `semaglutide.webp`, `tirzepatide.webp`, `microdose-tirzepatide.webp`; Longevity (blue) `nad-injectable.webp`, `sermorelin.webp`, `mic-b12.png`; Testosterone (red/maroon) `testosterone-cypionate.webp`, `testosterone-oral.webp`, `enclomiphene.webp`. Each carries the small "fridays compounded … Rx only" label; sourced from the homepage `images[]` payload (website-files CDN bucket `…/66c8a0fb54f84ec4a09643a1/`), not a per-PDP scrape. Asset only — never a roster column.

## Provenance

- **Pages read:** the 9 captures under `captures/2026-06-04/` — homepage + /pricing, /weight-loss, /longevity, /testosterone, /microdosing, /whats-included, /compounded-medications, /happy-sleep — plus the /map census (208 product/locale URLs) for slug attestation.
- **Scope:** all four prescription programs + the Happy Sleep partner enumerated at the product level (complete at the indexed level). Supply-tier leaves (1/3/6/12-month variants of each SKU) are **noted, not exploded** into rows — they are pricing tiers, not distinct products. Spanish `/es/*` mirrors excluded.
- **Gated/unreachable:** exact per-dose prices (intake flow, not submitted); standalone prices for oral-compounded-semaglutide, microdose-semaglutide, and Wegovy (no captured price); partner-pharmacy names.
- **Point-in-time:** pricing is a snapshot during a perpetual 50%-off "Spring Sale" with stackable codes (NEWYOU/NYNY/FORBES/EXPERTISE/SHOP100/TRT50) — floors and codes rotate; re-check before quoting.
- **Run profile:** guided — `offerings.md` enabled alongside `profile.md` + `telehealth.md`; **+ hero product-image capture** (the 9 isolated vial renders in `images/`), per the "flagship product images" emphasis. Plain roster otherwise (no PDP-anatomy block).
