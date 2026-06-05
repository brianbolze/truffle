---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

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
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow (data-wf-/website-files.com; designSystem payload says 'unknown' — ignore). No JSON-LD. No /about or /pricing page — products + faq + press carry positioning. Per-product pricing lives in a plan-length table on each product page (12-mo cheapest → 1-mo dearest; homepage 'From $X' = the 1-mo rate). Funnel on intake./enroll.joinamble.com, customer portal on my.joinamble.com. Nav recoverable from <nav>. /tesamorelin-injection is nav-linked (top strip + Anti-aging dropdown) but its PDP 404s (depublished) — the only product in nav with a dead page. Product images are AVIF on the Webflow CDN (use a browser UA + sips to fetch/convert); each PDP ships a clean isolated vial render ('Stylized vial for marketing purposes only'). branding.images.logo IS the inline 'amble' wordmark SVG this run (was null before). A/B: yes — rotating hero (Anti-aging ⇄ Weight loss) and inconsistent self-reported stats run-to-run (member count, avg-loss) — point-in-time."
key_pages:
  weight_loss_glp1: /glp-1-injections
  nad: /nad-injections
  sermorelin: /sermorelin-injections
  glutathione: /glutathione
  lipo_b: /lipo-b
  lipo_c: /lipo-c
  skin: /skin
  faq: /faq
  tesamorelin_dead: /tesamorelin-injection   # nav-linked, PDP 404s
unverified_fields:
  - "Founding date, team, headcount, ownership — no /about page on site; deep-research job, not capture. (Press release dates the Amble Cares launch to May 2026.)"
  - "Tesamorelin: nav-linked (top strip + Anti-aging dropdown) but /tesamorelin-injection returns HTTP 404 'Page Not Found' — depublished, no live PDP/price this run. Not a live SKU."
  - "Prices/IA are a point-in-time snapshot, not fixed — A/B-tested rotating hero (Anti-aging ⇄ Weight loss) plus run-to-run inconsistent self-reported stats: this run shows '100,000+ members' and '33 lbs lost on average' (≈14.4%); a prior same-week run captured a '250,000+ patients' hero badge and a 34-lbs GLP-1-page figure."

description: "A DTC telehealth brand delivering compounded GLP-1 weight-loss and anti-aging injectables plus prescription skincare 100% online, pairing licensed-physician review with home delivery through a partner pharmacy network."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — the inline "amble" SVG from branding.images.logo this run (was favicon fallback in the 2026-06-03 capture, when branding.logo came back null)
logos:
  wordmark: { src: assets/wordmark.svg, w: 88, h: 28 }                                                                # rectangle — lowercase "amble" serif logotype, single dark charcoal color; extracted from branding.images.logo data-URI (viewBox 88×28)
  logomark: { src: "https://www.google.com/s2/favicons?domain=joinamble.com&sz=256", px: 256, transparent: false }    # square "a" mark on a BAKED white rounded square (apple-touch-icon identical) — shows as a white chip on a dark slide
  og:       { src: "https://cdn.prod.website-files.com/67fec0a64d109843c12f501a/6a03010ea30adcab15cb4bdf_amble-open-graph.avif", w: 1200, h: 630 }  # dark cover: amber GLP-1 + purple NAD+ vials, white "amble" wordmark
brand_colors: { primary: "#F18F20", accent: "#8078AD" }  # warm orange (weight loss) + purple (anti-aging), both confirmed in hero panels + vial renders; branding's #3898EC is Webflow's default blue (chrome)
fonts: [Geist, Manrope]              # Geist body, Manrope headings (generic "sans-serif" ranked first — excluded)
color_scheme: light
design_framework: webflow
---

## Overview

Amble (Amble Health, Inc.) is a direct-to-consumer telehealth platform selling prescription weight-loss, anti-aging, and skincare treatments delivered entirely online. A free online intake routes the patient to a state-licensed physician (video/phone consult "where required by state law") who, if appropriate, prescribes medication that ships free to the door, with ongoing provider messaging. The site is explicit that Amble is a **managed-services provider** — it supplies the technology and administrative coordination, but does **not** offer medical advice, fill prescriptions, or operate as a pharmacy; medications (compounded and FDA-approved) are filled through an affiliated 503A/503B pharmacy network.

