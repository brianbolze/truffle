---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: bluechew.com
name: BlueChew
aliases: []
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/GetBlueChew/
  instagram: https://www.instagram.com/bluechew/
  tiktok: https://www.tiktok.com/@bluechew
  youtube: https://www.youtube.com/@BlueChew
  x: https://x.com/bluechew
  linkedin: https://www.linkedin.com/company/bluechew
external:
  crunchbase: https://www.crunchbase.com/organization/bluechew

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Angular SPA (ng-version; custom <*-com> web components). Commerce lives in a walled app at app.bluechew.com (Sign Up/Login + checkout). Products are NOT in the top nav (thin hamburger) — reach PDPs by direct URL (/sildenafil, /gold, /max, /energy, …) or the /quiz funnel. Per-unit 'From $X/ea' floor + a '$20/month' entry are shown on molecule PDPs; the FULL quantity-tier ladder is exposed only on /<product>/plan (e.g. /gold/plan) — molecule ladders sit behind the /plans;s=<code> funnel. Map is ~95% /our-stories blog noise (350+ URLs: 'BlueChew vs X', 'sex shops in <city>', celebrity-ED SEO). LegitScript seal + named partner pharmacies in /faq/general. /max and /sildenafil-tadalafil-combo are the SAME product (MAX)."
key_pages:
  about: /about
  gold: /gold
  gold_plan: /gold/plan
  sildenafil: /sildenafil
  tadalafil: /tadalafil
  vardenafil: /vardenafil
  daily_tad: /daily-tad
  max: /max
  vmax: /vardenafil-tadalafil-combo
  energy: /energy
  safety: /safety-info
  faq: /faq/general
  reviews: /reviews
  quiz: /quiz
unverified_fields:
  - "Full per-molecule plan ladders (SIL/TAD/VAR/DailyTad/MAX/VMAX/Energy quantity × monthly price) — behind the /plans;s=<code> funnel/app; only floors captured. Gold's full ladder is exposed on /gold/plan."
  - "Pharmacy ownership: site claims 'our own compounding pharmacies' yet names three separate third-party LLCs as partner pharmacies (Meds Health, National Treatment Delivery and Care, Curexa) — claim recorded, not adjudicated."

