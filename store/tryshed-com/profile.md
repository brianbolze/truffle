---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: tryshed.com
name: Shed
aliases: [ShedRx]
parent: []
owns: ["shednutrition.com", "shedsupplements.com"]   # "Supplements by Shed" sibling brands, self-attested in footer
socials:
  instagram: https://www.instagram.com/tryshed/
  facebook: https://www.facebook.com/tryshed
  x: https://x.com/tryshed
  linkedin: https://www.linkedin.com/company/tryshed
  youtube: https://www.youtube.com/@try_shed
  tiktok: https://www.tiktok.com/@tryshed
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow site (cdn.prod.website-files.com); full mega-menu carries the product hierarchy. Pricing lives on PDPs as 1/6/12-month plan tiers (per-month price drops with longer prepay) — NO single /pricing page. Category cards show a higher 'Starting at $X/month' than the matching PDP 1-month tier (Tirzepatide $399 card vs $349 PDP; Semaglutide $299 vs $249) — treat the card as a soft floor, the PDP plan grid as authoritative. Map is mostly /blog/post + /es-us locale dupes + /lp/ ad-landers (noise — filter). Supplements live off-site on shednutrition.com / shedsupplements.com. Portal/signup at portal.tryshed.com; help at help.tryshed.com (Intercom). No /about page — /press is a news feed."
key_pages:
  weight_loss: /products/category/weight-loss
  longevity: /products/category/longevity
  mens_hair: /products/mens-hair-solutions
  semaglutide: /products/compounded-semaglutide-injections
  tirzepatide: /products/compounded-tirzepatide-injections
  foundayo: /products/foundayo
  press: /press
  portal: https://portal.tryshed.com/
  help: https://help.tryshed.com/en/
unverified_fields:
  - "Founding date, founders, parent/operating company — no about/company page captured (/press is a news feed); not on the marketing pages."
  - "Headline metrics (150,000+ members, 800,000+ pounds lost, 9.8% weight loss) are self-reported (VIP/self-reported member data per footnotes), not independently verified. Tirzepatide PDP says '100,000+ members' — inconsistent with 150,000+ elsewhere."
  - "Prices are a point-in-time snapshot, not fixed; category 'Starting at' figures disagree with PDP 1-month tiers by ~$50 for the two compounded flagships."
  - "Women's-hair and most longevity/hair PDPs not individually scraped — those prices taken from category cards. Health-coaching price not captured."
  - "Brand color hexes are visually estimated from screenshots (the branding payload's primary was the default link blue — unreliable)."

