---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: prohealth.com
name: ProHealth Longevity
aliases: ["ProHealth", "ProHealth, Inc.", "ProHealth Nutritional Supplements", "prohealth-longevity.myshopify.com"]
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/ProHealthLongevity/
  x: https://twitter.com/PHLongevity
  instagram: https://www.instagram.com/prohealthlongevity/
  pinterest: https://www.pinterest.com/ProHealthLongevity/
  youtube: https://www.youtube.com/channel/UCulo3enQ4yRU2VcwIEgzLxg
external:
  bbb: https://www.bbb.org/us/ca/carpinteria/profile/vitamins-and-supplements/prohealth-nutritional-supplements-1236-10000243

# Capture meta
captured_at: 2026-06-07
capture_method: firecrawl
site_notes: "Shopify (prohealth-longevity.myshopify.com; Rebuy upsell, ReCharge subscriptions, Glopal intl proxy). Collection-grid prices LAZY-LOAD — not in markdown; verbatim $ only on PDPs + the Rebuy 'you may also like' widget. Compounded-Rx arm lives off-store: rx.prohealth.com (Rx login) + rxcheckout.prohealth.com/start-online-visit/<rxNN> (async quiz → Beluga Health provider → compounding pharmacy). Wholesale on wholesale.prohealth.com. Footer carries Glopal country-selector noise + a 'shop.app blocked by client' stub — both capture artifacts, ignore."
key_pages:
  shop_all: /collections/all
  nad_boosters: /collections/nad
  pharmaceuticals: /collections/pharmaceuticals
  at_home_tests: /collections/testing
  longevity_experts: /pages/longevity-experts
  our_story: /pages/our-story
  faq: /pages/faq
  rx_portal: https://rx.prohealth.com/login
unverified_fields:
  - "Catalog prices — collection grids lazy-load; only exemplar PDP/widget prices captured ($64.95, $58.46, $42.95, $119.95). Most of the ~hundreds-of-SKU catalog is unpriced in this capture."
  - "Partner pharmacy name — FAQ 'Partner Pharmacy Information' accordion did not expand in capture; pharmacy stated 'US-licensed / FDA-regulated US-based' but unnamed."
  - "Payment rails (HSA/FSA/insurance) — no payer copy captured; standard card checkout assumed but not page-stated."

# Description — one sentence
description: "A longevity-focused supplement company that makes and sells NMN, NAD+ boosters, and anti-aging nutraceuticals direct-to-consumer, with a newer compounded-Rx telehealth arm (GLP-1, peptides, metformin) fulfilled via third-party providers and a compounding pharmacy."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B]            # primary DTC e-commerce; secondary B2B (wholesale.prohealth.com + healthcare-partner program)
offering_category: [Consumer Packaged Goods (CPG), Biotech / Pharma Products]   # own-brand supplements (primary) + compounded Rx (secondary); also resells some 3rd-party brands
portfolio_shape: Catalog
business_model: Transactional / One-time    # e-commerce purchase; Subscribe & Save (ReCharge autoship, up to 30% off) is the recurring secondary
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://www.prohealth.com/cdn/shop/files/Prohealth-logo-v_64fa65b2-df23-4554-886f-c374e8dc1f60_1445x.png?v=1702253638
logos:
  wordmark: { src: "https://www.prohealth.com/cdn/shop/files/Prohealth-logo-v_64fa65b2-df23-4554-886f-c374e8dc1f60_1445x.png?v=1702253638", w: 278, h: 69 }   # white "ProHealth.com" + rainbow underline, reversed for the dark navy header — transparent
  logomark: { src: "https://www.google.com/s2/favicons?domain=prohealth.com&sz=256", px: 32, transparent: true }   # "ph" monogram, navy on transparent; small (sz=256 served 32px)
  og:       { src: "http://www.prohealth.com/cdn/shop/files/PH_Logo_Full_Blue_Shopify_1200x1200.png?v=1700239368", w: 1200, h: 600 }   # full blue ProHealth wordmark on white
brand_colors: { primary: "#08192A", secondary: "#113B8C", accent: "#1A80C1" }   # deep navy ground + science-blue accents; verified against the dark navy homepage hero
fonts: [Poppins, ITC Avant Garde Gothic Std]   # Poppins body, ITC Avant Garde Gothic headings
color_scheme: light            # white commerce surfaces (collections/PDP/cart); the homepage hero band is a dark-navy photo treatment (see Visual)
design_framework: shopify      # cdn.shopify.com, prohealth-longevity.myshopify.com — read from rawHtml/links
---

## Overview

