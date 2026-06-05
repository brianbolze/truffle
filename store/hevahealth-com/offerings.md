---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: hevahealth.com
captured_at: 2026-06-04
site_notes: "Catalog spans three stacks. (1) CURRENT clinical plans on the Astro pages (/weight-loss, /hormones, /labs) — the live front-door pricing. (2) A wide LEGACY Sanity treatment catalog at /treatments/<category>/ — SIX categories, now fully enumerated off their index pages: hormone-treatment, dermatology (11 topicals), peptides (7), longevity (4), sexual-wellness (2); /treatments/allergy is a live-but-EMPTY scaffold ('No treatments in this category yet'). The Sanity INDEX cards carry molecules + verbatim prices directly (e.g. derm creams $85–$249, enclomiphene $189, glutathione $299/qtr) — a separate, à-la-carte / older pricing model from the Astro plans; treat as point-in-time and don't conflate with the current /hormones $149 plan. A few Sanity PDPs render blank (testosterone-cypionate, dihexa H1-only shells) — the index card is the better source. The dead singular /treatment/<slug> scheme is 404. (3) A Shopify supplement store on shop.hevahealth.com — **23 SKUs via /products.json** (the storefront homepage tiles showed only ~14; the JSON is authoritative). Pricing is promo-laden (first-month codes SEMA1/TIRZ1; shop WELCOME10; Sanity -first50 promo slugs) — point-in-time. Hormone Core is $149/mo on the Astro /hormones; a separate $99/mo Concierge/Wellness tier exists (homepage FAQ) — don't conflate."
---

## Portfolio overview

`Multi-product` — a deliberately narrow three-line front door (weight loss, hormones, labs) sitting on a **wide functional-medicine practice**: a legacy Rx treatment catalog across five live categories (dermatology, peptides, longevity, sexual-wellness, à-la-carte hormones) plus a 23-SKU Shopify supplement store. The Astro clinical plans are **all-in subscriptions** (medication + labs + provider support bundled into one monthly price); labs, the legacy `/treatments/` SKUs, and supplements are one-time / à-la-carte.

Prominence (calibrated): **weight loss + hormones + labs** are co-equal hero lines `[MED]` — the homepage's "Three ways to start" grid orders weight loss first `[LOW]` (single position cue, no badge). Everything in the `/treatments/` Sanity catalog and the Shopify store is secondary, surfaced only in the footer / mega-nav and the about-page "full catalog" framing `[MED]`.

**Shape finding (now enumerated, not just asserted):** the front door is 3 lines but the practice behind it is **~50 distinct SKUs across 9 lines**. The prior run rostered the legacy catalog by name only (peptides ×4, dermatology ×1) and the shop off its homepage tiles (~14) — both badly under-reported. This pass enumerated every line off its index page: dermatology is **11 topicals**, peptides **7**, plus whole **longevity** and **sexual-wellness** lines that weren't rostered at all, and the shop is **23 SKUs**. The "full treatment library… no menu of three things" (/clinic) is literal.

