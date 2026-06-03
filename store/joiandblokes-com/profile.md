---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: joiandblokes.com
name: Joi + Blokes
aliases: ["Joi", "Blokes", "Joi and Blokes", "Joi+Blokes"]   # Joi = women's brand, Blokes = men's brand; one company, two consumer-facing halves
parent: []
owns: []
socials:                              # operates PARALLEL handles per platform — Joi (women) listed here; Blokes (men): facebook.com/getblokes, instagram.com/getblokes, tiktok.com/@getblokes (see Credibility)
  facebook: https://www.facebook.com/JOIwomenswellness
  instagram: https://www.instagram.com/joiwomenswellness/
  youtube: https://www.youtube.com/channel/UC-UexQLpWPuk-5j09qCuulg
  tiktok: https://www.tiktok.com/@joiwomenswellness
external:
  trustpilot: https://www.trustpilot.com/review/joiandblokes.com

# Capture meta
captured_at: 2026-06-01
capture_method: firecrawl
site_notes: "WordPress (custom theme `joiandblokes`, no WooCommerce/Elementor markers). Every page's markdown is prepended by ~60 lines of persistent cart/login/promo chrome ($0.00 line items) — strip it. Homepage is Cloudflare edge-cached (cf HIT); deep nav pages render full content only on the EXACT trailing-slash nav URL (a malformed/guessed path returns a real WordPress 404 'Not found' template). NY & NJ get different pricing via a geo modal. TRT cannot ship to AL/AR/CT/DE/GA/HI/LA/MN/MO/MS/NC/ND/OK/PA/RI/SC. Trustpilot widget embeds live review text (point-in-time). Operates dual brand social handles (joiwomenswellness / getblokes)."
key_pages:
  about: /about/
  shop_men: /shop/men/
  shop_women: /shop/women/
  trt: /shop/men/hormone-health/testosterone-replacement-therapy/
  glp1: /glp-1/
  mens_labs: /mens-labs/
  womens_labs: /womens-labs/
  schedule: /schedule/
unverified_fields:
  - "Prices, promo codes, and 'first month' intro pricing are a point-in-time snapshot, not fixed — a sitewide promo banner ('MEN'S HEALTH MONTH: 25% OFF + 65% OFF LABS, code MENSHEALTH') was live at capture, and NY/NJ see different pricing via a geo modal."
  - "Funding stage, headcount, revenue, ownership structure — not on the marketing site (deep-research job)."

description: "A DTC telehealth company running parallel men's (Blokes) and women's (Joi) brands that pair at-home diagnostic lab panels with licensed-clinician care to prescribe hormone therapy, compounded GLP-1s, peptides, and supplements nationwide."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://joiandblokes.com/wp-content/themes/joiandblokes/images/full-logo-joi-and-blokes-black.svg
brand_colors: { primary: "#BACDFF", secondary: "#176F4F", text: "#363636", background: "#E5E5E5" }   # periwinkle is the CTA/accent hue over a near-grayscale light UI; green is a secondary
fonts: [Basis Grotesque, Simula]     # Basis Grotesque (sans body/headings) + Simula (serif display)
color_scheme: light
design_framework: WordPress          # rawHtml: wp-content/wp-json/wp-includes, custom theme `joiandblokes`; no WooCommerce/Elementor
---

## Overview

Joi + Blokes is a direct-to-consumer telehealth company practicing across all 50 states, structured as two consumer-facing brands under one platform: **Blokes** (men's health) and **Joi** (women's health). It sells a "diagnostics-first" model — most journeys start with an at-home or lab-draw blood panel, followed by a licensed-clinician consult and a personalized, subscription-based treatment plan with a dedicated non-clinical health coach. Founded by husband-and-wife **Josh and Katy Whalen** (both styled "CEO"/"Founder"); per the about page, Josh built Blokes first out of his own low-testosterone experience, and Katy built Joi for women navigating perimenopause/menopause. The pitch is "Not just another telemedicine company" — functional/root-cause, preventative, longevity-oriented care with transparent pricing and no membership fees.

## What they offer

Multi-product across two audiences; therapies are monthly subscriptions, labs and supplements are one-time/recurring purchases. Prices are shown openly on catalog and product pages even for Rx items (which carry a "Lab Required" tag). Per-SKU depth defers to `offerings.md`.

