---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: hyperice.com
name: Hyperice
aliases: []
legal_entity: ""
parent: []
owns: []
socials:
  x: https://twitter.com/Hyperice
  facebook: https://facebook.com/Hyperice
  instagram: http://instagram.com/Hyperice
  youtube: https://www.youtube.com/@HypericeVideo
  tiktok: https://www.tiktok.com/@hyperice
external: {}

# Capture meta
captured_at: 2026-06-24
capture_method: firecrawl
site_notes: "Shopify storefront (cdn/shop, Shopify product registry, Suisse Intl theme webfonts). Heavily geo/locale-prefixed — map is mostly /de-de, /en-fr, /fr-fr, /en-de, /it-it etc.; filter to bare US paths for the storefront. Prices live on collection cards; /collections/shop-all is the master US surface. /products.json?limit=250 is the catalog backbone and exposed 65 handles: 59 surfaced in captured US storefront/card pages plus 6 registry-only hidden/legacy handles. Hidden PDP attempts for Premier/Contrast legacy handles returned duplicate homepage bodies, so use products_json for those rows rather than the PDP shell. Gift card denominations live on /products/gift-card. Support/FAQ offloaded to hyperice.zendesk.com; returns via /apps/returns."
key_pages:
  about: /pages/about-us
  shop_all: /collections/shop-all
  hypervolt: /collections/hypervolt
  normatec: /collections/normatec
  hyperboot: /collections/hyperboot-by-nike-hyperice
  hyperice_x: /collections/hyperice-x
  venom: /collections/venom
  vyper_hypersphere: /collections/vyper-hypersphere
  accessories: /collections/accessories
  outlet: /collections/outlet
  sale: /collections/sale
  gift_card: /products/gift-card
  catalog_registry: /products.json?limit=250
unverified_fields:
  - "Founding year 2011 and 'over 60 countries' are from /pages/about-us self-description; headcount, revenue, ownership/funding, and legal entity are not stated on the captured site."
  - "Prices/availability are a point-in-time snapshot, not fixed — the captured storefront was running a Prime Day sale and the Shopify registry carried hidden/unavailable legacy handles."
  - "brand_colors accent: brand is monochrome black/white; the signature blue→orange gradient is image-based — no exact accent hex on the page (branding payload's #1990C6 is a sampled UI/gradient color)."

# Description — one sentence
description: "Designs and sells recovery and warm-up hardware — percussion, dynamic air-compression, heat, vibration, and contrast-therapy devices across Hypervolt, Normatec, Venom, Hyperice X, and Hyperboot lines."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Physical Products / Hardware]
portfolio_shape: Multi-product
business_model: Transactional / One-time
primary_industry: Sports & Recreation

