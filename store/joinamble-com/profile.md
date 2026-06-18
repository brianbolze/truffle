---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: joinamble.com
name: Amble
aliases: []
legal_entity: "Amble Health, Inc."   # 2.6 — site-derivable: footer "©2026 Amble Health, Inc." + ad/safety disclaimers
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/joinamble/
  tiktok: https://www.tiktok.com/@joinamble
  facebook: https://www.facebook.com/JoinAmbleHealth/
external:
  trustpilot: https://www.trustpilot.com/review/joinamble.com

# Capture meta
captured_at: 2026-06-18
capture_method: firecrawl
site_notes: "Webflow (data-wf-/website-files.com; designSystem payload says 'unknown' — ignore). No JSON-LD. No /about or /pricing page — products + faq + amble-cares + footer disclaimers carry positioning. Per-product pricing lives in a plan-length table on each subscription PDP (12-mo cheapest → 1-mo dearest; homepage 'From $X' = the 1-mo rate). NEW since 6/04: a /medkits/ line of one-time prescription emergency/preparedness kits ($285–$945, 'one time purchase paid upfront') — built on a SEPARATE Webflow CDN project (691513c1de5d326f0f8e5ba1) vs the core site's 67fec0a64d109843c12f501a, i.e. a distinct section. Funnel on intake./enroll.joinamble.com + a Typeform for Amble Cares eligibility; customer portal on my.joinamble.com. Nav recoverable from <nav>. /tesamorelin-injection is nav-linked (top strip + Anti-aging dropdown) but its PDP 404s (re-confirmed 6/18) — the only nav product with a dead page. Product images are AVIF/WEBP on the Webflow CDN (browser UA + sips to fetch/convert). branding.images.logo IS the inline 'amble' wordmark SVG (viewBox 88×28, unchanged from 6/04). og:image CHANGED this run: was a dark vials cover, now a clean warm-orange radial-sunburst with the white 'amble' wordmark. A/B: yes — rotating hero (Anti-aging ⇄ Weight loss; showed Anti-aging first this run) and inconsistent self-reported stats run-to-run (100,000+ vs 250,000+ members/patients; Trustpilot 4.5 vs 4.6) — point-in-time."
key_pages:
  weight_loss_glp1: /glp-1-injections
  nad: /nad-injections
  sermorelin: /sermorelin-injections
  glutathione: /glutathione
  lipo_b: /lipo-b
  lipo_c: /lipo-c
  skin: /skin
  faq: /faq
  amble_cares: /amble-cares-program
  medkit_just_in_case: /medkits/just-in-case-kit
  medkit_mayday: /medkits/mayday-kit
  medkit_breathe_easy: /medkits/breathe-easy-kit
  medkit_cold_reaper: /medkits/cold-reaper-kit
  medkit_viral_ick: /medkits/viral-ick-kit
  medkit_oh_sht: /medkits/oh-sht-kit
  medkit_ouch_pouch: /medkits/ouch-pouch-kit
  medkit_panic_pack: /medkits/panic-pack-kit
  tesamorelin_dead: /tesamorelin-injection   # nav-linked, PDP 404s (re-confirmed 6/18)
unverified_fields:
  - "Founding date, team, headcount, ownership — no /about page on site; deep-research job, not capture. (Amble Cares press footprint dates to ~May 2026.)"
  - "Tesamorelin: nav-linked (top strip + Anti-aging dropdown) but /tesamorelin-injection returns HTTP 404 'Page Not Found' (re-confirmed 6/18) — depublished, no live PDP/price. Not a live SKU."
  - "Self-reported scale/ratings/efficacy are A/B-volatile and not independently verified: this run shows '100,000+ members' (marquee) alongside a '100,000+ / 250,000+ patients' split and Trustpilot '4.5'/'4.6' on the same homepage; weight-loss efficacy figures ('33 lbs lost on average') are point-in-time."
  - "Medkit contents/counts captured per PDP, but exact per-kit medication rosters beyond those listed are not exhaustively transcribed for all 8 kits (full lists pulled for Just in Case + Panic Pack; others sampled)."

