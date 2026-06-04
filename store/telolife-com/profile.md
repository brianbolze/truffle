---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: telolife.com
name: TeloLife
aliases: []                          # legal entity "TeloLife, Inc."; prior brand "TELO" survives only in a stale og:image — noted in prose, not asserted as a live alias
parent: []
owns: []
socials: {}                          # looked — none found (no social anchors in footer/nav; no JSON-LD sameAs)
external: {}                         # looked — none found (LegitScript is a cert seal → Credibility, not a 3rd-party record)

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Static React/Vite SPA built with Lovable, hosted on S3/CloudFront. Map returns 0 URLs (custom SPA) — discover via homepage nav + footer links. SPA routes (/packages, /pricing, /financing) return HTTP 404 on direct scrape but render FULL content (soft-404, trust the body — §5.6). Pricing & packages are fully PUBLISHED (no quiz wall): /pricing has the per-molecule monthly rate, /packages the bundle totals. /packages has Cash↔Financing + Semaglutide↔Tirzepatide toggles — captured state was Financing+Semaglutide, so only Semaglutide bundle totals are in-capture (Tirz needs the toggle). Footer S3 logo (telolife-assets.s3…/telolife-logo.png) 403s; the live mark is only the Vite-hashed /assets/telolife-logo-*.png (a square TELO monogram, not a horizontal wordmark). og:image is a STALE Lovable preview showing prior 'TELO' branding (cream palette + family-photo hero), not the current sage/vials design."
key_pages:
  packages: /packages
  pricing: /pricing
  financing: /financing
  how_it_works: /#how
  terms: /legal/terms.html
unverified_fields:
  - "Tirzepatide bundle totals (3/6/9/12-mo) — /packages defaulted to the Semaglutide toggle; only the Tirzepatide monthly rate ($275/mo) is in-capture."
  - "Named Provider Groups and compounding pharmacies — Terms reference them generically ('independent, licensed Provider Groups'; 'FDA-registered, state-licensed compounding pharmacies'); none is named on the site."
  - "Founders, team, headcount, funding, launch date — no about/team page exists (the © 2026 site reads freshly launched; testimonials are explicitly placeholder)."

# Description — one sentence (~160-220 chars)
description: "Sells compounded GLP-1 weight-loss therapy (semaglutide, tirzepatide) direct to consumers via independent licensed telehealth provider groups, on an all-inclusive monthly cash price with optional Cherry financing, shipped to the door."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth hybrid: clinician-delivered care (primary) + compounded Rx product
portfolio_shape: Single              # one offering — compounded GLP-1 weight loss — in two molecules × duration tiers; not separately-positioned lines
business_model: Subscription         # recurring monthly; multi-month bundles prepay the same monthly rate
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint, confirmed against the homepage screenshot
logo_url: "https://www.google.com/s2/favicons?domain=telolife.com&sz=256"   # the square "TELO" monogram — the brand's sole reachable mark (no horizontal wordmark; footer S3 wordmark 403s)
logos:
  # wordmark slot omitted — TRUE absence of a horizontal mark+name asset (the header uses the square monogram + HTML "TeloLife" text; the named S3 wordmark 403s)
  logomark: { src: "https://www.google.com/s2/favicons?domain=telolife.com&sz=256", px: 256, transparent: true }   # stacked "TELO": blue letters + a mint-green "O" ring; transparent PNG (live header copy is 410×404, hasAlpha)
  og:       { src: "https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/47fd8db1-2aa9-4a9b-b9c7-90b64ae4f245/id-preview-04492acf--fdf8ddbd-217d-4de5-8f12-ee819a55cb15.lovable.app-1777210831364.png", w: 1920, h: 1080 }   # STRAIN: STALE Lovable preview — prior "TELO" branding (cream palette, family-photo hero), NOT the current sage/vials design; do not use as a current-brand cover
brand_colors: { primary: "#556650", accent: "#4A7340", secondary: "#D4D9C4" }   # sage / forest green — confirmed vs screenshot; note the BLUE/teal logo is off-palette from the green site
fonts: [DM Sans]                     # body (branding.fonts[0]); a display serif sets the headlines ("made simple.") — unidentified, see Visual
color_scheme: light
design_framework: Lovable            # rawHtml: 3× "lovable" refs + a lovable.app og preview; Vite-hashed assets under the hood (AI app-builder output, not branding.designSystem's "custom")
---

