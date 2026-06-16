---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: altrx.com
name: altRx
aliases: []
legal_entity: ""                     # site states no registered legalName; care delivered via affiliated PCs (CareGLP Affiliated P.C.s, CareValidate Health) — see Overview
parent: []
owns: []
socials: {}                          # footer social icons link to bare facebook.com / instagram.com / linkedin.com / x.com (no handle) — placeholders, none operated-and-verifiable
external: {}

# Capture meta
captured_at: 2026-06-16
capture_method: firecrawl
site_notes: "Nuxt.js SPA (rawHtml __NUXT__; branding payload mislabels framework as 'tailwind'). A/B: yes — pricing is promo-driven: homepage cards + product pages render a SPRING promo ($89 / $129) while <meta> + JSON-LD carry different figures ($159 / $279) — point-in-time, not fixed. Real wordmark at /assets/altrx-logo.svg; JSON-LD `logo` is the OG image (alt-og.png) — do NOT use it. Products mega-nav is JS (flattened in markdown) — recover flyout from /products/* map URLs + homepage cards. Spanish locale mirrored under /es/. Map returns 83 URLs incl. many /glp1/offer-v9* funnel landers, /v2-* and /take-the-quiz* variants — noise, skip."
key_pages:
  homepage: /
  about: /about
  semaglutide: /products/compounded-semaglutide
  tirzepatide: /products/compounded-tirzepatide
  contact: /contact
  consultation: /consultation
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — active SPRING promo ($89 / $129 rendered) vs. meta/JSON-LD list prices ($159 / $279); brand-name med floors ($1149–$1579/mo) are likewise promo-sensitive."
  - "Final all-in program price is gated behind the /consultation eval — not submitted."
  - "Products flyout contents inferred from /products/* map URLs + homepage cards (markdown flattened the JS dropdown)."
  - "Founding date, headcount, ownership, and registered legal entity — not stated on the captured pages."

description: "A DTC telehealth brand selling compounded GLP-1 (semaglutide) and GLP-1/GIP (tirzepatide) weight-loss injections on cash-pay monthly plans, via a 2-minute online eval, clinician review, and home delivery to all 50 states."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint, verified against screenshot
logo_url: https://www.altrx.com/assets/altrx-logo.svg
brand_colors: { primary: "#C6EC87", background: "#FAF8F4" }   # lime-green accent on warm-cream ground; confirmed vs. homepage screenshot
fonts: [Geist]
color_scheme: light
design_framework: nuxt.js
---

## Overview

altRx is a direct-to-consumer telehealth weight-loss brand built around a single promise: the cheapest GLP-1 program. It sells compounded semaglutide and tirzepatide injections — plus brand-name GLP-1s (Zepbound, Mounjaro, Wegovy, Ozempic) — on a self-pay monthly model: a free 2-minute online evaluation, licensed-clinician review, and home delivery to all 50 states. Medical care is delivered through affiliated professional corporations (CareGLP Affiliated P.C.s and CareValidate Health), and medications are filled by partner compounding pharmacies. The positioning is explicit and price-first: *"GLP-1s have already proven to work. We fixed what didn't: the price."*

## What they offer

All offerings are GLP-1 weight-loss medications; the two compounded molecules are the price-story heroes, the four brand-name meds are premium alternatives. Program price bundles consult + prescription + shipping; Buy Now Pay Later offered.

- **Compounded GLP-1 (semaglutide):** once-weekly subcutaneous injection — **"$89/mo"** (homepage card *"Starting at $199/mo $89/mo"*; meta/JSON-LD list *"$159/mo"*) `[published]`
- **Compounded GLP-1 / GIP (tirzepatide):** dual-action once-weekly injection — **"$129/mo"** (card *"Starting at $299/mo $129/mo"*; meta/JSON-LD *"$279/mo"*) `[published]`
- **Zepbound (brand-name):** injection — **"Starting at $1249/mo"** `[published]`
- **Mounjaro (brand-name):** injection — **"Starting at $1249/mo"** `[published]`
- **Wegovy (brand-name):** injection — **"Starting at $1579/mo"** `[published]`
- **Ozempic (brand-name):** injection — **"Starting at $1149/mo"** `[published]`

Hero/promo banner: *"SPRING Promo! Only $89 + Fast, Free Shipping"* and *"The #1 most affordable GLP-1 program, from just $89."*

## How it works / model

