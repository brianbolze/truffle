---
schema_version: "2.2"

# Identity
domain: casio.com
name: Casio
aliases: ["Casio Computer Co., Ltd.", world.casio.com]
parent: []
owns: [gshock.casio.com, edifice-watches.com]

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "casio.com geo-routes to a regional storefront (root → /us/ for a US visitor; map was ~65% /es/ Spanish watch SKUs). Built on Adobe Experience Manager (AEM) — rawHtml shows _jcr_content / etc.clientlibs / content/dam/casio / .casiocoreimg (branding.designSystem says 'custom' — wrong, as usual). Corporate/company info (founding, IR, CSR) lives on the separate world.casio.com host — a thin AEM portal that links to /corporate/, /ir/, /csr/. US store catalog is dominated by G-SHOCK watches; list/category pages carry $ prices inline. No A/B tool fingerprinted."
key_pages:
  corporate: https://world.casio.com
  about: https://world.casio.com/corporate/
  watches: /us/watches
  calculators: /us/calculators
  music: /us/electronic-musical-instruments
  moflin: /us/moflin
  support: /us/support
unverified_fields:
  - "Moflin retail price — not shown on the captured product page (only a '$99 free-shipping' threshold); price sits behind add-to-cart."
  - "Founding year, financials, headcount, corporate structure — not on the consumer storefront; world.casio.com/corporate + /ir carry them but weren't captured at depth this run."
  - "Prices/catalog are the US-region storefront snapshot, not fixed — casio.com geo-routes, so per-region pricing and assortment differ."

description: "A Japanese electronics manufacturer that designs and sells consumer devices direct-to-consumer and via retail — G-SHOCK and Casio watches, scientific and graphing calculators, digital pianos and keyboards, and the Moflin AI companion robot."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Physical Products / Hardware]
portfolio_shape: Catalog
business_model: Transactional / One-time
primary_industry: Technology

# Visual identity
logo_url: https://www.casio.com/etc.clientlibs/casio/clientlibs/clientlib-resources/casio/resources/icon-192x192.png  # STRAIN: branding.images.logo was an inline data-URI SVG; favicon fallback used
brand_colors: { primary: "#092981", secondary: "#D92D2D", accent: "#000000" }  # STRAIN: primary = Casio blue (wordmark); red is a CTA/sale accent — screenshot-confirmed
fonts: [DIN 2014, Noto Sans JP]
color_scheme: light
design_framework: Adobe Experience Manager (AEM)
---

## Overview

Casio (Casio Computer Co., Ltd.) is a Japanese consumer-electronics maker that designs, manufactures, and sells durable digital devices worldwide. The US site (`casio.com/us`) is a direct-to-consumer storefront spanning four live consumer lines — watches, calculators, electronic musical instruments, and the Moflin AI companion robot — plus label printers. Watches, led overwhelmingly by the rugged G-SHOCK brand, dominate the merchandising. The corporate identity sits on a separate host (`world.casio.com`), whose stated purpose is *"Through the power to put wonder at hand, bring new levels of joy to lives one by one."*

## What they offer

A broad consumer-electronics catalog (Catalog shape — hundreds of SKUs per line; per-SKU depth defers to `offerings.md`). Hardware sold outright, not subscription. Four storefront lines + accessories:

- **Watches:** the flagship category — `/us/watches`. Sub-brands: **G-SHOCK** (rugged, dominant; own site at gshock.casio.com), **Baby-G**, **EDIFICE** (own site edifice-watches.com), **PRO TREK**, **OCEANUS**, and **CASIO/Vintage** (classic budget models — F-91W, A158W, A168). Listing prices span roughly **$100–$165+** for standard lines, far higher for metal/MR-G.
- **Electronic Musical Instruments:** digital pianos & keyboards — `/us/electronic-musical-instruments`. Three brand lines: **Casiotone** (portable keyboards, CT-S), **Privia** (digital/stage pianos, PX-S), **Celviano** (console pianos). Featured pianos run **$99–$449.99** and up (PX-S7000 tier higher).
- **Calculators:** `/us/calculators` — **Graphing** (FX-CG50, FX-9750GIII), **Scientific/Fraction** (FX-300ESPLUS), **Basic/Desktop**, **Printing**, and **Software/Apps**. Prices from **~$10.99** (basic) into the **$140s** (graphing).
- **Moflin (AI Pet):** `/us/moflin` — a furry AI "smart companion" robot with simulated emotions and a developing personality; positioned for emotional-wellness/companionship (deployed to a pediatric hospital ward per a corporate news release). On-page price not shown.
- **Also:** Label Writer (label printers), plus marketing/experience surfaces **Dimension Shifter** and **Casio Lab**.

## How it works / model