description: "Sells compounded chewable and sublingual ED medications — sildenafil, tadalafil, vardenafil — to men via an async telehealth subscription, with licensed-provider review and discreet direct-to-door delivery."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Biotech / Pharma Products, Services / Consulting]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://bluechew.com/assets/svg/logo/bluechew.svg
logos:
  wordmark: { src: https://bluechew.com/assets/svg/logo/bluechew.svg, w: 1340, h: 224 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=bluechew.com&sz=256", px: 180, transparent: false }
  og:       { src: "https://static.bluechew.com/new-chew/fallback/og.webp", w: 3952, h: 3161 }
brand_colors: { primary: "#3238FA", accent: "#D72D33" }   # STRAIN: royal-blue primary = the logomark hue (verified); red is the secondary/CTA. Gold product line uses gold/amber — a SKU color, not the brand.
fonts: [Roboto]
color_scheme: light
design_framework: angular
---

## Overview

A DTC men's sexual-health telehealth brand — the original "chewable ED" company (founded 2018, Chicago). It sells compounded PDE5-inhibitor chewables and sublinguals (sildenafil, tadalafil, vardenafil, plus apomorphine/oxytocin/caffeine blends) on a monthly auto-refill subscription. The model is async: an online medical-profile intake → licensed-provider review (usually within 24h) → discreet shipment, with no in-person or video visit. Differentiates on **form** (no-swallow flavored chewables/sublinguals) rather than molecule, and markets heavily through podcast/comedian endorsements ("5 Million+ Men Served").

## What they offer

One category (men's ED / sexual performance), a flagship plus a companion roster of forms and molecule combinations — all compounded, all subscription. Per-SKU detail in `offerings.md`.

- **GOLD — flagship, "#1 Best Seller":** 4-in-1 sublingual (Sildenafil + Tadalafil + Apomorphine + Oxytocin), 70/90/110 MG, ready in 15 min, lasts 24–36 hrs — **$79–$269/mo** by pack (6/12/18/24), "From: $7.30/ea" `[published]`
- **SIL:** Sildenafil chewable, as-needed, up to 45 MG, lasts 4–6 hrs ("the active ingredient in Viagra®") — **From: $2.95/ea**, plans "as low as $20/month" `[partial]`
- **TAD:** Tadalafil chewable, longer-acting up to 24–36 hrs ("the active ingredient in Cialis®") — **From: $3.58/ea** `[partial]`
- **VAR:** Vardenafil chewable, as-needed, 4–6 hrs ("the active ingredient in Levitra®") — **From: $4.34/ea** `[partial]`
- **MAX:** 2-in-1 sublingual (45 mg Sildenafil + 18 mg Tadalafil), ready 15 min, lasts 24–36 hrs — **From: $5.63/ea** `[partial]` *(also served at /max)*
- **VMAX:** 2-in-1 sublingual (14 mg Vardenafil + 18 mg Tadalafil) — **From: $5.63/ea** `[partial]`
- **DailyTad:** daily Tadalafil (+ vitamins), taken every day — **Starting at $100/mo** `[partial]`
- **Energy:** 2-in-1 liquid shot (30 mg Sildenafil + 60 mg Caffeine), 2 oz / 60 mL, as-needed, 4–6 hrs — **From: $4.50/ea** `[partial]`

## How it works / model

Customer journey (homepage + every PDP): **01** choose your plan (or take the /quiz), **02** complete your medical profile online (minutes), **03** a licensed provider reviews your profile (usually within 24h), **04** ships discreetly within 24h if approved. Async telemedicine — no appointment, no in-person or video visit; the provider reviews the intake and writes a prescription "if medically appropriate." Monthly auto-refill subscription billed to a card; price includes product, shipping, and taxes; **no separate membership or consult fee** ("No doctor appointments or patient support charges"). Pause or cancel anytime through the account (request ≥24h before renewal to skip the next charge). Compounded meds are filled by partner compounding pharmacies. Available across the US **except North Dakota** (+ Guam, Puerto Rico, US Virgin Islands); no international shipping.

## Positioning & audience

Targets men 18+ with ED or wanting performance/confidence enhancement. The wedge is **form + convenience + discretion**: chewable/sublingual instead of pills ("up to 40% of Americans have difficulty swallowing pills"), 100% online, discreet packaging, "affordable." Positions as the original chewable-ED brand; the 4-in-1 Gold (adding apomorphine for dopamine/arousal + oxytocin for libido — "the only formula that works on both brain and body") is the current premium differentiator. Competitive set is the broader DTC ED telehealth field — its blog is saturated with "BlueChew vs Hims / Roman / Rugiet / REX MD / Lemonaid" comparison SEO.

## Nav structure

Thin hamburger menu (products are not in nav — reached via /quiz funnel or direct PDP URLs):

```
- Sign Up/Login — https://app.bluechew.com/register
- Take the Quiz — /quiz
- About Us — /about
- FAQs — /faq/general
- Reviews — /reviews
- Contact Us — /contact
- American Heroes Program (military) — /heroes
Footer:
- HELP — Account Login (app.bluechew.com/log-in) · FAQs · Reviews · Returns & Refunds (/return-and-refund) · American Heroes · Contact
- LEARN — About Us · Blog (/our-stories) · Swag (blueswag.com)
- Social — Facebook · X · Instagram · TikTok
- Legal — Privacy & Security · Terms · Accessibility · Consumer Health Data Privacy · Your Privacy Choices
```

## Credibility & proof

- **"5 Million+ Men Served":** homepage headline (self-reported)
- **LegitScript Certified:** footer seal linking to legitscript.com/websites/bluechew.com (verified present)
- **Press logos:** "Featured on" NBC, ESPN, FOX, GOLF, ABC
- **Celebrity/comedian endorsers:** video testimonials from Andrew Schulz, Tony Hinchcliffe, Tom Segura, Bert Kreischer, Bobby Lee, Steve-O, "Uncle Lazer"
- **Testimonials:** /reviews shows "Results 1-11 of 263," all 5-star anecdotes, flagged **"Results have not been independently verified. Individual results may vary."** (self-reported; no aggregate numeric rating displayed)
- **FDA compounding disclaimer:** prominent on homepage and every Rx page — "featured products are compounded drugs… not FDA-approved… the FDA does not approve or verify compounded drugs"
- **Clinicians:** "licensed medical providers" referenced, but **no named-physician page**
- **Partner pharmacies (named, /faq/general):** Meds Health LLC (Elmhurst, IL); National Treatment Delivery and Care LLC (Deerfield Beach, FL); Curexa Pharmacy (Egg Harbor Township, NJ)

## Visual & brand impression

Royal-blue (#3238FA) identity: a white "BC" monogram logomark on a solid blue square (background baked in — not transparent) and a thin, wide letter-spaced "BLUECHEW" wordmark. Clean, modern, conversion-optimized Angular SPA. The homepage hero runs dark (black/blue) to foreground the Gold product in gold/amber; the rest of the site is light with blue accents and red CTAs. Product photography is polished and consistent (black sachets, blue tablets, liquid shots). Tone is confident, masculine, and cheeky ("HAVE BETTER SEX!", comedian endorsers) while staying inside compliance guardrails (compounding/FDA disclaimers everywhere). Design maturity is high.

## Strategic read

BlueChew created the chewable-ED niche in 2018 and competes on **delivery form**, not active ingredient — every SKU is the same generic PDE5 inhibitor a competitor sells, compounded into chewables/sublinguals/shots. Gold (apomorphine + oxytocin layered onto sil/tad) is the one SKU that feels proprietary and is the current hero push. The growth engine is podcast/comedian influencer advertising plus heavy programmatic SEO (350+ blog URLs). Notable strategic facts: **single-vertical focus** (sexual health only — no TRT, weight-loss, or hair, unlike Hims/Ro's multi-line sprawl); **compounded-only posture** (rides the 503A compounding lane — a real regulatory-exposure axis, which is why FDA disclaimers are pervasive); and fulfillment routed to named **third-party** compounding pharmacies (Curexa et al.) despite "our own pharmacies" framing.

## Provenance

- **Pages:** map (379 URLs) + 15 scrapes via Firecrawl — homepage, /about, /gold, /gold/plan, /sildenafil, /tadalafil, /vardenafil, /daily-tad, /max, /sildenafil-tadalafil-combo, /vardenafil-tadalafil-combo, /energy, /safety-info, /faq/general, /reviews.
- **Verify:** all 15 sourceURLs matched; all bodies md5-unique; no junk soft-404s.
- **Credits:** 16 (1 map + 15 scrapes).
- **Couldn't get:** full per-molecule plan ladders (behind the /plans;s=<code> funnel/app) — floors captured, Gold's full ladder exposed on /gold/plan.
- **Run profile:** express — +offerings, +telehealth, +logos.
- **Enriched (page JSON-LD, in prose):** founding 2018; founders Steve Sullivan & Alex Jovanovich; HQ 345 N Canal St STE 201, Chicago, IL 60606 — all from on-page schema.org markup, not model priors.
