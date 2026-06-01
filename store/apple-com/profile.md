---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: apple.com
name: Apple
aliases: []
parent: []
owns: []
socials: { youtube: "https://www.youtube.com/user/Apple", linkedin: "https://www.linkedin.com/company/apple", facebook: "https://www.facebook.com/Apple", x: "https://www.twitter.com/Apple" }   # JSON-LD sameAs
external: { wikidata: "http://www.wikidata.org/entity/Q312" }   # JSON-LD sameAs — third-party record

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "apple.com → 301 → www.apple.com (strip www). Genuinely custom front-end (Apple's `ac-*` global-nav / `/assets/` stack — NO standard framework markers; one of the rare cases where 'custom' is correct, not a designSystem misread). The complete mega-nav renders into homepage markdown (every product flyout + Explore/Shop/More groups) — use the homepage, not /map, for IA. The /map is flooded with subdomain noise (support./developer./apps./music./discussions.) and is useless for the marketing-site product set; filter to netloc=www.apple.com or just read homepage links (179 www links). Product pages carry verbatim 'From $X or $Y/mo.' pricing inline (mac page). No bot-defense or geo issues hit on US capture; all 7 pages md5-unique."
key_pages:
  homepage: /
  iphone: /iphone/
  mac: /mac/
  services: /services/
  apple_intelligence: /apple-intelligence/
  retail: /retail/
  environment: /environment/
  store: /us/shop/goto/store
  apple_one: /apple-one/

unverified_fields:
  - "Per-SKU prices beyond Mac entry tiers — most product pages route to the shop funnel; only Mac page captured 'From $X' anchors this run."
  - "Headcount, revenue mix (hardware vs. Services), funding — not on the marketing site; a deep-research job, not capture."

description: "Designs and sells premium consumer hardware — iPhone, Mac, iPad, Apple Watch, Vision Pro, AirPods — built on its own silicon and operating systems, monetized one-time at sale plus a growing tier of subscription services (App Store, iCloud+, Apple Music, TV+, Pay)."

# Classification
entity_type: Company
target_market: [B2C, B2B, B2G]
offering_category: [Physical Products / Hardware, Media / Content, Software / SaaS, Financial / Fintech Products]
portfolio_shape: Catalog
business_model: Transactional / One-time
primary_industry: Technology

# Visual identity
logo_url: https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202604211141
brand_colors: { primary: "#0071E3", background: "#FFFFFF", text: "#1D1D1F" }  # STRAIN: #0071E3 is the link/CTA blue; the true brand identity is monochrome black-on-white (see Visual section)
fonts: [SF Pro Display, SF Pro Text]
color_scheme: light
design_framework: custom
---

## Overview

Apple designs, makes, and sells a tightly integrated line of consumer electronics — iPhone, Mac, iPad, Apple Watch, Apple Vision Pro, AirPods, and home/TV devices — each running Apple's own operating systems on Apple silicon. The site presents the company as a single vertically-integrated stack: hardware, software, and a layer of recurring services (App Store, iCloud+, Apple Music, Apple TV, Arcade, Fitness+, News+, Pay/Card) that bind devices together. The dominant pitch across pages is the integrated experience, privacy, and design quality rather than spec-sheet competition.

## What they offer

A **catalog** too broad to enumerate — captured by shape, not list. Two layers:

- **Hardware (the revenue core, sold one-time):** iPhone (17 Pro / 17 / 17e / Air), Mac (MacBook Neo, MacBook Air, MacBook Pro, iMac, Mac mini, Mac Studio, Displays), iPad (Pro / Air / iPad / mini), Apple Watch (Series 11 / SE 3 / Ultra 3 / Hermès / Nike), Apple Vision Pro, AirPods (4 / Pro 3 / Max 2), TV & Home (Apple TV 4K, HomePod / mini), and accessories (incl. Beats, AirTag). Entry pricing quoted inline: *"MacBook Neo … From $599 or $49.91/mo. for 12 mo."*, *"MacBook Air … From $1099 or $91.58/mo. for 12 mo."*
- **Services (the recurring layer, subscription):** App Store, iCloud+, **Apple One** (the bundle), Apple Music (*"All music. Highest audio quality. Zero ads."*), Apple TV, Apple Arcade, Apple Fitness+, Apple News+, Apple Podcasts, Apple Books, plus Wallet / Apple Pay / Apple Card / Apple Cash and AppleCare.
- **Cross-cutting:** **Apple Intelligence** (the on-device AI layer — *"AI for the rest of us."*) is positioned as a feature spanning all devices, not a separate product.

## How it works / model

Two intertwined revenue engines. **Hardware is sold outright** (transactional / one-time), increasingly with monthly financing, trade-in credit (*"up to $195–$695 … when you trade in iPhone 13 or higher"*), and carrier deals lowering the entry price. **Services run on subscription**, individually or bundled via Apple One, and are the growth/lock-in layer layered on the installed device base. Distribution is omnichannel: the online Apple Store, ~physical Apple Store retail (Genius Bar, in-store sessions, Personal Setup), plus carrier/education/business/government channels. The integration across device + OS + service is the moat and the up-sell mechanism.

## Positioning & audience

