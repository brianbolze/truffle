---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: etsy.com
name: Etsy
aliases: ["Etsy, Inc."]
parent: []
owns: [reverb.com, depop.com]            # "house of brands" — consolidated figures span Etsy + Reverb + Depop (/press)
socials: { facebook: "https://www.facebook.com/Etsy", x: "https://x.com/etsy", instagram: "https://www.instagram.com/etsy/", pinterest: "https://www.pinterest.com/etsy/", youtube: "https://www.youtube.com/@Etsy", tiktok: "https://www.tiktok.com/@etsy", linkedin: "https://www.linkedin.com/company/etsy" }   # JSON-LD sameAs

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Marketplace app-shell homepage carries little positioning — self-description lives on /about, /press, /sell, /categories. Map returns ~all listing/market/shop noise (the catalog); pull corporate pages from homepage links. Corporate metrics on /press are consolidated (Etsy+Reverb+Depop, dated 'as of Dec 31 2025'); /about stats are an older Etsy-marketplace-only snapshot. Full fee schedule on /sell. Investor site: investors.etsy.com (NASDAQ: ETSY). branding.designSystem said 'bootstrap' (wrong); real stack = custom React/webpack SPA per rawHtml. Logo is an inline data-URI SVG — favicon fallback used."
key_pages:
  about: /about
  sell: /sell
  press: /press
  impact: /impact
  categories: /categories
  investors: https://investors.etsy.com
unverified_fields:
  - "Two non-reconciling figure-sets captured: /about shows 45M items / 1.9M active sellers / 31.7M active buyers (UNDATED, no scope note); /press shows 100M+ listings / 8.7M sellers / 93.5M buyers / $11.9B GMS, labelled 'as of Dec 31, 2025' and 'consolidated to include Etsy, Reverb, and Depop'. Treated /press as authoritative (dated + scoped). The reason /about is lower (stale page vs. Etsy.com-only scope) is NOT stated on the page — do not assert a cause."
  - "/impact figures are dated 2022–2023 (e.g. $3.6B seller income 2022) — point-in-time, not current."
  - "Publicly traded (captures link SEC filings + investor relations at investors.etsy.com) — but the specific exchange/ticker is NOT on any captured page."
  - "owns: reverb.com, depop.com — brand NAMES are captured (the /press consolidation line); their domains were assigned, not curl-resolved this run, and what each brand sells was not captured."

# Description
description: "A global online marketplace for handmade, vintage, and craft-supply goods that connects independent creative-entrepreneur sellers with consumer buyers, earning listing, transaction, payment, and advertising fees on each sale."

# Classification
entity_type: Company
target_market: [B2C, B2B]                # consumer buyers (B2C, the brand-facing identity) + small-business sellers who pay fees/tools (B2B)
offering_category: [Marketplace / Platform]
portfolio_shape: Catalog                 # 100M+ listings across 17 top-level categories — capture the shape, not the list
business_model: Marketplace / Commission
primary_industry: Retail & E-Commerce

# Visual identity
logo_url: https://i.etsystatic.com/site-assets/etsy-logo.svg   # JSON-LD `logo` (canonical mark) — supersedes the favicon fallback
brand_colors: { primary: "#FFA300", teal: "#0D424E", cream: "#FAF8F5" }   # STRAIN: orange (#FFA300) is the signature CTA/logo hue (visually confirmed); branding mislabels it "secondary"
fonts: [ABC Diatype, ABC Otto, Charter]
color_scheme: light
design_framework: react                  # rawHtml: React + webpack, no SSG/CMS marker → custom SPA (branding said "bootstrap" — ignored per playbook §5.4)
---

## Overview

Etsy is a global online marketplace for "unique and creative goods" — handmade items, vintage treasures, and craft supplies — sold directly by independent makers and small businesses. Founded in 2005 and headquartered in the DUMBO neighborhood of Brooklyn, NY, it has ~2,400 employees and is publicly traded (the captures link SEC filings and an investor-relations site). Its stated mission is to **"Keep Commerce Human"**: position a people-powered alternative to automated, mass-market e-commerce. Beyond the core Etsy.com marketplace, the company operates a "house of brands" that the `/press` page states also includes **Reverb** and **Depop**.

## What they offer

Etsy doesn't make products — it operates the two-sided marketplace and tooling that connects sellers and buyers. Across the consolidated house of brands (as of Dec 31, 2025):

- **Marketplace (Etsy.com):** 100M+ listings, **8.7M active sellers**, **93.5M active buyers**, **$11.9B** annual gross merchandise sales (2025, consolidated)
- **Seller platform:** shop hosting, listing/inventory tools, payments (Etsy Payments), Offsite Ads, Etsy Ads, shipping tools, plus the Seller Handbook (education) and support specialists
- **Reverb** and **Depop**: the other two marketplaces in the consolidated "house of brands" (named on `/press`; what each sells was not captured this run)

Catalog spans **17 top-level categories** (see Nav). Buyer-side discovery surfaces include curated Editors' Picks, "Gift Mode" gift finder, and registries.

## How it works / model

Two-sided marketplace monetized by **commission + fees on seller transactions**, not subscriptions. Sellers list for **$0.20/listing** (active 4 months or until sold), and pay on each sale. Verbatim fee schedule (/sell):

- **Listing fee:** "$0.20 Listing fee" — "Listings are active for four months, or until they sell."
- **Transaction fee:** "6.5 % Transaction fee" — "a small commission" per sale
- **Payment processing:** "3% + $0.25 payment processing fee" (standard)
- **Offsite Ads fee:** "15% Offsite Ads Fee" — charged only when a sale comes from an Etsy-purchased external ad
- **Currency conversion:** "2.5% Currency Conversion fee" when listing currency ≠ payment-account currency
- **One-time shop set-up fee:** charged at shop creation (amount shown before final setup; varies)
- Stated: "No additional monthly fees."

