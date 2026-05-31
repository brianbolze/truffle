---
schema_version: 1

# Identity
domain: telolife.com                 # primary key (telolife.com → www.telolife.com)
name: TeloLife
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "MAJOR PIVOT since the 2026-05-11 weekly snapshot — do NOT trust the old site_notes. Then: a SHOPIFY storefront with a MULTI-VERTICAL catalog (weight loss + longevity/'Thrive' + hair: NAD/Sermorelin/Glutathione/MIC/Methylene Blue/Follicle Revive etc.) and a blue+cream brand (#0000EE / #F3E8E0). NOW (2026-05-30): a single-vertical, GLP-1-weight-loss-ONLY brand on a CUSTOM React/Vite SPA (hashed /assets/*; logo on telolife-assets.s3.us-east-2.amazonaws.com) with a fully REBRANDED sage-green identity. All longevity + hair verticals are GONE. Financing-led (Cherry soft-credit-check). firecrawl-only; /v2/map returns 0 URLs (SPA, no crawlable sitemap) — discover routes from homepage links. HAZARD: SPA deep-links /packages and /pricing return HTTP 404 status but STILL render full content (client-side routing 'soft 404'); the markdown/pricing is real — don't discard on the 404. waitFor:3500-4000 renders cleanly. No §5.1 contamination (3 bodies unique, sourceURLs matched)."
key_pages:
  packages: /packages                  # 3/6/9/12-mo bundles (returns 404 status, content renders)
  pricing: /pricing                    # monthly Sema/Tirz pricing (404 status, content renders)
  how_it_works: /#how                  # 6-step flow (hash anchor on homepage)
  financing: /financing                # Cherry financing
  apply: /apply                        # health questionnaire / intake
  checkout: /checkout                  # pay by card; /commit = Cherry checkout
unverified_fields:
  - "Exact 'five GLP-1 plans' lineup — monthly Semaglutide $199/mo and Tirzepatide $275/mo are confirmed; the bundle tiers (3/6/9/12-mo, financed $/mo vs paid-in-full) are partially captured; full plan matrix + the 'up to 15% card discount' math not fully resolved."
  - "Testimonials are explicitly illustrative — 'Photos and quotes shown are for illustrative purposes. Real patient testimonials will be added as program participants share their stories.' (so '92% patient satisfaction' / '15–20% avg weight loss' are program/clinical figures, not verified TeloLife outcomes)."
  - "No named clinician / medical leadership on-site — 'licensed clinicians' / 'your clinician' generic framing only."
  - "Headcount / revenue / funding / ownership — not on the marketing site."

# Description — one sentence
description: "A single-vertical DTC telehealth brand offering doctor-guided compounded GLP-1 weight-loss treatment (semaglutide or tirzepatide) on flexible monthly or multi-month plans, delivered to the door, with Cherry financing and no insurance required."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth clinician service + the compounded GLP-1 Rx — same canonical hybrid as the cohort
portfolio_shape: Single              # SINGLE vertical: GLP-1 weight loss — semaglutide vs tirzepatide are drug options, 3/6/9/12-mo are duration variants of one program, not distinct offerings
business_model: Subscription         # monthly plans + multi-month bundles (Cherry-financed or card); recurring treatment plan
primary_industry: Healthcare & Life Sciences

# Visual identity — lifted from Firecrawl `branding` (homepage), confirmed against screenshot
logo_url: https://telolife-assets.s3.us-east-2.amazonaws.com/telolife-logo.png   # hostable S3 logo (footer); no favicon set
brand_colors: { primary: "#556650", accent: "#4A7340", secondary: "#D4D9C4", background: "#FFFFFF", text: "#1F2A1B" }   # branding.colors, screenshot-confirmed: a sage/olive + forest-green identity on white. NB this is a full REBRAND from the 2026-05-11 snapshot's blue #0000EE + cream #F3E8E0.
fonts: [DM Sans]                     # branding.fonts
color_scheme: light                  # branding.colorScheme + screenshot
design_framework: custom             # custom React/Vite SPA (hashed /assets/*; no __NEXT_DATA__/wp-content/shopify). Here branding.designSystem='custom' is plausibly correct (cf. the usual §5.4 miss).
---

## Overview

TeloLife is a focused, single-vertical DTC telehealth brand: **"Weight loss, made simple. Doctor-guided GLP-1 care."** A customer picks a plan, completes a ~5-minute online health questionnaire, a licensed clinician reviews and (if appropriate) prescribes a **compounded GLP-1** (semaglutide or tirzepatide), and the medication ships discreetly in 3–5 days with 24/7 provider support. The distinctive mechanic is **financing-first** — Cherry runs a 30-second soft credit check so customers can spread payments over time, or pay by card. No insurance required. (This is a substantially different, narrower company than the 2026-05-11 capture, which was a multi-vertical Shopify catalog — see `site_notes`.)

## What they offer

**One offering: compounded GLP-1 weight-loss treatment**, sold as "five flexible plans":

- **Semaglutide** — $199/mo (monthly); bundles: 3-mo ($597 total), 6-mo ($1,194), 9-mo ($1,791), 12-mo ($2,388) — financed from ~$26–$106/mo via Cherry, or paid by card (save up to 15%).
- **Tirzepatide** — $275/mo (monthly), with equivalent multi-month bundles.

