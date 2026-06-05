---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: marekhealth.com
captured_at: 2026-06-04
site_notes: "Two catalogs. (1) marekhealth.com treatments = goal/condition landing pages (one per vertical); molecules are named in copy but per-drug pricing is entirely GATED behind the $299 intake/login — only the $299 intake, $450 lab floor, and $80–200/mo ongoing-care figures are public. (2) Labs live on the SIBLING Shopify store marekdiagnostics.com with PUBLISHED à-la-carte prices (panels + 100+ individual biomarkers + lab-builder) — drawn in-person at Quest; not in NY/NJ/RI. Apparel SKUs at /apparel (merch). Prices A/B-volatile (homepage cart_variant split) — re-check next run. No isolated product/SKU renders exist (service brand); treatment pages carry editorial lifestyle heroes only."
---

## Portfolio overview

Marek's roster is a **service funnel, not a product catalog**. The public, purchasable layer is thin and front-loaded — a **$0 discovery call → $299 Guided Optimization® intake → "from $450" lab panel → ongoing à-la-carte care** — while the actual therapeutics (TRT, GLP-1s, peptides, "500+ therapies") sit **behind the intake/login with no public per-drug price**. So nearly every treatment line is `on-request` by design; the only published prices on marekhealth.com are the intake/funnel anchors. The one place with real published per-SKU pricing is the **sibling labs storefront marekdiagnostics.com** (Shopify), which sells panels and 100+ individual biomarkers à la carte.

Prominence (calibrated):
- **Guided Optimization® intake + labs** — the hero offering: `$299` CTA repeated site-wide, the homepage's central pricing card. `[HIGH]` (own hero + CTA).
- **TRT / testosterone** — the lead therapeutic vertical: deepest page, first treatment nav, hero biomarker (870 ng/dL), the protocol exemplar ("Testosterone Cypionate 80mg"). `[HIGH]` (own depth + hero).
- **Diagnostic labs (marekdiagnostics.com)** — a separately-prominent wedge with its own storefront and "lab prices down 33%" hero. `[HIGH]`.
- **Weight-loss (GLP-1), Sexual health** — prominent co-equal secondary tiles. `[MED]` (tile/nav order).
- **Hair, Look-younger, Heart, Fertility, Brain fog, Sleep, Performance** — long-tail treatment tiles, same template. `[MED/LOW]` (grid order; A/B-volatile).

## Roster