# Description — one sentence
description: "Delivers GLP-1 weight-loss, longevity, and hair treatments to consumers through licensed-provider online visits and a partner dispensing pharmacy — shipped to the door on monthly subscriptions with coaching support."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://cdn.prod.website-files.com/67e50a30ed05c373d6f69a0d/67e7c56ff29a4db7216f183c_ShedRx%20Logo.svg
logos:
  wordmark: { src: "https://cdn.prod.website-files.com/67e50a30ed05c373d6f69a0d/67e7c56ff29a4db7216f183c_ShedRx%20Logo.svg", w: 818, h: 238 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=tryshed.com&sz=256", px: 256, transparent: false }   # "SHED" serif on a baked cream tile
brand_colors: { primary: "#6E4A2D", accent: "#5E6B4E" }   # warm brown wordmark + muted sage CTAs (visually estimated)
fonts: [GT America]
color_scheme: light
design_framework: Webflow
---

## Overview

Shed (the header mark reads "ShedRx") is a US direct-to-consumer telehealth brand selling provider-guided **weight loss, longevity/vitality, and hair** treatments. GLP-1 weight loss is the clear hero — the homepage leads with "Sustainable wellness, made simple," "Trusted by over 150,000 members nationwide," and "Over 800,000 pounds lost." The model is fully async: a 5-minute online health form → a licensed provider reviews and prescribes when appropriate (no appointment) → medication ships discreetly from a third-party dispensing pharmacy → ongoing coaching, unlimited follow-ups, courses, and a community. It positions as a full-service "wellness program" with a named human care team (nurse, provider, dietitian, health coach, member-success manager) rather than a transactional pill service. Based in South Jordan, UT (per JSON-LD: 10813 S River Front Pkwy, Suite 550).

## What they offer

Three priced lines (all monthly subscription) plus a not-yet-launched skin line and an off-site supplements brand. Per-SKU roster in [`offerings.md`](offerings.md); family grain here, verbatim price + visibility token per line:

- **Compounded GLP-1 injections (the wedge):** Tirzepatide "**Starting at $399/month**" (PDP plan grid: 1-mo **$349** → 6-mo **$279** → 12-mo **$245**); Semaglutide "**Starting at $299/month**" (PDP: 1-mo **$249** → 6-mo **$199** → 12-mo **$175**) `[published]`
- **Brand-name GLP-1s:** Wegovy®, Zepbound® "**Starting at $349/month**"; Ozempic®, Mounjaro® also listed `[published]`
- **Foundayo® (orforglipron — FDA-approved once-daily oral GLP-1 pill):** "**Starting at $149/month + additional $125/month Shed Membership**" `[partial]` (mandatory membership/provider fee on top; "Foundayo® is a registered trademark of Eli Lilly")
- **Needle-free GLP-1:** GLP-1 Liquid Drops (oral semaglutide) "**Starting at $229/month**"; GLP-1 Lozenges "**Starting at $199/month**" `[published]`
- **Non-GLP-1 weight-loss adjuncts:** Metformin + Naltrexone + Topiramate "**$169/month**"; MIC + B12 "**$115/month**"; Naltrexone + Bupropion "**$115/month**" `[published]`
- **Longevity + Vitality:** Microdose GLP-1 "**$149/month**", NAD+ "**$144/month**", Glutathione "**$119/month**", Sermorelin "**$199/month**", Low-Dose Naltrexone (LDN) "**$89/month**", Methylene Blue "**$99/month**" `[published]`
- **Hair (men's & women's):** topical/oral minoxidil + finasteride combos and copper-peptide (GHK-Cu) serums — men's from "**$43/month**" (Copper Peptide $76.33) `[published]`; women's lines (3-in-1, 5-in-1, copper peptide) priced on their own PDPs (not captured) `[on-request]`
- **Skin:** "coming soon" — nav slots present, no products live `[on-request]`
- **Health Coaching:** sold as a standalone product (`/products/health-coaching`) `[on-request]` (price not captured)
- **Shed Supplements (sibling brand, off-site):** protein, greens, collagen, magnesium, and GLP-1 companion powders (GLP-1 Boost / Revive, Clear Protein + Hydration) on shednutrition.com / shedsupplements.com `[published]`

## How it works / model

A four-step async telehealth journey, stated on the homepage: **(1)** complete a 5-minute health-history form (and pick your admin method) → **(2)** a medical provider reviews and prescribes if you're a fit — "no appointment required" → **(3)** medication shipped discreetly from a third-party dispensing pharmacy (*"Shed is not a pharmacy and does not dispense medications"*) → **(4)** ongoing support: health coaching, unlimited provider follow-ups, health courses, an online community, and the free **Pivot** GLP-1 shot-tracking app.

Revenue is recurring: per-medication monthly subscriptions sold as **1 / 6 / 12-month plans** where the per-month price drops for longer prepay (e.g. Semaglutide $249 → $175). Some products layer a **separate $125/month Shed Membership + provider fee** (explicit on Foundayo; implied by the `zepbound-shed-membership` slug). Products are **FSA eligible**. A "**Lose 10% of your bodyweight or your money back**" guarantee anchors the weight-loss program (terms apply). Compounded medications carry "not FDA-approved" disclaimers throughout.

## Positioning & audience

Targets US consumers (B2C), led by weight loss and extending to longevity and hair — built to capture lifetime value across one membership rather than a single script. The claimed edge is **breadth + a full-service, human experience**: a named care team, coaching, community, a tracking app, and a money-back guarantee, framed as "sustainable wellness, made simple" against pill-mill competitors. Early access to the FDA-approved oral GLP-1 (Foundayo®) is a differentiator vs. compounded-only rivals. Competitive set: Hims & Hers, Ro, Henry Meds, Mochi, and other GLP-1 telehealth brands.

## Nav structure

```
- Weight Loss — /products/category/weight-loss
  - GLP-1 Solutions:
    - Compounded Tirzepatide Injections — /products/compounded-tirzepatide-injections
    - Compounded Semaglutide Injections — /products/compounded-semaglutide-injections
    - GLP-1 Liquid Drops — /products/product/glp-1-liquid-drops
    - GLP-1 Lozenges — /products/product/glp-1-lozenges
    - Foundayo® — /products/foundayo
    - Wegovy® — /products/product/wegovy
    - Zepbound® — /products/product/zepbound-shed-membership
    (also: Ozempic® — /products/ozempic · Mounjaro® — /products/mounjaro)
  - Additional Weight-Loss Solutions:
    - Metformin + Naltrexone + Topiramate — /products/product/metformin-naltrexone-topiramate
    - MIC + B12 — /products/product/mic-b12-injections
    - Naltrexone + Bupropion — /products/product/naltrexone-bupropion
- Longevity + Vitality — /products/category/longevity  (also /products/longevity)
  - Microdose GLP-1 — /products/microdose
  - NAD+ — /products/nad
  - Glutathione — /products/glutathione-injections
  - Low-Dose Naltrexone (LDN) — /products/product/ldn
  - Sermorelin — /products/product/sermorelin
  - Methylene Blue — /products/product/methylene-blue
- Hair
  - Women's Hair — /products/womens-hair-solutions  (3-in-1, 5-in-1, Copper Peptide GHK-Cu)
  - Men's Hair — /products/mens-hair-solutions  (Minoxidil+Finasteride 2-in-1, 3-in-1 Tablet, 5-in-1, Copper Peptide)
- Skin — coming soon (placeholder slots, no live products)
- More
  - Health Coaching — /products/health-coaching
  - Supplements by Shed — https://shednutrition.com/
  - Refer and Earn: Referral Program — /resources/support/referrals · Affiliate Sign-Up
- Explore (blog) — /blog/explore   |   Help — https://help.tryshed.com/en/   |   Login — https://portal.tryshed.com/
```

## Credibility & proof

Self-reported claims (recorded verbatim, **not** endorsed):
- **"Over 800,000 pounds lost*"** and **"Trusted by over 150,000 members nationwide"** — footnoted as self-reported / all-member data. (Tirzepatide PDP separately says "Join 100,000+ members" — figures are inconsistent across pages.)
- **"9.8% weight loss*"** — footnoted as VIP-member-data average.
- **"Lose 10% of your bodyweight or your money back"** guarantee (full terms in Terms & Conditions).

Third-party / structural signals:
- **LegitScript-certified** seal in footer (verifiable approval for tryshed.com) — the regulatory trust counter to the compounded-not-FDA-approved exposure.
- Named **care team** with photos and credentials (Neely Wood RN, Dr. Asad Niazi MD, Roseanne Schnell RD, Pardise Mossalman CHC, member-success manager).
- Member **testimonials** with before/after (Alix, Alyssa, Maicy, Jesse, Christine, Aly).
- **FSA eligible**; clinical-trial framing for Wegovy® (15–20%) paired with explicit compounded-medication disclaimers.
- JSON-LD identity: phone +1-801-457-2249, support@tryshed.com, typed as Organization + MedicalBusiness (medicalSpecialty "Weight Management").

## Visual & brand impression

A warm, premium, editorial wellness aesthetic — closer to an upscale spa/lifestyle brand than a clinical telehealth site. Cream/sand/beige fields throughout, a refined **brown serif "SHED" wordmark** (classic, almost luxury-editorial), and muted **sage-green** accents on CTAs, the weight-loss calculator, and the money-back panel. Body type is GT America (clean grotesque sans), so display-serif + sans pairs "considered" with "modern." Heavy real-person photography (members, before/after, the care team), soft rounded cards, and generous whitespace give a calm, reassuring tone. High design maturity and visual consistency across pages.

## Strategic read

- **GLP-1 weight loss is the wedge; longevity, hair, and supplements extend LTV** across the same membership — a multi-line wellness ecosystem, not a single-script shop.
- **Full-stack experience as the moat:** owns the care team, coaching, community, tracking app (Pivot), and even a sibling supplements brand — competing on retention and breadth rather than lowest med price.
- **Foundayo® (orforglipron) early-mover:** offering the FDA-approved oral GLP-1 pill differentiates from compounded-only competitors — but it's gated behind the separate $125/month membership, so the headline "$149" understates the all-in.
- **Commitment mechanics:** 1/6/12-month prepay plans + a money-back guarantee push members toward longer, stickier commitments.
- **Pricing opacity is a real pattern:** category "Starting at" prices run ~$50 above the PDP 1-month tier, and some lines layer a membership on top — the true all-in isn't obvious until the PDP/checkout.
- **Regulatory exposure:** compounded medications are not FDA-approved (heavy disclaimers); LegitScript certification and the named clinical team are the credibility counterweights.

## Provenance

- **Pages:** 8 analyzed via Firecrawl (2026-06-04) — homepage; category pages weight-loss, longevity, men's-hair; PDPs compounded-semaglutide, compounded-tirzepatide, Foundayo; and /press.
- **Verify:** all sourceURLs match; all 8 bodies md5-unique (no geo/cache contamination).
- **Credits:** 9 (1 map + 1 homepage + 7 key pages; logos/signals extraction free).
- **Couldn't get:** no about/company page exists (/press is a news feed) → founding/founders/parent unverified; women's-hair and most longevity/hair PDPs not individually scraped (prices from category cards); health-coaching price.
- **Run profile:** guided — modules added: +logos:{}, +offerings.md (no emphasis).
- **Logos:** wordmark = ShedRx SVG 818×238 (hostable, Webflow CDN); logomark = google-s2 favicon 256px, "SHED" serif on a baked cream tile (not transparent); og slot absent (no og:image declared).