description: "A DTC telehealth brand selling compounded GLP-1 weight-loss and anti-aging injectables plus prescription skincare on monthly plans, and — newer — one-time prescription emergency/preparedness medication kits, all 100% online with licensed-physician review and fulfillment through a partner pharmacy network."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription   # dominant model (therapeutic core); the /medkits line is Transactional / One-time — see body
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # canonical wordmark — inline "amble" SVG from branding.images.logo (viewBox 88×28, unchanged 6/04→6/18)
logos:
  wordmark: { src: assets/wordmark.svg, w: 88, h: 28 }                                                                # rectangle — lowercase "amble" serif logotype, single dark charcoal color; committed text SVG
  logomark: { src: "https://www.google.com/s2/favicons?domain=joinamble.com&sz=256", px: 256, transparent: false }    # square black "a" mark on a BAKED white square (apple-touch-icon identical) — shows as a white chip on a dark slide
  og:       { src: "https://cdn.prod.website-files.com/67fec0a64d109843c12f501a/6a26f66222df058de5a3e0a2_amble_og.webp", w: 1200, h: 630 }  # CHANGED 6/18: warm-orange radial-sunburst cover, centered white "amble" wordmark (was dark vials cover)
brand_colors: { primary: "#F18F20", accent: "#8078AD" }  # warm orange (weight loss) + purple (anti-aging), confirmed in hero panels + vial renders + new og; branding's #3898EC is Webflow's default blue (chrome)
fonts: [Geist, Manrope]              # Geist body, Manrope headings (generic "sans-serif" ranked first — excluded)
color_scheme: light
design_framework: webflow
---

## Overview

Amble (Amble Health, Inc.) is a direct-to-consumer telehealth platform selling prescription weight-loss, anti-aging, skincare, and — as of mid-2026 — **emergency/preparedness medication kits**, delivered entirely online. A free online intake routes the patient to a state-licensed physician (video/phone consult "where required by state law") who, if appropriate, prescribes medication that ships free to the door, with ongoing provider messaging. The site is explicit that Amble is a **managed-services provider** — it supplies the technology and administrative coordination but does **not** offer medical advice, fill prescriptions, or operate as a pharmacy; medications (compounded and FDA-approved) are filled through an affiliated **503A/503B** pharmacy network.

The notable shift since the 2026-06-04 capture is a second business line bolted onto the subscription-injectables core: a catalog of **one-time prescription "just-in-case" kits** (antibiotics, antivirals, anti-parasitics, epinephrine, radiation prophylaxis, trauma supplies) in the Jase Medical / Duration Health mold — a different buyer, a different purchase model, and a different CDN section of the same site.

## What they offer

Two distinct lines now, on two purchase models. **Per-SKU grain (molecule · form · dose · price · kit contents) is in [`offerings.md`](offerings.md), captured this run.**

**Line 1 — Subscription injectables + skincare** (recurring monthly; per-month price falls with plan length, 12-mo cheapest → 1-mo dearest; each PDP also claims "same price, every dose"). Prices held **identical to the 6/04 capture**:

- **Weight loss — GLP-1 injection:** Compounded **semaglutide** & **tirzepatide**, self-administered subcutaneous, once weekly. **12-mo $135 · 6-mo $145 · 3-mo $160 · 1-mo $179** /mo (homepage "From $179") `[published]`
- **NAD+ injection:** Anti-aging — "Boost energy, sharpen focus." **12-mo $125 · 6-mo $167 · 3-mo $183 · 1-mo $199** /mo `[published]`
- **Sermorelin injection:** Anti-aging GHRH peptide. **6-mo $135 · 3-mo $149 · 1-mo $159** /mo (no 12-mo tier) `[published]`
- **Glutathione injection:** Antioxidant tripeptide. **12-mo $75 · 6-mo $83 · 3-mo $92 · 1-mo $100** /mo `[published]`
- **Lipo-B (MIC+B12) injection:** **12-mo $120 · 6-mo $125 · 3-mo $133 · 1-mo $149** /mo `[published]`
- **Lipo-C injection:** **12-mo $120 · 6-mo $125 · 3-mo $133 · 1-mo $149** /mo (priced identically to Lipo-B) `[published]`
- **Skin — prescription skincare:** Personalized compounded formulas (tretinoin, clindamycin, azelaic acid, niacinamide, GHK-Cu, hydroquinone, tranexamic acid, etc.). **Starting at $55** /mo `[published]`
- **Tesamorelin injection:** Listed in nav (top strip + Anti-aging dropdown) but **the PDP `/tesamorelin-injection` 404s** (re-confirmed 6/18) — depublished, no live price. Not a live SKU. `[on-request]`

**Line 2 — Medkits (NEW; one-time upfront purchase, not a subscription).** Eight prescription emergency/preparedness kits, "Total price represents a one time purchase paid upfront," each a curated set of named generic Rx drugs (+ some OTC and supplies). All require the same physician-review flow:

