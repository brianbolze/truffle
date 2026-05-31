---
schema_version: 1

# Identity
domain: maximustribe.com             # primary key (maximustribe.com → www.maximustribe.com, 200, clean resolve)
name: Maximus
aliases: [Maximus Tribe]             # "Maximus Tribe" is the legal/brand long-form (maximustribe.com, @maximustribe); app at app.maximustribe.com
parent: []                           # independent, founder-led (Dr. Cameron Sepah); no parent company evident on-site
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "maximustribe.com → www.maximustribe.com (plain curl 200, no bot block; Firecrawl clean). Stack = Gatsby (React SSG: rawHtml has ___gatsby, gatsby-*, /page-data/, page-data.json) on a Sanity headless CMS (all imagery cdn.sanity.io/images/qag74ilj); branding.designSystem said 'custom' — WRONG (§5.4; another Gatsby-mislabeled-'custom' data point). MEGA-NAV RENDERS in markdown — full flyout (Testosterone/Weight Loss/Mood & Stress/Lab Testing/Growth Hormone Peptides/More) captured cleanly, unlike hims' JS-walled nav. /v2/map = 335 URLs but ~75% noise: /resources/* (blog), /resources/collections/*, /resources/articles/N pagination, /tools/*; the product catalog is the handful of /testosterone, /weight-loss, /hair-growth, /vardenafil-tadalafil-sildenafil-bloodflow, /growth-hormone-peptides, /oxytocin-calming-cream, /lab-tests + /labs, /building-blocks paths (all also in homepage links). PRICING IS IN MARKDOWN (US-geo'd, not JS-walled): list prices like 'Starting at $149.99' show on product + homepage; the funnel/checkout is the app.maximustribe.com subdomain (registration), support.maximustribe.com is the help center. Logo = inline data-URI SVG wordmark (not hostable, like linear/aws/nike) → favicon fallback https://www.maximustribe.com/favicon-32x32.png. Brand color #0053C5 cobalt blue CONFIRMED via screenshot (it's the hero/CTA/card hue, not chrome). Notable: /official-information-about-maximus is a deliberate 'Hey AI, learn about us' page (GEO/LLM-optimization) — a high-signal capture target. No §5.1 contamination (9 bodies unique, sourceURLs matched; maxAge:0 + location:US + waitFor:3500 + serialized)."
key_pages:
  testosterone: /testosterone                                  # flagship vertical (cream/injectable/oral/enclomiphene)
  weight_loss: /weight-loss                                    # GLP-1 (semaglutide) + GLP-1/GIP (tirzepatide)
  hair_growth: /hair-growth                                    # min/fin/dutasteride, all-in-one gel
  blood_flow: /vardenafil-tadalafil-sildenafil-bloodflow       # ED / sexual health
  peptides: /growth-hormone-peptides                           # sermorelin / GHRH peptides
  lab_tests: /lab-tests                                        # at-home T test (10 markers); comprehensive panel at /labs (146 markers)
  about: /about-us                                             # founding (2020, Dr. Cameron Sepah), "performance medicine" thesis
  science: /science                                            # clinical-research positioning; white papers at /science-all
  oxytocin: /oxytocin-calming-cream                            # patent-pending Oxytocin Calming Cream (Mood & Stress)
  multivitamins: /building-blocks                              # prescription multivitamins (not separately captured)
  ai_page: /official-information-about-maximus                 # "Hey AI, learn about us" — GEO page
unverified_fields:
  - "Per-protocol / per-dose pricing on product subpages (e.g. /testosterone/oral-testosterone, /weight-loss/tirzepatide-standard) — only hub + homepage list prices captured ('Starting at $X'); per-SKU detail is an offerings.md job."
  - "Comprehensive lab panel — 'up to 146 markers' claimed; the marker list itself was not enumerated."
  - "Founding-team size, headcount, funding, revenue — private company; not on the marketing site (a deep-research job)."
  - "Building Blocks (Rx multivitamin) page not separately captured — listed in nav under 'Prescription Multivitamins'."

# Description — one sentence
description: "A DTC 'performance medicine' telehealth clinic for men (now expanding to women) pairing licensed-physician oversight and at-home labs with compounded protocols across testosterone, GLP-1 weight loss, hair, sexual health, peptides, and mood — differentiating on its own published clinical research."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth platform service + Rx (compounded) products — the cohort pattern (cf. hims/hone)
portfolio_shape: Multi-product       # testosterone, weight loss, hair, blood flow/ED, peptides, mood/oxytocin, labs, multivitamins — distinct, separately-bought verticals
business_model: Subscription         # recurring monthly protocols (e.g. "$149.99/mo"); direct-pay, no insurance, FSA/HSA eligible
primary_industry: Healthcare & Life Sciences

