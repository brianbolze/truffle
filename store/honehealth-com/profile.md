---
schema_version: 1

# Identity
domain: honehealth.com               # primary key (resolves 200 directly; no redirect)
name: Hone Health
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Cloudflare-fronted; firecrawl-only (skip WebFetch). WordPress site (rawHtml has wp-content; favicon + images on /wp-content/). branding.designSystem.framework reports 'bootstrap' — WRONG (§5.4): it's WordPress, not bootstrap and not the strawman's claimed Next.js. Per-product/medication pricing lives on individual product pages as 'From $X/mo + membership', NOT on category pages. The canonical MEMBERSHIP-pricing surface is the homepage 'Membership with Meaning' section + the /how-it-works comparison table (there is a /membership-pricing stub but it's near-empty). Funnel/checkout on subdomains buy./start./app.honehealth.com — NOT reachable from the apex /v2/map (apex map surfaces only honehealth.com + help.honehealth.com). /v2/map at limit:500 ~491 URLs, /edge/ blog dominates. Pre-hero ribbon ('Low Energy/Hot Flashes/Inflammation/Cognition/TRT/Brain Fog') and process step-counter ('01'/'02') are Hone-side animations that surface into markdown intermittently — render artifacts, not content. No §5.1 contamination this run (6 bodies unique, sourceURLs matched; maxAge:0 + location:US + waitFor:3500 + serialized)."
key_pages:
  how_it_works: /how-it-works                              # canonical membership pricing table
  mens_trt: /mens/testosterone-replacement-therapy         # the wedge: TRT
  longevity_nad: /longevity/nad
  womens_menopause: /womens/menopause-treatment            # women's vertical (mixed-gender catalog)
  hone_at_home: /hone-at-home                              # concierge in-home arm (Botox/IV/biomarkers)
  peptides_waitlist: /peptides-waitlist                    # "coming soon" vertical
  membership_pricing: /membership-pricing                  # near-empty stub; homepage is canonical
  membership_help: https://help.honehealth.com/hc/en-us/articles/40161781101335   # Basic/Plus/Premium plan compare
unverified_fields:
  - "Per-SKU medication prices are 'From $X/mo + membership' anchors on product pages; the final price + which SKU maps to which membership tier is set behind the start.honehealth.com intake (not submitted)."
  - "Peptides vertical is a waitlist ('coming soon', 'this summer') — not yet purchasable; no pricing."
  - "A help-center article references Basic / Plus / Premium tiers, but the on-site pricing surfaces show only Basic ($25) and Premium ($155) — a 'Plus' tier was not surfaced on the marketing pages this run."
  - "Headcount / revenue / funding / ownership — not on the marketing site (deep-research job, not capture)."

# Description — one sentence
description: "A telehealth clinic offering hormone, longevity, weight-loss, sexual-health, and hair programs to both men and women, anchored on at-home/CLIA-lab biomarker testing and board-certified clinicians, sold on a Basic/Premium monthly membership plus per-medication cost."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth clinic service + the Rx drugs it prescribes/ships
portfolio_shape: Multi-product       # TRT, ED, weight loss, hair, NAD/longevity, women's menopause, Hone-at-Home concierge — distinct, separately-chosen programs
business_model: Subscription         # Basic $25/mo or Premium $155/mo membership (+ medication cost) — month-to-month
primary_industry: Healthcare & Life Sciences

# Visual identity — lifted from Firecrawl `branding` (homepage), confirmed against screenshot
logo_url: https://honehealth.com/wp-content/uploads/2024/04/cropped-favicon-150x150.png   # hostable favicon; the wordmark (branding.images.logo) is an inline data-URI SVG ("HONE")
brand_colors: { primary: "#F8F93F", secondary: "#E9D223", background: "#FFFFFF", text: "#0E0B20" }   # branding.colors. Screenshot-confirmed: #F8F93F (bright chartreuse-yellow) IS the true dominant brand hue (hero banner, "Membership" card, CTAs), paired with near-black navy #0E0B20 text on white. This run branding.colors.primary == the real hue (cf. AG1; unlike linear).
fonts: [DM Sans, STIX Two Text]      # branding.fonts: DM Sans=body, STIX Two Text=serif headings
color_scheme: light                  # branding.colorScheme + screenshot
design_framework: wordpress          # rawHtml wp-content. branding.designSystem said "bootstrap" — wrong (§5.4).
---

> **Strawman check (this domain is the SCHEMA.md example).** The strawman's **closed-set classification was exactly right** — `entity_type`, `target_market: [B2C]`, `offering_category: [Services / Consulting, Biotech / Pharma Products]`, `portfolio_shape: Multi-product`, `business_model: Subscription`, `primary_industry: Healthcare & Life Sciences` all match the captured reality. What was **wrong** was everything that must be *captured, not inferred*: the strawman invented `brand_colors {primary #0E3A2F green, accent #C7A867 gold}` (reality: yellow #F8F93F + navy), `fonts [Söhne, Tiempos]` (reality: DM Sans / STIX Two Text), `design_framework: next.js` (reality: WordPress), and over-narrowed the description to "to men" — Hone is **mixed-gender** (a full Women's Care line). The taxonomy is guessable; the payload-lifted fields are not. (See cohort FINDINGS.)

