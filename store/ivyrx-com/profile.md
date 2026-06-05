---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: ivyrx.com
name: Ivy RX
aliases: ["IVY RX", "Ivy RX PLLC"]          # meta title casing + legal entity (footer ©)
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/ivyrxhealth/
  facebook: https://www.facebook.com/people/IVY-RX/100087908052170/
  tiktok: https://www.tiktok.com/@joinivy
external:
  trustpilot: https://www.trustpilot.com/review/ivyrx.com

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow (cdn.prod.website-files.com). Commerce/online-visit on app.ivyrx.com; patient portal patient.ivyrx.com; help center support.ivyrx.com (Intercom). No JSON-LD on homepage. Full price grid lives on /treatments (category pages show only a few prices). PDPs headline a 'From $X' floor; a templated footnote on every PDP reads '$49.75/week = $199/mo (paid upfront with a 12-month plan)'. /products/glutathione-nasal-spray serves the glutathione-injection page byte-for-byte (no distinct PDP built) — dropped the dup capture. /products/glp1-oral-melts 404s though nav links it. No A/B tool fingerprinted."
key_pages:
  weight_loss: /weight-loss
  anti_aging: /anti-aging
  peptides: /peptides
  supplements: /supplements
  treatments: /treatments
  about: /about-us
  how_it_works: /how-it-works            # redirects to support.ivyrx.com Intercom article
  product_example: /products/personalized-glp-1-injections
unverified_fields:
  - "Founding date / founder — not stated on the site."
  - "Prescribing providers + partner pharmacy unnamed (only an advisory board is named)."
  - "Self-reported review count is inconsistent: '5000+ reviews' (header) vs '4000+ reviews' (footer)."
  - "Ozempic®/Mounjaro® show a $1,399 price but require an online medical visit to obtain."

description: "A DTC telehealth brand selling compounded GLP-1, NAD+, sermorelin, peptides and other 'longevity' medications, prescribed by licensed physicians via an online questionnaire and shipped from partner compounding pharmacies."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 39, h: 24 }                                                                                            # lowercase "ivy" mark, extracted from the inline nav <svg>
  logomark: { src: "https://cdn.prod.website-files.com/6740c7cb57461a7d58397b6e/697bcec7e3903f981b4726a7_webclip.svg", px: 256, transparent: false }  # gradient app icon; baked pink→violet background
brand_colors: { primary: "#3898EC", accent: "#1FC16B" }   # STRAIN: branding payload; #3898EC is Webflow's default link-blue, NOT the brand — true identity is a pink→violet gradient + green (#1FC16B). See Visual.
fonts: [Manrope, DM Sans]                                  # Manrope body, DM Sans heading
color_scheme: light
design_framework: webflow                                  # website-files.com CDN (rawHtml), not the branding payload
---

## Overview

Ivy RX (legal: Ivy RX PLLC, Miami, FL) is a direct-to-consumer telehealth brand that frames itself as "longevity medication, personalized to you." It connects patients to US-licensed physicians through a 100%-online questionnaire, then — if approved — ships prescription medications compounded at partner pharmacies (503B / USP <797>) discreetly to the door. The catalog spans two pillars: **weight loss** (compounded GLP-1 with tirzepatide or semaglutide, microdosing, lipotropics) and **anti-aging / longevity** (NAD+, sermorelin, glutathione, B12, peptides), plus a small line of oral supplements. No insurance is required; care is cash-pay, HSA/FSA-eligible.

## What they offer

Two Rx pillars plus a non-Rx supplement line; prices shown are per-month floors that assume a plan (often a 12-month upfront commitment), so the all-in moves with dose and plan length. Per-SKU detail in `offerings.md`.