**Legacy/current price split:** the Sanity `/treatments/` index cards show their own à-la-carte prices ($85 creams, $189 enclomiphene, $567–$687/quarterly TRT/HRT, $99/mo custom care) — a separate, older model from the live Astro all-in plans ($189 semaglutide, $149 Core hormones). The legacy cards are captured verbatim with their source page; current rows use the Astro prices. The legacy catalog also **closes the prior women's-hormone-pricing gap** (Women's HRT $687/quarterly, Women's Custom Care $99/mo — the Astro women's toggle was client-rendered and unreachable last run).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Weight Loss (GLP-1)** | family | — | /weight-loss | — | — | Compounded GLP-1 weight-loss programs · subcutaneous injection · all-in monthly plan *(current, Astro)* |
| Semaglutide | buyable | /weight-loss | /weight-loss | "$189/month" (m2m; "First month $149 with code SEMA1") | published | semaglutide (+ B-12, glycine, per legacy PDP) · subcutaneous injection · all-in plan, smart titration; m2m or 3-/6-mo |
| Tirzepatide | buyable | /weight-loss | /weight-loss | "$339/month" (m2m; "First month $149 with code TIRZ1") | published | tirzepatide · subcutaneous injection · all-in plan; "highest-efficacy option" |
| **Hormone Therapy (current)** | family | — | /hormones | — | — | Doctor-prescribed hormone optimization, men & women · injection/oral · all-in monthly membership *(current, Astro)* |
| Core | buyable | /hormones | /hormones | "$149/month" | published | testosterone therapy *or* enclomiphene + anastrozole (if indicated) · injection/oral · labs q90d + mobile phlebotomy included; 3-mo min then cancel |
| Enhanced | buyable | /hormones | /hormones | "$199/month" | published | everything in Core + gonadorelin (fertility/natural-production) · injection/oral · all-in |
| **Lab Testing** | family | — | /labs | — | — | At-home diagnostic panels · blood draw · one-time |
| Core 91 Panel | buyable | /labs | /labs | "$249 one-time" | published | 91 biomarkers (hormones, metabolic, nutrient, heart, immune) · at-home or walk-in draw · one-time, 50-pg report, no consult |
| Concierge Care | buyable | — | /clinic | "$99/mo" (homepage FAQ; "medications still billed at their plan rate") | partial | membership · provider visits + 4 labs/yr + personalized plan · all-in membership, meds extra; "Labs + Concierge" adds a 45-min consult (9 states) |
| **Hormone — legacy à-la-carte** | family | — | /treatments/hormone-treatment | — | — | The Sanity catalog's molecule-level hormone SKUs · injection/oral · Rx, provider-reviewed *(legacy; separate pricing model from the Astro plans above — bloodwork-gated)* |
| Fortify (Enclomiphene) | buyable | /treatments/hormone-treatment | /treatments/hormone-treatment/fortify | "$189/30 count" (alias /enclomiphene "$189"; promo /fortify-first50 "$199/month") | published | enclomiphene · oral · supports natural testosterone production; men |
| Gonadorelin | buyable | /treatments/hormone-treatment | /treatments/hormone-treatment/gonadorelin | "$49/mo" | published | gonadorelin · injection · fertility / hormonal balance; women + men |
| Sermorelin | buyable | /treatments/hormone-treatment | /treatments/hormone-treatment/sermorelin | "$159" | published | sermorelin · injection · GH-releasing peptide; energy/recovery/vitality |
| Anastrozole (estrogen blocker) | buyable | /treatments/hormone-treatment | /treatments/hormone-replacement-therapy/anastrozol-estrogen-blocker | — | on-request | anastrozole · oral · aromatase inhibitor (index card carries no price) |
| Men's Custom Care | buyable | /treatments/hormone-treatment | /treatments/hormone-treatment/mens-health | "$99/mo" | published | personalized testosterone/hormone therapy after bloodwork · injection/oral · men |
| Women's Custom Care | buyable | /treatments/hormone-treatment | /treatments/hormone-treatment/womens-health | "$99/mo" | published | personalized hormone therapy after bloodwork · injection/oral · women |
| Men's TRT (program) | buyable | /treatments/hormone-treatment | /treatments/hormone-treatment/testosterone-replacement-therapy | "$567/quarterly" | published | testosterone replacement therapy · injection · men *(legacy program pricing)* |
| Women's HRT (program) | buyable | /treatments/hormone-treatment | /treatments/hormone-treatment/hrt | "$687/quarterly" | published | perimenopause/menopause hormone replacement · injection/oral · women *(legacy program pricing)* |
| **Dermatology (Rx topicals)** | family | — | /treatments/dermatology | — | — | Prescription compounded creams · topical · charged if prescribed *(legacy Sanity catalog)* |
| Balance Acne Cream | buyable | /treatments/dermatology | /treatments/dermatology/balance-acne-treatment | "$85" | published | azelaic acid · clindamycin · niacinamide · tretinoin · cream · acne |
| Brightening Cream | buyable | /treatments/dermatology | /treatments/dermatology/brightening-cream | "$85" | published | azelaic acid · hydroquinone · kojic acid (+ green tea, resveratrol) · cream · melasma |
| Clarity Acne Cream | buyable | /treatments/dermatology | /treatments/dermatology/clarity-acne-treatment | "$85" | published | azelaic acid · clindamycin · niacinamide · tranexamic acid · cream · acne |
| Dawn Eye Cream (AM) | buyable | /treatments/dermatology | /treatments/dermatology/dawn-cream | "$85" | published | antioxidants + hydration (specifics not stated) · cream · daytime repair |
| Dusk Eye Cream (PM) | buyable | /treatments/dermatology | /treatments/dermatology/dusk-eye-cream | "$85" | published | caffeine · dexpanthenol · green tea · tretinoin · eye cream · nighttime repair |
| Flourish Cream | buyable | /treatments/dermatology | /treatments/dermatology/flourish-ghk-cu | "$115" | published | GHK-Cu · cream · anti-aging / cell renewal |
| Refine Cream | buyable | /treatments/dermatology | /treatments/dermatology/refine-cream | "$125" | published | peptides · tretinoin · estriol · niacinamide · cream · anti-aging |
| Restore Cream | buyable | /treatments/dermatology | /treatments/dermatology/restore | "$115" | published | NAD+ · cream · cellular repair / rejuvenation |
| Reversal Cream | buyable | /treatments/dermatology | /treatments/dermatology/reversal-anti-aging | "$115" | published | caffeine · GHK-Cu · niacinamide · tretinoin · cream · firming / anti-aging |
| Revitalize Eye Cream | buyable | /treatments/dermatology | /treatments/dermatology/revitalize-eye-cream | "$249/mo" | published | not stated · eye cream · under-eye (price reads "/mo" — verify) |
| Soothing Cream | buyable | /treatments/dermatology | /treatments/dermatology/soothing-cream | "$85" | published | azelaic acid · ivermectin · metronidazole · niacinamide (5/1/1/4%, per PDP) · cream · rosacea |
| **Peptides** | family | — | /treatments/peptides | — | — | Peptide therapy library · injection/oral · Rx / concierge-gated *(legacy; index lists names, no prices; some PDPs blank)* |
| BPC 157 | buyable | /treatments/peptides | /treatments/peptides/bpc-157 | — | on-request | BPC-157 · not stated · concierge/Rx |
| Dihexa | buyable | /treatments/peptides | /treatments/peptides/dihexa | — | on-request | dihexa · not stated · concierge/Rx (PDP is an H1-only shell) |
| GHK-Cu | buyable | /treatments/peptides | /treatments/peptides/ghk-cu | — | on-request | GHK-Cu · not stated · concierge/Rx |
| KPV | buyable | /treatments/peptides | /treatments/peptides/kpv | — | on-request | KPV · not stated · concierge/Rx |
| Methylene Blue | buyable | /treatments/peptides | /treatments/peptides/methylene-blue | — | on-request | methylene blue · not stated · concierge/Rx |
| NMN (peptide) | buyable | /treatments/peptides | /treatments/peptides/nmn | — | on-request | NMN · injectable (distinct from the $95 capsule NMN in the shop) · concierge/Rx |
| TB-4 | buyable | /treatments/peptides | /treatments/peptides/tb-4 | — | on-request | TB-4 (thymosin beta-4) · not stated · concierge/Rx |
| **Longevity** | family | — | /treatments/longevity | — | — | Cellular-health / anti-aging treatments · injection/oral · Rx *(legacy Sanity catalog)* |
| Glutathione | buyable | /treatments/longevity | /treatments/longevity/glutathione | "$299/quarterly" | published | glutathione · injection · antioxidant, brain/cellular support |
| L-Carnitine | buyable | /treatments/longevity | /treatments/longevity/l-carnitine | "$89" | published | L-carnitine · injection · fat metabolism / endurance / recovery |
| Lipo-Mino | buyable | /treatments/longevity | /treatments/longevity/lipo-mino | "$89" | published | lipotropic (MIC) blend · injectable · fat metabolism / detox |
| NAD+ | buyable | /treatments/longevity | /treatments/longevity/nad | "$179" | published | NAD+ · injection · mitochondrial energy / healthy aging |
| **Sexual Wellness** | family | — | /treatments/sexual-wellness | — | — | Intimacy / arousal treatments · oral/troche · Rx *(legacy Sanity catalog; "Sexual Health" in nav)* |
| Bloom | buyable | /treatments/sexual-wellness | /treatments/sexual-wellness/bloom | "$89" (promo /bloom-first50 "$89/month") | published | not stated · not stated · arousal/bonding, women + men |
| Rise | buyable | /treatments/sexual-wellness | /treatments/sexual-wellness/rise | "$99" | published | not stated (ED/arousal) · not stated · men |
| **Supplements (shop)** | family | — | shop.hevahealth.com | — | — | Shopify store · 23 SKUs · capsules/powders/creams/merch · one-time (WELCOME10 −10%; free ship >$75) |
| Lifespan Formula | buyable | shop.hevahealth.com | /products/heva-health-lifespan-formula | "$169.15" | published | proprietary longevity "Stack" (Powered by Vitaboom) · capsules · one-time |
| NMN (capsule) | buyable | shop.hevahealth.com | /products/heva-health-nmn | "$95.00" | published | NMN "Stack" · capsules · one-time |
| GLP-1 Activator | buyable | shop.hevahealth.com | /products/heva-health-glp-1-activator | "$93.50" | published | proprietary "Stack" (not stated) · capsules · one-time |
| Cognition Complex | buyable | shop.hevahealth.com | /products/heva-health-cognition-complex | "$85.00" | published | nootropic "Stack" (not stated) · capsules · one-time |
| Immune Booster | buyable | shop.hevahealth.com | /products/heva-health-immune-booster | "$80.00" | published | proprietary "Stack" (not stated) · capsules · one-time |
| Gut Harmony | buyable | shop.hevahealth.com | /products/heva-health-gut-harmony | "$65.00" | published | proprietary "Stack" (not stated) · capsules · one-time |
| Female Vitality Complex | buyable | shop.hevahealth.com | /products/heva-health-female-vitality-complex | "$63.75" | published | women's multivitamin "Stack" (not stated) · capsule pack · one-time |
| Liver Cleanse | buyable | shop.hevahealth.com | /products/heva-health-liver-cleanse | "$60.00" | published | proprietary "Stack" (not stated) · capsules · one-time |
| Revitalize Hair Formula | buyable | shop.hevahealth.com | /products/heva-health-revitalize-hair-formula | "$60.00" | published | proprietary "Stack" (not stated) · capsules · one-time |
| Male Vitality Complex | buyable | shop.hevahealth.com | /products/heva-health-male-vitality-complex | "$58.65" | published | men's multivitamin "Stack" (not stated) · capsule pack · one-time |
| Joint & Tissue Repair | buyable | shop.hevahealth.com | /products/heva-health-joint-tissue-repair | "$140.00" | published | BPC + KPV + PEA 500 + L-glutathione (per render) "Stack" · capsules · one-time |
| Restorative Sleep | buyable | shop.hevahealth.com | /products/heva-health-restorative-sleep | "$40.00" | published | proprietary "Stack" (not stated) · capsules · one-time |
| Complete Multivitamin | buyable | shop.hevahealth.com | /products/complete-multivitamin | "$34.99" | published | multivitamin (Vitamins & Minerals) · capsules · one-time |
| Digestive Support | buyable | shop.hevahealth.com | /products/glp-1-support | "$29.99" | published | digestive support (GLP-1 companion; handle = glp-1-support) · not stated · one-time |
| Colostrum Powder | buyable | shop.hevahealth.com | /products/colostrum-powder | "$29.00" | published | colostrum (Post-Workout Recovery) · powder · one-time |
| Creatine Monohydrate | buyable | shop.hevahealth.com | /products/creatine-monohydrate | "$25.00" | published | creatine monohydrate (Muscle Builders) · powder · one-time |
| MicroBurst Pre-Workout | buyable | shop.hevahealth.com | /products/microburst-pre-workout-fruit-punch | "$25.00" | published | pre-workout · powder · one-time · 3 flavors (Fruit Punch, Guava Berry, Cotton Candy) |
| Pure Whey Protein Isolate | buyable | shop.hevahealth.com | /products/pure-whey-protein-isolate-vanilla | "$45.00" | published | whey protein isolate · powder · one-time · 2 flavors (Vanilla, Chocolate) |
| Tallow Balm (Lemongrass & Lavender) | buyable | shop.hevahealth.com | /products/tallow-cream-lemongrass-lavender | "$27.00" | published | tallow balm (Body Care) · cream · one-time |
| Heva Signature Baseball Hat | buyable | shop.hevahealth.com | /products/heva-signature-baseball-hat | "$35.00" | published | merch (not a supplement) · apparel · one-time |

