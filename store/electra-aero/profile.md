---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: electra.aero
name: Electra
aliases: [Electra Aero]
legal_entity: ""
parent: []
owns: []
socials:
  x: https://x.com/ElectraAero
  linkedin: https://www.linkedin.com/company/electra-aero/
  youtube: https://www.youtube.com/@Electraaero
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "Statamic site with Alpine.js/Vite-style assets in rawHtml; branding.designSystem said Tailwind, ignored. Map returned 100 URLs but is news-heavy; homepage links are the reliable core nav. Direct Aviation page has interactive counters that render as zeros in markdown, so use stable text/screenshot claims rather than zero counters. Meaningful EL9 specs are on /technology and /preorders; /news/electra-unveils-first-product-configuration is thin. EL9 PDF brochure linked from /technology was not scraped."
key_pages:
  home: /
  company: /company
  technology: /technology
  defense: /defense
  direct_aviation: /direct-aviation
  team: /team
  preorders: /news/electra-secures-2-200-pre-orders
  product_configuration: /news/electra-unveils-first-product-configuration
unverified_fields:
  - "Public EL9 unit price, delivery terms, and defense procurement terms are not shown; pre-order pipeline value is site-reported, not a price card."
  - "EL9 PDF brochure linked from /technology was not parsed; profile uses the rendered technology page for public specs."
  - "Headcount, revenue, cap table, and ownership are not on the captured pages; funding appears only as a site milestone."
  - "Direct Aviation interactive widgets render some counters as 0 in markdown; those zero values were excluded."

description: "Builds the EL9 Ultra Short, a hybrid-electric fixed-wing aircraft for 150-foot takeoff and landing, positioning it for direct regional travel, cargo, and defense logistics without new airport infrastructure."

# Classification
entity_type: Company
target_market: [B2B, B2G]
offering_category: [Physical Products / Hardware]
portfolio_shape: Single
business_model: Transactional / One-time
primary_industry: Automotive & Mobility

# Visual identity
logo_url: "https://electra-aero.s3.us-east-1.amazonaws.com/electra-logo.svg"
logos:
  wordmark: { src: "https://electra-aero.s3.us-east-1.amazonaws.com/electra-logo.svg", w: 166, h: 48 }
  logomark: { src: "https://electra-aero.s3.us-east-1.amazonaws.com/68da8659ec9d608054e63a62_electra-favicon.png", px: 32, transparent: true }
  og:       { src: "https://electra-aero.s3.us-east-1.amazonaws.com/697a2da8db440eac198f0a71_db7193254d407922bec71c0ab931f546_electra-opengraph@2x.png", w: 2400, h: 1260 }
brand_colors: { primary: "#FFAA00", background: "#1A1A1A", text: "#FFFFFF" }
fonts: [Manrope, Exo]
color_scheme: dark
design_framework: Statamic
---

## Overview

Electra is an advanced air mobility aircraft company building the EL9 Ultra Short, a hybrid-electric fixed-wing airplane designed to take off and land in 150 feet. The company frames the aircraft as the unlock for "Direct Aviation": regional passenger, cargo, and defense missions that avoid long drives, hub airports, and new charging infrastructure. It was launched in 2020 by founder John Langford, with MIT Professors John Hansman and Mark Drela as key technical advisors; B. Marc Allen is President & CEO.

## What they offer

Electra has one core platform, the EL9 Ultra Short, with commercial and defense use cases. Public aircraft pricing is not shown `[on-request]`.

- **EL9 Ultra Short aircraft:** a nine-passenger hybrid-electric Ultra Short aircraft with **"1,100 nm"** ferry range plus **"+ 45 mins reserve"**, **"9 Passengers"** plus **"50 lbs baggage each"** or **"3,000 lbs of cargo"**, **"175 KTAS"** cruise speed, **"150 ft ground roll"**, **"75 dBA @ 300ft"**, and **"-40%"** lower fuel burn than comparable aircraft on an average 100-mile route `[on-request]`.
- **Defense / tactical mobility configuration:** the EL9 is positioned for runway-independent airlift, logistics, expeditionary power, and special missions; the defense page claims **"1,000 lbs over 1,000 NM"**, **"600 kW"** ground/airborne power, **"100x quieter"** than helicopters, and **"70% lower operating costs"** than helicopters `[on-request]`.
- **Direct Aviation market development:** a first-party market outlook and access-point thesis for operators, regional carriers, charter operators, and government entities; this is a go-to-market frame around the aircraft, not a separately priced product `[on-request]`.

## How it works / model

