---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: hevahealth.com
captured_at: 2026-06-04
site_notes: "Catalog spans three stacks: CURRENT clinical plans on the Astro pages (/weight-loss, /hormones, /labs) — prices live here; a LEGACY Sanity treatment catalog at /treatments/<category>/<slug>/ — stale '$149 + $99/mo Wellness Plan' pricing, useful only for molecule attestation + product renders, and two PDPs (testosterone-cypionate, dihexa) render blank (H1-only); a Shopify supplement store on shop.hevahealth.com — ~17 SKUs, prices on the storefront homepage. Pricing is promo-laden (first-month codes SEMA1/TIRZ1; shop WELCOME10) — point-in-time. Hormone Core price is $149/mo on /hormones; a separate $99/mo Concierge/Wellness tier exists (homepage FAQ) — don't conflate."
---

## Portfolio overview

`Multi-product` — three clinical lines lead (weight loss, hormones, labs), with a legacy Rx skincare/peptide catalog and a Shopify supplement store behind them. The clinical plans are **all-in subscriptions** (medication + labs + provider support bundled into one monthly price); labs and supplements are one-time.

Prominence (calibrated): **weight loss + hormones + labs** are co-equal hero lines `[MED]` — the homepage's "Three ways to start" grid orders weight loss first `[LOW]` (single position cue, no badge). The supplement store and the legacy `/treatments/` skincare/peptide catalog are secondary, surfaced only in the footer / mega-nav and the about-page "full catalog" framing `[MED]`.

