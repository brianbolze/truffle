---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: therabody.com
name: Therabody
aliases: []
legal_entity: "Therabody, Inc."   # PDP footnote names "Therabody, Inc." as ThermBack LED trial sponsor; site-derived.
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/therabody/
  facebook: https://www.facebook.com/therabody/
  x: https://twitter.com/therabody
  youtube: https://www.youtube.com/@Therabody
external: {}

# Capture meta
captured_at: 2026-06-24
capture_method: firecrawl
site_notes: "Shopify storefront (cdn.shopify.com; powered-by Shopify). Catalog breadth lives in collection pages: /collections/shop-all, family collections, /collections/bundles, and /collections/shop-accessories; /map also returns many color/size/refurbished variants and blog/support noise. A/B: Optimizely. Product prices and IA are a point-in-time snapshot, not fixed -- capture was during a Prime Day sale banner, with sale prices on many product cards. Every cleaned page has trailing ERR_BLOCKED_BY_CLIENT overlay text for www.therabody.com and a4544552325873664.cdn.optimizely.com; ignore it below the footer. Python logo fetches failed from the sandbox; the wordmark SVG was measured via curl from the homepage JSON-LD/branding URL."
key_pages:
  home: /
  shop_all: /collections/shop-all
  theragun: /collections/shop-theragun
  jetboots: /collections/shop-jetboots
  therm_series: /collections/shop-therm-series
  recoverypulse: /collections/shop-recoverypulse
  theraface: /collections/shop-theraface
  accessories: /collections/shop-accessories
  bundles: /collections/bundles
  science: /pages/science
  coach: /pages/coach
  reset: /pages/reset
  hsa_fsa: /pages/hsa-fsa-eligibility
  b2b_contact: /pages/b2b-contact
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed -- Prime Day sale pricing and Optimizely were active during capture."
  - "Reset by Therabody service pricing -- appointment-booking flow, not published on the captured page."
  - "Corporate/B2B pricing -- form-gated; corporate gifting page says exclusive corporate pricing is provided after inquiry."
  - "Founding date and full corporate history -- not captured on the current marketing pages."

description: "Makes app-connected wellness hardware for recovery, pain relief, sleep, and skincare, spanning Theragun massage guns, compression boots, thermotherapy, LED masks, rollers, and Reset/B2B services."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Physical Products / Hardware, Services / Consulting]
portfolio_shape: Catalog
business_model: Transactional / One-time
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: "https://www.therabody.com/cdn/shop/files/Therabody_Logo_d8775086-0719-4681-8ad1-61429f50ffe9.svg?v=1733528062&width=500"
logos:
  wordmark: { src: "https://www.therabody.com/cdn/shop/files/Therabody_Logo_d8775086-0719-4681-8ad1-61429f50ffe9.svg?v=1733528062&width=500", w: 159, h: 33 }
brand_colors: { primary: "#252525", accent: "#B03730", background: "#FFFCF5" }
fonts: ["Suisse Intl", "ABC Arizona Text Variable"]
color_scheme: light
design_framework: shopify             # rawHtml/header: cdn.shopify.com + Shopify checkout/storefront markers; branding.designSystem ignored.
---

## Overview

Therabody is a wellness-technology company built around app-connected physical devices for recovery, pain relief, sleep, stress, and skincare. Its current U.S. storefront is a broad Shopify catalog: Theragun massage guns, JetBoots compression boots, RecoveryPulse sleeves, Therm Series heat/cold devices, Wave rollers, SmartGoggles, SleepMask, TheraFace skincare devices, TheraCup, PowerDot pads, accessories, and bundles. The site also sells around the devices through Coach by Therabody in the app, Reset by Therabody in-person wellness services, HSA/FSA checkout, corporate gifting, and broader business/commercial inquiries.

## What they offer

Per-product roster in [`offerings.md`](offerings.md). Family lines below use captured sale/card prices where shown; many cards displayed strike-through regular pricing during this point-in-time sale capture.

