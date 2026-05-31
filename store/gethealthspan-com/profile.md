---
schema_version: 1

# Identity
domain: gethealthspan.com
name: Healthspan
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Next.js app (assets under /_next/; rawHtml came back empty this run — framework read off asset paths). Heavy VWO A/B instrumentation: the homepage markdown leads with a large inline VWO campaign blob (noise — skip it), and per-SKU prices + homepage modules flicker run-to-run. Per-treatment pricing is on the homepage product carousel and each /treatments/<slug> page; program ('membership') pricing shows only a 'Starting at $99/mo' floor on /programs — real cost sits behind the app.gethealthspan.com signup. Map returns ~493 URLs but is ~70% /research/article/* essays (314) — the real catalog is /treatments (41), /programs (12), /labs (7); pull those, not the research firehose. Marketing pages live on a separate marketing.gethealthspan.com subdomain; community.* and dev0*.development.* also appear in the map — ignore."
key_pages:
  how_it_works: /how-it-works
  programs: /programs
  treatments: /treatments
  labs: /labs
  research: /research
  our_mission: /our-mission
  signup_app: https://app.gethealthspan.com/#/product/signup/
unverified_fields:
  - "Pricing & homepage IA are a point-in-time snapshot — the site runs VWO A/B tests; per-SKU prices and homepage modules shift run-to-run (e.g. prior captures saw Rapamycin $64↔$65)."
  - "Program ('membership') pricing — /programs shows only a 'Starting at $99/mo' floor for all four programs; the real membership cost is behind the app signup flow, not captured."
  - "Founding year, HQ location, headcount, funding — not on the captured marketing pages (support phone is a 650/SF-Bay-Area number; © reads '2025 Healthspan')."
  - "design_framework inferred from /_next/ asset paths; rawHtml was empty this capture."

description: "A digital longevity clinic delivering rapamycin, metabolic, hormone, and GLP-1 protocols through telehealth clinicians, using 100+ biomarker lab testing and ongoing coaching to personalize and track each member's anti-aging plan."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url:                              # STRAIN: wordmark only — branding.images.logo is an inline data-URI SVG ("healthspan" in black), no favicon/og fallback present
brand_colors: { primary: "#FEF38E", secondary: "#81B1E2" }   # STRAIN: pale-yellow + light-blue accents on a black/white editorial base — see Visual read
fonts: [Suisse Intl, Soehne Mono]
color_scheme: light
design_framework: next.js
---

## Overview

Healthspan is a direct-to-consumer telehealth clinic built around the "longevity medicine" thesis — extending *healthspan* (quality years), not just lifespan. It pairs advanced lab testing (100+ biomarkers via Quest Diagnostics) with licensed-clinician oversight and PhD-level coaching to design and continuously optimize personalized anti-aging "protocols." It positions itself as "the world's first digital longevity clinic," with rapamycin as the flagship and a science/research-publishing posture as the wedge. Care is membership-based; medications and labs ship to the patient's door.

## What they offer

Several distinct, enumerable lines, all subscription:

- **Longevity medications & protocols** (flagship) — The Rapamycin Protocol ($64/mo, "Most Effective"), Topical Rapamycin for skin ($115/mo) and hair ($120/mo), Methylene Blue ($99/mo), Oxytocin / Oxytocin Troche ($135/mo), LDN ($40/mo).
- **Metabolic** — Acarbose ($25/mo), Metformin ($27/mo), SGLT2 Metabolic Protocol ($99/mo).
- **GLP-1 / weight** — Zepbound with ongoing care ($299/mo), Wegovy Pill ($149/mo), semaglutide.
- **Hormone** — Men's (Testosterone cream $64/mo, Enclomiphene $60/mo) and Women's (Bi-Est cream $64/mo, Micronized Progesterone $32/mo).
- **Programs (memberships)** — Longevity Optimization, GLP-1 Longevity Care, Men's Hormone Health, Women's Hormone Health (each "Starting at $99/mo"); all bundle BioAge+, Coaching, and Personalized Protocols.
- **Labs** — Longevity Pro ($349 one-time, 80+ biomarkers, CLIA-certified), Longevity Starter ($40), plus Heart/Hormone/Rapamycin-bioavailability panels ($25–$120).

Labs are the data wedge — most journeys start or recur with a panel; retesting every 3–6 months is recommended. (Prices are a snapshot — see `unverified_fields`.)

## How it works / model

A 5-step membership journey: **1) Assessment** (short online intake, medical history) → **2) Connect** (a dedicated longevity care team reviews the case) → **3) Protocol** (clinician designs a personalized plan of labs + medications) → **4) Delivered** (protocol ships to the door) → **5) Optimize** (ongoing tracking in the **MySpan** app, performance coaching, and periodic re-testing to adjust). Revenue is recurring membership/subscription plus per-treatment and lab fees; HSA/FSA eligible. Fulfillment is mail-order; lab draws happen at Quest Diagnostics locations.

## Positioning & audience

Targets health-conscious U.S. consumers — the "optimization"/longevity-curious segment — who want a clinical, evidence-graded alternative to both fragmented primary care and lighter wellness telehealth. Claimed edge: a research-first identity ("Follow the science," in-house review of clinical literature, a weekly "Longevity Blueprint" newsletter), comprehensiveness ("one place for diagnostics, treatments, and care"), and depth of data ("labs 3X more comprehensive," 70+ biomarkers tracked, 9 biological systems reviewed). Rapamycin is the hero molecule and the brand's credibility anchor.

## Nav structure

```
- Treatments
  - All Treatments — /treatments
  - Medications — /medications
  - Supplements — /supplements
  - Labs — /labs
  - Personalized Protocols — /personalized-protocols
- Programs
  - Longevity Optimization — /programs/longevity-optimization-core (hero: /program/longevity)
  - GLP-1 Longevity Care — /programs/glp1-care
  - Women's Health — /programs/womens-health
  - Men's Hormone Health — /programs/mens-hormone-health
  - (All programs include) BioAge+ — /bioage · Coaching — /coaching · Personalized Protocols — /personalized-protocols
- BioAge+ — /bioage
- About
  - Our Company — /our-company
  - Our Mission — /our-mission
  - How It Works — /how-it-works
- Research — /research  (Science: Senescence /science/senescence · Metabolism · Energy)
- Log in / Get Started → app.gethealthspan.com
```
Footer adds Community (community.gethealthspan.com), FAQs, Contact, phone (650) 563-8696.

## Credibility & proof

4.9/5 Trustpilot rating; "Trusted by 12,000+ patients"; "1st digital longevity clinic"; "20+ avg yrs of experience" and "150+ published works" from MD/PhD clinical + research teams; CLIA-certified labs; physician-reviewed results; "Featured In" press strip plus pull-quotes positioning rapamycin as "best-in-class for a longevity drug." On-site testimonials (named patients), an FAQ, and HSA/FSA eligibility reinforce trust.

## Visual & brand impression

Premium, editorial, science-forward. The full-page screenshot reads as predominantly **black** hero and feature bands (with cinematic medical/lab imagery and shader graphics) interleaved with clean **white** content sections — punctuated by a pale-yellow (#FEF38E) accent and a light-blue (#81B1E2) secondary used sparingly for highlights and links. Typography pairs a clean sans (Suisse Intl) with a monospace (Soehne Mono) used for labels/parentheticals ("(Follow the science)", "(Curiosity)") — a deliberately clinical, research-journal affectation. A giant "Healthspan" wordmark anchors the page foot. Overall maturity is high: this is a well-funded, design-led brand, not a template DTC funnel — though the live page carries A/B-test instrumentation and animated module flicker.

## Provenance

Captured 2026-05-30 via Firecrawl (`fc.py`), `maxAge:0` + `location:US`. Pages analyzed: homepage (all formats + screenshot), `/how-it-works`, `/programs`, `/program/longevity`, `/treatments/rapamycin`, `/labs`, `/our-mission` (markdown + links + screenshot each). Verify passed — 7/7 sourceURL-matched, all bodies md5-unique; no geo/cache contamination this run. `rawHtml` returned empty (framework inferred from `/_next/` asset paths). Map sampled ~493 URLs (≈314 of them `/research/article/*` essays — skipped). Not captured: program-membership pricing (behind app signup), per-treatment detail pages beyond rapamycin, corporate/funding facts (not on marketing site).
