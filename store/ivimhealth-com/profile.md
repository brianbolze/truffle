---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: ivimhealth.com
name: Ivím Health
aliases: [Ivim Health]
parent: []
owns: []
socials:
  instagram: https://instagram.com/ivimhealth_
  facebook: https://www.facebook.com/ivimhealth
  tiktok: https://www.tiktok.com/@ivimhealth
  youtube: https://youtube.com/@ivimhealth
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress + WooCommerce + Elementor marketing host (www); supplements on a SEPARATE Shopify storefront (shop.ivimhealth.com — `products.json?limit=250` returns the full 25-SKU catalog + verbatim prices, free roster backbone). Support on Zendesk (ivim.zendesk.com). No JSON-LD on homepage; socials live only in rawHtml footer, not the markdown — grep rawHtml. Rx pricing is PUBLIC on /glp1-pricing/ + program pages, but branded-GLP-1, oral-GLP-1, microdosing, and injectable (NAD+/B12/Lipotropic/Sermorelin) prices sit on their own quiz-gated PDPs (not captured). ConvertFlow popups + a sitewide compounded-GLP-1 FDA disclaimer on every page. Provider-title labels are inconsistent across pages (Taylor Kantor shown as both 'Chief Innovation Officer' and 'Chief Medical Officer')."
key_pages:
  weight_loss: /glp1idwt/
  glp1_pricing: /glp1-pricing/
  membership: /why-membership/
  women_hormone: /women-hormone-optimization/
  services: /our-services/
  about: /about-us/
  providers: /providers/
  shop: https://shop.ivimhealth.com/
unverified_fields:
  - "Branded GLP-1 (Wegovy/Ozempic/Mounjaro/Zepbound/Saxenda), oral GLP-1 (Wegovy Pill, Foundayo Pill), microdosing, compounded liraglutide, and injectable NAD+/B12/Lipotropic/Sermorelin prices — own PDPs / quiz-gated, not captured this run."
  - "Prices/IA are a point-in-time snapshot, not fixed — Rx pricing carries 'subject to change' footnotes and promo framing ('first month of membership on us'); membership shown as both $75/mo and $74.99/mo across pages."
  - "Men's Hormone Health and Peptide therapies are marketed 'coming soon' (waitlist) — not yet purchasable."
  - "Provider headcount stated as '~100' (homepage), '92 & counting' (/glp1idwt/), '~100' (homepage providers section) — point-in-time and self-reported."

# Description — what they do + how + focus
description: "Delivers GLP-1 weight-loss, women's hormone therapy, and a physician-formulated supplement line to U.S. consumers through licensed-clinician telehealth on a ~$75/mo membership, built around individualized, ongoing physician care with peer-reviewed published outcomes."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against screenshot
logo_url: https://media-s3-cdn.ivimhealth.com/assets/images/logos/ivim-black.svg
logos:
  wordmark: { src: "https://media-s3-cdn.ivimhealth.com/assets/images/logos/ivim-black.svg", w: 128, h: 22 }
  logomark: { src: "https://www.ivimhealth.com/wp-content/uploads/2022/10/cropped-ivim-new-v@2x-180x180.png", px: 180, transparent: true }
brand_colors: { primary: "#5A6859", secondary: "#373946", accent: "#DCE6CB" }   # sage-green primary (vision-confirmed across icons/section bands); accent = pale green; secondary = dark slate
fonts: [Poppins, Playfair Display, Noto Sans]   # Poppins body; Playfair Display the serif-italic display headers; Noto Sans headings (branding payload)
color_scheme: light
design_framework: wordpress   # rawHtml: wp-content×51, woocommerce×30, elementor×14 (storefront separately Shopify)
---

## Overview

Ivím Health is a DTC telehealth brand for cardiometabolic and metabolic-wellness care, anchored on GLP-1 weight loss and built around a recurring physician relationship rather than a one-time prescription. A patient completes an online quiz, meets a licensed provider by video, chat, or "e-visit," and — if qualified — receives compounded or branded medication shipped to their door under an ongoing ~$75/month membership. The pitch is "not just a prescription": unlimited provider visits, weekly dose check-ins through an app, functional health coaching, and a community layer wrapped around the medication.

It was founded in 2021 by cardiac surgeon **Dr. Taylor Kantor**, his brother **Anthony Kantor** (CEO), and Anthony's wife **Kelly** — to "reimagine care for cardiometabolic conditions." The company leans hard on a clinical/evidence identity: it has published two peer-reviewed retrospective studies in *Obesity Pillars* (semaglutide, Sept 2025; tirzepatide, March 2026) and a model paper in PMC ("Individualized virtual integrative medicine (IVIM)"). Beyond weight loss it runs a live Women's Hormone Optimization program, a 20-SKU physician-formulated supplement store, and markets injectable energy/metabolism and sleep therapies; **Men's Hormone Health and physician-prescribed peptide therapies are flagged "coming soon."**

