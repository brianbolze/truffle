---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: home.medvi.org
name: MEDVi
aliases: [medvi.org]                  # apex + www 302-redirect to home.medvi.org (the Framer-published canonical host)
parent: []
owns: []
socials: {}                          # none surfaced — no JSON-LD sameAs, no footer/header social anchors
external: {}                         # no crunchbase/wikipedia/etc. surfaced (LegitScript cert → Credibility, not a record-about-entity)

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Framer-hosted (server: Framer/*); 'home.' IS the canonical host — apex medvi.org + www 302 → home.medvi.org. Live product lines live on separate Framer subdomains the subdomains-off map drops, each its own funnel/brand: glp1.medvi.org (Weight Loss / compounded GLP-1 — SKUs + prices live here), quad.medvi.org (Men's Health 'QUAD'), meals.medvi.org (MEDVi Meals — a white-label meal-delivery storefront on mfg-whitelabel-prod S3, separate platform). Homepage carries NO prices (pricing is on the funnel subdomains). No JSON-LD; nav is a bare-div Framer 'marek' (rebuild Nav from screenshot). Map = 11 URLs, mostly legal pages + /about-us + a /weightloss/ LP variant. 'Coming Soon' verticals (Women's, Supplements, Peptides, Hair, Skincare) are roadmap, not buyable. Clinical delivery outsourced: OpenLoop Health provider network + CareGLP Affiliated P.C.s + 3rd-party compounding pharmacies (Triad Rx, RedRock, Beaker). Men's-health funnel uses a different contact (hello@medvi.org / (585) 312-4226) than home (help@medvi.org / (323) 690-1564)."
key_pages:
  about: /about-us
  weight_loss_glp1: https://glp1.medvi.org/
  mens_health_quad: https://quad.medvi.org/
  meals: https://meals.medvi.org/
unverified_fields:
  - "Branded-GLP-1 SKU pricing (Wegovy® Pill/Injection, Zepbound® Injection) — shown only as '$99 Membership + Medication Cost'; the medication cost is gated behind the intake quiz."
  - "'Coming Soon' lines (Women's Health, Supplements, Peptides & Longevity, Hair, Skincare) — announced, no products/pricing yet."
  - "The 'Proud to be featured and advertised in' press-logo wall (glp1 page) — logos not individually identifiable from the markdown; copy says 'advertised in' (paid placement), so not earned press."
  - "Prices/promos are a point-in-time snapshot, not fixed — glp1 ran a 'SUMMER Sale! Only $179' and meals ran a countdown + 'MEDVI20' 20%-off; re-check next run."

description: "A direct-to-consumer telehealth brand delivering online medical care through US-licensed providers, anchored on compounded GLP-1 weight loss and extending into men's sexual health, prepared meals, and a roadmap of other prescription wellness lines."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth
logo_url: https://framerusercontent.com/images/1BRDkIzVV7TxG8fJDyUWdUDDE.png   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: "https://framerusercontent.com/images/1BRDkIzVV7TxG8fJDyUWdUDDE.png", w: 500, h: 105 }                  # the dark "MEDVi" mark+name from the site header
  logomark: { src: "https://framerusercontent.com/images/xWKyg85eDVm8FJeXNodQY3RoGpE.png", px: 500, transparent: false }  # "M" monogram; baked WHITE square (hasAlpha:no, confirmed on a dark tile)
  og:       { src: "https://framerusercontent.com/assets/u2Ljgu8m4C9DCVQ3T4mC1WOGNc.png", w: 1200, h: 630 }               # branded cover: white "MEDVi" on sage + lifestyle photo
brand_colors: { primary: "#779D7C", accent: "#2E936F", text: "#242220" }  # STRAIN: branding payload's primary #0000EE is unstyled-link blue (noise); true palette = sage/forest green + charcoal text, confirmed on screenshot/og
fonts: [Onest, Red Hat Text]         # Onest = heading, Red Hat Text = body (branding payload)
color_scheme: light
design_framework: framer             # rawHtml: 918 data-framer / 6894 framer markers (payload designSystem said "custom" — ignored per §5.4)
---

## Overview

MEDVi is a DTC telehealth company that sells online medical care — "Healthcare, redefined for real life" — to US consumers, with **compounded GLP-1 weight loss as its wedge and dominant line**. A patient completes an online assessment, an independent US-licensed provider (via partner **OpenLoop Health** / **CareGLP Affiliated P.C.s**) reviews eligibility, and if appropriate a prescription is filled by a partner compounding pharmacy and shipped to the door, bundled with 1:1 physician guidance, dietitian visits, care coaching, and 24/7 support. Founded under two years ago by **Matthew Gallagher (Founder/CEO)**, it claims **500,000+ patients** and **1,000+ medical providers** (self-reported). It is broadening from the single weight-loss funnel into a multi-vertical platform: a live men's sexual-health product (**QUAD**), a meal-delivery line (**MEDVi Meals**), and announced-but-not-yet-live women's health, peptides, supplements, hair, and skincare lines.

## What they offer

Live lines route to separate Framer funnel subdomains; "Coming Soon" lines are roadmap. Prices verbatim with a visibility token:

- **Weight Loss — compounded GLP-1 (flagship):** the program "**Start for just $179**" first month (semaglutide), refills "**locked in at $299**"; "GLP-1 Injections" **Starting at $179** (weekly) and "GLP-1 Tablets" **Starting at $249** (daily). No membership; "No membership or hidden fees," HSA/FSA-eligible, cash-pay. → `glp1.medvi.org` `[published]`
- **Weight Loss — branded GLP-1:** "Wegovy® Pill," "Wegovy® Injection," "Zepbound® Injection," each "**$99 Membership + Medication Cost**" ("Availability is subject to change"); medication cost gated behind intake. `[partial]`
- **Men's Health — QUAD™:** a sublingual 4-in-1 ED/performance formula (apomorphine + vardenafil + sildenafil + tadalafil), "MEDVi QUAD™ Prescription" **$114** /month (struck **$179**, "36% Off Retail"), doctor consult + free rush shipping included. → `quad.medvi.org` `[published]`
- **MEDVi Meals:** chef-prepared, macro-friendly meal delivery (75+ weekly / 300+ rotating meals); Classic & Premium programs at 6/10/15/20 meals/week — Classic 10-meal box "**$124.88 $99.90**" (≈**$9.99**/serving, after "MEDVI20" 20% off). → `meals.medvi.org` `[published]`
- **Coming Soon (roadmap, not buyable):** Women's Health, Peptides & Longevity, Supplements, Hair restoration, Skincare — announced on the homepage, no products or pricing yet. `[on-request]`

