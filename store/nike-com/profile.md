---
schema_version: 1

# Identity
domain: nike.com
name: Nike
aliases: [NIKE, Inc.]                 # legal entity NIKE, Inc. (NYSE: NKE); the brand is "Nike"
parent: []
owns: [Jordan, converse.com, Nike SB, ACG, NikeLab, NikeSKIMS]   # owned sub-brands; converse.com has its own domain, the rest live under nike.com / are JVs (NikeSKIMS)

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Enormous catalog — DO NOT enumerate; capture the SHAPE (gender × product-type × sport × franchise). /v2/map returns ~286 URLs that are a RANDOM SAMPLE of PDPs (/t/<slug>/<style-code>) and browse pages (/w/<facets>) across ~12 locale prefixes (/be/ /ph/ /ie/ /at/ /ro/ /au/ /id/ /lu/ /gb/ /us/es/ ...) + corporate subdomains (about.nike.com, investors.nike.com, careers.nike.com, niketeam.nike.com) + sitemap XMLs — useless for completeness, but GOLD for revealing the browse taxonomy and product lines. The TAXONOMY shape lives in (a) the homepage FOOTER (Featured franchises / Shoes-by-sport / Clothing / Kids) and (b) the homepage `links` payload's /w/ facet URLs — the top mega-nav flyouts (Men/Women/Kids dropdowns) are client-rendered (only Men/Women/Kids/Jordan/Converse labels in markdown). One franchise browse page (/w/air-force-1-shoes...) returned 73 product tiles and is itself lazy-loaded/partial — concrete proof the catalog is un-scrapable; stop at the line/franchise level. Pages are large (homepage 42KB, /men 49KB, AF1 hub 74KB). Stack: Next.js/React (rawHtml __NEXT_DATA__ + /_next/ + react) on Akamai/static-nike CDN; branding.designSystem.framework says 'bootstrap' — WRONG (same wrong value AG1 got). branding.images.logo = inline data-URI SVG swoosh (not hostable, like linear/aws) → favicon fallback https://www.nike.com/favicon.ico?v=1. BRAND-COLOR snapshot trap: branding.colors.primary #111111 IS the real brand color (Nike black) but secondary #BAD168 (volt) + accent/link #FF7334 (orange) are CURRENT-CAMPAIGN accents (the 'TOMA June 7' volt event, red Jordan hero), not stable brand hues — Nike's enduring identity is just black swoosh on white. No geo/cache contamination; US+maxAge:0+waitFor:4000-5000 applied. Entity = NIKE, Inc. (investors.nike.com, about.nike.com '— NIKE, Inc.')."
key_pages:
  men: /men                                          # gender hub: Shop by Sport + Shop By Category (Shoes/Clothing/Gear)
  women: /women
  kids: /kids
  jordan: /jordan                                    # Jordan Brand sub-brand hub
  converse: /w/converse-akmjx                        # Converse (Nike-owned; primary site converse.com)
  air_force_1: /w/air-force-1-shoes-5sj3yzy7ok       # flagship sneaker franchise hub (sampled: 73 tiles, partial)
  running: /w/running-5g462                           # sport hub (pattern; running shoes /w/running-shoes...)
  nike_by_you: /w/nike-by-you-shoes-6ealhzy7ok       # customization
  membership: /membership                            # Nike Membership (free loyalty, not a subscription)
  retail: /retail                                     # Find a Store
  about: https://about.nike.com                       # NIKE, Inc. corporate (separate host)
  investors: https://investors.nike.com               # NYSE: NKE
unverified_fields:
  - "Full product catalog — thousands of SKUs, JS-walled + lazy-loaded; only the category/franchise SHAPE is captured, never the SKU list (by design — see site_notes)."
  - "Per-product pricing — on individual PDPs; not enumerated. (Prices ARE in PDP markdown when US-geo'd, like AG1 — not JS-walled like linear.)"
  - "Revenue / segment / headcount — a NIKE, Inc. 10-K fact (investors.nike.com), not on the consumer storefront."
  - "Women's / Kids' full sub-structure — captured Men's as the representative gender hub; Women/Kids mirror it (verified at the footer Kids block)."

