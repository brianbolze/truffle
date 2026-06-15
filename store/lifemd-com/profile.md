---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: lifemd.com
name: LifeMD
aliases: []
legal_entity: "LifeMD, Inc."          # JSON-LD Organization name + footer "© 2026 | LifeMD®" / "LifeMD, Inc. provides… services to the LifeMD Affiliated P.C.s"
parent: []
owns: [rexmd.com, shapiromd.com, navamd.com]   # JSON-LD subOrganization (REX MD™, Shapiro MD™, Nava MD™, Cleared Technologies, Inc.); Cleared = getcleared.com, now 301→lifemd.com (absorbed)
socials:
  instagram: https://www.instagram.com/lifemd/
  x: https://x.com/lifemd
  linkedin: https://www.linkedin.com/company/lifemd-inc/
  youtube: https://www.youtube.com/channel/UCaMRGswkXSXhIYapf8VYH1g
  tiktok: https://www.tiktok.com/@lifemd
external: {}

# Capture meta
captured_at: 2026-06-15
capture_method: firecrawl
site_notes: "Map dominated by /learn/* (blog) + /drugs/* drug-index pages — filter both; signal pages come from homepage links. Pricing lives on /membership + each program page (/weight-management, /womens-health, /psychiatry), NOT a single pricing page. Commerce is a WALLED funnel: every CTA leaves lifemd.com for care.lifemd.com (booking) or rx.lifemd.com/<program> (enrollment, behind a quiz); investor relations on ir.lifemd.com (public co, NASDAQ LFMD). /mental-health mirrors the homepage (its CTAs route to /psychiatry); the mental-health PROGRAM + 9-drug grid + pricing live on /psychiatry, where top-nav 'Mental Health' points. Friendly-PC/MSO structure: footer states 'LifeMD, Inc. provides a variety of administrative and management services to the LifeMD Affiliated P.C.s.' WM first-month promo is VOLATILE ($39 on the homepage hero ‡ footnote vs $75 on /membership — A/B/promo). Homepage carries LillyDirect®/Foundayo™ (orforglipron) Eli Lilly co-branding. Site is a jQuery 3.7.1 + slick-carousel + AOS multi-page build (NOT a JS-framework SPA), custom /assets/public JS; homepage loads PostHog (analytics + session replay + surveys), Transcend consent (airgap.js), GTM, FB Pixel. A/B: yes (PostHog + promo flicker)."
key_pages:
  about: /about
  how_it_works: /how-it-works
  membership: /membership
  lifemd_plus: /lifemd-plus
  weight_management: /weight-management
  wegovy: /wegovy
  womens_health: /womens-health
  psychiatry: /psychiatry
  mental_health: /mental-health
  cardiovascular_health: /cardiovascular-health
  medical_team: /medical-team
  treatment: /treatment
unverified_fields:
  - "Patient-count figure conflicts within the site: /about + /lifemd-plus hero say '745,000 Patients' while the /about body says '600,000+ Patients helped' — both quoted verbatim below, unreconciled."
  - "Prices/IA are a point-in-time snapshot, not fixed — LifeMD A/B-tests (PostHog session replay + surveys) and runs promos; the WM first-month program-fee discount shows '$39' on the homepage hero ‡ and '$75' on /membership in the same capture. Treat any single GLP-1/program figure as point-in-time."
  - "App Store / Google Play '4.9' ratings and the '4.9 Review' figure are self-reported on-page; source/sample not shown."

# Description — one sentence (~160-220 chars)
description: "A nationwide DTC telehealth company delivering virtual primary, urgent, and specialty care — GLP-1 weight loss, menopause HRT, mental health, cardiovascular — on a $19/mo membership, with at-home labs and prescription fulfillment."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://lifemd.com/css/img/logo.svg   # hostable wordmark (canonical mark, 2.5+)
logos:
  wordmark: { src: "https://lifemd.com/css/img/logo.svg", w: 232, h: 65 }                                        # hostable on-domain SVG wordmark (no file needed)
  logomark: { src: "https://www.google.com/s2/favicons?domain=lifemd.com&sz=256", px: 180, transparent: true }   # two-tone teal medical-cross mark; corners transparent on a checker tile
  og:       { src: "https://lifemd.com/img/og-image.webp?1781527776", w: 1200, h: 630 }                          # "LifeMD+ — The Doctor Will See You Now" branded cover (woman + faded Rx-bottle UI on blue gradient)