Per-SKU roster (molecule · form · price) → `offerings.md`.

## How it works / model

1. **Online assessment / intake quiz** (no doctor-patient relationship created by the assessment itself) — answers screen eligibility (OpenLoop exclusionary criteria).
2. **Provider review** — an independent US-licensed clinician (OpenLoop Health) meets with the patient after checkout and retains the decision to prescribe; men's health promises doctor review "within 24 hours."
3. **Compounded medication dispensed** by a state-licensed partner pharmacy (Triad Rx · RedRock · Beaker) and **shipped to the door** (free, discreet).
4. **Ongoing program** — "Medication is included in the cost of the MEDVi Program"; bundled 1:1 physician guidance, free dietitian visits, care coaching, and 24/7 unlimited support. Cash-pay, no insurance required, HSA/FSA-eligible.

Money: recurring **subscription/program** — weight loss $179 first month → $299 refills; QUAD $114/mo; Meals a weekly meal subscription. Compounded GLP-1s are not FDA-approved; branded products (Wegovy®, Zepbound®, Ozempic®) referenced for comparison only.

## Positioning & audience

Targets US consumers who want accessible, affordable online care without "waiting rooms" — primarily weight-loss seekers, plus men's sexual health, on a broadening wellness platform. The pitch is **convenience + transparent, budget-friendly pricing** ("Clear pricing," "No hidden fees," "no insurance required") wrapped in bundled clinical support (provider + dietitian + coaching). It sits squarely in the compounded-GLP-1 telehealth field against Hims & Hers, Ro, Henry Meds, Remedy Meds, and similar DTC men's/weight brands; QUAD's aggressive "4 meds in 1 dose" framing positions the men's line against single-molecule ED telehealth.

## Nav structure

Single-scroll Framer marketing page (no header `<nav>`); top-of-page category cards link to on-page anchors, "Get Started" CTAs route to the live funnel subdomains.

