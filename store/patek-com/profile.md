---
schema_version: 1

# Identity
domain: patek.com
name: Patek Philippe
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js SPA. No e-commerce/cart and NO public prices anywhere — brand + manufacture site; watches sold via a global network of authorized retailers/Salons, price on request. Every path is mirrored across locale prefixes (/fr, /ja, /zh, /de, /it, …) plus an /en mirror of the bare path — capture the bare or /en form, drop the rest. Map returned 494 URLs dominated by per-reference product pages (/collection/<line>/<ref-no>) × locale. Full nav lives in the homepage footer (mega-nav is video/JS-heavy). The /manufacture/a-story-of-independence URL redirects to /our-values (the 10 core values page)."
key_pages:
  collections: /collection
  values: /manufacture/a-story-of-independence/our-values
  stern_family: /manufacture/a-story-of-independence/the-stern-family
  finest_timepieces: /manufacture/quality-and-fine-workmanship/the-finest-timepieces-in-the-world
  service: /service/our-commitment-to-service
  generations: /manufacture/inside-patek-philippe/the-generations-campaign
  nautilus: /collection/nautilus

unverified_fields:
  - "Pricing — none published anywhere on the site (luxury convention); watches are sold through authorized retailers/Salons with prices on request. No per-reference price available."
  - "Headcount, revenue, annual production volume — not stated. Only qualitative scale given: 150+ references in current production, ~50 in-house movements, 'small series of from ten to several hundred watches' per reference."

# Description — one sentence
description: "The last family-owned Genevan watch manufacturer, designing and crafting mechanical luxury wristwatches, pocket watches, and clocks in-house since 1839, sold through authorized retailers and pledged to be serviced for life."

# Classification
entity_type: Company
target_market: [B2C, B2B2C]   # consumer luxury brand sold through a network of authorized retailers/Salons
offering_category: [Hardware / Physical Products]   # manufactured mechanical timepieces; luxury goods has no closer closed-set value
portfolio_shape: Catalog   # 150+ references across ~10 wristwatch collections + pocket watches + clocks; capture shape, not the list
business_model: Transactional / One-time   # watches bought outright; paid after-sales servicing/restoration is ancillary
primary_industry: Consumer Goods

# Visual identity
logo_url: https://www.patek.com/favicon.ico   # branding.images.logo is an inline data-URI SVG (the Calatrava cross) — favicon fallback
brand_colors: { primary: "#8C7A66", accent: "#AFA294" }   # muted bronze/taupe neutrals; identity reads as black-on-white + warm gold (see Visual)
fonts: [Lora, Open Sans]   # Lora serif headings, Open Sans body
color_scheme: light
design_framework: next.js   # rawHtml: __NEXT_DATA__ + /_next/
---

## Overview

Patek Philippe is a Geneva-based luxury watch manufacturer, in continuous operation since 1839 and owned by the Stern family since 1932 — it presents itself as "the last family-owned Genevan watch manufacturer." It designs, develops, and crafts mechanical timepieces entirely in-house — over 150 references in current production across roughly ten wristwatch collections, plus pocket watches, dome/table clocks, and rare-handcraft pieces. Output is deliberately limited ("small series of from ten to several hundred watches" per reference) and sold only through a global network of authorized retailers and the brand's own Salons. The site is a brand-and-manufacture showcase, not a store: there is no cart and no published pricing anywhere.

## What they offer

`Catalog` shape — 150+ references in current production, manufactured in limited series and certified by the in-house **Patek Philippe Seal**. The site organizes them into collections (the offering hierarchy); no prices are shown. Per-reference depth is out of Tier-0 scope.

Wristwatch collections (the families):

- **Grand Complications:** "the pinnacle of watchmaking" — the most complicated pieces (minute repeaters, perpetual calendars, astronomical watches)
- **Complications:** "a supreme test of ingenuity" — chronographs, calendars, dual-time, world-time; claimed largest collection of complicated watches in regular production
- **Calatrava:** "the quintessential round watch" — the brand's archetypal dress watch (e.g. Ref. 6119)
- **Gondolo:** "the Art Deco spirit" — shaped (rectangular/cushion) cases
- **Golden Ellipse:** elliptical case based on the golden section (Ref. 5738)
- **Cubitus:** "unmistakable elegance" — the newest line (squared/rounded sports design)
- **Nautilus:** "sporting elegance" — the iconic steel/gold luxury sports watch, launched 1976; **50th anniversary celebrated in 2026** with limited editions (Ref. 5811, 5712, 5990, etc.)
- **Aquanaut:** "modern, sporty and chic" — the younger, casual-sport sibling to the Nautilus
- **Twenty~4:** "24 hours of elegance" — the ladies' collection
- **Pocket Watches:** hunter and open-cased mechanical pocket watches, still in current production