## What they offer

Multi-product, all subscription/membership-gated. Bold-led families with price-visibility tokens (per-SKU depth in `offerings.md`):

- **Weight loss — GLP-1 ID (anchor):** compounded **semaglutide** ("$499 (4-month)") and **tirzepatide** ("$900 (4-month)") on individualized weekly dosing; branded Wegovy/Ozempic/Mounjaro/Zepbound/Saxenda and oral pills (Wegovy Pill, Foundayo Pill) via a "traditional GLP-1 program"; plus a **microdosing** track. Med floor "starting at $75/mo" (semaglutide) / "$133/mo" (tirzepatide) **+ $74.99/mo program fee**, "$75/mo required thereafter" `[partial]`
- **Women's Hormone Optimization:** estradiol/estriol + progesterone (oral capsule, transdermal patch) — **"$199/month* (4 Month Commitment)"**, all-inclusive of meds + membership; DHEA / PT-141 / apomorphine-oxytocin sexual-wellness **add-ons billed extra** `[published]`
- **Energy & Metabolism (injectables):** NAD+, B12, Lipotropic — provider-prescribed `[on-request]`
- **Sleep & Stress:** Sermorelin (peptide), plus supplement options (Magnesium+, Glycine) `[on-request]`
- **Supplements & wellness (Shopify storefront):** ~20 physician-formulated SKUs — multivitamin, NMN, collagen, creatine, protein, electrolytes, Cu copper-peptide hair/skin — **"$30.00"–"$105.00"**, 20% off for members `[published]`
- **Men's Hormone Health:** marketed **"coming soon"** `[on-request]`
- **Peptide therapies:** energy/sleep/body-composition/immune/longevity peptides — **waitlist, "coming soon"** `[on-request]`

Labs (at-home hormone kits) are optional, not a required first step. The clinical wedge is the *care model* — "12+ provider interactions per patient over 1 year" — not the molecule.

## How it works / model

Quiz-led, membership-anchored telehealth. Journey (from /our-services/ + /glp1idwt/): **(1)** register + complete an interest-based quiz (weight loss / hormone / etc.); **(2)** sign up for membership, then schedule a telehealth **video visit or faster "e-visit"** — or, for those who qualify, Ivím submits a **prior authorization** so insurance covers the med at the patient's pharmacy of choice; **(3)** provider reviews, prescribes, routes the script to an **independent licensed compounding pharmacy** (cash/"accessibility programs" route, ships 7–14 days) or the patient's insurance pharmacy; **(4)** ongoing weekly app check-ins, unlimited visits, dose titration.

Money: recurring **membership ($75/mo, first month free)** is the spine; **medication is billed separately** by plan length (1/2/4/6-month commitments) or as a per-SKU storefront purchase; supplements are one-time/subscription Shopify orders with a 20% member discount. **HSA/FSA eligible**; Klarna financing offered. Compounded GLP-1 purchases are non-cancellable once the program starts (meds shipped for the full selected term).

## Positioning & audience

All-genders today, with weight-loss as the gender-neutral front door and **Women's Hormone Optimization** the live gendered line (Men's "coming soon"). Positions explicitly against "standard telehealth" ("a prescription and a portal") and traditional episodic care — its claimed edge is **continuity + individualization + published outcomes**: in-house W2 providers ("100% employed by us"), a named medical team, and peer-reviewed data rather than marketing claims. Premium-but-accessible wellness tone; B2B2C extension via the **"Ivím at Work"** employer program.

## Nav structure

```
- Your Goals
  - Weight Loss
    - By Program: GLP-1 Compounded — /glp1idwt/ · Microdosing — /microdosing/
    - By Medication: Wegovy Pill — /wegovypill/ · Foundayo Pill — /foundayopill/ · Zepbound — /zepbound/ ·
      Mounjaro — /mounjaro/ · Ozempic — /ozempic/ · Wegovy — /wegovy/ · Saxenda — /saxenda/ ·
      Liraglutide — /compounded-liraglutide/
  - Hormone Health
    - Women's Hormone Optimization — /women-hormone-optimization/
  - Energy & Metabolism: NAD+ — /nad/ · B12 — /b12/ · Lipotropic — /lipotropic/ ·
    Multi-V · Vitamin D3+K2 · Greens+ · Berberine · Fiber  (→ shop.ivimhealth.com)
  - Sleep & Stress: Sermorelin — /sermorelin/ · Magnesium+ · Glycine  (→ shop)
  - Body Composition: Protein Powder · Creatine · Amino+  (→ shop)
  - Immune & Repair: Colostrum Complex · Akkermansia+ · Electrolyte Blend · Hepatic  (→ shop)
  - Longevity & Skin: Collagen+ · Krill · Renu (NMN) · Cu Hair Spray · Cu Skin Cream  (→ shop)
- Membership
  - Why Membership — /why-membership/
  - Corporate Program (Ivím at Work) — /ivim-at-work/
- Resource Center
  - Blog — /blog/ · Press — /news/
- About Us
  - Our Mission — /about-us/ · Our Research — /our-research/ · Our Providers — /providers/
- Footer adds: Our Services — /our-services/ · FAQs/Contact (Zendesk) · Klarna FAQs · HIPAA Notice
```