Transactional hardware sales. The US storefront is a full e-commerce shop (cart/"My Bag", order tracking, product registration, rewards, military discount, outlet/sale) selling devices direct, alongside a retail/distribution channel. Revenue is one-time product purchase, not recurring. Catalog is geo-routed: `casio.com` redirects each visitor to a regional store (US, Europe, intl, etc.) with region-specific pricing and assortment.

## Positioning & audience

Mass-market consumers across distinct use-cases rather than one segment: watch enthusiasts (G-SHOCK toughness, vintage nostalgia, collabs like Mandalorian/Grogu, Pac-Man, Stranger Things), students and educators (the calculator line leans hard on "Gear up for School" / affordable math tools), hobbyist and pro musicians (keyboards/pianos), and a wellness/companionship angle for Moflin. Claimed edge is reliable, affordable, innovative engineering — the corporate "put wonder at hand" purpose framing.

## Nav structure

```
- Watches — /us/watches
  - All Watches — /us/watches/
  - New Arrivals — /us/watches/new/
  - G-SHOCK — /us/watches/gshock/  (+ 2100, 5600, 110, Full Metal, MR-G luxury, military)
  - CASIO / Vintage — /us/watches/casio/
  - Baby-G, EDIFICE, PRO TREK, OCEANUS (sub-brands)
- Digital Pianos / Portable Keyboards — /us/electronic-musical-instruments
  - Portable Keyboards — /categories/portable-keyboards
  - Stage Pianos — /categories/stage-pianos
  - Console Pianos — /categories/console-pianos
  - Lighted-Key Keyboards — /categories/lighted-key-keyboards
  - Brands: Casiotone, Privia, Celviano
- Calculators — /us/calculators
  - Graphing — /graphing
  - Scientific / Fraction — /scientific-fraction
  - Basic / Desktop — /basic-desktop
  - Printing — /printing
  - Software & Apps — /software-apps
- Moflin (AI Pet) — /us/moflin
- Dimension Shifter — /us/dimensionshifter
- Casio Lab — /us/lab
- Label Writer — /us/label-writer
- Sale — /us/sale  (+ Outlet)
- Support — /us/support  |  Corporate — world.casio.com (About / IR / Sustainability)
```

## Credibility & proof

- **Heritage & scale:** publicly traded (Casio Computer Co., Ltd.); decades-long brands (G-SHOCK, the F-91W classic, calculator line celebrating "60th"); global multi-region presence.
- **Licensed collaborations:** Mandalorian & Grogu, Pac-Man, Stranger Things, A.P.C. — signals cultural reach and brand demand.
- **Corporate governance surface:** world.casio.com publishes investor relations, financial results, CSR/sustainability, and an AI policy.
- **Social proof:** on-site testimonials (Moflin), recommendation/best-seller modules, and a real-world hospital deployment of Moflin cited in corporate news.

## Visual & brand impression

Clean, high-volume retail storefront on a white background with black body text and the blue Casio wordmark. Layout is a classic e-commerce product grid — hero banner (G-SHOCK collab), "Recommended for You," "What's New," "New Products" carousels, then a "Shop by Category" row (watches, keyboards, Moflin, calculators, label printer). Product photography is crisp and dominant; watches carry the visual weight. A mustard/yellow promo band (Dimension Shifter) adds the only strong color block. Tone reads professional, product-forward, and mainstream rather than premium-boutique — DIN 2014 display type over Noto Sans body. Mature, well-maintained design system (AEM-driven).

## Provenance

- **Pages:** 6 captured via Firecrawl (`maxAge:0`, `location:US`, all-formats homepage) — homepage (`casio.com`→`/us/`), `world.casio.com` (corporate portal), `/us/watches`, `/us/calculators`, `/us/electronic-musical-instruments`, `/us/moflin`. Map (500 URLs) used for inventory only.
- **Verify:** all 6 sourceURLs matched the requested URLs; all body md5s unique — no geo/cache contamination this run.
- **Credits:** 7 (1 map + 6 scrapes; all basic proxy, 1cr each).
- **Couldn't get:** corporate depth (founding year, financials, headcount, segment breakdown — on `world.casio.com/corporate` + `/ir`, not scraped at depth); Moflin retail price (not on the product page); non-US pricing (site geo-routes — US snapshot only).
- **Migrations:** 2026-06-01 v1→v2.0 — offering_category remapped by rule (not re-captured): [Hardware / Physical Products, Retail / E-Commerce] → Physical Products / Hardware.
- **Structured layer (schema 2.2):** ran `fc.py signals` on the persisted 2026-05-31 homepage rawHtml — no `application/ld+json` present, so no JSON-LD structured-layer fields (Nav already captured). Re-stamped 2.0→2.2.