Beyond wristwatches:

- **Rare Handcrafts:** dome/table clocks and pieces decorated with enameling, engraving, marquetry, guillochage, gemsetting (e.g. cloisonné-enamel dome clocks)
- **Movements** and **Jewelry & Accessories:** listed as nav categories
- **After-sales service & restoration:** paid servicing/repair/restoration of any Patek Philippe made since 1839 (see model)

## How it works / model

Vertically integrated manufacture: Patek designs, builds movements, and finishes by hand in-house in Geneva (the PP6 manufacture, inaugurated 2020, ~133,650 m²), under its own **Patek Philippe Seal** quality hallmark (est. 2009). It does **not** sell online — purchase happens through authorized retailers, Boutiques, and the brand's own Salons/Maisons; revenue is one-time purchase of the watch. A distinct, recurring revenue/relationship layer is **after-sales service**: the brand pledges to "service, repair, or restore any Patek Philippe timepiece regardless of its age" (back to 1839), performed only by Patek-trained-and-certified watchmakers; vintage pieces (typically 45+ years) go to a dedicated Geneva restoration atelier. Adjacent paid/relationship services: Extract from the Archives, watch registration, and the client-only Patek Philippe Magazine.

## Positioning & audience

Targets high-net-worth collectors and connoisseurs of fine mechanical watchmaking; the defining claim is **independence** — "the oldest and only remaining family-owned Geneva watchmaking company." The brand frames its watches against time itself rather than against competitors, leaning on heritage, rarity, hand-craftsmanship, and inter-generational value retention. Its ten stated core values: **Independence, Tradition, Innovation, Quality and Fine Workmanship, Rarity, Value, Aesthetics, Service, Emotion, Heritage.** The famous campaign line anchors the whole positioning:

> "You never actually own a Patek Philippe. You merely look after it for the next generation." (the "Generations" campaign, running 25+ years)

Founders' stated mission, repeated across the site: "to create the finest timepieces in the world."

## Nav structure

```
- Manufacture — /manufacture
  - A Story of Independence — /manufacture/a-story-of-independence
    - Our values — /manufacture/a-story-of-independence/our-values
    - The founders — /manufacture/a-story-of-independence/the-founders
    - The Stern family — /manufacture/a-story-of-independence/the-stern-family
    - Anchored in Geneva and Switzerland — /manufacture/a-story-of-independence/anchored-in-geneva-and-switzerland
    - The Calatrava cross — /manufacture/a-story-of-independence/the-calatrava-cross
    - The Patek Philippe Seal — /manufacture/a-story-of-independence/the-patek-philippe-seal
  - Quality and Fine Workmanship — /manufacture/quality-and-fine-workmanship
    - The finest timepieces in the world — /.../the-finest-timepieces-in-the-world
    - The Patek Philippe Sound · Calendar watches · Chronograph watches · Cases · Dials · Bracelets
  - A Tradition of Innovation — /manufacture/a-tradition-of-innovation
    - Advanced Research — /manufacture/a-tradition-of-innovation/advanced-research
  - Artisans of Time (Rare Handcrafts) — /manufacture/artisans-of-time
    - Enameling · Engraving · Gemsetting · Guillochage · Hand-finishing · Marquetry
  - Inside Patek Philippe — /manufacture/inside-patek-philippe
    - Salons and Maisons · Watch Art Grand Exhibitions · The Generations campaign · The Patek Philippe Magazine · The Patek Philippe books · The Philosophies series · Rare Handcrafts exhibition
  - Sustainability — /manufacture/sustainability
- Collection — /collection
  - Find your timepiece (Watch Finder) — /collection/watch-finder
  - Grand Complications — /collection/grand-complications
  - Complications — /collection/complications
  - Calatrava — /collection/calatrava
  - Gondolo — /collection/gondolo
  - Golden Ellipse — /collection/golden-ellipse
  - Cubitus — /collection/cubitus
  - Nautilus — /collection/nautilus  (+ Nautilus 50th anniversary — /collection/nautilus-50th-anniversary)
  - Aquanaut — /collection/aquanaut
  - Twenty~4 — /collection/twenty4
  - Pocket Watches — /collection/pocket-watches
  - Rare Handcrafts — /collection/rare-handcrafts
  - Movements — /collection/movements
  - Jewelry & Accessories — /collection/jewelry-and-accessories
  - New models — /collection/new-models
- Service — /service
  - Our commitment to service — /service/our-commitment-to-service
  - Taking care of your watch (care, instructions, settings, register) — /service/taking-care-of-your-watch
  - Extract from the Archives — /service/extract-from-the-archives
  - Frequently asked questions — /service/frequently-asked-questions
- Museum — /museum
  - The Patek Philippe Museum — /museum/the-patek-philippe-museum
  - Plan your visit — /museum/plan-your-visit
- Points of Sale — /points-of-sale  (by region: Africa, America, Asia, Australasia, Caribbean, Europe, Middle East)
- Owners — /owners  (Magazine extra, TechNews, Welcome)
- Careers — /careers
```

