---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: honehealth.com
name: Hone Health
aliases: [Hone]                       # JSON-LD alternateName
legal_entity: "Time Therapeutics, Inc."   # 2.6 — JSON-LD legalName (site-derivable)
parent: []
owns: []
socials: { linkedin: "https://www.linkedin.com/company/honeyourhealth", x: "https://twitter.com/HoneHealth", instagram: "https://www.instagram.com/hone.health/", youtube: "https://www.youtube.com/channel/UC63XVHmQBqFh5ADIjp7zg4Q", facebook: "https://www.facebook.com/hone.your.health/" }  # JSON-LD sameAs (FB/IG/X also verified in footer)
external: { trustpilot: "https://www.trustpilot.com/review/honehealth.com" }   # JSON-LD sameAs — third-party record; the 4.8/5 rating itself is in Credibility & proof

# Capture meta
captured_at: 2026-06-18
capture_method: firecrawl
site_notes: "WordPress (wp-content + wp-json markers; About page leaks the Cloudways origin host wordpress-1321605-5563180.cloudwaysapps.com). A/B: Optimizely — live (an `a5292374380249088.cdn.optimizely.com is blocked` blob leaks into markdown as noise on most pages); captured pricing + which homepage/landing modules render are a point-in-time snapshot, expect run-to-run flicker. /membership-pricing renders client-side and returns an empty (chrome-only) markdown body — membership pricing instead lives in the homepage FAQ and per-product pages (every Rx page carries the same Basic $25 / Premium $155 FAQ block + a $65 entry). Product catalog is under /mens/* and /womens/* (hub pages /mens, /womens), with per-med prices listed ON the treatment-line page ('From $X/mo + membership'); the newer Heart Health line is the exception — its meds have their own PDPs under /heart-health/<molecule>/ (colchicine, ezetimibe, rosuvastatin). The full mega-nav DOES serialize into the homepage markdown (no flyout-recovery needed). Map is ~80% noise — ~497 URLs, mostly /edge/* blog + programmatic /biomarkers/* SEO — so pull the catalog from homepage links, not the map. Funnel + app live on subdomains: start.honehealth.com & buy.honehealth.com (onboarding/quiz), app.honehealth.com (member login), shop.honehealth.com (supplements), help.honehealth.com (support)."
key_pages:
  how_it_works: /how-it-works
  membership_pricing: /membership-pricing
  about: /about
  clinical_policy: /clinical-policy
  physicians: /physicians
  consults: /consults
  mens_hub: /mens
  womens_hub: /womens
  mens_trt: /mens/testosterone-replacement-therapy
  mens_weight_loss: /mens/weight-loss
  mens_longevity: /mens/longevity
  mens_ed: /mens/erectile-dysfunction-treatment
  mens_hair_loss: /mens/hair-loss
  mens_heart_health: /mens/heart-health
  mens_thyroid: /hypothyroidism/men
  womens_menopause: /womens/menopause-treatment
  womens_testosterone_cream: /womens/testosterone-cream
  womens_weight_loss: /womens/weight-loss
  womens_low_libido: /womens/low-libido-treatment
  womens_heart_health: /womens/heart-health
  hone_at_home: /hone-at-home
unverified_fields:
  - "Membership pricing taken from homepage + per-product FAQ blocks — /membership-pricing is JS-walled (empty markdown body)."
  - "Biomarker-panel size is stated inconsistently: '40+ biomarkers' (homepage, /hone-at-home) vs '50-biomarker blood testing' / '50+ biomarkers' (TRT, heart-health, women's pages) — likely an A/B or copy-version artifact."
  - "Prices ($15–$165/mo med lines; $25/$155 membership) & which modules/landing pages render are a point-in-time snapshot, not fixed — Optimizely A/B testing is live; expect run-to-run flicker."
  - "Per-SKU molecule→price mapping lives in offerings.md; profile carries representative line-level anchors only."
  - "Headcount, funding stage, revenue — not on the marketing site (deep-research job)."

description: "An online longevity-focused telehealth clinic prescribing hormone therapy, weight-loss, sexual-health, thyroid, and now heart-health treatments to men and women, using at-home biomarker lab testing and licensed physicians to personalize each plan on a membership."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — "HONE" header SVG extracted from rawHtml (white-fill, built for the dark hero)
logos:
  wordmark: { src: assets/wordmark.svg, w: 1321, h: 262 }                                                                       # "HONE" bold serif; WHITE-fill (invisible on white)
  logomark: { src: "https://honehealth.com/wp-content/uploads/2024/04/cropped-favicon-300x300.png", px: 300, transparent: true }  # triangle outline, transparent ground (the "TriangleWhite" mark family)
  og:       { src: "https://honehealth.com/wp-content/uploads/2024/09/Hone_SocialShare_TRT.png", w: 1200, h: 900 }                # Hone product bottles ("HONE") — real share cover