ProHealth Longevity is the anti-aging arm of **ProHealth, Inc.**, a Carpinteria, CA supplement company founded in 1988 by **Rich Carson** after his own diagnosis with ME/CFS. The original business sold purity-first supplements to chronic-illness patient communities (ME/CFS, fibromyalgia, Lyme) under the motto *"Commerce with Compassion"*; after ~30 years it extended into longevity science, and **ProHealth Longevity** is the consumer-facing brand today. The catalog spans hundreds of SKUs — a hero NAD+/NMN line (own-brand **Uthever® NMN**), a broad nutraceutical catalog across ~40 health categories, at-home lab tests, and a newer **compounded-pharmaceutical / telehealth arm** (GLP-1, peptides, NAD+ injectables) sold cash-pay via an online medical visit. It both *makes* its own products and *resells* select third-party brands.

## What they offer

Catalog-shape — hundreds of SKUs; the families below are the shape, per-SKU depth lives in `offerings.md`:

- **NAD+ boosters (hero line):** NMN, NR, NMNH, NADH — anchored on **Uthever® NMN** (NMN Pro 1000 **$64.95** one-time / $58.46 Subscribe & Save) `[published]`
- **Compounded pharmaceuticals / Rx (telehealth):** **Personalized GLP-1 Injection** (semaglutide/tirzepatide), Compounded Sermorelin, NAD+ Injection, NAD+ Nasal Spray, Metformin, Methylene Blue — quiz → licensed-provider visit → compounding pharmacy; **price behind the free consult** `[on-request]`
- **Peptides / specialty (OTC):** Pure BPC-157 (**$119.95**, sold as a 500 mcg capsule) `[published]`
- **Broad nutraceutical catalog:** adaptogens, sleep, mood, immune, cardiovascular, joint, blood-sugar, brain/nootropics, beauty, antioxidants, methylation, etc. — own-brand + resold brands (e.g. Niagen® NR) `[published]`
- **At-home lab tests:** TruMe at-home DNA Biological Age Test (TST100) `[published]` (price not captured this run)
- **Bulk / wholesale:** bulk NMN, berberine, TMG, resveratrol (100g–1kg); wholesale registration on a separate subdomain `[published]`

Commercial sweeteners: **Subscribe & Save** (ReCharge autoship, up to 30% off), free US shipping over $30, a **100-day refund**, and a price-match policy.

## How it works / model

Two distinct journeys:
- **Supplements (the core):** standard Shopify e-commerce — browse → buy (one-time or Subscribe & Save). No consult gates a purchase. An optional, **free "Longevity Expert"** concierge (a 15-min Calendly session or text/email, quiz-matched to an advisor) helps build a supplement protocol — advisory, not clinical, and not required.
- **Compounded Rx (the telehealth arm):** the buyer starts a **free online visit** at `rxcheckout.prohealth.com` → completes a brief async quiz → **a licensed provider (Beluga Health) reviews and, if appropriate, prescribes** → the prescription is **compounded by a US-licensed pharmacy** and ships (same-day approval claimed, ~4 h weekdays; two-day delivery). Cash-pay; sold per-product (often subscription).

Revenue is product margin (DTC retail + autoship subscriptions), plus wholesale and a healthcare-affiliate channel.

## Positioning & audience

All-genders, science-forward longevity — pitched at health-serious adults who want *"reliable information and supplements that work"* over *"generic AI or influencer stacks."* The wedge is **NAD+/NMN credibility**: ProHealth leans hard on Uthever® being *"the world's first clinically studied NMN brand"* (double-blind, placebo-controlled, peer-reviewed) and on 35 years of trust. The newer pharma arm positions compounded GLP-1/peptides as *"the same powerful ingredients found in popular prescriptions like Ozempic®, Wegovy®, Mounjaro®, Zepbound®… without the hefty price tag."* Competes with both longevity-supplement DTC (e.g. ProHealth vs. NOVOS, DoNotAge, Renue) and the compounded-GLP-1 telehealth field.

## Nav structure

```
- Shop — /collections/all
  - Uthever NMN — /collections/nmn
  - Uthever NMNH — /collections/nmnh-supplements
  - Essentials NMN & NMNH — /collections/essentials-nmn-and-nmnh
  - NAD+ Boosters — /collections/nad
    - NMN — /collections/nmn
    - NR — /collections/nicotinamide-riboside
    - NMNH — /collections/nmnh-supplements
    - All NAD+ Boosters — /collections/nad
  - New — /collections/new-products
  - Shop By Category — /collections
    - Customer Favorites — /collections/best-sellers
    - Adaptogens · Adrenals · AMPK Activation · Antioxidants
    - At-Home Lab Tests — /collections/testing
    - Beauty · Blood Sugar Management · Bone Health · Cardiovascular Health
    - Cellular Energy · Cellular Health · Detoxification & Liver · Digestion & Probiotics
    - Fertility Support · General Health · HPA Axis Support · Immunity Support
    - Joint / Connective Tissue · Methylation · Mood Support · Muscle Health
    - NAD+ Boosters · NAD+ Injection · Niagen NR · Nootropics & Brain Health
    - Senescence / Autophagy · Sirtuin Activation · Sleep Support · Stress Management
    - Telomerase Activity · Thyroid Support · Gift Cards
  - Active Ingredients — /collections  (~50 single-ingredient filters: 5-HTP, ALA, Apigenin, Berberine,
      Collagen, Creatine, Curcumin, DHA, Ergothioneine, Glutathione, Magnesium, NAC, NMN,
      Pterostilbene, Quercetin, Resveratrol, TMG, Vitamin B/C/D, Zinc, …)
  - Pharmaceuticals — /collections/pharmaceuticals
  - At-Home Lab Tests — /collections/testing
  - Bulk — /collections/bulk-supplements
  - Sale — /collections/deals-of-the-week
  - View all — /collections/all
- Learn — /pages/learn
  - Longevity Experts — /pages/longevity-experts
  - Articles — /blogs/control-how-you-age
  - NAD+ News & Research · NAD+ 101 · Breaking News · Press Releases
  - FAQs — /pages/faq
Footer — Help: Contact · My Account · Rx Account Login (rx.prohealth.com) · Shipping · Returns · Price Match · Privacy · Terms
       — More Info: Longevity Experts · Articles · Our Story · Subscribe & Save · Customer Reviews · Affiliates · Healthcare Affiliates · Wholesale · Where to Find Us
```