- **Diagnostic lab panels (the wedge):** Complete Panel **$149** (56 biomarkers, 30-min clinician visit), Advanced Panel **$399** (71 biomarkers, full thyroid + biological age), Comprehensive Panel **$699** (110 biomarkers, 60-min visit); at-home Tasso blood test + Quest/BioReference draws, optional in-home phlebotomist **+$100**. `[published]`
- **Testosterone Replacement Therapy (Blokes):** testosterone cypionate + consults + quarterly labs, tiered by commitment — **$149/mo** (3-mo, $447 upfront) · **$129/mo** (6-mo, $774) · **$99/mo** (12-mo, $1,188); "Start now for $75." `[published]`
- **Enclomiphene (Blokes):** oral, raises natural testosterone — **$99/mo**, lab required. `[published]`
- **$1/mo hair + ED add-ons:** active TRT/Enclomiphene members can add oral sildenafil, tadalafil, finasteride, and minoxidil for **$1 each/mo** (state-restricted) — a headline differentiator vs. competitors' $20–$90/mo. `[published]`
- **Compounded GLP-1 / GLP-1·GIP (weight loss):** compounded semaglutide **$199/mo** (first month $99) and compounded tirzepatide **$299/mo** (first month $149), billed quarterly, meds included; also Liraglutide **$299/mo** and **Zepbound®** program **$99/mo billed quarterly (plus the cost of meds)** `[partial]`. GLP-1s prescribed via partner clinicians and dispensed through U.S.-licensed pharmacies. `[published]`
- **Hormone Replacement Therapy / BHRT (Joi):** customized hormone support — **from $59/mo**; plus Thyroid Care **$99/mo**. `[published]`
- **Longevity / peptides:** Sermorelin **$199/mo**, NAD+ **$150/mo**, VIP Peptide **$159/mo**, Rapamycin (Sirolimus) **$83/mo**, B12+MIC **$50/mo**, Glutathione, Low-Dose Naltrexone, Pain Cream. `[published]`
- **Sexual health:** The Mood **from $119/mo**, Oxytocin nasal spray **$159/mo**, (Joi) Scream Cream, vFit® Gold+ device. `[published]`
- **Supplements:** Levels (men) / Balance (women), Focus **$74/mo**, Sleep **$74/mo**, Smart Supplements **$149/mo**, GLP-1 Assist, Creatine **from $45/mo**, Gut Health, Thyroid Support, Hair Support. `[published]`
- **Skin care (Joi):** Luxe Skin Cream, GHK-Cu Peptide Cream, Essentials. `[published]`
- **Gear/merch & Fertility (coming soon):** branded clothing + extras; fertility teased as forthcoming.

## How it works / model

Customer journey: complete a health-history form → order a lab panel (or start a therapy) → review results with a licensed partner clinician (async or synchronous) → start a subscription treatment plan delivered to the door, with ongoing monitoring (e.g. TRT: ~6-week then quarterly labs/follow-ups) and a dedicated health coach as the primary contact. Revenue is primarily recurring therapy subscriptions plus one-time/recurring lab and supplement sales. **No membership or consultation fees** (positioned against competitors at "$129+"). Pays out-of-pocket/cash-pay; does not bill insurance directly but supports HSA/FSA (via Flex) and local-pharmacy insurance routing for estrogen/progesterone, thyroid meds, and FDA-approved GLP-1s. Compounded medications are dispensed from state-licensed pharmacies and flagged as not FDA-approved.

## Positioning & audience

