---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: brellohealth.com
name: Brello Health
aliases: [BrelloHealth, Brello, www.brellohealth.com]   # JSON-LD name "BrelloHealth"; site uses "Brello Health" + "Brello"
parent: []                           # operating entity not stated on the marketing site; telehealth app is packaged co.alliahealth.brello (Allia Health platform) — a vendor signal, not a confirmed corporate parent (see Overview)
owns: []
socials: {}                          # no JSON-LD sameAs; footer carries no social-profile links — only a private Facebook *group* (unlinked) and app-store badges
external: { trustpilot: "https://www.trustpilot.com/review/brellohealth.com" }   # third-party record (rating → Credibility, flagged self-embedded)

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress + WooCommerce + Elementor 4.1.1 (rawHtml: woocommerce/elementor/wp-content; generator meta names Elementor). Products live at /product/<slug>; authoritative catalog census = /product-sitemap.xml (7 products: 4 single compounded meds + 3 bundles) — the nav + homepage grid agree. PRICES ARE PROMOTIONAL/POINT-IN-TIME: PDPs show struck-through 'Original price $749 → $499' via a Deadline Funnel countdown ([deadlinefunnel] shortcode) — re-check next run. 'Starting at $X/Month' = the 3-month plan total ÷ 3; real billing is a 3-month plan charged upfront, auto-renewing 'every 10 weeks' (sermorelin: 'every 11 weeks'). MODEL IS BUY-FIRST: you pay before any intake ('No Intake Form Required Before You Pay'), then complete intake in the telehealth app (app.brellohealth.com); full refund if not approved. 2025/01 wp-content image paths are hotlink-protected (403 to bare fetch; 2026/02 'Bottle-1' renders open with a Referer). Self-reported member count is inconsistent (80,000 on homepage, 70,000 on the sermorelin PDP). /the-brello-process is image-only (thin markdown); the 3-step flow lives on the homepage + PDPs."
key_pages:
  homepage: /
  about: /about-us
  faq: /faq
  start: /start-wellness
  states: /states-we-operate-in
  weight_loss_bor: /weight-loss-bill-of-rights
  tirzepatide: /product/tirzepatide-b6
  semaglutide: /product/semaglutide-b6
  nad: /product/compounded-nad
  sermorelin: /product/compounded-sermorelin
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — PDPs run promo pricing (struck-through 'original price') under a Deadline Funnel countdown; the per-SKU numbers can flicker run-to-run."
  - "Per-SKU dose ladders / exact mg per plan — not shown before checkout (buy-first model; clinical dosing happens post-intake in the app)."
  - "Active-member count — self-reported and internally inconsistent (80,000 homepage vs 70,000 sermorelin PDP); not independently verified."
  - "Partner pharmacy name — only 'a USA-based 503A Partner Pharmacy' is stated; the pharmacy is never named."
  - "Founders / operating corporate entity — not on the marketing site (a deep-research job); the Android app id co.alliahealth.brello points at an Allia Health telehealth platform, but the entity that *operates* Brello isn't stated."

description: "A DTC telehealth brand that helps women get clinician-prescribed compounded longevity and weight-loss medications — GLP-1s, NAD+, and sermorelin — shipped from a 503A partner pharmacy on cash-pay quarterly plans with app, coaching, and community support."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # clinician telehealth + compounded prescription pharma
portfolio_shape: Flagship + companions   # GLP-1 weight loss is the clear hero (all testimonials, in every bundle); NAD+ + Sermorelin are longevity companions; bundles stack them
business_model: Subscription             # quarterly (3-month) auto-renewing plans
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against the homepage screenshot
logo_url: https://www.brellohealth.com/wp-content/uploads/2026/01/cropped-brello-logo-2026.png   # the lowercase "brello" wordmark (transparent PNG)
logos:
  wordmark: { src: "https://www.brellohealth.com/wp-content/uploads/2026/01/cropped-brello-logo-2026.png", w: 924, h: 271 }   # real on-brand "brello" wordmark, deep-indigo, transparent PNG
  logomark: { src: "https://www.google.com/s2/favicons?domain=brellohealth.com&sz=256", px: 192, transparent: false }          # navy abstract "B"/reaching-figure mark; baked WHITE background (judged on a tile — not transparent)
  # og: omitted — no og:image declared in metadata (true absence)
brand_colors: { primary: "#1C1056", accent: "#F9F8A2", secondary: "#EF3F56" }   # deep indigo (wordmark + caps), pale-yellow CTA/price badges, coral accents — verified vs screenshot
fonts: []                            # branding.fonts returned only system fallbacks (Arial/Roboto/Helvetica); real type is a custom chunky display serif (wordmark) + sans body — not reliably named, left empty
color_scheme: light
design_framework: WordPress (WooCommerce + Elementor)   # rawHtml: wp-content/woocommerce/elementor; generator meta "Elementor 4.1.1" — not the branding payload
---

## Overview