# Visual identity
logo_url: https://hyperice.com/cdn/shop/files/logo_footer_white.svg?v=1765839129
logos:
  wordmark: { src: "https://hyperice.com/cdn/shop/files/logo_footer_white.svg?v=1765839129", w: 200, h: 28 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=hyperice.com&sz=256", px: 32, transparent: true }
  og:       { src: "https://hyperice.com/cdn/shop/files/hyperice-social-share.jpg?v=1775020762", w: 1200, h: 628 }
brand_colors: { primary: "#000000", background: "#FFFFFF" }
fonts: [Suisse Intl]
color_scheme: light
design_framework: Shopify
---

## Overview

Hyperice makes performance recovery and warm-up hardware: percussion massage guns, dynamic air-compression systems, heated/vibrating wearables, contrast-therapy wraps, vibration rollers/balls, and the Nike co-branded Hyperboot. It sells direct through a Shopify storefront, with Best Buy pickup, FSA/HSA checkout messaging, affiliate/press/sales channels, and a separate sales-inquiry path for team or business buyers. The site positions the brand as a category-defining recovery-tech maker founded in 2011, used by elite athletes and consumers in "over 60 countries."

## What they offer

Per-SKU roster in [`offerings.md`](offerings.md). Captured scope: 65 Shopify product handles total — 59 surfaced through captured US storefront/card pages, plus 6 registry-only hidden/legacy handles from the captured Shopify product registry.

- **Hypervolt — percussion massage guns and parts:** surfaced devices from Hypervolt Go 2 **$109.00** to Hypervolt 3 Pro **$299.00** during the sale; heated head, applicator set, battery, and open-box variants `[published]`
- **Normatec — dynamic air-compression systems:** surfaced devices from Normatec Go **$299.00** to Normatec 3 Full Body **$1,349.00**, plus Elite Pack **$1,548.00**, attachments, control unit, cases, chargers, open-box rows, and registry-only Premier/Lower Legs legacy handles `[published]`
- **Hyperboot by Nike × Hyperice:** wearable heat + Normatec compression boot **$699.00** and Warm Up Pack **$899.00** `[published]`
- **Hyperice X / Contrast — hot, cold, and air-compression wraps:** Hyperice X 2 Knee / Shoulder **$359.00** each, open-box rows, plus registry-only Hyperice Contrast 2 legacy handles `[published]`
- **Venom — heat + vibration wearables:** Venom Go **$99.00**, Venom 2 Back **$215.00**, Venom 2 Shoulder/Leg **$239.00**, Venom Go Pack **$149.00**, accessories, and open-box rows `[published]`
- **Vyper + Hypersphere — vibration roller/ball:** Hypersphere Go **$109.00**, Vyper 3 **$209.00**, and Open Box Vyper 3 **$100.00** `[published]`
- **Accessories, bundles, and gift cards:** chargers/cases/attachments **$25.00–$549.00**, Legacy Pack **$1,328.00**, gift-card denominations **$25–$1000** `[published]`

## How it works / model

Direct e-commerce: browse by product line, therapy, sale, outlet, or shop-all; buy outright. No subscription or membership is shown. Revenue model is transactional hardware sales, supplemented by retail distribution (Best Buy pickup), affiliate marketing, corporate/team sales inquiries, and likely gifting. Site-level purchase promises include free shipping over $49, 30-day returns, 1-year warranty messaging, and FSA/HSA card acceptance at checkout.

## Positioning & audience

Targets athletes, fitness-minded consumers, and organizations building recovery experiences. The copy frames Hyperice as an innovation-led recovery-tech brand: "Move better" is the core message, with elite-athlete proof, product-line breadth across recovery modalities, and the Nike × Hyperice co-brand as a partnership asset. The current homepage strongly foregrounds Prime Day savings and Hyperboot warm-up use cases.

## Nav structure

```
- Shop — /collections/shop-all
  - Hypervolt — /collections/hypervolt
    - Percussion massage
  - Hyperboot by Nike × Hyperice — /collections/hyperboot-by-nike-hyperice
    - Heat and Normatec compression
  - Hyperice X — /collections/hyperice-x
    - Hot, cold, contrast and air compression
  - Normatec — /collections/normatec
    - Dynamic air compression massage
  - Venom — /collections/venom
    - Heat and vibration massage
  - Vyper + Hypersphere — /collections/vyper-hypersphere
    - Vibration rollers
  - Gift Cards — /products/gift-card
  - Accessories — /collections/accessories
  - Outlet — /collections/outlet
  - Sale — /collections/sale
  - Shop all — /collections/shop-all
- Therapy — /collections/shop-all
  - Massage — /pages/massage
  - Warm up — /pages/warm-up
  - Recovery — /pages/recovery
  - Pain relief + tension — /pages/pain-relief-tension
  - Normatec card — /products/normatec-elite-hips
  - Hyperice X 2 card — /products/hyperice-x-2-shoulder
- Explore — /collections/shop-all
  - About us — /pages/about-us
  - Recovery room — /pages/hyperice-recovery-rooms
  - Retail partners — /pages/retail-partners
  - Gift guide — /pages/gift-guide
  - Blog — /blogs/hyperhub
  - FSA and HSA availability — /pages/purchase-hyperice-products-with-fsa-hsa-funds
```

## Credibility & proof

- **Athlete roster:** Virgil van Dijk, Sha'Carri Richardson, Jayden Daniels, Erling Haaland, Patrick Mahomes, Naomi Osaka, Jayson Tatum, Rory McIlroy, Colleen Quigley, Kelly Slater, Fernando Tatís Jr., and Joe Holder are shown on /pages/about-us with role/credential captions.
- **Awards (verbatim, self-reported):** "recognized by Fast Company as one of the World's Most Innovative Companies, honored by TIME Best Inventions, and named to the Inc. 5000 Fastest-Growing Companies list."
- **Reach (verbatim, self-reported):** "Founded in 2011"; "used by the world's best athletes and consumers in over 60 countries."
- **Purchase trust:** "Order online and pick up at Best Buy today"; "Use your FSA/HSA card at checkout"; "Free shipping on orders over $49"; 30-day returns and 1-year warranty messaging.
- **B2B hooks:** affiliate program, press inquiries, and sales inquiries are all explicit on /pages/about-us.

## Visual & brand impression

Premium athletic-tech storefront. The core UI is bright, restrained, and product-led: white/near-white surfaces, black typography, floating product renders, and large performance-athlete photography. The current homepage adds darker hero panels and a blue/orange campaign gradient around Prime Day and Hyperboot. Suisse Intl gives the brand a precise Swiss-grotesque feel; the angular Hyperice mark reads as motion/forward direction.

## Provenance

- **Pages:** Analyzed 14 active Firecrawl scrapes — homepage, /pages/about-us, /collections/{shop-all, hypervolt, normatec, hyperboot-by-nike-hyperice, hyperice-x, venom, vyper-hypersphere, accessories, outlet, sale}, /products/gift-card, and /products.json?limit=250 — plus the map. Homepage `rawHtml` JSON-LD/nav read via `fc.py signals`; logos measured from unchanged declared sources and archived measured assets.
- **Verify:** sourceURL match + md5-unique across all 14 active scrapes; no junk soft-404s. Two hidden PDP attempts (`/products/premier-pack`, `/products/normatec-premier-legs`) returned duplicate homepage bodies and were quarantined/marked `discarded` in the manifest.
- **Credits:** 17 (1 map + 14 active scrapes + 2 discarded hidden-PDP attempts).
- **Couldn't get:** Legal entity, ownership/funding/headcount/revenue from the site. Registry-only hidden/legacy SKUs have registry price/availability evidence, but their bare PDP scrapes did not produce product bodies in this run.
- **Run profile:** express — +offerings with full catalog emphasis; added `products_json`, `outlet`, `sale`, and `gift_card` coverage beyond the prior roster.
