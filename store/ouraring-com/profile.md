---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: ouraring.com
name: Oura
aliases: [Oura Ring, Oura Health]
legal_entity: "Oura Health Oy"
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/ouraring
  x: https://x.com/ouraring
  youtube: https://www.youtube.com/channel/UCf-xFf4xPcT9DVdOkcCaScg
  facebook: https://www.facebook.com/ouraring
  tiktok: https://www.tiktok.com/@ouraring
  pinterest: https://www.pinterest.com/ouraring/
external: {}

# Capture meta
captured_at: 2026-06-24
capture_method: firecrawl
site_notes: "Next.js storefront. Ring PDP per-finish prices render client-side — the Oura Ring 4 PDP markdown carried NO prices (read finish prices off the Ring 5 PDP finish picker or the homepage/membership cross-sell modules). Heavy flash-sale pricing (strikethroughs) — treat every ring price as point-in-time. Homepage + /membership cross-sell modules and the Ring 4 Ceramic PDP disagreed on the ceramic price ($279 vs $399) on the SAME day. No JSON-LD on homepage; nav is JS-rendered flyouts (Shop / Health Features / Experience / For Organizations). B2B lives on organizations.ouraring.com (separate subdomain, not captured). Images served via ourahealth.imgix.net."
key_pages:
  why_oura: /why-oura
  how_it_works: /how-it-works
  ring5: /store/rings/oura-ring-5
  ring4: /store/rings/oura-ring-4
  ring4_ceramic: /store/rings/oura-ring-4-ceramic
  membership: /membership
  about: /about-us
  science: /science-and-research
unverified_fields:
  - "Ring prices are a point-in-time snapshot, not fixed — site runs flash sales (homepage: 'Take up to 44% off Oura Ring 4', 'Flash Sale and free shipping through June 26th'); strikethrough pricing throughout."
  - "Oura Ring 4 Ceramic price disagrees across captured pages, same day: '$279' (homepage + /membership cross-sell modules) vs '$399 ~~$499~~' (the /store/rings/oura-ring-4-ceramic PDP finish picker — Midnight & Cloud). Reported, not reconciled."
  - "Oura Ring 4 base/per-finish price absent from its captured PDP (client-rendered); only the cross-sell 'From $244' (flash sale) is attested."
  - "Founders / exact founding year not stated on captured pages (about page: 'born in Finland', '12+ Years' of research, '10 years ago we created a tool')."
  - "Headcount / $11B valuation / $900M raise are press-reported (homepage 'In the News' links), not Oura's own page claims — see Credibility."

description: "Makes the Oura Ring, a titanium smart ring, and pairs it with a $5.99/mo app membership that turns 50+ sleep, heart, activity, stress, and women's-health metrics into daily Readiness, Sleep, and Activity scores."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Physical Products / Hardware, Software / SaaS]
portfolio_shape: Flagship + companions
business_model: Subscription            # STRAIN: hybrid — one-time ring sale ($349–$499) + recurring membership; membership tagged primary as the recurring, strategically-central model. See "How it works / model".
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint, verified against the screenshot.
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 993, h: 311 }                                                            # extracted OURA logotype (inline-SVG data-URI in branding.logo); white fill on transparent
  logomark: { src: "https://www.google.com/s2/favicons?domain=ouraring.com&sz=256", px: 180, transparent: false }  # the "Ō" mark, white on a baked black square (judged on a checker tile)
# og slot omitted — only opengraph-400x400.png declared (400px square, < 600px wide-cover bar)
brand_colors: { primary: "#5B6550", accent: "#F7F1E8" }   # sage-green brand tone + warm cream canvas (verified vs screenshot); functional link/CTA blue #2A72DE
fonts: [Editorial New, AkkuratLL]        # Editorial New = serif headings; AkkuratLL = sans body (verified — serif headline "Subtle. Power." in screenshot)
color_scheme: light
design_framework: next.js                # rawHtml: /_next/, _app
---

## Overview

Oura is a Finnish-founded consumer health company built around a single product: the **Oura Ring**, a titanium smart ring worn 24/7 that tracks 50+ health metrics. The ring pairs with the **Oura App** and a paid **Oura Membership** ($5.99/mo) that translates raw biometric data into daily **Readiness, Sleep, and Activity** scores plus longer-term insights across sleep, heart health, activity, stress, and women's health. The company leans hard on a science/accuracy positioning — an in-house research team, 130+ peer-reviewed publications, and a named medical advisory board — to differentiate from smartwatch competitors. As of this capture, **Oura Ring 5** is the current flagship; **Oura Ring 4** and a ceramic-finish **Oura Ring 4 Ceramic** remain on sale as lower-priced companions.