Electra commercializes through aircraft pre-orders, launch/customer agreements, strategic partnerships, and government programs rather than public e-commerce. The site says the EL9 integrates blown-lift aerodynamics, hybrid-electric propulsion, and triplex redundant fly-by-wire controls: electric motors blow air over the wing/flaps for low-speed lift, batteries support takeoff and landing, a turbogenerator supports cruise, and batteries can charge in flight or on the ground. The March 2025 preorder page says the EL9 has **"2,200 pre-orders"**, an order pipeline **"valued at nearly $9 billion"**, and recent customers across Turkey, Senegal, Nigeria, Denmark, the US, India, and Brazil, joining Bristow Group, JetSetGo, Blade India, Flapper, flyv, LYGG, JSX, and Surf Air.

## Positioning & audience

Electra targets commercial aviation operators, air mobility innovators, cargo/logistics use cases, and government/defense buyers who need short-field access, lower noise, and lower operating cost than helicopters. Its main positioning contrast is not "electric air taxi" spectacle; it argues for a practical fixed-wing aircraft that can use existing infrastructure first, then expand to heliports, parking lots, grass fields, ships, unimproved surfaces, and other access points. The Direct Aviation page frames the regional opportunity around trips that sit between slow car travel and hub-and-spoke flying, including a claimed **"more than 6,000 new U.S. commercial air routes"** opportunity.

## Nav structure

```
- Company — /company
- Defense — /defense
- Technology — /technology
- Careers — /careers
- Team — /team
- News — /news
- Videos — /videos
- Contact — /contact
- Direct Aviation Market Outlook — /direct-aviation
- Store — https://electraaero.myshopify.com/
```

## Credibility & proof

- **Flight and certification milestones:** company timeline says the EL2 Goldfinch first flew on **"November 11, 2023"**, later proved Ultra Short takeoff/landing in **"less than 150 ft"**, and Electra submitted an FAA Part 23 type-certification application for the nine-passenger EL9 in **"December 2025"**.
- **Commercial demand (self-reported):** homepage/company/preorder pages say **"more than 2,200 aircraft on pre-order"** from **"over 60 operators"**; the preorder release says the pipeline is **"valued at nearly $9 billion"**.
- **Launch/customer proof:** company timeline says Bristow signed a Pre-Delivery Payment deposit agreement with binding terms for the first EL9 delivery slot; the preorder page lists Bristow, JSX, Surf Air, JetSetGo, Blade India, Flapper, flyv, LYGG, and other operators.
- **Strategic partners and investors:** company page says Honeywell agreed to supply safety-critical flight-control computers and actuation and became a strategic investor alongside Lockheed Martin and Safran; defense page also lists Lockheed Martin, Honeywell, and Safran as defense partners.
- **Funding/programs:** company page says Electra raised **"$115 million in Series B funding"** in April 2025 to enter pre-production/certification, and that the U.S. Air Force awarded a Strategic Funding Partnership **"valued up to $85M"** in January 2023.
- **Defense/government signals:** defense page lists government customers/logos for U.S. Air Force, U.S. Army, U.S. Navy, and NASA, and positions Donn Yates as VP/GM Electra Defense with retired senior military advisors.

## Visual & brand impression

The site feels like polished aerospace hardware rather than a consumer travel app: full-bleed aircraft video, hangar/runway photography, technical renderings, and direct shots of the yellow-and-black demonstrator. The identity is high-contrast black/white with a bright yellow accent, squared technical typography, and big declarative section titles ("Opening a New Era of Aviation", "People. Power. Payload. Anywhere."). The visuals make the aircraft itself the first-viewport signal and repeatedly show runway/field/defense contexts to reinforce the short-field claim.

## Strategic read

Electra's clearest wedge is practical infrastructure independence: make a fixed-wing aircraft act more like a helicopter at the edge, while keeping range, payload, cost, and certification closer to conventional aviation. That lets the same EL9 story stretch across regional passenger routes, cargo, and defense logistics without needing a separate product family. The risk visible from the site is stage: the profile is heavy on pre-orders, milestones, and partner commitments, while public pricing, production delivery terms, and certification completion are not shown.

## Provenance

- **Pages:** 8 pages captured with Firecrawl on 2026-06-14: home, company, technology, defense, direct-aviation, team, preorders, and product_configuration.
- **Verify:** `fc.py verify` passed: all source URLs matched, all bodies unique, no junk soft-404s.
- **Structured layer:** no JSON-LD on homepage; nav region exposed top-level nav plus X, LinkedIn, and YouTube anchors. RawHtml/metadata showed Statamic; branding payload's Tailwind guess was ignored.
- **Run profile:** guided — +logos.
- **Credits:** 9 credits spent (1 map + 8 page scrapes; logos measured from cached/curl-fetched assets, no Firecrawl credit).
- **Couldn't get:** public EL9 pricing/procurement terms; EL9 PDF brochure was linked but not scraped; headcount/revenue/ownership not stated on captured pages.
