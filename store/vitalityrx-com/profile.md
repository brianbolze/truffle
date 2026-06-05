---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: vitalityrx.com
name: Vitality Rx
aliases: []
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/VitalityRx/
  x: https://x.com/myvitalityrx
  instagram: https://www.instagram.com/vitalityrx/
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress + Elementor marketing site on vitalityrx.com; commerce lives on a separate SPA storefront store.vitalityrx.com (kit at /test-kit, packs at /checkout/product/<Salesforce-id>, the Reboot subscription at /checkout?sku=<uuid>). Prices render ONLY at the store checkout, not on the marketing pages — scrape the store PDP to read a price. Main-domain /map is ~80% blog noise; select key pages from homepage links. Store /map returns only root (SPA, no sitemap). A 'tag.trovo-tag.com is blocked' banner (a blocked analytics tag) leaks into every markdown head — ignore it. Rx Reboot Program limited to 25 states; at-home test kit ships all 50. One vitamins page lists a duplicate store id (Brain Support Stack shares Women's Optimal Vitality's id) — likely a page copy-paste error, not a real shared SKU."
key_pages:
  pricing: /pricing/
  vitamins: /vitamins/
  fertility: /fertility/
  veterans: /veterans/
  faq: /faq/
  store_test_kit: https://store.vitalityrx.com/test-kit
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — store checkout SPA + WordPress blog modules can rotate; pack prices read only at store checkout."
  - "Vitamin-pack prices: 3 of 9 stacks captured at checkout ($69.50–$75.50/mo); the other 6 render a price at checkout but were not individually scraped this run."
  - "Compounding pharmacy: not named on the site — 'proprietary Vitality Rx compounded prescription capsule' is the only fulfillment claim; 503A/503B lane and owner not stated."
  - "Brand fonts: branding payload reported system fallbacks (SF Pro Text / Times New Roman); the real wordmark is a thin wide-tracked serif that could not be named from the capture."

# Description — one sentence
description: "A men's-health telehealth brand delivering at-home hormone testing, telemed physician consults, and a compounded enclomiphene-based capsule positioned as a safer, fertility-preserving alternative to testosterone replacement therapy."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth.
logo_url: https://vitalityrx.com/wp-content/uploads/2024/12/Sleek-Logo-Black-1.png
logos:
  wordmark: { src: "https://vitalityrx.com/wp-content/uploads/2024/12/Sleek-Logo-Black-1.png", w: 536, h: 101 }
  logomark: { src: "https://vitalityrx.com/wp-content/uploads/2024/06/cropped-VRx-180x180.png", px: 180, transparent: false }
  og:       { src: "https://vitalityrx.com/wp-content/uploads/2025/12/Sleek-Logo-Black-1-300x57-1.png", w: 1200, h: 630 }
brand_colors: { primary: "#1F1F1F", secondary: "#36444E" }  # near-black wordmark/text + a slate section; warm cream/tan product photography (branding payload hexes unreliable — #0000EE was the default link blue)
fonts: []                            # wordmark is a thin, wide-tracked serif; UI/body a system sans — no real brand font determinable (see unverified_fields)
color_scheme: light
design_framework: WordPress (Elementor)   # rawHtml: wp-content + elementor markers; commerce is a separate store.vitalityrx.com SPA
---

## Overview

Vitality Rx is a direct-to-consumer men's-health telehealth brand built around hormone optimization — branded "Hormone Longevity For The Modern Man." Its wedge is an at-home hormone test (the **Vitality Test™**, a Tasso shoulder-blood-draw kit read by a CLIA lab), followed by a telemed consult with a men's-health physician, and — if the labs qualify — a monthly **Reboot Program™**. The Reboot Program's defining position is *anti-TRT*: rather than exogenous testosterone, it prescribes a compounded oral capsule (enclomiphene citrate, DHEA, 7-Keto DHEA, progesterone, anastrozole only if needed) intended to restart the body's own testosterone production while preserving fertility. A separate à-la-carte line of doctor-formulated daily **Vitality Packs** (supplements) rounds out the catalog.

## What they offer

Flagship hormone funnel (test → consult → program) plus a companion supplement line (bold lead-in, verbatim price + visibility token):

- **The Vitality Test™:** at-home hormone test kit + telemed consult — **$149** one-time, ships all 50 states; measures 6 biomarkers (Free & Total Testosterone, LH, SHBG, Estradiol, PSA) via an FDA-cleared Tasso device, CLIA-certified lab `[published]`
- **The Reboot Program™:** $199/mo all-in monthly program — compounded Rx capsule (enclomiphene citrate · DHEA · 7-Keto DHEA · progesterone · anastrozole *only if needed*) + personalized daily vitamin packs + periodic follow-up testing & telemed; "**No hidden or additional costs**"; Rx available in 25 states only `[published]`
- **Vitality Packs (supplements):** doctor-formulated daily supplement stacks, à-la-carte monthly subscription — **$69.50–$75.50/mo** (Men's Max Vitality $74.50, Hair Support $69.50, Men's Fertility Boost $75.50); 9 stacks incl. Deep Sleep, Brain Support, Performance & Recovery, Post Op Recovery, Hangover Gone, Women's Optimal Vitality `[published]`

Per-SKU roster (prices, store keys, the molecule audit) in `offerings.md`. The telehealth cohort cuts are in `telehealth.md`.

## How it works / model

