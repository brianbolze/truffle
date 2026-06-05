---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: struthealth.com
name: Strut Health
aliases: ["Strut Health, LLC", "strutyours.com"]   # legal entity (footer ©); strutyours.com appears in the Authorize.net seal URL
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/struthealth
  facebook: https://www.facebook.com/struthealth
  x: https://twitter.com/struthealth
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow marketing site (cdn.prod.website-files.com; data-wf-* confirmed). The app + cart live on a separate SPA at my.struthealth.com / checkout.struthealth.com (checkout links carry ?priceId=). Category HUB pages (/mens-<cat>, /womens-<cat>) are the price backbone — each renders product cards with verbatim prices + a molecule/dose line + the checkout link; PDPs add richer dose detail. No JSON-LD on the homepage; nav is a bare div (rebuild from screenshot). /mens-testosterone-support is a thin, mis-titled landing (H1 'Testosterone Support' but ED/PE copy + 'No items found') — testosterone is served via enclomiphene (Strut Mojo), not injectable TRT. Hero carousel + the <title> rotate the lead category (anchor is snapshot-volatile). Map is ~80% /blog/ (huge content corpus) — select from homepage links, not the map."
key_pages:
  our_story: /our-story
  how_it_works: /how-it-works
  faq: /faq
  mens_hair_loss: /mens-hair-loss
  mens_sexual_health: /mens-sexual-health
  mens_weight_loss: /mens-weight-loss
  mens_skin_care: /mens-skin-care
  wellness_longevity: /mens-wellness-and-longevity
  health_testing: /mens-health-testings
unverified_fields:
  - "Anchor/featured category is a point-in-time snapshot, not fixed — the homepage hero carousel and the <title> ('Sex, Skin & Hair Meds') rotate the lead vertical."
  - "Founding year not stated on the site (founder named: Dr. Simal Patel). Headcount, funding, revenue not on a marketing site."
  - "Minor lines (nails, cold sores/valacyclovir, allergy & wellness, topical pain cream) appear in nav/URL map but weren't price-captured this run."

# Description — one sentence
description: "A DTC telehealth company and compounding pharmacy that prescribes and ships custom-compounded and generic medications for hair loss, sexual health, skin, weight loss, and longevity to men and women, via async online visits with U.S.-licensed doctors."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://cdn.prod.website-files.com/6095ae7ee40374852364f71d/6095b0ee93cc7d46fae96c97_logo.webp
logos:
  wordmark: { src: "https://cdn.prod.website-files.com/6095ae7ee40374852364f71d/6095b0ee93cc7d46fae96c97_logo.webp", w: 204, h: 62 }   # navy "strut" lowercase serif wordmark on transparent
  logomark: { src: "https://www.google.com/s2/favicons?domain=struthealth.com&sz=256", px: 256, transparent: false }                   # cream "S" monogram on a baked dark-navy square
  og:       { src: "https://cdn.prod.website-files.com/6095ae7ee40374852364f71d/60eb8a20b792b7fdfe4de944_home-bg-desk.png", w: 2878, h: 1548 }
brand_colors: { primary: "#FF8268", secondary: "#002021" }   # coral CTA primary/accent; near-black teal-navy footer + monogram. textPrimary #2F2D2E, link #E4EEFF (branding payload)
fonts: [Basis]
color_scheme: light
design_framework: webflow
---

## Overview

Strut Health is a direct-to-consumer telehealth brand and accredited compounding pharmacy serving **both men and women** across a wide menu of everyday, often-stigmatized conditions: hair loss, sexual health, skin, weight loss, wellness/longevity, sleep, and at-home lab testing. Founder **Dr. Simal Patel** (an ER/clinic/telemedicine physician) built it to pair *FDA-approved generics* with *custom-compounded prescriptions* tailored per patient and shipped to the door. The journey is asynchronous: pick a treatment → 10–15-min medical questionnaire → review (and message) a U.S.-licensed doctor → discreet 2-day shipping, with free visits, free shipping, free unlimited follow-ups, and cancel-anytime subscriptions. Compounded "Strut" and "Hairfect Rx" house formulas are the differentiator alongside cheap generics.

## What they offer

Broad, both-genders menu; prices are published on each category hub/PDP and billed as auto-refill subscriptions. Family lines (verbatim floors, with price-visibility token):