**Shape finding:** the front door is deliberately narrow (3 lines) but the practice behind it is wide — /clinic advertises "the complete Heva pharmacy catalog and the full treatment library… no menu of three things," gating peptides, dermatology, allergy, sexual-health, and longevity through the concierge tier. Also note the **legacy/current price split**: the Sanity `/treatments/` pages still show the old model (semaglutide "$149" inside a "$99/month Heva Wellness Plan"); the live Astro pages have replaced it with direct all-in plan pricing ($189 semaglutide). Current rows below use the Astro prices.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight Loss (GLP-1) | family | — | /weight-loss | — | — | Compounded GLP-1 weight-loss programs · subcutaneous injection · all-in monthly plan |
| Semaglutide | buyable | /weight-loss | /weight-loss | "$189/month" (m2m; "First month $149 with code SEMA1") | published | semaglutide (+ B-12, glycine, per legacy PDP) · subcutaneous injection · all-in plan, smart titration; m2m or 3-/6-mo |
| Tirzepatide | buyable | /weight-loss | /weight-loss | "$339/month" (m2m; "First month $149 with code TIRZ1") | published | tirzepatide · subcutaneous injection · all-in plan; "highest-efficacy option" |
| Hormone Therapy (TRT/HRT) | family | — | /hormones | — | — | Doctor-prescribed hormone optimization, men & women · injection/oral · all-in monthly membership |
| Core | buyable | /hormones | /hormones | "$149/month" | published | testosterone therapy *or* enclomiphene + anastrozole (if indicated) · injection/oral · labs q90d + mobile phlebotomy included; 3-mo min then cancel |
| Enhanced | buyable | /hormones | /hormones | "$199/month" | published | everything in Core + gonadorelin (fertility/natural-production) · injection/oral · all-in |
| Lab Testing | family | — | /labs | — | — | At-home diagnostic panels · blood draw · one-time |
| Core 91 Panel | buyable | /labs | /labs | "$249 one-time" | published | 91 biomarkers (hormones, metabolic, nutrient, heart, immune) · at-home or walk-in draw · one-time, 50-pg report, no consult |
| Concierge Care | buyable | — | /clinic | "$99/mo" (homepage FAQ; "medications still billed at their plan rate") | partial | membership · provider visits + 4 labs/yr + personalized plan · all-in membership, meds extra; "Labs + Concierge" adds a 45-min consult (9 states) |
| Dermatology (Rx) | family | — | /treatments/dermatology | — | — | Prescription topicals · cream · charged only if prescribed *(legacy Sanity catalog)* |
| Soothing Cream | buyable | /treatments/dermatology | /treatments/dermatology/soothing-cream/ | "$85" *(legacy)* | published | azelaic acid · ivermectin · metronidazole · niacinamide (5/1/1/4%) · topical cream · rosacea Rx |
| Peptides | family | — | /treatments/peptides | — | — | Peptide therapy library · injection/oral · concierge/Rx-gated *(legacy; PDPs render blank)* |
| Dihexa | buyable | /treatments/peptides | /treatments/peptides/dihexa/ | — | on-request | not stated · not stated · concierge/Rx (PDP is an H1-only shell) |
| Methylene Blue | buyable | /treatments/peptides | /treatments/peptides/methylene-blue/ | — | on-request | not stated · not stated · concierge/Rx |
| GHK-Cu | buyable | /treatments/peptides | /treatments/peptides/ghk-cu/ | — | on-request | not stated · not stated · concierge/Rx |
| TB-4 | buyable | /treatments/peptides | /treatments/peptides/tb-4/ | — | on-request | not stated · not stated · concierge/Rx |
| Supplements (shop) | family | — | shop.hevahealth.com | — | — | Shopify store · capsules/powders/creams · one-time (WELCOME10 −10%; free ship >$75) |
| Lifespan Formula | buyable | shop.hevahealth.com | /products/heva-health-lifespan-formula | "$169.15" | published | proprietary longevity stack (molecule not stated) · capsules · one-time |
| NMN | buyable | shop.hevahealth.com | /products/heva-health-nmn | "$95.00" | published | NMN · capsules · one-time |
| GLP-1 Activator | buyable | shop.hevahealth.com | /products/heva-health-glp-1-activator | "$93.50" | published | proprietary (not stated) · capsules · one-time |
| Cognition Complex | buyable | shop.hevahealth.com | /products/heva-health-cognition-complex | "$85.00" | published | nootropic stack (not stated) · capsules · one-time |
| Immune Booster | buyable | shop.hevahealth.com | /products/heva-health-immune-booster | "$80.00" | published | not stated · capsules · one-time |
| Gut Harmony | buyable | shop.hevahealth.com | /products/heva-health-gut-harmony | "$65.00" | published | not stated · capsules · one-time |
| Female Vitality Complex | buyable | shop.hevahealth.com | /products/heva-health-female-vitality-complex | "$63.75" | published | women's multivitamin stack (not stated) · capsule pack · one-time |
| Liver Cleanse | buyable | shop.hevahealth.com | /products/heva-health-liver-cleanse | "$60.00" | published | not stated · capsules · one-time |
| Revitalize Hair Formula | buyable | shop.hevahealth.com | /products/heva-health-revitalize-hair-formula | "$60.00" | published | not stated · capsules · one-time |
| Male Vitality Complex | buyable | shop.hevahealth.com | /products/heva-health-male-vitality-complex | "$58.65" | published | men's multivitamin stack (not stated) · capsule pack · one-time |
| Pure Whey Protein Isolate (Vanilla) | buyable | shop.hevahealth.com | /products/pure-whey-protein-isolate-vanilla | "$45.00" | published | whey protein isolate · powder · one-time |
| Joint & Tissue Repair | buyable | shop.hevahealth.com | /products/heva-health-joint-tissue-repair | "$140.00" | published | BPC + KPV + PEA 500 + L-glutathione (per render) · capsules · one-time |
| Restorative Sleep | buyable | shop.hevahealth.com | /products/heva-health-restorative-sleep | "$40.00" | published | not stated · capsules · one-time |
| Heva Signature Baseball Hat | buyable | shop.hevahealth.com | /products/heva-signature-baseball-hat | "$35.00" | published | merch (not a supplement) · apparel · one-time |
| Colostrum Powder | buyable | shop.hevahealth.com | /products/colostrum-powder | — | on-request | colostrum · powder · one-time (price not captured) |
| Microburst Pre-Workout (Fruit Punch) | buyable | shop.hevahealth.com | /products/microburst-pre-workout-fruit-punch | — | on-request | pre-workout (not stated) · powder · one-time (price not captured) |

## Verbatim anchors