# Description — one sentence
description: "Nike is the world's largest athletic footwear and apparel company, designing and selling shoes, clothing, and gear across sports (running, basketball, soccer, training, golf) and iconic sneaker franchises (Air Force 1, Air Max, Jordan, Dunk) to consumers via its own DTC channels and wholesale, under the Nike, Jordan, and Converse brands."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company          # clean — top-level public company (NYSE: NKE). NO parent strain. But it's the PARENT side of the relationship gap: owns Jordan, Converse, etc. (see Identity NOTE).
target_market: [B2C]          # nike.com is a consumer storefront (DTC). Secondary B2B exists off-site (niketeam.nike.com team uniforms; wholesale to retailers; corporate sales) — noted in body, not in the key since the captured site is B2C.
offering_category: [Apparel & Footwear, Retail / E-Commerce]   # Apparel & Footwear (added post-capture) now leads; CPG dropped — it was the forced-fit consumer-goods proxy before the value existed
portfolio_shape: Catalog      # the SCALE EXTREME (alongside AWS): thousands of SKUs across dozens of franchises × sports × demographics — un-enumerable, captured as shape
business_model: Transactional / One-time   # buy a product, no recurring commitment. Nike Membership is FREE loyalty (not subscription). Contrast AG1's subscription-DTC.
primary_industry: Consumer Goods   # athletic footwear & apparel maker. Close alternative: "Sports & Recreation" (Nike IS the archetypal sports brand) — single-select forces choosing structural-sector (Consumer Goods) vs domain-flavor (Sports). Minor strain; see body.

# Visual identity — lifted from Firecrawl `branding` (homepage pass), confirmed against screenshot
logo_url: https://www.nike.com/favicon.ico?v=1   # branding.images.logo = inline data-URI SVG swoosh (not hostable, like linear/aws); favicon is the URL fallback. The Swoosh is black.
brand_colors: { primary: "#111111", accent: "#FF7334", secondary: "#BAD168", background: "#FFFFFF" }   # copied from branding.colors. primary #111111 = Nike black (the real, enduring brand color — black swoosh on white). secondary #BAD168 (volt/lime) + accent/link #FF7334 (orange) are CURRENT-CAMPAIGN accents (TOMA volt event, red hero), NOT stable brand hues — a 4th brand_colors pattern: branding.colors is a snapshot of THIS page's palette, ephemeral campaign colors included.
fonts: [Helvetica Now Text, Helvetica Now Display]   # Nike's custom Helvetica Now (Text=body, Display=headlines); branding.fonts[0] correct here
color_scheme: light           # verified from screenshot (white canvas) + branding.colorScheme
design_framework: next.js     # rawHtml __NEXT_DATA__ + /_next/ + react on Akamai/static-nike CDN; branding.designSystem said "bootstrap" — wrong (same miss as AG1)
---

## Overview

Nike (NIKE, Inc., NYSE: NKE) is the world's largest **athletic footwear and apparel** company. `nike.com` is its flagship direct-to-consumer storefront: a vast catalog of shoes, clothing, and gear organized along four axes — **gender/age** (Men, Women, Kids), **product type** (Shoes, Clothing, Accessories/Gear), **sport/activity** (Running, Basketball, Soccer, Training, Golf, Tennis, Baseball, Swim, Skateboarding, Outdoor/ACG), and **iconic franchises** (Air Force 1, Air Max, Jordan, Dunk, Blazer, Pegasus, Vomero, Metcon). The site is heavily editorial and media-driven, fronting current launches (a major **NikeSKIMS** women's line, the "TOMA" event, "Latest in Hoops") over the catalog. The capture's mandate was explicitly **shape, not SKUs** — the catalog is un-enumerable (one franchise page alone returned 73 lazy-loaded tiles).

**Relationship gap, from the PARENT side (no SCHEMA field):** unlike Benadryl (a brand *of* Kenvue) or AWS (a subsidiary *of* Amazon), Nike is the top-level parent — and it *owns* sub-brands: **Jordan Brand** (`/jordan`, its own franchises and athletes), **Converse** (`converse.com`, its own domain), **Nike SB**, **ACG** (All Conditions Gear), **NikeLab**, and the new **NikeSKIMS** joint venture. The store has no frontmatter field to express "Nike owns Jordan/Converse" — the same missing parent/child relationship as the other two captures, just inverted. Recorded in the Identity NOTE + here.

## What they offer

Captured **breadth-first as a portfolio shape** (doro rule: one representative per family, never the SKU list). The shape, grounded in the homepage footer + `/men` "Shop by Sport"/"Shop By Category" + the `/w/` facet URLs:

