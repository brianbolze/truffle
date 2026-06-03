---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: lifemd.com
name: LifeMD
aliases: ["LifeMD, Inc."]
parent: []
owns: [rexmd.com, shapiromd.com, navamd.com]   # JSON-LD subOrganization; Cleared Technologies also owned (getcleared.com now redirects to lifemd.com — absorbed)
socials:
  instagram: https://www.instagram.com/lifemd/
  x: https://x.com/lifemd
  linkedin: https://www.linkedin.com/company/lifemd-inc/
  youtube: https://www.youtube.com/channel/UCaMRGswkXSXhIYapf8VYH1g
  tiktok: https://www.tiktok.com/@lifemd
external: {}

# Capture meta
captured_at: 2026-06-02
capture_method: firecrawl
site_notes: "Map dominated by /learn/* (blog) + /drugs/* drug-index pages — filter both; signal pages come from homepage links. Pricing lives on /membership + each program page (/weight-management, /womens-health), NOT a single pricing page. Care funnel runs on care.lifemd.com (booking) + rx.lifemd.com (enrollment) subdomains; investor relations on ir.lifemd.com (public co). Site is a jQuery + slick/AOS multi-page build (NOT a JS-framework SPA); homepage loads PostHog (analytics + session replay + surveys), Transcend consent (airgap.js), GTM, FB Pixel."
key_pages:
  about: /about
  how_it_works: /how-it-works
  membership: /membership
  weight_management: /weight-management
  womens_health: /womens-health
  treatment: /treatment
  lifemd_plus: /lifemd-plus
unverified_fields:
  - "Cardiovascular Health program price — page not captured; listed in nav/specialty care but no price pulled."
  - "Patient-count figure conflicts within the site: /about hero says '745,000 Patients' while its body says '600,000+ Patients helped' — both quoted verbatim below, unreconciled."
  - "Weight-management GLP-1 prices vary by tier/insurance (Wegovy Pen 'from $199' and 'from $499' both shown on one page) — point-in-time, likely insurance/eligibility-dependent."

# Description — one sentence (~160-220 chars)
description: "A nationwide DTC telehealth company delivering virtual primary, urgent, and specialty care — weight loss, women's HRT, mental health, cardiovascular — via a $19/mo membership, with at-home labs and prescription fulfillment."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://lifemd.com/css/img/logo.svg
brand_colors: { primary: "#0D6EFD", text: "#000229" }   # STRAIN: blue CTA + near-black navy text; brand also leans on a bright multi-color condition palette + teal/green weight-loss sections (screenshot-confirmed)
fonts: [Manrope]
color_scheme: light
design_framework: custom   # STRAIN: jQuery 3.7.1 + slick-carousel + AOS, custom /assets/public JS; no Next/Vite/Gatsby/Angular marker in rawHtml
---

## Overview

LifeMD is a publicly-traded, nationwide DTC telehealth company (HQ: 236 5th Ave, New York, NY 10001) that sells board-certified virtual care across all 50 states on a low-cost monthly membership. Its model bundles 24/7 urgent + primary care with a set of separately-positioned specialty programs — weight management (GLP-1s), women's health (HRT/menopause), mental health, and cardiovascular care — plus at-home/lab-network testing (Quest, Labcorp) and prescription fulfillment. The parent also owns several condition-specific DTC brands (RexMD, Shapiro MD, Nava MD, Cleared) that run on their own domains; LifeMD.com itself is the flagship general-care brand. Positioning is built around taking "the cost out of healthcare" — transparent upfront pricing, no waiting rooms, same-day access.

## What they offer

Membership-gated virtual care; the LifeMD+ membership is the spine, with specialty programs priced on top (prices verbatim from /membership + program pages, "without insurance" unless noted):

