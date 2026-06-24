---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: nike.com
name: Nike
aliases: []
legal_entity: "Nike, Inc."   # homepage footer "© 2026 Nike, Inc. All Rights Reserved"
parent: []
owns: ["converse.com", "Jordan Brand"]   # JSON-LD `subOrganization` (Nike #organization → Converse [converse.com] + Jordan Brand [no own domain → name]). STRAIN: NikeSKIMS is a Nike×SKIMS JV (not in subOrganization) — affiliation, kept to prose per 2.6 relation-evidence.
socials: { youtube: "https://www.youtube.com/user/nike", linkedin: "https://www.linkedin.com/company/nike", facebook: "https://www.facebook.com/nike", x: "https://twitter.com/nike", instagram: "https://www.instagram.com/nike/" }   # JSON-LD sameAs (Nike-owned handles; the Converse/Jordan entries nested under subOrganization left out)
external: { wikipedia: "https://en.wikipedia.org/wiki/Nike,_Inc.", wikidata: "https://www.wikidata.org/wiki/Q483915" }   # JSON-LD sameAs — third-party records (Nike Inc)

# Capture meta
captured_at: 2026-06-24
capture_method: firecrawl
site_notes: "Next.js SPA (rawHtml __NEXT_DATA__ ×1, /_next/ ×15 — branding.designSystem says 'bootstrap', wrong). Full mega-nav + footer IA render into homepage markdown — that's the discovery surface, not the map (map returns ~480-url sample of /t/ product + /w/ category URLs plus heavy locale subtrees /at /de /au /ch /fr …, mostly noise — filter locale prefixes). branding.colors returns chrome + the rotating CAMPAIGN palette (volt #BAD168), NOT brand identity — Nike's identity is black swoosh on white; verify against the screenshot. Homepage hero rotates (this run: football 'Rip the Script'/Toma, Jordan, Sabrina, The Opening, Nike Mind) — recovery/wellness is NOT surfaced on the homepage; it lives in the catalog. Recovery hardware roster lives on /w/performance-recovery-collection-… and /w/recovery-collection-w274; prices on the collection grid + PDPs. about.nike.com is a separate newsroom host (heavy football PR), no founding/financials. Membership is free; per-product pricing lives on /t/ PDPs."
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
  recovery_collection: /w/performance-recovery-collection-3k7dgz8hfx3z90poyzw274
  recovery_collection_all: /w/recovery-collection-w274
  hyperboot: /t/hyperice-hyperboot-shoes-0v8aYsXz
  nike_mind: /mind
  yoga: /w/yoga-anrlj
  rejuven8: /w/nike-rejuven8-shoes-a2h2lzy7ok
  find_a_store: /retail
  snkrs_launch: /launch
unverified_fields:
  - "Per-product pricing for the broad catalog — lives on /t/ PDPs; only the Recovery/Wellness line was enumerated this run (see offerings.md)."
  - "Homepage hero & carousels are a point-in-time snapshot, not fixed — rotating merchandising; captured state differs run-to-run."
  - "Financials, headcount, revenue split (DTC vs wholesale) — not on the consumer site; a deep-research job. about.nike.com is newsroom-only, no founding facts."

description: "Designs and sells athletic footwear, apparel, and equipment direct-to-consumer and via wholesale across the Nike, Jordan, and Converse brands, and now extends into performance-recovery hardware through a Hyperice partnership."

# Classification
entity_type: Company
target_market: [B2C, B2B]            # B2C dominant (DTC + retail); B2B via wholesale + Corporate Sales (/corporate-sales), team/federation kit
offering_category: [Physical Products / Hardware]   # maker of footwear/apparel/equipment + (new) electronic recovery devices; the athletic/fashion vertical is a tag, not a category
portfolio_shape: Catalog
business_model: Transactional / One-time   # product sales; Nike Membership is a FREE loyalty layer, not a subscription
primary_industry: Sports & Recreation