# Visual identity — from Firecrawl `branding` (homepage), confirmed against screenshot
logo_url: https://www.maximustribe.com/favicon-32x32.png   # favicon fallback — real logo is an inline data-URI SVG "Maximus" serif wordmark (not hostable)
brand_colors: { primary: "#0053C5", secondary: "#01429B", background: "#FFFFFF", text: "#000000" }   # cobalt blue confirmed via screenshot (hero tiles, CTAs, product cards, stat callouts); white-ground, blue-accent identity
fonts: [Inter, Victor Serif]         # branding.fonts: Inter=body, Victor Serif=heading (serif heds are a deliberate "premium clinical" signal)
color_scheme: light                  # branding.colorScheme + screenshot
design_framework: gatsby             # rawHtml: ___gatsby + gatsby-* + /page-data/ (Gatsby React SSG) on a Sanity CMS; NOT branding.designSystem's "custom" (§5.4)
---

## Overview

Maximus (Maximus Tribe) is a direct-to-consumer **"performance medicine"** telehealth clinic, founded in 2020 by **Dr. Cameron Sepah** (Harvard-educated clinical psychologist, ex-UCSF psychiatry professor). It began by treating low testosterone in men and has expanded into a multi-vertical men's-health platform — testosterone, GLP-1 weight loss, hair, blood flow/ED, growth-hormone peptides, mood/sleep, and lab testing — now positioned for **both men and women**. The model is the cohort standard (free questionnaire → 100% online physician consult → optional at-home labs → personalized protocol compounded and shipped → ongoing care team), but the brand's explicit thesis is *optimization, not normalization* — "treating people, not averages," with 50k+ members claimed.

## What they offer

Eight verticals, each its own storefront (a future `offerings.md` would enumerate per-protocol; list prices below are verbatim from the captured pages):

- **Testosterone** — the flagship and origin line, sold by *format*: **Testosterone Cream**, **Injectable Testosterone (TRT)**, **Oral Testosterone**, and **Enclomiphene** (a fertility-preserving, secondary-hypogonadism option Maximus leans into heavily). Anchored by proprietary white papers ("Oral Native TRT," "liver-safe" oral-T, enclomiphene protocols).
- **Weight Loss (GLP-1)** — **Semaglutide** "Starting at $149.99/mo" (GLP-1) and **Tirzepatide** "Starting at $249.99" (GLP-1 + GIP, "our most powerful"). Custom-dosage and starter-pack variants exist.
- **Mood & Stress** *(NEW)* — **Oxytocin Calming Cream**, a **patent-pending** proprietary transdermal formulation ("Starting at $99.99"), pitched for sleep/stress/calm with its own clinical-trial stats.
- **Lab Testing** *(NEW)* — **Comprehensive panel (up to 146 markers)** at `/labs` and an **At-Home Testosterone Test (10 markers)** at `/lab-tests`; labs double as the funnel wedge.
- **Growth Hormone Peptides** *(NEW)* — GHRH peptides incl. **Sermorelin** ("reduce fat, recover faster").
- **Blood Flow / ED** — **Vardenafil, Tadalafil, Sildenafil** (PDE5 inhibitors).
- **Hair Growth** — **All-in-One Gel** plus oral/topical minoxidil, finasteride, dutasteride combinations.
- **Prescription Multivitamins** — **Building Blocks** (foundational nutrition).

`portfolio_shape: Multi-product` — eight distinct, separately-chosen verticals, not variants of one thing.

## How it works / model

A telehealth clinic model, direct-pay (no insurance, FSA/HSA eligible): **free detailed health questionnaire → 100% online visit with a US-licensed, board-certified physician → optional at-home lab work → a personalized protocol (medications + supplements + lifestyle guidance) compounded at a licensed partner pharmacy and shipped discreetly → ongoing care-team messaging and doctor-led dose adjustments.** Monetized via recurring monthly protocols (e.g. "$149.99/mo"). Medications are **compounded** at US-based, USP-compliant licensed pharmacies sourcing APIs from FDA-registered manufacturers; compounded-drug FDA non-approval disclaimers appear on product pages.

## Positioning & audience

- **Who:** B2C, originally men optimizing testosterone/performance; explicitly broadening to women ("empowers both men and women").
- **The claimed edge — the differentiator that recurs everywhere:** Maximus frames most telehealth as commodity *prescription-delivery* services and itself as a **performance-medicine R&D company** that **runs and publishes its own clinical trials**, develops **proprietary/patent-pending formulations** (Oxytocin Calming Cream), and designs protocols with academic clinicians. "If we haven't seen strong data supporting a treatment's efficacy, we don't offer it… prioritizing safety over biohacking."
- **Against:** the men's-health telehealth field (Hims, Hone, PeterMD, Healthspan) and TRT/GLP-1 players — competing on **clinical rigor + proprietary protocols + an academic advisory board**, not breadth or price.

## Nav structure

Full mega-nav (rendered in markdown):