- **Semaglutide molecule (legacy PDP):** "Ingredients: Semaglutide, B-12, Glycine" · "Subcutaneous injection as directed by your provider." · "503A compounding facilities may only compound medications upon prescription…" — /treatments/weight-loss/semaglutide-copys/
- **Semaglutide current price (Astro):** "$189/month … Save $10/month vs. month-to-month … First month $149 with code SEMA1" — /weight-loss
- **Tirzepatide current price (Astro):** "$339/month … Save $60/month vs. month-to-month … First month $149 with code TIRZ1" — /weight-loss
- **Compounded disclaimer:** "Heva prescribes compounded Semaglutide and Tirzepatide prepared by licensed U.S. compounding pharmacies. Compounded medications are not FDA-approved…" — /weight-loss
- **Hormone Core (verbatim list):** "$149/month … Testosterone therapy or enclomiphene · Anastrozole (if clinically indicated) · Lab testing every 90 days · Mobile phlebotomy — at-home blood draws … 3-month minimum, then cancel anytime." — /hormones
- **Hormone Enhanced:** "$199/month … Everything in the Core plan · Gonadorelin (fertility preservation + natural production support)." — /hormones
- **Concierge $99/mo:** "For everything bundled — four labs a year, provider visits, and a personalized treatment plan — that's Concierge Care, our $99/mo all-in tier (medications still billed at their plan rate)." — homepage
- **Soothing Cream:** "$85 … AZELAIC ACID/IVERMECTIN/METRONIDAZOLE/NIACINAMIDE 5/1/1/4%" — /treatments/dermatology/soothing-cream/
- **Molecule-sourcing audit (`not stated`):** the Shopify supplements list ingredient *brands* (Swanson, CodeAge, Premier Research, Vitaboom) on the pouch renders but no single active molecule per SKU on captured surfaces → `not stated`. Peptide PDPs are blank shells → `not stated`. Joint & Tissue Repair's "BPC + KPV + PEA 500" is read off the render image, not body text — treat as render-attested.

## Deep blocks

Earned blocks for the two flagship clinical SKUs that carry captured **hero product renders** (opt-in for this run), plus the legacy-pricing disambiguation:

### Semaglutide — the GLP-1 flagship
The weight-loss anchor. **Current price $189/mo** (Astro /weight-loss), promo first month $149 (SEMA1). Heva's formulation is **compounded semaglutide + B-12 + glycine** (the B12/glycine added to blunt nausea and preserve muscle, per the legacy PDP), subcutaneous, smart-titrated. Not FDA-approved (compounded, 503A). **Hero render:** `captures/2026-06-04/images/semaglutide.jpg` — a clean isolated dark-olive vial, silver cap, "SEMAGLUTIDE / HEVA®" on the brand cream ground.
*Legacy-price note:* the Sanity PDP still shows the old "$149/mo within a $99/month Heva Wellness Plan" model — superseded by the all-in Astro pricing; do not cite the legacy number as current.

### Soothing Cream — Rx dermatology exemplar
Represents the legacy `/treatments/` Rx-topical line. **$85** (legacy), a rosacea cream of **azelaic acid / ivermectin / metronidazole / niacinamide (5/1/1/4%)**, once-daily topical, charged only if a provider prescribes. **Hero render:** `captures/2026-06-04/images/soothing-cream.png` — a clean isolated olive tube, "HEVA / Soothing / Rosacea Cream / RX ONLY."

### Supplement stacks — Shopify line shape
The shop sells **curated multivitamin "stacks"** repackaged from third-party brands ("Powered by Vitaboom"), not single-molecule SKUs — hence `not stated` molecules across the line. **Reference render:** `captures/2026-06-04/images/supplement-stack.webp` — the cream "HEVA Supplement Stack" box + a labeled daily pouch (Male Vitality Complex) + loose pills.

## Provenance

- **Pages read:** /weight-loss, /hormones, /labs, homepage (current prices); /treatments/weight-loss/semaglutide-copys/, /treatments/dermatology/soothing-cream/ (legacy molecules + renders); shop.hevahealth.com (Shopify catalog). Blank shells (no body): /treatments/.../testosterone-cypionate/, /treatments/peptides/dihexa/.
- **Scope:** the 3 clinical lines fully enumerated (current pricing); Concierge tier captured from homepage FAQ; legacy skincare/peptide catalog rostered by name (peptide prices unreachable — blank PDPs); Shopify line rostered to the indexed level (14 of ~17 SKUs priced; Colostrum, Microburst, Whey-Chocolate slugs present but prices not captured).
- **Gated/unreachable:** women's hormone pricing (client-rendered toggle); peptide per-SKU prices (legacy/concierge-gated); 3 shop prices (not on captured homepage tiles).
- **Snapshot caveat:** prices are point-in-time — promo codes (SEMA1/TIRZ1/WELCOME10) and a brand mid-replatform (legacy Sanity → Astro) make several numbers volatile; re-check next run.
- **Run profile:** non-vanilla — guided run added per-SKU offerings + **hero product images** (3 renders promoted to `captures/2026-06-04/images/`). Hero capture per `firecrawl-capture.md` §1.1.
