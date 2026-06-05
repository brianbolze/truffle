---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: struthealth.com
captured_at: 2026-06-04
site_notes: "Prices live on the category HUB pages (/mens-<cat>, /womens-<cat>) AND the PDPs — each product card shows a verbatim 'Starting at $X' floor + a molecule/dose line + a checkout link (checkout.struthealth.com/<slug>?priceId=). The within-company key is the www PDP relative URL; the checkout slug differs (e.g. PDP /mens-sexual-health/strut-mojo → checkout /enclomiphine). Prices are auto-refill subscription floors that move with dose/multi-month tiers (e.g. Strut Mojo $79 base → $99/$119/$237 multi-month). Men's and women's mirror most SKUs at the same price; hair + sexual-health diverge by gender. A/B: rotating hero — featured set is snapshot-volatile."
---

## Portfolio overview

Strut Health is a **Multi-product** DTC telehealth catalog spanning ~12 categories across both men and women — built on two pricing tiers: cheap **generic** Rx (sildenafil/tadalafil $30, finasteride tablets $25, ketoconazole $25) and pricier **custom-compounded "Strut" / "Hairfect Rx" house formulas** (multi-active topicals/orals, GLP-1s, peptides). Every priced line is **`published`** — floors render right on the category page. The catalog's "shape" finding: Strut's **"testosterone support" is enclomiphene (a SERM), not injectable TRT**, and its branded combos (Strut Mojo, Super Strut, ParoxetineMax, Hairfect combos) are the margin/differentiation layer over commodity generics.

**Prominence (calibrated):** hair loss leads the treatment-selector grid and is the deepest line (~13 SKUs) `[MED]` — but the `<title>` ("Sex, Skin & Hair Meds") and a rotating hero give sexual health + skin co-equal billing `[LOW]`. The promoted banner this capture pushed **"NEW Sermorelin injections"** (Wellness & Longevity) `[HIGH — company's own "NEW" label]`. Weight-loss GLP-1s sit at the top of the price ladder ($99–$199).

## Roster