## Overview

Hone Health is a DTC telehealth clinic positioned around **hormone health and longevity** — "Longevity engineered around your biology." It serves **both men and women** (the homepage runs parallel five-card "Men's Care" and "Women's Care" grids), with testosterone replacement therapy (TRT) as its anchor and biomarker lab testing as the wedge: most journeys start with a blood panel ("Measure & Assess → Consult & Plan → Treat & Act → Optimize & Adapt"). Treatments are gated behind a monthly membership (Basic $25/mo or Premium $155/mo) plus the cost of any prescribed medication. A concierge in-home arm (**Hone-at-Home**) adds Botox, IV therapy, and 40+ biomarker testing.

## What they offer

Multiple distinct programs, split by gender, behind a membership (a future `offerings.md` would enumerate per-SKU):

- **Men's TRT** — `/mens/testosterone-replacement-therapy` (the wedge): Testosterone cypionate "From $28/mo," Cream "$60/mo," Troches "$60/mo," Clomiphene "$38/mo," Enclomiphene "$42/mo," Anastrozole "$22/mo" — all **+ membership**.
- **Men's:** ED (Tadalafil/Sildenafil ~$25/mo, PT-141 $130/mo), Weight Loss (naltrexone/bupropion/phentermine/topiramate/sermorelin/compounded liraglutide $60–$160), Hair Loss (Finasteride + Minoxidil $38/mo).
- **Longevity:** **NAD+** "$165/mo + membership" (hedged "may…" claims, FDA non-evaluation disclaimer).
- **Women's Care** — `/womens/menopause-treatment`: ~10 SKUs (testosterone injection/cream, estradiol patch, bi-est cream, progesterone, DHEA, estriol, Vagifem, Estrace — $28–$80 range); clitoral cream; shared weight-loss/longevity programs.
- **Hone-at-Home** (concierge): **Botox $350+, Biomarker Testing $65, IV Therapy $249+** — delivered in-home.
- **Peptides** — waitlist only ("coming soon," "this summer"); not yet purchasable.

**`portfolio_shape: Multi-product`** — clearly: TRT, ED, weight loss, hair, NAD/longevity, women's menopause, and the Hone-at-Home concierge line are distinct programs a customer chooses between, each with its own page and pricing.

## How it works / model

A **membership + medication** model. Journey: pick men's/women's → start a lab test (Basic $25 + $25 onboarding, or Premium $65) → board-certified clinician reviews biomarkers → prescribed protocol + ongoing monitoring. Two tiers (verbatim from the /how-it-works comparison table):

- **Hone Basic — $25/month:** advanced lab testing every 6 months, ability to purchase physician consults, members-only pricing on *select* (BASIC-labeled) medications/supplements. Initial test $25 + $25 onboarding fee.
- **Hone Premium — $155/month + medication cost:** regular lab testing, physician consults, full access to all Hone treatments/supplements/diagnostics. Initial test $65. ("Chosen by 95% of patients.")

Month-to-month, cancel anytime. **No insurance accepted** — "transparent, upfront pricing, no deductibles or co-pays"; FSA/HSA eligible (Hone provides a receipt). (Per prior weekly snapshots, Premium rose from $149→$155/mo on this capture date.)

## Positioning & audience