## What they offer

One product (the smart ring) across three model/material lines, plus a mandatory-for-value app membership. Prices are flash-sale snapshots (see `unverified_fields`):

- **Oura Ring 5:** flagship titanium smart ring, "the world's smallest smart ring" — **$399** (Silver, Black) / **$499** (Gold, Deep Rose, Stealth, Brushed Silver) `[published]`
- **Oura Ring 4:** prior-gen titanium ring, 6 finishes — **From $244** (flash sale; base/per-finish price not on captured PDP) `[published]`
- **Oura Ring 4 Ceramic:** zirconia-ceramic exterior over a titanium interior, 4 finishes (Midnight, Cloud, Tide, Petal) — **$279** (cross-sell modules) / **$399 ~~$499~~** (PDP, Midnight & Cloud only) `[published]` *(prices disagree — see `unverified_fields`)*
- **Oura Membership:** the app subscription that unlocks the scores, 50+ metrics, and **Oura Advisor** (AI health companion) — **$5.99 USD/month or $69.99 USD/year**, first month free for new members; HSA/FSA eligible `[published]`
- **Accessories:** size-specific chargers + USB-C cable included with each ring; a fast-charging **Charging Case** is "sold separately" (not priced in capture). Not enumerated.

Per-SKU roster (all three ring lines + membership) in [`offerings.md`](offerings.md).

## How it works / model

**Device + subscription hybrid.** A customer buys the ring once ($244–$499) and then pays a recurring **$5.99/mo (or $69.99/yr) membership** for the full experience. The two are sold as inseparable — "purchasing, activating, and consistently wearing an Oura Ring is the only way to unlock... the Oura Membership," and without the membership "your Oura Ring and Oura App will still function, but the insights... will be much more limited." The ring's sensors (red/IR + green/IR LEDs, temperature sensor, accelerometer) collect data 24/7; the app surfaces daily Readiness/Sleep/Activity scores and in-the-moment guidance, getting more personalized over time. Revenue is therefore both transactional hardware (5.5M+ rings sold, self-reported) and recurring membership; `business_model` is tagged `Subscription` for the recurring layer, but the one-time device sale is co-equal. A **B2B** arm (Oura for Business / `organizations.ouraring.com`) and clinical/research partnerships extend the model beyond DTC.

## Positioning & audience

Primarily **B2C** wellness consumers who want passive, accurate, around-the-clock health tracking without a screen on their wrist — positioned against the Apple Watch / Samsung / Google smartwatch category (the CNN headline frames Oura's plan "to stay ahead of Apple and Google"). The pitch is **"rooted in wellness, not burnout"** — Nordic, balance-oriented, design-led ("Design is in our DNA", aerospace-grade titanium, Finnish craftsmanship), and **science-validated** (the differentiator the smartwatch incumbents can't claim as cleanly). Strong secondary lean into **women's health** (cycle/ovulation tracking, Natural Cycles partnership) and **longevity/cardiovascular** framing. A growing **B2B/clinical** audience (organizations, researchers).

## Nav structure

Top-level menu attested via the homepage screenshot + `<header>` region (flyout sub-items reconstructed from on-page links — the JS mega-nav did not fully render in markdown):

```
- Shop
  - Oura Ring 5 — /store/rings/oura-ring-5
  - Oura Ring 4 — /store/rings/oura-ring-4
  - Oura Ring 4 Ceramic — /store/rings/oura-ring-4-ceramic
  - Sizing — /sizing
- Health Features
  - Sleep and Rest — /sleep-and-rest
  - Heart Health — /heart-health
  - Activity and Movement — /activity-and-movement
  - Stress — /stress
  - Women's Health — /womens-health
  - Metabolic Health — /metabolic-health
- Experience
  - How It Works — /how-it-works
  - Membership — /membership
  - Why Oura — /why-oura
  - Science & Research — /science-and-research
- For Organizations — https://organizations.ouraring.com/   (B2B)
```

Footer adds: Our Company (About Us, Leadership, Medical Advisory Board, Careers, Newsroom) · Support (Member Care, Sizing, Recycling Program, Flexible Spending/HSA-FSA, Orders) · Partner With Us (For Organizations, Developers) · Connect (The Pulse blog + social channels).

## Credibility & proof

Self-reported claims recorded **verbatim and flagged** — captured as the company's own marketing, not endorsed as fact:

- **Scale (self-reported, /about-us):** "5.5M+ Rings sold worldwide", "900+ Employees", "12+ Years" of research, "30+ PhDs" on an in-house science team. *(The /why-oura page states "25+ PhDs" — minor self-reported inconsistency.)*
- **App rating (self-reported, /membership):** "4.9 App Store Rating based on 137k reviews".
- **Accuracy (self-reported, cited to Oura studies/blog):** "99% Heart Rate Accuracy" (r² vs ECG), "98% Heart Rate Variability Accuracy", "94% Ovulation Detection Accuracy", "92% Body Temperature Accuracy", "79% Sleep Tracking Accuracy" (vs clinical polysomnography at 83%).
- **Outcomes (self-reported surveys):** "88% of Oura Members see their health improve" (survey of 699 members after 30 days); "90% Members Feel Healthier" (new-member NPS survey).
- **Research (self-reported, /science-and-research):** "130+ peer-review publications", "14 active collaborations with academic and clinical institutes". Independently validated in the *Journal of Medical Internet Research*, *Sensors*, and *Sleep Medicine*. Named research partners: UCSF, UCLA, Scripps, National University of Singapore, Duke, Google Fitbit, UNC-Chapel Hill, University of Michigan.
- **Medical Advisory Board (named):** Dr. Rebecca Robbins (Harvard Medical School / Brigham & Women's), Dr. Elissa Epel (UCSF), Dr. Eleni Jaswa (UCSF, ObGyn/REI), Dr. Jagmeet P. Singh (Harvard), Dr. Michael Chee (National University of Singapore).
- **Awards:** "TIME: Oura Ring 4 — The Best Inventions of 2025"; "CNBC Disruptor 50 List" (2024); "Webby — Best App, Health and Wellness" (2023); "Women's Health — Best Sleep Tracker" (2024).
- **Press headlines (third-party, verbatim from homepage 'In the News'):** "CNBC: Oura reaches $11 billion valuation with new $900 million fundraise" (Oct 2025); "CNN: CEOs and celebrities love Oura's sleep-tracking ring..." (Dec 2025); Cosmopolitan year-long review.
- **Trust / compliance:** HSA/FSA eligible; GDPR compliant ("adhere to Europe's strictest data privacy laws", data de-identified); Natural Cycles (the "first FDA-cleared birth control app") temperature-sync partnership; integrations with Flo, Clue. Payment: Affirm, PayPal, Apple Pay, Google Pay, major cards.

## Visual & brand impression

High-end, editorial, unmistakably premium-wellness. A warm **cream/sand canvas (#F7F1E8)** with a **sage-green** brand tone and black type; elegant **serif headlines** (Editorial New — "Subtle. Power.") over a clean sans body (AkkuratLL). Hero and product photography is cinematic and human — rings on hands in natural, softly-lit, earthy settings rather than spec-sheet renders. The aesthetic reads luxury-meets-calm (Nordic minimalism, jewelry-adjacent) — deliberately *un*-gadgety, distancing the ring from the techy smartwatch category. Dark footer anchors the otherwise light, airy layout. Design maturity is very high — this is a brand that invests in craft.

## Strategic read

- **The moat is "accurate + invisible + science-backed."** Oura's whole differentiation against Apple/Samsung/Google (who can out-distribute it) is a jewelry form factor people will actually wear to bed plus a credible research apparatus. The science page is unusually deep for a consumer brand — that's the defensibility bet.
- **Subscription is the real business under a hardware skin.** The ring is the wedge; the $5.99/mo membership (required for the value prop) is the recurring revenue and the lock-in. Reported scale (5.5M+ rings) × membership = the model the $11B valuation prices.
- **Flash-sale dependence is visible.** Heavy strikethrough/"up to 44% off" pricing and an internal price disagreement on the ceramic line suggest aggressive promo cadence — useful context for anyone reading the prices as MSRP. Treat every captured price as point-in-time.
- **Women's health is a quiet second pillar** (cycle/ovulation, Natural Cycles FDA-cleared partnership) — a category smartwatches under-serve and Oura's finger-temperature sensing is well-suited to.

## Provenance

- **Pages:** 9 captured via Firecrawl (`firecrawl` / `fc.py`), all 2026-06-24 — homepage, /why-oura, /how-it-works, /store/rings/oura-ring-5, /store/rings/oura-ring-4, /store/rings/oura-ring-4-ceramic, /membership, /about-us, /science-and-research.
- **Verify:** all 9 sourceURLs matched; all 9 bodies md5-unique; no junk soft-404s.
- **Credits:** 10 (1 map + 9 scrapes: homepage + 8 key pages).
- **Couldn't get:** Oura Ring 4 per-finish PDP prices (client-rendered, absent from markdown); B2B `organizations.ouraring.com` (separate subdomain, not captured); accessories (Charging Case et al.) not priced; Ring 4 Ceramic Tide & Petal finishes shown but unpriced.
- **Run profile:** guided — +offerings (per-SKU roster); no emphasis, standard scope otherwise.