- **By gender/age:** Men · Women · Kids (Infant & Toddler, Little, Big Kids).
- **By product type:** **Shoes** · **Clothing** (Tops/Tees, Hoodies, Jackets, Pants, Joggers, Shorts, Jerseys, Compression/Nike Pro, Tights, Sports Bras) · **Accessories & Gear** (Socks, Bags/Backpacks, Balls, Hats, Gloves, Sunglasses, Belts).
- **By sport/activity:** Running · Basketball · Soccer (Football) · Training & Gym · Golf · Tennis · Baseball · Swim · Skateboarding (Nike SB) · Outdoor (ACG: hiking/trail) · plus fan gear (NFL, WNBA, college).
- **Iconic franchises (the "Featured" sneaker lines — where competitive comparison actually happens):** **Air Force 1**, **Air Max** (90, 95, 97, 270, Dn), **Air Jordan / Jordan 1**, **Dunk**, **Blazer**, **Cortez**, **Pegasus** & **Vomero** (running), **Vaporfly / Alphafly** (racing), **Metcon** (training), **Mercurial / Phantom** (soccer), athlete signatures (**G.T. Cut**, **LeBron**, **KD**, **Giannis**, **Kobe**, Wembanyama/Booker editions).
- **Sub-brands & services:** **Jordan Brand**, **Converse** (Nike-owned), **Nike SB**, **ACG**, **NikeLab**, **NikeSKIMS**; **Nike By You** (customization); **Nike Membership** + the **Nike** and **SNKRS** apps.

**`is_multi_product: true` — the scale extreme.** Thousands of distinct, separately-bought products across dozens of franchises and sports; you absolutely comparison-shop Air Max vs. Pegasus vs. Jordan. The corpus lesson: `is_multi_product` is **trivial at the extremes** (Nike/AWS obviously true; a one-product SaaS obviously false) and **only hard in the middle** — the single-brand-many-forms cases like Benadryl (`false`) and the flagship-plus-companions case like AG1 (`true`). Nike anchors the "huge true" end.

## How it works / model

DTC e-commerce + brick-and-mortar + wholesale, monetized as **one-time retail purchases** (no subscription). On `nike.com`: browse by gender→sport→franchise or search → PDP (prices are in the markdown when US-geo'd) → cart/checkout, or customize via **Nike By You**. **Nike Membership** is a *free* loyalty program (early access to launches via SNKRS, member pricing, Run/Training Club apps) — engagement/retention, not a paywall. Off the consumer site, NIKE, Inc. also sells **B2B** (Nike Team / `niketeam.nike.com` custom uniforms, corporate sales) and **wholesale** to retailers (Foot Locker, Dick's, etc.) — channels not on the captured storefront but part of the company's model.

## Positioning & audience

