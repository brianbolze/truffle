---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: gethealthspan.com
name: Healthspan
aliases: []
parent: []
owns: []
socials: { instagram: "https://www.instagram.com/healthspan", x: "https://www.twitter.com/healthspanmed", facebook: "https://www.facebook.com/healthspanmed" }   # linked from homepage; handles "healthspan"/"healthspanmed"
external: {}                            # JSON-LD is WebSite-only (no sameAs); no 3rd-party records declared on-site

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js app (assets under /_next/; this run rawHtml came back populated — framework read directly). A/B: VWO — per-SKU prices + which homepage modules render flicker run-to-run; the homepage markdown leads with repeated banner-text loops (mantra strip 'Pioneers in Longevity / HSA-FSA / Trusted by 12K…' ×~20 — noise, skip it). Catalog is clean and stable across index pages: /medications (~23 Rx + protocols), /supplements (6 OTC), /labs (6 priced panels), /programs (4 memberships). Map returns ~499 URLs but is ~70% /research/article/* essays — the real catalog is the four index pages, not the research firehose; many /treatments/* slugs are A/B or legacy variants (-old, -fb, -troche-a, -hero) not surfaced on the index grids. PRICING MODEL (key): two structures — (1) all-inclusive longevity protocols (rapamycin/oxytocin/methylene blue/SGLT2/acarbose/metformin/LDN/supplements): one '$X/mo' price, 'Everything included: labs, meds, dosing', cancel anytime → self-contained; (2) Membership + medication-separate for HRT/GLP-1/men's-TRT: Membership '$129/mo or $99/mo for 3 months', med 'billed separately' (GLP-1 via LillyDirect) → the index 'Starting at $X/mo' is the member-discounted MED price, not all-in. Program ('membership') floor shows 'Starting at $99/mo' on /programs; exact tier cost sits behind app.gethealthspan.com signup. Marketing pages also live on marketing.gethealthspan.com; community.* + careers.* + dev/development.* subdomains appear in the map — ignore for catalog. Product renders live on methodical-vitality-*.media.strapiapp.com ('*_Gallery_Card_540x540' = clean isolated bottle on white; '*_Image_Card' = lifestyle)."
key_pages:
  medications: /medications
  supplements: /supplements
  labs: /labs
  programs: /programs
  how_it_works: /how-it-works
  our_company: /our-company
  our_mission: /our-mission
  personalized_protocols: /personalized-protocols
  signup_app: https://app.gethealthspan.com/#/product/signup/
unverified_fields:
  - "Prices & homepage IA are a point-in-time snapshot, not fixed — VWO A/B tests shift per-SKU prices and which homepage modules render run-to-run (Topical Rapamycin-for-Hair showed $120/mo on the /medications index vs $140/mo on the rapamycin PDP cross-sell this run)."
  - "Membership tier cost — /programs and the PDPs show 'Starting at $99/mo' (and membership '$129/mo or $99/mo for 3 months'); the exact program/membership price by tier sits behind the app.gethealthspan.com signup flow, not captured."
  - "GLP-1 medication cost — billed separately via LillyDirect ('based on the prescription and pharmacy used'); the '$299/mo + membership' (Zepbound) is the shown floor, real all-in not on-site."
  - "Founding YEAR, HQ address, headcount, funding — not stated on captured pages. Origin anchors to a 2019 event (co-founder's wife's lymphoma relapse); support phone is a (650)/SF-Bay-Area number; © reads '2025 Healthspan'."

description: "A digital longevity clinic delivering rapamycin, metabolic, hormone, and GLP-1 protocols through telehealth clinicians, using 100+ biomarker lab testing and ongoing coaching to personalize and track each member's anti-aging plan."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg          # canonicalized to the wordmark (2.5) — the inline data-URI "Healthspan" SVG, extracted + committed
logos:
  wordmark: { src: assets/wordmark.svg, w: 140, h: 28 }                                                                  # high-contrast display serif "Healthspan"; viewBox 160x32
  logomark: { src: "https://www.google.com/s2/favicons?domain=gethealthspan.com&sz=256", px: 256, transparent: false }  # deconstructed-monogram mark; baked WHITE bg (hasAlpha:no, confirmed on a dark tile)
  og:       { src: "https://methodical-vitality-96814f361f.media.strapiapp.com/healthspan_metadata_image_e56b98d16c.jpg", w: 2400, h: 1260 }   # yellow wordmark on dark-teal gradient + "PERSONAL CARE FOR OPTIMAL HEALTH"
brand_colors: { primary: "#FEF38E", secondary: "#81B1E2" }   # STRAIN: pale-yellow signature accent + light-blue secondary on a black/white editorial base — see Visual read
fonts: [Suisse Intl, Soehne Mono]      # body sans + monospace labels; the wordmark/headlines add an (unnamed in payload) high-contrast display serif
color_scheme: light
design_framework: next.js              # rawHtml: /_next/ present (ignore branding.designSystem "custom", §5.4)
---

## Overview

Healthspan is a direct-to-consumer telehealth clinic built around the "longevity medicine" thesis — extending *healthspan* (quality years), not just lifespan. It pairs advanced lab testing (100+ biomarkers via Quest Diagnostics) with licensed-clinician oversight and PhD-level coaching to design and continuously optimize personalized anti-aging "protocols." It bills itself as "the world's first digital longevity clinic," with rapamycin as the flagship and a science/research-publishing posture as the wedge. It was founded by **Daniel Tawfik** (CEO, molecular-biology background) with co-founders **Aman Fahimullah** (CPO) and **Fazil Azhar** (CTO); the origin story traces to 2019, when Tawfik's wife, **Dr. Elana Miller**, relapsed with lymphoma and the couple found advanced mTOR/rapamycin longevity care "rarely available and cost a fortune" (one renowned longevity doctor's fees were "more than $120,000 per year") — Healthspan's stated mission is to make that care accessible. Care is membership/subscription-based; medications and labs ship to the patient's door (SF Bay Area company — (650) phone; © 2025 Healthspan).

## What they offer

Several distinct, enumerable lines. Two commercial structures coexist (per-SKU roster + verbatim footnotes in [`offerings.md`](offerings.md)):

- **Longevity protocols (all-inclusive subscriptions):** med + labs + dosing bundled into one self-contained monthly price, "Modify or cancel anytime." The Rapamycin Protocol **Starting at $64/mo** `[published]` (flagship; FDA-approved enteric-coated rapamycin / "Sirolimus" panel, compounded option available), Topical Rapamycin Skin **$115/mo** / Hair **$120/mo** `[published]`, Methylene Blue **$99/mo** `[published]`, Oxytocin nasal spray / troche **$135/mo** `[published]`, LDN **$40/mo** / LDN Troche **$99/mo** `[published]`, SGLT2 Protocol **$99/mo**, Acarbose **$25/mo**, Metformin **$27/mo** `[published]`.
- **GLP-1 / weight (Membership + medication-separate):** Zepbound w/ Ongoing Care **"Starting at $299/mo + membership"** `[partial]` (tirzepatide; med billed separately via **LillyDirect**), Wegovy Pen **$199/mo** / Wegovy Pill **$149/mo** (semaglutide), Foundayo Pill **$149/mo** (oral GLP-1) — all `[partial]`.
- **Hormone (HRT — Membership + medication-separate):** Men's TRT (Testosterone Cypionate injection **$85/mo**, Testosterone Gel **$85/mo**, Enclomiphene **$60/mo**) and Women's (Bi-Est 50/50 Cream **$64/mo**, Estradiol Patch **$112/mo**, Micronized Progesterone **$32/mo**, low-dose Testosterone Topical Cream **$64/mo**) — "accessed through Membership," med billed separately, `[partial]`.
- **Supplements (OTC):** Cellular Renewal Stack **$105/mo**, Mitophagy **$60/mo**, Autophagy Blend **$56/mo**, AMPK Blend **$56/mo**, Protein Powder **$55/mo**, Creatine + Electrolytes **$48/mo** — all `[published]`.
- **Labs (one-time):** Longevity Pro **$349** (100+ biomarkers, CLIA-certified), Longevity Starter **$40**, Heart Vitality / Female Hormone / Male Hormone panels **$120** each, Rapamycin Bioavailability **$25** — all `[published]`.
- **Programs (memberships):** Longevity Optimization, GLP-1 Longevity Care, Men's Hormone Health, Women's Hormone Health — each **"Starting at $99/mo"** `[partial]`; all bundle BioAge+, Coaching, and Personalized Protocols (exact tier cost behind app signup).

Labs are the data wedge — most journeys start or recur with a panel; retesting every 3–6 months is recommended. (Prices are a snapshot — see `unverified_fields`.)

## How it works / model

A 5-step membership journey: **1) Assessment** (a short online intake — "No clipboards or waiting rooms," medical history) → **2) Connect** (a dedicated longevity care team reviews the case) → **3) Protocol** (clinician designs a personalized plan of labs + medications) → **4) Delivered** (protocol ships to the door) → **5) Optimize** (ongoing tracking in the **MySpan** app, performance coaching, and periodic re-testing to adjust). The front-door consult is **async** (online assessment + team review, no required live video visit). Revenue is recurring: all-inclusive protocol subscriptions for longevity meds, and a Healthspan **Membership ("$129/month or $99/month for 3 months," 20% member discount on meds)** plus separately-billed medication for HRT/GLP-1. HSA/FSA eligible; fulfillment is mail-order (NABP-accredited pharmacies, USP-tested); lab draws happen at Quest Diagnostics locations.

## Positioning & audience

Targets health-conscious U.S. consumers — the "optimization"/longevity-curious segment — who want a clinical, evidence-graded alternative to both fragmented primary care and lighter wellness telehealth. Claimed edge: a research-first identity ("Follow the science," in-house review of clinical literature, a weekly "Longevity Blueprint" newsletter, a "Beyond Healthspan" podcast), comprehensiveness ("one place for diagnostics, treatments, and care"), and depth of data ("Labs 3X More Comprehensive," "70+ Biomarkers Tracked," "9 Biological Systems Reviewed"). Rapamycin is the hero molecule and the brand's credibility anchor; the founding narrative (accessibility vs. a $120k/yr longevity doctor) is the positioning spine.

## Nav structure

```
- Treatments
  - All Treatments — /treatments
  - Medications — /medications
  - Programs — /programs
  - Labs — /labs
  - Supplements — /supplements
- Programs
  - Longevity Optimization — /programs/longevity-optimization-core
  - GLP-1 Longevity Care — /programs/glp1-care
  - Women's Health Program — /programs/womens-health
  - Men's Hormone Health — /programs/mens-hormone-health
  - (All Programs Include) BioAge+ — /bioage · Coaching — /coaching · Personalized Protocols — /personalized-protocols
- BioAge+ — /bioage
- About
  - Our Company — /our-company
  - Our Mission — /our-mission
  - How it Works — /how-it-works
  - (Read our latest research → /research/article/* features)
- Research — /research  (Science: Senescence /science/senescence · Metabolism · Hormone · Energy)
- Log in / Get Started → app.gethealthspan.com
```
Footer adds Top Treatments (Methylene Blue, Rapamycin, Oxytocin), Community (community.gethealthspan.com), Careers (careers.gethealthspan.com), FAQs, Contact, phone (650) 563-8696.

## Credibility & proof

Self-reported (record, don't endorse): **"4.9/5 Trustpilot"**, **"Trusted by 12K Patients"** / "more than 12,000 Healthspan patients across the country," **"1st digital longevity clinic"** / "We pioneered modern longevity care," **"20+ avg. yrs of experience"** and **"150+ published works"** from the MD/PhD clinical + research teams, **"Labs 3X More Comprehensive,"** **"70+ Biomarkers Tracked,"** **"9 Biological Systems Reviewed."** Named **founding team** (Daniel Tawfik, Aman Fahimullah, Fazil Azhar) and a named **medical advisory board** (Dr. Rick Cohen MD — Duke/Hahnemann, A4M; Dr. Elana Miller — Harvard/USC, UCLA residency; Dr. Scott Sanderson — Anti-Aging + Emergency Medicine, JABSOM faculty). CLIA-certified labs; NABP-accredited pharmacies; USP-tested batches; HSA/FSA eligibility; a "Featured In" press strip with pull-quotes positioning rapamycin as "the current best-in-class for a longevity drug"; named on-site testimonials and an FAQ.

## Visual & brand impression

Premium, editorial, science-forward — reads as a well-funded, design-led brand, not a template DTC funnel. The full-page screenshot alternates **black** hero/feature bands (cinematic medical-lab imagery + shader graphics) with clean **white** product sections, punctuated by the signature **pale-yellow (#FEF38E)** accent and a **light-blue (#81B1E2)** secondary used sparingly. Typography is a deliberate three-way system: a **high-contrast display serif** for the "Healthspan" wordmark and headlines (a giant serif wordmark anchors the page foot and the og cover — yellow-on-dark-teal), a clean **sans (Suisse Intl)** for body, and **Soehne Mono** for parenthetical labels ("(Follow the science)", "(Curiosity)") — a clinical, research-journal affectation. Product renders are consistent and catalog-grade: each SKU is a clean isolated amber pharmacy bottle (or grey/lavender HRT bottle) on white, with a category chip (SENESCENCE / METABOLIC / ENERGY / HORMONES) and the Healthspan wordmark — see the six captured renders in `captures/2026-06-04/images/`. The live page still carries VWO A/B instrumentation and looping banner text.

## Provenance

- **Pages:** homepage, `/medications`, `/supplements`, `/labs`, `/programs`, `/how-it-works`, `/our-company`, and 5 flagship PDPs (`/treatments/rapamycin`, `/zepbound`, `/testosterone-topical-cream`, `/oxytocin`, `/methylene-blue-prescription`) (12) — all Firecrawl (`fc.py`), `maxAge:0` + `location:US`, all formats + screenshot each; the four index pages + flagship PDPs ran the rich `--homepage`/`--images` pass. `design_framework` read from `rawHtml` (`/_next/`). Map sampled ~499 URLs (≈70% `/research/article/*` — skipped).
- **Verify:** 12/12 sourceURL-matched, all bodies md5-unique (clean); no geo/cache contamination this run.
- **Credits:** 13 (1 map + 1 homepage + 6 index/signal + 5 PDPs).
- **Couldn't get:** exact program/membership tier price (behind app.gethealthspan.com signup), GLP-1 medication cost (billed separately via LillyDirect), corporate facts beyond names (founding year, HQ address, funding — not on the marketing site).
- **Run profile:** guided — modules `+offerings` (per-SKU roster), `+telehealth` (cohort pack), `+logos` (wordmark/logomark/og), `+hero images` (6 flagship product renders → `captures/2026-06-04/images/`); refresh forced over a warm (2026-05-30) capture to gather the modules.
- **Structured layer (2.5):** `fc.py signals` — JSON-LD is WebSite-only (no `sameAs`/`logo`); `socials` (instagram/x/facebook) recovered from homepage links, verified Healthspan-branded handles; `logo_url` upgraded to the extracted inline-SVG wordmark; nav recovered from the `<header>` mega-nav, validated vs the screenshot.