- **Theragun massage guns:** Relief, Mini, Prime, Sense, Mini Plus, Prime Plus, PRO, and PRO Plus; captured sale/card prices span **$99.99** to **$549.99** `[published]`
- **JetBoots compression boots:** JetBoots Prime and JetBoots PRO Plus; captured card prices **$439.99** and **$899.99** `[published]`
- **Therm Series / hot-cold recovery:** CryoTherm Palm, ThermBack LED, RecoveryTherm Knee, and RecoveryTherm Cube; captured card prices span **$159.99** to **$449.99** `[published]`
- **RecoveryPulse sleeves:** arm and calf compression/vibration sleeves; captured card price **$89.99** `[published]`
- **Wave Series rollers:** WaveSolo, WaveDuo, and WaveRoller; captured card prices **$99.99**, **$119.99**, and **$179.99** `[published]`
- **Sleep and stress devices:** SmartGoggles and SleepMask; captured card prices **$169.99** and **$84.99** `[published]`
- **TheraFace skincare devices:** Mask Glo, Mask, PRO, and Depuffing Wand; captured card prices span **$129.99** to **$599.99** `[published]`
- **Cupping, PowerDot pads, accessories, and bundles:** TheraCup, PowerDot replacement pads, Theragun/TheraFace accessories, and five bundles; captured bundle prices span **$234.99** to **$1,249.99** `[published]`
- **Coach by Therabody:** AI-driven recovery plans in the Therabody app, with wearable syncing and expert-designed routines for compatible Theragun devices; price not shown as a standalone paid product `[on-request]`
- **Reset by Therabody:** in-person services such as Theragun Massage, cryotherapy, red light therapy beds, hyperbaric oxygen, pneumatic compression, TheraFace Facial, and infrared sauna at the captured Los Angeles location; service prices not published `[on-request]`
- **Corporate / commercial programs:** corporate gifting with "exclusive corporate pricing" after form inquiry, plus a business-inquiries form for gyms, hotels, spas, retailers, distributors, sports teams, and other commercial channels `[on-request]`

## How it works / model

Therabody's core model is direct product commerce: users choose devices by product family or use-case collection, add to cart, and checkout on Shopify with options including HSA/FSA via Flex, Afterpay, and Klarna. Many device PDPs label products as HSA/FSA Accepted or FDA Registered/Cleared, and the HSA/FSA page tells customers to choose "Flex | Pay with HSA/FSA" or use Flex for reimbursement documentation. The app layer extends device use: Coach by Therabody creates personalized recovery plans from fitness goals, activity data, wearables such as Garmin, Apple Health, Strava, or Google Fit, and Theragun session data. B2B demand routes through corporate gifting and a business-inquiries form rather than published bulk pricing.

## Positioning & audience

The site targets health-conscious consumers, athletes, active adults, people managing aches/pain/sleep/stress, and skincare buyers who want "science-backed technology" rather than generic wellness accessories. Therabody frames the products around outcomes: pain relief, better sleep, faster recovery, peak performance, radiance, and clinical validation. The B2B copy broadens the buyer to gyms, hotels, spas, retailers, distributors, teams, and corporate wellness/gifting programs.

## Nav structure

```
- Shop
  - Enhance Fitness & Recovery
    - Full-Body Heated Massage: Theragun Prime Plus, Theragun PRO Plus
    - Full-Body Deep Massage: Theragun Prime, Theragun PRO
    - Portable Heated Massage: Theragun Mini Plus
    - Wireless Leg Compression: JetBoots Prime, JetBoots PRO Plus
    - Palm Cooling: CryoTherm Palm
    - Vibrating Muscle Rollers: WaveSolo, WaveDuo, WaveRoller
    - Compression Sleeves: RecoveryPulse Arm, RecoveryPulse Calf
  - Reduce Aches & Pains
    - Full-Body Gentle Massage: Theragun Sense, Theragun Relief
    - Portable Massage: Theragun Mini
    - Hot & Cold Wearables: ThermBack LED, RecoveryTherm Cube, RecoveryTherm Knee
    - Heated Cupping: TheraCup
  - Improve Sleep & Stress
    - Eye & Temple Massage: SmartGoggles
    - Blackout Sleep Mask: SleepMask
  - Clinically Proven Skincare
    - Red Light LED Masks: TheraFace Mask Glo, TheraFace Mask
    - Complete Facial Care: TheraFace PRO
    - Portable Facial Depuffing: TheraFace Depuffing Wand
  - Shop Sale, Shop All, Best Sellers, Bundle & Save, Accessories, Product Finder Quiz
- Explore: Product Finder Quiz, For Fitness & Recovery, For Aches & Pains, For Sleep & Stress, For Beauty
- Learn: Therabody App, Our Science, Coach by Therabody, Blog
- Gifts: Gift Guide, Gift Finder Quiz
- Footer: HSA/FSA, Returns, Warranty, Product Registration, Reset by Therabody, Our Science, Reviews, Professional Education, Corporate Gifting, Business Inquiries
```

