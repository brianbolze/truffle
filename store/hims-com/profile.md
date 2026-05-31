---
schema_version: 1

# Identity
domain: hims.com
name: Hims
aliases: [www.hims.com]
parent: ["Hims & Hers Health, Inc."]   # NYSE: HIMS; men's brand of the public co. No distinct corporate domain (investors.hims.com is a subdomain). forhers.com is the sister women's brand.
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Custom in-house React SPA — hashed webpack bundles named `hims.us.legacy.*` (NOT Next/Gatsby/Shopify); Cloudinary for images, Stripe checkout, GTM, reCAPTCHA, Transcend consent. Mega-nav is client-rendered (not in markdown) — reconstruct category hierarchy from the homepage product grid + footer. Category pages show 'Starting at $X/mo' / 'From $X/mo' per SKU; full out-the-door price is gated behind the per-condition intake quiz. Weight-loss membership is billed SEPARATELY from medication ($39 first month, auto-renews $149/mo); advertised drug prices are medication-only. Investor/financial data lives at investors.hims.com (NYSE: HIMS)."
key_pages:
  weight_loss: /weight-loss
  sexual_health: /sexual-health
  hair_loss: /hair-loss
  testosterone: /testosterone
  labs: /labs
  how_it_works: /about/how-it-works
  about_company: /about/the-company
unverified_fields:
  - "Out-the-door / total prices — only 'starting at' per-SKU teasers are public; real cost is behind each condition's intake quiz, not submitted."
  - "Headcount, revenue, subscriber count — financials are at investors.hims.com (NYSE: HIMS), not on the marketing site; a deep-research job, not capture."
  - "Full mega-nav taxonomy — client-rendered and absent from the captured markdown; nav below is reconstructed from the homepage category grid + footer."

description: "The men's half of NYSE-listed Hims & Hers — a DTC telehealth brand connecting men to licensed clinicians for prescription sexual-health, hair-loss, weight-loss, testosterone, and mental-health care, delivered as a monthly membership with at-home labs."

# Classification
entity_type: Company                 # runs its own P&L / sells directly under a public parent → Company, not Brand (per SCHEMA example)
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # clinician telehealth + prescription pharma
portfolio_shape: Multi-product       # six co-equal, separately-positioned condition lines
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://www.hims.com/forhims/image/upload/q_auto,f_auto,fl_lossy,c_limit/Hims/apple-touch-icon-hims  # branding.images.logo was an inline data-URI SVG wordmark → favicon fallback
brand_colors: { primary: "#C79B85", accent: "#FFC671", text: "#453421" }  # warm tan + amber-gold on dark-brown text, verified against screenshot. branding's secondary "#0000EE" is default-link chrome — dropped.
fonts: [Sofia Pro]                   # branding.fonts[0], role:body
color_scheme: light
design_framework: custom React SPA   # hashed webpack bundles (hims.us.legacy.*) in rawHtml — NOT branding.designSystem ("custom" happened to be right here, but read from rawHtml regardless)
---

## Overview

Hims is the men's-facing telehealth brand of Hims & Hers Health, Inc. (NYSE: HIMS; founded 2017, co-founder/CEO Andrew Dudum). It connects men with licensed healthcare providers who review a digital intake and, where appropriate, prescribe treatment — spanning sexual health, hair loss, weight loss, testosterone, and mental health — fulfilled and refilled on a monthly membership. The pitch is convenience, discretion, and affordability versus in-person care: "we meet customers where they are — digitally, discreetly, and on their own time." Hers (forhers.com) is the sibling women's brand under the same public company.

## What they offer

Six separately-positioned condition lines, all subscription, most starting from a digital intake:

- **Weight loss:** the current hero. A "holistic program" (nutrition + app tracking + meds) gating a wide **GLP-1 lineup**: Wegovy® Pill from $149/mo, Wegovy® Pen from $199/mo, Ozempic® Pill from $149/mo, Foundayo® (orforglipron) from $149/mo, Zepbound® KwikPen® / Vial $299/mo — *medication-only prices; a separate Weight Loss Membership is $39 first month, then $149/mo*. Compounded and brand-name options coexist.
- **Sexual health:** the original franchise: ED (sildenafil/"generic Viagra," tadalafil/Cialis, branded Cialis®) and premature ejaculation (sertraline for PE). Starting at $19–$39/mo for generics (brand-name SKUs run far higher, e.g. one at $543/mo).
- **Hair loss:** finasteride, minoxidil, topical finasteride, combo kits; starting $15–$60/mo.
- **Testosterone:** enclomiphene-based "Testosterone by Hims," from $99/mo (10-month plan paid upfront), plus T-boosting supplements and at-home T labs.
- **Mental health / psychiatry:** generics sertraline (Zoloft®), escitalopram (Lexapro®).
- **Labs:** a newer wedge: a Quest Diagnostics blood draw testing 75+ biomarkers at baseline (130+ available), twice-yearly panels, plus the Galleri® multi-cancer early-detection test; results + an "Action Plan" surfaced in-app.

## How it works / model