## Credibility & proof

- **Heritage:** continuous operation since 1839; Stern-family-owned since 1932 (4 generations; current President Thierry Stern since 2009).
- **Own quality hallmark:** the Patek Philippe Seal (2009), positioned as exceeding existing industry labels/norms (e.g. the Geneva Seal), covering movement, externals, aesthetics, and rate accuracy.
- **Lifetime service pledge:** will service/restore any Patek made since 1839; service is itself a Seal criterion.
- **In-house institution:** the Patek Philippe Museum (Geneva, opened 2001) and the Watch Art Grand Exhibitions (since 2012).
- **Provenance service:** Extract from the Archives for any past timepiece.
- **Scale/rarity signals:** 150+ references in current production, ~50 in-house movements, limited series per reference; the PP6 manufacture (2020).
- **Milestone pieces cited:** Grandmaster Chime (2014, 175th anniversary); Ref. 5470P chronograph measuring 1/10th second.

## Visual & brand impression

Restrained, editorial luxury. The homepage is light/white-grounded with large full-bleed photography and autoplaying video — macro shots of movements and hand-finishing, the modernist manufacture building, and emotive lifestyle imagery (a woman wearing the watch; parent-and-child "Generations" stills). Generous whitespace, thin pill-outline buttons, serif headings (Lora) over sans body (Open Sans). The palette is effectively black-on-white with warm gold/bronze accents drawn from the watches themselves; the Firecrawl `branding` neutrals (#8C7A66 bronze, #AFA294 taupe) match that muted, understated read. The overall feel is museum-grade and unhurried — closer to a heritage cultural institution than a product e-commerce site, consistent with "we never advertise the price, only the legacy."

## Strategic read

Patek's entire moat is **scarcity + independence + intergenerational value**, and the site is engineered to protect it: no prices, no cart, no urgency — the opposite of DTC. Demand is deliberately throttled (limited series, allocation through retailers), which sustains the secondary-market premiums the "Value" message leans on. The lifetime-service pledge is both a genuine differentiator and a flywheel: it deepens owner lock-in, feeds the archives/provenance business, and reinforces the "custodian, not owner" narrative. The 2026 Nautilus 50th anniversary and the new Cubitus line are the current commercial focal points. The independence claim is also a competitive jab — implicitly contrasting Patek against rivals owned by conglomerates (Richemont, LVMH, Swatch Group).

## Provenance

- **Pages:** 8 captured via Firecrawl (Next.js, US/en, maxAge:0, waitFor) — homepage, /collection, /manufacture/a-story-of-independence (→ /our-values), /the-stern-family, /the-finest-timepieces-in-the-world, /service/our-commitment-to-service, /collection/nautilus, /the-generations-campaign. Full-page screenshots + branding/rawHtml on the homepage pass.
- **Verify:** all 8 sourceURLs match; all 8 body md5s unique — no geo/cache contamination. All HTTP 200.
- **Credits:** 9 (1 map + 1 homepage + 7 key pages).
- **Couldn't get:** any pricing (not published — luxury convention); company financials/headcount/production volume (not on a marketing site); per-reference catalog depth (deferred — `Catalog` shape, not enumerated).
