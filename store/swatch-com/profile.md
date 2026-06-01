---
schema_version: "2.0"

# Identity
domain: swatch.com
name: Swatch
aliases: ["Swatch Ltd"]
parent: []                           # © reads "SWATCH LTD"; corporate parent (The Swatch Group) not stated on captured pages — see unverified_fields
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Salesforce Commerce Cloud (Demandware/SFCC) storefront — rawHtml has demandware.static + /s/Sites-swarp-AM-Site/dw/; branding.designSystem said 'custom' (wrong). swatch.com 301→ www.swatch.com, then locale-routes to /en-us/ (US-geolocated, USD). Map returns ~all product .html PDPs, locale-prefixed (en-us / en-ca / fr-ca) — not the company-info pages; brand self-description lives on /our-world.html. MoonSwatch (OMEGA collab) is in-store-only — no online price, 1 watch/person/day/store. Footer 'Company Info' = Press + Jobs + legal only; no swatchgroup.com link. Logo is inline data-URI SVG → logo_url falls back to favicon."
key_pages:
  watches: /watches/
  moonswatch: /bioceramic-moonswatch-collection.html
  scuba_fifty_fathoms: /bioceramic-scuba-fifty-fathoms.html
  our_world: /our-world.html
  bioceramic: /bioceramic.html
  essentials: /collection/swatch-essentials/
unverified_fields:
  - "Corporate parent (The Swatch Group Ltd) not asserted on captured pages — © is 'SWATCH LTD 2026'; left parent empty per capture-from-page rule."
  - "MoonSwatch (OMEGA X Swatch) online price unavailable — collection is in-store purchase only."
  - "Prices/IA are a point-in-time snapshot, not fixed — US-geolocated /en-us/ storefront serving USD; other regions differ."

description: "A Swiss fashion-watch brand selling colorful, affordable quartz and automatic timepieces, jewelry, and accessories direct-to-consumer online and in its own stores, known for artist and luxury (OMEGA, Blancpain) collaborations."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Physical Products / Hardware]
portfolio_shape: Catalog
business_model: Transactional / One-time
primary_industry: Consumer Goods

# Visual identity
logo_url: https://www.swatch.com/on/demandware.static/Sites-swarp-AM-Site/-/default/dwc0ab0989/images/favicons/swatch/favicon-196x196.png
brand_colors: { primary: "#E2001A", accent: "#146AFF" }   # signature Swatch red confirmed via logo SVG rect fill rgb(226,0,26); blue/orange are UI/playful accents
fonts: [SwatchCTWeb]
color_scheme: light
design_framework: salesforce-commerce-cloud
---

## Overview

Swatch is the Swiss fashion-watch brand that revolutionized watchmaking in 1983 with affordable, stylish, Swiss-made quartz watches. It sells watches, jewelry, sunglasses, and accessories direct to consumers — online (a locale-routed Salesforce Commerce Cloud storefront) and through its own retail stores worldwide. The brand is built on three pillars it states explicitly — **sport, art, and innovation** — and on a "joy of life, positive provocation, creativity" identity. Its modern cultural engine is high-profile collaborations: the OMEGA X Swatch Bioceramic MoonSwatch and the Blancpain X Swatch Scuba Fifty Fathoms, both reinterpreting luxury Swatch Group siblings at an accessible price.

## What they offer

A `Catalog` of hundreds of watch models (the map returns near-exclusively product PDPs) organized into collections rather than a small enumerable set. Watches sell **outright (one-time)**, not subscription. Breadth + price bands:

