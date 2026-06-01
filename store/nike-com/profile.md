---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: nike.com
name: Nike
aliases: []
parent: []
owns: ["converse.com", "Jordan Brand", "NikeSKIMS"]   # STRAIN: Jordan = nike.com/jordan (no own domain); NikeSKIMS = Nike×SKIMS JV, also on-site

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Next.js SPA (rawHtml __NEXT_DATA__/_next/ — branding.designSystem says 'bootstrap', wrong). Full mega-nav + footer IA render into homepage markdown — that's the discovery surface, not the map (map returns thousands of /t/ product + /w/ category URLs plus heavy locale subtrees /de /gb /jp …, mostly noise). branding.colors returns the rotating homepage CAMPAIGN palette (volt/pink/orange), NOT brand identity — Nike's identity is black swoosh on white; verify against the screenshot. about.nike.com is a separate newsroom-style host (en path), heavy on football PR. Membership is free; pricing lives only on PDPs (/t/...)."
key_pages:
  home: /
  men: /men
  women: /women
  kids: /kids
  jordan: /jordan
  nikeskims: /nikeskims
  sport: /gear-up
  membership: /membership
  about: https://about.nike.com/en
  find_a_store: /retail
  snkrs_launch: /launch
unverified_fields:
  - "Per-product pricing — lives on product detail pages (/t/...), none captured this run."
  - "Homepage hero & 'Latest in Hoops' carousel are a point-in-time snapshot, not fixed — rotating merchandising; captured state differs run-to-run."
  - "Financials, headcount, revenue split (DTC vs wholesale) — not on the consumer site; a deep-research job."

description: "Designs and sells athletic footwear, apparel, and equipment direct-to-consumer and through wholesale, spanning performance sport and lifestyle, across the Nike, Jordan, and Converse brands."

# Classification
entity_type: Company
target_market: [B2C, B2B]            # B2C dominant (DTC + retail); B2B via wholesale, Corporate Sales, team/federation kit
offering_category: [Physical Products / Hardware]   # maker of footwear/apparel/equipment; the athletic/fashion vertical is not a category
portfolio_shape: Catalog
business_model: Transactional / One-time   # product sales; Nike Membership is a FREE loyalty layer, not a subscription
primary_industry: Sports & Recreation

# Visual identity
logo_url: https://www.nike.com/favicon.ico?v=1   # branding.images.logo is an inline data-URI swoosh SVG → favicon fallback
brand_colors: { primary: "#111111", background: "#FFFFFF" }   # STRAIN: true identity is black swoosh / white; branding API returned campaign colors (volt #BAD168, pink #FF009E, orange #FF7334) — content, not brand
fonts: [Helvetica Now Text, Helvetica Now Display]
color_scheme: light
design_framework: next.js
---

## Overview

Nike is the world's largest athletic-goods company, selling footwear, apparel, equipment, and
accessories for sport and everyday lifestyle. The consumer site (`nike.com`) is a global
direct-to-consumer storefront organized by gender (Men / Women / Kids), by owned brand (Jordan,
NikeSKIMS, Converse), and by sport (basketball, running, soccer, training, tennis, golf, and a long
tail from baseball to skateboarding). Its self-description is broad and identity-driven rather than
category-driven: *"Inspiring the world's athletes, Nike delivers innovative products, experiences and
services"* — and, on about.nike.com, *"If you have a body, you are an athlete."*

## What they offer

A `Catalog`-scale assortment — too large to enumerate; the shape is what matters:

- **By audience:** Men, Women, Kids (Big / Little / Baby & Toddler), Teens.
- **By owned brand:** **Jordan** (the dominant sub-brand, full Men/Women/Kids lines + its own sport
  range), **NikeSKIMS** (Nike × SKIMS women's collection — bras, leggings, the "Studio Stretch"
  material story), **Converse** (linked, but transacts on its own domain).
- **By product type:** Shoes, Clothing, Accessories & Equipment — each subdivided per sport.
- **By sport:** Basketball, Running, Soccer, Training & Gym, Tennis/Court (+ Pickleball), Golf, plus
  Baseball, Cheer, Football, Gymnastics, Lacrosse, Skateboarding, Softball, Swimming, Volleyball,
  Wrestling, and ACG (All Conditions Gear). "Locker Room" carries licensed league gear (NBA, NFL,
  MLB, WNBA, NCAA, NWSL).
- **Innovation platforms (footer "Guides"):** Air, Air Force 1, Air Max, FlyEase, Flyknit, Free,
  React, Vaporfly, ZoomX, Space Hippie — the technology franchises Nike markets as durable IP.
- **Services:** Nike By You (customization), SNKRS (launch/drops), and the app ecosystem (below).

## How it works / model

Primarily **transactional product sales** through three channels: nike.com DTC, owned retail
(Find a Store), and wholesale. Revenue is one-time purchase, not subscription.

**Nike Membership is a free loyalty layer**, not a paid tier — *"100% yes [it's free]… Zero money
gets you access to all of it."* Member benefits, quoted: **free shipping on $50+ orders**, a
**60-day Wear Test** ("Try it for 60 days—return if it's not a fit"), **receiptless returns**,
member-only experiences/events, and expert sport/style advice. Membership unlocks an app ecosystem —
**Nike App** (personalized shopping), **Nike Run Club (NRC)**, **Nike Training Club (NTC)**, and
**SNKRS** (sneaker drops/community) — that doubles as the engagement + DTC funnel.

## Positioning & audience