# Visual identity
logo_url: https://static.nike.com/a/images/f_jpg,q_auto:eco/61b4738b-e1e1-4786-8f6c-26aa0008e80b/swoosh-logo-black.png   # JSON-LD `logo` — the canonical black Swoosh; Nike's symbol serves as its wordmark (no separate text mark on-site)
logos:
  wordmark: { src: "https://static.nike.com/a/images/f_jpg,q_auto:eco/61b4738b-e1e1-4786-8f6c-26aa0008e80b/swoosh-logo-black.png", w: 1600, h: 1600 }   # the black Swoosh on white (f_jpg → opaque); square because the symbol IS the wordmark for Nike
  logomark: { src: "https://www.nike.com/apple-touch-icon.png", px: 152, transparent: false }   # Nike-hosted app icon — small Swoosh on light-gray ground (opaque); google-s2 favicon also available at 192px
  og:       { src: "https://c.static-nike.com/a/images/w_1920,c_limit/bzl2wmsfh7kgdkufrrjq/image.jpg", w: 1920, h: 1088 }
brand_colors: { primary: "#111111", background: "#FFFFFF" }   # STRAIN: true identity is black swoosh / white; branding returned chrome + campaign (primary #2B333F, secondary volt #BAD168, accent #111111) — content, not brand
fonts: [Helvetica Now Text, Helvetica Neue]   # branding.fonts: Helvetica Now Text Medium (body) / Helvetica Now Text (heading) / Helvetica Neue (fallback); "Helvetica Now" ×89 in rawHtml
color_scheme: light
design_framework: next.js
---

## Overview

Nike is the world's largest athletic-goods company, selling footwear, apparel, equipment, and
accessories for sport and everyday lifestyle. The consumer site (`nike.com`) is a global
direct-to-consumer storefront organized by gender (Men / Women / Kids), by owned brand (Jordan,
Converse) and the **NikeSKIMS** women's joint venture (Nike × SKIMS — affiliation, not a wholly-owned
subsidiary), and by sport (basketball, running, soccer, training, tennis, golf, and a long tail from
baseball to skateboarding). Its self-description is broad and identity-driven rather than
category-driven: on about.nike.com the manifesto reads *"WE SERVE KIDS, PROS, DREAMERS, WOMEN, TEAMS,
COACHES, MEN… ATHLETES. *If you have a body, you are an athlete."*

**This capture was run with a wellness/recovery + consumer-hardware emphasis.** The headline finding:
Nike now fronts a full **performance-recovery hardware line**, most of it co-branded with **Hyperice**
(massage guns, dynamic-air-compression boots, a heated wearable boot), alongside its own simple
recovery tools and recovery footwear. That line is enumerated per-SKU in
[`offerings.md`](offerings.md); the rest of the universal `profile.md` contract is filled below.

## What they offer

A `Catalog`-scale assortment — too large to enumerate in full; the shape is what matters, with the
recovery/wellness line broken out because it was this run's focus:

- **Performance Recovery & Wellness `[published]`** — a small, enumerable hardware-forward line (full
  roster + prices in [`offerings.md`](offerings.md)). The **Nike × Hyperice** collaboration anchors
  it: **Hyperboot** ($699.97, a battery-powered heated + NormaTec-air-compression wearable boot),
  **NormaTec Elite Legs** ($999.97, "Best Seller") and **Elite Hips** dynamic air compression,
  **Hypervolt 3 / 3 Pro / Go 3** massage guns ($209.97–$299.97 / $119.97), and the **Venom 2 Back**
  heated massage wrap ($215.97). Nike-branded recovery tools sit beside them: **Recovery Ball** ($30),
  **Recovery Roller Bar** ($35) and **Foam Roller** ($50), **Training Mat 2.0** ($75); plus
  recovery footwear, the **Nike ReactX Rejuven8** men's shoe ($75, "Best Seller") and women's slide
  ($65). Wellness content/programming: **Nike Training Club** recovery + regeneration, **Yoga**
  apparel/accessories, and the **Nike Well Festival** event.