B2C, targeting symptom-driven adults dismissed by conventional primary care ("your labs are normal" but you don't feel normal) — men seeking testosterone/performance/longevity (Blokes) and women navigating perimenopause/menopause/hormonal imbalance (Joi). Claimed edge: diagnostics-first + functional/root-cause care, transparent no-hidden-fee pricing, dedicated coaching, and aggressive add-on bundling ($1/mo hair+ED). On the TRT page it names competitors directly — **Maximus, Hone Health, Hims** — and contrasts on $1 add-ons and a 30–60 min clinician consult. Heavy male-performance signaling (Joe Rogan Experience guests Dan Henderson & Cameron Hanes cited as Blokes customers; Jason Khalipa and Ben Bikman, PhD as advisors).

## Nav structure

```
- Women (Joi) — /shop/women/
  - Hormone Health — /shop/women/hormone-health/
    - Hormone Replacement Therapy — /shop/women/hormone-health/hrt/
    - Thyroid Care — /shop/women/hormone-health/thyroid-care/
  - Weight Loss — /shop/women/weight-loss/
    - Zepbound — /shop/women/weight-loss/zepbound/
    - Liraglutide — /shop/women/weight-loss/liraglutide/
    - Compounded GLP-1 & GLP-1/GIP — /glp-1/
  - Sexual Health — /shop/women/sexual-health/
    - The Mood — /shop/women/sexual-health/mood/
    - (!) Scream Cream — /shop/women/sexual-health/skin-creme/
    - Oxytocin Nasal Spray — /shop/women/sexual-health/oxytocin/
    - vFit® Gold+ Device — /shop/women/sexual-health/vfit-gold-device/
  - Longevity — /shop/women/longevity/
    - NAD+, Sermorelin, B12 + MIC, Glutathione, Rapamycin (Sirolimus), VIP, Low Dose Naltrexone (LDN), Pain Cream
  - Diagnostic Labs — /shop/women/diagnostic-labs/
    - Food Sensitivity, At Home Blood Test (Tasso), Complete Hormone Panel, Advanced Panel, Comprehensive Panel
    - Compare All Labs — /womens-labs/
    - Beyond the Labs (Consultations) — /beyondthelabs/
  - Supplements — /shop/women/supplements/
    - Smart Supplements, Balance, Focus, Sleep, GLP-1 Assist, Longevity, Thyroid Support, Creatine, Sexual Performance, Hair Care, Gut Health
  - Skin Care — /shop/women/skin-care/
    - Luxe Skin Cream, GHK-Cu Peptide Skin Cream, Essentials Skin Cream
  - Fertility (coming soon) — /fertility/
- Men (Blokes) — /shop/men/
  - Hormone Health — /shop/men/hormone-health/
    - Testosterone Replacement Therapy — /shop/men/hormone-health/testosterone-replacement-therapy/
    - Enclomiphene — /shop/men/hormone-health/enclomiphene/
    - Thyroid Care — /shop/men/hormone-health/thyroid-care/
  - Weight Loss — /shop/men/weight-loss/ (Zepbound, Liraglutide, Compounded GLP-1 & GLP-1/GIP)
  - Sexual Health — /shop/men/sexual-health/ (Oxytocin Nasal Spray, The Mood)
  - Longevity — /shop/men/longevity/ (NAD+, Sermorelin, B12 + MIC, Glutathione, Rapamycin, VIP, LDN, Pain Cream)
  - Diagnostic Labs — /shop/men/diagnostic-labs/ (Food Sensitivity, At Home Blood Test, Complete/Advanced/Comprehensive Panels)
    - Compare All Labs — /mens-labs/
    - Beyond the Labs (Consultations) — /beyondthelabs/
  - Supplements — /shop/men/supplements/ (Smart Supplements, Levels, Focus, Sleep, GLP-1 Assist, Gut Health, Longevity, Thyroid Support, Hair Support, Creatine, Sexual Performance)
  - Fertility (coming soon) — /fertility/
- Gear — /gear/shop/clothing/ (Hoodies, T-Shirts, Sweatpants) · /gear/shop/extras/ (Water Bottle, Duffle Bag)
- Schedule a Consult — /schedule/
- Footer — Company: About /about/, Journal /journal/, Podcasts /podcasts/, Webinars /webinars/, Press /press/
  - Wear & Share: Gift Cards, Affiliates (Impact), Advocates (/direct-sellers-landing/)
  - Support: Contact, FAQs (joi-and-blokes.frontkb.com), Refunds, Accessibility
  - Privacy portal: privacy.joiandblokes.com; patient portal: portal.joiandblokes.com
```

## Credibility & proof

- **Trustpilot (company-displayed widget, third-party data):** "Reviews 1,335 … 4.6" out of 5.0 — embedded live on product pages, linking to trustpilot.com/review/joiandblokes.com. Recorded verbatim; third-party-sourced but self-selected for display.
- **LegitScript certified:** footer carries a LegitScript "Verify Approval" seal (id 44312975) for joiandblokes.com.
- **Press logos (self-displayed, unlinked):** Esquire, Forbes, Goop, Medium, Men's Health, Poosh, Vice, Vogue.
- **Named advisors:** Dr. Melissa Loseke DO (Medical Director), Ben Bikman PhD (scientist/research advisor), Brooke Estes DnP FNP-C (lead nurse advisor), Dr. Jaclyn Tolentino MD, Paul Reynolds PhD, Dr. Clay Moss MD, Mohit Joshipura MD (telehealth), Jocelyn Freimuth (pharmacy).
- **Provider-speed claim (self-reported, verbatim):** "1.4 [average] days … to connect with a provider at Joi + Blokes as of August 17th, 2025" vs. an industry "26" days.
- **Celebrity/influencer association:** Joe Rogan Experience guests Dan Henderson (ep 149) & Cameron Hanes (ep 2068) cited as Blokes customers; Jason Khalipa lab-testing endorsement.
- **Testimonials:** ~12 named first-person quotes on the homepage (e.g. Laurie Shifler, Megan Stoy, Joe Udell), plus live Trustpilot review snippets.

## Visual & brand impression

Clean, premium-clinical, minimalist. A near-grayscale light palette (white/#E5E5E5 fields, #363636 text) with a soft periwinkle (#BACDFF) carrying the CTAs/accents and a muted green (#176F4F) as a secondary; squared (0px-radius) buttons read modern and editorial. Sans-serif body (Basis Grotesque) paired with a Simula serif for display gives an upscale wellness-magazine feel. Hero imagery is literal and clinical — a gloved hand holding a blood-draw vial — reinforcing the diagnostics-first promise; a recurring hexagon-flower motif and a "Live longer • Feel better" marquee anchor the brand. The dual-brand split (Joi/women, Blokes/men) is handled with one shared visual system rather than two distinct looks.

## Strategic read

Near-exact structural analog to the Teleprescribe venture's model: cash-pay DTC telehealth, diagnostics-first, routing compounded prescriptions (TRT, GLP-1s, peptides) through licensed clinicians and compounding pharmacies — but with two differentiators worth studying. (1) **Dual-gender brand architecture** (Blokes + Joi) doubles the addressable market off one platform/clinical/pharmacy backend, with the men's side clearly the performance-marketing engine (Rogan, Khalipa, Bikman). (2) **The $1/mo hair+ED add-on** is an aggressive retention/LTV lever explicitly weaponized against Hims/Hone/Maximus — near-free adjacent scripts that lock in the TRT subscription. They also lead with labs as a low-friction $149 entry wedge and bundle "no membership fee" against competitors charging $129+. The compounded-GLP-1 + dispense-via-licensed-pharmacy language mirrors the venture's intended Meta Pharmacy routing almost verbatim — a useful template for both copy posture (FDA-disclaimer handling, state restrictions) and unit economics.

## Provenance

- **Pages:** 8 captured via Firecrawl (firecrawl, basic proxy, maxAge:0, US geo) — homepage + about, shop/men, shop/women, TRT product, men's-labs, glp-1 (rich); shop/men/weight-loss returned thin (1,442 chars, mostly chrome — its offerings are covered by the catalog + glp-1 pages). Women's-labs not separately scraped (mirrors men's-labs). Enrichment also read the homepage `branding` payload, the full-page screenshot, and `rawHtml` JSON-LD + nav (`fc.py signals`).
- **Verify:** all 8 sourceURLs matched; all body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 9 (1 map + 1 homepage + 7 key pages) for this profile. NOTE: an earlier run wasted 7 credits on malformed URLs (a `"<url> <name>"` arg-splitting bug sent a literal space in the path → genuine WordPress 404s); those captures were discarded and re-scraped. True session spend: 16 credits.
- **Structured layer:** JSON-LD Organization confirmed name "Joi + Blokes", logo (square jb-logo-schema.png — but on-domain SVG wordmark kept as `logo_url` per real-brand-mark rule), and `sameAs` socials (dual handles per platform). No `alternateName`/`legalName`; founders taken from about-page prose, not frontmatter.
- **Couldn't get:** corporate/legal entity name, ownership/funding, headcount, the legacy "Blokes"→"Joi + Blokes" timeline (getblokes handle predates the combined brand — likely Blokes was the original company, unconfirmed). Per-state pricing variants (NY/NJ) not enumerated.