## Overview

TeloLife is a **direct-to-consumer telehealth brand selling compounded GLP-1 weight-loss medication** (semaglutide and tirzepatide). The journey is built for speed and discretion: a customer picks a plan, optionally clears Cherry financing, fills out an online health questionnaire (~5 minutes), and a licensed clinician reviews it and — if appropriate — prescribes a compounded GLP-1 that ships from an FDA-registered pharmacy in 3–5 business days, with 24/7 messaging support thereafter. Legally, **TeloLife, Inc. is a technology platform, not a medical practice** — clinical care is delivered by "independent, licensed Provider Groups" and medication is dispensed by third-party compounding pharmacies (per its Terms). The site is brand-new (© 2026), single-category, and unusually transparent on price for the GLP-1 telehealth cohort: full cash pricing is published, not quiz-walled.

## What they offer

One offering — compounded GLP-1 weight-loss therapy — in two molecules, sold as an all-inclusive monthly cash plan or a prepaid multi-month bundle. Per-SKU detail in [`offerings.md`](offerings.md).

- **Semaglutide (compounded):** **$199/mo** all-inclusive — bundles 3-mo **$597** / 6-mo **$1,194** / 9-mo **$1,791** / 12-mo **$2,388** (12-mo flagged "Most popular"); all resolve to $199/mo `[published]`
- **Tirzepatide (compounded):** **$275/mo** all-inclusive; bundles exist (3/6/9/12-mo) but totals not in-capture `[published]`

Pricing is stated **"ALL-INCLUSIVE REGARDLESS OF DOSAGE… No consultation fees, No shipping fees, No membership fees, and absolutely No hidden charges"** (/pricing). A card/wallet purchase triggers an automatic discount; financing spreads the bundle total over Cherry terms (e.g. the 3-mo bundle is shown "As low as $26/mo… *Based on Cherry approval").

## How it works / model

Six-step flow (homepage): **(1) pick a plan → (2) finance or pay by card → (3) Cherry soft credit check ~30s, or skip straight to checkout → (4) online health questionnaire (~5 min) → (5) licensed clinician reviews & prescribes → (6) medication ships discreetly, 3–5 business days**, then ongoing 24/7 provider messaging. Intake is **asynchronous** (store-and-forward questionnaire; video/audio "where applicable"). Money model: a **monthly subscription** charged on the same day each month via Stripe (auto-renews; cancel anytime, effective end of billing period), or a prepaid multi-month bundle. No membership/consult/shipping fees — the plan price is the medication-inclusive all-in. Cash-pay, **no insurance**; HSA/FSA may be eligible; third-party financing via Cherry, plus pay-in-4 (Affirm/Klarna/Afterpay) and Apple/Google Pay.

## Positioning & audience

