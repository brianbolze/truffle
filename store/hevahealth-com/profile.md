---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: hevahealth.com
name: Heva Health
aliases: [Dose, "Dose | Hormone & Longevity Center", yourheva.com]   # /clinic: "One practice. Two names." — Dose = the in-person flagship; yourheva.com = patient-app domain (dashboard.yourheva.com)
parent: []
owns: []
socials: {}                          # looked (no JSON-LD; footer carries only LegitScript + Calendly + login) — none found
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Astro marketing site; patient portal on dashboard.yourheva.com, Shopify storefront on shop.hevahealth.com. CURRENT offering pages + prices are the Astro /weight-loss, /hormones, /labs. Legacy product PDPs live at /treatments/<category>/<slug>/ (Sanity CMS) — STALE pricing (old '$99/mo Wellness Plan' model); use only for molecule attestation + clean product renders. Singular /treatment/<slug> scheme is DEAD (404). Some legacy Sanity PDPs render blank (testosterone-cypionate, dihexa = H1-only shells). 'Our Services' mega-nav is JS-rendered (absent from rawHtml/markdown) — recover from footer + /how-it-works. /hormones defaults to 'Men's Hormone Care' with a client-rendered man/woman toggle (women's view not captured). No JSON-LD on homepage. A/B: pricing is promo-laden (first-month codes SEMA1/TIRZ1, shop WELCOME10) — point-in-time."
key_pages:
  how_it_works: /how-it-works
  about: /clinic
  weight_loss: /weight-loss
  hormones: /hormones
  labs: /labs
  shop: https://shop.hevahealth.com
  get_started: /get-started
unverified_fields:
  - "Homepage hormone card reads 'From $99/mo' but the /hormones floor is '$149/mo' (Core) — the $99 appears to be the Concierge Care / Wellness membership tier (homepage FAQ + legacy PDPs), not the hormone plan floor. Reported, not reconciled."
  - "Women's hormone pricing not captured — /hormones defaults to the men's view; the man/woman toggle is client-rendered."
  - "Legacy /treatments/ PDP prices (semaglutide $149, soothing cream $85) reflect an older membership model, not current Astro plan pricing — cited as legacy."
  - "Prices/promos are a point-in-time snapshot, not fixed — first-month codes (SEMA1/TIRZ1) and shop discount (WELCOME10)."
  - "Founders, funding, headcount — not on the marketing site."

# Description — one sentence: [what they do] + [how] + [focus/differentiator].
description: "A functional-medicine telehealth clinic for men and women, delivering doctor-prescribed GLP-1 weight loss, hormone therapy (TRT/HRT), and a 91-biomarker lab panel on all-in cash-pay pricing — running protocols developed at its in-person Phoenix clinic, Dose."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint to verify; confirmed against screenshots.
logo_url: https://www.hevahealth.com/images/logo/GreenHevaLogo.svg
logos:
  wordmark: { src: "https://www.hevahealth.com/images/logo/GreenHevaLogo.svg", w: 884, h: 199 }                          # "HEVA®" geometric sans, dark-olive #39442B — hostable SVG
  logomark: { src: "https://www.google.com/s2/favicons?domain=hevahealth.com&sz=256", px: 256, transparent: false }     # "H" monogram; baked CREAM square background (composited on dark — not transparent)
  og:       { src: "https://www.hevahealth.com/og-image.png", w: 1200, h: 630 }                                          # dark-olive cover, "Vitality, refined."
brand_colors: { primary: "#39442B", accent: "#6F7F5C", background: "#FDFDF1" }  # deep olive is the dominant hue (wordmark/buttons/og); sage #6F7F5C the companion; cream ground
fonts: [PP Editorial New, Inter]     # PP Editorial New = the italic-serif headlines ("Vitality, refined."); Inter = body
color_scheme: light
design_framework: astro              # rawHtml — Astro markers; scripts are Intercom, Clarity, GTM
---

## Overview

Heva Health is a DTC functional-medicine telehealth clinic that pairs licensed-provider oversight with at-home diagnostics to deliver three front-door programs — **GLP-1 weight loss, hormone optimization (TRT/HRT), and a 91-biomarker lab panel** — to men and women nationwide, on transparent all-in cash-pay pricing. Its differentiator is a real-clinic origin story: Heva is the national telehealth arm of **Dose | Hormone & Longevity Center**, a full-service in-person practice in Phoenix, Arizona where its clinical team develops, tests, and refines every protocol before national rollout ("One practice. Two names." — /clinic). Positioning is deliberately upmarket "modern functional medicine" — root-cause, whole-patient care — set against transactional "vending-machine" telehealth.

