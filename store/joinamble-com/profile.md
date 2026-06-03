---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: joinamble.com
name: Amble
aliases: ["Amble Health, Inc."]      # legal/operating name per safety-info disclaimers; brand is "Amble"
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/joinamble/
  tiktok: https://www.tiktok.com/@joinamble
  facebook: https://www.facebook.com/JoinAmbleHealth/
external:
  trustpilot: https://www.trustpilot.com/review/joinamble.com

# Capture meta
captured_at: 2026-06-03
capture_method: firecrawl
site_notes: "Webflow (data-wf-/website-files.com; designSystem payload says 'unknown' — ignore). No JSON-LD. No /about or /pricing page — products + faq + press carry positioning. Per-product pricing lives in a plan-length table on each product page (12-mo cheapest → 1-mo dearest; homepage 'From $X' = the 1-mo rate). Funnel on intake./enroll.joinamble.com, customer portal on my.joinamble.com. Nav recoverable from <nav>. Rotating hero (Anti-aging ⇄ Weight loss) and inconsistent self-reported stats across pages — point-in-time."
key_pages:
  weight_loss_glp1: /glp-1-injections
  nad: /nad-injections
  sermorelin: /sermorelin-injections
  skin: /skin
  faq: /faq
  press: /press
unverified_fields:
  - "Founding date, team, headcount, ownership — no /about page on site; deep-research job, not capture. (Press release dates the Amble Cares launch to May 2026.)"
  - "Per-SKU pricing for Tesamorelin, Glutathione, Lipo-B (MIC+B12), Lipo-C — those product pages were not individually captured this run; they follow the same plan-table model. Defer per-SKU grain to offerings.md."
  - "Prices/IA are a point-in-time snapshot, not fixed — rotating hero (Anti-aging ⇄ Weight loss) plus inconsistent self-reported stats captured the same day: member count '100,000+ members' / '100,000+ patients' / '250,000+ patients'; avg loss '33 lbs' (homepage) vs '34 lbs' (GLP-1 page)."

description: "A DTC telehealth brand delivering compounded GLP-1 weight-loss and anti-aging injectables plus prescription skincare 100% online, pairing licensed-physician review with home delivery through a partner pharmacy network."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://cdn.prod.website-files.com/67fec0a64d109843c12f501a/68803a3b82b7cf8ed115ecec_favv-icon.svg  # branding.images.logo null; no on-page wordmark img; og:image is a share banner — favicon fallback
brand_colors: { primary: "#F18F20", accent: "#8078AD" }  # warm orange + purple, both confirmed in hero panels; branding's #3898EC is Webflow's default blue (chrome)
fonts: [Geist, Manrope]              # Geist body, Manrope headings (generic "sans-serif" ranked first — excluded)
color_scheme: light
design_framework: webflow
---

## Overview

Amble (Amble Health, Inc.) is a direct-to-consumer telehealth platform selling prescription weight-loss, anti-aging, and skincare treatments delivered entirely online. A free online intake routes the patient to a state-licensed physician (video/phone consult "where required by state law") who, if appropriate, prescribes medication that ships free to the door, with ongoing provider messaging. The site is explicit that Amble is a **managed-services provider** — it supplies the technology and administrative coordination, but does **not** offer medical advice, fill prescriptions, or operate as a pharmacy; medications (compounded and FDA-approved) are filled through an affiliated 503A/503B pharmacy network.

## What they offer

Three categories, all sold as recurring monthly plans where the per-month price falls with plan length (12-mo cheapest, 1-mo dearest). Per-line, bold-led, prices verbatim:

- **Weight loss — GLP-1 injections:** Compounded **semaglutide** & **tirzepatide**, self-administered subcutaneous, once weekly. Plan table: **12-mo $135 · 6-mo $145 · 3-mo $160 · 1-mo $179** per month (homepage "From $179") `[published]`
- **NAD+ injection:** Anti-aging — "Boost energy, sharpen focus." **12-mo $125 · 6-mo $167 · 3-mo $183 · 1-mo $199** per month `[published]`
- **Sermorelin injection:** Anti-aging GH-boosting peptide — "Produce more growth hormone." **6-mo $135 · 3-mo $149 · 1-mo $159** per month `[published]`
- **Tesamorelin injection:** Anti-aging — "Naturally boost growth hormone." Same plan-table model; per-SKU price not captured this run `[published]`
- **Glutathione injection:** Anti-aging — "Feel energized, support immune system." Per-SKU price not captured this run `[published]`
- **Lipo-B (MIC+B12) injection:** "Blend of lipotropic nutrients and B12." Per-SKU price not captured this run `[published]`
- **Lipo-C injection:** "Lipotropic nutrients, vitamin C, and B." Per-SKU price not captured this run `[published]`
- **Skin — prescription skincare:** Personalized compounded formulas (tretinoin, clindamycin, azelaic acid, niacinamide, GHK-Cu, hydroquinone, tranexamic acid, vitamin B5/E, estriol, caffeine) for acne, aging, hyperpigmentation, hydration, rosacea. **Starting at $55 per month** `[published]`

Weight loss is the foregrounded line (the referral program counts only Weight Loss sign-ups; Amble Cares is weight-loss-focused). Per-SKU/molecule depth defers to `offerings.md` if the cohort enables it.

