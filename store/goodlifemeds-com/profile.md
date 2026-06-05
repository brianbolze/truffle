---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: goodlifemeds.com
name: Good Life Meds
aliases: ["Good Life", "Good Life Meds LLC"]   # "Good Life" brand voice; "Good Life Meds LLC" is the legal entity (© footer)
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/goodlifemeds/
  facebook: https://www.facebook.com/goodlifemeds/
external:
  trustpilot: https://www.trustpilot.com/review/goodlifemeds.com   # third-party review record; the rating itself is in Credibility

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow site. Products live at /products/<slug>; the 4 category hubs (/weight-loss, /daily-wellness, /sexual-health, /hair) carry NO prices — pricing is PDP-only. PDP header price widget renders split across lines ($\\n199) but greps fine. Weight-loss + daily-wellness PDPs show a flat monthly price; sexual-health + hair PDPs show a dose/tier 'Starting at $X' FLOOR (true price set in the intake quiz). Sitewide 'SUMMER30' 30%-off promo discounts every shown price (base + promo both captured). Intake/checkout = app.goodlifemeds.com; member portal = portal.goodlifemeds.com. /products/oral-semaglutide is listed in the mega-nav but returns a thin 404 — no live PDP. No A/B tool fingerprinted (Transcend handles consent only)."
key_pages:
  weight_loss: /weight-loss
  daily_wellness: /daily-wellness
  sexual_health: /sexual-health
  hair: /hair
  health_guide: /health-guide
  help_center: /help-center
  tirzepatide_pdp: /products/tirzepatide   # exemplar PDP — the repeated product-page template
unverified_fields:
  - "Prices are a point-in-time snapshot, not fixed — a sitewide 'SUMMER30' 30%-off promo discounts every shown price (base + promo both captured)."
  - "Pharmacy identity/ownership — site says it 'partners with U.S.-based, state-licensed' 503A/503B pharmacies but names no pharmacy entity; ownership not determinable (claim recorded in telehealth.md, never adjudicated)."
  - "Self-reported scale — 'Trusted by over 100K subscribers' and 'thousands of customers nationwide' are the company's own claims."
  - "Founders, founding date, legal/funding/headcount — not on the marketing site."

# Description — one sentence (~160-220 chars)
description: "A DTC telehealth brand connecting U.S. patients with licensed providers and compounding pharmacies to deliver compounded and brand-name GLP-1 weight-loss, sexual-health, hair, and daily-wellness medications online, on all-in transparent pricing."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth hybrid: clinician service + the dispensed Rx
portfolio_shape: Multi-product            # 4 co-equal lines (weight-loss / daily-wellness / sexual-health / hair)
business_model: Subscription              # auto-renewing medication subscriptions
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against screenshot
logo_url: assets/wordmark.svg             # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: assets/wordmark.svg, w: 264, h: 43 }                                                                  # "Good Life" display-serif wordmark, extracted from inline branding SVG; fill normalized to currentColor
  logomark: { src: "https://www.google.com/s2/favicons?domain=goodlifemeds.com&sz=256", px: 256, transparent: false }   # the apple-touch-icon: "Good Life" wordmark on a baked charcoal tile. Only true square monogram is a 32px "G" favicon (transparent, below the deck bar)
  og:       { src: "https://cdn.prod.website-files.com/690106919d240fb80310c681/692f49f1afb55cbab80de786_GL-open-graph.png", w: 1200, h: 630 }   # "Good Life" wordmark on charcoal
brand_colors: { primary: "#6A8360", accent: "#D2A382", background: "#FFFEF8", ink: "#222222" }   # signature hue = sage/olive green (#6A8360 — the vials + links); warm cream bg, charcoal ink. (branding 'secondary' #3898EC is the generic Webflow link blue — not brand.)
fonts: [PP Neue Montreal]                 # body sans (branding.fonts[0]); headings + wordmark use an unnamed high-contrast display serif (see Visual)
color_scheme: light
design_framework: webflow                 # rawHtml: data-wf-* ×680, website-files.com (branding.designSystem said "bootstrap" — wrong, as usual)
---

## Overview

A direct-to-consumer telehealth brand operating as **Good Life Meds LLC**. It runs a 100%-online flow — a free medical-intake questionnaire reviewed asynchronously by a state-licensed provider, then medication shipped from a partner pharmacy in 3–5 business days — across all 50 states. Four co-equal lines: **weight loss** (the anchor), **daily wellness**, **sexual health**, and **hair**. The catalog mixes compounded medications (503A/503B-made tirzepatide, semaglutide, peptides) with name-brand FDA drugs (Wegovy, Ozempic, Zepbound, Mounjaro). The pitch is convenience + price transparency: one all-in cost covering the consult, medication, and shipping, "no hidden fees" and **no required membership**.

## What they offer