- **Who:** broad global **B2C** — athletes and consumers across every sport and the huge "sport-lifestyle"/sneaker-culture segment; segmented hard by gender, age, and sport.
- **Against:** Adidas, Puma, New Balance, On, Hoka, Under Armour, Lululemon (apparel) — competing on brand, athlete endorsement, innovation (Air, Flyknit, Vaporweave), and franchise heritage rather than price.
- **Claimed edge:** "**Just Do It**" — the brand itself is the moat: the Swoosh, decades of athlete/franchise equity (Jordan), relentless product innovation, and a DTC + membership flywheel. Current bets visible in the capture: **NikeSKIMS** (women's), GenAI-era editorial, and a heavy "Latest in Hoops" basketball push.

## Nav structure

Top mega-nav flyouts (Men/Women/Kids dropdowns) are client-rendered — only top labels in markdown; the taxonomy below is reconstructed from the homepage footer + `/men` page + `/w/` facet links.

```
- Top bar: Jordan — /jordan · Converse — /w/converse-akmjx · Find a Store — /retail · Help — /help · Join Us / Sign In — /membership
- Men — /men   | Women — /women   | Kids — /kids   (each: Shop by Sport + Shop By Category)
  - <Gender> Shoes: Running · Basketball · Golf · Tennis · Jordan · Football · Soccer · Training · Nike Sportswear · Nike By You
  - <Gender> Clothing: Tops & T-Shirts · Jackets · Hoodies · Pants · Joggers · Shorts · Jerseys · Compression/Nike Pro · Tights · Tanks
  - <Gender> Gear: Socks · Bags & Backpacks · Balls · Hats · Gloves · Sunglasses · Belts · Duffel Bags
  - Shop by Sport: Soccer · Basketball · Running · Baseball · Golf · Swim · Training
- Footer · Featured (franchises): Air Force 1 · Jordan 1 · Air Max Dn · Vomero · Metcon · Air Max 270 · Air Max 90 · Blazer · Pegasus
- Footer · Shoes: All · Jordan · Running · Basketball · Tennis · Training · Custom · Sale · Soccer Cleats
- Footer · Clothing: All · Tops & Tees · Shorts · Hoodies · Joggers · Sports Bras · Pants/Tights · Socks · Yoga · NikeLab · Plus Size · Big & Tall · Sale
- Footer · Kids: Infant/Toddler Shoes · Kids Shoes · Kids Basketball · Kids Running · Kids Jordan · Kids Clothing · Backpacks · Socks · Sale
- Footer · Company: About Nike · News · Careers · Investors · Purpose · Sustainability · Accessibility (→ about.nike.com / investors.nike.com)
- Footer · Help/Orders: Order Status · Shipping · Returns · Payment Options · Gift Cards · Contact Us
- Regional footers: Africa · Americas · Asia Pacific · Europe · Middle East (locale switcher)
```

## Credibility & proof

- **Scale/heritage:** the world's largest athletic brand; "Just Do It"; the Swoosh is among the most recognized logos globally; decades of franchise equity (Air Force 1 since 1982, Air Jordan since 1985).
- **Athlete & league ties:** signature lines (LeBron, KD, Giannis, Kobe, Wembanyama, Devin Booker), team/league gear (NFL, WNBA, college, national soccer teams), elite racing (Vaporfly/Alphafly marathon records).
- **Public-company transparency:** NYSE: NKE; `investors.nike.com` (earnings, 10-K), `about.nike.com` (Impact Reports, sustainability/SDGs, newsroom) — heavy corporate-citizenship apparatus.
- **Innovation marketing:** named technology platforms (Air, Zoom, React, Flyknit, Dri-FIT, Therma-FIT, ACG) as proof of performance.

## Visual & brand impression

Flagship-grade editorial commerce — **light-mode**, white canvas, a **black** top nav and the **black Swoosh**, with huge full-bleed campaign photography and video driving the page (a red Jordan hero "THE WAIT IS OVER," the volt-green "TOMA" event banner, NikeSKIMS fashion imagery, athlete portraiture in "Latest in Hoops"). Type is **Helvetica Now** (Text + Display) — confident, condensed, sport-editorial. The design read: maximal brand confidence, image-first, the product as cultural object. The capture surfaces a **fourth distinct `brand_colors` pattern**: `branding.colors.primary` (#111111, Nike black) IS the enduring brand color, but the captured `secondary` (#BAD168 volt) and `accent` (#FF7334 orange) are **current-campaign accents**, not stable brand hues — `branding.colors` is a *snapshot of this page's palette*, and for a brand that re-skins seasonally it captures ephemeral campaign colors as if they were identity.

## Strategic read

The durable state: Nike is the **scale-leader athletic-goods brand-and-retailer**, monetized by one-time DTC + wholesale sales across an un-enumerable catalog whose real structure is **franchise × sport × gender**. Two structurally interesting facts for a market/competitor read: (1) it is the **parent of a brand house** (Jordan, Converse, ACG, NikeSKIMS) — the inverse of the AWS/Benadryl sub-entity shape, and the same place the SCHEMA has no relationship field; and (2) for classification it is the corpus's clearest **`offering_category` gap** — a global apparel/footwear maker with no "Apparel & Footwear / Fashion" value to land on (Retail/E-Commerce + CPG are both proxies). The captured moment shows Nike leaning into women's (NikeSKIMS) and basketball culture, fronting brand/editorial over catalog — consistent with a DTC-and-membership flywheel strategy.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30, US locale + maxAge:0 + waitFor:4000-5000):** homepage (`/`, full pass: markdown + html + rawHtml + links + branding + full-page screenshot, 42KB), `/men` (gender hub, 49KB), `/w/air-force-1-shoes...` (flagship franchise hub, 74KB; 73 sampled tiles) — each markdown + links + screenshot. Site inventory via `/v2/map` (286 URLs — random PDP/browse sample across ~12 locales + corporate subdomains).
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned page markdown: `captures/2026-05-30/*.md`.
- **Catalog captured as SHAPE (gender × type × sport × franchise), NOT enumerated** — the brief's mandate; the catalog is JS-walled + lazy-loaded + thousands of SKUs (see `unverified_fields`).
- **Visual identity** from the homepage `branding` payload (colors/fonts), confirmed against the homepage screenshot (and the campaign-vs-brand color caveat applied).
- **Entity:** NIKE, Inc. — a clean `Company` and the *parent* of Jordan/Converse/etc.; the parent→child relationship has no frontmatter field (Identity NOTE). Flagged in the Experiment-3 FINDINGS.
- **Couldn't get:** the full catalog, per-SKU pricing, women's/kids' full sub-structure, segment financials (see `unverified_fields`).