- **Just in Case Kit — $285** — "first line of defense," 9 Rx (antibiotics, antivirals, anti-parasitics, antifungals, anti-nausea) `[published]`
- **Mayday (Travel Emergency Kit) — $325** — 10 meds for travel infections, nausea, traveler's stomach, altitude, cough `[published]`
- **Breathe Easy (Mold & Allergy Kit) — $325** — Rx for inflammation, asthma, nasal/airway, allergy, infections `[published]`
- **Cold Reaper (Cold & Immunity Kit) — $325** — 8 Rx for respiratory infections, inflammation, nausea, fever `[published]`
- **Viral Ick Kit — $325** — 7 Rx antivirals/anti-inflammatories/immune meds + a nebulizer `[published]`
- **Oh Sht (Radiation Emergency Kit) — $345** — radiological-exposure prep incl. potassium iodide `[published]`
- **Ouch Pouch (first-aid kit) — $425** — Rx + OTC: topical antibiotics, painkillers, antihistamines, motion-sickness patch, **epinephrine auto-injector**, Rx antibiotics `[published]`
- **Panic Pack (Field Emergency Kit) — $945** — the comprehensive tier: antibiotics, antivirals, antiparasitics, painkillers, epinephrine, respiratory, GI rescue, radiation prep, wound/trauma supplies `[published]`

Named generics seen across kits: amoxicillin-clavulanate, azithromycin, doxycycline, metronidazole, TMP-SMX (Bactrim), cephalexin, mupirocin, hydroxychloroquine, **ivermectin**, valacyclovir, potassium iodide.

Weight loss remains the foregrounded therapeutic line (the referral program counts only Weight Loss sign-ups; Amble Cares is weight-loss-only). The catalog itself is entirely **compounded** on the therapeutic side; the medkit drugs are named generics filled through the pharmacy network.

## How it works / model

- **Journey:** Free online quiz/intake → state-licensed **physician** reviews and (where state law requires) conducts a live video/phone consult → tailored recommendation in the patient's Amble portal → if prescribed, medication ships in discreet packaging, free → unlimited ongoing provider messaging + 24/7 support.
- **Make-up:** Amble is the tech/admin layer; **licensed physicians** (claimed in all 50 states) prescribe; an affiliated **503A (state-licensed) / 503B (FDA-registered)** pharmacy network fills, including **compounded** (not FDA-approved) and FDA-approved meds. No owned pharmacy, no named partner.
- **Money:** Two models now — **subscription / plan-length** pricing for injectables + skincare ("transparent, all-inclusive," no insurance), and **one-time upfront** purchase for medkits. **HSA/FSA cards accepted for 3-month-or-longer plans** (itemized receipts). BNPL via **Affirm, Klarna, Afterpay**. Referral (GrowSurf): **"Give $50, Get $50"** in account credit on a referred friend's first eligible (weight-loss) order; FL residents excluded.
- **Reach:** Available in all 50 states ("exclusions apply").

## Positioning & audience

B2C consumers across two now-distinct jobs: (1) low-friction online prescription care for **weight loss / anti-aging / skin**, and (2) **emergency preparedness** ("help isn't always close, pharmacies don't always stay open") for the prepper / traveler / just-in-case buyer. Stated promise on the core line: *"Science backed care, tailored to your goals,"* *"100% online,"* "no hidden fees," "no in-person visit." Not gender-targeted — diverse lifestyle imagery, no men's/women's split.

The **Amble Cares Program** (now fully built out vs the 6/04 announce) adds an access/equity angle: *"Closing the Wealth Gap in GLP-1 Access,"* **"up to 50% lower cost"** on GLP-1 for patients whose financial need is verified by an **independent third-party partner** (apply via a Typeform). Direct-pay only — program pricing can't be combined with insurance or FSA/HSA.

## Nav structure

```
- Weight loss — /glp-1-injections
- Anti aging (dropdown)
  - NAD+ injection — /nad-injections              (Boost energy, sharpen focus)
  - Sermorelin injection — /sermorelin-injections (Produce more growth hormone)
  - Tesamorelin injection — /tesamorelin-injection (Naturally boost growth hormone) — ⚠ links to a 404
  - Glutathione injection — /glutathione          (Feel energized, support immune system)
  - Lipo-B (MIC+B12) injection — /lipo-b           (Blend of lipotropic nutrients and B12)
  - Lipo-C injection — /lipo-c                     (Lipotropic nutrients, vitamin C, and B)
- Skin — /skin
- Medkits (homepage-featured line) — /medkits/{just-in-case,mayday,breathe-easy,cold-reaper,viral-ick,oh-sht,ouch-pouch,panic-pack}-kit
- More (resources / calculators) — BMI / TDEE / calorie-deficit / protein / water-intake calculators
- Login — my.joinamble.com/login
```

