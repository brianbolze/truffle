---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: honehealth.com
name: Hone Health
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "WordPress (wp-content + wp-json markers; About page leaks the Cloudways origin host wordpress-1321605-5563180.cloudwaysapps.com). A/B: Optimizely — live (an `optimizely.com is blocked` blob leaks into markdown as noise); captured pricing + which homepage/landing modules render are a point-in-time snapshot, expect run-to-run flicker. /membership-pricing renders client-side and returns an empty (chrome-only) markdown body — membership pricing instead lives in the homepage FAQ and per-product pages. The full mega-nav DOES serialize into the homepage markdown (no flyout-recovery needed). Product catalog is under /mens/* and /womens/* (hub pages /mens, /womens); the map is ~80% noise — 328 of 484 URLs are /edge/* blog + programmatic /biomarkers/* SEO — so pull the catalog from homepage links, not the map. Funnel + app live on subdomains: start.honehealth.com & buy.honehealth.com (onboarding/quiz), app.honehealth.com (member login), shop.honehealth.com (supplements), help.honehealth.com (support)."
key_pages:
  how_it_works: /how-it-works
  membership_pricing: /membership-pricing
  about: /about
  mens_hub: /mens
  womens_hub: /womens
  mens_trt: /mens/testosterone-replacement-therapy
  womens_menopause: /womens/menopause-treatment
  mens_weight_loss: /mens/weight-loss
  longevity: /mens/longevity
  hone_at_home: /hone-at-home
  biomarkers: /biomarkers
  physicians: /physicians
  consults: /consults
unverified_fields:
  - "Membership pricing taken from homepage FAQ + product pages — /membership-pricing is JS-walled (empty markdown body)."
  - "Biomarker-panel size is stated inconsistently across pages: '40+ biomarkers' (homepage, /hone-at-home) vs '50-biomarker blood testing' (TRT page) — likely an A/B or copy-version artifact."
  - "Prices ($28–$160/mo) & which modules/landing pages render are a point-in-time snapshot, not fixed — Optimizely A/B testing is live; expect run-to-run flicker."
  - "Weight-loss GLP-1 molecule→price mapping not fully resolved per-SKU; price band $60–$160/mo + membership captured at the line level."
  - "Headcount, funding stage, revenue — not on the marketing site (deep-research job)."

description: "An online telehealth clinic delivering hormone therapy, weight-loss, longevity, and sexual-health treatments to men and women through licensed physicians, using at-home 40+ biomarker lab testing to personalize and monitor each plan."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://honehealth.com/wp-content/uploads/2024/04/cropped-favicon-150x150.png  # STRAIN: branding logo LLM failed (rejected); fell back to favicon
brand_colors: { primary: "#F8F93F", text: "#0E0B20", background: "#FFFFFF" }  # STRAIN: chartreuse-yellow #F8F93F is the verified hero/section brand hue; branding.accent (#0E0B20) is the near-black text/footer color
fonts: [STIX Two Text, DM Sans]   # display serif (headings) + sans body
color_scheme: light
design_framework: wordpress       # rawHtml: wp-content + wp-json (Cloudways-hosted); branding.designSystem said "unknown" (ignored)
---

## Overview

Hone Health is a DTC telehealth clinic that frames itself as a **longevity platform** — "Longevity engineered around your biology." It serves **both men and women** (it began men's-only and has since added a full women's line), pairing at-home or at-lab **biomarker blood testing** with **licensed-physician** telehealth consults to prescribe and ship treatments to the patient's door. The wedge is diagnostics: nearly every journey starts with a $65 lab panel (40+ biomarkers across hormones, heart, thyroid, liver, kidney, immunity, metabolism, nutrients), after which a physician builds a personalized protocol. Founded by **Saad Alam** (HQ: 154 W. 14th Street, New York, NY); brands itself around the "Death to Midlife" idea.

## What they offer

Several distinct, separately-positioned lines, split by sex, all wrapped in a membership:

- **Hormone therapy:** the flagship. *Men:* TRT (testosterone injections, cream, dissolvable troches), plus testosterone-supporting/fertility-preserving agents (clomiphene, enclomiphene) and estrogen control (anastrozole). *Women:* menopause HRT — testosterone (injection/cream), estradiol (patch, vaginal cream/Estrace, Vagifem), bi-est cream, progesterone (oral + cream), DHEA.
- **Weight loss:** GLP-1 and adjuncts: compounded liraglutide, plus naltrexone, bupropion, phentermine, topiramate, sermorelin (men's + women's).
- **Longevity / peptides:** NAD+, metformin, low-dose naltrexone, glutathione, B12, prescription omega-3 (peptides waitlist live).
- **Sexual health:** men's ED (sildenafil, tadalafil, PT-141); women's low libido (PT-141, clitoral cream).
- **Thyroid:** desiccated thyroid, T3, Synthroid (men's + women's).
- **Hair loss / appearance:** finasteride + minoxidil.
- **Supplements:** separate storefront at shop.honehealth.com.
- **Hone at Home:** a concierge in-person arm (Botox $350+, IV Therapy $249+, at-home 40+ biomarker draw $65) in Orlando FL, Denver CO, Phoenix AZ, and NY metro.

## How it works / model

A four-step journey, marketed as **Measure & Assess → Consult & Plan → Treat & Act → Optimize & Adapt**: (1) buy the **$65 biomarker test + consult** (risk-free entry; complete at a partner lab or via a free at-home nurse draw where available); (2) a licensed physician reviews labs + history and builds a plan (~5 days); (3) medications/supplements ship to the door (~10 days) with ongoing care-team support; (4) retesting and protocol adjustment over time.