- **Hair loss (men's + women's):** compounded *Hairfect Rx* topicals (finasteride **$59/mo**, dutasteride **$69/mo**) + oral capsules (HairfectRx **$69**); generic finasteride tablets **$25**, dutasteride capsules **$39**, oral minoxidil 1.25mg **$55**, ketoconazole 2% shampoo **$25**, latanoprost hair booster **$49**, Strut Dermaroller **$11.99**; combos **$45–$89** `[published]`
- **Sexual health (men's):** *Super Strut* 4-in-1 dissolvable ED tablet **$79/mo**, *Strut Mojo* (enclomiphene + tadalafil) **$79**, *ParoxetineMax* 4-in-1 (PE) **$49**, generic sildenafil **$30**, generic tadalafil **$30** `[published]`
- **Sexual health (women's):** *Strut O Cream* **$49** `[published]`
- **Skin care:** compounded *Strut* formulas — rosacea **$59**, anti-aging **$49**, brightly **$49**, melasma **$69**, scar (women's) **$49**, eye/neck cream **$58**; tretinoin cream **$90** (men) / **$70** (women); *StrutVite* supplement **$24.99**; Flawless Combo **$89** `[published]`
- **Weight loss (men's + women's):** compounded oral semaglutide **$99**, injectable semaglutide **$149**, oral tirzepatide **$199**, injectable tirzepatide **$199**, *PeptideVite* **$46.99** `[published]`
- **Wellness & longevity:** oral sermorelin **$99**, injectable sermorelin 9mg **$119**, NAD+ injection 500mg **$149** `[published]`
- **Health testing:** at-home Men's Testosterone Panel **$89** (T, DHEA-S, Estradiol, Cortisol, SHBG), Respiratory Panel **$159** `[published]`
- **Sleep:** Strut Sleep Capsule **$59/mo** `[published]`
- **Other lines (nav-surfaced, not price-captured this run):** nails (StrutVite), cold sores (valacyclovir), allergy & wellness, topical pain cream

Per-SKU roster with molecule · dose · slug → `offerings.md`. Telehealth cohort cuts → `telehealth.md`.

## How it works / model

- **Journey:** browse a treatment → complete a quick medical questionnaire (10–15 min) → a U.S. board-certified doctor reviews and, if appropriate, prescribes → meds ship in ~2 days. "Some states do not require a phone consultation" — i.e. **async by default**, with optional physician messaging/phone/video on request.
- **Make money:** auto-refill **subscriptions** per product (monthly; some products offer 90-day supply). Free online MD visit, free 2-day shipping, free unlimited follow-ups, cancel/pause/delay anytime with no fees.
- **Fulfillment:** prescriptions route to "the pharmacy to process and ship"; the company markets **custom-compounded formulations** and carries PCAB/ACHC compounding-pharmacy accreditation seals (see `telehealth.md` for the verbatim ownership posture). Patients may opt to use their own Surescripts-network pharmacy (noted as 3–4× pricier).
- **Cash-pay:** "Strut does not accept insurance"; accepts major credit cards; HSA/FSA "may be rejected by the card issuer."

## Positioning & audience

Positions as a low-cost, low-friction, **judgment-free** digital clinic for stigmatized everyday conditions — "walk tall, unhindered by embarrassment." Explicitly **for men and women** (parallel `/mens-*` and `/womens-*` hubs, "For him / For her" tabs). Competes with the broad DTC-telehealth field (Hims/Hers/Ro-style) but leans on **in-house compounded formulas + accredited compounding pharmacy** and aggressively cheap generics ("prices much lower than competitors for the same exact drug"; "3–4× as expensive" at a retail pharmacy) as its claimed edge. SEO title bills it as "Sex, Skin & Hair Meds"; the historical core is hair loss + sexual health + dermatology, now extended into GLP-1 weight loss, peptides/NAD, sleep, and labs.

## Nav structure

Mega-nav under a "What we treat" flyout, split For him / For her (rebuilt from homepage screenshot + links; nav is a bare div, no `<header>`):

```
- What we treat
  - For him
    - Hair loss — /mens-hair-loss
    - Sexual health — /mens-sexual-health
    - Skin care — /mens-skin-care
    - Men's health testing — /mens-health-testings
    - Weight loss — /mens-weight-loss
    - Sleep — /mens-sleep
    - Wellness & Longevity — /mens-wellness-and-longevity
    - (also in URL map: testosterone support, nail formulas, cold sores, allergy & wellness, topical pain cream)
  - For her
    - Hair loss — /womens-hair-loss
    - Sexual health — /womens-sexual-health
    - Skin care — /womens-skin-care
    - Women's health testing — /womens-health-testing
    - Weight loss — /womens-weight-loss
    - Sleep — /womens-sleep
    - Wellness & Longevity — /womens-wellness-and-longevity
- My account — https://my.struthealth.com/sign-in
- How it works — /how-it-works
- Our story — /our-story
- (footer) FAQ — /faq · Help/Support — support.struthealth.com · The Journal (Blog) — /blog · Press — press@struthealth.com
```

## Credibility & proof

- **Compounding-pharmacy accreditation (footer seals):** **PCAB** + **ACHC** gold seal (links to achc.org/compounding-pharmacy) — health-merchant trust signals specific to a compounding pharmacy.
- **Security seals:** Authorize.net verified merchant (seal URL points to strutyours.com), RapidScan Secure.
- **Clinicians:** "U.S.-licensed and board-certified physicians" (FAQ); founder physician **Dr. Simal Patel** named in /our-story. No public `/physicians` roster page found.
- **Testimonials:** numerous 5-star customer quotes across homepage + category pages (self-reported, first-name-attributed; e.g. "Prices are much lower than competitors for the same exact drug!").
- **Coverage/limits (verbatim, FAQ):** ships to all U.S. states **except Arkansas** (as of Sept 2024); no international shipping; phone 1-833-Strut24; care@struthealth.com; HQ "701 Commerce Street, Dallas, TX 75202."
- *Placeholder copy note:* one homepage block still shows "Lorem ipsum" filler — minor unfinished marketing content.

## Visual & brand impression

Clean, friendly, value-oriented consumer-health aesthetic. **Coral/salmon (#FF8268)** "Start for Free" CTAs over a white canvas, anchored by a near-black **teal-navy (#002021)** footer; cream "S" serif monogram. Photography is approachable, real-people lifestyle (couples, mature adults), and product renders for the branded "Strut" SKUs are tidy isolated bottle/jar shots on soft pastel blobs (e.g. the blue *Super Strut* jar, white *Strut* pump bottle). Body type is **Basis** (geometric sans). Overall read: mid-maturity Webflow build — competent and warm, slightly busy, with a few rough edges (Lorem ipsum block, dense category grids).

## Strategic read

The interesting wedge is **vertical integration into compounding**: unlike pure telehealth routers, Strut foregrounds PCAB/ACHC-accredited compounding and its own "Strut"/"Hairfect Rx" house formulas, and competes hard on price against both retail pharmacies and DTC peers. It's a *generalist* — 12+ categories across both genders — rather than a single-vertical brand, which broadens TAM but blurs the front door (the lead category rotates between hair, sexual health, skin, and weight loss). GLP-1 weight loss, peptides/NAD, and at-home labs are the recent expansion edges. Watch items: the thin/mis-labeled testosterone page suggests catalog churn, and the cash-pay + compounded-GLP-1 posture carries the usual regulatory-exposure questions (a consumer-side judgment, not captured here).

## Provenance

- **Pages:** 20 pages analyzed via Firecrawl (maxAge:0, US geo) — homepage (rich: rawHtml + branding + full screenshot); /our-story, /how-it-works, /faq; 11 category hubs (mens + womens hair/sexual/skin/weight/wellness/testing/sleep) with rich pass for the price+prominence read; 5 flagship PDPs (Strut Mojo, Hairfect topical-finasteride, injectable semaglutide, StrutVite, injectable sermorelin) with `--images`. Map (497 URLs, ~80% /blog) used only for inventory.
- **Verify:** all 21 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** ~22 (1 map + 1 homepage + 19 page scrapes; hero/logos/signals reads free). See `fc.py spend`.
- **Couldn't get:** founding year; headcount/funding/revenue (not on a marketing site); per-SKU prices for the minor lines (nails/cold-sores/allergy/pain); exact pharmacy-ownership legal structure (only the marketing claim + accreditation seals, recorded in `telehealth.md`).
- **Run profile:** guided — full module set requested: `+offerings` (per-SKU roster), `+offerings hero images` (flagship PDP renders), `+telehealth` cohort pack, `+logos`.
- **Enriched (model knowledge):** none — all classification from captured pages.