- **By audience:** Men, Women, Kids (Big / Little / Baby & Toddler), Teens.
- **By owned brand / line:** **Jordan** (the dominant sub-brand — full Men/Women/Kids lines + its own
  sport range), **Converse** (subOrganization; transacts on its own domain), and **NikeSKIMS**
  (Nike × SKIMS JV — bras, leggings, the "Studio Stretch" material story).
- **By product type:** Shoes, Clothing, Accessories & Equipment — each subdivided per sport.
- **By sport:** Basketball, Running, Soccer, Training & Gym, Tennis/Court (+ Pickleball), Golf, plus
  Baseball, Cheer, Football, Gymnastics, Lacrosse, Skateboarding, Softball, Swimming, Volleyball,
  Wrestling, and ACG (All Conditions Gear). "Locker Room" carries licensed league gear (NBA, NFL,
  MLB, WNBA, NCAA, NWSL).
- **Innovation platforms (footer "Guides"):** Air, Air Force 1, Air Max, FlyEase, Flyknit, Free,
  React, **Nike Mind** ("a mind-altering shoe" — neuroscience footwear tech that *amplifies* sensation
  via mechanoreceptors underfoot; **a shoe platform, not a wellness/meditation product**), Vaporfly,
  ZoomX, Space Hippie — the technology franchises Nike markets as durable IP.
- **Services:** Nike By You (customization), SNKRS (launch/drops), and the app ecosystem (below).

## How it works / model

Primarily **transactional product sales** through three channels: nike.com DTC, owned retail
(Find a Store), and wholesale (plus Corporate Sales for B2B). Revenue is one-time purchase, not
subscription.

**Nike Membership is a free loyalty layer**, not a paid tier. Captured member mechanics this run:
*"Members: Free Shipping on Orders $50+"* and, on the Hyperboot PDP, *"Free standard shipping on
orders $50+ and free 60-day returns for Nike Members."* Membership unlocks an app ecosystem — **Nike
App** (personalized shopping), **Nike Run Club (NRC)**, **Nike Training Club (NTC)** (which carries
recovery/regeneration, nutrition, mindset content), and **SNKRS** (sneaker drops) — that doubles as
the engagement + DTC funnel.

## Positioning & audience

Positions as the premium performance-and-culture leader across essentially every sport and the
lifestyle/streetwear adjacent to it. The brand voice is aspirational and inclusive — the about-page
manifesto deliberately widens "athlete" to everyone. The recovery push extends that performance
identity past the workout into warm-up and recovery, leaning on a credentialed third party (Hyperice)
rather than building the devices in-house. Athlete and team endorsements (Sabrina Ionescu, Ja Morant,
LeBron, Kobe/Mamba, Eduardo Camavinga, Erling Haaland; federations like Brasil, U.S. Soccer) are the
primary proof and merchandising engine.

## Nav structure

```
- Men — /men · Women — /women · Kids — /kids (Big 7–15 / Little 3–7 / Baby & Toddler 0–3; Teens)
  Shoes / Clothing / Accessories, each subdivided (Basketball, Jordan, Lifestyle, Running, Soccer,
  Training & Gym, Sandals & Slides, Custom/Nike By You; Bras, Hoodies, Leggings, Jackets, Pants, etc.)
- Jordan — /jordan (New & Featured, Best Sellers, Heat Check; Men/Women/Kids; Sport: Basketball, Golf, Cleats)
- NikeSKIMS — /nikeskims (Shoes [Rift]; Bras, Jackets, Leggings, Shorts, Tops; Shine/Matte/Airy/Seamless/Stretch-Knit; Bra & Fabric Guides)
- Sport — /gear-up
  - Basketball (Kobe, Jordan, LeBron) · Court — /tennis (Tennis, Pickleball) · Soccer (Federation Kits, Cleats, Indoor)
  - Training — /training · Running (Road, Race, Trail, Track & Field, Shoe Finder) · Golf
  - More Sports: Baseball, Cheer, Football, Gymnastics, Lacrosse, Skateboarding, Softball, Swimming, Volleyball, Wrestling
  - Locker Room: NBA, NFL, MLB, WNBA, NCAA, NWSL, Soccer Clubs, Federations · ACG — /acg (Trail Run, Hike, Explore)
- Performance > Accessories & Equipment > Recovery Collection — /w/performance-recovery-collection-… (Hyperice + Nike recovery hardware)
- Converse — /w/converse-akmjx (links out; transacts on converse.com)
Top utility: Find a Store (/retail) · Help (/help) · Join Us / Membership (/membership) · Sign In · Search
Footer — Company: About (about.nike.com), News, Careers, Investors, Purpose, Sustainability, Accessibility
Footer — Promotions: Student, Military, Teacher, First Responders & Medical, Birthday discounts
```

