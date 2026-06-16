---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: sermorelin.com
name: Sermorelin.com
aliases: []
legal_entity: "Sermorelin Strategic Holdings, LLC"
parent: []
owns: []
socials: {}                          # looked (JSON-LD sameAs + footer/header) — no operated channel found
external:
  trustpilot: https://www.trustpilot.com/review/sermorelin.com

# Capture meta
captured_at: 2026-06-16
capture_method: firecrawl
site_notes: "Webflow (cdn.prod.website-files.com, data-wf-). Programmatic-SEO content farm underneath the funnel — 100+ /article/, /listicles/, /author/ paths (filter as noise). Pricing lives on the homepage + each product page (Injectable/Oral tabs, $149/$169/$199 plan tiers); no separate /pricing. Companion lines (enclomiphene, GHK-Cu) are NOT in the header nav — reachable only by direct URL / SEO. GHK-Cu runs a SEPARATE intake+fulfillment backend (meds.you.withrefill.com / Refill) vs start.sermorelin.com for sermorelin + enclomiphene. Cloudflare Turnstile on email-capture forms. Meta description is geo-templated ('Sermorelin in Sheridan, WY'). No clean standalone wordmark — header is a square 's' Webclip mark + a raster Sermorelin+Trustpilot lockup (rendered white via SVG color-matrix for the dark header)."
key_pages:
  homepage: /
  about: /about
  what_is_sermorelin: /what-is-sermorelin
  enclomifene: /enclomifene
  ghk_cu: /ghk-cu
  glp1_combination: /glp1-combination
  intake: /intake
  start_visit: https://start.sermorelin.com/start-online-visit/serm-v2
  patient_login: https://my.sermorelin.com/
unverified_fields:
  - "Trustpilot rating value — Trustpilot is linked/badged in the header lockup but no numeric rating was captured verbatim on the analyzed pages."
  - "Prices are a point-in-time promo snapshot, not fixed — every plan shows a struck-through $199/mo against a discounted $149–$179/mo with a 'Save $50 every month' / 'auto-applied at checkout' promo; the discount may rotate."

# Description
description: "A DTC telehealth brand selling physician-prescribed, compounded sermorelin peptide therapy (injection + oral tablets) on a monthly subscription, with enclomiphene and GHK-Cu companion lines, fulfilled by a third-party U.S. compounding pharmacy."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://cdn.prod.website-files.com/694bd7eea6624d2162babab6/69bf2624401dbded0b4569c5_Copy%20of%20Sermorelin%20PLUS%20Trustpilot%20logo.svg   # STRAIN: header lockup (Sermorelin name + Trustpilot widget), not a clean wordmark — no standalone mark on site
logos:
  wordmark: { src: "https://cdn.prod.website-files.com/694bd7eea6624d2162babab6/69bf2624401dbded0b4569c5_Copy%20of%20Sermorelin%20PLUS%20Trustpilot%20logo.svg", w: 222, h: 131 }   # STRAIN: Sermorelin+Trustpilot header lockup (raster-in-SVG, white-filtered for dark header); only mark+name asset on site
  logomark: { src: "https://www.google.com/s2/favicons?domain=sermorelin.com&sz=256", px: 256, transparent: false }   # black lowercase 's' on a baked white square
  og: { src: "https://cdn.prod.website-files.com/694bd7eea6624d2162babab6/698b7bf00d0cf54678ca77dd_690b68cd0dc6bcc6c38945051e215a13_Sermorelin.com%20Open%20Graph.png", w: 1200, h: 630 }   # hand holding a blue 'Sermorelin 5mL 10mg' vial on cream
brand_colors: { primary: "#1C5087", accent: "#00C9A7" }   # brand blue (sections, vial label, text) + teal/mint CTAs, on a #FAF8F5 cream background
fonts: [Inter Tight, Inter]
color_scheme: light
design_framework: Webflow
---

## Overview