Revenue is **subscription** on top of medication cost. Two membership tiers (verbatim, homepage):
- **Hone Basic ($25/mo):** "plus cost of medication": advanced testing of 40+ biomarkers every 6 months, ability to *purchase* telehealth consults, members-only pricing on BASIC medications & supplements.
- **Hone Premium ($155/mo):** "plus cost of medication" ("Chosen by 95% of patients"): 40+ biomarker testing, included physician consults, personalized protocols (testosterone, estrogen, weight loss & more), retesting + follow-ups every 90 days.
- **Entry ($65 per Biomarker Test + Consult):** the funnel's risk-free first step. "No commitments. Cancel anytime."

Medication is priced separately per-SKU, "+ membership." Representative captured prices: testosterone from $28/mo, testosterone cream/troches $60/mo, clomiphene $38, enclomiphene $42, anastrozole $22 (men's TRT); estradiol patch $58, bi-est cream $80, progesterone $49 / cream $79, Estrace $40, Vagifem $65, DHEA cream $56 (women's HRT); weight-loss line $60–$160/mo.

## Positioning & audience

Aimed at aging adults (broadly 35–60) who feel "off" and were told it's "just aging" — the founder's own origin story. Positions as a **clinical, data-driven, physician-led longevity** offering: lab-grounded and personalized, against both in-person clinics (slow, generic) and lighter "wellness"/DTC telehealth (no real diagnostics). The longevity/"healthspan" framing and the dual men+women scope distinguish it from male-only TRT players. Celebrity **brand ambassadors**: Paul Wesley, Nikki & Brie Garcia, Dan Churchill, Louisa Nicola, Brendan Fallis. Public campaigns: "Death to Midlife" and a "Menopause Time Off" workplace-leave coalition.

## Nav structure

```
- Men — /mens  (All Men's Health)
  Treatments:
  - Increase Testosterone (TRT) — /mens/testosterone-replacement-therapy
  - Lose Weight — /mens/weight-loss
  - Live Longer & Better (Longevity) — /mens/longevity
  - Improve Sexual Function (ED) — /mens/erectile-dysfunction-treatment
  - Manage Thyroid — /hypothyroidism/men
  - Improve Appearance (Hair Loss) — /mens/hair-loss
  - Supplements — shop.honehealth.com/supplements/mens
  Trending: Testosterone — /mens/buy-testosterone
- Women — /womens  (All Women's Health)
  Treatments:
  - Relieve Menopause Symptoms — /womens/menopause-treatment
  - Lose Weight — /womens/weight-loss
  - Live Longer & Better (Longevity) — /womens/longevity
  - Improve Sexual Function (Low Libido) — /womens/low-libido-treatment
  - Manage Thyroid — /hypothyroidism/women
  - Improve Appearance (Hair Loss) — /womens/hair-loss
  - Supplements — shop.honehealth.com/supplements/womens
  Trending: Testosterone (Cream) — /womens/testosterone-cream
- How It Works — /how-it-works
- The Edge Blog — /edge  (Low Testosterone, Menopause, Longevity, Testing)
- Get Started — start.honehealth.com/hermes/landing
- Sign In — app.honehealth.com/login
Footer — Why Hone: How It Works, Hone Biomarkers /biomarkers, Physicians /physicians,
  Consults /consults, Clinical /clinical-policy · Our Company: About /about, Careers,
  Help Center, Concierge Nursing /hone-at-home/nurses
```

## Credibility & proof

- **Trustpilot:** 4.8 / 5 across 11,526 reviews (homepage widget).
- **LegitScript-approved:** seal links to LegitScript verification of honehealth.com — a meaningful regulatory trust signal for a prescribing telehealth clinic.
- **Physician-led:** Hone-affiliated medical practices are independently owned/operated by licensed physicians using the Hone telehealth platform (`/clinical-policy`).
- **Testimonials:** compensated-patient testimonials (named, with ages) and named celebrity ambassadors.
- **Trust pages:** `/physicians`, `/consults`, `/clinical-policy`, plus a deep programmatic biomarker library (`/biomarkers/*`).

## Visual & brand impression

Polished, premium, editorial. The identity is built on a single bold **chartreuse-yellow (#F8F93F)** against near-black (#0E0B20) on white — used in the hero band, section backgrounds, and membership cards (verified in the screenshot). Typography pairs a **display serif (STIX Two Text)** for headlines with a **clean sans (DM Sans)** for body — a science-meets-lifestyle, slightly luxury feel rather than clinical-sterile. Imagery is aspirational lifestyle (diverse midlife couples, athletes) interleaved with product-credibility visuals (lab-result UI mockups, app screens, medication renders). Reads as a mature, well-funded consumer brand, not an MVP.

## Provenance

- **Pages:** homepage (rich pass: markdown/html/rawHtml/links/branding/screenshot), how-it-works, membership-pricing (JS-walled — chrome only), about, /mens/testosterone-replacement-therapy, /womens/menopause-treatment, /mens/weight-loss, /hone-at-home (8 pages) — Firecrawl `maxAge:0`, `location:US`, `waitFor:3500`; WordPress site (wp-content + wp-json); Optimizely A/B testing live, capture is a point-in-time snapshot.
- **Verify:** all sourceURLs matched, all bodies md5-unique (clean).
- **Credits:** 9 (1 map + homepage + 7 key pages).
- **Couldn't get:** server-rendered membership-pricing detail (recovered from homepage FAQ instead); per-SKU weight-loss price map; any financials/headcount (not on site).