- **Journey:** free 2-minute online evaluation → licensed clinician reviews intake and prescribes if appropriate → medication ships to the door. Full flow *"typically takes ~2–3 weeks."*
- **Money:** self-pay, *"Insurance is not required"*; recurring monthly plan; free shipping (5–7 days); Buy Now Pay Later available. Pricing claimed to include consult, prescription, and delivery with *"no hidden fees."*
- **Eligibility:** 18+; serviced in *"all 50 states."*
- **Supply chain:** compounded in an *"FDA-registered, 503A-compliant facility"* under *"USP <797>"* cleanroom conditions; the site states compounded GLP-1s are *"not FDA-approved or evaluated for safety, efficacy, or quality."*
- **Clinical/pharmacy layer:** medical treatment by **CareGLP Affiliated P.C.s** and **CareValidate Health** (affiliated networks of medical PCs; CareValidate sets exclusionary criteria and its clinicians retain sole prescribing discretion). Partner pharmacies: **Belmar Pharmacy, Strive Pharmacy, Epiq Scripts, Casa Pharma Rx.**
- **Support:** patient portal at care.altrx.com; help@altrx.com (≤48h, non-urgent); (321) 641-0765.

## Positioning & audience

Targets cost-sensitive US adults who want GLP-1 weight loss without insurance or in-person clinics. The single claimed edge is price + transparency — undercutting both traditional care and pricier telehealth. Branding tone reads "modern," audience "health-conscious individuals." Competes in the crowded compounded-GLP-1 telehealth field (Hims/Ro/Mochi-adjacent) primarily on the dollar figure.

## Nav structure

```
- Home — /
- Products  (JS flyout — contents from /products/* + homepage cards)
  - Compounded GLP-1 (semaglutide) — /products/compounded-semaglutide
  - Compounded GLP-1 / GIP (tirzepatide) — /products/compounded-tirzepatide
  - Zepbound — /products/zepbound
  - Mounjaro — /products/mounjaro
  - Wegovy — /products/wegovy
  - Ozempic — /products/ozempic
- About — /about
- Contact — /contact
- Blogs — /blogs
- [utility] Get Started — /consultation · Log in — care.altrx.com/login
- [locale] Spanish mirror — /es/...
```

## Credibility & proof

- **Press strip ("Recognized by"):** Fortune, Fast Company, Bloomberg, Healthline, Forbes, WebMD — logos only, no linked coverage (self-presented; treat as unverified).
- **Certifications/badges:** LegitScript Certified (links to the LegitScript lookup for altrx.com), HIPAA Compliant, Made in USA.
- **Self-reported scale/outcome claims (verbatim, self-reported):** *"Trusted by thousands"*; *"Over 10 million people can't be wrong"*; program to *"lose 15% of your body weight"*; *"altRx patients typically experience 1-2 lbs per week weight loss after 4 weeks."*
- **Cited clinical claims (verbatim):** semaglutide patients *"lost an average of 12–15% of their body weight over 68 weeks"*; tirzepatide users *"lost an average of 15–22% of body weight versus 12–15% with semaglutide."*
- **Testimonials:** UGC-style testimonial videos + named text quotes; disclaimer present — *"Some testimonials on this site are of paid endorsers. Individual results may vary."*

## Visual & brand impression

Clean, modern DTC-telehealth aesthetic: warm-cream ground, lime-green (#C6EC87) accents, rounded product cards, and lifestyle photography of smiling, relatable people interspersed with UGC testimonial video thumbnails. Competent and firmly on-trend for the category, but heavily templated and funnel-driven (multiple A/B landers, repeated *"Take the 2-Minute Quiz"* CTAs, press/trust badges foregrounded). Polished and credible-looking, not distinctive — the design defers entirely to the price message.

## Strategic read

The entire brand is a price-leader play on an increasingly commoditized compounded-GLP-1 market — the moat is thin (cheap pricing + multi-pharmacy fulfillment, no proprietary molecule or clinical IP). Two structural risks the capture surfaces: (1) the business rides **compounded** semaglutide/tirzepatide, whose legality hinges on FDA shortage-list status — a regulatory shift can remove the core SKUs; (2) heavy reliance on funnel/promo mechanics (SPRING promo, A/B landers, "from $89" everywhere) over durable differentiation. Press logos and "10 million people" claims are unsubstantiated on-page, consistent with an acquisition-first, performance-marketing posture.

## Provenance

- **Pages:** homepage, /about, /products/compounded-semaglutide, /products/compounded-tirzepatide, /contact (5 pages) + site map — Firecrawl, location US, maxAge:0.
- **Verify:** all sourceURLs matched; all page bodies md5-unique; no junk soft-404s.
- **Credits:** 6 (1 map + 1 homepage + 4 key pages).
- **Couldn't get:** final all-in program price (behind /consultation eval, not submitted); founding date / ownership / registered legal entity (not stated on site); Products flyout contents (JS nav — inferred from /products/* + homepage cards).
