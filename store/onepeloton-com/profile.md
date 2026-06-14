---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: onepeloton.com
name: Peloton
aliases: ["Peloton Interactive, Inc.", "onepeloton.com"]
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/onepeloton
  facebook: https://www.facebook.com/onepeloton
  x: https://twitter.com/onepeloton
  youtube: https://www.youtube.com/c/onepeloton
external: {}

# Capture meta
captured_at: 2026-06-10
capture_method: firecrawl
site_notes: "Next.js; storefront under /shop/<sku>, marketing PLPs at /exercise-bikes, /treadmills, /row-plus. Top product nav (Bikes/Treads/Row/Apps/Accessories) is JS-rendered flyouts — markdown shows only 'Arrow', so reconstruct nav from footer + PLP links, not the homepage dropdowns. Hardware prices live on the comparison PLPs (no PDP scrape needed for the new lineup). Subscription pricing on /membership + /app-membership. Apparel is a separate subdomain (apparel.onepeloton.com); used-equipment marketplace at repowered.onepeloton.com; commercial at business.onepeloton.com. No JSON-LD on homepage. Promo banners + refurb 'limited-time' pricing are point-in-time."
key_pages:
  membership: /membership
  app_membership: /app-membership
  exercise_bikes: /exercise-bikes
  treadmills: /treadmills
  row_plus: /row-plus
  bike: /bike
  company: /company
unverified_fields:
  - "Refurbished/promo pricing is a point-in-time snapshot, not fixed — homepage flags 'Limited-time offer ends June 15, 2026' for the $695 Refurbished Original Bike; the financing footnote on /exercise-bikes still bases refurb Bike+ on $1,995 while the card shows $1,395."
  - "Founder names — the /company page shows a 'Peloton Founders' photo and a 2012 origin story but names no founders in body text."
  - "Headcount, revenue, member counts beyond the verbatim 'millions of Members' claim — not on the marketing site."

# Description — one sentence
description: "Makes connected-fitness hardware — the Bike, Tread, and Row — paired with a required monthly membership that streams live and on-demand instructor-led classes, now layered with Peloton IQ AI coaching; also sells an equipment-free app subscription."

# Classification
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Physical Products / Hardware, Media / Content]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Sports & Recreation

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 117, h: 16 }
  logomark: { src: "https://www.onepeloton.com/images/apple-touch-icon-192.png", px: 192, transparent: false }
  og:       { src: "https://images.ctfassets.net/7vk8puwnesgc/7xxrCy285YvsxiLAIjujGw/7fd9d03438f0a0c04f7b483d2aca9eb1/meta-data-generic.jpg", w: 2400, h: 1260 }
brand_colors: { primary: "#181A1D", accent: "#DF1C2F" }   # near-black wordmark/text; Peloton red on CTAs + promo banner (branding payload mislabels the red as primary)
fonts: [Inter]
color_scheme: light
design_framework: next.js
---

## Overview

Peloton (Peloton Interactive, Inc.) sells internet-connected fitness equipment — stationary bikes, treadmills, and a rower — bundled with a recurring membership that streams live and on-demand classes from its own instructors, with a live Leaderboard and community features. Founded in 2012 to "bring the community and excitement of boutique fitness into the home," it now spans two hardware tiers (the premium **Cross Training Series** "Powered by Peloton IQ" and refurbished/rental **Original Series**), an equipment-free **App** subscription, apparel, and accessories. Peloton IQ — its AI coaching layer (personalized plans, rep/form tracking, performance estimates) — is the current product throughline across the new lineup.

## What they offer

Two revenue legs: one-time hardware and a recurring membership the hardware requires. Lines below are bold-led with verbatim price + visibility token; per-SKU roster in [`offerings.md`](offerings.md).

**Hardware — Cross Training Series (new):**
- **Cross Training Bike:** **"Starting at $1,695"** — All-Access Membership separate `[partial]`
- **Cross Training Bike+:** **"Starting at $2,695"**, Powered by Peloton IQ — membership separate `[partial]`
- **Cross Training Tread:** **"From $3,295"** — membership separate `[partial]`
- **Cross Training Tread+:** **"From $6,695"**, Powered by Peloton IQ — membership separate `[partial]`
- **Cross Training Row+:** **"As low as $3,495"**, Powered by Peloton IQ — membership separate `[partial]`

**Hardware — Original Series (refurbished / rental only):**
- **Original Bike:** **"Refurbished from $695"** (~~$1,145~~, limited-time, ends June 15, 2026) — membership separate `[partial]`
- **Original Bike+:** **"Refurbished from $1,395 or rent for $124.99/mo"** (rental membership included) `[partial]`

**Memberships:**
- **All-Access Membership:** **"$49.99/mo"** — required for Bike/Tread/Row owners; unlocks all hardware content + household profiles `[published]`
- **App+:** **"$28.99/mo"** or "$289/yr (save $58)" — unlimited app classes incl. cardio-equipment classes, includes Strength+ `[published]`
- **App One:** **"$12.99/mo"** or "$129/yr (save $26)" — full library, but only 3 cardio-equipment classes/mo `[published]`
- **Strength+:** **"$9.99/mo"** — standalone gym/strength app (audio-guided, workout generator) `[published]`

**Adjacent:** Apparel (separate subdomain), accessories (shoes, weights, mats, heart-rate bands), and a used-equipment marketplace (Peloton Repowered).

## How it works / model