Targets U.S. adults (18+) seeking GLP-1 weight loss **without insurance, clinics, or waiting rooms** — "Weight loss, made simple." The claimed edge is **simplicity + transparency + financing**: a 5-minute path, all-inclusive flat pricing shown up front, and modern financing ("cost should never stand in the way of treatment"). Gender-neutral front door (the one testimonial is a woman, but there's no men's/women's hub). It competes in the crowded compounded-GLP-1 telehealth field (Hims, Henry Meds, LifeMD, Noom, et al.); its differentiators are published pricing and Cherry-led affordability rather than clinical depth or brand heritage.

## Nav structure

```
- Home — /
- How it works — /#how
- Packages — /packages          (Cash↔Financing + Semaglutide↔Tirzepatide toggles; #faq)
- Pricing — /pricing
- Financing — /financing         (Cherry pre-qual lead form)
- Questionnaire — /apply         (intake; ?plan=<key>, e.g. ?plan=sema-6mo)
- Pay by Card — /checkout
- Cherry Checkout — /commit
- Stories — /stories
- FAQ — /packages#faq
- Sign in — /auth?mode=signin
Footer ▸ Company: Contact (mailto:Support@telolife.com) · Text Message Sign-Up — /pages/text-message-sign-up · Affiliate Program — /affiliate/apply
Footer ▸ Legal: Privacy · California Privacy Notice · Terms · HIPAA Notice · Medical Disclaimer · Cancellation & Refund (all /legal/*.html)
```

## Credibility & proof

- **LegitScript Certified:** footer seal linking to LegitScript's verification — *"TeloLife is verified for safe, transparent telehealth practices"* (the one third-party health credential shown).
- **HIPAA compliant:** stated in footer and throughout; a HIPAA Notice legal page exists.
- **FDA-registered pharmacies:** *"Medication shipped in plain packaging from FDA-registered pharmacies"* — but compounded meds are explicitly *"not FDA-approved drug products"* (Terms §9).
- **Self-reported outcome stats (illustrative):** *"92% Patient satisfaction · 15–20% Avg. weight loss · 24/7 Care support"* — flagged self-reported, and the page concedes the testimonials are placeholder: *"Photos and quotes shown are for illustrative purposes. Real patient testimonials will be added as program participants share their stories."*
- **Results guarantee (not a refund):** if you follow the plan and don't see measurable progress, the care team adjusts the plan at no charge — *"does not constitute a refund guarantee"* (Terms §8).
- **No named clinicians or pharmacies:** providers are anonymous "Provider Groups"; no /physicians page, no named pharmacy partner.

## Visual & brand impression

Clean, soft, modern DTC-wellness aesthetic — a muted **sage-green** canvas (`#556650`/`#D4D9C4`) with cream rounded cards, deep **forest-green** footer/CTA blocks (`#4A7340`→darker), and a serif/sans pairing (a Tiempos/Canela-style display serif italic for accents — "*made simple.*", "*around your life.*" — over DM Sans body). Hero imagery is a pair of green-capped compounded-GLP-1 vials; a stock testimonial portrait carries the social proof. The overall feel is **template-polished but thin** — consistent spacing and tasteful type, but it reads as a fast, recently-shipped build (placeholder testimonials, no team/about page). Tell-tale: the site is **built with Lovable** (AI app builder) on Vite/React. One brand inconsistency worth noting — the **logo is blue + mint-teal** (a stacked "TELO" monogram, the O drawn as a ring), visually off-key from the all-green site palette.

## Strategic read

A **freshly-minted, lightweight GLP-1 telehealth entrant** assembled on a no-code/AI stack (Lovable), competing on **price transparency + financing** rather than clinical or brand depth. Three things stand out: (1) it **publishes full cash pricing** ($199 sema / $275 tirz, all-inclusive) where many peers quiz-wall it — a genuine positioning choice; (2) it leans hard on **Cherry financing** ("as low as $26/mo") to lower the entry barrier, the dominant CTA pattern; (3) the **thin operational surface** — anonymous Provider Groups, unnamed pharmacies, placeholder testimonials, no team page, a stale "TELO" og from a prior brand iteration — suggests a very early-stage or affiliate/drop-style operation routing intake to independent provider+pharmacy networks. Standard compounded-GLP-1 structure (tech platform → Provider Groups → 503A-style patient-specific compounding pharmacies); the wedge is purely commercial (simplicity, published price, pay-over-time), not differentiated care.

## Provenance

- **Pages:** homepage, /packages, /pricing, /financing, /legal/terms.html — 5 pages, Firecrawl (all-formats), captured 2026-06-04.
- **Verify:** all 5 sourceURLs match; all bodies md5-unique (no DUP-BODY contamination). SPA routes returned HTTP 404 with full soft-404 content (§5.6) — body trusted, confirmed against screenshots.
- **Credits:** 6 (1 map + 5 scrapes); map returned 0 URLs.
- **Couldn't get:** Tirzepatide bundle totals (/packages defaulted to the Semaglutide toggle); named Provider Groups / compounding pharmacies (generic in Terms, none named); founders/team/funding/launch date (no about page).
- **Run profile:** guided — all modules (+logos, +offerings.md, +telehealth.md cohort pack); no emphasis.
