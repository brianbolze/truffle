---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: joinfridays.com
name: Fridays
aliases: ["Join Fridays", "Thrive Health, Inc."]   # "Join Fridays" = Vimeo/social handle; "Thrive Health, Inc." = legal entity operating Fridays (footer ©)
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/joinfridays
  tiktok: https://www.tiktok.com/@joinfridays
  facebook: https://www.facebook.com/joinfridays
  linkedin: http://linkedin.com/company/joinfridays
external:
  trustpilot: https://www.trustpilot.com/review/joinfridays.com   # review record; rating in Credibility (self-reported, varies by page)

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow (rawHtml: data-wf-*, website-files.com CDN; branding.designSystem says 'bootstrap' — ignore §5.4). Shopify checkout backend (joinfridays.myshopify.com) fronts ONLY the Merch store; the meds catalog is Webflow CMS at /products/<slug> — products.json on the main domain returns the SPA shell, not JSON, so the catalog backbone is the /map census (208 URLs) + category-hub product cards. Clinical services by OpenLoop Health (billing descriptor 'OPNLP FRIDAYS'); app + intake at app.joinfridays.com/onboarding. Spanish locale dupes at /es/* (skip). GLP-1 prices live on /pricing (a tabbed Webflow widget — markdown leaks template placeholders like '$99/mo'/'$xxx' alongside the real per-SKU cards; read the cards); longevity/TRT/microdose prices sit on their category hubs (separate PDPs NOT needed for price). Clean transparent product renders for every SKU ride homepage images[] (website-files bucket .../66c8a0fb54f84ec4a09643a1/*-noLogo-trans.webp). Heavy promo/sale A/B: perpetual 'Spring Sale 50% OFF', stackable codes (NEWYOU/NYNY/FORBES/EXPERTISE/SHOP100), rotating self-reported stats (members 75k↔115k+, Trustpilot 4.4↔4.7). No /about page — company info is footer-only. Partner-pharmacy list at /terms-conditions/#pharma."
key_pages:
  pricing: /pricing
  weight_loss: /weight-loss
  longevity: /longevity
  testosterone: /testosterone
  microdosing: /microdosing
  whats_included: /whats-included
  compounded_medications: /compounded-medications
  happy_sleep: /happy-sleep
unverified_fields:
  - "Exact per-dose prices are intake/quiz-gated (app.joinfridays.com/onboarding, not submitted); captured prices are page-stated 'starting at' floors or per-plan rates from the category hubs + /pricing."
  - "Prices/IA are a point-in-time snapshot, not fixed — perpetual promo/sale A/B (50%-off 'Spring Sale', stackable discount codes, /pricing template placeholders) + rotating self-reported stats (members 75k↔115k+, Trustpilot 4.4↔4.7, IG 33k↔40k)."
  - "Partner compounding pharmacies named only at /terms-conditions/#pharma (not captured); no owned-pharmacy claim. 503A/503B lane not stated on captured pages."

description: "A DTC telehealth brand delivering GLP-1 weight loss, longevity, testosterone, and microdosing programs through OpenLoop-network clinicians and partner compounding pharmacies, bundling medication, coaching, and labs into one monthly subscription."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against screenshot
logo_url: https://cdn.prod.website-files.com/66c8a0fb54f84ec4a09643c7/66c8a0fb54f84ec4a096448b_new-fridays-logo.png   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: "https://cdn.prod.website-files.com/66c8a0fb54f84ec4a09643c7/66c8a0fb54f84ec4a096448b_new-fridays-logo.png", w: 646, h: 201 }   # lowercase "fridays" serif, dark sage-green, transparent
  logomark: { src: "https://www.google.com/s2/favicons?domain=joinfridays.com&sz=256", px: 256, transparent: true }   # stylized green "f" on transparent bg (matches apple-touch webclip.png, also 256/transparent)
  og:       { src: "https://cdn.prod.website-files.com/66c8a0fb54f84ec4a09643c7/69a1d793e932e907fe38bccd_fridaysjourney-nologos.webp", w: 2400, h: 1260 }   # "fridays journey" lifestyle cover (no logos)
brand_colors: { primary: "#606D5B", accent: "#223A46" }   # STRAIN: sage/olive-green wordmark (#606D5B) + dark-teal footer (#223A46); program sections add green (WL) / blue (longevity) / red (TRT) accents; bg #FFFAF8
fonts: [DM Sans]   # branding body font; the "fridays" wordmark is a custom serif (display only)
color_scheme: light
design_framework: webflow   # rawHtml: data-wf-*, website-files.com
---

## Overview

Fridays (operated by **Thrive Health, Inc.**, Irvine CA) is a DTC telehealth brand built around GLP-1 weight loss and expanded into longevity, testosterone, and microdosing — a "holistic" multi-program wellness platform. The journey: a ~2–3-minute eligibility quiz → an **OpenLoop Health**–network licensed clinician reviews and, if appropriate, prescribes → medication ships from a **partner compounding pharmacy**, all wrapped in one flat monthly subscription that bundles unlimited provider visits, group + 1:1 coaching (dietitian, mental-health, fitness), Quest labs, and an insurance concierge — marketed as "one single price … no membership fees, no sign-up fees, no lab fees." Fridays owns the brand, funnel, and app; the clinical entity, pharmacy, and (for sleep) the testing hardware are all outsourced.

## What they offer

Four prescription programs (all monthly subscription, cash-pay) plus a co-branded sleep partner; bold lead-in, verbatim price + visibility token (per-SKU depth in `offerings.md`):

- **GLP-1 Weight Loss (anchor):** compounded semaglutide **"Starting at $150/mo"** (annual; "$249/mo for month-to-month plan") and compounded tirzepatide **"Starting at $240/mo"** (annual; "$359/mo … month-to-month"); brand-name **Ozempic® $1498/mo** and **Zepbound® $1828/mo** with insurance support — `[partial]` (all-in but a dose/plan-moving floor; promo floors to $117/$198)
- **Longevity:** NAD+ — injectable **$125/mo**, oral liposomal **$179/mo**, nasal spray **$229/mo**; Sermorelin **$179/mo**; MIC-B12 **$179/mo** (quarterly billing) `[published]`
- **Testosterone (TRT):** Injectable Testosterone Cypionate **$129/mo**, Oral Testosterone **$129/mo**, Enclomiphene **$169/mo** (anastrozole add-on where appropriate) `[published]`
- **GLP-1 Microdosing:** Compounded Microdose Tirzepatide **$198/month** (weekly injectable), Compounded Microdose Semaglutide **$249/month** (daily oral, 10mg) `[published]`
- **Happy Sleep (co-branded partner):** at-home sleep-apnea test via the FDA-cleared **Happy Ring** + a board-certified sleep physician — **"$396"** self-pay (was $499) / **"$0 due today"** with insurance `[published]`
- **Companions:** Fridays Meals (meal-prep, fridaysmealprep.com), Merch (joinfridays.myshopify.com), SESH™ fitness-app membership (included in plans)

## How it works / model

**Quiz → clinician → meds → subscription.** A 2–3-minute quiz (GLP-1 requires BMI ≥ 20) feeds an OpenLoop-network clinician who reviews and may prescribe; eligible patients "schedule a prescription fill with a video visit or, depending on the state, … without a video visit" (sync-default, **async where state law allows**). Medication, if prescribed, is dispensed by a partner compounding pharmacy. Revenue is a flat **monthly subscription** per program, billable monthly / quarterly / annually (annual is cheapest; a "Buy 3, get 1 free" promo bills every 4 months at a 25% discount). For compounded meds the **medication cost is included** in the program price; brand-name GLP-1s are "priced based on insurance coverage." Cancel anytime (≥ 72 hours before renewal). Card descriptor: "OPNLP FRIDAYS." Fridays is explicitly **not** the medical provider, pharmacy, or manufacturer — "Clinical services are provided by OpenLoop Health and other networks of U.S.-licensed clinicians," and "Fridays does not manufacture compounded medications."

## Positioning & audience

All-genders, GLP-1-anchored. Weight-loss and longevity messaging is gender-neutral; TRT targets men ("Is low T holding you back?"); PCOS/menopause content and the testimonial roster skew female. Fridays competes head-on with **Hims** ("$69/mo") and **Ro** ("$145/mo") on an explicit comparison chart, claiming **$0 membership fee** plus the most-bundled program — "The best GLP-1 provider in the game," "the most comprehensive GLP-1 program on the Forbes list," "Why pay more for less results?"

## Nav structure

```
- GLP-1 Pricing — /pricing
- Microdosing — /microdosing
- Longevity — /longevity
- Testosterone — /testosterone
- Merch — https://joinfridays.myshopify.com/
- Contact Us — /contact-us
- [CTA] Get Started / Login — https://app.joinfridays.com/onboarding/main-info
Footer:
- GLP-1 Weight Loss — /pricing   · Longevity — /longevity   · GLP-1 Microdosing — /microdosing
- Merch — joinfridays.myshopify.com   · Fridays Meals — fridaysmealprep.com   · Blog — /blog   · Contact — /contact-us
- Apps: Fridays Health (iOS id6751423409 · Android com.fridays.fridayshealth)
- Whitepapers (PDF): NAD+ · Semaglutide · Sermorelin · Testosterone · Tirzepatide
- Legal: Privacy · Terms & Conditions (#pharma partner-pharmacy list, #refund) · Medication Safety Information
- Socials: Facebook · TikTok · Instagram · LinkedIn
(Unlinked from main nav: Happy Sleep — /happy-sleep; products at /products/<slug>; Spanish mirror at /es/*)
```
*(Header items confirmed from homepage nav; flyouts are client-rendered — sub-paths reconstructed from the /map census + footer.)*

## Credibility & proof

- **Trustpilot (self-reported widget):** number varies by page — homepage JSON-LD "4.7 / 4000 reviews"; /pricing widget "Excellent **4.4** / **4,426** reviews"; /pricing hero "4.5 stars | 4K+ review." Flagged self-reported; links to trustpilot.com/review/joinfridays.com.
- **Scale claims (self-reported, rotating):** "**115,000+ members**" (also renders "75,000+"); "**96.8%** success rate nationwide" — defined in fine print as "recent internal fulfillment and delivery performance … does **not** represent clinical outcomes."
- **Press wall "As seen on":** Forbes Health, Bloomberg, Forbes, Healthline, WebMD, Fortune, Fast Company, The New York Times (logo wall; comparison-chart data dated "as of September 1, 2025").
- **Outcome claims (self-reported, disclaimed):** "average Fridays patient loses 9 lbs in the first month" (cohort: baseline > 175 lbs, ≈ 9.75 lbs/mo); "15.28% average body-weight reduction at 12 months (as of April 2025)." Testimonials are paid ("These Fridays members were paid for their testimonials").
- **Compliance:** HIPAA-compliant badge; compounded meds "produced in FDA-registered facilities but … not FDA-approved." No LegitScript seal observed; no named-clinician / `/physicians` page; partner pharmacies listed at /terms-conditions/#pharma.

## Visual & brand impression

Warm, optimistic consumer-wellness aesthetic — a cream/off-white base (#FFFAF8) with a sage/olive-green primary and **color-coded program sections** (green = weight loss, blue = longevity, red/maroon = testosterone). A custom lowercase serif **"fridays"** wordmark sits beside a stylized green **"f"** logomark. Imagery mixes bright real-people lifestyle photography, before/after pairs, and Vimeo testimonial videos with a striking set of **clean, isolated 3D product-vial renders** color-matched to each line (captured to `captures/2026-06-04/images/`). Design maturity is high — a polished Webflow build that reads more lifestyle-DTC than clinical — though it's blanketed in promo overlays (sale banners, stacked discount codes, "$100 OFF" pop-ups).

## Strategic read

Fridays is an **OpenLoop-powered DTC GLP-1 brand sprinting toward a multi-program platform** (weight → longevity → TRT → microdosing → sleep), monetized through an all-in subscription that folds medication cost into a coaching-heavy bundle and competes on **$0-membership transparency** against Hims/Ro. Nearly the entire stack is rented — OpenLoop for clinicians, third-party compounding pharmacies for meds, Happy Sleep for the sleep vertical, a sibling meal-prep service — so Fridays' moat is brand, funnel, and app, not clinical or pharmacy assets. The relentless promo intensity (perpetual 50%-off "sale," stackable codes, countdown urgency) reads as an aggressive paid-acquisition / CAC-driven growth play.

## Provenance

- **Pages:** 9 via Firecrawl — homepage + 8 hubs (pricing, weight-loss, longevity, testosterone, microdosing, whats-included, compounded-medications, happy-sleep) — plus the /map census (208 URLs), homepage rawHtml/branding/screenshot, and JSON-LD (`MedicalBusiness`). No `/about` exists; company identity taken from the footer.
- **Verify:** all 9 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 10 (1 map + 9 scrapes; one `/pricing` attempt errored `ConnectionRefused` and didn't bill, re-scraped).
- **Couldn't get:** exact intake-gated per-dose prices; partner-pharmacy names (/terms-conditions/#pharma not captured); enumerated supported-state list; oral-semaglutide & microdose-semaglutide standalone PDP prices.
- **Run profile:** guided — emphasis "offerings + telehealth pack + logos + product images"; all modules enabled (+telehealth, +offerings, +logos, +offerings hero-image capture).
