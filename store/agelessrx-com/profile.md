---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: agelessrx.com
name: AgelessRx
aliases: []
parent: []
owns: []
socials: { facebook: "https://www.facebook.com/agelessrx1/", x: "https://x.com/ageless_rx", instagram: "https://www.instagram.com/agelessrx_longevity/", linkedin: "https://www.linkedin.com/company/agelessrx", youtube: "https://www.youtube.com/channel/UCHtmUJeRukilnzfNVJwbnuw" }   # JSON-LD sameAs (handles match the entity)

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "WordPress (wp-content/themes/agelessrx-2024; hosted on WP Engine — image CDN surfaces as arxdotcom.wpengine.com; branding.designSystem said 'bootstrap' — wrong, ignore per playbook). Map returns ~479 URLs but ~63% is blog noise (253 /tag/*, 49 /category/*); the real catalog is /treatments/ (48 products) — pull it + the homepage nav, not the map. Nav has two parallel axes: by Treatment (product family) and By Need (19 conditions). Pricing shows as 'Starting at $X' on each product + category page (e.g. /metformin, /semaglutide-glp-1s, /biological-age-test); real checkout + final price sits behind the customer.agelessrx.com portal, and CTA deep-links carry rotating coupon codes (MET20, GLP100, SEMA100OFF…) — treat those prices/codes as point-in-time."
key_pages:
  treatments: /treatments/
  how_it_works: /how-we-work/
  about: /about/
  research: /research/
  longevity_science: /longevity-science/
  glp1: /semaglutide-glp-1s/
  nad: /all-nad-support/
  bioage_tests: /biological-age-test/
  metformin: /metformin/
  faq: /faq/
  portal: https://customer.agelessrx.com/
unverified_fields:
  - "Founding year, headcount, funding/financing — not on captured marketing pages (© reads '2026 by AgelessRx'; XPRIZE Healthspan semi-finalist is mentioned but no funding stated)."
  - "Per-SKU prices are a point-in-time snapshot, not fixed — each product/category page shows a 'Starting at $X' floor and CTA links bake in rotating coupon codes; final price is set behind the customer.agelessrx.com portal."
  - "Full per-product pricing — only category + flagship pages captured (Metformin, GLP-1, BioAge); the ~40 other product detail pages were not individually scraped."