## What they offer

Three categories, all sold as recurring monthly plans where the per-month price falls with plan length (12-mo cheapest, 1-mo dearest); each PDP also claims "same price, every dose." Per-line, bold-led, prices verbatim. **Per-SKU grain (molecule · form · dose · hero render) is in [`offerings.md`](offerings.md), captured this run.**

- **Weight loss — GLP-1 injection:** Compounded **semaglutide** & **tirzepatide**, self-administered subcutaneous, once weekly. **12-mo $135 · 6-mo $145 · 3-mo $160 · 1-mo $179** per month (homepage "From $179") `[published]`
- **NAD+ injection:** Anti-aging — "Boost energy, sharpen focus." **12-mo $125 · 6-mo $167 · 3-mo $183 · 1-mo $199** per month `[published]`
- **Sermorelin injection:** Anti-aging GHRH peptide — "Produce more growth hormone." **6-mo $135 · 3-mo $149 · 1-mo $159** per month (no 12-mo tier) `[published]`
- **Glutathione injection:** Anti-aging antioxidant tripeptide — "Feel energized, support immune system." **12-mo $75 · 6-mo $83 · 3-mo $92 · 1-mo $100** per month `[published]`
- **Lipo-B (MIC+B12) injection:** "Blend of lipotropic nutrients and B12." **12-mo $120 · 6-mo $125 · 3-mo $133 · 1-mo $149** per month `[published]`
- **Lipo-C injection:** "Lipotropic nutrients, vitamin C, and B." **12-mo $120 · 6-mo $125 · 3-mo $133 · 1-mo $149** per month `[published]`
- **Tesamorelin injection:** Listed in nav (top strip + Anti-aging dropdown, "Naturally boost growth hormone") but **the PDP `/tesamorelin-injection` 404s** — depublished, no live price this run. Not a live SKU. `[on-request]`
- **Skin — prescription skincare:** Personalized compounded formulas (tretinoin, clindamycin, azelaic acid, niacinamide, GHK-Cu, hydroquinone, tranexamic acid, vitamin B5/E, estriol, caffeine) for acne, aging, hyperpigmentation, hydration, rosacea. **Starting at $55 per month** `[published]`

Weight loss is the foregrounded line (the referral program counts only Weight Loss sign-ups; Amble Cares is weight-loss-focused). The anti-aging menu is six injectables sharing one plan-table template; lipo-B/lipo-C are priced identically.

## How it works / model

- **Journey:** Free online quiz/intake (health history, goals) → state-licensed **physician** reviews and (where state law requires) conducts a live video/phone consult → tailored recommendation in the patient's Amble portal → if prescribed, medication ships in discreet packaging, free → unlimited ongoing provider messaging + 24/7 support.
- **Make-up:** Amble is the tech/admin layer; **licensed physicians** (claimed in all 50 states) prescribe; an affiliated **503A (state-licensed) / 503B (FDA-registered)** pharmacy network fills, including **compounded** (not FDA-approved) and FDA-approved meds. The catalog itself is entirely **compounded**.
- **Money:** Subscription / plan-length pricing, "transparent, all-inclusive," **no insurance required/accepted**; **HSA/FSA cards accepted for 3-month-or-longer plans** (itemized receipts for self-submission). BNPL via **Affirm, Klarna, Afterpay**. Referral (GrowSurf): **"Give $50, Get $50"** in account credit on a referred friend's first eligible (weight-loss) order; FL residents excluded.
- **Reach:** Available in all 50 states ("exclusions apply").

## Positioning & audience

B2C consumers pursuing weight loss, anti-aging/longevity, and skincare via low-friction online prescription care. Stated promise: *"Science backed care, tailored to your goals,"* *"Medical treatment delivered to your door, 100% online,"* with "no hidden fees" and "no in-person visit." The **Amble Cares Program** (announced May 2026) adds an access/equity angle — affordable weight-loss treatment for low-income Americans, which the press release frames as "The First Telehealth Platform" to do so (self-claimed). Not gender-targeted — diverse lifestyle imagery, no men's/women's split.

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
- More (resources / calculators)
  - BMI calculator — /bmi-calculator
  - TDEE calculator — /tdee-calculator
  - Calorie deficit calculator — /calorie-deficit-calculator
  - Protein calculator — /protein-calculator
  - Water intake calculator — /daily-water-intake-calculator