Complete at the indexed level (category line + buyable SKUs). Men's/women's share most SKUs at identical prices; women-only and men-only SKUs are marked. Molecule/form is page-attested; all are Rx unless noted OTC. Prices verbatim from the cited hub/PDP capture.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Hair loss** | family | — | /mens-hair-loss · /womens-hair-loss | — | — | Compounded + generic hair regrowth; deepest line |
| Hairfect Rx Topical w/ Finasteride | buyable | /mens-hair-loss | /mens-hair-loss/finasteride-hair-loss-formula | **$59/mo** | published | finasteride + minoxidil + biotin · compounded topical 30ml · Rx |
| Hairfect Rx Topical w/ Dutasteride | buyable | /mens-hair-loss | /mens-hair-loss/topical-dutasteride | **$69/mo** | published | dutasteride (+minoxidil) · compounded topical · Rx |
| HairfectRx Hair Capsules (Finasteride / Dutasteride) | buyable | /mens-hair-loss | /mens-hair-loss/hairfect-rx-oral-finasteride · /hairfect-rx-oral-dutasteride | **$69** | published | finasteride or dutasteride · compounded oral capsule · Rx |
| Finasteride Tablets | buyable | /mens-hair-loss | /mens-hair-loss/finasteride-formula | **$25** | published | finasteride · generic tablet · Rx |
| Dutasteride Capsules | buyable | /mens-hair-loss | /mens-hair-loss/dutasteride-capsules | **$39** | published | dutasteride · capsule · Rx |
| Oral Minoxidil Tablets | buyable | /mens-hair-loss | /mens-hair-loss/oral-minoxidil-tablets | **$55** | published | minoxidil 1.25mg daily · oral tablet · Rx |
| Ketoconazole 2% Shampoo | buyable | /mens-hair-loss | /mens-hair-loss/ketoconazole-2-shampoo | **$25** | published | ketoconazole 2% · shampoo · Rx |
| Strut Hair Booster w/ Latanoprost | buyable | /mens-hair-loss | /mens-hair-loss/strut-hair-booster-with-latanoprost | **$49** | published | latanoprost · compounded topical · Rx |
| Strut Dermaroller for Hair | buyable | /mens-hair-loss | /mens-hair-loss/strut-dermaroller-for-hair | **$11.99** | published | microneedle device · OTC |
| Hairfect Combo: Finasteride Tablets + StrutVite | buyable | /mens-hair-loss | /mens-hair-loss/hairfect-combo | **$45** | published | finasteride tablet + StrutVite supplement · bundle · Rx |
| Hairfect Combo: Finasteride Formula + StrutVite | buyable | /mens-hair-loss | /mens-hair-loss/hairfect-gel-combo | **$79** | published | finasteride topical + StrutVite · bundle · Rx |
| Hairfect Combo: Dutasteride Topical + StrutVite | buyable | /mens-hair-loss | /mens-hair-loss/dutasteride-hair-combo | **$89** | published | dutasteride topical + StrutVite · bundle · Rx |
| Strut Women's Hair Loss Formula | buyable | /womens-hair-loss | /womens-hair-loss/womens-finasteride-hair-loss-formula | **$59** | published | women's compounded hair-growth Rx · topical/oral · Rx (women-only) |
| Hairfect Combo: Women's Hair Growth + StrutVite | buyable | /womens-hair-loss | /womens-hair-loss/womens-hairfect-combo | **$75** | published | women's hair-growth formula + StrutVite · bundle · Rx (women-only) |
| **Sexual health** | family | — | /mens-sexual-health · /womens-sexual-health | — | — | ED / PE / libido; branded combos + generics |
| Super Strut (4-in-1 dissolvable ED) | buyable | /mens-sexual-health | /mens-sexual-health/superstrut | **$79/mo** | published | compounded 4-in-1 dissolvable ED tablet · Rx (men) |
| Strut Mojo | buyable | /mens-sexual-health | /mens-sexual-health/strut-mojo | **$79** | published | enclomiphene 6.25–25mg + tadalafil 2.5–5mg · compounded capsule · Rx (men) — see Deep block |
| ParoxetineMax (4-in-1) | buyable | /mens-sexual-health | /mens-sexual-health/paroxetinerx | **$49** | published | paroxetine-based 4-in-1 (PE) · compounded · Rx (men) |
| Sildenafil | buyable | /mens-sexual-health | /mens-sexual-health/sildenafil | **$30** | published | sildenafil · generic tablet · Rx (men) |
| Tadalafil | buyable | /mens-sexual-health | /mens-sexual-health/tadalafil | **$30** | published | tadalafil · generic tablet · Rx (men) |
| Strut O Cream | buyable | /womens-sexual-health | /womens-sexual-health/strut-o-cream | **$49** | published | compounded arousal cream · topical · Rx (women-only) |
| **Skin care** | family | — | /mens-skin-care · /womens-skin-care | — | — | Compounded "Strut" derm formulas + tretinoin + StrutVite |
| Tretinoin Cream | buyable | /mens-skin-care | /mens-skin-care/tretinoin-cream | **$90** (men) / **$70** (women) | published | tretinoin · compounded cream · Rx |
| Strut Rosacea Formula | buyable | /mens-skin-care | /mens-skin-care/strut-rosacea-formula | **$59** | published | compounded rosacea topical · Rx |
| Strut Anti-Aging Formula | buyable | /mens-skin-care | /mens-skin-care/strut-anti-aging-formula | **$49** | published | compounded anti-aging topical · Rx |
| Strut Brightly Formula | buyable | /mens-skin-care | /mens-skin-care/strut-brightly-formula | **$49** | published | compounded brightening topical · Rx |
| Strut Melasma Formula | buyable | /mens-skin-care | /mens-skin-care/strut-melasma-formula | **$69** | published | compounded melasma topical · Rx |
| Strut Eye Cream | buyable | /mens-skin-care | /mens-skin-care/strut-eye-cream | **$58** (12g) | published | compounded eye cream · Rx |
| Strut Neck Cream | buyable | /mens-skin-care | /mens-skin-care/strut-neck-cream | **$58** (30g) | published | compounded neck cream · Rx |
| Strut Scar Formula | buyable | /womens-skin-care | /womens-skin-care/strut-scar-formula | **$49** | published | compounded scar topical · Rx (women's page) |
| Flawless Combo (Brightly + Anti-Aging) | buyable | /mens-skin-care | /mens-skin-care/flawless-combo | **$89** | published | brightly + anti-aging · bundle · Rx |
| StrutVite | buyable | /mens-skin-care | /mens-skin-care/strutvite | **$24.99** | published | hair/skin/nail vitamin · supplement · OTC |
| **Weight loss** | family | — | /mens-weight-loss · /womens-weight-loss | — | — | Compounded GLP-1 (oral + injectable) — top of price ladder |
| Oral Semaglutide | buyable | /mens-weight-loss | /mens-weight-loss/oral-semaglutide | **$99** | published | semaglutide · compounded oral · Rx |
| Injectable Semaglutide | buyable | /mens-weight-loss | /mens-weight-loss/injectable-semaglutide | **$149** | published | semaglutide · compounded injectable · Rx |
| Oral Tirzepatide | buyable | /mens-weight-loss | /mens-weight-loss/oral-tirzepatide | **$199** | published | tirzepatide · compounded oral · Rx |
| Injectable Tirzepatide | buyable | /mens-weight-loss | /mens-weight-loss/injectable-tirzepatide | **$199** | published | tirzepatide · compounded injectable · Rx |
| PeptideVite | buyable | /mens-weight-loss | /mens-weight-loss/peptidevite | **$46.99** | published | metabolic vitamin/peptide support · supplement |
| **Wellness & longevity** | family | — | /mens-wellness-and-longevity · /womens-wellness-and-longevity | — | — | Peptides (sermorelin) + NAD+ |
| Oral Sermorelin Peptide Therapy | buyable | /mens-wellness-and-longevity | /mens-wellness-longevity/oral-sermorelin-peptide-therapy | **$99** | published | sermorelin · oral troche · Rx |
| Injectable Sermorelin Peptide Therapy | buyable | /mens-wellness-and-longevity | /mens-wellness-longevity/injectable-sermorelin-peptide-therapy | **$119** | published | sermorelin 9mg (2.5mg/ml) · compounded injectable · Rx |
| NAD+ Therapy | buyable | /mens-wellness-and-longevity | /mens-wellness-longevity/mens-nad-therapy | **$149** | published | NAD+ 500mg (200mg/ml) · injectable · Rx |
| **Health testing** | family | — | /mens-health-testings · /womens-health-testing | — | — | At-home lab panels (self-collection kits) |
| Men's Testosterone Panel | buyable | /mens-health-testings | /mens-health-testing/mens-testosterone-panel | **$89** | published | T · DHEA-S · Estradiol · Cortisol · SHBG · at-home collection kit |
| Respiratory Panel | buyable | /mens-health-testings | /mens-health-testing/respiratory-panel | **$159** | published | respiratory lab panel · at-home collection kit |
| **Sleep** | family | — | /mens-sleep · /womens-sleep | — | — | Sleep support |
| Strut Sleep Capsule | buyable | /mens-sleep | /mens-sleep/strut-sleep-capsule | **$59/mo** | published | sleep-support capsule · subscription |
| **Other lines** *(exemplar — not enumerated)* | family | — | nav/URL map | — | on-request | Testosterone support (→ enclomiphene/Strut Mojo; thin landing), nails (StrutVite), cold sores (valacyclovir, /valacyclovir), allergy & wellness, topical pain cream — surfaced in nav/map, prices not captured this run |

## Verbatim anchors

- **Strut Mojo dose/molecule** — "Enclomiphene 6.25-25mg + Tadalafil 2.5-5mg Capsules" (/mens-sexual-health, /mens-sexual-health/strut-mojo). Add-on offered: "Testosterone test kit… measures for Testosterone, DHEA-S, Estradiol, Cortisol, & SHBG."
- **Strut Mojo price ladder** — base **$79**; multi-month tiers **$99 / $119 / $237** appear on the PDP (auto-refill floor moves with supply length).
- **Hairfect Topical (finasteride)** — finasteride + minoxidil + biotin compounded topical, 30ml, **$59/mo** (PDP also shows a **$40** tier).
- **Oral Minoxidil** — "1.25mg daily dose," **$55** (both genders).
- **Injectable Sermorelin** — "9mg (2.5MG/ML)," **$119**. **NAD+** — "500mg (200MG/ML)," **$149**.
- **GLP-1** — oral semaglutide **$99**, injectable semaglutide **$149**, tirzepatide (oral & injectable) **$199**; PDPs describe these as **compounded**.
- **Price pages cited:** every `$` above is greppable in `captures/2026-06-04/` — category hubs `mens-hair-loss.md`, `mens-sexual-health.md`, `mens-weight-loss.md`, `mens-skin-care.md`, `mens-wellness-and-longevity.md`, `mens-health-testings.md`, `mens-sleep.md`, and the womens-* mirrors; PDPs `pdp-strut-mojo.md`, `pdp-hairfect-topical-fin.md`, `pdp-injectable-semaglutide.md`, `pdp-strutvite.md`, `pdp-injectable-sermorelin.md`.

## Deep blocks

- **Strut Mojo — "testosterone support" is not TRT (disambiguation, earned).** Strut routes its testosterone-support funnel to **Strut Mojo = enclomiphene + tadalafil** (a SERM that raises *endogenous* testosterone, plus a PDE5 for ED), **not** injectable Schedule-III testosterone. `/mens-testosterone-support` is a thin landing page (H1 "Testosterone Support," body is ED/PE copy, product grid "No items found"). Consequence for the cohort read: Strut carries **no scheduled controlled substance** — important when comparing to TRT clinics that prescribe testosterone cypionate. Verbatim dose: "Enclomiphene 6.25-25mg + Tadalafil 2.5-5mg Capsules." Hero render: a clean isolated **Super Strut** jar (sibling SKU in this line) at `captures/2026-06-04/images/super-strut.png`.
- **Hero product renders (opt-in asset).** Clean isolated renders exist for the **branded "Strut" SKUs** and were captured: `images/super-strut.png` (blue Super Strut jar) and `images/strut-skincare-bottle.png` (white Strut pump bottle, the shared skincare-line vessel — surfaced off the StrutVite PDP). The **compounded/injectable flagships** (Hairfect topical, injectable semaglutide, injectable sermorelin) lead their PDPs with **lifestyle/process imagery, not isolated product renders** — no clean hero available for those (an honest finding, typical of compounded-Rx telehealth).

## Provenance

- **Pages read:** homepage + 11 category hubs (mens + womens hair/sexual/skin/weight/wellness/testing/sleep) + 5 flagship PDPs (Strut Mojo, Hairfect topical-finasteride, injectable semaglutide, StrutVite, injectable sermorelin), all in `captures/2026-06-04/`.
- **Scope:** all priced lines enumerated at the SKU level; minor lines (testosterone-support landing, nails, cold sores, allergy & wellness, topical pain cream) noted as a single exemplar family row, not enumerated (prices not captured this run).
- **Point-in-time:** prices are auto-refill subscription floors that move with dose/multi-month tier; the featured/hero set rotates (A/B) — this is a snapshot, re-check for drift.
- **Run profile:** non-vanilla — `+offerings` with **`+hero images`** (flagship PDP renders promoted to `images/`). No PDP-template-anatomy block (not requested).