## Credibility & proof

All self-reported unless noted — recorded, not endorsed:
- **"FEATURED IN 200+ NEWS SITES"** — logo wall: CBS News, NBC News, Fox, ABC News, Google, Reddit
- **35 consecutive years BBB A+** (since 1988); BBB business-review seal in footer (verifiable third-party link)
- **~$5,000,000 donated** to ME/CFS, fibromyalgia, and Lyme research/advocacy since founding
- **Uthever® NMN clinical claim:** *"The FIRST NMN proven to boost NAD+ in a double blind, placebo controlled, peer reviewed published clinical study"*; *"participants' biological age decreased by an average of 12 years"*
- **Manufacturing badges:** "Clinically Studied," "FDA Registered / GMP Manufacturing," "Manufactured & Lab Tested in the USA," "3rd-Party Tested for Purity & Potency," "Mission Driven Since 1988"
- **Product reviews (Judge.me):** NMN Pro 1000 — *4.82 / 5 stars, 1,967 reviews*
- **HIPAA / compliance:** Compliancy Group monitoring seal in footer (the Rx arm's HIPAA posture)
- **Named experts:** Dr. Joseph Maroon (neurosurgeon, longevity author — *"Square One"*) featured; Rx clinical providers **Beluga Health c/o Jonah Mink MD**
- Standard supplement disclaimer present (*"These statements have not been evaluated by the FDA…"*)

## Visual & brand impression

Premium, clinical, science-forward. The homepage is a **dark-navy** canvas (`#08192A`) with science-blue accents, NAD+-decline line charts, athletic black-and-white photography, and glowing blue capsule/bottle renders — a "longevity biotech," not a vitamin-shop, aesthetic. The store/commerce pages (collections, PDP, cart, footer) revert to a clean white Shopify layout, so the dark treatment reads as a hero/marketing device rather than a full dark-mode UI. Poppins + ITC Avant Garde Gothic give it a modern, slightly technical voice. Mature and trust-signal-heavy (badges, COAs, review counts, BBB).

## Strategic read

ProHealth is a **35-year incumbent** repositioned for the longevity moment — its moat is trust (BBB A+, patient-advocacy heritage, own-brand Uthever NMN with a real clinical study) rather than novelty. The interesting recent move is bolting a **compounded-Rx telehealth arm** (GLP-1, sermorelin, NAD+ injectables) onto a supplement storefront — outsourcing the clinical layer to **Beluga Health** and dispensing via a partner compounding pharmacy, so it captures the GLP-1/peptide demand wave without building its own clinic or pharmacy. That makes it a hybrid: an OTC nutraceutical maker/retailer *and* a thin-clinical-layer compounded-Rx reseller. Watch the pharma line — it's the highest-growth, highest-regulatory-exposure surface (FDA compounding-rule volatility around semaglutide/tirzepatide directly threatens it).

## Provenance

- **Pages:** homepage, /pages/our-story, /pages/longevity-experts, /collections/nad (rich/full-page), /collections/pharmaceuticals, /collections/testing, /pages/faq, /products/…nmn-pro-1000-ph593, /collections/pharmaceuticals/products/…personalized-glp-1-rx013 — all Firecrawl, `location:US`, `maxAge:0`.
- **Verify:** all 9 sourceURLs matched; all bodies md5-unique; no junk soft-404s.
- **Credits:** 10 (1 map + 9 scrapes); logos rode the homepage payload (no new credits).
- **Couldn't get:** catalog prices (collection grids lazy-load — only 4 exemplar prices greppable); partner-pharmacy name (FAQ accordion unexpanded); HSA/FSA/insurance copy (none captured).
- **Run profile:** express — +telehealth.md, +offerings.md, +logos.