- Login — my.joinamble.com/login
```

## Credibility & proof

All self-reported (record, don't endorse); several figures are **volatile run-to-run** (A/B-tested site):

- **Scale (self-reported):** "100,000+ members" (marquee, this run). A prior same-week run captured an inconsistent "250,000+ patients" hero badge — treat as point-in-time.
- **Trustpilot:** on-site badge **"4.5"** / **"4.5 • 2000+ reviews"** linking to trustpilot.com/review/joinamble.com (self-reported display; rating not independently verified here).
- **Efficacy (self-reported):** "33 lbs lost on average (≈ 14.4% of weight)" this run; "Drop a clothing size," "Reduce your cravings," "Shrink your waist." Before/after transformation testimonials (e.g. 357→120 lbs) with named customer IG/TikTok handles.
- **Trust framing:** "FDA regulated pharmacies," "Licensed physicians" in all 50 states, "503A/503B pharmacies," "Free expedited delivery," "Unlimited 24/7 support."
- **Press:** "Amble in the news: No items found." One press release — May 2026, the Amble Cares Program launch. Extensive on-page Important Safety Information for semaglutide/tirzepatide and the compounded-drug disclaimers.
- **No LegitScript seal** found in the footer; providers described as "physicians… licensed in all 50 states" but **no named-clinician page**.

## Visual & brand impression

Clean, modern wellness-DTC aesthetic on white: full-width gradient hero panels in warm **orange** (weight loss) and **purple** (anti-aging), rounded product cards, generous whitespace, and friendly diverse lifestyle photography (real smiling customers, not stock-clinical). Product renders are premium 3-D vials — an amber GLP-1 vial on orange, purple vials for the anti-aging line — each with a clean isolated "Rx Only" label. Lowercase **"amble"** serif wordmark, Geist/Manrope type, a single dark pill CTA ("Find your treatment"). Reads professional and approachable — premium-but-accessible rather than clinical or luxury.

## Strategic read

A young, fast-moving brand (2026 press footprint, no /about, rotating A/B hero, inconsistent headline stats, and a live-in-nav-but-dead Tesamorelin page all point to a recent/iterating launch) in the crowded DTC GLP-1 + anti-aging telehealth space. Two notable bets: (1) **breadth** — pairing the weight-loss flagship with a wide anti-aging peptide/injectable menu and prescription skincare under one roof; (2) the **Amble Cares** low-income-access positioning as a differentiator. The plan-length pricing ladder (commit longer, pay less per month), layered with "same price, every dose," is the retention lever.

## Provenance

- **Pages:** 11 analyzed via Firecrawl (`maxAge:0`, US geo, serial) — homepage (all formats), 7 live PDPs (/glp-1-injections, /nad-injections, /sermorelin-injections, /glutathione, /lipo-b, /lipo-c, /skin), the dead /tesamorelin-injection (404 confirmed), /faq, + map. No /about or /pricing page exists; resource/calculator + /press + /amble-cares + /referral pages skipped this run (press synthesized from the 2026-06-03 archive).
- **Verify:** all sourceURLs matched; all body md5s unique (no §5.1 geo/cache contamination). Tesamorelin body = a real 404 stub (trust-marquee + GrowSurf widget only), not a §5.6 soft-404-with-content.
- **Credits:** 12 (1 map + 1 homepage + 8 PDPs + 1 faq + 1 tesamorelin-search). Logos + hero images near-free (rode the homepage/PDP payloads; headed CDN fetches, no credits).
- **Run profile:** guided — refresh over a still-warm (2026-06-03) capture; +offerings.md, +telehealth.md cohort pack, +logos:{} module (2.5), +flagship product hero images (6 injectable vial renders → captures/2026-06-04/images/). Emphasis: the requested modules.
- **Couldn't get:** company/founding/team data (no /about); a live Tesamorelin price (PDP 404s); a clean isolated Skin product render (topical — before/after + lifestyle only); independent verification of self-reported scale, ratings, and efficacy claims.
