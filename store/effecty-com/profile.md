---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: effecty.com
name: Effecty
aliases: ["Effecty LLC", "Effecty Health"]
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/effectyhealth/
  facebook: https://www.facebook.com/effectyhealth
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow (cdn.prod.website-files.com; design_framework custom/Webflow). Full 16-SKU roster + 1/3/12-mo prices render on the homepage AND /treatments grid — the price index needs no PDP; per-SKU dose-ladder + first-month promo price live on the PDP (e.g. /weight-loss/glp-1, two lanes: Compounded GLP-1 vs GLP-1+GIP). Hero H1 rotates across the 3 verticals — A/B: yes (captured 'Hormone therapy, made simple' in markdown, 'Longevity treatment, made simple' in the screenshot, same run; no named tool). Sitewide promo banner 'Up to 50% off … code EFFECTY100' (first-month, first-time customers). No JSON-LD on homepage. Cloudflare-fronted (Turnstile widget = footer markdown noise). Subdomains: patient.effecty.com (login), support.effecty.com (help), go.effecty.com (intake funnel)."
key_pages:
  treatments: /treatments
  weight_loss: /weight-loss
  glp1: /weight-loss/glp-1
  hormones: /hormones
  longevity: /longevity
  about: /about-us
  faq: /faq
  safety: /legal/safety
unverified_fields:
  - "Founding date, founders, team — not on the marketing site (deep-research job)."
  - "Headcount, funding, ownership — not stated."
  - "Pharmacy partner not named — FAQ says 'trusted pharmacy partner' / 'state-licensed compounding pharmacies' (unnamed)."
  - "Prices/hero are a point-in-time snapshot, not fixed — sitewide EFFECTY100 first-month promo + a rotating hero H1 across the 3 verticals."

# Description
description: "A women-focused telehealth brand delivering GLP-1 weight loss, menopause hormone therapy, and longevity/peptide treatments through an async chat-based provider visit, dispensing compounded and FDA-brand meds shipped nationwide with no membership fee."

# Classification
entity_type: Company
target_market: [B2C, B2B2C]      # STRAIN: B2C core; B2B2C employer/partner channel ("works with employers, fitness studios, wellness platforms" — /about-us)
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 800, h: 309 }                                                            # inline-SVG "effecty." mark, viewBox 0 0 800 308.86
  logomark: { src: "https://www.google.com/s2/favicons?domain=effecty.com&sz=256", px: 256, transparent: false }   # navy "ef." monogram on a baked pale-blue tile
  og:       { src: "https://cdn.prod.website-files.com/68c8e1f82998e98e8dbd122c/6977abfef6b60d2472dc1e5a_9230216dd88255a186cc93bdc998c0be_social.png", w: 1200, h: 630 }
brand_colors: { primary: "#CED4BC", accent: "#171717" }   # sage-green packaging/cards + charcoal chrome; payload-reported #D14424 terracotta reads as imagery, not chrome
fonts: [Poppins]
color_scheme: light
design_framework: webflow
---

## Overview

A DTC, women-forward telehealth brand selling three lines of prescription wellness: **GLP-1 weight loss**, **menopause/perimenopause hormone therapy**, and **longevity / peptide** treatments. Patients complete an intake questionnaire, have an async chat-based visit with a state-licensed provider, and — if eligible — receive medication (compounded or FDA-brand) shipped to their door. It charges **no membership or consult fee**: the medication price is all-in, and it leans on transparent, same-at-every-dose pricing as its wedge. Tagline: *"Unveil your best self."*

## What they offer

Three subscription lines, all cash-pay / HSA-FSA-eligible, no membership fee (bold lead-in, verbatim price + visibility token; per-SKU grain in [`offerings.md`](offerings.md)):

- **Weight loss (GLP-1):** compounded GLP-1 injection **"Starting at $160/month"** (12-mo plan; up to **$205/mo** at 1-mo), a "Compounded GLP-1 + GIP" tier from **$240/mo**, oral **Metformin $80/month**, plus FDA-brand pens — **Ozempic® $1,300, Mounjaro® $1,300, Zepbound® $1,400, Wegovy® $1,600** /month `[published]`
- **Menopause hormone therapy:** **Estradiol** patch / cream / tablet, **$55–$180/month** by form + plan length; oral progesterone added **free** during intake "if you still have a uterus" `[published]`
- **Longevity / peptides:** **NAD+** injection (**$160–$225**) & nasal spray (**$180**), **Sermorelin** (**$200–$225**) & Sermorelin ODT (**$170–$190**), **Glutathione** (**$125–$175**), **Lipotropic (MIC) + B12** (**$95–$150**) /month `[published]`

Prices are the standard monthly rates shown on the homepage / `/treatments` grid (lower number = longer plan). All a point-in-time snapshot under the sitewide EFFECTY100 first-month promo.

## How it works / model

A **3-step async telehealth** journey: (1) fill out a medical intake questionnaire; (2) a board-certified, state-licensed provider reviews it and you consult via a **chat-based exchange** through a secure, HIPAA-compliant system — **24/7 access**, response within 24 hours, no scheduled video visit; (3) if prescribed, medication is dispensed by **state-licensed compounding pharmacies** and shipped free (expedited 2-day; quoted 5–7 business days). Money: recurring **medication subscriptions** (monthly / 3 / 6 / 12-month plans) — no membership or consult fee, the med price is all-in; the card is only charged once an Rx is written. **Affirm / Klarna** financing offered. Cancel anytime *before* the prescription is sent to the pharmacy for fulfillment.