## Verbatim anchors

- **Semaglutide current price (Astro):** "$189/month … Save $10/month vs. month-to-month … First month $149 with code SEMA1" — /weight-loss
- **Tirzepatide current price (Astro):** "$339/month … Save $60/month vs. month-to-month … First month $149 with code TIRZ1" — /weight-loss
- **Semaglutide molecule (legacy PDP):** "Ingredients: Semaglutide, B-12, Glycine" · "Subcutaneous injection as directed by your provider." — /treatments/weight-loss/semaglutide-copys/
- **Hormone Core (verbatim, Astro):** "$149/month … Testosterone therapy or enclomiphene · Anastrozole (if clinically indicated) · Lab testing every 90 days · Mobile phlebotomy … 3-month minimum, then cancel anytime." — /hormones
- **Legacy hormone catalog (index cards):** "Enclomiphene … $189/30 count" · "Gonadorelin … $49/mo" · "Sermorelin … $159" · "TRT … $567/quarterly" · "HRT … $687/quarterly" · "Men's Custom Care … $99/mo" · "Women's Custom Care … $99/mo" — /treatments/hormone-treatment
- **Dermatology (index cards, verbatim):** "Balance Acne Cream … azelaic acid, clindamycin, niacinamide, and tretinoin … $85" · "Flourish … GHK-Cu … $115" · "Refine … peptides, tretinoin, estriol, and niacinamide … $125" · "Soothing Cream … azelaic acid, ivermectin, and niacinamide … $85" — /treatments/dermatology
- **Longevity (index cards):** "Glutathione … $299/quarterly" · "L-Carnitine … $89" · "Lipo-Mino injectable … $89" · "NAD+ … $179" — /treatments/longevity
- **Sexual wellness (index cards):** "Bloom … Arousal, excitement, and bonding formulated for women + men … $89" · "Rise … formulated just for men … $99" — /treatments/sexual-wellness
- **Peptides library (index, no prices):** "BPC 157 · Dihexa · GHK-Cu · KPV · Methylene Blue · NMN · TB-4" — /treatments/peptides
- **Empty category:** "No treatments in this category yet." — /treatments/allergy
- **Shop catalog (authoritative):** 23 products via `shop.hevahealth.com/products.json` — 12 VITABOOM "Stack" SKUs (vendor `VITABOOM COLLECTIVE`, product_type `Stack`) + 11 first-party `Heva Shop` items (Vitamins, Muscle Builders, Pre-Workout, Proteins, Body Care, Digestive, Recovery). Homepage tiles showed only ~14.
- **Molecule-sourcing audit (`not stated`):** the VITABOOM "Stack" supplements list ingredient *brands* on pouch renders but no single active per SKU → `not stated`. Peptide PDPs are blank shells; the index lists names only. Dermatology/longevity/hormone/sexual molecules are read off the **index-card descriptions** (product copy) — attested. Joint & Tissue Repair's "BPC + KPV + PEA 500" is read off the render image — render-attested.