description: "A direct-to-consumer longevity telehealth platform prescribing off-label anti-aging medications (rapamycin, metformin, NAD+, GLP-1s), peptides, and biological-age testing through US-licensed clinicians, fulfilled by compounding pharmacies as auto-refill subscriptions."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://agelessrx.com/wp-content/themes/agelessrx-2024/assets/images/agelessrx-logo-2024.svg   # canonical wordmark (on-domain SVG)
logos:                               # 2.5 module — measured by fc.py logos; the consumer applies the size bar
  wordmark: { src: https://agelessrx.com/wp-content/themes/agelessrx-2024/assets/images/agelessrx-logo-2024.svg, w: 146, h: 32 }   # dark "ageless" + teal "rx"; on-brand, reads on light
  logomark: { src: "https://www.google.com/s2/favicons?domain=agelessrx.com&sz=256", px: 100, transparent: false }                 # white "a." on a baked dark-green square; <128px short side (recorded anyway)
  # og omitted — the only DECLARED og:image is a NYT press logo (newyorktimes-logo.png, 400x53), fails the >=600px cover gate
brand_colors: { primary: "#023B37", accent: "#FFB54C", link: "#0B857D" }   # STRAIN: brand hue is the deep forest-green hero/footer bands; amber is the CTA accent. branding payload inverted these (primary→amber) — corrected against screenshot.
fonts: [AgelessSans, CheltenhamPro]   # CheltenhamPro = editorial NYT-style serif for headings; AgelessSans for body
color_scheme: light
design_framework: wordpress
---

## Overview

AgelessRx is a DTC longevity/anti-aging telehealth company built around the thesis that aging is a treatable, preventable process ("aging is a puzzle that can be solved"). It runs a 100%-online platform where US-licensed clinicians review an intake, and — if appropriate — prescribe off-label longevity medications, peptides, and supplements that are compounded/fulfilled by 503A pharmacy partners and shipped as auto-refill subscriptions. Alongside the pharmacy it sells at-home and lab-based **biological-age testing** (methylation + phenotypic) as the measurement layer. Headquartered in Ann Arbor, MI; positions itself as a research-leading, "first-of-its-kind" preventative-care platform and is an XPRIZE Healthspan semi-finalist.

## What they offer

A broad catalog — **48 products across 19 need-categories**, organized into enumerable therapeutic families (all prescription items are subscription with ongoing monitoring; prices are "Starting at" floors — see `unverified_fields`):

- **Core longevity Rx (flagship family):** Metformin ("Starting at $25"/mo, billed $75 quarterly), Rapamycin (monitoring + bloodwork included), Acarbose, Methylene Blue, Low Dose Naltrexone (LDN), SGLT2 inhibitors (Brenzavvy®, Invokana®), Atorvastatin, Telmisartan, Tadalafil (Daily / As-Needed).
- **GLP-1 / weight management:** Injectable GLP-1 ("Starting at $139"), Microdosing GLP-1 ("$99"), Compounded Liraglutide, plus brand access-&-monitoring for Wegovy® (pill + injection) and Zepbound® ("$50 + cost of medication").
- **NAD+ support:** Injection, Nasal Spray, Patch (iontophoresis), Face Cream.
- **GSH (glutathione) support:** Injection, Nasal Spray, Patch.
- **Peptides:** Sermorelin (injection + nasal spray), PT-141 (injection + nasal spray), GHK-Cu Cream.
- **Biological-age testing & monitoring:** At-Home Methylation Saliva Test (TruMe, "$170"), Lab-Based Phenotypic Blood Test ("$75", at Quest), iollo Advanced Metabolic Test (600+ biomarkers, "$399"), Core Longevity Panel (40+ biomarkers), Online Phenotypic Calculator (FREE), Galleri multi-cancer early-detection test, glucose biosensors (Stelo/Nutrisense CGM).
- **Skin & hair:** Tretinoin, DMAE Firming Gel (AgelessRx exclusive), Powers Hair Solution v5.1 (minoxidil + dutasteride compound), NAD+ Face Cream.
- **Supplements & packs:** Infinite Longevity Support, Heart Health Pack (berberine + aged garlic), Glucose Control Supplement (inositol), Tran-Q Sleep, Trazodone, B12 / B12-MIC injections.
- **Women's Hormone Care:** clinician-guided, starts with a 1:1 consultation.

## How it works / model

Five-step journey: **1) Find your solution** (browse by treatment or by need, or book a paid Longevity Consultation) → **2) Complete online visit** (doctor-created intake; ID + photo + payment captured, only charged if approved) → **3) Medical review** (US-licensed clinician reviews within up to 5 business days; some states require a video consult) → **4) Delivered** (compounded/fulfilled by 503A FDA-registered pharmacy partners, free discreet shipping in 5–7 business days) → **5) Ongoing support** (auto-refills, provider messaging, periodic check-ins, dose adjustments; pause/cancel anytime). Revenue is recurring subscription on medications (often billed quarterly) plus one-time diagnostic tests; HSA/FSA eligible. A portion of profits funds longevity-research nonprofits (SENS, Lifespan.io, Fight Aging!, others).

## Positioning & audience

Targets U.S. adults across the lifespan ("whether you're 25 or 70") who want proactive, preventative, science-backed longevity care rather than reactive sick-care. Claimed edge: a research-first identity (XPRIZE Healthspan semi-finalist, in-house clinical studies — "5,200+ participants," "we read the clinical trials so you don't have to / gatekeeping is so traditional healthcare"), breadth ("30+ unique diagnostics and therapeutics"), affordability vs. IV/clinic alternatives (NAD+/glutathione "at a fraction of the cost of IV infusions"), and a credentialed medical team. Core message: "What would you do with *more* healthy years?" — healthspan over lifespan, 70% of aging within your control. Rapamycin and Metformin are the credibility-anchor molecules.

## Nav structure

```
- Treatments (by product family)
  - All Treatments — /treatments/
  - Longevity — /products-longevity/
  - GLP-1 Support — /semaglutide-glp-1s/
  - NAD+ Support — /all-nad-support/
  - GSH Support — /all-gsh-support/
  - BioAge Tests — /biological-age-test/
  - Health Monitoring — /health-monitoring/
- By Need (by condition)
  - General Longevity — /products-longevity/
  - Weight Management — /products-weight-management/
  - Energy & Fatigue — /products-energy-fatigue/
  - Chronic Pain & Arthritis — /products-pain-arthritis/
  - Diabetes Prevention — /products-diabetes-prevention/
  - Glucose Management — /glucose-management/
  - Heart Health — /heart-health/
  - Blood Pressure — /products-blood-pressure/
  - Cognitive Function — /products-cognitive-function/
  - Sleep — /sleep/
  - Autoimmune Support — /products-autoimmune-support/
  - Mood Support — /products-mood-support/
  - Aging Skin — /products-aging-skin/
  - Men's Aging — /products-mens-aging/
  - Women's Aging — /products-womens-aging/
- How We Work — /how-we-work/
- Learn
  - Longevity Science — /longevity-science/
  - Longevity Quiz / Wellness Assessment — /wellness-assessment/
  - Blog — /blog/
  - Testimonials — /testimonials/
  - About — /about/
  - Research — /research/
  - FAQ — /faq/
- Patient Portal / Sign In → customer.agelessrx.com
```
Footer adds: Product Science (per-molecule science pages: Metformin, LDN, NAD+, GSH, Wegovy®, Powers Hair, Tretinoin), Using HSA/FSA, AgelessRx Community, Careers, Patient Resources. Contact: 650-503-9990 · info@agelessrx.com · 2370 E Stadium Blvd #2049, Ann Arbor, MI 48104.