Sermorelin.com is a physician-supervised DTC telehealth brand selling **compounded sermorelin peptide therapy** to U.S. adults on a monthly subscription. The model is the now-standard async funnel: a 5-minute online eligibility quiz, an asynchronous review/prescription by a licensed physician, then home delivery from a compounding pharmacy — "You won't be charged unless your doctor approves." Sermorelin (the namesake molecule, a GHRH analog pitched as a natural-feedback alternative to synthetic HGH) is the hero; **enclomiphene** (a testosterone-optimizing SERM) and **GHK-Cu** (a copper-peptide skin/hair/longevity line) are companion lines reachable only by direct URL, not the header nav. The brand is a thin marketing/clinical-routing layer — a Wyoming holding company over a named third-party physician group and compounding pharmacy.

## What they offer

Flagship + companions, all monthly subscription. Every plan shows a struck-through **$199/mo** against a promo-discounted price ("Save $50 every month," auto-applied):

- **Sermorelin therapy (flagship):** Injectable + Oral dissolving tablets (ODT, sublingual), same price both formats — **$199/mo monthly · $169/mo 3-month (save 15%) · $149/mo 6-month (save 25%, "Most Popular")** `[published]`
- **Enclomiphene:** oral capsule, "Optimize Your Testosterone Naturally" — Standard **375mg/month $149/mo** · High Dose **750mg/month $179/mo** `[published]`
- **GHK-Cu (copper peptide):** Injectable **$199/mo** · Topical Skin (Aquabiome+ GHK-Cu Cream, 30g/mo) **$190 / $214 / $225/mo** · Hair Restoration (topical solution, 30mL/mo) **$229/mo** · with Epithalon (weekly injection, 400u/mo) **$219/mo** `[published]`
- **Sermorelin + GLP-1 combination:** education/positioning page only — sermorelin pitched as a *companion* to GLP-1 for lean-mass preservation; **no standalone SKU sold** `[on-request]`

Per-SKU roster (formats × plan tiers, all verbatim prices) in `offerings.md`. Cohort cuts in `telehealth.md`.

## How it works / model

1. **Eligibility Quiz** — short online health/medical-history quiz (`start.sermorelin.com`; GHK-Cu routes to `meds.you.withrefill.com`).
2. **Provider Evaluation** — a licensed physician reviews asynchronously and prescribes "if appropriate" / "a personalized plan."
3. **Free Delivery** — a U.S. state-licensed compounding pharmacy ships directly, free 2-day discreet shipping.

Revenue is a recurring monthly med subscription ($149–$229/mo depending on line/plan), all-in with no separate membership or consult fee, "cancel anytime." Risk-reversal: 180-day money-back guarantee on the 6-month plan (months 2–6).

## Positioning & audience