## How it works / model

- **Journey:** Free online quiz/intake (health history, goals) → state-licensed **physician** reviews and (where state law requires) conducts a live video/phone consult → tailored recommendation in the patient's Amble portal → if prescribed, medication ships in discreet packaging, free → unlimited ongoing provider messaging + 24/7 support.
- **Make-up:** Amble is the tech/admin layer; **licensed physicians** (claimed in all 50 states) prescribe; an affiliated **503A (state-licensed) / 503B (FDA-registered)** pharmacy network fills, including **compounded** (not FDA-approved) and FDA-approved meds.
- **Money:** Subscription / plan-length pricing, "transparent, all-inclusive," **no insurance required/accepted**. BNPL offered via **Affirm, Klarna, Afterpay**. Referral (GrowSurf): **"Give $50, Get $50"** in account credit on a referred friend's first eligible (weight-loss) order; FL residents excluded.
- **Reach:** Available in all 50 states ("exclusions apply").

## Positioning & audience

B2C consumers pursuing weight loss, anti-aging/longevity, and skincare via low-friction online prescription care. Stated promise: *"Science backed care, tailored to your goals,"* *"Medical treatment delivered to your door, 100% online,"* with "no hidden fees" and "no in-person visit." The **Amble Cares Program** (announced May 2026) adds an access/equity angle — affordable weight-loss treatment for low-income Americans, which the press release frames as "The First Telehealth Platform" to do so (self-claimed).

## Nav structure

```
- Weight loss — /glp-1-injections
- Anti aging (dropdown)
  - NAD+ injection — /nad-injections          (Boost energy, sharpen focus)
  - Sermorelin injection — /sermorelin-injections   (Produce more growth hormone)
  - Tesamorelin injection — /tesamorelin-injection  (Naturally boost growth hormone)
  - Glutathione injection — /glutathione       (Feel energized, support immune system)
  - Lipo-B (MIC+B12) injection — /lipo-b        (Blend of lipotropic nutrients and B12)
  - Lipo-C injection — /lipo-c                  (Lipotropic nutrients, vitamin C, and B)
- Skin — /skin
- More (resources / calculators)
  - BMI calculator — /bmi-calculator
  - TDEE calculator — /tdee-calculator
  - Calorie deficit calculator — /calorie-deficit-calculator
  - Protein calculator — /protein-calculator
  - Water intake calculator — /daily-water-intake-calculator
- Login — my.joinamble.com/login
```

## Credibility & proof

All self-reported (record, don't endorse), and several figures are **internally inconsistent across pages captured the same day**:

- **Scale (self-reported, inconsistent):** "100,000+ members" (marquee) · "100,000+ patients" · "250,000+ patients" (hero badge).
- **Trustpilot:** on-site badge **"4.5"** linking to trustpilot.com/review/joinamble.com (self-reported display; rating not independently verified here).
- **Efficacy (self-reported, inconsistent):** "33 lbs lost on average" (homepage) vs "34 lbs lost on average" (GLP-1 page); "Drop a clothing size," "Reduce your cravings," "Shrink your waist."
- **Trust framing:** "FDA regulated pharmacies," "Licensed physicians" in all 50 states, "503A/503B pharmacies," "Free expedited delivery," "Unlimited 24/7 support."
- **Testimonials:** "Real people, real results" section with named customer IG/TikTok handles.
- **Press:** "Amble in the news: No items found." One press release — May 2026, the Amble Cares Program launch. Extensive on-page Important Safety Information for semaglutide/tirzepatide and the compounded-drug disclaimers.

## Visual & brand impression

Clean, modern wellness-DTC aesthetic on white: full-width gradient hero panels in warm **orange** (weight loss) and **purple** (anti-aging), rounded product cards, generous whitespace, and friendly diverse lifestyle photography (real smiling customers, not stock-clinical). Lowercase **"amble"** wordmark, Geist/Manrope type, a single dark pill CTA ("Find your treatment"). Reads professional and approachable — premium-but-accessible rather than clinical or luxury.

## Strategic read

A young, fast-moving brand (2026 press footprint, no /about, rotating hero, and inconsistent headline stats all point to a recent/iterating launch) in the crowded DTC GLP-1 + anti-aging telehealth space. Two notable bets: (1) **breadth** — pairing the weight-loss flagship with a wide anti-aging peptide/injectable menu and prescription skincare under one roof; (2) the **Amble Cares** low-income-access positioning as a differentiator. The plan-length pricing ladder (commit longer, pay less per month) is the retention lever.

## Provenance

- **Pages:** 7 analyzed via Firecrawl (`maxAge:0`, US geo, serial) — homepage (all formats) + /glp-1-injections, /nad-injections, /sermorelin-injections, /skin, /faq, /press. No /about or /pricing page exists; resource/calculator pages skipped as funnel content.
- **Verify:** all 7 `sourceURL`s matched the requested URL; all body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 8 (1 map + 1 homepage + 6 key pages).
- **Couldn't get:** company/founding/team data (no /about); per-SKU pricing for Tesamorelin, Glutathione, Lipo-B, Lipo-C (pages not individually scraped this run); independent verification of self-reported scale, ratings, and efficacy claims.