```
- Testosterone — /testosterone
  - Testosterone Cream — /testosterone/Testosterone-Cream
  - Injectable Testosterone — /testosterone/Injectable-TRT
  - Oral Testosterone — /testosterone/oral-testosterone
  - Enclomiphene — /testosterone/enclomiphene-only
  - At-Home Testosterone Test — /lab-tests
- Weight Loss — /weight-loss
  - Tirzepatide — /weight-loss/tirzepatide-standard
  - Semaglutide — /weight-loss/semaglutide-standard
- Mood & Stress (NEW)
  - Oxytocin Calming Cream — /oxytocin-calming-cream
- Lab Testing (NEW)
  - Comprehensive Lab Testing (146 markers) — /labs
  - At-Home Testosterone Test (10 markers) — /lab-tests
- Growth Hormone Peptides (NEW) — /growth-hormone-peptides
  - Sermorelin Injections — /growth-hormone-peptides/sermorelin-growth-hormone-therapy
- More
  - Blood Flow — /vardenafil-tadalafil-sildenafil-bloodflow
  - Prescription Multivitamins (Building Blocks) — /building-blocks
  - Hair Growth — /hair-growth (All-in-One Gel — /hair-growth/all-in-one-gel)
  - Scientific Research / white papers — /science-all
- Learn: Blog — /resources ; Research — /science-all
- Company: About — /about-us ; Community — /community ; Partners — /partners ; Careers ; Contact ;
  "Hey AI, learn about us" — /official-information-about-maximus
```

## Credibility & proof

- **Academic medical advisory board** (the central trust signal): Dr. Cameron Sepah (CEO; Harvard, ex-UCSF), Dr. Matt Coward (Urology, UNC), Dr. Wayne Hellstrom (Professor of Urology / Chief of Andrology, Tulane), Dr. Justin Houman (Urology, Cedars-Sinai), Dr. Eugene Shippen (author, *The Testosterone Syndrome*).
- **Proprietary clinical research:** publishes its own white papers / clinical studies (`/science-all`) — e.g. "Liver Enzyme Trends in Patients using Oral Testosterone," enclomiphene & topical-T-for-fertility papers.
- **Scale & trust badges:** "50k+ members," **LegitScript-approved** (seal links to verification), press "as seen in" logos, clinical-trial stat callouts (e.g. Oxytocin: ↑71% happiness, ↓51% anxiety, +25 min sleep).
- **Compliance:** "Compounded medications are not approved or evaluated for safety, efficacy, or quality by the FDA"; supplement-style "not been evaluated by the Food and Drug Administration"; a refund guarantee if "not approved for treatment" (minus consult cost).

## Visual & brand impression

A clean, premium, **clinical-but-masculine** light-mode identity: white ground with **cobalt-blue `#0053C5`** as the single dominant brand hue (hero "Boost testosterone" tile, product cards, CTAs, and data-viz callouts), confident lifestyle photography, and blue product packaging. **Serif headings (Victor Serif)** over **Inter** body deliberately signal "scientific authority / premium" rather than the warmer DTC look (cf. hims' earthy tan). Heavy use of clinical data visualization (↑3.1x free testosterone, −28% body fat curves) and professor headshots reinforces the science-forward positioning. Reads as a well-funded, brand-mature site on par with the top of the cohort.

## Strategic read

Maximus's durable, recordable state: a **founder-led (Dr. Sepah), independent** men's-health telehealth clinic whose wedge is **proprietary, published clinical research + patent-pending formulations**, not breadth or price — the self-described "performance medicine *R&D* company" vs. commodity "prescription delivery." Two signals worth tracking for a consumer: (1) the **men→women expansion** (origin was male TRT; site now claims both), a TAM move; and (2) **enclomiphene / oral-native-TRT** as a fertility-preserving differentiator it has invested white-papers in. Distinctive tell: a dedicated **`/official-information-about-maximus` "Hey AI, learn about us" page** — explicit GEO/LLM-optimization, a forward-looking signal few cohort peers show. Unlike hims (public-company parent) it has **no parent** — an independent, clinician-built company.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30):** homepage (`/`, rich pass: markdown + html + rawHtml + links + branding + images + full-page screenshot); `/testosterone`, `/weight-loss`, `/hair-growth`, `/vardenafil-tadalafil-sildenafil-bloodflow`, `/growth-hormone-peptides`, `/lab-tests`, `/about-us`, `/science` — each markdown + links + full-page screenshot. Site inventory via `/v2/map` (limit 500; ~75% `/resources/*` blog noise filtered out).
- **Capture mechanics:** `maxAge:0` + `location:{country:US}` + `waitFor:3500` + serialized; all 9 bodies unique + sourceURLs matched (no §5.1 contamination). **10 credits**, clean run.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned markdown: `captures/2026-05-30/*.md`.
- **Couldn't get:** per-protocol/dose pricing on product subpages; lab marker lists; private-company financials/headcount. See `unverified_fields`.