## Credibility & proof

- **Research program (self-reported):** Science page claims **"46 completed scientific studies"**, **"17 peer-reviewed published studies"**, and **"75,000+ studies support"** the treatment modalities in Therabody products.
- **Scientific staff/advisory board:** site names Chief Science Officer Tim Roberts, Head of Science Research and Communication Dr. Rachelle Reed, and advisory board members Dr. Daniel Giordano, Dr. Dhaval Bhanusali, Dr. Pamela Peeke, and Dr. Robin Thorpe.
- **Category proof claims:** Science page says Theragun studies show improved mobility, reduced pain, increased blood flow, delayed fatigue, and improved muscular performance; JetBoots studies show improved cardiovascular recovery; SmartGoggles and SleepMask studies report sleep improvements; ThermBack LED is "clinically proven to reduce lower back pain"; TheraFace PRO lists 91% / 97% / 83% study outcomes for eye wrinkles and skin elasticity.
- **Regulatory/payment cues:** multiple captured PDPs show HSA/FSA Accepted and FDA Registered or FDA Cleared badges; HSA/FSA page says Therabody partnered with Flex for eligible product checkout.
- **Customer proof:** product cards and PDPs carry visible star/review modules, for example PRO Plus based on 173 reviews, SmartGoggles based on 130 reviews, TheraFace Mask Glo based on 135 reviews, and TheraCup based on 53 reviews.

## Visual & brand impression

Premium consumer-health hardware with a warm clinical tone. The UI uses a light cream/off-white canvas, near-black text and buttons, muted red accents, soft rounded cards, polished product renders, and lifestyle/device photography. The typography pairs compact Swiss-style sans text (Suisse Intl in the branding payload) with an editorial display face (ABC Arizona Text Variable), giving the site a more refined wellness/beauty feel than a hard sports-equipment store. The first viewport during capture was promotion-led ("Prime Day Sale | Save up to 40% off"), but the broader system reads as mature DTC wellness commerce.

## Strategic read

Therabody is no longer just a Theragun company in the storefront. Theragun remains the anchor and the app/Coach layer is built most tightly around Theragun routines, but the catalog has expanded into adjacent modalities: compression, hot/cold therapy, LED and microcurrent skincare, sleep/stress, cupping, rollers, and in-person recovery services. The strategic throughline is owning the recovery/wellness routine across home devices, app guidance, and professional settings, with "science-backed" evidence and HSA/FSA eligibility used to pull the brand away from commodity massage-gun positioning.

## Provenance

- **Pages:** homepage, map, shop-all, Theragun, JetBoots, Therm Series, RecoveryPulse, Wave Series, TheraFace, SmartGoggles, SleepMask, TheraCup, PowerDot, accessories, bundles, 14 representative PDPs, science, Coach, Reset, HSA/FSA, corporate gifting, B2B contact -- 35 Firecrawl pages total, 2026-06-24, US geo, full-page screenshots.
- **Verify:** all 35 sourceURLs matched, all bodies md5-unique, no junk soft-404s. One TheraCup PDP initially returned a thin 503 shell and was successfully re-scraped with enhanced proxy.
- **Credits:** see `fc.py spend`; capture included 1 map, 1 homepage, 33 scrape calls, with one enhanced-proxy retry.
- **Couldn't get:** Reset service prices; corporate/B2B pricing; complete color/size/refurbished variant census beyond the current indexed product/family collection level; founding date/full corporate history from first-party pages.
- **Run profile:** express -- standard profile + per-SKU/category `offerings.md`; no flagship image capture.