## Positioning & audience

**Women-forward generalist telehealth.** Every hero image and testimonial is a woman; the HRT line is menopause/estradiol (women-exclusive), while the GLP-1 and longevity lines are clinically gender-neutral but marketed women-first — there is no men-facing content. Bundles the three hottest cash-pay DTC categories (GLP-1, menopause HRT, longevity) under one roof. Claimed edge: **transparent, all-in pricing** — "no membership fee," "no hidden fees, ever," "same price at every dose," free shipping, and unlimited provider messaging. Implicit competitive set: the broad DTC GLP-1 / menopause telehealth field (Hims & Hers, Ro, Midi, Noom, etc.). Also runs a **B2B2C partner channel** (employers, fitness studios, wellness platforms).

## Nav structure

```
- Weight Loss — /weight-loss
  - GLP-1 Injection — /weight-loss/glp-1
  - Metformin — /weight-loss/metformin
  - Mounjaro® — /weight-loss/mounjaro
  - Ozempic® — /weight-loss/ozempic
  - Wegovy® — /weight-loss/wegovy
  - Zepbound® — /weight-loss/zepbound
- Longevity — /longevity
  - NAD+ Injection — /longevity/nad
  - Sermorelin — /longevity/sermorelin
  - Sermorelin ODT — /longevity/sermorelin-odt
  - Glutathione — /longevity/glutathione
  - NAD+ Nasal Spray — /longevity/nad-nasal-spray
  - Lipotropic (MIC) + B12 — /longevity/lipotropic-b12
- Hormone Therapy — /hormones
  - Estradiol Patch — /hormones/estradiol-patch
  - Estradiol Cream — /hormones/estradiol-cream
  - Estradiol Tablet — /hormones/estradiol-tablet
- About us — /about-us
- FAQ — /faq
- Login — patient.effecty.com/login
# Footer also: Wellness Library, BMI Calculator, Testimonials, Contact Us,
#   Help Center (support.effecty.com), Shipping & Returns, Influencer Program,
#   Referral Program, Terms, Safety & Legal, Physician Code of Conduct, Consent to Telehealth
```

## Credibility & proof

- **LegitScript certified:** footer "Certified" seal linking to the legitscript.com checker for effecty.com.
- **Named physician:** "Dr. Nunzio Pagano, MD — Licensed Physician" quoted on the GLP-1 page; providers described as "board certified US-licensed healthcare professionals," paired by state.
- **Self-reported outcomes (flagged self-reported, not independently verified):** "**9/10** patients experienced weight loss," "**>80%** report their appetite is lower," "**85%** said side effects were very manageable or reported none," "**8/10** feel more in control of their eating" — from "anonymized, self-reported survey responses from 102 Effecty patients" (FAQ elsewhere says 106).
- **Testimonials:** ~8 before/after weight-loss stories (all women); disclaimer notes "certain individuals may be compensated by Effecty for their testimonials."
- **Trustpilot:** an "Excellent" Trustpilot widget is displayed (self-shown, not verified here).
- **Payment posture:** no insurance accepted; **HSA/FSA eligible** (stated on the GLP-1 page); Affirm/Klarna available.

## Visual & brand impression

Polished, warm **wellness-DTC** aesthetic that reads closer to a modern beauty/longevity brand than a clinical telehealth site. Cream/beige section bands, signature **sage-green** product cards and "effecty." packaging boxes, soft rounded corners, generous whitespace, a charcoal footer, and a lowercase serif "effecty." wordmark with a small leaf flourish. Photography is exclusively women across ages — including gray-haired, menopause-stage women — shot in warm, natural light. Design maturity is high and consistent. Two off-palette notes: the Webflow `branding` payload reports a terracotta **#D14424** "primary" that shows up mostly in lifestyle imagery (an orange dress), not brand chrome; and the app-icon/favicon is a **dark-navy "ef." ligature monogram on a pale-blue tile** — a cooler mark than the sage/cream site.

## Strategic read

A **women-first generalist** stacking the three highest-demand cash-pay DTC categories — GLP-1, menopause HRT, longevity/peptides — and competing on the **pricing axis**: all-in, no-membership, same-at-every-dose, undercutting membership-gated peers. The model is **heavily compounded-med dependent** (compounded GLP-1/liraglutide, compounded estradiol, injectable peptides), which is exactly the FDA-compounding regulatory exposure its disclaimers foreground — a structural risk if compounding rules tighten. The **rotating hero** signals it hasn't committed to a single anchor vertical; it's casting across all three, even though *every* piece of social proof (testimonials, outcome stats, primary promo funnel) is GLP-1/weight-loss — suggesting weight loss is the real acquisition engine and HRT/longevity are the cross-sell.

## Provenance

- **Pages:** homepage, /treatments, /weight-loss/glp-1, /hormones, /about-us, /faq, /legal/safety (+ /map) — Firecrawl, 2026-06-04.
- **Verify:** all 7 sourceURLs matched the request; all body md5s unique — no geo/cache contamination.
- **Credits:** 8 (1 map + 7 scrapes).
- **Run profile:** guided — even-capture emphasis; **+offerings**, **+telehealth**, **+logos** (no flagship hero-image variant).
- **Couldn't get:** founding date / founders / team, headcount, funding, the named compounding-pharmacy partner — none on the marketing site.