## Deep blocks

Earned blocks for the two flagship clinical SKUs that carry captured **hero product renders**, plus the supplement-line shape.

### Semaglutide — the GLP-1 flagship
The weight-loss anchor. **Current price $189/mo** (Astro /weight-loss), promo first month $149 (SEMA1). Heva's formulation is **compounded semaglutide + B-12 + glycine** (the B12/glycine added to blunt nausea and preserve muscle, per the legacy PDP), subcutaneous, smart-titrated. Not FDA-approved (compounded, 503A). **Hero render:** `captures/2026-06-04/images/semaglutide.jpg` — a clean isolated dark-olive vial, silver cap, "SEMAGLUTIDE / HEVA®" on the brand cream ground.
*Legacy-price note:* the Sanity PDP still shows the old "$149/mo within a $99/month Heva Wellness Plan" model — superseded by the all-in Astro pricing; do not cite the legacy number as current.

### Soothing Cream — Rx dermatology exemplar
Represents the 11-SKU legacy `/treatments/dermatology` Rx-topical line. **$85** (index card), a rosacea cream of **azelaic acid / ivermectin / metronidazole / niacinamide (5/1/1/4%)** (the index card lists three actives; the PDP adds metronidazole + percentages), once-daily topical, charged only if prescribed. **Hero render:** `captures/2026-06-04/images/soothing-cream.png` — a clean isolated olive tube, "HEVA / Soothing / Rosacea Cream / RX ONLY." The other ten derm creams ($85–$249) follow the same olive-tube identity.