Four lines, all sold as auto-renewing medication subscriptions. Per-SKU roster (26 buyable products + verbatim prices) is in [`offerings.md`](offerings.md); telehealth-specific cuts in [`telehealth.md`](telehealth.md). Family-grain here:

- **Weight loss (anchor line):** the front door. Compounded GLP-1s — **Compounded Tirzepatide "Monthly = $297"**, **Compounded Semaglutide "1 Month Supply = $199"**, **Microdose GLP-1 $149** `[published]` (no membership) — alongside name-brand pens **Wegovy $499 · Ozempic $649 · Mounjaro $1149 · Zepbound $1349** `[published]`, and the **Wegovy Pill "starting at $149/month"** which adds an **"Additional $74 membership fee required"** `[partial]`.
- **Daily wellness:** injectable longevity/performance shots — **NAD+ Injections $174**, NAD+ Nasal Spray $139, Sermorelin $149, Glutathione $149, Slim Shot $169, MIC+B12 $129, Vitamin B12 $119 (all flat monthly, no membership) `[published]`.
- **Sexual health:** ED + arousal meds for men and women — generic **Tadalafil "5mg (30 tablets) = $69"** and dose tiers `[published]`; **Sildenafil "Starting at $5/dose"**, brand **Cialis $15/dose · Viagra $95/dose**, **Ignite Strips $10/dose** (men) and **Bliss Strips $12/dose** (women, PT-141) `[partial]` (floor only — real price dose-gated); **ED Mints** chewables `[on-request]` (no price shown).
- **Hair:** regrowth for men and women — **3-in-1 topical spray "Starting at $45/month"**, **Oral Minoxidil "$30/month"**, **Finasteride "$20/month"** `[partial]` (floor only).

## How it works / model