Brello Health is a DTC telehealth brand that markets **clinician-prescribed compounded "longevity medicine" to women**. The homepage states it plainly: "We help women transform their lives through clinician prescribed longevity medicine." The catalog is small and Rx-only — compounded **GLP-1s** (tirzepatide, semaglutide, both "with B6"), compounded **NAD+**, and compounded **sermorelin** — sold individually or in stacked "Longevity Protocol" bundles. The wedge is **weight loss**: every customer testimonial is a GLP-1 weight-loss story ("down 108 pounds"), and a GLP-1 sits inside all three bundles, with NAD+ and sermorelin positioned as longevity/vitality companions.

The model is unusually **buy-first**: you purchase a plan before any medical intake ("No Intake Form Required Before You Pay"), then complete a provider-reviewed questionnaire inside the Brello telehealth app (app.brellohealth.com, Android pkg `co.alliahealth.brello` — an Allia Health platform); if approved, a **USA-based 503A partner pharmacy** ships the compounded med; if not approved, you're refunded. Plans are **cash-pay**, 3-month minimum, and bundle the consult, medication, injection supplies, the Brello app, "Brello Rise" virtual fitness/nutrition classes, and a private Facebook community. Brello reports "80,000 Active Members" and a Trustpilot rating of 4.1/5 across 3,860 reviews.

## What they offer

Four single compounded medications + three bundles (all subscription, all 3-month minimum, prices verbatim + visibility token — full per-SKU roster in [`offerings.md`](offerings.md)):

- **Compounded Tirzepatide (with B6):** the dual-GIP/GLP-1 weight-loss hero — **"Starting at $166/Month"** (a 3-month plan: ~~$749~~ **$499** today, then $499 every 10 weeks) `[published]`
- **Compounded Semaglutide (with B6):** GLP-1 weight loss, the value option — **"Starting at $133/Month"** (~~$599~~ **$399**/3mo, then $399 every 10 weeks); badged "Most Popular" `[published]`
- **Compounded NAD+:** longevity/cellular-energy, "minimum (3) 1,000mg vials" — **"Starting at $79/Month"** ($239/3mo, then $239 every 10 weeks) `[published]`
- **Compounded Sermorelin:** a GH-secretagogue peptide for "focus and motivation" — **"Starting at $116/Month"** (~~$599~~ **$349**/3mo, then $349 every 11 weeks) `[published]`
- **Empowered+ (GLP-1 + NAD+):** bundle — **"From $199/month"** (Semaglutide+NAD+ $598/3mo; Tirzepatide+NAD+ $698/3mo) `[published]`
- **The Longevity Stack (GLP-1 + NAD+ + Sermorelin):** the "Most Complete" bundle — **"From $299/month"** (Semaglutide variant $897/3mo; Tirzepatide variant $997/3mo) `[published]`
- **The Metabolic Compass (GLP-1 + Lumen Metabolism Tracker):** bundle with a hardware device — **"From $166/month"** (Semaglutide+Lumen billed $499 today; Tirzepatide+Lumen $599 today); the **Lumen app renews $19.90/mo after a 90-day included trial** `[partial]`

Every medication is explicitly **compounded** (repeated FDA "compounded drugs are not FDA-approved" disclaimers); there are no FDA-brand drugs and no controlled substances in the catalog.

## How it works / model

Buy-first journey: **pick a plan → pay** (3-month minimum, charged upfront) → **complete an online intake form** inside the telehealth app → **a healthcare provider reviews** and, if you qualify, prescribes → **the 503A partner pharmacy ships** the compounded medication + syringes/needles to your door (5–7 business days where there are no shipping delays) → **ongoing support** via provider/customer service, the app (progress tracking, provider messaging), Brello Rise classes, and the Facebook community. Money is made on **recurring quarterly plan revenue** (medication included in the plan price); no separate membership fee. Refund posture: full refund if not approved; if you cancel after the provider writes a prescription, a refund "less a $50 professional services fee" within 24h of the completed review.

## Positioning & audience

Targets **women** (exclusively, in voice and imagery — beach/lifestyle photography, "for women who are done doing it alone," "some women report") seeking weight loss and "longevity" without an in-person clinic or insurance. Claimed edge is **price + support**: "Priced for out-of-pocket payers with no increase as dose goes up and no membership fee," plus the community/coaching wrapper (Brello Rise, private FB group) and an app-centric experience. It competes with the broad compounded-GLP-1 telehealth field (Hims, Ro, Henry Meds, etc.) but distinguishes on a women-only frame and a longevity/NAD+/peptide stack rather than a pure weight-loss pitch. Note: the compounded meds (GLP-1, NAD+, sermorelin) are not sex-specific — the women-only stance is an audience/marketing choice, not a clinical gate.

## Nav structure

Mega-nav recovered from rawHtml `<header>`, validated against the homepage screenshot:

