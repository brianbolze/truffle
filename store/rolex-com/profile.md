---
schema_version: 1

# Identity
domain: rolex.com
name: Rolex
aliases: []
parent: []                           # site states "independent"; ownership not asserted on captured pages
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Locale-prefixed paths (/en-us/…); root rolex.com 403s (Akamai) but Firecrawl renders fine. Custom React SPA (Create React App: /static/js/main.<hash>.js) — Adobe markers are just Launch/DTM analytics, not the CMS. /watches catalog page is a thin SPA grid (~480c, model families come from homepage mega-nav, not that page). No prices anywhere on the site — Rolex sells only through authorized Official Jewelers (configurator + store-locator, no cart/e-commerce). Map (500 urls) is dominated by /rolex-dealers/* + ~40 locale subtrees + newsroom.rolex.com — pull signal pages from homepage links. CPO page geo-picker label leaked 'United Kingdom'/en-gb but body content is correct."
key_pages:
  watches: /en-us/watches
  about: /en-us/about-rolex
  behind_the_crown: /en-us/about-rolex/behind-the-crown
  manufactory: /en-us/watchmaking/manufactory
  cpo: /en-us/buying-a-rolex/rolex-certified-pre-owned
  daytona: /en-us/watches/cosmograph-daytona
  oyster_story: /en-us/oyster-story
  configure: /en-us/watches/configure
  store_locator: /en-us/store-locator
unverified_fields:
  - "No pricing published anywhere on the site — Rolex sells exclusively through authorized Official Jewelers; the site offers a configurator and store/service locators, no cart or e-commerce. No price data could be captured."
  - "Ownership/parent not asserted on captured pages (about page calls Rolex 'integrated and independent'); not recorded from memory."
  - "Headcount, revenue, and a precise founding date are not stated on the captured marketing pages (founder Hans Wilsdorf and the 1926 Oyster are; a /history/1905-1919 chapter implies a 1905 origin but the year isn't on the captured pages)."

description: "Swiss luxury watch manufacture that designs, develops and produces its mechanical Oyster timepieces almost entirely in-house in Geneva, selling them worldwide through a network of authorized Official Jewelers."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Hardware / Physical Products]   # manufactured precision timepieces; brand frames itself as a "manufacture," not fashion apparel
portfolio_shape: Catalog
business_model: Transactional / One-time
primary_industry: Consumer Goods

# Visual identity
logo_url: https://static.rolex.com/icons/rolex_fav_icon.png   # branding.images.logo is the inline data-URI gold-crown SVG; favicon used as the hostable fallback
brand_colors: { primary: "#127749", accent: "#D4AF37" }   # Rolex green (branding payload: #329066/#127749) + the gold crown; verified against screenshot
fonts: [Helvetica Now Text]
color_scheme: light
design_framework: react   # Create React App SPA (/static/js/main.<hash>.js); read from rawHtml, not branding.designSystem ("custom")
---

## Overview

Rolex is an integrated, independent Swiss watch *manufacture* headquartered in Geneva. It designs, develops, and produces the majority of its watch components in-house, building mechanical wristwatches around the Oyster waterproof case and the Perpetual self-winding rotor — the two innovations from founder Hans Wilsdorf that anchor a century-long "quest for excellence" narrative. The company sells a tightly curated, high-precision collection of luxury timepieces and backs them with its own "Superlative" quality certification, worldwide service network, and a Certified Pre-Owned programme. Rolex pairs the product with a large patronage platform across sport, the arts, exploration, and the environment ("Perpetual Initiatives").

## What they offer

A single product universe — luxury mechanical watches — organized into Classic and Professional model families (no public pricing; sold via Official Jewelers). The named lines:

- **Datejust / Lady-Datejust:** the archetypal Classic dress watch (datejust, lady-datejust)
- **Day-Date:** the prestige "President" line (day-date)
- **Oyster Perpetual:** the entry-classic, time-only Oyster (oyster-perpetual)
- **Land-Dweller:** newest Classic line, transparent case back (land-dweller)
- **Sky-Dweller / 1908 / Air-King:** dual-time, formal "1908," and pilot heritage models
- **Cosmograph Daytona:** flagship motorsport chronograph, tachymetric bezel, launched 1963 (cosmograph-daytona)
- **Submariner / Sea-Dweller / Deepsea:** dive Professional watches at escalating depth ratings
- **GMT-Master II:** dual-timezone traveler's watch (gmt-master-ii)
- **Explorer / Explorer II:** exploration Professional line
- **Yacht-Master / Yacht-Master II:** sailing/regatta watches
- **New watches 2026:** the current-year releases hub (new-watches)
- **Accessories:** straps and small goods (accessories)
- **Certified Pre-Owned (RCPO):** factory-backed second-hand programme — watches ≥2 years old, sold by Official Jewelers with a Rolex plaque, fully serviced, with a **two-year international guarantee** and a distinct seal + guarantee card

Catalog-shaped: ~17 model families, each spanning many references (materials, dials, sizes) — far more SKUs than are enumerable here. Per-reference depth (e.g. the Daytona's m126500ln-0001, Oystersteel, 40 mm) defers to `offerings.md`.

## How it works / model

- **No direct e-commerce.** Rolex does not sell or price watches online. The journey is: browse the collection or use **"Configure your Rolex"** / **"Find your Rolex"** → locate an **Official Jeweler** via the store locator → purchase in person. Revenue is a one-time transactional sale of the timepiece.
- **Vertical integration.** Components, cases, and calibres are made in-house ("the brand designs, develops and produces the majority of its watch components in-house"), governed by an internal **"Superlative"** quality-control unit certifying precision, water resistance, autonomy, robustness, and durability.
- **Lifecycle aftermarket.** A worldwide network of service centers ("our servicing philosophy," "caring for your Rolex") plus the RCPO programme extends ownership and resale under the brand's own guarantee — framed as both quality and sustainability.

## Positioning & audience

Targets affluent consumers buying a precision status object built to last ("made to last," "withstand the test of life"). The claimed edge is the *manufacture* itself — a self-contained, founder-rooted house of in-house innovation (the first waterproof wristwatch, the Perpetual rotor) and uncompromising quality ("We would never sell a single timepiece that is not technically faultless" — Hans Wilsdorf). Competes against other haute-horlogerie maisons on heritage, reliability, and resale durability rather than price (never shown) or breadth.

## Nav structure

```
- Rolex watches and accessories — /en-us/watches
  - Classic: Oyster Perpetual, Datejust, Lady-Datejust, Day-Date, Land-Dweller, Sky-Dweller, 1908, Air-King
  - Professional: Cosmograph Daytona, Submariner, Sea-Dweller, Deepsea, GMT-Master II, Explorer, Explorer II, Yacht-Master, Yacht-Master II
  - New watches 2026 — /en-us/watches/new-watches
  - Find your Rolex — /en-us/watches/find-rolex  (Men's /man · Women's /woman · Gold /gold)
  - Configure your Rolex — /en-us/watches/configure
  - Accessories — /en-us/accessories
- Watchmaking — /en-us/watchmaking/excellence-in-the-making
  - At the core of excellence — /watchmaking/excellence-in-the-making/quest-for-excellence
  - Behind the seal (Manufactory) — /en-us/watchmaking/manufactory
  - Rolex anatomy (Features) — /en-us/watchmaking/features
- Oyster Story — /en-us/oyster-story
  - The film — /oyster-story/oyster-film
  - The exhibition — /oyster-story/oyster-exhibition
- About Rolex — /en-us/about-rolex
  - Sustainability — /about-rolex/sustainable-development
  - Behind the crown — /about-rolex/behind-the-crown
  - History — /about-rolex/history/1905-1919
- Sports, Arts and Planet
  - Rolex and sports — /en-us/rolex-and-sports
  - Perpetual Planet — /perpetual-initiatives/perpetual-planet
  - Perpetual Arts — /perpetual-initiatives/perpetual-arts
  - The Rolex family — /en-us/rolex-family
- Buying and servicing
  - Buying a Rolex — /buying-a-rolex/experiencing-a-rolex
  - Rolex Certified Pre-Owned — /buying-a-rolex/rolex-certified-pre-owned
  - Servicing your Rolex — /watch-care-and-service/our-servicing-philosophy
  - Caring for your Rolex — /watch-care-and-service/caring-for-your-rolex
  - Store locator — /en-us/store-locator
  - Service Center locator — /watch-care-and-service/service-locator
  - FAQ — /watch-care-and-service/faq
  - Media: Wallpapers / Brochures / User guides — /en-us/media/*
```

## Credibility & proof

- **Founder & heritage:** Hans Wilsdorf, the Oyster (first waterproof wristwatch, 1926), the Perpetual self-winding rotor — innovations positioned as marking "the history of global watchmaking."
- **"Superlative" certification:** an in-house quality-control standard and unit ("standards are unparalleled") spanning precision, water resistance, autonomy, robustness, durability.
- **Patronage at scale:** Rolex Testimonees and partnerships across tennis (Roland-Garros), motorsport (Goodwood Revival, Pebble Beach, Rolex Monterey Motorsports Reunion), equestrianism, yachting (SailGP), the arts (Mentor and Protégé, cinema), and the environment (Perpetual Planet).
- **Guarantees:** RCPO carries a two-year international guarantee with seal + guarantee card; "fully serviced … using our scrupulously maintained stock of genuine replacement parts."

## Visual & brand impression

Restrained luxury. The homepage is a full-bleed editorial sequence — a Roland-Garros hero (BNP Paribas court), a hero "Rolex collection" shot of a Datejust on a clean light ground, then patronage and Perpetual-Initiatives panels — separated by generous whitespace. Light color scheme, near-black body type set in Helvetica Now Text, and the signature **green-and-gold** identity (Rolex green accents, the gold crown logo). Heavy use of autoplay video and responsive landscape/portrait/square art per module. The overall feel is premium, editorial, and confident — selling provenance and craft, not transactions; there is no price, no cart, no urgency anywhere on the page.

## Strategic read

Rolex is the rare luxury maker whose website is deliberately *not* a store — it's a brand cathedral plus a locator. The entire commercial funnel routes to in-person Official Jewelers, which keeps pricing, allocation, and scarcity off the public web and under the brand's (and its retail network's) control. The RCPO programme is the strategically interesting move: by certifying and guaranteeing second-hand watches itself, Rolex inserts the manufacture into the lucrative, previously third-party-dominated pre-owned market and reframes resale durability as a sustainability story — extending its margin and its quality narrative across the full ownership lifecycle.

## Provenance

- **Pages:** 8 analyzed (Firecrawl scrape, all-formats homepage + 7 key pages): homepage, /watches, /about-rolex, /about-rolex/behind-the-crown, /watchmaking/manufactory, /buying-a-rolex/rolex-certified-pre-owned, /watches/cosmograph-daytona, /oyster-story. Map (500 urls) used for inventory only.
- **Verify:** all 8 sourceURLs matched; all 8 body md5s unique (no §5.1 geo/cache contamination). /watches returned thin (~480c SPA grid) — model families recovered from homepage mega-nav. CPO page geo-label showed en-gb but body content is correct.
- **Credits:** 9 (1 map + 1 homepage + 7 key pages); see `fc.py spend`.
- **Couldn't get:** any pricing (none published — Official-Jeweler sales only); ownership/parent (not asserted on site); headcount/revenue/founding year (not on captured marketing pages).