Complete at the **indexed level** Marek exposes publicly: the funnel offerings, the 10 treatment families (molecules page-attested in `What`; per-drug leaves are gated, not public), and the diagnostics line + tier/exemplar SKUs (a Shopify catalog — tiers + marked exemplars, not all 108 biomarkers).

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Guided Optimization® | family | — | /sign-up | — | — | Marek's master telehealth program: labs + coaching + partnered-provider Rx |
| Free Discovery Call | buyable | Guided Optimization® | /dc/form/discovery-intro | "$0" | published | consult · 30-min video · no commitment, no card |
| Guided Optimization® Intake | buyable | Guided Optimization® | /sign-up | "$299" | partial | intake service · 45-min video coach session + health-history + lab-panel strategy · labs & drugs paid separately on top |
| Lab panel (intake floor) | buyable | Guided Optimization® | /sign-up | "starting at $450" | partial | diagnostics · custom panel built at intake · floor; final set varies |
| Ongoing care / coaching | buyable | Guided Optimization® | /sign-up | "averages $80–200/month" | partial | coaching + Rx refills + monitoring · monthly · cancel anytime; drug cost gated (homepage JSON-LD gives a lower in-house estimate — see profile.md) |
| Testosterone / TRT | family | Guided Optimization® | /testosterone | behind intake | on-request | testosterone · injection (preferred) + topical cream · Rx via intake; Schedule-III; ester "Testosterone Cypionate 80mg" on homepage mock |
| Weight loss | family | Guided Optimization® | /weight-loss | behind intake | on-request | semaglutide · tirzepatide · GLP-1 (injectable) · Rx via intake |
| Sexual health | family | Guided Optimization® | /sexual-health | behind intake | on-request | tadalafil · bremelanotide (PT-141) · oral/injectable · Rx via intake |
| Hair loss prevention | family | Guided Optimization® | /hair-loss | behind intake | on-request | finasteride · dutasteride · minoxidil · oral/topical · Rx via intake |
| Look younger | family | Guided Optimization® | /look-younger | behind intake | on-request | BHRT (bio-identical hormone therapy) · form not stated · Rx via intake |
| Better heart health | family | Guided Optimization® | /heart-health | behind intake | on-request | bempedoic acid · oral · Rx via intake |
| Fertility | family | Guided Optimization® | /fertility | behind intake | on-request | HCG · NAD+ · injectable · Rx via intake |
| Remove brain fog | family | Guided Optimization® | /think-sharper | behind intake | on-request | molecule not stated · protocol · Rx via intake |
| Sleep better | family | Guided Optimization® | /sleep-better | behind intake | on-request | molecule not stated · protocol · Rx via intake |
| Perform better | family | Guided Optimization® | /performance | behind intake | on-request | molecule not stated (peptides referenced) · protocol · Rx via intake |
| Marek Diagnostics (labs) | family | — | marekdiagnostics.com | — | — | sibling Shopify storefront; à-la-carte panels + 100+ biomarkers; Quest draw; not in NY/NJ/RI |
| Total Health Panel — Comprehensive | buyable | Marek Diagnostics | marekdiagnostics.com/products/total-health-panel-comprehensive | "$595.00" | published | lab panel · 80+ biomarkers · "from $53.70/mo" Affirm; Male/Female × ±45-min lab review |
| Total Health Panel — Complete / Executive | buyable | Marek Diagnostics | marekdiagnostics.com/products/total-health-panel-complete · …-executive | — | on-request | lab panel · higher tiers · *(exemplar; tier prices not captured this run)* |
| Total + Free Testosterone | buyable | Marek Diagnostics | (no PDP — /pages/lab-builder card) | "$55.00" | published | biomarker · Total Testosterone (ECLIA) + Free Testosterone (Direct) · *(exemplar)* |
| Comprehensive Metabolic Panel (CMP) | buyable | Marek Diagnostics | (no PDP — /pages/lab-builder card) | "$9.00" | published | biomarker · kidney/metabolic · *(exemplar — cheapest tier)* |
| Estradiol, Standard (ECLIA) | buyable | Marek Diagnostics | (no PDP — /pages/lab-builder card) | "$20.00" (reg "$30.00") | published | biomarker · sex hormones · *(exemplar)* |
| Androgen Receptor Sensitivity (CAG) | buyable | Marek Diagnostics | marekdiagnostics.com/products/androgen-receptor-cag-repeat-genetic-test | "$500.00" | published | genetic test · CAG-repeat · *(exemplar — priciest)* |
| APOE Genotyping (Alzheimer's Risk) | buyable | Marek Diagnostics | marekdiagnostics.com/products/apoe-genotyping-alzheimers-risk | "$200.00" (reg "$400.00") | published | genetic test |
| MTHFR, DNA Analysis | buyable | Marek Diagnostics | marekdiagnostics.com/products/mthfr-dna-analysis | "$225.00" (reg "$275.00") | published | genetic test |
| Build your own panel | buyable | Marek Diagnostics | marekdiagnostics.com/pages/lab-builder | from "$9.00" / marker | published | custom panel · 100+ (108) individual biomarkers |
| Apparel / merch | family | — | /apparel | — | — | branded merch — tees, flannel, trucker hat, university crew *(exemplar SKUs; prices not captured)* |

## Verbatim anchors

- **$299 intake (homepage pricing card):** "Marek Health Protocol — $299 to get started… What's included: 45-min intake assessment; Health history review; Custom lab panel strategy." Then "What comes next (paid separately): **Lab panel — starting at $450**… Lab review + medical provider consultation… Treatments shipped to your door… Exclusive access and pricing* On TRT, GLP-1s, peptides, and 500+ other treatments." → intake = a published floor, all-in gated ⇒ `partial`.
- **Ongoing cost:** homepage FAQ (rendered) — *"Ongoing treatment averages **$80–200/month** with no subscription required."* The homepage JSON-LD SEO block states a different, lower in-house estimate (year-1 vs thereafter; not shown on the rendered page) — recorded verbatim in `profile.md`, not reconciled.
- **Free consult:** "Free Consultation — $0 · 30-min call… No commitment, No credit card, No pressure."
- **TRT forms (/testosterone):** "**Testosterone Injections** — As our preferred route of administration of TRT…" and "**Topical Testosterone Cream** — …needle-free optimization." (no price on page).
- **Diagnostics (marekdiagnostics.com):** "Total Health Panel - Comprehensive **$595.00** … 4 interest-free installments, or from **$53.70/mo**"; individual markers "CMP **$9.00**", "Lipid Panel **$9.00**", "CBC **$9.00**$12.00 -25%", "Estradiol, Standard **$20.00**$30.00 -33%", "Total Testosterone … & Free Testosterone **$55.00**"; genetics "Androgen Receptor … **$500.00**", "APOE … Sale **$200.00** Regular $400.00", "MTHFR … Sale **$225.00** Regular $275.00".
- **Molecule sourcing audit (`not stated` rows):** /think-sharper, /sleep-better, /performance name no molecule for their own line (copy is symptom/benefit + the cross-sell grid only) — grepped; recorded `not stated`, not inferred. /look-younger names the modality "**BHRT**" (benefits-of-BHRT section) but no specific molecule. The **$1,754** figure on /look-younger is a *consumer-skincare-spend survey stat*, **not** a Marek price — excluded from the roster.

## Deep blocks

**None earned at the per-SKU level** — the roster carries this company: the public layer is a handful of funnel anchors + a gated drug catalog, and the diagnostics SKUs are self-explanatory Shopify rows. One portfolio-level asset note (opt-in for this run):

- **Treatment-page imagery (the run's "product page images" ask).** Marek is a **service** brand with **no isolated product/SKU renders** — its treatment ("product") pages use dramatic editorial chiaroscuro lifestyle photography, not bottle/vial shots. The closest thing to a product render anywhere is a single low-res **vial + syringe** on the TRT page (the "Testosterone Injections" option image). Representative treatment-page heroes were promoted to `captures/2026-06-04/images/`:
  - `testosterone-trt-vial.webp` — the **one genuine product render** (vial + syringe; the injectable-TRT option)
  - `testosterone-hero.webp` (rim-lit man) · `sexual-health-hero.webp` (couple) · `performance-hero.webp` (silhouetted athlete) · `fertility-hero.webp` (father + newborn) · `heart-health-hero.webp` (anatomical heart) · `think-sharper-hero.webp` (man studying) · `sleep-better-hero.webp` (6:00 clock) · `look-younger-hero.webp` (beauty portrait)
  - These are **editorial heroes, not SKU renders** — useful as visual-identity reference, not product photography. (`og:image` and JSON-LD logo both 404 on this site.)

## Provenance

- **Pages read:** homepage + all 10 treatment pages + `/faqs` + `/about-marek` (marekhealth.com), and `marekdiagnostics.com` home (the published-price source) — all Firecrawl, 2026-06-04, md5-unique. Treatment molecules are page-attested from each treatment page's copy; the only dosed example is the homepage protocol mockup.
- **Scope:** enumerated = the public funnel offerings, the 10 treatment families (molecules named, per-drug prices gated), and the diagnostics line + tier/exemplar SKUs. Noted-but-not-enumerated = the full 108 individual biomarkers (Catalog leaf — exemplars only), the Complete/Executive panel tiers (PDPs not captured), specialty/budget panel collections, and apparel SKUs (prices not captured).
- **Gated/unreachable:** every per-drug treatment price (behind the $299 intake/login) — `on-request` by design; "500+ therapies" not publicly enumerable.
- **Point-in-time caveat:** marekhealth.com A/B-tests the homepage pricing module (cart_variant); marekdiagnostics runs promo strike-through pricing. Captured prices are a snapshot, not fixed.
- **Run profile:** `+offerings` with the **hero-product-images** opt-in (treatment-page heroes promoted; documented that no isolated SKU renders exist). Sibling labs domain pulled in for published lab pricing.