## Credibility & proof

- **Trustpilot:** 4.4/5 "Excellent" rating.
- **Press strip:** The New York Times, Forbes, Wall Street Journal, CNET, USA Today, Yahoo Finance.
- **XPRIZE Healthspan semi-finalist** — 1 of 40 global teams.
- **Self-reported efficacy:** "82.7% of patients reported one or more improvements by their first check-in" (n=7,084 surveyed customers, 1/21/24–4/8/24); "5,200+ participants completed clinical studies"; "30+ unique diagnostics and therapeutics."
- **Community:** "200k+ people" on the email/community list.
- **Medical team (named, on /about):** Anar Isman (Co-founder & CEO); Dr. Stefanie Morgan, PhD (VP Operations & Applied Science — Stanford/Harvard); Dr. Jenell Decker, MD (Medical Director, Board Certified Family Medicine); Dr. Terry Grossman, MD (Medical Advisor — noted anti-aging physician); Dr. Mirna Jadan, MD (Asst. Medical Director); Dr. Aaron Stecker, DO (Telehealth Physician).
- **Safety posture:** 503A certified / FDA-registered pharmacy partners, lab-tested for purity (calls out it was unaffected by the 2020 NDMA metformin recall, uses Tagi Pharma); heavy citation of peer-reviewed studies on each product page; HSA/FSA eligible.

## Visual & brand impression

Mature, well-funded, science-forward DTC brand — clearly design-led, not a template funnel. The palette is a confident **deep forest-green** (#023B37) for hero/footer bands and feature sections, set against clean **white** content, with a warm **amber** (#FFB54C) reserved for CTAs and a teal (#0B857D) for links. Typography pairs an editorial **serif** heading face (CheltenhamPro — a classic NYT-style serif) with a neutral sans body (AgelessSans), giving a credible "medical-journal-meets-wellness" tone. Imagery is aspirational-lifestyle (active older adults, families) interleaved with conceptual motifs (a chessboard for "aging is a puzzle," methylation/DNA graphics) and lab/product photography. Overall maturity is high; the brand reads trustworthy, clinical, and optimistic rather than hype-driven.

## Strategic read

AgelessRx is the **broad-catalog generalist** of the longevity-telehealth cohort: where peers anchor on one hero protocol (Healthspan→rapamycin, Hone→TRT), AgelessRx fields a 48-SKU pharmacy spanning nine therapeutic families plus a full biological-age testing layer, sold across two nav axes (by molecule and by condition) — closer to a longevity *pharmacy/marketplace* than a single-protocol clinic. Its differentiators are research credibility (XPRIZE, in-house studies, citation-heavy pages), an Ann Arbor (not SF/NY) base, and an explicit measure-then-treat loop (BioAge tests → therapies → re-test). The flip side of breadth is funnel complexity: pricing is fragmented across product pages with rotating coupon codes, and the true cost only resolves inside the portal — making cross-shopping and price transparency harder than single-product peers.

## Provenance

- **Pages:** homepage, `/treatments/`, `/how-we-work/`, `/about/`, `/metformin/`, `/semaglutide-glp-1s/`, `/all-nad-support/`, `/biological-age-test/` (8) — all Firecrawl (`fc.py`), `maxAge:0` + `location:US`, all formats + full-page screenshot each; `design_framework` read from `rawHtml` (`wp-content` → WordPress; branding.designSystem "bootstrap" ignored per playbook).
- **Verify:** 8/8 sourceURL-matched, all bodies md5-unique (clean); no geo/cache contamination this run.
- **Credits:** 9 (1 map + 8 scrapes, 1 credit each).
- **Couldn't get:** final per-SKU pricing (behind customer.agelessrx.com portal; pages show "Starting at" floors only), the ~40 individual product detail pages beyond Metformin, corporate facts (founding year, headcount, funding).
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-05-31 rawHtml, hint-to-verify) — filled `socials` (sameAs fb/x/ig/linkedin/youtube); JSON-LD `logo` was an OG share image (`agelessrx-social-share.jpg`) so kept the existing on-domain SVG logo; no legalName/`external`. Re-stamped 2.0→2.2.
- **Run profile:** +logos — 2.5 logos module added 2026-06-04 over the existing capture (cached homepage payload, no re-scrape); marks measured by `fc.py logos`, `transparent` judged on a checker tile. og omitted (declared og:image is a press logo). Re-stamped 2.2→2.5.