Buyer journey: search/browse → purchase directly from independent shops → Etsy provides payments, security, fraud detection, and Purchase Protection. Seller journey: open a shop ("20 cents and your imagination") → list → fulfill → pay per-sale fees.

## Positioning & audience

- **Buyers:** consumers seeking "an alternative—something special with a human touch," gifts, custom/personalized, and one-of-a-kind items.
- **Sellers:** "creative entrepreneurs" / makers running shops as a "creative outlet, part-time job, or full-time career," courted with "low fees, powerful tools, and support and education."
- **Claimed edge:** human, handmade, and unique vs. automated mass-market commerce — "Keep Commerce Human." Differentiates on breadth of one-of-a-kind inventory ("the perfect wedding gift and a cape for your bearded lizard").

## Nav structure

```
Shop All Categories (/categories) — 17 top-level:
- Accessories — /c/accessories
- Art & Collectibles — /c/art-and-collectibles
- Bags & Purses — /c/bags-and-purses
- Bath & Beauty — /c/bath-and-beauty
- Books, Movies & Music — /c/books-movies-and-music
- Clothing — /c/clothing
- Craft Supplies & Tools — /c/craft-supplies-and-tools
- Electronics & Accessories — /c/electronics-and-accessories
- Gifts — /c/gifts
- Home & Living — /c/home-and-living
- Jewelry — /c/jewelry
- Kids & Baby — /c/kids-and-baby
- Paper & Party Supplies — /c/paper-and-party-supplies
- Pet Supplies — /c/pet-supplies
- Shoes — /c/shoes
- Toys & Games — /c/toys-and-games
- Weddings — /c/weddings

Discovery / buyer:
- Gift Mode (gift finder) — /gift-mode
- Featured hubs — /featured/hub/{gifts,home-favorites,fashion-favorites}
- Etsy Journal (blog) — /blog/en
- Registry — /registry · Gift cards — /giftcards

Seller / corporate (footer):
- Sell on Etsy — /sell · Affiliates — /affiliates
- About — /about · Careers — /careers · Press — /press · Impact — /impact
- Investors — investors.etsy.com · Community — community.etsy.com
- Developers — developers.etsy.com · Help — /help · Legal — /legal
```

## Credibility & proof

- **Scale (consolidated, Dec 31 2025):** 100M+ listings, 8.7M active sellers, 93.5M active buyers, $11.9B GMS (2025).
- **Publicly traded:** SEC filings, quarterly reports, and governance info at investors.etsy.com (specific exchange/ticker not stated on captured pages).
- **Tenure & footprint:** founded 2005; HQ Brooklyn (DUMBO) plus offices in Dublin, London, and Mexico City; buyers/sellers in "nearly every country in the world"; localized into ~28 country/region storefronts.
- **Buyer trust:** Etsy Purchase Protection, SSL-encrypted payments, 24/7 fraud detection/security specialists.
- **Impact claims:** Net Zero by 2040 (SBTi-approved goal); ~$3.6B income generated for small businesses (2022); Etsy Uplift Initiative + Nest nonprofit partnership; EcoEnclose packaging partnership.

## Visual & brand impression

Clean, editorial, photography-forward storefront — a white/cream (#FAF8F5) canvas with dense product-image grids and lifestyle photography doing the selling. The signature **Etsy orange** (#FFA300) anchors the logo and primary CTAs; a deep indigo/plum footer bar grounds the page. Custom display type (ABC Otto headlines, ABC Diatype body) gives a crafted, design-conscious feel consistent with the "human, handmade" positioning. Mature, well-resourced consumer-brand design — warm and approachable rather than utilitarian-marketplace.

## Strategic read

Etsy is a **catalog-scale, asset-light marketplace**: it owns no inventory and books revenue as a take-rate on seller GMS, so its economics hinge on listing volume, conversion, and fee levels rather than merchandising. The expanding **fee stack** (transaction, payment, Offsite Ads, currency) is the real monetization lever and a recurring source of seller tension — worth tracking as a state change. The **house-of-brands** structure (Reverb, Depop alongside Etsy.com) means the headline 8.7M-seller / $11.9B-GMS figures are *consolidated* across all three, not Etsy.com alone — a meaningful distinction for any competitive comparison, and the likely reason the `/about` and `/press` counts diverge. The "Keep Commerce Human" mission is also a defensive moat narrative against AI-generated/mass-produced listings flooding the platform.

## Provenance

- **Pages:** 6 captured via Firecrawl (maxAge:0, location:US) — homepage, /about, /sell, /press, /impact, /categories; map returned mostly listing/market catalog noise (corporate pages pulled from homepage links). Screenshots in `.payloads/`.
- **Verify:** all 6 sourceURLs matched; all body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 7 (1 map + 6 scrapes), all base 1cr, no enhanced-proxy.
- **Couldn't get:** current Etsy.com-only (non-consolidated) seller/buyer counts — /about carries only an older marketplace-only snapshot; SEC-grade financials live on investors.etsy.com, not captured (deep-research scope).
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-05-31 rawHtml, hint-to-verify) — filled `socials` (fb/x/ig/pinterest/youtube/tiktok/linkedin); upgraded `logo_url` favicon→JSON-LD `logo` (`etsy-logo.svg`); founding already in prose; no `external`. Re-stamped 2.0→2.2.