```
- Weight Loss — /#weight-loss  → glp1.medvi.org (LIVE)
- Peptides & Longevity — /#peptides  (Coming Soon)
- Men's Health — /#mens-health  → quad.medvi.org (LIVE)
- Women's Health — /#womens-health  (Coming Soon)
- (homepage sections, top→bottom): Weight Loss · Women's Health · MEDVi Meals (meals.medvi.org, LIVE) ·
  Supplements (Coming Soon) · Men's Health · Peptides & Longevity (Coming Soon) · Hair (Coming Soon) ·
  Skincare (Coming Soon) · Care coaching & nutrition · Testimonials
- About Us — /about-us
- Footer: Terms & Conditions · Privacy Policy · Privacy Practices · Refund Policy · Medical Consent ·
  For California Residents · Bill of Rights · LegitScript verification
```

## Credibility & proof

All figures are **self-reported** unless noted; recorded verbatim, not endorsed.
- **Scale claims:** "Join **500,000+** MEDVi patients" (home); "**1,000+** Medical Providers," "**500,000+** Patients Served," "**<2** Years Since Founding" (about); "**10,000+** Patients Agree" (glp1); "Verified Results from **50,000+** Men" (quad).
- **Outcome claims (weight loss, MEDVi patient self-report):** "6x more weight loss than exercise and diet alone," "Lose an average of **18%** of your body weight," "**93%** kept the weight off," "patients in the MEDVi program lose **15-20%** of their body weight."
- **Third-party rating (self-displayed):** "TrustPilot — **Excellent 4.5 out of 5**" (quad page; not verified against Trustpilot).
- **Certifications / partners:** **LegitScript**-verified (links to legitscript.com check for medvi.org); clinical care by **OpenLoop Health** + **CareGLP Affiliated P.C.s**; partner pharmacies **Triad Rx, RedRock Pharmacy, Beaker Pharmacy & Compounding** (named with addresses/phones).
- **Guarantee:** "MEDVi Guarantee" (money-back framing); free expedited shipping; "No hidden fees."
- **Press wall:** glp1 page shows a "Proud to be featured and **advertised** in" logo strip (paid placement; logos not individually identified).
- **Testimonials:** heavy first-name patient testimonials site-wide (privacy note: images may use models; some content AI-generated/enhanced).

## Visual & brand impression

Clean, warm, modern wellness aesthetic — sage/forest green + cream against dark charcoal-brown text (`#242220`), rounded cards, generous whitespace, and aspirational lifestyle photography of diverse patients. Reads "premium-accessible lifestyle brand" more than "clinic" — soft and approachable, dense with testimonial social proof. The QUAD men's sub-brand deliberately flips register: darker, high-contrast, masculine (a black labeled bottle, bold "Speed. Strength. Stamina." copy). Design execution is polished and consistent for a Framer build.

## Strategic read

A textbook compounded-GLP-1 telehealth playbook — weight loss as the acquisition wedge (500k patients in <2 years on self-report) — now levering that base into a **multi-vertical wellness platform** (men's ED, meals, and a five-line roadmap). MEDVi is the **brand / marketing / UX layer**: the medical group (OpenLoop / CareGLP P.C.s) and the compounding pharmacies are third parties, so the moat is acquisition + experience, not clinical or pharmacy assets. That structure plus the compounded-GLP-1 reliance (explicitly *not* FDA-approved) carries the regulatory exposure the whole compounded-semaglutide cohort shares. Two things stand out vs. peers: aggressive promo pricing (a $179 summer sale, a published $299 refill anchor that undercuts membership-stacked rivals) and the unusually bold QUAD men's product (four PDE5/dopamine actives in one sublingual dose) — a differentiated, claim-forward bet in a crowded ED-telehealth space.

## Provenance

- **Pages:** homepage, /about-us, glp1.medvi.org (weight loss), quad.medvi.org (men's health/QUAD), meals.medvi.org (MEDVi Meals) — 5 pages, Firecrawl all-formats; map (11 URLs). Screenshots used for visual read + nav reconstruction + logo/transparency judgement.
- **Verify:** all sourceURLs matched; all body md5s unique (no geo/cache contamination).
- **Credits:** 6 (1 map + 5 scrapes); hero/logo asset fetches were headed (no credits).
- **Couldn't get:** branded-GLP-1 medication cost (intake-gated); "Coming Soon" line detail (pre-launch); individual press-wall logo IDs.
- **Run profile:** guided — no emphasis; +offerings.md (per-SKU roster) with flagship hero product images; +logos:{} module.
- **Enriched (model knowledge):** none — founder/founding-window facts are from the captured /about-us page, not a prior.