**`portfolio_shape: Single` — and this is the cohort's lone `Single`.** Unlike every peer (Eden/Hone/PeterMD/Hims, all `Multi-product`), TeloLife sells *one thing*: GLP-1 weight loss. Semaglutide vs tirzepatide are **drug options within the one program** (a clinician picks the molecule for you), and 3/6/9/12-month are **duration variants** — not distinct offerings a customer comparison-shops between. By the TAXONOMIES test (and the Benadryl "one purpose, many forms → `Single`" cue), this is a clean `Single`. **It is also a real divergence, not a classification wobble:** TeloLife *used* to be multi-product (the 2026-05-11 snapshot had three verticals) and deliberately dropped longevity + hair to become GLP-1-only.

## How it works / model

A streamlined 6-step funnel (verbatim headers): (1) Pick the plan → (2) Finance or pay by card → (3) Get approved in 30 seconds (Cherry soft credit check) or skip to checkout → (4) Health questionnaire (~5 min) → (5) Meet your clinician (reviews + prescribes compounded GLP-1) → (6) Care delivered to your door (3–5 days, 24/7 support). Money is made on **recurring monthly plans and prepaid multi-month bundles**, with consumer financing (Cherry) as the conversion lever and a card-payment discount as the alternative.

## Positioning & audience

- **Who:** B2C adults seeking GLP-1 weight loss who want a simple, financeable, no-insurance path ("I didn't want another fad diet").
- **Against:** the broad multi-vertical telehealth players (Eden, Hims, Hone) and other GLP-1-only brands — TeloLife competes on **simplicity + financing accessibility + discretion**, deliberately narrow.
- **Claimed edge:** "made simple" — month-to-month or bundle flexibility, Cherry financing, no insurance hurdles, no waiting rooms, discreet delivery.

## Nav structure

Custom-SPA nav (renders in markdown; no mega-nav):

```
- Home — /
- How it works — /#how
- Packages — /packages   ·   Pricing — /pricing   ·   Financing — /financing
- Questionnaire (intake) — /apply   ·   Pay by Card — /checkout   ·   Cherry Checkout — /commit
- Stories — /stories   ·   FAQ — /packages#faq
- Sign in — /auth?mode=signin
- Affiliate Program — /affiliate/apply
```

## Credibility & proof

- **LegitScript Certified** (footer seal) — the primary trust signal.
- **HIPAA compliant · Licensed clinicians · FDA-registered pharmacies** (hero trust row).
- **Program stats (caveated):** "92% Patient satisfaction," "15–20% Avg. weight loss," "24/7 Care support" — but the site explicitly states the photos/quotes are *illustrative* and real testimonials are pending, so these read as program/clinical figures, not verified TeloLife outcomes.
- **Legal completeness:** full legal suite (Privacy, California Privacy Notice, Terms, HIPAA Notice, Medical Disclaimer, Cancellation & Refund) — more buttoned-up than the thin 2026-05-11 site.
- **No named medical leadership** — generic "your clinician" framing (a credibility gap vs. Hims' named advisory board or Hone's ambassadors).

## Visual & brand impression

A clean, calm, **single-hue light-mode** design built entirely around **green** — sage/olive `#556650` and forest `#4A7340` on a pale-sage `#D4D9C4` / white canvas, with near-black-green `#1F2A1B` text and minimalist green GLP-1 vial photography. DM Sans throughout; a serif-italic accent on headlines ("made simple."). The feel is modern-wellness and uncluttered — appropriate to the "made simple" single-vertical positioning. **This is a full rebrand** from the 2026-05-11 snapshot's electric-blue (#0000EE) + cream identity — color, framework (Shopify → custom SPA), and scope (multi-vertical → GLP-1-only) all changed together.

## Strategic read

TeloLife is the cohort's **focused outlier**: where the others sprawl across hormones/hair/longevity/sexual health, TeloLife stripped down to a single financeable GLP-1 weight-loss product on a custom SPA. The capture caught a company mid-reinvention — a multi-vertical Shopify catalog rebuilt into a narrow, conversion-optimized, financing-led GLP-1 brand. The durable state worth recording: a single-vertical compounded-GLP-1 telehealth brand competing on simplicity + Cherry financing + discretion, with thin proof (illustrative testimonials, no named clinicians) and a complete legal footprint. For the store, TeloLife is the valuable `portfolio_shape: Single` data point in an otherwise uniformly-`Multi-product` cohort — and a vivid example of why captures must re-read the live site, not trust prior snapshots (the pivot would be invisible to a memory-based classifier).

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30):** homepage (`/`, rich pass: markdown + html + rawHtml + links + branding + images + full-page screenshot), `/packages`, `/pricing` (both render content under a 404 status — SPA soft-404). Site inventory via `/v2/map` (limit 500 → **0 URLs**, SPA has no crawlable sitemap).
- **Capture mechanics:** `maxAge:0` + `location:{country:US}` + `waitFor:3500–4000` + serialized; all 3 bodies unique + sourceURLs matched (no §5.1 contamination). **~4 credits** (1 map + 3 scrapes) — lean, because the brand is single-vertical.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned markdown: `captures/2026-05-30/*.md`.
- **Couldn't get:** full five-plan bundle matrix + card-discount math; named clinicians (none on-site). See `unverified_fields`.