## Credibility & proof

Global market leadership and ubiquity are the implicit proof; explicit signals on-site: deep athlete
and federation roster, licensed-league partnerships across NBA/NFL/MLB/WNBA/NCAA/NWSL, and an
innovation narrative (neuroscience "Nike Mind" footwear, Vaporfly/ZoomX, the Hyperice recovery
collaboration). Buyer-trust mechanics captured this run: *"free 60-day returns for Nike Members,"*
free member shipping on $50+, and a documented accessibility program. On the recovery hardware,
third-party credibility is explicit — the Hyperboot's *"One year warranty is through Hyperice only,"*
and devices are noted **FSA/HSA eligible**.

## Visual & brand impression

Stark, confident, image-first. White background, black monochrome chrome, the black Swoosh as the
only persistent mark — the homepage is edge-to-edge product and athlete photography (this capture: a
football "Rip the Script"/Toma block, Jordan, a Sabrina Ionescu feature, "The Opening," a Nike Mind
"Engineered for Every Move" panel) with minimal text and small black pill CTAs. Typeface is Helvetica
Now (Text), reinforcing the clean, high-contrast, premium-mass feel. The design system is mature and
template-driven; brand color is deliberately *neutral* (black/white) so the rotating product imagery
and its campaign colors (volt, etc.) carry all the visual energy.

## Provenance

- **Pages (5, all Firecrawl scrape, US geo):** homepage (`/`), Performance Recovery Collection
  (`/w/performance-recovery-collection-…`), Hyperboot PDP (`/t/hyperice-hyperboot-shoes-0v8aYsXz`),
  Nike Mind (`/mind`), about (`about.nike.com/en`). Map captured (492-url sample, locale-heavy) plus
  two `map --search` passes (`hyperice`, `recovery`) to surface the recovery line; key pages came from
  homepage links + those searches.
- **Verify:** all 5 sourceURLs matched, all bodies md5-unique (clean; no geo/cache contamination).
- **Logos:** wordmark = the black Swoosh PNG (1600×1600, opaque); logomark = Nike apple-touch-icon
  (152px, opaque); og = declared og image (1920×1088). Measured by `fc.py logos`, confirmed by eye.
- **Credits:** ~8 credits this run (1 homepage + 1 map + 2 map-search + 4 page scrapes).
- **Couldn't get:** broad-catalog PDP pricing (only the recovery line enumerated — see offerings.md),
  Converse (separate domain), gated app experiences, founding/financials (newsroom about page only).
- **Structured layer (2.6):** `fc.py signals` over this run's homepage rawHtml — `socials`
  (youtube/linkedin/facebook/x/instagram, Nike-owned), `external` (wikipedia/wikidata), `logo`
  (Swoosh), and `subOrganization` (Converse + Jordan Brand → `owns`; NikeSKIMS absent → JV, prose).
  `legal_entity` from footer ©.
- **Migrations:** prior capture 2026-05-30 (schema 2.2) archived to `captures/_archive/2026-05-30`;
  this run re-captured fresh and re-stamped 2.2 → 2.6 (added `legal_entity`, `logos:{}` block;
  tightened `owns` to subOrganization-attested, dropped the NikeSKIMS JV per 2.6 relation-evidence).
- **Run profile:** guided — emphasis "wellness/recovery, esp. consumer hardware"; +offerings.md.
- **Enriched (model knowledge):** none beyond identity context already on-site.