brand_colors: { primary: "#F8F93F", text: "#0E0B20", background: "#FFFFFF" }  # STRAIN: chartreuse-yellow #F8F93F is the verified hero/section brand hue; branding.accent (#0E0B20) is the near-black text/footer color
fonts: [STIX Two Text, DM Sans]   # display serif (headings) + sans body
color_scheme: light
design_framework: wordpress       # rawHtml: wp-content + wp-json (Cloudways-hosted); branding.designSystem ignored
---

## Overview

Hone Health is a DTC telehealth clinic that frames itself as a **longevity platform** — "Longevity engineered around your biology." It serves **both men and women** (it began men's-only and has since added a full women's line), pairing at-home or at-lab **biomarker blood testing** with **licensed-physician** telehealth consults to prescribe and ship treatments to the patient's door. The wedge is diagnostics: nearly every journey starts with a **$65 lab panel** (40+ biomarkers across Hormones, Heart, Brain, Liver, Kidneys, Immunity, Metabolism, Nutrients), after which a physician builds a personalized protocol. JSON-LD self-classifies the specialties as Endocrinology, Menopause, and Andrology. Founded in **2021** by **Saad Alam** (his "told it was just aging at 35" origin story anchors the brand); HQ 154 W. 14th Street, New York, NY; legal entity Time Therapeutics, Inc.; campaign idea "Death to Midlife."

## What they offer

Several distinct, separately-positioned lines, split by sex, all wrapped in a membership. Per-line prices are med-only floors with a **mandatory membership on top** (so `[partial]`); the membership + lab entry are self-contained (`[published]`). Per-SKU/molecule depth is in `offerings.md`.

- **Hormone therapy (flagship):** *Men:* TRT — testosterone **From $28/mo** (injection/cream/troche) + supporting agents (anastrozole **$22**, clomiphene **$38**, enclomiphene **$42**) `[partial]`. *Women:* menopause HRT + women's testosterone cream **From $60/mo**; estradiol/progesterone/DHEA lines **$40–$80/mo** `[partial]`.
- **Weight loss:** GLP-1 + adjuncts — **$60–$160/mo + membership** (men's & women's) `[partial]`.
- **Longevity / peptides:** NAD+, metformin, low-dose naltrexone, B12, etc. — **$20–$165/mo + membership** `[partial]`.
- **Heart health (NEW line):** cardiometabolic Rx with their own PDPs — Rosuvastatin / Ezetimibe / Colchicine **$37/mo + membership** (+ cross-listed testosterone From $28) `[partial]`; backed by a 50-biomarker cardiac panel.
- **Sexual health:** men's ED **From $25/mo** (+ a $130 line); women's low libido **$70/$130/mo** `[partial]`.
- **Thyroid:** desiccated thyroid / T3 / Synthroid — **$15–$52/mo + membership** (men's & women's) `[partial]`.
- **Hair loss / appearance:** finasteride + minoxidil — **$38/mo + membership** `[partial]`.
- **Supplements:** separate storefront at shop.honehealth.com.
- **Hone at Home:** concierge in-person arm — Botox **$350+**, IV Therapy **$249+**, at-home 40+ biomarker draw **$65** `[published]`.
- **Membership & entry:** Hone Basic **$25/mo**, Hone Premium **$155/mo** ("plus cost of medication"), risk-free entry **$65 per Biomarker Test + Consult** `[published]`.

## How it works / model

A four-step journey, marketed **Measure & Assess → Consult & Plan → Treat & Act → Optimize & Adapt**: (1) buy the **$65 biomarker test + consult** (complete at a partner lab or via a free at-home nurse draw where available); (2) a licensed physician reviews labs + history and builds a plan (~5 days); (3) medications/supplements ship to the door (~10 days) with ongoing care-team support; (4) retesting + protocol adjustment every 90 days.

Revenue is **subscription** on top of medication cost, with two membership tiers (verbatim, homepage):
- **Hone Basic ($25/mo)** "plus cost of medication": advanced testing of 40+ biomarkers every 6 months, ability to *purchase* telehealth consults, members-only pricing on **BASIC** medications & supplements.
- **Hone Premium ($155/mo)** "plus cost of medication" ("Chosen by 95% of patients"): 40+ biomarker testing, included physician consults, personalized protocols, retesting + follow-ups every 90 days.
- **Entry ($65 per Biomarker Test + Consult):** the funnel's risk-free first step. "No commitments. Cancel anytime."

Clinical governance is explicit: the prescribing physicians "work for an **independent, physician-owned medical group**," compensated solely for completing a consult — not on diagnoses or whether a prescription is issued (`/clinical-policy`). Stated patient base: **25–80 years of age**. Pharmacy fulfillment is unnamed — meds "ship to the door" but no owned or third-party pharmacy appears on the captured pages.

## Positioning & audience