## Credibility & proof

- **Scale (self-reported):** "470K+ Patients served"; "~100" / "92 & counting" board-certified providers, "100% employed by us."
- **Published research:** two peer-reviewed retrospective observational studies in *Obesity Pillars* — 1,131 patients (Sept 2025, semaglutide) and 1,166 patients (March 2026, tirzepatide); a model paper in PMC ("IVIM: A clinical model for enhanced GLP-1 therapeutic outcomes," PMC12272120). Outcomes cited verbatim: **"27% Average total body weight loss with tirzepatide," "22%… with semaglutide," "99%+ of Ivím patients achieved… 5%+ total body weight loss"** — all flagged not-RCT, individual-results-vary.
- **Press logos:** The New York Times, Men's Health, TIME, Forbes, CNN, Esquire, GQ, goop.
- **Named medical team:** Dr. Taylor Kantor MD (co-founder; titled both "Chief Innovation Officer" and "Chief Medical Officer" across pages), Dr. Jessica Duncan MD DABOM DABA (CMO / Medical Director), Andrew Schrotenboer DO, + NPs (Melissa Raymond, Courtney Goode, Ciji Boothe, Amy Padilla, Solange Loseille, Stacey Boucher, Elizabeth Neudecker, Courtney Floyd).
- **Founder lore (verbatim):** "Turned down a nine-figure acquisition because the buyer didn't share the vision."
- **Compliance posture:** prominent sitewide compounded-GLP-1 FDA disclaimer; "Medications are prepared by independent, licensed compounding pharmacies."

## Visual & brand impression

Clean, editorial premium-wellness. **Sage-green (#5A6859) + cream/pale-green (#DCE6CB)** palette over white, with deep-green section bands and warm, real photography (patients, providers, founders). Serif-italic display headers (Playfair Display — "This is what care is supposed to feel like," "Peptide therapies are coming") set against Poppins body — a calm, clinical-yet-human tone, not the loud neon of mass-market GLP-1 brands. Mark is a minimalist green bracketed-**[V]** logomark + lowercase "ivím" wordmark. Reads more "modern integrative clinic" than "supplement startup."

## Strategic read

The differentiator is deliberately **the care model, not the drug** — "the same medications are prescribed everywhere; what's different is how care is delivered around them." That, plus self-published peer-reviewed outcomes and in-house W2 clinicians, is a credibility moat aimed squarely at the "is compounded GLP-1 legit?" objection. Structurally it's a weight-loss-anchored brand **expanding outward** (women's HRT live; men's hormones + peptides on the runway) on a hybrid stack: WordPress/WooCommerce for the Rx front door, Shopify for the cash supplement catalog, prior-auth rails for insurance-covered branded GLP-1. Pharmacy is **third-party** (independent compounders) — no captive/owned pharmacy claimed, a contrast to vertically-integrated peers.

## Provenance

- **Pages:** homepage, /glp1idwt/ (weight-loss anchor), /glp1-pricing/, /why-membership/, /women-hormone-optimization/, /our-services/ (how-it-works), /about-us/, /providers/ — 8 pages via Firecrawl (markdown + screenshots), plus `shop.ivimhealth.com/products.json` for the supplement catalog. Map: 73 URLs (WordPress, blog/safety-info heavy).
- **Verify:** all sourceURLs matched, all 8 bodies md5-unique, no junk soft-404s.
- **Credits:** 10 (1 map + 1 homepage + 7 key pages); products.json fetched free.
- **Couldn't get:** branded/oral/microdosing GLP-1 + injectable (NAD+/B12/Lipotropic/Sermorelin) prices (own quiz-gated PDPs, not scraped); Men's hormone + peptide programs (pre-launch waitlists).
- **Run profile:** Express invocation — +offerings.md (per-SKU roster), +telehealth.md (cohort pack), +logos (2.5 module).