The core model is **hardware-as-entry → recurring subscription**. A buyer purchases (or rents/refurbishes) a Bike, Tread, or Row, then must hold an **All-Access Membership ($49.99/mo)** to use the content and connected features — that recurring fee is the durable revenue and the lock-in. The **App** tiers (App One / App+ / Strength+) are a separate, equipment-free funnel for people who don't own hardware. Purchase is eased with Affirm financing (as low as 0% APR, $0 down), a 30-day home trial, HSA/FSA eligibility via Truemed, and old-equipment haulaway. Delivery is US-focused (48 contiguous states for the trial). A commercial arm places equipment in hotels (hospitality), gyms/corporate (Peloton for Business), and studios.

## Positioning & audience

Primarily **B2C** — consumers building a home-fitness habit — with a real **B2B** commercial arm (hospitality, corporate wellness, multi-unit). Positions on immersive instructor-led content, a motivating community/Leaderboard, premium hardware design, and now AI personalization (Peloton IQ). The "Cross Training Series" rename reframes the bikes/treads/row as cardio **and** strength stations (swivel screen, movement-tracking camera, weight tracking) rather than single-modality cardio machines. Competes against home gyms, boutique studios (SoulCycle, Orangetheory), and connected-fitness rivals (NordicTrack/iFit, Hydrow, Tonal).

## Nav structure

Top product nav is JS-rendered flyouts (contents not captured in markdown); top-level + the full captured footer:

```
- Bikes (flyout) — /exercise-bikes, /bike, /bike-plus
- Treads (flyout) — /treadmills, /tread, /tread-plus
- Row (flyout) — /row-plus
- Apps (flyout) — /app-membership, /app
- Accessories (flyout) — /shop/accessories/*
- Apparel — apparel.onepeloton.com
- Deals — /offers
- Shop and Learn
  - Home Trial — /home-trial
  - Membership — /membership
  - Refurbished Bikes — /refurbished
  - Shop used: Peloton Repowered — repowered.onepeloton.com
  - Special Pricing — /offers/specialpricing
  - Purchasing Used Peloton Bikes — /used-bikes
  - Financing — /financing
  - Instructors — /instructors
  - Peloton for Business — business.onepeloton.com
  - The Peloton Report — (PDF)
- About
  - Our Story — /company
  - Team — /company/team
  - Careers — careers.onepeloton.com
  - Press — /press
  - Blog — /blog
  - Investors — investor.onepeloton.com
  - Impact & Inclusion — /impact-inclusion
  - Peloton Member Stories — /success-stories
- Visit Us
  - Store locator — stores.onepeloton.com
  - Hotel Finder — hospitality.onepeloton.com
  - Book a Test Class — booking.onepeloton.com
  - Studio — studio.onepeloton.com
- Support — support.onepeloton.com (Contact, Returns, Warranties, Delivery, Recalls)
```

## Credibility & proof

- **Tenure:** "In 2012, we brought the best talent in technology, hardware and production together" — origin story on /company (verbatim).
- **Scale claim (self-reported):** "Millions of Members use our platform" / "our millions-strong community" — /company, **unquantified, self-reported**.
- **Member testimonials:** named first-person stories on the homepage (Laura/PA, James/Canada, Tiffany/NY) and a /success-stories hub.
- **Class library (self-reported):** "over 10,000 classes across more than 15 disciplines" — homepage (verbatim).
- **Audio partner:** Cross Training Bike+/Tread+/Row+ ship with "speakers featuring technology licensed by Sonos" (verbatim, homepage footnote).
- **Trust mechanics:** 30-day home trial, Affirm financing, HSA/FSA eligibility (Truemed), published return/warranty/recall policies.

## Visual & brand impression

Premium, confident, and highly polished — a mature DTC brand. Light theme: generous white space, large product photography, alternating black full-bleed sections for emphasis, and Peloton-red (`#DF1C2F`) reserved for CTAs and the top promo banner. The wordmark is a clean black lowercase logotype with the looping "P" logomark; typography is Inter throughout. Imagery leans on instructors mid-class and real members, reinforcing the community/aspiration message. The full-page screenshot reads as a flagship consumer-hardware site (Apple-adjacent restraint), not a discount fitness storefront.

## Strategic read

The capture catches Peloton mid-repositioning on two axes. **(1) Cardio → cross-training:** the entire new lineup is rebranded "Cross Training Series" with swivel screens, movement-tracking cameras, and strength/weight features — an explicit move to be a whole-body home gym, not a spin bike, and to justify premium prices against a strength-equipment field (Tonal). **(2) Hardware → AI-software:** "Peloton IQ" is the foregrounded throughline (personalized plans, rep tracking, form feedback), pushing the value story toward recurring software/subscription rather than the one-time hardware sale. Notably, the **Original Series is now refurbished/rental-only** — the new-unit catalog is entirely Cross Training — and a deep discount funnel (refurb Original Bike at $695, rentals, used "Repowered" marketplace, military/student special pricing) signals aggressive work to lower the entry price and grow the subscription base.

## Provenance

- **Pages:** homepage, /membership, /app-membership, /exercise-bikes, /treadmills, /row-plus, /bike, /company — 8 pages via Firecrawl (`maxAge:0`, US geo, full-page screenshots). Hardware prices read off the comparison PLPs + verified against the homepage/PLP financing footnotes; subscription prices off /membership + /app-membership.
- **Verify:** all 8 sourceURLs matched; all bodies md5-unique; no junk soft-404s.
- **Credits:** see run summary (1 homepage + 3 map calls + 7 key pages).
- **Couldn't get:** product-nav flyout contents (JS-rendered — only "Arrow" in markdown); founder names; member/financial counts.
- **Run profile:** guided — emphasis "logos and offerings"; +logos, +offerings.
- **Enriched (model knowledge):** Nasdaq ticker PTON (identity only).