Positions as the premium performance-and-culture leader across essentially every sport and the
lifestyle/streetwear adjacent to it. The brand voice is aspirational and inclusive — the about-page
manifesto ("WE SERVE KIDS, PROS, DREAMERS, WOMEN, TEAMS, COACHES, MEN… athletes") deliberately
widens "athlete" to everyone. Athlete and team endorsements (Jalen Brunson, Sabrina Ionescu, Devin
Booker, LeBron, Kobe; federations like Paris Saint-Germain, Brasil) are the primary proof and
merchandising engine.

## Nav structure

```
- Men — /men
  - New & Featured: New Arrivals, Best Sellers, Latest Drops, SNKRS Launch Calendar, Shop All Sale
  - Shoes: All, Basketball, Jordan, Lifestyle, Running, Sandals & Slides, Soccer, Training & Gym, Custom (Nike By You)
  - Clothing: All, Hoodies & Sweatshirts, Jackets & Vests, Pants, Shorts, Swim, Tops & Graphic Tees
  - Accessories: All, Bags & Backpacks, Hats & Headwear, Socks
- Women — /women
  - New & Featured; Shop by Color (Crimson, Dark Neutrals, Light Magenta, Orange Pulse, Steam Green, University Blue, Warm Neutrals)
  - Shoes: All, Basketball, Jordan, Lifestyle, Running, Sandals & Slides, Soccer, Training & Gym, Custom
  - Clothing: All, Bras, Hoodies, Leggings, Matching Sets, Jackets, Pants, Shorts, Skirts & Dresses, Swim, Tops
  - Accessories: All, Bags & Backpacks, Hats & Headwear, Socks
- Kids — /kids
  - New & Featured; Nike x LEGO® Collection; Teens
  - Shoes by age: Big (7–15), Little (3–7), Baby & Toddler (0–3); + Basketball, Jordan, Lifestyle, Running, Sandals, Soccer
  - Clothing by age + Bras & Tights, Hoodies, Matching Sets, Jackets, Pants, Shorts, Skirts & Dresses, Swim, Tops
  - Accessories: Bags & Backpacks, Hats & Headwear, Socks
- Jordan — /jordan
  - New & Featured, Best Sellers, Heat Check, Jordan x Brasil Futebol
  - Men / Women / Kids (each: Shop All, Shoes, AJ1, Clothing, Accessories)
  - Sport: Basketball, Golf, Cleats
- NikeSKIMS — /nikeskims
  - Shoes (NikeSKIMS Rift); Clothing (Bras, Jackets, Leggings, Shorts, Tops & Tanks, Accessories)
  - Shop by Color / Material (Shine, Matte, Airy, Seamless, Stretch Knit, Studio Stretch)
  - Guides: Lookbook, Bra Guide, Fabric Guide
- Sport — /gear-up
  - Basketball (Kobe, Jordan, LeBron) — /basketball
  - Court — /tennis (Tennis, Pickleball)
  - Soccer — /soccer (Federation Kits, Cleats, Indoor)
  - Training — /training
  - Running — /running (Road, Race, Trail, Track & Field, Running Shoe Finder)
  - Golf — /golf
  - More Sports: Baseball, Cheer, Football, Gymnastics, Lacrosse, Skateboarding, Softball, Swimming, Volleyball, Wrestling
  - Locker Room: NBA, NFL, MLB, WNBA, NCAA, NWSL, Soccer Clubs, Federations
  - ACG — /acg (Trail Run, Hike, Explore)
- Jordan — /jordan   (also a top-level entry)
- Converse — /w/converse-akmjx   (links out; transacts on converse.com)
Top utility: Find a Store (/retail) · Help (/help) · Join Us / Membership (/membership) · Sign In · Ask NikeAI (search)
Footer — Company: About (about.nike.com), News, Careers, Investors, Purpose, Sustainability, Accessibility
Footer — Promotions: Student, Military, Teacher, First Responders & Medical, Birthday discounts
```

## Credibility & proof

Global market leadership and ubiquity are the implicit proof; explicit signals on-site: deep athlete
and federation roster (PSG "back-to-back European Champions," national teams, NBA/WNBA stars),
licensed-league partnerships across NBA/NFL/MLB/WNBA/NCAA/NWSL, and an innovation narrative
(neuroscience-based "Nike Mind" footwear, Aero-FIT cooling apparel, Vaporfly/ZoomX). Buyer-trust
mechanics: 60-day Wear Test guarantee, free returns/receiptless returns, free member shipping, and a
documented accessibility program.

## Visual & brand impression

Stark, confident, image-first. White background, black monochrome chrome, the black Swoosh as the
only persistent mark — the homepage is edge-to-edge product and athlete photography (a red Air Jordan
4 "THE WAIT IS OVER" hero, a "Latest in Hoops" athlete carousel) with minimal text and small black
pill CTAs ("Shop," "Explore"). Typeface is Helvetica Now (Text + Display), reinforcing the clean,
high-contrast, premium-mass feel. The design system is mature and template-driven; brand color is
deliberately *neutral* (black/white) so the rotating product imagery and its campaign colors carry
all the visual energy.

## Provenance

- **Pages:** homepage (`/`), about (`about.nike.com/en`), membership (`/membership`) — 3 pages, all Firecrawl scrape, US geo; map captured (~thousands of product/category URLs, locale-heavy) but used only to confirm Catalog scale; key pages came from homepage links. Full-page screenshot captured (brand visual read); Next.js confirmed from rawHtml (`__NEXT_DATA__`).
- **Verify:** all sourceURLs matched, all 3 bodies md5-unique (clean; no geo/cache contamination).
- **Credits:** ~5 credits spent.
- **Couldn't get:** product detail pages / pricing (lives on `/t/...` PDPs, none captured), Converse (separate domain), the gated app experiences.
- **Migrations:** 2026-06-01 v1→v2.0 — offering_category remapped by rule (not re-captured): Apparel & Footwear → Physical Products / Hardware.