- **Weight loss — compounded GLP-1:** tirzepatide / semaglutide injections — **"From $197 $175 (4 doses/month)"**; a microdose option **$155**; lipotropic **MIC + B12 $179** and **anti-nausea (ondansetron) $19.99** as companions `[partial]`
- **Weight loss — branded GLP-1:** **Ozempic® $1,399**, **Mounjaro® $1,399** — listed as premium FDA-brand alternatives, obtained via online visit `[partial]`
- **Anti-aging / longevity (injectable Rx):** **NAD+ injection $199**, **NAD+ nasal spray "From $179"**, **glutathione injection "From $179"**, **B12 injection $179**, **sermorelin $175** `[partial]`
- **Metformin:** off-label for weight-loss / anti-aging — **$90** `[partial]`
- **Supplements (oral, non-Rx):** **GLP-1 Boost $72**, **Gut Peptide Complex $89**, **BPC-157 $129**, **Methylene Blue $89** `[published]`
- **GLP-1 Oral Melts:** listed in the weight-loss nav but the PDP 404s — no live price `[on-request]`

## How it works / model

A three-step async telemedicine flow: **(1)** a ~5-minute online questionnaire about health and goals; **(2)** a US-licensed physician reviews the same day and, if appropriate, prescribes; **(3)** medication ships from an FDA-registered / partner compounding pharmacy, typically in 3–5 business days, free and discreet. Patients message providers anytime through the patient portal (`patient.ivyrx.com`); the checkout/online-visit funnel runs on `app.ivyrx.com`. Revenue is subscription/plan-based (monthly, with cheaper per-month rates on multi-month upfront plans); no insurance, HSA/FSA accepted, itemized receipts for reimbursement.

## Positioning & audience

Targets health-conscious US adults (both genders — testimonials and heroes are mixed) who want GLP-1 weight loss and/or "longevity" wellness without insurance friction. It sits in the crowded compounded-GLP-1 telehealth field (Hims, Ro, and many longevity-focused peers), differentiating on a **longevity umbrella** (weight loss as the front door, anti-aging/peptides as the broader promise), claimed personalization, quality-tested compounding, transparent cash pricing, and convenience. Brand-name Ozempic/Mounjaro at $1,399 anchor the compounded $175 as the value option.

## Nav structure

```
- Weight loss — /weight-loss
  - GLP-1 Injections — /products/personalized-glp-1-injections
  - GLP-1 Microdose — /products/microdose-glp-1-injections
  - GLP-1 Oral Melts — /products/glp1-oral-melts   (PDP 404s)
  - MIC + B12 Injection — /products/lipotropic-mic-b12-injection
  - Anti-Nausea Tablets — /products/anti-nausea-tablets
  - GLP-1 Boost — /products/glp-1-boost
  - Ozempic® — /products/ozempic
  - Mounjaro® — /products/mounjaro
  - Metformin — /products/metformin
- Anti-aging — /anti-aging
  - NAD+ Injection — /products/nad-injection
  - NAD+ Nasal Spray — /products/nad-nasal-spray
  - Glutathione Injection — /products/glutathione-injection
  - Glutathione Nasal Spray — /products/glutathione-nasal-spray   (serves the injection PDP)
  - B12 Injection — /products/vitamin-b12-injection
  - Sermorelin — /products/sermorelin-injection
  - Metformin — /products/metformin
- Peptides — /peptides
  - Sermorelin — /products/sermorelin-injection-old
  - BPC 157 — /products/bpc-157
- Supplements — /supplements
  - BPC 157 — /products/bpc-157
  - GLP-1 Boost — /products/glp-1-boost
  - Gut Peptide Complex — /products/gut-peptide-complex
  - Methylene Blue — /products/methylene-blue
- Meet Ivy Rx
  - About us — /about-us
  - How it works — /how-it-works
  - Reviews — /reviews
  - Journal (blog) — /blog
  - Help center — support.ivyrx.com
  - Contact us — /contact
- Login — patient.ivyrx.com
Footer also: Ambassador program — /ambassador-program · BMI Calculator — /resources/bmi-calculator · TDEE Calculator — /resources/tdee-calculator
```

## Credibility & proof

Trust signals are heavy and largely self-reported — recorded, not endorsed:

- **Patient count:** "200,000+ patients" / "200,000+ members thriving and age defying" (self-reported)
- **Reviews:** Trustpilot **4.5**, with "**5000+ reviews**" (header) and "**4000+ reviews**" (footer) — counts disagree across the page
- **LegitScript-certified:** seal in the site footer
- **Medical advisory board (named):** Silvia Mosher, MD (board-certified hematologist, 25+ yrs; founder, Onco Solution & Medical Monitoring Solutions); Rocio Reategui, MD (board-certified oncologist, Medical Director at MMS); Katy Ordoñez, MD (pediatric oncologist) — note the board skews oncology/hematology, while the homepage FAQ claims expertise across "psychology, oncology, men's health, sexual health, neurology, and family medicine"
- **Quality testing (claimed):** potency (±10%), sterility (USP 797), endotoxicity (USP 85), and pH testing; "prepared in a state-licensed pharmacy, independently verified in FDA- and DEA-registered labs"
- **Compounding standard:** "compounded in pharmacies compliant with 503B / USP <797> standards"
- **Compliance / social impact:** HIPAA-compliant consults; "a part of each purchase supports not-for-profits focused on enhancing health care access for underserved communities"
- **FDA disclaimer (verbatim):** "The FDA does not review compounded medications for safety or effectiveness… If approved, prescriptions can be filled at a partner pharmacy."

## Visual & brand impression

Modern, polished DTC-health aesthetic on a light background. The brand mark is a lowercase **"ivy"** wordmark (bold custom serif-ish face, rendered black); the app icon places that wordmark in white on a **pink→violet gradient** rounded square. Section backgrounds lean on soft **violet and green** pastel gradients with product vials/bottles composited on them — a calm, premium "wellness" feel rather than clinical. Type is Manrope (body) / DM Sans (headings). The page is conversion-engineered: announcement banner, mega-nav flyouts, a rotating priced "treatments" carousel, repeated "Order Now" / "Find my treatment" CTAs, big social-proof numbers, video testimonials, BMI/TDEE calculators. (The `branding` payload's `primary #3898EC` is Webflow's default link-blue, not the real palette — the brand's signature is the violet/pink gradient + green `#1FC16B` accent.)

## Strategic read

- **GLP-1 boom, longevity wrapper.** Compounded tirzepatide/semaglutide is the commercial engine, but the brand deliberately positions under a broader "longevity / age-defying" tent (NAD+, sermorelin, peptides) to extend beyond a single weight-loss molecule's regulatory and competitive risk.
- **Massive SEO content farm.** ~250+ blog/journal posts targeting comparison and how-to queries (semaglutide vs tirzepatide, NAD dosing, competitor "reviews") — organic acquisition is clearly a core channel.
- **Compounding-forward, partner-pharmacy model.** It routes to external state-licensed compounding pharmacies (no owned pharmacy claimed), so its moat is brand/marketing + provider network, not vertical pharmacy integration.
- **Site QA gaps.** A nav-listed product PDP 404s (GLP-1 Oral Melts) and the glutathione-nasal-spray URL serves the injection page — signs of a fast-moving catalog where the storefront outruns the page build.

## Provenance

- **Pages:** 14 analyzed via Firecrawl (homepage; /weight-loss, /anti-aging, /peptides, /supplements, /treatments; /about-us; /how-it-works; PDPs: personalized-glp-1-injections, glp1-oral-melts [404], nad-nasal-spray, glutathione-injection, methylene-blue, ozempic, mounjaro). `map` returned 285 URLs; `signals` (no JSON-LD found) and `logos` run on the homepage payload.
- **Verify:** sourceURL matched on every page; md5-unique after dropping `pdp-glutathione-nasal-spray` (byte-identical to glutathione-injection — confirmed deterministic over two scrapes; the site serves the injection page at that URL, not §5.1 contamination).
- **Credits:** ~17 (1 map + 16 scrapes, including a confirming re-scrape of glutathione-nasal-spray).
- **Couldn't get:** founding date/founder; named prescribing providers; named partner pharmacy; reconciliation of the 5000+/4000+ review counts.
- **Run profile:** guided — +telehealth pack, +offerings roster, +logos; no emphasis given.
