---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: hyperice.com
name: Hyperice
aliases: []
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
captured_at: 2026-06-10
capture_method: firecrawl
site_notes: "Shopify storefront (cdn/shop, Suisse Intl theme webfonts). Heavily geo/locale-prefixed — map is ~80% /de-de, /en-fr etc. dupes; filter to bare paths for the US store. Prices live on collection pages (Shopify card grid), no separate pricing page; /collections/shop-all is the master US roster. Mega-nav lists 6 product lines; 'Hyperice Contrast' + 'Normatec Premier'/'Premier Pack'/'Contrast 2' appear in the product map but are EU-locale only — absent from US nav and shop-all. JSON-LD logo is an inline data-URI (skip); real wordmark is logo_footer_white.svg. Support/FAQ offloaded to hyperice.zendesk.com; returns via /apps/returns."
key_pages:
  about: /pages/about-us
  shop_all: /collections/shop-all
  hypervolt: /collections/hypervolt
  normatec: /collections/normatec
  venom: /collections/venom
  hyperice_x: /collections/hyperice-x
  vyper_hypersphere: /collections/vyper-hypersphere
  hyperboot: /collections/hyperboot-by-nike-hyperice
  accessories: /collections/accessories
unverified_fields:
  - "Founding year 2011 and '60+ countries' are from /pages/about-us self-description; headcount, revenue, ownership/funding not on the marketing site."
  - "brand_colors accent: brand is monochrome black/white; the signature blue→orange gradient is image-based — no exact accent hex on the page (branding payload's #1990C6 is a gradient sample)."

# Description — one sentence
description: "Designs and sells recovery and warm-up hardware — percussion, dynamic air-compression, heat, vibration, and contrast-therapy devices across the Hypervolt, Normatec, Venom, and Hyperice X lines — direct to consumers and elite athletes."

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
  og:       { src: "http://hyperice.com/cdn/shop/files/hyperice-social-share.jpg?v=1775020762", w: 1200, h: 628 }
brand_colors: { primary: "#000000", background: "#FFFFFF" }
fonts: [Suisse Intl]
color_scheme: light
design_framework: Shopify
---

## Overview

Hyperice makes high-performance recovery and warm-up hardware — massage guns, pneumatic compression boots, heated/vibrating wearables, and contrast-therapy devices — sold direct via a Shopify storefront and through retail partners (Best Buy). Founded in 2011, it positions as the brand that "helped define an entire category" of athletic recovery technology, anchored by endorsements from elite athletes across football, track, tennis, golf, and the major US pro leagues. Products are organized by therapy modality (percussion, air compression, heat, vibration, contrast) and most are FSA/HSA-eligible.

## What they offer

Six enumerable product lines, all one-time hardware purchases — every line's price is shown on its collection page `[published]`. Per-SKU roster in [`offerings.md`](offerings.md).

- **Hypervolt — percussion massage guns:** Hypervolt 3 Pro **$349.00** down to Hypervolt Go 2 **$139.00** `[published]`
- **Normatec — dynamic air-compression systems:** hoseless Elite boots and the modular Normatec 3 system; **$379.00 (Normatec Go) – $1,549.00 (Normatec 3 Full Body)** `[published]`
- **Hyperboot by Nike × Hyperice:** wearable heat + Normatec compression boot, co-branded with Nike — **$799.00** `[published]`
- **Hyperice X — contrast therapy:** Hyperice X 2 Knee / Shoulder, hot + cold + air compression — **$449.00** each `[published]`
- **Venom — heat + vibration wearables:** Venom 2 Back/Shoulder/Leg **$269.00**, Venom Go **$129.00** `[published]`
- **Vyper + Hypersphere — vibration rollers/balls:** Vyper 3 **$209.00**, Hypersphere Go **$109.00** `[published]`
- **Bundles:** Elite Pack **$1,548.00** (~~$1,698.00~~), Legacy Pack **$1,328.00** (~~$1,428.00~~), Venom Go Pack **$187.00** `[published]`
- **Accessories & parts:** attachments, control units, chargers, cases, refill pads — **$25.00 – $549.00** `[published]`

## How it works / model