## Credibility & proof

All self-reported (record, don't endorse); several figures are **volatile run-to-run** (A/B-tested site):

- **Scale (self-reported):** "100,000+ members" (marquee, this run) appears on the *same* homepage as a "100,000+ / 250,000+ patients" split — treat as point-in-time, not a fixed number.
- **Trustpilot:** on-site badges show both **"4.5"** and **"4.6"** linking to trustpilot.com/review/joinamble.com (self-reported display; not independently verified here).
- **Efficacy (self-reported):** "33 lbs lost on average," "Drop a clothing size," "Reduce your cravings." Before/after transformation testimonials with named customer IG/TikTok handles.
- **Trust framing:** "FDA regulated pharmacies," "Licensed physicians" in all 50 states, "503A/503B pharmacies," "Free expedited delivery," "Unlimited 24/7 support." Footer: "©2026 Amble Health, Inc."
- **No LegitScript seal** found in the footer; providers described as "physicians… licensed in all 50 states" but **no named-clinician page**.
- Extensive on-page Important Safety Information for semaglutide/tirzepatide and compounded-drug disclaimers; medkit PDPs carry the same managed-services + compounded disclaimers.

## Visual & brand impression

Clean, modern wellness-DTC aesthetic on white: full-width gradient hero panels in warm **orange** (weight loss) and **purple** (anti-aging), rounded product cards, generous whitespace, friendly diverse lifestyle photography (real smiling customers, not stock-clinical). Therapeutic product renders are premium 3-D vials (amber GLP-1, purple anti-aging) with clean "Rx Only" labels; medkit imagery shifts to flat-lay kit photography and individual pill/tube product shots. Lowercase **"amble"** serif wordmark, Geist/Manrope type, single dark pill CTA ("Find your treatment" / "Get started"). The refreshed og image — a minimalist warm-orange radial sunburst behind the white wordmark, replacing the older product-vials cover — reads as a move toward a cleaner, more brand-forward identity. Overall: professional and approachable, premium-but-accessible rather than clinical or luxury.

## Strategic read

A young, fast-moving brand (2026 footprint, no /about, rotating A/B hero, inconsistent headline stats, a live-in-nav-but-dead Tesamorelin page) in the crowded DTC GLP-1 + anti-aging telehealth space — now making a **second bet that widens its addressable buyer well beyond men's-health adjacency**: one-time prescription emergency/preparedness kits (the Jase Medical / Duration Health "stockpile antibiotics, just in case" category). That line monetizes the same pharmacy-network + physician-review rails on a one-time-purchase model (no subscription retention needed), at $285–$945 AOVs far above a monthly injectable. Three notable plays: (1) **breadth** — weight-loss flagship + wide anti-aging menu + skincare + now emergency kits under one roof; (2) **Amble Cares** low-income GLP-1 access (now a built-out "up to 50% off" program, not just a press release); (3) the plan-length pricing ladder ("commit longer, pay less") + "same price, every dose" as the subscription retention lever. The medkit line is the one to watch — it's a meaningfully different business with a different regulatory surface (mass-prescribed antibiotics/ivermectin/HCQ "just in case") and a different customer than the rest of the catalog.

## Provenance

- **Pages:** 18 analyzed via Firecrawl (`maxAge:0`, US geo, serial) + 1 map — homepage (all formats), 6 live injectable PDPs (/glp-1-injections, /nad-injections, /sermorelin-injections, /glutathione, /lipo-b, /lipo-c), /skin, /faq, /amble-cares-program, and all 8 /medkits/ PDPs. Tesamorelin re-confirmed 404 via curl (not scraped). No /about or /pricing page exists; resource/calculator + /press + /referral-program pages skipped this run.
- **Verify:** all 18 sourceURLs matched; all body md5s unique (no §5.1 geo/cache contamination); no junk soft-404s.
- **Credits:** 19 (1 map + 1 homepage + 7 therapeutic PDPs + 8 medkit PDPs + faq + amble-cares; +1 retry on viral-ick after a transient Firecrawl 500). Logos near-free (rode the homepage payload).
- **Run profile:** express (fresh re-capture over a 6/04 warm capture, per command); +offerings.md, +telehealth.md cohort pack, +logos:{} module. Depth gate: Deep — Notion Companies row reads `Direct competitor? = Yes`, `Importance to us = High`, `Sells to = Consumers`.
- **Couldn't get:** company/founding/team data (no /about); a live Tesamorelin price (PDP 404s); independent verification of self-reported scale, ratings, and efficacy; exhaustive per-kit medication rosters for all 8 medkits (sampled — see offerings.md).