Care is **async-first**: a questionnaire is reviewed by a licensed provider who messages a plan ("for a few treatments, a short video call is required"), then medication ships from third-party compounding-pharmacy partners. Beyond the three hero lines the practice treats a fuller spectrum (peptides, dermatology, allergy, longevity) through its concierge tier, and runs a separate Shopify supplement store.

## What they offer

Multi-product across six lines (price-visibility tokens per line; current prices from the Astro pages, legacy where noted):

- **Weight loss (GLP-1):** compounded **Semaglutide — $189/mo** (first month $149, code SEMA1) and **Tirzepatide — $339/mo** (first month $149, code TIRZ1); month-to-month or 3-/6-month plans, "longer commitments mean better value." Compounded, not FDA-approved (disclaimed). `[published]`
- **Hormone therapy (TRT/HRT):** **Core — $149/mo** (testosterone therapy or enclomiphene + anastrozole if indicated) and **Enhanced — $199/mo** (+ gonadorelin for fertility/natural-production support); for men and women; labs every 90 days + mobile phlebotomy + provider support included; 3-month minimum then cancel anytime. `[published]`
- **Lab testing:** **Core 91 Panel — $249, one-time** — 91 biomarkers across hormones, metabolism, nutrients, heart, immunity; at-home phlebotomy or walk-in; 50-page Functional Health Report; no provider consult (DIY). `[published]`
- **Concierge Care:** **$99/mo** all-in membership — four labs/yr, provider visits, and a personalized treatment plan ("medications still billed at their plan rate"); also sold as "Labs + Concierge Care" with a 45-minute provider consult in 9 states. `[partial]` (homepage FAQ; meds extra)
- **Legacy `/treatments/` Rx catalog (Sanity):** a wide à-la-carte practice behind the three hero lines — **dermatology** (11 compounded creams, $85–$249: acne, melasma, anti-aging, eye), **peptides** (7: BPC 157, dihexa, GHK-Cu, KPV, methylene blue, NMN, TB-4), **longevity** (4: glutathione, NAD+, L-carnitine, Lipo-Mino), **sexual wellness** (Bloom, Rise), and **à-la-carte hormones** (enclomiphene/Fortify, gonadorelin, sermorelin, men's/women's custom care). Index cards carry molecules + their own (older-model) prices; `/treatments/allergy` is a live-but-empty scaffold. Mostly concierge/Rx-gated. Skincare/longevity/hormones `[published]` (legacy); peptides `[on-request]`.
- **Supplements (shop.hevahealth.com):** **23 Shopify SKUs**, **$25–$169** — 12 curated "Vitamin Stacks" (Male/Female Vitality Complex, Lifespan Formula, NMN, GLP-1 Activator, Cognition Complex; "Powered by Vitaboom") + 11 first-party Heva Shop basics (creatine, whey, multivitamin, pre-workout, colostrum, tallow balm, a GLP-1 digestive aid, merch). `[published]`

Per-SKU roster + molecules in `offerings.md`.

## How it works / model

Customer journey: **online intake (questionnaire) → async provider review (message with a plan, usually within a day; short video call for a few treatments) → medication ships from a pharmacy partner → ongoing chat support + provider-reviewed refills + lab monitoring.** Everything runs from the phone/dashboard (dashboard.yourheva.com); no waiting rooms, available in all 50 states where licensed.

Money: **cash-pay, all-in.** Treatment plans bundle medication + necessary labs + provider visits into one monthly price ("billed simply, no follow-up fees"); does not bill insurance directly; most plans HSA/FSA-eligible with a superbill available for out-of-network reimbursement. Cancel anytime (hormone plans carry a 3-month minimum). Fulfillment is outsourced to **named third-party compounding pharmacies — Strive Pharmacy and Stryker Compounding Pharmacy** (503A compounded, per the legacy Rx pages); labs run through CLIA-certified labs.

## Positioning & audience

Targets health-motivated adults — **both men and women** — who want clinician-backed, data-driven optimization rather than either a primary-care clinic or lightweight "wellness" telehealth. The claimed edge is depth + legitimacy: "a real clinic, not a prescription mill," with one provider/one chart/one plan, protocols proven at the Phoenix bedside, and named board-certified clinicians. The three hero lines (weight loss, hormones, labs) are presented as co-equal "ways to start," with weight loss ordered first; the deeper sell is the full-spectrum functional-medicine practice behind them. Hormone care is structured man/woman (the /hormones hub defaults to "Men's Hormone Care" with a gender toggle), but the brand and care team explicitly serve both.

## Nav structure