- **LifeMD+ membership:** front-door subscription — 24/7 urgent & primary care, video + message consults, lab testing access — **$19/month**, "No commitment. Cancel anytime." `[published]`
- **Urgent & Primary Care:** same-day refills + common conditions (colds, flu, rashes) — care **"Starting at $49 /visit"** cash, or **"$19 + copay/visit"** with insurance; video visits **$50 (cash)** or copay, message consults **$20** `[published]`
- **Weight Management (flagship):** GLP-1 program (Wegovy®, Zepbound®, Ozempic®) + oral "Triple Therapy" (metformin, bupropion, topiramate) + metabolic labs — care **"as low as $75 for your first month, and just $149 a month thereafter"** ($29/mo with insurance); medication priced separately: **"Zepbound® Vial Starting At $349/mo," "Wegovy® Pen Starting At Just $199," "As Low As $0 Copay … with insurance"** `[partial]`
- **Women's Health:** HRT for perimenopause/menopause (bioidentical estradiol, micronized progesterone, thyroid replacement) + lifestyle support — **"starting at $79 per month, plus the cost of your medication"** `[partial]`
- **Mental Health / Psychiatry:** virtual care for anxiety/depression, medication included in membership — **"Starting at $49 /month"** `[published]`
- **Cardiovascular Health:** board-certified cardiologists managing blood pressure, cholesterol, long-term risk — price not captured `[on-request]`
- **Labs (at-home / lab-network):** Diabetes Test, Heart Health Panel, Cholesterol Panel, Thyroid Function Panel, Female/Male Hormone Panel, Inflammation Panel; program-ordered labs at no cost at Quest/Labcorp (excl. NY/NJ/RI by state rule) `[on-request]`
- **Primary-care condition catalog:** 80+ acute/chronic conditions treated through the membership (acne, UTI, STD testing, hypertension, type-2 diabetes, GERD, insomnia, birth control, etc.) — catalog breadth, not separately priced `[partial]`

Note: erectile-dysfunction and premature-ejaculation links on /treatment route off to **rexmd.com** (sibling brand), not LifeMD's own funnel.

## How it works / model

Quiz/condition selection → book or enroll (booking on `care.lifemd.com`, program enrollment on `rx.lifemd.com`) → meet a licensed provider online (video within ~60 min, message replies within 4 hrs, 24/7) → ongoing subscription with refills, secure messaging, and labs through the patient portal. Money is made on the recurring **$19/mo membership** plus per-program care fees ($49–$149/mo) and per-visit charges; medication and most labs are billed separately (cash, insurance, or discounted self-pay). Insurance is optional and supported but not required ("does not replace insurance"). No controlled substances prescribed.

## Positioning & audience