Customer journey: pick a condition → complete a dynamic **digital intake** (symptoms, history, goals) + identity verification → a licensed provider reviews and, at their independent clinical judgment, prescribes → medication ships to the door → ongoing **unlimited secure messaging** with a care team, dosage adjustments, and refills. Money is made on recurring **subscription/membership** revenue plus medication margin; the weight-loss line explicitly splits a recurring membership fee from medication cost. An in-app experience (iOS/Android) anchors tracking, labs, and care-team contact.

## Positioning & audience

Targets men who'd otherwise avoid or delay care (ED, hair loss, weight, low T, anxiety), positioning as a clinical, doctor-led, data-driven alternative to both in-person clinics and lighter "wellness" telehealth. Claimed edge: breadth of access (especially the FDA-approved GLP-1 catalog), affordability/transparency ("pass cost savings onto customers"), a named bench of specialist clinicians, and an app-centric, always-on care relationship. Deeper voice/positioning work belongs in `brand.md` if enabled.

## Nav structure

Reconstructed from the homepage category grid + footer (mega-nav is client-rendered, not captured):

```
- Weight Loss — /weight-loss
  - Wegovy Pen/Pill, Zepbound KwikPen/Vial, Ozempic Pill, Foundayo — /weight-loss/<sku>
  - The science — /weight-loss/science · Membership — /weight-loss/membership
- Sexual Health — /sexual-health  (homepage entry: /g/i/sh)
  - ED: sildenafil, tadalafil, Cialis — /erectile-dysfunction/<drug>
  - Premature ejaculation: sertraline for PE — /premature-ejaculation/sertraline-for-pe
- Hair Loss — /hair-loss  (homepage entry: /c/hl)
  - finasteride, minoxidil, topical finasteride — /hair-loss/<drug>
- Testosterone — /testosterone  (homepage entry: /g/i/tt)  · Learn — /learn/testosterone
- Mental Health — /mental-health
  - psychiatry: sertraline, escitalopram — /psychiatry/<drug>
- Labs — /labs
  - Biomarkers — /labs/biomarkers · Multi-cancer (Galleri) — /labs/cancer-test
- About — /about
  - The company — /about/the-company · How it works — /about/how-it-works
  - Clinical excellence — /about/clinical-excellence · Innovation — /about/innovation
  - Quality & Safety — /quality-and-safety · Hims Benefits — /benefits
- Tools — /tools/{bmi,tdee,calorie-deficit,protein,water-intake}-calculator
- Drugs — /drugs/compare · /drugs/info
```

## Credibility & proof

- **Public company**: Hims & Hers Health, Inc., NYSE: HIMS, founded 2017; now in retail (Target).
- **Named clinical bench** on the homepage: Dr. Craig Primack (Head of Weight Loss, obesity medicine), Dr. Peter Stahl (Head of Men's Sexual Health & Urology), Dr. Brian Williams (Head of Medical Affairs), Dr. Alicia Warnock (Endocrinology Advisor, ex-Walter Reed), Dr. Deepak L. Bhatt (Cardiology Advisor).
- **LegitScript-certified** pharmacy seal in the footer; testimonials throughout.
- Heavy, consistent **regulatory disclaiming**: GLP-1 trademark/affiliation notices, "compounded products are not FDA-approved," cancer-test false-positive/negative caveats, "not available in all 50 states," Lancet citation for the 25%-body-weight claim — a notably compliance-forward presentation.

## Visual & brand impression

Premium, editorial, lifestyle-catalog feel. A warm earthy palette — sand, cream, terracotta, and amber-gold backgrounds with dark-brown/near-black type — set against soft studio photography of real men. The oversized lowercase "hims" wordmark closes the page. Clean geometric sans (Sofia Pro), generous whitespace, restrained motion, product cards with hover states. Reads as a mature, well-funded DTC brand that wants to feel like a modern men's-grooming/wellness label rather than a clinic — confident, calm, and aspirational, not clinical-sterile.

## Strategic read

The capture catches Hims mid-pivot from its sexual-health/hair-loss origins to a **weight-loss-led, GLP-1-centric** company: the homepage hero, the "GLP-1 pill is here" banner, and the breadth of branded + compounded GLP-1 SKUs dominate. Two adjacent bets are visible — **at-home labs** (Quest panels + Galleri cancer screening, an "optimization"/longevity wedge that also feeds the testosterone and weight lines) and a heavy **AI/infra** signal (a CTO hired from Cruise). The membership-separate-from-medication pricing structure and dense regulatory disclaiming reflect both the compounding-GLP-1 scrutiny of this market and Hims's posture as the compliance-forward, clinician-fronted incumbent.

## Provenance

- **Pages:** homepage (+ rawHtml/branding/screenshot), /weight-loss, /sexual-health, /hair-loss, /testosterone, /labs, /about/how-it-works, /about/the-company (8) — all Firecrawl (`fc.py`, `maxAge:0`, `location:US`); map returned 306 URLs (heavy blog/guides/support/investor noise; core catalog pulled from homepage links).
- **Verify:** all sourceURLs matched, all bodies md5-unique (clean — no geo/cache contamination).
- **Credits:** ~9 Firecrawl credits.
- **Couldn't get:** per-condition pricing past the "starting at" teaser (behind intake quizzes); the client-rendered mega-nav; financials (investor site).