```
- Our Services            (mega-nav — JS-rendered; recovered from footer + /how-it-works)
  - Weight Loss — /weight-loss            (GLP-1: Semaglutide, Tirzepatide)
  - Hormone Optimization — /hormones      (TRT/HRT: Core, Enhanced; men & women)
  - Lab Testing — /labs                   (Core 91 Panel)
  - Supplements Store — https://shop.hevahealth.com
  - (legacy treatment catalog — /treatments/<category>/<slug>/: weight-loss, hormone-replacement-therapy, peptides, dermatology)
- How It Works — /how-it-works
- About Us — /clinic                       (Heva + Dose; care team)
- Blog — /blog
- Talk to our team — https://calendly.com/krystina-hevahealth
- Member Login — /auth/login  (→ dashboard.yourheva.com)
- Get Started — /get-started
- Footer › Company: How It Works · About Us · Blog · Talk to Our Team
- Footer › Legal: Terms of Service · Privacy Policy
```

## Credibility & proof

- **LegitScript-certified:** footer seal (static.legitscript.com/seals/21223651.png) linking to LegitScript's verification page.
- **Named clinical team (/clinic):** Dr. Caroline Tade, NMD (Chief Clinical Officer — hormones, regenerative, peptides); Dr. Daniel Hall, DNP (men's health, regenerative/PRP, sexual health); Kasey Horrell, PA-C (women's health, functional medicine, allergy); Kelly Moore, FNP (hormones, thyroid, weight management). "Licensed in all 50 states."
- **Self-reported scale (verbatim, /clinic):** "3,000+ Patients Trusted," "20+ Years of Combined Clinical Experience," "Board-Certified Providers." *(self-reported — recorded, not endorsed.)*
- **Pharmacy/lab posture:** "We work with Strive Pharmacy and Stryker Compounding Pharmacy — both state-licensed specialty pharmacies"; "a licensed pharmacist verifies every prescription"; labs through CLIA-certified labs; "FDA-approved or compounded at FDA-registered, state-licensed pharmacies."
- **Clinical citations:** weight-loss page cites STEP-1 (NEJM 2021) and SURMOUNT-1 (NEJM 2022) trial outcomes with verbatim figures, plus Wegovy®/Zepbound® non-affiliation disclaimers.
- **Member testimonials:** first-name reviews on /weight-loss (Julia B., Maddie J., Luke) — testimonial presence, not third-party verified.

## Visual & brand impression

Genuinely premium and restrained — this reads like a design-led wellness brand, not a typical telehealth funnel. A sage/deep-olive palette (`#39442B` over a warm cream `#FDFDF1`) with a single dark-olive section for contrast, large italic-serif headlines in **PP Editorial New** ("Vitality, refined.") against clean Inter body copy, pill-shaped buttons, and calm, editorial lifestyle photography (soft morning light, at-home moments). Product packaging is its own asset class: dark-olive-and-silver vials/tubes (Semaglutide, Soothing cream) and cream supplement-stack boxes that all carry the wordmark — a coherent, mature identity that signals "modern functional medicine" over clinical or hype-driven competitors.

## Strategic read

The distinctive move is the **clinic-first provenance**: rather than the usual "we're a real telehealth company" claim, Heva ties itself to a named, in-person Phoenix practice (Dose) and frames the telehealth arm as that clinic's national delivery layer — a credibility bridge most DTC telehealth lacks. Two operational tells worth noting: (1) it runs on three stacks — an **Astro** marketing site, a **Sanity**-CMS legacy treatment catalog (now stale/partly broken), and a **Shopify** supplement store on a separate subdomain — suggesting a brand mid-replatform from an older "$99/mo Wellness Plan" membership model to the current all-in plan pricing; and (2) breadth far exceeds the three hero lines (peptides, dermatology, allergy, longevity, sexual health), gated behind the concierge tier — the front door is intentionally narrow, the practice behind it deliberately wide.

## Provenance

- **Pages:** homepage, /how-it-works, /clinic, /weight-loss, /hormones, /labs (current Astro); /treatments/weight-loss/semaglutide-copys, /treatments/dermatology/soothing-cream (legacy Sanity, molecule + render source); shop.hevahealth.com (Shopify catalog). All via Firecrawl (`fc.py`), location US, maxAge:0.
- **Verify:** all sourceURLs matched; all captured bodies md5-unique (no §5.1 geo/cache contamination).
- **Credits:** 16 (2 maps + 14 scrapes; includes a dead /resource/membership 404 and 2 wasted retries on the blank testosterone/dihexa Sanity shells).
- **Couldn't get:** women's hormone pricing (client-rendered toggle); the Concierge $99/mo vs hormone $149/mo discrepancy (reported in unverified_fields); legacy testosterone-cypionate + dihexa PDPs render blank (H1-only); peptide per-SKU pricing (legacy/concierge-gated).
- **Run profile:** guided — +offerings (per-SKU roster), +offerings hero product images, +logos, +telehealth cohort pack. Three hero renders promoted to captures/2026-06-04/images/.