```
- Explore Medications
  - Tirzepatide — /product/tirzepatide-b6
  - Semaglutide — /product/semaglutide-b6
  - NAD+ — /product/compounded-nad
  - Sermorelin — /product/compounded-sermorelin
  - Explore Our Plans — /start-wellness
- Explore Bundles
  - GLP-1, NAD+ (Empowered+) — /product/empowered-longevity-lifestyle-plan
  - GLP-1, NAD+ & Sermorelin (Longevity Stack) — /product/thrive-forward-longevity-lifestyle-plan
  - GLP-1 + Metabolism Tracker (Metabolic Compass) — /product/the-metabolic-compass-plan
- Resources
  - Help Center — intercom.help/brello-health · FAQ — /faq · App Download — /app-download · Blog — /blog · Careers (ADP)
- Contact Us — /contact-us
- About Us — /about-us
- Telehealth Login — app.brellohealth.com/login
- Let's Get Started — /start-wellness
- (footer) States We Operate In — /states-we-operate-in · Weight Loss Bill of Rights — /weight-loss-bill-of-rights · Refund Policy · Disclaimer · Telehealth Consent · Privacy Practices
```

## Credibility & proof

- **Trustpilot 4.1/5, "3,860 reviews"** — embedded TrustBox widget, repeated across pages (third-party but self-embedded; recorded, not endorsed).
- **"80,000 Active Members"** self-reported on the homepage — but the sermorelin PDP says **"70,000 Active Members,"** an internal inconsistency (flagged in `unverified_fields`).
- **Named clinicians:** provider/coach bios exist (`/health-guide/bio`, `/bio/dr-stephanie-chan`, `/bio/christian-terneus`) — a "Brello Care Team."
- **503A partner pharmacy** named only by lane ("USA based 503A Partner Pharmacy"), not by entity.
- **Compliance-forward disclaiming:** FDA "compounded drugs are not FDA-approved" notice on every page; a **Florida Weight-Loss Consumer Bill of Rights** page; telehealth-consent and controlled-substance-policy pages in the footer.
- Heavy testimonial use (weight-loss results: "down 59.1 / 62 / 108 pounds"), all "Verified Member"-tagged.

## Visual & brand impression

A warm, feminine **lifestyle-wellness** look — not a clinic. Deep-indigo (#1C1056) brand color against cream/lavender backgrounds, pale-yellow (#F9F8A2) "special price" sunburst badges, and coral accents; a chunky lowercase serif "brello" wordmark. Hero imagery is joyful women on a beach, midlife-leaning models, and clean studio renders of purple-capped compounding vials ("Compounded Tirzepatide/Semaglutide/NAD+/Sermorelin"). The build is a polished WooCommerce/Elementor storefront with marquee "EXTREMELY HIGH order volume" urgency banners, a live state-availability map, and a heavy testimonial/community emphasis. Reads as a conversion-optimized DTC funnel (countdown timers, struck-through pricing) wearing a soft, supportive, women's-wellness skin.

## Strategic read

Brello is a **compounded-GLP-1 weight-loss business wrapped in a women's-longevity narrative**. The "longevity medicine" framing (NAD+, sermorelin, the "Longevity Stack," Lumen device bundle) widens cart value and softens the GLP-1-mill perception, but the demand engine is clearly weight loss (every testimonial). Two structural tells: (1) the **buy-before-intake** flow optimizes funnel conversion over clinical-first positioning (refund-if-declined is the safety valve), and (2) the catalog is **100% compounded** — exposing it to the same FDA/503A compounded-GLP-1 regulatory risk that is reshaping this category, with no FDA-brand fallback line. The Allia Health app packaging suggests Brello runs on a third-party telehealth/pharmacy platform rather than owned infrastructure. Aggressive urgency mechanics (Deadline Funnel countdowns, "EXTREMELY HIGH volume," struck-through prices) place it at the performance-marketing end of the cohort.

## Provenance

- **Pages:** homepage (+ rawHtml/branding/images/screenshot), /about-us, /faq, /weight-loss-bill-of-rights, /the-brello-process (image-only stub), + 7 product PDPs (tirzepatide, semaglutide, nad, sermorelin, empowered-plan, thrive-forward-plan, metabolic-compass-plan) — 12 Firecrawl scrapes (`fc.py`, `maxAge:0`, `location:US`) + 1 map; catalog census cross-checked against /product-sitemap.xml.
- **Verify:** all 12 sourceURLs matched, all bodies md5-unique (clean — no geo/cache contamination).
- **Credits:** 14 Firecrawl credits (2 map calls + 12 scrapes; the 2nd map was a re-list for the full inventory, no new pages); hero-image + logo fetches were headed downloads (0 credits).
- **Couldn't get:** the partner-pharmacy name; exact per-SKU dose ladders (post-intake, buy-first); the operating corporate entity / founders (deep-research); a stable price (promo/countdown — point-in-time).
- **Run profile:** guided — +offerings.md (per-SKU roster), +offerings flagship hero renders (4 single-med vial images), +logos (2.5 module), +telehealth.md cohort pack. No emphasis steer beyond the requested modules.
- **Structured layer (schema 2.5):** read homepage JSON-LD + `<header>` via `fc.py signals` — JSON-LD `sameAs` absent (no socials/external seed); Organization `logo` was a small 205×61 PNG → superseded by the measured 924×271 header wordmark for `logo_url`/`logos.wordmark`. Trustpilot review URL → `external`. Mega-nav recovered from the `<header>` region, validated vs screenshot.