Mass-market US consumers wanting fast, affordable, all-online care — explicitly framed against "bureaucratic, delayed, and costly" traditional healthcare and in-person clinics. The wedge is **price transparency + access** ("No-surprise Pricing by Program," "low, upfront costs," same-day/24-7). Breadth (general + specialty under one membership) differentiates it from single-condition DTC telehealth brands; it competes on the GLP-1 weight-loss front (Wegovy/Zepbound) and the menopause-HRT front against focused players, while owning condition-specific brands (RexMD men's, Shapiro MD hair, Nava MD, Cleared allergy) for verticals it keeps off the main domain.

## Nav structure

```
- LifeMD+ — /lifemd-plus
- Weight Management — /weight-management
- Women's Health — /womens-health
- Mental Health — /psychiatry
- [Mega-menu] Main Menu
  - Start Your Online Visit
    - All Treatments — /treatment (80+ conditions; e.g. Acne, Acute Bronchitis, Anxiety→/mental-health, Athlete's Foot via care.lifemd.com/create-appointment)
  - Labs (enroll via rx.lifemd.com/plus)
    - Diabetes Test · Heart Health Panel · Cholesterol Panel · Thyroid Function Panel · Female Hormone Panel · Inflammation Panel · Male Hormone Panel
  - Specialty Care (— /membership: All Membership Plans)
    - Weight Loss — /weight-management
    - Women's Health — /womens-health
    - Mental Health — /psychiatry
    - Cardiovascular Health — /cardiovascular-health
    - Urgent + Primary Care — /lifemd-plus
  - Membership Plans — /membership
  - About Us
    - Company: About Us /about · What is Telehealth /what-is-telehealth · Medical Team /medical-team · Careers /careers · Press ir.lifemd.com/press-releases.php
    - Learn: Ways We Help /help · How It Works /how-it-works · Browse Medications /drugs · Blog /learn
    - Contact: /contact · (800) 852-1575 · info@lifemd.com
  - Support
    - Information: Contact /contact · FAQ /faq · Accessibility /accessibility · Support Desk support.lifemd.com · Investors ir.lifemd.com
    - Legal: Telehealth Consent · CCPA · Terms · Privacy · NOPP
- Login — care.lifemd.com/login
```

## Credibility & proof

Self-reported unless noted — recorded verbatim, not endorsed:
- **Scale:** "745,000 Patients" (/about hero, /lifemd-plus) vs "600,000+ Patients helped" (/about body) — internal conflict, see unverified_fields
- **Coverage:** "Available in all 50 states," "Board-certified providers," "100% Online Virtual Care"
- **Ratings:** "4.9" review rating (/about); "4.9 Star App Store Rating," "4.9 Star Google Play Store Rating" (/lifemd-plus) — self-reported, source not shown
- **Clinical claims (weight loss):** "patients lost up to 15-20% of their body weight" using branded GLP-1s, attributed to "clinical studies"; **(women's health):** "estrogen therapy reduces the frequency of common menopause symptoms by 77%," attributed to "clinical trials" — third-party study claims, not LifeMD outcomes
- **Lab partners (named):** Quest Diagnostics, Labcorp
- **Testimonials:** rotating "Verified Patient" reviews with named providers (Dr. Sehgal, Dr. Culpepper, Dr. Puopolo); insurance-provider logo wall on homepage
- **Trust/privacy posture:** "No data selling," "Secure by design," Transcend consent management deployed

## Visual & brand impression

Clean, modern, mass-consumer healthcare aesthetic — high design maturity. Bright, friendly multi-color system: pastel condition cards (pink/orange/blue/green), a teal/green hero band for the Wegovy weight-loss section, a deep-blue gradient footer CTA, and lifestyle/nature photography (outdoor, "feel like yourself again"). Manrope throughout reads contemporary and approachable; lots of phone-mockup/portal-message motifs ("Your labs are complete…") to signal an app-first, always-on experience. Tone is warm and reassuring, not clinical-sterile — leans optimistic/wellness while keeping a board-certified, legitimate-medicine credibility frame.

## Strategic read

Breadth is the strategy. LifeMD runs a **portfolio**: a broad general-care flagship (lifemd.com) wrapped around a cheap $19/mo membership that funnels into higher-margin recurring specialty programs (GLP-1 weight loss is the clear growth engine, menopause HRT a fast-follow), plus a stable of acquired/owned single-vertical DTC brands (RexMD, Shapiro MD, Nava MD, Cleared) kept on separate domains. The membership-as-front-door + insurance-optional + own-pharmacy-fulfillment structure is the recurring-revenue flywheel and the acquirability story. The Cleared absorption (getcleared.com → lifemd.com) suggests a roll-up-then-consolidate pattern worth watching.

## Provenance

- **Pages:** homepage + /about, /how-it-works, /membership, /weight-management, /treatment, /lifemd-plus, /womens-health (8 total) — Firecrawl scrape, maxAge:0 + location:US, all-formats homepage; map filtered for /learn + /drugs noise; structured layer (JSON-LD + nav) read via `fc.py signals`.
- **Verify:** all 8 sourceURLs matched, all body md5s unique (no geo/cache contamination).
- **Credits:** 9 (1 map + 8 scrapes); 0 add-ons; 1118→~1109 plan balance.
- **Couldn't get:** Cardiovascular Health pricing (page not scraped); reconciled patient-count + per-tier GLP-1 prices flagged in unverified_fields.
- **Enriched (model knowledge):** LifeMD is publicly traded as NASDAQ **LFMD** (identity prior; ir.lifemd.com confirms a public co, ticker not on captured pages). Sub-brand domains rexmd.com / shapiromd.com / navamd.com resolved live via curl HEAD (free identity check); getcleared.com 301→lifemd.com.
