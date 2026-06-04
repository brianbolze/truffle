---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: henrymeds.com
name: Henry Meds
aliases: ["Henry", "Adonis Health Inc."]   # footer: "Adonis Health Inc.™ (DBA: Henry Meds) • (DBA: Henry™)"
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/gethenrymeds/
  facebook: https://www.facebook.com/TryHenryMeds
  linkedin: https://www.linkedin.com/company/henry-meds/
external:
  trustpilot: https://www.trustpilot.com/review/henrymeds.com   # review record; rating in Credibility

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Framer site (rawHtml: 5,524 'framer' hits, data-framer, events.framer; branding.designSystem says 'unknown' — ignore per §5.4). All imagery + logos on framerusercontent.com CDN (content-hashed, hostable). No JSON-LD on homepage. Map clean — 39 URLs, no subdomain swamp; treatment slugs under /treatments/<category>/<sku>, marketing LPs under /landing/* (funnel — skip). No dedicated pricing page: each treatment PDP states its price in a bottom-of-page FAQ ('How much does X cost'). GLP-1 family floor '$179/month' is stated on the category hub + every GLP-1 molecule PDP EXCEPT the /semaglutide PDP, whose markdown carries no price. App at app.henrymeds.com; onboarding at onboard.henrymeds.com."
key_pages:
  how_it_works: /how-it-works
  values: /values
  faq: /faq
  weight_glp1: /treatments/weight-management/glp-1-weight-management
  hrt: /treatments/hrt
  trt: /treatments/trt
  ed_oral: /treatments/erectile-dysfunction/ed-oral
unverified_fields:
  - "Exact per-dose/per-plan prices are set in the intake flow (not submitted) — captured prices are page-stated 'starting at' floors or flat monthly figures from PDP FAQs."
  - "/semaglutide (injectable) PDP states no price in its captured markdown; the GLP-1 family floor ($179/month) is stated on the category hub and sibling GLP-1 PDPs."
  - "State availability — site says 'one of the states we support' but does not enumerate a list; KYZATREX oral TRT noted 'not available in California.'"

description: "Delivers compounded and FDA-approved weight-loss, hormone, and sexual-health treatments to U.S. adults through licensed telehealth providers, on flat monthly cash-pay plans that bundle provider visits, medication, supplies, and shipping."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against screenshots
logo_url: https://framerusercontent.com/images/X8gJWeCJg9RLJiX3grch93h22A.png   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: "https://framerusercontent.com/images/X8gJWeCJg9RLJiX3grch93h22A.png", w: 1868, h: 766 }   # green script "Henry", transparent
  logomark: { src: "https://framerusercontent.com/images/XNjvKiHQNtUsA7fe8Q6xZ7BQbY.png", px: 360, transparent: false }   # cream "H" on a BAKED dark-green square (apple-touch-icon)
  og:       { src: "https://framerusercontent.com/images/IKj7vJsVwoMUvKCMszjsaFHfjBo.png", w: 1200, h: 630 }   # "Henry" + tagline + lifestyle photo
brand_colors: { primary: "#113D36", accent: "#2B5745" }   # STRAIN: deep green (wordmark) + brighter green (logomark/og bg); branding 'primary' #0000EE is a default link blue, ignored
fonts: [Avenir, Poltawski Nowy]   # Avenir (Heavy/Book/Medium) body+UI; Poltawski Nowy serif display headings. branding ranked generic "sans-serif" first.
color_scheme: light
design_framework: framer   # rawHtml: data-framer, events.framer, framerusercontent
---

## Overview

Henry Meds (legal entity Adonis Health Inc., also branded "Henry") is a DTC telehealth service selling prescription treatment programs across four condition lines: weight management, women's hormone therapy (HRT), testosterone therapy (TRT), and erectile dysfunction. The model is insurance-free: a patient completes a short medical intake, meets (or is reviewed by) a licensed provider, and — if prescribed — gets medication mailed, all wrapped in one flat monthly fee that includes the visit, medication, supplies, and ongoing care. Medications are a mix of **compounded** (503A/503B) and **FDA-approved** drugs. The site positions on transparency and affordability ("up-front pricing for all parts of the healthcare process") for "average Americans."

## What they offer

Four condition lines, all flat-monthly subscription, cash-pay (bold lead-in, verbatim price + visibility token; per-SKU depth in `offerings.md`):

- **Weight management — GLP-1:** compounded semaglutide & tirzepatide (injectable + oral, plus lower-dose "microdose" and liraglutide) — **"starts at $179/month"** (all-inclusive, varies by dose/plan) `[published]`
- **Weight management — Phentermine:** compounded phentermine — **"The total monthly price for Phentermine is $149"** `[published]`
- **Women's HRT:** compounded + FDA-approved estrogen/progesterone/testosterone in cream, vaginal cream, patch, tablet — **"$149/month"** `[published]`
- **Testosterone therapy (TRT):** compounded testosterone (injectable) + KYZATREX™ oral (FDA-brand) — **"Starting at $129 per Month ($179 for KYZATREX™ oral … not available in California)"**; labs + aromatase inhibitor (if appropriate) included `[published]`
- **Erectile dysfunction — oral:** oral ODT pills (molecule not named on page) — **"three month supply for $50 each month ($150 total)"** `[published]`
- **Erectile dysfunction — injectable (ICP):** Trimix/Bimix + alprostadil/papaverine/phentolamine intracavernosal — **"Starting as low as $149/mo"** `[published]`

Every price is all-in (provider visit + medication + supplies + shipping + ongoing care); there is no separate membership fee.

## How it works / model

Three steps, stated identically across pages: **(1) Medical Forms** — share medical details, "<5 minutes"; **(2) Meet with a Healthcare Provider** — "schedule a provider visit face-to-face with a video call, or depending on your home state, choose an independent provider review without a video call" (i.e. sync video by default, **async** where state law allows); **(3) Receive Medication** — if prescribed, mailed "within 8–10 business days" (longer in California due to compound testing). Revenue is a flat **monthly subscription** per condition line; "no long-term contracts" but multi-month plans exist for some treatments (early cancellation may owe the balance). No insurance accepted or billed.

## Positioning & audience

A general-population (all-genders) DTC telehealth brand spanning men's and women's needs — title: "Henry | Personalized Weight Loss, Hormone & Sexual Health Care." Competes with the Hims/Hers/Ro tier on price transparency and an "affordable for average Americans" message. Stated values: **Transparent** (up-front pricing), **Proven** ("we don't hide behind … 'science-backed' … to sell dubious supplements"; only long-history medications), **Affordable**.

## Nav structure

```
- Weight Management — /treatments/weight-management/glp-1-weight-management  (flyout)
  - GLP-1 Weight Management — /treatments/weight-management/glp-1-weight-management
  - Phentermine Weight Management — /treatments/weight-management/phentermine
  - (GLP-1 molecule pages: /semaglutide, /semaglutide-oral, /tirzepatide-tablets,
     /liraglutide, /microdose, /microdose-oral)
- Women's HRT — /treatments/hrt
- Testosterone Therapy — /treatments/trt
- Erectile Dysfunction — /treatments/erectile-dysfunction/ed-oral  (flyout)
  - Oral — /treatments/erectile-dysfunction/ed-oral
  - Injectable (ICP) — /treatments/erectile-dysfunction/icp
- Log In — https://app.henrymeds.com/
Footer: Who We Are (/values) · Learn More (/faq) · In The News (/in-the-news) · My Account
        Legal: Privacy, CCPA, NPP, Important Safety Information, Medical Consent, ADA,
               Medical Weight Loss Bill of Rights, Refunds/Returns/Replacements, Terms, Programs, Sitemap
```
*(Top-level items confirmed from the `<header>` region; Weight Management & ED flyouts are client-rendered — sub-items reconstructed from the map's `/treatments/` slugs + homepage cards.)*

## Credibility & proof

- **Trustpilot (self-reported widget):** "TrustScore **4.4** · **12,482** reviews" — flagged self-reported; links to trustpilot.com/review/henrymeds.com.
- **LegitScript certified:** footer seal linking to legitscript.com verification.
- **HIPAA compliant:** footer badge.
- **"Compounded by Licensed Pharmacies in the USA":** footer trust badge; legal copy — "Henry Meds exclusively works with licensed U.S. compounding pharmacies (503A or 503B facilities)."
- **Medical disclaimer:** care provided by "licensed healthcare professionals employed by or contracted with independent professional entities"; "Henry Meds provides administrative and operational support through a telehealth platform" (the friendly-PC / MSO structure, stated).
- No named-clinician / `/physicians` page found; no customer-count claim beyond the Trustpilot widget.

## Visual & brand impression

Warm, approachable, consumer-wellness aesthetic — not clinical. A cream/off-white background (#FFFCF8) with deep forest-green (#113D36 / #2B5745) as the single brand color; the wordmark is a friendly hand-script "Henry." Photography is bright, diverse, real-people lifestyle (people smiling at phones at home), reinforcing the "care from the comfort of your home" message. The app icon (logomark) is a cream "H" on a solid green square. Design maturity is high and cohesive — a polished Framer build with a deliberately soft, premium-DTC feel closer to a lifestyle brand than a pharmacy.

## Provenance

- **Pages:** 15 captured via Firecrawl (homepage, how-it-works, values, + 12 treatment PDPs: GLP-1 hub, semaglutide, semaglutide-oral, tirzepatide-tablets, microdose, microdose-oral, liraglutide, phentermine, trt, hrt, ed-oral, icp). Synthesized across all + screenshots + branding/rawHtml.
- **Verify:** all 15 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 16 (1 map + 15 scrapes).
- **Couldn't get:** exact intake-gated per-dose prices; enumerated state list; /semaglutide PDP price (GLP-1 floor applies).
- **Run profile:** guided — all modules (+telehealth, +offerings, +logos); no emphasis.