- **Core / Swatch ESSENTIALS:** the everyday-style line, "continually refreshed" — observed range **$75.00–$235.00** (most $75–$135).
- **Bioceramic MoonSwatch (OMEGA X Swatch):** the flagship phenomenon — a Bioceramic take on the OMEGA Speedmaster Moonwatch (launched 2022). 11-watch "Mission to [planet]" line plus Mission to the Moonphase, Mission to Earthphase (incl. Moonshine™ Gold), and MOONSWATCH 1965. **In-store purchase only** — no online price; limited to one per person, per day, per store.
- **Bioceramic Scuba Fifty Fathoms (Blancpain X Swatch):** diver's-watch collab honoring Blancpain's 1953 Fifty Fathoms, on Swatch's automatic **SISTEM51** movement, water-resistant to 50 fathoms (91 m), nudibranch-themed by ocean. **$420.00** each (Atlantic / Pacific / Indian / Arctic / Antarctic / Ocean of Storms).
- **Watches by attribute:** automatic, chronograph, skeleton, classic, originals, big & oversized, small, square, ultra-thin (Skin Irony), transparent, and by color (black/blue/gold-tone/pastel/pink/red/white).
- **Accessories:** jewelry, sunglasses, watch straps (incl. MoonSwatch rubber/VELCRO® straps), Royal Pop line.
- **Gifting:** curated gift guides (gifts for her / for him, seasonal e.g. Mother's Day).

Overall price spread across captured pages: **~$50–$420** (a few jewelry/gold SKUs higher, e.g. $801).

## How it works / model

Direct-to-consumer retail. Customers browse the online storefront (US storefront serves USD, free shipping advertised) or buy in Swatch's own physical stores; a store locator is prominent. Revenue is **transactional** — watches are bought outright, no membership. Notably, the hottest collab (MoonSwatch) is deliberately **kept offline and in-store-only** with per-person daily limits, using scarcity and the in-store visit as the channel. Payment methods: Visa, Mastercard, PayPal, Discover, Amex, Affirm (financing), UnionPay, Apple Pay.

## Positioning & audience

`branding.personality`: modern tone, high energy, "fashion-conscious individuals." Swatch positions watches as **affordable Swiss-made fashion + self-expression**, not horological investment or tech — playful, provocative, colorful. Its claimed edge is the marriage of (a) Swiss quality at low price, (b) proprietary innovation (quartz pioneering, SISTEM51, Swatch Pay, patented Bioceramic), and (c) cultural cachet via art and luxury-brand collaborations that put a $270–$420 "OMEGA" or "Blancpain" on a mass-market wrist. Competes against both fashion-accessory watch brands and, via collabs, punches up into entry-luxury.

## Nav structure

```
- Watches — /watches/
  - Best selling — /watches/best-selling-watches/
  - New releases — /watches/new-watch-releases/
  - Originals — /watches/originals/
  - Automatic — /watches/automatic-watches/
  - Chronograph — /watches/chronograph-watches/
  - Skeleton — /watches/skeleton-watches/
  - Classic — /watches/classic-watches/
  - Big & oversized — /watches/big-oversized-watches/ (Big Bold)
  - Small — /watches/small-watches/
  - Square — /watches/square-watches/
  - Ultra-thin — /watches/ultra-thin-watches/ (Skin Irony)
  - Transparent — /watches/transparent-watches/
  - Art watches — /watches/art-watches/
  - By color — black / blue / gold-tone / pastel / pink / red / white / colorful / stainless-steel
- Men's watches — /mens-watches/
- Women's watches — /womens-watches/
- Accessories — /accessories/
  - Jewelry — /accessories/jewelry/
  - Sunglasses — /accessories/sunglasses/
  - Watch straps — /accessories/watch-straps/ (MoonSwatch straps)
  - Royal Pop accessories — /accessories/royal-pop-accessories/
- Collections
  - Bioceramic MoonSwatch (OMEGA X Swatch) — /bioceramic-moonswatch-collection.html
  - Scuba Fifty Fathoms (Blancpain X Swatch) — /bioceramic-scuba-fifty-fathoms.html
  - Bioceramic — /bioceramic.html
  - Swatch ESSENTIALS — /collection/swatch-essentials/
  - Royal Pop — /royal-pop.html
  - AI-DADA — /about-ai-dada.html
- Gifting — /gifting/ (gifts for her / for him / gift guide)
- Our world — /our-world.html (sport / art / innovation)
- Find a store — /stores
- Customer service — /customer-service/
- Brand switcher → Flik Flak (kids), @81 BEATS / Internet Time
```

## Credibility & proof

- **Heritage:** Swiss made, "© SWATCH LTD 2026"; pioneered affordable Swiss quartz (1983) — narrated on /our-world.html.
- **Proprietary tech:** patented Bioceramic (2/3 ceramic + 1/3 castor-oil-derived biosourced material), SISTEM51 automatic movement, Swatch Pay, Swatch ACCESS.
- **Luxury co-signs:** active collaborations with OMEGA and Blancpain (both Swatch Group maisons), plus Audemars Piguet press feature; artist collaborations (Roy Lichtenstein, Saype) and the Swatch Art Peace Hotel.
- **Sport sponsorships:** Swatch Proteam athletes (Sky Brown), beach volleyball (Gstaad Beach Pro), skate/snow (LAAX, Swatch Nines) — official timekeeper heritage.
- **Trust mechanics:** free shipping, returns & exchanges, financing (Affirm), global store network, newsletter, large social presence (FB/YouTube/Instagram/X/LinkedIn/TikTok).

## Visual & brand impression

The screenshot reads as a polished, high-energy fashion e-commerce flagship: clean white canvas, dark top nav, and dense grids of vividly colored watches shot against bright lifestyle backdrops (jellyfish blues, candy pinks, pop-art panels). Photography-forward and product-saturated — color *is* the brand. The signature Swatch red (#E2001A) anchors the logo while the merchandising leans into a full rainbow, signalling playful, accessible, youthful fashion rather than austere Swiss-luxury restraint. Mature, well-maintained, conversion-optimized design.

## Strategic read

The interesting move is the **scarcity-as-channel** play on collaborations. Swatch is structurally an entry-price catalog brand ($75–$235 core), but it manufactures cultural heat by borrowing the equity of its Swatch Group luxury siblings (OMEGA, Blancpain) into Bioceramic at $270–$420 — then deliberately withholding the MoonSwatch from e-commerce entirely to force in-store visits and one-per-day queues. That converts a commodity quartz brand into a drop-culture / hype engine and drives footfall to physical retail, while the broad ESSENTIALS catalog monetizes the resulting traffic. The brand's three stated pillars (sport/art/innovation) are the durable identity; the collabs are the renewable demand spikes.

## Provenance

- **Pages:** 7 captured via Firecrawl (SFCC storefront, /en-us/, US-geolocated) — homepage; /watches/ (taxonomy); /bioceramic-moonswatch-collection.html; /bioceramic-scuba-fifty-fathoms.html; /our-world.html (brand story); /bioceramic.html (material); /collection/swatch-essentials/ (core pricing). All key URLs drawn from the captured map + homepage-link inventory, none hand-typed.
- **Verify:** `fc.py verify` — all 7 sourceURLs matched, all body md5s unique; no geo/cache contamination. (Map is a 500-URL sample, near-all product PDPs.)
- **Credits:** 9 — 2 map + 1 homepage (all-formats) + 6 key pages, 1 credit each.
- **Couldn't get:** MoonSwatch online price (in-store-only by design); explicit Swatch Group parent linkage (not on captured marketing pages); per-SKU catalog depth (deferred — `Catalog` shape, captured by shape not enumeration).
- **Migrations:** 2026-06-01 v1→v2.0 — offering_category remapped by rule (not re-captured): [Apparel & Footwear, Retail / E-Commerce] → Physical Products / Hardware.