- **Journey:** pick a treatment → free online medical-intake + health-history form → async review by a state-licensed provider → if approved, the partner pharmacy ships in **3–5 business days** in discreet packaging. No video visit surfaced (async).
- **Money:** medication **subscriptions that auto-renew** at the selected interval (monthly / quarterly / 6-month) unless cancelled before renewal. One bundled price covers **doctor consult + prescription + free/expedited shipping** — "no hidden or additional fees." If not approved, "a full refund for all cost incurred," including cancellation of any subscription selected.
- **Pricing architecture:** **no membership required** on most lines (the one exception is the Wegovy Pill's +$74 platform fee). Cash-pay only — "Insurance isn't needed." A sitewide **SUMMER30** promo (and rotating WELCOME10 / HAPPY2026 coupons) discounts the shown prices.
- **Fulfillment:** "Good Life partners with U.S.-based, state-licensed pharmacies"; compounded SKUs carry the 503A patient-specific disclaimer, and the FAQ names both **503A (state-board-licensed) and 503B (FDA-registered)** pharmacies. No pharmacy entity is named.

## Positioning & audience

Targets cost- and convenience-driven U.S. consumers who want GLP-1 weight-loss and lifestyle meds without a clinic visit or insurance — squarely in the Hims/Ro/Henry Meds compounded-GLP-1 lane. Claimed edge is **price transparency + no membership**: "Transparent pricing, no hidden fees," everything (visit, meds, shipping) in "one affordable cost." Gender-neutral overall, with explicit **for-men / for-women** splits inside sexual health and hair. Leans on **compounded affordability** ("over 90% less" than brand Cialis; generic Viagra "95% cheaper than branded") while still stocking the premium brand pens.

## Nav structure

```
- Weight Loss — /weight-loss
  - Medication: Compounded Tirzepatide — /products/tirzepatide · Compounded Semaglutide — /products/semaglutide · Microdose GLP-1 — /products/microdose-glp-1 · Oral Semaglutide — /products/oral-semaglutide (dead 404)
  - Name Brand: Wegovy Pill [new] — /products/wegovy-pill · Wegovy — /products/wegovy · Ozempic — /products/ozempic · Zepbound — /products/zepbound · Mounjaro — /products/mounjaro
- Daily Wellness — /daily-wellness
  - Daily performance: MIC+B12 — /products/mic-b12 · Vitamin B12 — /products/vitamin-b12 · Glutathione — /products/glutathione · Slim Shot — /products/slim-shot
  - Longevity: Sermorelin — /products/sermorelin · NAD+ Injections — /products/nad · NAD+ Nasal Spray — /products/nad-nasal-spray · Microdose GLP-1 — /products/microdose-glp-1
- Sexual Health — /sexual-health
  - For men: ED Mints [new] — /ed-mints · Ignite Strips — /products/ignite-strips · Tadalafil (Generic Cialis) — /products/tidalafil-generic-cialis · Sildenafil (Generic Viagra) — /products/generic-viagra
  - For women: Bliss Strips — /products/bliss-strips
- Hair — /hair
  - Medication for Men: Hair Regrowth — /products/hair-regrowth-for-men · Oral Minoxidil — /products/oral-minoxidil · Finasteride (Generic Propecia) — /products/finasteride-generic-propecia
  - Medication for Women: Hair Regrowth — /products/hair-regrowth-for-women · Oral Minoxidil — /products/oral-minoxidil
- Login — portal.goodlifemeds.com/login
- Footer: Resources (Health Guide, Help Center, BMI/TDEE/Protein/Water/Calorie calculators), Return/Shipping policy, Privacy, Terms, Telehealth Consent
```
*Brand-only ED PDPs `/products/cialis` and `/products/viagra` exist (in the map) but aren't surfaced in the mega-nav.*

## Credibility & proof

- **Trustpilot (self-embedded widget):** "Excellent — 4.5 out of 5 star rating on Trustpilot, **1,884 reviews**" (verbatim; third-party platform, rating shown via the brand's own TrustBox).
- **Self-reported scale:** "Trusted by over **100K subscribers**" and "thousands of customers nationwide" — the company's own claims, repeated in the top trust bar.
- **Trust-bar claims (every page):** "100% online process · No memberships requirements · FDA-Regulated Pharmacies · Transparent pricing, no hidden fees · Board certified physicians · US sourced ingredients."
- **Quality testing (PDPs):** every batch "fully tested in full chemistry and microbiology labs" for **Potency / Sterility (USP 797) / pH / Endotoxicity (USP 85)**, "strict compliance with cGMP regulations" — page-attested process claims.
- **Compounding disclaimer (verbatim, on Rx PDPs):** "This drug is compounded by a licensed pharmacy in accordance with Section 503A… The FDA does not review or approve compounded medications… not affiliated with, endorsed or approved by… Eli Lilly / Novo Nordisk."
- **Testimonials:** first-name customer quotes on the homepage and PDPs (e.g. "I lost 70 lbs in 10 months"). No press logos or named clinicians (no /physicians page).

## Visual & brand impression

Premium, editorial "quiet-luxury" wellness aesthetic that deliberately downplays the compounded-meds reality. Warm off-white (#FFFEF8) canvas, generous whitespace, magazine-style section numerals ("01 Weight Loss / 02 Daily Wellness"), and a high-contrast **display-serif wordmark** ("Good Life") paired with a clean grotesque body sans (PP Neue Montreal). The hero device is a set of **minimalist frosted/olive-green apothecary vials** with understated single-word labels (Tirzepatide+, Semaglutide, NAD+) and sachet/spray renders — closer to a high-end supplement or skincare line than a pharmacy. Lifestyle photography is calm, diverse, and aspirational (stretching, foam-rolling). Sage-green (#6A8360) is the signature accent against charcoal blocks. Execution is mature and consistent — design is a real differentiator versus clinical telehealth peers.

## Strategic read

- **Design-led commoditizer.** The product (compounded GLP-1 + generic ED/hair meds) is undifferentiated category-wide; Good Life's wedge is *brand + price legibility* — listing flat monthly numbers and "no membership" where peers gate prices behind quizzes and memberships. Most weight-loss and daily-wellness prices are genuinely `published`; the sexual-health/hair lines quietly revert to dose-gated "Starting at" floors.
- **GLP-1 is the engine.** Weight loss is line 01, the homepage hero (Compounded Tirzepatide, "Most Popular"), and the deepest catalog; everything else is attach/retention surface area.
- **Compounded-pharma regulatory exposure.** The whole compounded-GLP-1 model rides 503A/503B compounding under the FDA shortage framework — a live regulatory risk for the cohort; the site front-loads the disclaimers but names no pharmacy partner.
- **Copy tell:** the brand-Cialis PDP contains stray competitor boilerplate ("Hims offers access to once-a-day Cialis®") — lifted template copy, a small sign of fast catalog assembly.

## Provenance

- **Pages (32 captured, firecrawl):** homepage; 4 category hubs (weight-loss, daily-wellness, sexual-health, hair); 26 product PDPs across all four lines + the /ed-mints landing. Map (45 URLs) + homepage links drove selection; structured-layer read via `fc.py signals` (no JSON-LD present; socials from footer anchors).
- **Verify:** all 32 sourceURLs matched; all bodies md5-unique (no §5.1 geo/cache contamination). `/products/oral-semaglutide` returned a thin 404 stub (635 chars) — excluded, noted as a dead mega-nav link.
- **Credits:** 33 (1 map + 32 scrapes); hero-image fetches + logos measurement were headed downloads (0 credits).
- **Couldn't get:** pharmacy entity/ownership; founders/founding date; any insurance/HSA rail (site is cash-pay only); the true all-in price on dose-gated sexual-health/hair SKUs (intake-quiz-walled).
- **Run profile:** guided — modules: +offerings.md (per-SKU roster), +telehealth.md (cohort pack), +logos:{} (wordmark/logomark/og), +flagship product images (5 hero renders → `captures/2026-06-04/images/`).