Direct e-commerce: browse by product line or by therapy ("Massage / Warm up / Recovery / Pain relief"), buy outright. No subscription. Revenue is transactional hardware sales, supplemented by retail distribution (same-day pickup at Best Buy), corporate gifting, an affiliate program, and B2B "recovery rooms" + team/pro sales (dedicated sales inquiry channel). Free shipping over $49; 30-day returns and a 1-year warranty; FSA/HSA cards accepted at checkout. Customer support is offloaded to a Zendesk help center ("HyperCare").

## Positioning & audience

Targets athletes and fitness-minded consumers — "elite athlete or an individual… looking for solutions to combat the impact of daily life." Competes with other recovery-tech makers (Therabody/Theragun is the obvious foil in percussion). Claimed edge: category-definer credibility, an athlete-endorsement roster, and breadth across every recovery modality under one brand. The Nike co-brand (Hyperboot) is a distinctive partnership asset.

## Nav structure

```
- Shop — /collections/shop-all
  - Hypervolt (Percussion massage) — /collections/hypervolt
  - Hyperboot by Nike × Hyperice (Heat + Normatec compression) — /collections/hyperboot-by-nike-hyperice
  - Hyperice X (Hot, cold, contrast + air compression) — /collections/hyperice-x
  - Normatec (Dynamic air compression massage) — /collections/normatec
  - Venom (Heat + vibration massage) — /collections/venom
  - Vyper + Hypersphere (Vibration rollers) — /collections/vyper-hypersphere
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
- Explore — /collections/shop-all
  - About us — /pages/about-us
  - Recovery room — /pages/hyperice-recovery-rooms
  - Retail partners — /pages/retail-partners
  - Gift guide — /pages/gift-guide
  - Blog (HyperHub) — /blogs/hyperhub
  - FSA and HSA availability — /pages/purchase-hyperice-products-with-fsa-hsa-funds
```

## Credibility & proof

All self-reported on /pages/about-us unless noted:
- **Athlete roster:** Virgil van Dijk, Sha'Carri Richardson, Jayden Daniels, Erling Haaland, Patrick Mahomes, Naomi Osaka, Jayson Tatum, Rory McIlroy, Kelly Slater, Colleen Quigley, Fernando Tatís Jr., Joe Holder — each listed with their credential (e.g. "3x Super Bowl Champion").
- **Awards (verbatim, self-reported):** "recognized by Fast Company as one of the World's Most Innovative Companies, honored by TIME Best Inventions, and named to the Inc. 5000 Fastest-Growing Companies list."
- **Reach (verbatim):** "used by the world's best athletes and consumers in over 60 countries"; "Founded in 2011… helped define an entire category."
- **Guarantees:** "30 day returns and 1 year warranty"; free shipping over $49; FSA/HSA eligible technology.
- **Distribution:** Nike co-brand (Hyperboot); Best Buy same-day pickup.

## Visual & brand impression

High-maturity, premium athletic-tech aesthetic. Predominantly white/light-gray storefront (clean floating product renders on #F7F5F5) punctuated by full-bleed dark hero panels and signature blue→orange gradient sections behind athlete photography. Monochrome black/white core palette with the gradient as the only chromatic signature; typography is Suisse Intl (a crisp Swiss grotesque), reinforcing a precise, engineered tone. Imagery pairs studio product shots with elite athletes mid-effort. The angular "H" arrow logomark doubles as a motion/forward-momentum motif.

## Provenance

- **Pages:** Analyzed 12 captured pages (firecrawl) — homepage, /pages/about-us, /collections/{shop-all, hypervolt, normatec, venom, hyperice-x, vyper-hypersphere, hyperboot-by-nike-hyperice, accessories, hyperice-contrast}, plus the map. Homepage `branding` + `rawHtml` (JSON-LD, mega-nav, @font-face) read via `fc.py signals`/`logos`.
- **Verify:** sourceURL match + md5-unique across all 11 scrapes; no junk soft-404s.
- **Credits:** 12 (1 map + 11 scrapes).
- **Couldn't get:** Corporate facts (founding beyond the 2011 claim, headcount, ownership/funding) — not on a marketing site. EU-locale Premier/Contrast-2 SKUs not enumerated (absent from US storefront).
- **Run profile:** guided — +offerings (per-SKU roster), +logos module; emphasis "logos and offerings".