Primarily **B2C** premium consumers ("tech-savvy consumers," per the site's own tone), with dedicated **B2B** (Business, Enterprise, Mac for Business), **education** (college/K-12 buying), and **government** storefronts. The claimed edge is the integrated hardware-software-services experience, design, and **privacy** (a recurring theme — *"Your data. Just where you want it."*; Apple Intelligence *"Designed with groundbreaking privacy at every step."*). Competes against the entire device landscape (Android/Samsung, Windows PCs, streaming/music incumbents) but rarely names rivals — it positions on switching ease (*"Switch from Android"*, *"Switch from PC to Mac"*) and resale value (*"iPhone holds its value longer than other smartphones"*).

## Nav structure

The global mega-nav is product-category-first; each category opens Explore / Shop / More groups.

```
- Store — /us/shop/goto/store
  - Shop the Latest, Mac, iPad, iPhone, Apple Watch, Apple Vision Pro, AirPods, Accessories
  - Quick Links: Find a Store, Order Status, Apple Trade In, Financing, Personal Setup
  - Special Stores: Certified Refurbished, Education, Business, Veterans & Military, Government
- Mac — /mac/
  - Explore: MacBook Neo, MacBook Air, MacBook Pro, iMac, Mac mini, Mac Studio, Displays, Compare, Switch from PC
  - More: macOS Tahoe, Apple Intelligence, Apps by Apple, Apple Creator Studio, Continuity, iCloud+, Mac for Business
- iPad — /ipad/
  - Explore: iPad Pro, iPad Air, iPad, iPad mini, Apple Pencil, Keyboards, Compare
  - More: iPadOS 26, Apple Intelligence, iCloud+, Education
- iPhone — /iphone/
  - Explore: iPhone 17 Pro, iPhone Air, iPhone 17, iPhone 17e, iPhone 16, Compare, Switch from Android
  - More: iOS 26, Apple Intelligence, iPhone Privacy, Continuity, iCloud+, Wallet/Pay/Card, Siri
- Watch — /watch/
  - Explore: Series 11, SE 3, Ultra 3, Nike, Hermès, Compare, Why Apple Watch
  - More: watchOS 26, Apple Watch For Your Kids, Apple Fitness+
- Vision — /apple-vision-pro/
  - Explore: Apple Vision Pro, Tech Specs · More: visionOS 26, Vision Pro for Enterprise
- AirPods — /airpods/
  - Explore: AirPods 4, AirPods Pro 3, AirPods Max 2, Compare
  - More: Hearing Health, Apple Music, Apple Fitness+
- TV & Home — /tv-home/
  - Explore: Apple TV 4K, HomePod, HomePod mini
  - More: Apple TV app, Apple TV, Home app, Apple Music, Siri, AirPlay
- Entertainment — /services/
  - Apple One, Apple TV, Apple Music, Apple Arcade, Apple Fitness+, Apple News+, Apple Podcasts, Apple Books, App Store
- Accessories — /us/shop/goto/buy_accessories
  - Made by Apple, Beats, AirTag, Assistive Technologies
- Support — support.apple.com (Community, Check Coverage, Genius Bar, Repair, AppleCare)
```

## Credibility & proof

The brand itself is the trust signal — no testimonial/press-logo wall is needed. Proof surfaces instead as: a global physical-retail footprint (store locator, Genius Bar, in-store sessions); Apple Trade In and AppleCare; WWDC (developer conference, "June 8–12"); and a deep **Environment** program with concrete, science-based claims — *"Apple 2030"* carbon-neutral goal, *"reduce … greenhouse gas emissions by 75% compared with 2015,"* 100% recycled cobalt in batteries, the "Daisy" disassembly robot ("200 devices disassembled per hour"), and the Restore Fund. Privacy is presented as a credentialed differentiator throughout.

## Visual & brand impression

Reference-grade design maturity. The homepage is a vertical stack of full-bleed product heroes on a white canvas — iPhone 17 Pro in cosmic orange, MacBook Air in sky blue — each with a one- or two-word headline (*"All out Pro." / "Magichromatic." / "Now supercharged by M5."*) and minimal Learn-more/Buy CTAs. The identity is fundamentally **monochrome**: black/near-black text (#1D1D1F) and the black Apple mark on white, with photography supplying all the color; the only chromatic accent is the system link/CTA blue (#0071E3). Typography is Apple's proprietary **SF Pro** (Display for headlines, Text for body). The overall feel is calm, confident, premium, product-as-hero — the design language the rest of the DTC world imitates.

## Strategic read

The site quietly tells the bull story: a hardware **catalog** so deep it can't be listed, wrapped in a services layer (Apple One, iCloud+, TV, Music, Pay) that converts one-time device buyers into recurring subscribers — the margin-and-retention flywheel. **Apple Intelligence** is deliberately framed as a cross-device *feature*, not a standalone AI product, keeping the integration story central and privacy as the wedge against cloud-AI rivals. For a company-research store dominated by DTC telehealth, Apple is the opposite archetype — `Catalog` shape, hardware-primary, transactional-first with subscription overlay — a useful classification stress-test for the taxonomy (the multi-select `offering_category` and dual hardware/subscription model are doing real work here).

## Provenance

- **Pages:** homepage (full mega-nav + hero stack + branding/screenshot), /iphone/, /mac/ (verbatim pricing), /services/ (services + Apple One), /apple-intelligence/, /retail/ (store locator), /environment/ — 7 pages via Firecrawl (`fc.py`, US location, `maxAge:0`, full-format); `/map` discarded as subdomain noise; IA and product set from homepage links; no geo/cache contamination, no bot defense.
- **Verify:** all md5-unique (clean).
- **Credits:** not recorded this run.
- **Couldn't get:** per-SKU pricing behind the shop funnel; financials/headcount (off-site, out of scope).
- **Migrations:** 2026-06-01 v1→v2.0 — offering_category remapped by rule (not re-captured): Hardware / Physical Products → Physical Products / Hardware.
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-05-31 rawHtml, hint-to-verify) — filled `socials` (youtube/linkedin/facebook/x) + `external` (wikidata); JSON-LD `logo` is lateral to the existing OG logo — kept current. Re-stamped 2.0→2.2.