- **Audience:** adults 30+ with fatigue, poor sleep, declining recovery, or "signs of aging." Male-leaning execution (muscular-man hero, muscle/energy/vitality benefits, an enclomiphene testosterone line) but not men-only — female testimonials and women-targeted SEO content are present.
- **Against:** synthetic HGH (sermorelin framed as the safer, body's-own-feedback alternative); in-person clinics; and lab-heavy competitors — testimonials explicitly knock **MaleMD** and **Eden** for "full blood panels and months of back and forth."
- **Claimed edge:** physician-prescribed + no labs required + same-day approval + 48-hour shipping, wrapped in published-research citations.

## Nav structure

Header nav covers only the sermorelin education pages (companion lines are unlisted):

```
- What is Sermorelin — /what-is-sermorelin
- Sermorelin Dosage — /dosage
- Side Effects — /side-effects
- Muscle Growth — /muscle-growth
- Sermorelin and GLP-1 — /glp1-combination
- Read Reviews — https://www.trustpilot.com/review/sermorelin.com
- Get Started — https://start.sermorelin.com/start-online-visit/serm-v2
- Login — https://my.sermorelin.com/
Footer:
- About — /about
- Authors — /authors
- Physician Code — /legal/physician-code-of-conduct
- Telehealth Consent — /legal/telehealth-consent
- Shipping / Refund / Return / Terms / Privacy — /legal/*
Unlisted (direct-URL / SEO only): /enclomifene, /ghk-cu, /refill, /dosage, /muscle-growth
```

## Credibility & proof

- **LegitScript Certified** — footer + /about seal (cert 48955804), "Sermorelin.com is LegitScript approved."
- **Named medical provider:** "Wasef Health, PC / Dr. Michael Wasef, MD," 5260 78th Ave N, PO Box 1697, Pinellas Park, FL 33780 (contact@wasef-health.com) — /about + homepage FAQ.
- **Named pharmacy partner:** "SmartScripts / PerfectRx," 5810 Long Prairie Rd, Flower Mound, TX 75028, (866) 866-6806, perfectrx.com — /about + homepage FAQ.
- **Research citations** (cited, not endorsements): Mayo Clinic; Walker RF, *Clinical Interventions in Aging* 2006 (PMC2699646); Sattler F et al., *Transl Androl Urol* 2020 (PMC7108996); an MDPI study.
- **Trustpilot** reviews linked + a Trustpilot widget in the header lockup (no numeric rating captured verbatim — see `unverified_fields`).
- **"50+ Sold Today"** badges on the product cards — self-reported, flagged.
- **Verified Patient** testimonials with specific weight-loss/sleep/recovery claims; FDA disclaimer present ("not evaluated by the FDA… not intended to diagnose, treat, cure, or prevent any disease").
- **Guarantee:** 180-day money-back on the 6-month plan; free 2-day discreet shipping.

## Visual & brand impression

Polished, conversion-optimized Webflow funnel. Cream (#FAF8F5) ground with deep-blue (#1C5087) section blocks and teal/mint (#00C9A7) pill CTAs; Inter / Inter Tight type; rounded cards (24px) and product-vial renders throughout. Trust signals are stacked heavily (LegitScript, NIH/Mayo/MDPI logos, Trustpilot, guarantee badges, "50+ sold today"). Underneath sits a large programmatic-SEO content farm (100+ articles/listicles). Professional but template-driven — and the template shows: the GHK-Cu page carries a stray "Next-generation *testosterone* therapy" heading and a reused "BPC-157 Vial" product image, evidence of fast, templated SKU expansion.

## Strategic read

- **This is close to the Teleprescribe V1 plan already live in market:** single-molecule sermorelin lead, ~$199/mo all-in, physician-prescribed, compounding-pharmacy fulfillment, *no labs required* — and it competes head-on on speed ("same-day approval, 48h shipping") and on undercutting the lab-heavy players it names (MaleMD, Eden).
- **They've already expanded past the lead molecule** into **enclomiphene** (a testosterone-optimization SERM — adjacent to the TRT lane TV avoids, though non-scheduled) and **GHK-Cu** (skin/hair/longevity). The brand name is sermorelin but the catalog is becoming a general compounded-peptide shop.
- **Two backends, one brand:** sermorelin + enclomiphene route to `start.sermorelin.com`; GHK-Cu routes to `meds.you.withrefill.com` (Refill). Suggests a bolt-on platform/pharmacy for the newer line — a thin brand over potentially multiple fulfillment partners.
- **Thin-brand / holding-co structure:** "Sermorelin Strategic Holdings, LLC" (Wyoming; 307 phone; geo-templated "Sheridan, WY" meta) over a named third-party physician group (Wasef Health) and pharmacy (PerfectRx/SmartScripts) — the brand owns acquisition + funnel, outsources clinical + fulfillment.
- **Acquisition engine = programmatic SEO:** 100+ templated articles/listicles ("best sermorelin for sleep," "cheapest sermorelin online in 2026") farming long-tail sermorelin search — a different growth motion than paid-social, and a moat worth noting for a competitor leading with the same molecule.

## Provenance

- **Pages:** 6 analyzed via Firecrawl (`maxAge:0`, US, all-formats) — homepage, /about, /what-is-sermorelin, /enclomifene, /ghk-cu, /glp1-combination; + 1 map. Structured layer (`fc.py signals`) read off the homepage `rawHtml` (JSON-LD Organization/Physician/Product + branding).
- **Verify:** `fc.py verify` — all 6 sourceURLs match, all bodies md5-unique, no junk soft-404s.
- **Credits:** 7 (1 map + 6 scrapes). Logos rode the homepage payload (no new credits).
- **Couldn't get:** Trustpilot numeric rating (linked/badged, not on captured pages); /dosage, /side-effects, /muscle-growth, /refill not scraped (education/flow pages, no new offering signal).
- **Run profile:** Express — telehealth cohort pack (`telehealth.md`) + `+offerings` roster + `+logos` (deep gate: Companies `Direct competitor? = Yes`).
