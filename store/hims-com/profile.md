---
schema_version: 1

# Identity
domain: hims.com                     # primary key (hims.com → www.hims.com)
name: Hims
aliases: []                          # forhims.com asset host seen; hers.com/forhers.com is a SIBLING entity, not an alias
parent: ["Hims & Hers Health, Inc."]   # brand-of; parent shares hims.com (no distinct corporate domain). Sibling brand: Hers (forhers.com)
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Cloudflare-fronted (plain curl to hims.com → www.hims.com 403; skip WebFetch, Firecrawl-only). JS-driven mega-nav does NOT render as <nav> in Firecrawl HTML — reconstruct nav from homepage hrefs + map. Quiz-funnel URLs (/g/i/*) are JS-hydrated, return only a consent banner via Firecrawl. Asset CDN is Cloudinary (forhims/image/upload). rawHtml shows NO __NEXT_DATA__/_next or wp-content marker this run — framework left unverified (branding.designSystem said 'custom'; don't assert Next.js without a marker, §5.4). /v2/map at limit:500 ~292 URLs; investors.hims.com + support.hims.com subdomains appear — filter to www.hims.com. Per-product pricing shows as 'Starting at $X/mo' / 'From $X/mo†'; final price set behind quiz funnels. KNOWN: occasional Firecrawl 'Bad Gateway' (502) on the first homepage pass — retry once (did NOT recur this run). No §5.1 contamination (6 bodies unique, sourceURLs matched; maxAge:0 + location:US + waitFor:4000 + serialized)."
key_pages:
  weight_loss: /weight-loss                # flagship GLP-1 storefront
  weight_loss_membership: /weight-loss/membership   # $39 first mo / $149/mo
  erectile_dysfunction: /erectile-dysfunction
  testosterone: /testosterone              # enclomiphene; Kyzatrex/cypionate "Coming in 2026"
  labs: /labs                              # at-home blood testing + Galleri multi-cancer
  psychiatry: /psychiatry
  about_company: /about/the-company        # parent (Hims & Hers Health, Inc.) info
  how_it_works: /how-it-works
unverified_fields:
  - "Final per-product prices for ED / weight loss / testosterone are 'Starting at $X/mo' anchors; the real price is set behind the quiz funnels (/g/i/*), which are JS-walled and were not submitted."
  - "Top-level mega-nav structure is inferred from homepage hrefs (JS nav doesn't render as <nav>)."
  - "Testosterone: Kyzatrex® and testosterone cypionate still 'Coming in 2026' — not purchasable, no pricing (carry-forward 5+ prior captures)."
  - "design_framework — no rawHtml marker found; left empty (Cloudinary CDN only confirms the asset host, not the app framework)."
  - "Headcount / revenue / funding — public-company financials are off-site (10-K territory), not the marketing site."

# Description — one sentence
description: "The men's consumer brand of Hims & Hers Health, Inc. (NYSE: HIMS) — a DTC telehealth platform connecting men to licensed providers for ED, hair loss, weight loss (GLP-1s), testosterone, mental health, and at-home labs, with prescriptions filled by partner pharmacies on monthly subscriptions."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company                 # operates as a full business; it's a brand of a parent (see NOTE) but transacts independently → Company, not Other
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth platform service + Rx (incl. branded + compounded) products
portfolio_shape: Multi-product       # ED, hair, weight loss/GLP-1, testosterone, mental health, skin, labs — distinct, separately-bought verticals
business_model: Subscription         # per-product monthly subscriptions + a separate Weight Loss Membership ($39 first / $149/mo)
primary_industry: Healthcare & Life Sciences

# Visual identity — lifted from Firecrawl `branding` (homepage), confirmed against screenshot
logo_url: https://www.hims.com/forhims/image/upload/q_auto,f_auto,fl_lossy,c_limit/Hims/apple-touch-icon-hims   # Cloudinary-hosted touch icon (favicon); wordmark is lowercase "hims" in brand brown
brand_colors: { primary: "#C79B85", accent: "#FFC671", secondary: "#0000EE", background: "#FFFFFF", text: "#453421" }   # branding.colors. Screenshot read: a warm, earthy palette — tan/sand #C79B85 section blocks, dark-brown #453421 text/wordmark, gold #FFC671 highlights. The #0000EE 'secondary' is a generic link blue, not a brand hue. Warm-masculine identity.
fonts: [Sofia Pro, Helvetica]        # branding.fonts: Sofia Pro=body/brand
color_scheme: light                  # branding.colorScheme + screenshot
design_framework:                    # unverified — no __NEXT_DATA__/wp-content marker in rawHtml; branding said "custom" (don't trust, §5.4)
---

## Overview

Hims is the **men's consumer brand** of **Hims & Hers Health, Inc.** (NYSE: HIMS, founded 2017) — a publicly traded DTC telehealth platform. The hims.com storefront connects men to a network of 400+ U.S.-licensed providers across all 50 states: an online intake → provider review → prescription filled by a partner pharmacy and discreetly shipped, on a monthly subscription. Originally launched (2017) for ED, hair loss, and anxiety, the brand now spans sexual health, hair, **weight loss (GLP-1s)**, testosterone, mental health, skin care, and at-home labs. (Hers, the women's brand at forhers.com, is the sibling brand of the same parent.)

## What they offer

Seven consumer verticals, each a distinct storefront (a future `offerings.md` would enumerate per-SKU):

- **Weight Loss (GLP-1)** — the headline line. Branded **Wegovy® Pen** "From $199/mo†," **Wegovy® Pill** "From $149/mo†," **Zepbound® Vial/KwikPen®** "From $299/mo†," **Ozempic® Pill/Pen** "From $149–$199/mo†," compounded **Foundayo®**, plus higher-priced branded Mounjaro®/Zepbound® pens ($1,899/mo). Requires a **Weight Loss Membership** ($39 first month, then $149/mo) on top of medication cost.
- **Sexual Health / ED** — `/erectile-dysfunction`: a deep lineup — Hard Mints, sildenafil/tadalafil chews ("Starting at $30/mo"), generic Viagra® "Starting at $22/mo," generic Cialis® "Starting at $24/mo," and 2-in-1 "Sex Rx +" bundles "Starting at $39/mo."
- **Hair Loss** — finasteride ($22/mo), topical/serum/spray hybrids ($29–$33/mo), minoxidil, Hair Power Pack ($60/mo).
- **Testosterone (Testosterone Rx+)** — enclomiphene "starts at $99/month"; Kyzatrex® + cypionate **"Coming in 2026."**
- **Mental Health / Psychiatry** — "plans starting at $49/mo," 8 generic SSRIs/SNRIs.
- **Labs by Hims** — at-home blood testing ("1,000+ health conditions," 130+ tests/yr); add-on **Multi-Cancer Test by Galleri®**.
- **Skin Care** — `/skin-care`.

**`portfolio_shape: Multi-product`** — seven distinct verticals a customer chooses among, each its own storefront/pricing.

## How it works / model

A telehealth **platform** model: detailed online intake (dynamically branching) + identity verification → licensed provider reviews and, if appropriate, prescribes → partner pharmacy fills + ships → 24/7 care-team messaging via the Hims app. Monetized through **per-product monthly subscriptions** plus a separate **Weight Loss Membership** ($39 first month / $149/mo, medication extra). Compounded products carry FDA non-approval disclaimers; the model spans branded *and* compounded drugs.

## Positioning & audience

- **Who:** B2C men ("Men's healthcare, built for real life," "The care you've always deserved").
- **Against:** the men's-telehealth field (PeterMD, Hone) and the GLP-1 players — Hims competes on **breadth + brand + scale + FDA-approved branded GLP-1 access** (it carries branded Wegovy/Zepbound/Ozempic alongside compounded options).
- **Claimed edge:** "The best care by the best in medicine" — 400+ vetted providers, a named medical advisory board (dermatology/internal medicine/psychiatry/pharmacy), at-home labs, and the trust of a public company.

## Nav structure

JS mega-nav (inferred from hrefs + map):

```
- Weight loss — /weight-loss  (Wegovy Pen/Pill, Zepbound Vial/KwikPen, Foundayo, Ozempic Pill/Pen; The Science; Membership /weight-loss/membership)
- Sexual health (ED) — /erectile-dysfunction  (sildenafil, tadalafil, Cialis, sertraline-for-PE; quiz /g/i/sh)
- Hair loss — /hair-loss  (finasteride, topical finasteride, minoxidil, Hair Power Pack)
- Testosterone — /testosterone  (enclomiphene; Kyzatrex/cypionate "Coming 2026")
- Mental health — /mental-health, /psychiatry
- Skin care — /skin-care
- Labs — /labs  (Biomarkers, Multi-Cancer Test by Galleri®)
- About — /about, /about/the-company, /about/clinical-excellence; Tools (free calculators); Blog
```

## Credibility & proof

- **Public company:** Hims & Hers Health, Inc., **NYSE: HIMS** (the strongest trust signal in the cohort).
- **Provider network:** "more than 400 U.S.-licensed healthcare providers in all 50 states," "highly trained and rigorously vetted"; a medical advisory board; featured medical leadership (Dr. Craig Primack, Dr. Peter Stahl, Dr. Brian Williams, Dr. Alicia Warnock, Dr. Deepak L. Bhatt).
- **Trust badges:** "FDA Approved" on branded GLP-1 cards; "FSA & HSA eligible" propagating across GLP-1 PDPs; **LegitScript** seal.
- **Compliance:** recurring compounded-drug disclaimer ("Compounded drug products are not approved nor evaluated for safety, effectiveness, or quality by the FDA. Rx required"); Testosterone Rx+ "not approved or evaluated… not available in all 50 states"; Galleri multi-cancer-test non-FDA-approved footnote; off-label-use framing on T2D-only GLP-1 PDPs (Ozempic Pill/Pen).

## Visual & brand impression

A premium, **warm-earthy** light-mode aesthetic that sets Hims apart from the clinical-white peers: tan/sand `#C79B85` section blocks, **dark-brown** `#453421` text and the lowercase "hims" wordmark, and gold `#FFC671` highlights, with cinematic product photography (GLP-1 pens, confident male portraiture). Sofia Pro is the brand type. The look is editorial and lifestyle-led — "normalizing health and wellness" — reading as the most brand-mature, consumer-marketing-polished site in the cohort (consistent with a public, scaled company). (`branding.colors.secondary` #0000EE is a generic link blue, not a brand hue — another reminder the slots aren't semantically stable.)

## Strategic read

Hims is the **scaled, public-company anchor** of the cohort — the one with branded FDA-approved GLP-1 access, a 400+ provider network, a named advisory board, and a polished consumer brand. The durable state worth recording: a two-brand (Hims/Hers) telehealth *platform* under one public parent, monetizing per-vertical subscriptions plus a GLP-1 membership, spanning branded *and* compounded drugs. **The relationship is the key system signal here: hims.com is a brand-of Hims & Hers Health, Inc., with a sibling brand (Hers) — and the SCHEMA still has no frontmatter field to express parent/brand-of/sibling links** (now the 4th sighting after AWS→Amazon, Benadryl→Kenvue, Nike→Jordan/Converse). Worth tracking: testosterone-vertical expansion (Kyzatrex/cypionate "Coming 2026") and the systematic off-label-use framing on T2D-only GLP-1 PDPs.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30):** homepage (`/`, rich pass: markdown + html + rawHtml + links + branding + images + full-page screenshot), `/weight-loss`, `/erectile-dysfunction`, `/testosterone`, `/labs`, `/about/the-company` — each markdown + links + full-page screenshot. Site inventory via `/v2/map` (limit 500, filtered off investors./support. subdomains).
- **Capture mechanics:** `maxAge:0` + `location:{country:US}` + `waitFor:4000` + serialized; all 6 bodies unique + sourceURLs matched (no §5.1 contamination; no 502 this run). **7 credits**, clean run.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned markdown: `captures/2026-05-30/*.md`.
- **Couldn't get:** final quiz-walled prices (/g/i/* JS-hydrated); app framework (no rawHtml marker). See `unverified_fields`.