Aimed at aging adults (broadly mid-30s–60) who feel "off" and were told it's "just aging" — the founder's own story. Positions as a **clinical, data-driven, physician-led longevity** offering: lab-grounded and personalized, against both in-person clinics (slow, generic) and lighter "wellness"/DTC telehealth (no real diagnostics). The longevity/"healthspan" framing and dual men+women scope distinguish it from male-only TRT players. The new **heart-health** line is the first concrete step toward the stated vision of becoming "the optimization platform for your life" — expanding from hormones into cardiovascular-risk management. Celebrity **brand ambassadors**: Paul Wesley, Nikki & Brie Garcia, Dan Churchill, Louisa Nicola, Brendan Fallis. Public campaigns: "Death to Midlife" and a "Menopause Time Off" workplace-leave coalition.

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
  - Heart Health — /mens/heart-health        ← new since 2026-05-31
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
  - Heart Health — /womens/heart-health      ← new since 2026-05-31
  - Supplements — shop.honehealth.com/supplements/womens
  Trending: Testosterone (Cream) — /womens/testosterone-cream
- How It Works — /how-it-works
- The Edge Blog — /edge  (Low Testosterone, Menopause, Longevity, Testing, Editorial Standards, Medical Review Process)
- Get Started — start.honehealth.com/hermes/landing
- Sign In — app.honehealth.com/login
Footer — Why Hone: How It Works, Hone Biomarkers /biomarkers, Physicians /physicians,
  Consults /consults, Clinical /clinical-policy · Our Company: About /about, Careers,
  Help Center, Concierge Nursing /hone-at-home/nurses
```

## Credibility & proof

- **Trustpilot:** "TrustScore 4.8 / 11,677 reviews" (homepage widget; self-embedded, flagged self-reported — up from 11,526 on 2026-05-31).
- **LegitScript-approved:** seal links to LegitScript verification of honehealth.com — a meaningful regulatory trust signal for a prescribing telehealth clinic.
- **Independent physician-owned medical group:** physicians "are not compensated based on any treatment decisions… compensated based solely on completing a consult" (`/clinical-policy`) — a stated conflict-of-interest guardrail.
- **Physician-led:** Hone-affiliated medical practices "independently owned and operated by licensed physicians who provide services using the Hone telehealth platform."
- **Testimonials:** compensated-patient testimonials (named, with ages 37–52) and named celebrity ambassadors.
- **Trust pages:** `/physicians`, `/consults`, `/clinical-policy`, plus a deep programmatic biomarker library (`/biomarkers/*`).

## Visual & brand impression

Polished, premium, editorial. The identity is built on a single bold **chartreuse-yellow (#F8F93F)** against near-black (#0E0B20) on white — hero band, section backgrounds, membership cards. Typography pairs a **display serif (STIX Two Text)** for headlines with a **clean sans (DM Sans)** for body — science-meets-lifestyle, slightly luxury rather than clinical-sterile. Imagery is aspirational lifestyle (diverse midlife couples, athletes) interleaved with product-credibility visuals (lab-result UI mockups, app screens, medication renders). Reads as a mature, well-funded consumer brand, not an MVP. *(A blind, cited visual read is in `visual.md`.)*

## Provenance

- **Pages:** homepage (rich pass: markdown/html/rawHtml/links/branding/screenshot), how-it-works, about, clinical-policy, physicians, consults, hone-at-home, and the full /mens/* + /womens/* treatment grid incl. both new heart-health pages and thyroid (24 pages total) — Firecrawl `maxAge:0`, `location:US`; WordPress (wp-content + wp-json, Cloudways); Optimizely A/B live, capture is a point-in-time snapshot.
- **Verify:** 24 pages — all sourceURLs matched, all bodies md5-unique, no junk soft-404s (clean).
- **Credits:** 25 (1 map + 1 homepage + 23 key pages).
- **Couldn't get:** server-rendered /membership-pricing detail (recovered from homepage + per-product FAQ blocks); named pharmacy/fulfillment partner (not stated); any financials/headcount (not on site).
- **Run profile:** Express fresh capture over a warm (18-day-old) base; +offerings (deep per-SKU roster), +telehealth (cohort pack), +logos. Deep roster gated on by Companies row (Direct competitor=Yes, Importance=Highest).
- **Structured layer (schema 2.6):** `socials`, `external` (trustpilot), `aliases` (alternateName "Hone"), `legal_entity` (legalName "Time Therapeutics, Inc."), `logo_url`, founding year 2021, founder Saad Alam, and address read from this capture's homepage JSON-LD via `fc.py signals` — hint-to-verify (socials cross-checked against the footer; Trustpilot rating in Credibility). `medicalSpecialty` (Endocrinology/Menopause/Andrology) noted in Overview prose, not frontmatter (per 2.2 — no `specialties` field).
- **Migrations:** none — captured fresh under 2.6.