brand_colors: { primary: "#0D6EFD", text: "#000229" }   # STRAIN: blue CTA + near-black navy text; brand also leans on a two-tone TEAL mark + a bright multi-color condition palette + teal/green weight-loss sections (screenshot-confirmed)
fonts: [Manrope]
color_scheme: light
design_framework: custom   # STRAIN: jQuery 3.7.1 + slick-carousel + AOS + custom /assets/public JS; rawHtml shows no __NEXT_DATA__/_next/wp-content/gatsby/shopify/Drupal marker
---

## Overview

LifeMD is a publicly-traded (NASDAQ: LFMD), nationwide DTC telehealth company (HQ: 236 5th Ave, 4th floor, New York, NY 10001) that sells board-certified virtual care across all 50 states on a low-cost monthly membership. The model pairs 24/7 urgent + primary care with a set of separately-positioned, higher-margin specialty programs — weight management (branded GLP-1s), women's health (menopause HRT), mental health, and cardiovascular care — plus at-home/lab-network testing (Quest, Labcorp) and prescription fulfillment through a "nationwide mail-order pharmacy network." Care is delivered by the **LifeMD Affiliated P.C.s** (a friendly-PC/MSO structure — "LifeMD, Inc. provides administrative and management services to the… P.C.s"). The parent also owns several condition-specific DTC brands (RexMD, Shapiro MD, Nava MD, and the absorbed Cleared) that run on their own domains; lifemd.com is the flagship general-care brand. Positioning is built on "taking the cost out of healthcare" — transparent, upfront, no waiting rooms, same-day access.

## What they offer

Membership-gated virtual care: the $19/mo LifeMD+ membership is the spine, with specialty programs priced on top (a separate per-program **care fee** + separately-billed **medication**). Prices verbatim from /membership + /lifemd-plus + each program page ("without insurance" unless noted):

