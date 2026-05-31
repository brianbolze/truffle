---
schema_version: 1

# Identity
domain: getpetermd.com               # primary key — the live canonical host
name: PeterMD
aliases: [petermd.com]               # petermd.com is referenced colloquially but does NOT resolve to this site (Cloudflare-blocked / non-serving on curl 2026-05-30); getpetermd.com is the real domain. NB store folder is `getpetermd-com`, NOT the brief's `petermd-com`.
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Cloudflare-fronted (skip WebFetch). REQUIRES waitFor=5000 on homepage + all key pages (graduated permanent — waitFor:3000 was marginal). WordPress + WooCommerce + Elementor (rawHtml has wp-content + woocommerce + elementor; favicon /wp-content/Favicon-PMD.svg). branding.designSystem.framework='custom' — WRONG (§5.4). Storefront URL patterns: /category/* taxonomy, /product/* SKUs, /shop; huge set of paid-funnel landing slugs (/trt-survey, /trt-start, /landing-page*, /your-trt-assessment, etc.) in /v2/map (~494 URLs). Homepage hero is a feature-bullet ribbon — NO distinct H1 (use the ribbon as the hero proxy). Per-product state-availability strings on PDPs (e.g. NAD excludes AL/ID/LA; Tirzepatide/Sermorelin exclude AL/ID). Known render nondeterminism: a 244-line country-code phone-dropdown widget + image-src placeholders cause large byte deltas that are noise, not content; the /how-it-works 4-step bloodwork block + '133+ Biomarkers' alt lazy-load and may not render in markdown (ground-truth against the screenshot, not markdown alone) — confirmed: how_it_works rendered FAQ-heavy this run. No §5.1 contamination (6 bodies unique, sourceURLs matched; maxAge:0 + location:US + waitFor:5000 + serialized)."
key_pages:
  trt: /buy-testosterone-therapy           # TRT wedge ("View All" testosterone)
  glp1_weight_loss: /glp1-weight-loss
  tirzepatide: /tirzepatide                # FDA-language bellwether (asymmetric softening)
  nad: /nad                                # longevity
  sermorelin: /sermorelin
  hair_loss: /hair-loss
  erectile_dysfunction: /erectile-dysfunction
  how_it_works: /how-it-works              # insurance-for-labs claim
  for_her: /women-trt-product              # women's / For Her sub-line
  shop: /shop
unverified_fields:
  - "TRT tier→SKU mapping — annual ($79/mo), 6-month ($109/mo), monthly ($139/mo) tiers + $95 intro / $190 strike visible, but which SKU maps to which tier is set behind the quiz funnel (not submitted)."
  - "Biomarker count inconsistency — homepage rendered 'Up to 129 biomarkers' this run; a '133+ Biomarkers' image-alt did not surface (image-render nondeterminism). Unresolved."
  - "how_it_works 4-step bloodwork block (incl. STEP-4 'Function tracks your data') lazy-loaded and rendered FAQ-only in markdown this run; present on the page per prior captures (render artifact, not a removal)."
  - "Headcount / revenue / funding / ownership — not on the marketing site (deep-research job, not capture)."

# Description — one sentence
description: "A men's-health-led DTC telehealth clinic (with a 'For Her' line) positioning as the largest, most affordable online clinic in North America, prescribing TRT, GLP-1 weight loss, sexual-health, hair, and longevity treatments on monthly subscriptions, with insurance accepted for lab work."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth clinic service + the (largely compounded) Rx drugs
portfolio_shape: Multi-product       # TRT, weight loss/GLP-1, sexual health, performance, hair, longevity — distinct programs across 6 mega-nav verticals
business_model: Subscription         # monthly autorenew plans ($29/mo floor); annual/6-mo/monthly cadences
primary_industry: Healthcare & Life Sciences

# Visual identity — lifted from Firecrawl `branding` (homepage), confirmed against screenshot
logo_url: https://getpetermd.com/wp-content/uploads/Favicon-PMD.svg   # hostable favicon SVG; wordmark "PeterMD"
brand_colors: { primary: "#FFFF64", secondary: "#57817E", background: "#FFFFFF", text: "#000000", link: "#57817E" }   # branding.colors. Screenshot read: NOT a single-hue brand — a color-blocked, earthy-masculine palette (terracotta, mustard, teal, brown tiles); #FFFF64 (bright yellow) is the CTA/highlight accent and #57817E (muted teal) the link/secondary. Treat as a multi-color identity (see Visual & brand impression).
fonts: [GT America]                  # branding.fonts (body)
color_scheme: light                  # branding.colorScheme; white base with colored/dark section blocks
design_framework: wordpress          # rawHtml wp-content + woocommerce + elementor. branding.designSystem said "custom" — wrong (§5.4).
---

## Overview

PeterMD is a DTC telehealth clinic built around **men's health** ("Modern men's healthcare. Clear. Simple. Effective.") that competes explicitly on **scale and price** — its meta positioning is "the largest online health clinic in North America" with "unmatched pricing." TRT is the anchor vertical, surrounded by weight loss/GLP-1, sexual health, performance/longevity, and hair. It runs a small **"For Her"** line (`/women-trt-product`, women's hair/weight-loss categories) but is overwhelmingly men's-led. A distinctive claim: it's "the only national men's health clinic that allows patients to use their insurance for all lab work" (for a $25 processing fee) — a sharp contrast to peers who accept no insurance at all.

## What they offer

Six mega-nav verticals, WooCommerce SKUs behind each (a future `offerings.md` would enumerate per-SKU):

- **Increase Testosterone** — `/buy-testosterone-therapy` (the wedge): Injectable TRT **"$190 → $95" intro**, then **$79/mo (annual), $109/mo (6-month), $139/mo (monthly)** (regular $1668/yr); HCG.
- **Lose Weight** — `/glp1-weight-loss` ($105/$134/$158.50/mo tiers), **Tirzepatide** ($315/$628 intro, $149 get-started, $249/mo quarterly), B12+MIC, Phentermine.
- **Enhance Performance** — Sermorelin ($211.65 4-wk / $585 12-wk), B12+MIC, Thyroid Optimization, Modafinil.
- **Improve Sexual Function** — Sildenafil/Tadalafil ($5/tab), Mount Everest ($10/tab Max), Scream Cream, Cabergoline; "price-match 20% off" guarantee.
- **Hair Loss** — Finasteride ($60/$90), Finasteride + Follicure RX ($130), ReGenX Bundle.
- **Live Longer** — **NAD+** ($369 / 200mg/ml / 8–10 wk supply; excludes AL/ID/LA).

**`portfolio_shape: Multi-product`** — six distinct verticals, each a separately-bought program with its own page/pricing.

## How it works / model

Self-serve men's telehealth, **subscription-first**, price-led. Journey: land (very heavy paid-funnel apparatus — dozens of `/trt-survey`, `/landing-page*`, `/your-trt-assessment` slugs) → online assessment/quiz → licensed-in-each-state physician → prescription + monthly autorenew shipment. The `/how-it-works` "$29 per month" minimum is the only on-site price floor (the old "$99/month" anchor was removed in a 2026-05-13 redesign). Money is recurring subscription revenue across cadences (annual/6-mo/monthly), with deep intro discounts ($95 TRT intro vs $190 strike) as the hook.

## Positioning & audience

- **Who:** primarily B2C men (TRT, ED, weight loss, performance); a small "For Her" women's line.
- **Against:** the men's-health cohort (Hims, Hone) — PeterMD's wedge is **lowest price + largest scale + insurance-for-labs**, not clinical prestige. Generic-price-anchoring ($5/tab sildenafil) is a recurring tactic.
- **Claimed edge:** "largest online healthcare clinic in North America," "unmatched pricing," "FDA-regulated care providers," "U.S.-sourced medications," "Made In The USA," and uniquely **insurance accepted for lab work** ($25 processing fee).

## Nav structure

Rendered mega-nav (waitFor=5000). (Per prior weekly captures the mega-nav has dropped Phentermine/Modafinil submenu items for ~5 weeks while their product URLs + homepage cards persist — a static-config quirk, not a catalog change.)

```
- Increase Testosterone — /#increaseTestosterone (HCG /hcg · View All /buy-testosterone-therapy)
- Lose Weight — GLP1 /glp1-b12 · B12+MIC /b12-mic · Tirzepatide /tirzepatide · View All /pmd-weight-loss
- Enhance Performance — B12+MIC · Sermorelin /sermorelin · Thyroid /thyroid-treatment · View All /enhance-performance
- Improve Sexual Function — Sildenafil /sildenafil · Tadalafil /tadalafil · Mount Everest /mount-everest · Scream Cream · Cabergoline · View All /sexual-wellness
- Hair Loss — Finasteride /finasteride · Follicure RX /follicure-rx · ReGenX Bundle · View All /hair-loss
- Live Longer — /#LiveLonger (NAD+ /nad)
- For Her — /women-trt-product
```

## Credibility & proof

- **Scale:** "Over 400,000 patients served" / "Trusted by 400K+ subscribers."
- **Reviews:** "4.9/5 ★ — Based on 20k+ Reviews."
- **Trust badges:** "Made In The USA," "FSA, HSA Eligible With All Plans," "FDA-regulated care providers," "U.S.-sourced medications," **LegitScript** seal.
- **Regulatory self-claims (verbatim, `/how-it-works`):** physicians hold "the mandatory state medical licenses, controlled substance licenses and individual state DEA licenses"; HIPAA-compliant software; Ryan Haight Act compliance language. Per-product state-availability strings on PDPs.
- **Tirzepatide FDA-language asymmetry (a watched bellwether):** the buy panel says **"Clinically proven"** while the lower descriptive block retains "FDA-approved and clinically proven" / "Originally FDA-Approved for Weight Loss" — for a *compounded* version. A deliberate, persistent softening of FDA-approval claims in the conversion-critical panel.

## Visual & brand impression

A bolder, more **color-blocked and masculine** light-mode design than the clean-white peers — the homepage is a stack of saturated category tiles (terracotta, mustard, teal, brown) rather than whitespace. `branding.colors` reports bright yellow `#FFFF64` and muted teal `#57817E`; on the page the yellow reads as a CTA/highlight accent and the teal as link/secondary, but neither is a singular brand hue — PeterMD has a **multi-color, almost editorial-catalog identity**. GT America is the type. The overall feel is energetic, value-forward, and product-dense — consistent with the "affordable, accessible, for everyone" positioning rather than a premium-clinical one. (Notable: this is the **second yellow-forward brand** in the cohort after Hone — `#FFFF64` vs Hone's `#F8F93F`.)

## Strategic read

PeterMD is the **scale-and-price** play of the cohort: it wins on "largest + cheapest + insurance-for-labs" rather than clinical prestige or lab-first science. The durable state: a WooCommerce-backed men's-health clinic with a sprawling paid-funnel acquisition machine (dozens of survey/landing slugs), generic-price-anchoring, deep intro discounts, and a uniquely insurance-friendly lab posture. Two things worth tracking: the **persistent Tirzepatide FDA-language softening** (a compounded-GLP-1 marketing-compliance bellwether) and the small **"For Her" expansion** (a men's brand testing the women's market — mirrors the mixed-gender pattern seen across the cohort). Unlike prestige peers, PeterMD surfaces no 503A/503B carve-out or FDA-evaluated-statements disclaimer footer (a carry-forward compliance gap).

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, waitFor=5000, 2026-05-30):** homepage (`/`, rich pass: markdown + html + rawHtml + links + branding + images + full-page screenshot), `/buy-testosterone-therapy`, `/glp1-weight-loss`, `/tirzepatide`, `/nad`, `/how-it-works` — each markdown + links + full-page screenshot. Site inventory via `/v2/map` (limit 500).
- **Capture mechanics:** `maxAge:0` + `location:{country:US}` + `waitFor:5000` + serialized; all 6 bodies unique + sourceURLs matched (no §5.1 contamination). **7 credits**, clean run.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned markdown: `captures/2026-05-30/*.md`.
- **Couldn't get:** TRT tier→SKU mapping (quiz-walled); the homepage biomarker-count inconsistency (129 vs 133+); the /how-it-works 4-step block (lazy-load). See `unverified_fields`.