### Supplement stacks — Shopify line shape
The shop is **two sub-lines**: 12 curated multivitamin **"Stacks"** repackaged from third-party brands (vendor `VITABOOM COLLECTIVE`, "Powered by Vitaboom") — single-molecule `not stated` — and 11 **first-party "Heva Shop"** basics with real categories (creatine, whey, multivitamin, pre-workout, colostrum, tallow balm, a GLP-1 digestive aid, merch). 23 SKUs total, **$25–$169**. **Reference render:** `captures/2026-06-04/images/supplement-stack.webp` — the cream "HEVA Supplement Stack" box + a labeled daily pouch (Male Vitality Complex) + loose pills.

## Provenance

- **Pages read (this pass):** shop.hevahealth.com/products.json (authoritative shop census, free); /treatments/ index pages — peptides, dermatology, longevity, sexual-wellness, hormone-treatment, allergy (all via `fc.py scrape --homepage`); `fc.py map --search treatments` for the catalog census; sitemap-index.xml (free, Astro pages only — Sanity catalog not in it). Carried forward from the prior pass: /weight-loss, /hormones, /labs, homepage (current Astro prices); semaglutide + soothing-cream legacy PDPs (molecules + hero renders).
- **Scope — complete at the indexed level across all 9 lines:** the 3 current Astro clinical lines (full pricing); Concierge from homepage FAQ; the **legacy Sanity catalog now fully enumerated off its index pages** — dermatology (11, priced + molecules), peptides (7, names only — no index prices), longevity (4, priced), sexual-wellness (2, priced), hormone-treatment (à-la-carte molecules, priced; **closes the prior women's-hormone-pricing gap**); shop **23 SKUs** via /products.json. /treatments/allergy = live-but-empty scaffold (rostered as a finding, not a line).
- **Collapsed leaf-variants (by design):** Shopify flavor SKUs (MicroBurst ×3, Whey ×2) → one row each, flavors noted; Sanity promo slugs (`-first50`) and a disabled `(X) Enclomiphene+` (heva-fortify) card → noted on the primary row, not separate rows; `/treatments/hormone-treatment/{enclomiphene,hrt,mens-health,…}` category-alias landings folded into the molecule rows.
- **Gated/unreachable:** peptide per-SKU prices (index lists names only; PDPs blank/concierge-gated); Anastrozole index price (card carried none); Astro women's hormone toggle still client-rendered (but the *legacy* catalog supplied women's HRT/Custom-Care pricing).
- **Snapshot caveat:** prices are point-in-time — Astro promo codes (SEMA1/TIRZ1/WELCOME10), Sanity `-first50` promos, and a brand mid-replatform (legacy Sanity → Astro) make several numbers volatile; the Sanity index-card prices are a separate model from the Astro plans. Re-check next run.
- **Run profile:** deepen-offerings (breadth) — +7 credits (1 map + 6 index scrapes; shop /products.json + sitemap free). Roster ~2× the prior pass (≈30 → ≈50 SKUs); 4 new/expanded lines (dermatology 1→11, peptides 4→7, longevity +4, sexual-wellness +2, legacy hormone +8, shop 14→23). Hero renders carried from the prior same-day capture (no new asset capture this pass).