- **LifeMD+ membership:** front-door subscription — 24/7 urgent & primary care, video + message consults, at-home/lab-network testing access — **"$19/month"**, "No commitment. Cancel anytime." `[published]`
- **Urgent & Primary Care:** same-day refills + common conditions (colds, flu, rashes) — care **"Starting at $49 /visit"** (cash) or **"$19 + copay/visit"** (insurance); video visits **$50 (cash)** or copay, message consults **$20** `[published]`
- **Weight Management (lead program):** GLP-1 program (Wegovy®, Zepbound®, Ozempic®, Saxenda®, Lilly's Foundayo™/orforglipron) + oral "Triple Therapy" (metformin, bupropion, topiramate) + metabolic labs — care **"as low as $39 for your first month, and just $149 a month thereafter"** (/weight-management; /membership shows **"$75/month"** cash / **"$29/month"** insured — promo-volatile); medication billed separately: homepage hero **"Access FDA-approved Wegovy®, starting at just $149‡"** (pill) / **"$199"** (pen), Zepbound® Vial **"$349/mo"** — the `‡` footnote confirms these are *medication-only* and exclude the $149/mo program fee `[partial]`
- **Women's Health:** bioidentical HRT for perimenopause/menopause (estradiol patch/insert/gel, micronized progesterone, thyroid replacement) + lifestyle support — **"starting at $79 per month, plus the cost of your medication"** `[partial]`
- **Mental Health / Psychiatry:** virtual care for anxiety/depression (as-needed + daily plans); **medication included** in the program fee — **"Starting at $49 /month"** `[published]`
- **Cardiovascular Health:** board-certified cardiologists (Dr. Rahul Deo, Dr. Calum MacRae) managing blood pressure, cholesterol, AFib, long-term risk — **no price shown**, only "Insurance accepted*" `[on-request]`
- **Labs (at-home / lab-network):** Diabetes, Heart Health, Cholesterol, Thyroid Function, Female/Male Hormone, Inflammation panels (+ a "GLP-1 Health Insights Panel"); program-ordered labs at no cost at Quest/Labcorp (excl. NY/NJ/RI by state rule); enroll via rx.lifemd.com/plus `[on-request]`
- **Primary-care condition catalog:** 80+ acute/chronic conditions treated through the membership (acne, UTI, STI/STD testing, hypertension, type-2 diabetes, GERD, IBS, insomnia, birth control, etc.) — catalog breadth, not separately priced `[partial]`

Note: erectile-dysfunction, premature-ejaculation, and sleep links route OFF-domain (rexmd.com sibling brand; rx.lifemd.com/sleep-xp1), not LifeMD's own funnel. Per-SKU depth (incl. the GLP-1 two-price trap and the 9-drug mental-health grid) is in `offerings.md`; cohort cuts in `telehealth.md`.

## How it works / model

Quiz/condition selection → book or enroll (booking on `care.lifemd.com`, program enrollment on `rx.lifemd.com/<program>` behind an intake quiz) → meet a LifeMD-affiliated licensed provider online (video within ~60 min, message replies within 4 hrs, 24/7) → ongoing subscription with refills, secure messaging, and labs through the patient portal. Modality is **hybrid** — synchronous video plus message-based async care for certain conditions. Money is made on the recurring **$19/mo membership** plus per-program care fees ($49–$149/mo) and per-visit/per-consult charges ($50 video, $20 message); medication and most labs are billed separately (cash, insurance, or discounted self-pay, plus a prescription discount card "accepted at over 60,000 pharmacies"). Insurance is optional and supported (copay pricing, Medicare accepted, an insurance-benefits-check service) but not required ("Does this replace insurance? No"). No controlled substances prescribed.

## Positioning & audience

Mass-market US consumers (all-genders, no gendered front door) wanting fast, affordable, all-online care — explicitly framed against "bureaucratic, delayed, and costly" traditional healthcare and in-person clinics. The wedge is **price transparency + access** ("No-surprise Pricing by Program," "low, upfront costs," same-day/24-7, "Care without the wait"). Breadth (general + specialty under one cheap membership) differentiates it from single-condition DTC telehealth brands; it competes on the GLP-1 weight-loss front (Wegovy/Zepbound, plus Lilly's Foundayo via LillyDirect®) and the menopause-HRT front against focused players, while owning condition-specific brands (RexMD men's, Shapiro MD hair, Nava MD, Cleared allergy) for verticals it keeps off the main domain.

## Nav structure

```
- LifeMD+ — /lifemd-plus
- Weight Management — /weight-management
- Women's Health — /womens-health
- Mental Health — /psychiatry
- Login — care.lifemd.com/login
- [Mega-menu] Main Menu
  - Urgent Care / Start Your Online Visit
    - All Treatments — /treatment (80+ conditions; e.g. Acne, Acute Bronchitis, Altitude Sickness Prevention, Animal Bite, Anxiety→/mental-health, Athlete's Foot via care.lifemd.com/create-appointment?c=…)
    - Join LifeMD+ — rx.lifemd.com/plus
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
    - Social: Instagram · TikTok · LinkedIn · X
  - Support
    - Information: Contact /contact · FAQ /faq · Accessibility /accessibility · Support Desk support.lifemd.com · Investors ir.lifemd.com
    - Legal: Telehealth Consent /consent-to-telehealth · CCPA /ccpa · Terms /terms · Privacy /privacy · NOPP /notice-of-privacy-practices
```

## Credibility & proof

Self-reported unless noted — recorded verbatim, not endorsed:
- **Scale:** "745,000 Patients" (/about + /lifemd-plus hero) vs "600,000+ Patients helped" (/about body) — internal conflict, see unverified_fields
- **Coverage:** "Available in all 50 states," "Board-certified providers," "100% Online Virtual Care," providers "licensed to practice in all 50 states"
- **Ratings:** "4.9" review rating (/about); "4.9 Star App Store Rating," "4.9 Star Google Play Store Rating" (/lifemd-plus) — self-reported, source/sample not shown
- **Named clinical team** (each with a /medical-team/<name> page): Dr. Anthony Puopolo (Family Medicine + psychiatry), Dr. David Culpepper (Internal Medicine, 30+ yrs), Dina Whiteaker FNP (hormone therapy/telemedicine), Dr. Doug Lucas (orthopedic; hormonal/metabolic), Sherri Richardson FNP, Kim Calloway RN, Dr. Tara Scott (Internal Medicine; 15+ yrs telehealth); cardiology leads Dr. Rahul Deo (Harvard lecturer) + Dr. Calum MacRae (Harvard professor, Brigham & Women's)
- **Clinical claims:** weight-loss "patients lost up to 15-20% of their body weight" with branded GLP-1s, attributed to "clinical studies"; women's-health "estrogen therapy reduces the frequency of common menopause symptoms by 77%," attributed to "clinical trials" — third-party study claims, not LifeMD outcomes
- **Trust signals:** BBB "Accredited Business" badge (footer); "HIPAA compliant platform"; prescription discount card "accepted at over 60,000 pharmacies to save up to 92%"; "Medicare accepted"; lab partners Quest Diagnostics + Labcorp (named); rotating "Verified Patient" testimonials with named providers (Dr. Sehgal, Dr. Culpepper, Dr. Puopolo); privacy posture "No data selling," "Secure by design," Transcend consent management. No LegitScript seal on the captured pages.

## Visual & brand impression

*(Lightweight read; superseded by `visual.md` when the visual-evidence module is active.)* Clean, modern, mass-consumer healthcare aesthetic — high design maturity. Bright, friendly multi-color system: pastel condition cards, a teal/green band for the GLP-1 weight-loss section, a deep-blue gradient hero/footer, and lifestyle photography. Heavy use of phone-mockup / patient-portal message motifs ("Your labs are complete…," in-range/above-range lab tiles) to signal an app-first, always-on experience. Manrope throughout reads contemporary and approachable; the two-tone teal medical-cross logomark anchors a warm, reassuring (not clinical-sterile) tone while keeping a board-certified credibility frame.

## Strategic read

Breadth is the strategy. LifeMD runs a **portfolio**: a broad general-care flagship (lifemd.com) wrapped around a cheap $19/mo membership that funnels into higher-margin recurring specialty programs (GLP-1 weight loss is the clear growth engine — now stacking Lilly's Foundayo/orforglipron via LillyDirect® on top of Wegovy/Zepbound; menopause HRT a fast-follow), plus a stable of acquired/owned single-vertical DTC brands (RexMD, Shapiro MD, Nava MD, Cleared) kept on separate domains. The membership-as-front-door + insurance-optional + affiliated-P.C./MSO + mail-order-pharmacy-network structure is the recurring-revenue flywheel and the acquirability story (public co, NASDAQ: LFMD). **Note for downstream readers:** the site claims a "nationwide mail-order pharmacy network" / "local pharmacy" fulfillment — it does **not** page-attest an *owned* pharmacy, so "own-pharmacy fulfillment" is a consumer-side inference, not site-supported (see `telehealth.md` Fulfillment). The Cleared absorption (getcleared.com → lifemd.com) suggests a roll-up-then-consolidate pattern worth watching.

## Provenance

- **Pages:** homepage + /about, /how-it-works, /membership, /lifemd-plus, /weight-management, /wegovy, /womens-health, /psychiatry, /mental-health, /cardiovascular-health, /medical-team, /treatment (13 total) — Firecrawl scrape, maxAge:0 + location:US, all-formats homepage; map filtered for /learn + /drugs noise; structured layer (JSON-LD + nav) read via `fc.py signals`.
- **Verify:** all 13 sourceURLs matched, all 13 body md5s unique (no geo/cache contamination); no junk soft-404s.
- **Credits:** 14 (1 map + 13 scrapes); 0 add-ons.
- **Couldn't get:** Cardiovascular Health pricing — re-checked this run, genuinely **no price shown** pre-enrollment (resolved: `on-request`, not a missed capture). Per-tier/insurance GLP-1 prices + the patient-count conflict flagged in unverified_fields.
- **Enriched (model knowledge):** LifeMD trades as NASDAQ **LFMD** (identity prior; ir.lifemd.com confirms a public co, ticker not on captured pages). Sub-brand domains rexmd.com / shapiromd.com / navamd.com map to the JSON-LD subOrganization names; getcleared.com 301→lifemd.com (absorbed).
- **Run profile:** guided — full re-capture refresh (prior 2026-06-02/03/04 archived). Modules refreshed alongside: `offerings.md` (per-SKU roster), `telehealth.md` (cohort pack), `logos:{}` re-measured (all three slots stable URLs, no committed asset). Blind `visual.md` mined separately via /visual-evidence. Stamped 2.6 (promotes `legal_entity` out of aliases).
- **Migrations:** none (re-captured, not rule-rewritten).