Quiz-free, test-first funnel: **(1)** order the $149 at-home Vitality Test (one-click Tasso shoulder draw, no fasting; prepaid overnight FedEx return) → **(2)** results in 5–7 business days, delivered in a free HIPAA-compliant telemed consult with a men's-health physician → **(3)** if clinically indicated, the physician prescribes the $199/mo Reboot Program (compounded capsule + daily vitamin packs + ongoing testing/consults). Revenue is subscription (monthly program / supplement packs) plus the one-time test. No insurance; HSA/FSA cards accepted. Cancel anytime, money-back guarantee, free shipping. The Rx program is limited to 25 states (AL, AZ, CA, CO, CT, FL, GA, IL, IN, MD, MI, MN, MT, NJ, NY, NC, OH, OK, PA, SC, TN, TX, VT, VA, WI); the test kit is available in all 50.

## Positioning & audience

Targets men (40–55 "andropause" framing, but also under-40 men with lifestyle-driven low T) who want to raise testosterone *without* TRT's tradeoffs. The entire site is a head-to-head argument against testosterone replacement: a recurring "Reboot Program Vs. TRT" comparison claims TRT causes dependency (100% of patients), declining sperm (55%), testicular shrinkage (20%), while enclomiphene raises testosterone 1.5–2.5x with rare side effects (headache 3%). A dedicated **Veterans** vertical (partnered with SEAL Future Foundation and Dawson's Peak) extends the same hormone-nutrition-inflammation thesis to veteran transition/TBI. Claimed wedge: "integrative" — combining holistic and conventional medicine, doctor-directed and diagnostics-backed.

## Nav structure

```
- Pricing — /pricing/
- Vitamins — /vitamins/        (the Vitality Packs supplement line)
- Veterans — /veterans/
- Fertility — /fertility/
- Learn — /#
  - Blog — /blog/
  - FAQ — /faq/
  - Media — /media/            (footer-only)
- Get Started (CTA) — https://store.vitalityrx.com/test-kit
Footer · Explore: Vitamins · Veterans · Fertility · Privacy Policy · Terms · Cancellation & Refund Policy
Footer · Reach us: Phone 323.986.6605 · Email Medstaff@vitalityrx.com · "live in select states"
```

## Credibility & proof

- **Named clinicians (verbatim, on homepage):** Dr. Mehran Movassaghi, Dr. Garrett Wdowin, Dr. Ali Afshar, Dr. Ariel Moradzadeh, Dr. Ramkishen Narayanan — "Trusted by top doctors in both traditional and naturopathic medicine."
- **Self-reported (flag self-reported):** "1,000+ Active Subscribers", "4.8/5 Average Rating", "95% [of customers] take their vitamins more consistently" (vitamins page); member testimonial claims e.g. "Total T level increased from 358 to 966 (+270%)".
- **Clinical / device proof:** at-home test uses the Tasso device ("FDA-approved device" / "FDA cleared device" per copy), results from a "CLIA certified lab with clinically validated accuracy"; supplements "third-party tested", "Certified C.L.E.A.N", produced in "FDA-registered, cGMP-certified facilities".
- **Guarantees:** "No hidden or additional costs", cancel anytime, money-back / 30-day satisfaction guarantee, free shipping.
- No LegitScript seal or pharmacy accreditation (PCAB/NABP) observed on the captured pages.

## Visual & brand impression

Clean, minimal, editorial wellness aesthetic — generous white/cream space, a thin wide-tracked uppercase serif wordmark ("VITALITY RX"), circular lifestyle photography of fit men, and warm tan/amber tones in the product renders (the translucent capsule bursting with powder; the matte-black "VITALITY TEST" kit with its red Tasso device). One dark slate/charcoal section anchors the lower page. The overall read is premium, calm, and clinical-but-approachable — closer to a longevity/biohacking brand than a discount telehealth funnel. The "VRx" monogram (logomark) sits on an opaque white square (not transparent).

## Strategic read

The whole brand is a single contrarian bet: own the "**TRT alternative**" lane. Where most men's-health telehealth either sells testosterone or routes around the category, Vitality Rx's product, copy, and comparison tables are built to convert the TRT-curious man who fears dependency/infertility — enclomiphene (a SERM) is the hero molecule precisely because it *raises* testosterone and sperm rather than suppressing them. That niche doubles as a regulatory/fulfillment simplification: no Schedule-III testosterone means a lighter controlled-substance burden than TRT competitors. Constraints to watch: the Rx is geographically narrow (25 states), the compounding pharmacy is unnamed (fulfillment opacity), and clinical claims lean heavily on self-reported member numbers and a pointed (one-sided) TRT-risk comparison.

## Provenance

- **Pages:** homepage, /pricing/, /vitamins/, /fertility/, /veterans/, /faq/ (vitalityrx.com) + store PDPs store.vitalityrx.com/test-kit, /checkout/product/{Men's Max Vitality, Hair Support, Men's Fertility Boost} — all via Firecrawl (`maxAge:0`, `location:US`, all-formats homepage + store PDPs with `--images`).
- **Verify:** all 10 scrapes — sourceURLs match, all bodies md5-unique (no §5.1 contamination).
- **Credits:** 12 (1 main map + 1 store map + homepage + 8 page/PDP scrapes).
- **Couldn't get:** 6 of 9 vitamin-pack prices (render only at the store checkout SPA; not individually scraped); compounding-pharmacy identity/lane (not stated on site); real brand fonts (system fallbacks reported).
- **Run profile:** guided — +offerings, +telehealth cohort pack, +logos, +flagship hero images (Vitality Test kit, Reboot capsule → captures/2026-06-04/images/).
- **Structured layer:** homepage JSON-LD (`HealthAndBeautyBusiness`/`Organization` "Vitality Rx") → socials seeded from page anchors (facebook/x/instagram, all verified to this entity); JSON-LD `logo` = the black wordmark → logo_url. No `sameAs` external records present.