- **Who:** health-conscious adults, both genders — men seeking TRT/energy/longevity and women seeking menopause/hormone care.
- **Against:** the men's-health telehealth cohort (Hims, PeterMD) and longevity clinics (Healthspan) — Hone's differentiator is **lab-first / biomarker-led** care + a **dual-gender** book and an in-home concierge tier.
- **Claimed edge:** "Longevity engineered around your biology" — board-certified clinicians, CLIA-certified partner labs, evidence-based treatments, and continuous biomarker monitoring.

## Nav structure

Mega-nav with men's/women's dropdowns; product pricing lives on PDPs, membership on homepage + /how-it-works. (Funnel CTAs route to buy./start.honehealth.com subdomains.)

```
- Men's Care — Increase Testosterone (/mens/testosterone-replacement-therapy) · Improve Sexual Function (/mens/erectile-dysfunction-treatment) · Lose Weight (/mens/weight-loss) · Improve Appearance/Hair (/mens/hair-loss) · Live Longer & Better
- Women's Care — Relieve Menopause Symptoms (/womens/menopause-treatment) · Improve Sexual Function (/womens/clitoral-cream) · Lose Weight · Improve Appearance · Live Longer & Better
- Longevity — NAD+ (/longevity/nad) · Manage Thyroid · Peptides (/peptides-waitlist, waitlist)
- Hone-at-Home — /hone-at-home (Botox / IV Therapy / Biomarker Testing)
- How It Works — /how-it-works   ·   Membership — homepage / /membership-pricing (stub)
- Get Started → start.honehealth.com/hermes/landing
```

## Credibility & proof

- **Trustpilot:** "TrustScore **4.8**, **11,526** reviews" (homepage widget).
- **LegitScript Approved** seal (footer); **board-certified clinicians**; **CLIA-certified partner labs**; "Evidence-based treatments"; HSA/FSA eligible.
- **Brand ambassadors** (homepage): Paul Wesley, Nikki & Brie Garcia, Dan Churchill, Louisa Nicola, Brendan Fallis. Named "Real People, Real Stories" testimonials ("*Compensated Hone Patient").
- **Compliance:** NAD+ FDA non-evaluation disclaimer; "Hone-affiliated medical practices are independently owned and operated" (`/clinical-policy`); prescription gatekeeping language.

## Visual & brand impression

Confident, high-energy **light-mode** design on white with a single bold brand hue: **bright chartreuse-yellow `#F8F93F`** (the pre-hero banner, the "Membership with Meaning" card, and CTAs) against **near-black navy `#0E0B20`** text. Typography pairs **DM Sans** (clean sans body) with **STIX Two Text** (a serif used for the big "Measure & Assess / Consult & Plan / Treat & Act / Optimize & Adapt" section heads) — a science-meets-editorial feel. The hero pairs a man and a woman, signalling the dual-gender book up front. Reads as modern-clinical and premium, not sterile. (Here `branding.colors.primary` correctly captured the real hue — the yellow — unlike the linear failure mode.)

## Strategic read

Hone is the **lab-first, dual-gender** entry in the cohort: the membership ($25 Basic / $155 Premium) decouples the platform fee from medication cost, and the biomarker panel is both the wedge and the retention loop (re-test every 6 months → adjust protocol). The Hone-at-Home concierge arm (Botox/IV/in-home draws) is a differentiator none of the pure-DTC peers offer. The durable state worth recording: a biomarker-led longevity clinic monetizing a separable membership + per-medication subscription across both men's and women's hormone care, with a heavy compensated-ambassador/testimonial trust apparatus. Worth noting for the strawman: Hone's real implementation (WordPress, yellow/navy, mixed-gender) diverges sharply from the SCHEMA example's invented specifics even though the classification was dead-on.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30):** homepage (`/`, rich pass: markdown + html + rawHtml + links + branding + images + full-page screenshot), `/how-it-works`, `/mens/testosterone-replacement-therapy`, `/longevity/nad`, `/womens/menopause-treatment`, `/hone-at-home` — each markdown + links + full-page screenshot. Site inventory via `/v2/map` (limit 500, apex only).
- **Capture mechanics:** `maxAge:0` + `location:{country:US}` + `waitFor:3500` + serialized; all 6 bodies unique + sourceURLs matched (no §5.1 contamination). **7 credits**, clean run.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned markdown: `captures/2026-05-30/*.md`.
- **Couldn't get:** funnel-subdomain checkout pricing / SKU-to-tier mapping (behind start.honehealth.com intake); the "Plus" tier referenced in the help center (not on marketing pages). See `unverified_fields`.
