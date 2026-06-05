---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: malemd.com
name: MaleMD
aliases: ["MaleMD LLC", "Male MD"]
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/Malemd-Men-105027885208409/
  instagram: https://www.instagram.com/malemdhealth/
external:
  trustpilot: https://www.trustpilot.com/review/malemd.com

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Cloudflare-fronted jQuery/Bootstrap-5 server-rendered MPA (no JSON-LD on homepage). Products live on campaign-coded funnel paths (/sermorelin/v2/hc, /nad/v3, /25again/ckh, /hairsy/v2n/cj/h) — the clean canonical entry points are in /site-map + the homepage 'Explore' nav; per-line floor pricing is on the landing pages, full dose/plan tiers behind the questionnaire (/<product>/medication step). A/B: Convert + Google Optimize — hero headline rotates ('Better Sex' in the screenshot vs 'Better Energy' in the markdown, same scrape); treat hero/anchor + promo pricing as point-in-time. Partner pharmacy named in a footer modal: Curexa (Egg Harbor Twp, NJ). BPC-157 sits at /repair (homepage link, not in /site-map)."
key_pages:
  about: /about-us
  telehealth_consent: /telehealth
  safety_profile: /safety-profile
  site_map: /site-map
  sexual_health_knockout: /knockout
  sexual_health_hammerrx: /HammerRx
  generic_ed: /25again/ckh
  pe: /pe
  sermorelin: /sermorelin/v2/hc
  nad: /nad/v3
  metformin: /metformin
  sleep: /slp/lp
  hair: /hairsy/v2n/cj/h
  pain: /pain
  bpc157: /repair
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — A/B-tested (Convert + Google Optimize); hero headline and per-line promo pricing rotate run-to-run."
  - "Full dose/quantity and multi-month plan tiers sit behind the questionnaire (/<product>/medication step) — only landing-page floor prices captured."
  - "Provider count, ownership/founders, and Curexa relationship terms not on the marketing site (deep-research, not capture)."

description: "A DTC men's-health telehealth brand selling prescription sexual-health, longevity/peptide, hair, sleep and pain treatments online via an async questionnaire, filled by a third-party US pharmacy on cash-pay subscriptions."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://malemd.com/app-client/images/malemd_logo_white2.png   # STRAIN: canonical MaleMD wordmark, but a WHITE knockout (needs a dark surface); a black "5 years" anniversary lockup also ships at /app-client/images/home_v2/malemd_5years_logo_black.png
logos:
  wordmark: { src: "https://malemd.com/app-client/images/malemd_logo_white2.png", w: 269, h: 59 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=malemd.com&sz=256", px: 208, transparent: true }
  # og omitted — no og:image declared on the homepage (true absence)
brand_colors: { primary: "#DB3E4D", secondary: "#338DBF", accent: "#0D6EFD" }   # red is the brand hue (headline accent + promo stripes); blue = links/CTAs
fonts: [Montserrat, Poppins]   # Montserrat body, Poppins headings; Avenir LT Std tertiary
color_scheme: light
design_framework: Bootstrap 5 + jQuery   # STRAIN: from rawHtml script srcs (bootstrap@5.3.0, jquery 3.6.0, OwlCarousel/Swiper) — a server-rendered MPA, the rare case "bootstrap" is correct, not the branding-payload guess
---

## Overview

MaleMD is a DTC men's-health telehealth platform: a man fills out a short online health questionnaire, a US-licensed physician reviews it and prescribes if appropriate, and medication ships free and discreetly from a partner pharmacy. It spans five front-door categories — **sexual health, longevity/peptides, sleep, hair, and pain** — under one cash-pay, no-insurance subscription model, leaning on convenience, discretion, and "transparent pricing with no hidden fees." It markets ~5 years in business (a "5 years" anniversary logo) and operates in all 50 states + DC. The brand presents as physician-led and clinical ("100% physicians, no nurse practitioners") but the site itself is a conversion-optimized performance-marketing funnel, not a premium clinical brand.

## What they offer

Eleven prescription lines across five categories, all cash-pay subscription, intake-gated. Floor prices shown on landing pages; full dose/plan tiers sit behind the questionnaire. (Per-SKU roster + verbatim anchors in `offerings.md`.)

**Sexual health**
- **KnockoutRx:** daily compounded ED troche — tadalafil + vardenafil ("3-in-1"); "Start Today for **$1.64/pill**" `[partial]` — "Not all ingredients in KnockoutRx are FDA-approved"
- **HammerRx 2-in-1 Mint:** dissolving sildenafil + tadalafil mint — "**$6/dose**" / "As low as $6 per dose" `[published]`
- **Generic ED:** generic sildenafil & tadalafil — "As Low as **$1.65/pill**" `[published]`
- **PE Treatment:** sertraline for premature ejaculation — "**$0.87/dose** if prescribed" `[partial]`

**Longevity / peptides**
- **Sermorelin:** growth-hormone peptide (the site's promoted "Hot New Product") — "**$149/mo**" `[published]`
- **NAD+:** anti-aging/energy — "Starting at **$199**" (shown "$299 $199", "$100 Off Treatment Plans") `[published]`
- **Metformin:** metabolic/longevity — "**$5** for First Month / billed $55 first shipment, shipped quarterly / **$25 per Month After**" `[partial]`
- **BPC-157:** healing/gut-health peptide (at /repair) — **no price shown, quiz-gated** `[on-request]`

**Sleep · Hair · Pain**
- **Sleep Treatments:** hydroxyzine / ramelteon / trazodone / melatonin — "starting at **$1.50 per day**", tiers "As Low as **$47.20**" and "**$66.75**" `[published]`
- **Hair Regrowth:** finasteride + minoxidil — "Start for **$1.56 / Day**" / "Starting at **$47/Month**" `[published]`
- **Pain Management:** topical diclofenac gel — "**$89/month**", "$149/month", "$199/month" `[published]`

## How it works / model

- **Journey:** "3–5-minute" online health questionnaire → US board-certified physician reviews medical history "in a few short hours" → prescribes if appropriate → medication ships free in discreet plain packaging ("Customer Service" as the return-address name) → ongoing 24/7 provider messaging + monthly refills.
- **Modality:** **async** — questionnaire-driven, no scheduled video visit in the front-door flow (the /telehealth consent boilerplate references audio/video generically, but the described path is store-and-forward intake review).
- **Money:** cash-pay **subscription** / recurring rebill (Sublytics billing stack). "You won't be charged unless your doctor approves." "Medical visit, ongoing shipments, and provider messaging are all included in one low price." No insurance accepted.
- **Fulfillment:** prescriptions filled by partner pharmacies and shipped to the patient; partner pharmacy named as **Curexa** (see `telehealth.md`).

## Positioning & audience

- **Audience:** **men-only** — "MaleMD," "Men's Health, Simplified," male imagery and copy throughout; no women's line.
- **Pitch:** convenience + discretion + transparent flat pricing vs. the doctor's office ("Skip the doctor's office," "No waiting rooms," "discreet packaging"). Clinical credibility cues ("U.S. Licensed & Board Certified Physicians," "100% physicians, no nurse practitioners").
- **Against:** the broad men's-health telehealth field (Hims, Ro, Maximus, Mosh, etc.). Differentiators it foregrounds: physicians-only (no NPs), peptides (sermorelin/NAD+/BPC-157) alongside the usual ED/hair, and aggressive low entry pricing.
- **Notable gap:** **no TRT / testosterone** and no GLP-1 weight-loss line — unusual for the "men's optimization" segment; the longevity wedge here is peptides + metformin, not hormones.

## Nav structure

```
- Explore
  - Sexual Health
    - KnockoutRx — /knockout
    - HammerRx 2-in-1 Mint — /HammerRx
    - Generic ED — /25again/ckh
    - PE Treatment — /pe
  - Longevity
    - Sermorelin — /sermorelin/v2/hc
    - NAD+ — /nad/v3
    - Metformin — /metformin
  - Sleep Treatments — /slp/lp
  - Hair Regrowth — /hairsy/v2n/cj/h
  - Pain Management — /pain
- Meet MaleMD
  - About Us — /about-us
  - How it Works (on-page)
  - FAQs (on-page)
- Login — /login
- (footer) Telehealth — /telehealth · Terms — /terms-and-conditions · Privacy (privacy.cptn.co) · Do Not Sell — /do_not_sale · Accessibility — /accessibility-statement · Site Map — /site-map · American Heroes Discount — /heroes
```
(Homepage product grid also surfaces BPC-157 at /repair, not present in the nav or /site-map.)

## Credibility & proof

- **Trustpilot (self-reported widget):** "Excellent — **4.4 out of 5**, **1,644 reviews**" — recorded verbatim, self-embedded TrustBox, not independently verified.
- **LegitScript Certified** — footer seal links to LegitScript's verification page (cert #10453213).
- **HIPAA Compliant** + "FDA Regulated Pharmacies" / "USA FDA-regulated pharmacies" badges.
- **Provider claim:** "100% physicians… we do not have any nurse practitioners," "U.S.-licensed, board-certified," "licensed in all 50 states and DC" — page-attested, no named physicians / `/physicians` roster.
- **"American Heroes Discount"** (/heroes) — a military/first-responder discount program.
- **5-years anniversary** logo lockup — implies founded ~2021.

## Visual & brand impression

Light theme, white base with **red (`#DB3E4D`) as the brand accent** (headline highlight — "Better **Sex**" — and the repeating promo divider stripes) and **blue CTAs/links**. Montserrat/Poppins type. The design is competent mid-tier DTC-funnel: a dense product grid of bottle/pill renders, repeated trust badges, a long testimonial wall, an FAQ accordion, and a sticky "Hot New Product Alert" bar. It reads as performance-marketing-driven (heavy Taboola/Bing/GTM/Convert/Optimize instrumentation, campaign-coded URLs) rather than a polished, minimalist clinical brand à la Hims/Hone. Imagery is stock-style fitness/lifestyle men. The captured hero **A/B-flickers between "Better Sex" (screenshot) and "Better Energy" (markdown)** — a live read of the experimentation stack.

## Strategic read

- **Peptide-forward, hormone-free.** The longevity wedge is **sermorelin / NAD+ / BPC-157 + metformin**, explicitly compounded ("featured products include compounded products which have not been approved by the FDA"). It deliberately avoids TRT (Schedule III) and GLP-1s — a lower-regulatory-friction, lower-COGS, all-compounded/generic lineup. That's a different risk and supply posture than TRT-anchored men's brands.
- **Funnel-first, brand-second.** URL structure (`/v2`, `/v3`, `/ckh`, `/promo7g`), dual A/B tools, Taboola native ads, and Sublytics rebill point to a paid-acquisition + subscription-rebill model. The "$5 first month / $25 after," "$0.87/dose," "$1.50/day" framing is classic low-friction trial economics.
- **Third-party pharmacy, not vertically integrated** (Curexa) — it routes scripts rather than owning fulfillment, which caps the margin/integration story relative to a brand that owns its pharmacy.

## Provenance

- **Pages:** 16 captured via Firecrawl (homepage rich pass + /about-us, /telehealth, /safety-profile, /site-map, and 11 product landers: knockout, HammerRx, 25again/ckh, pe, sermorelin/v2/hc, nad/v3, metformin, slp/lp, hairsy, pain, repair). Map (78 URLs) used for inventory; key pages selected from homepage nav + /site-map.
- **Verify:** `fc.py verify` — all 16 sourceURLs matched, all bodies md5-unique, no junk soft-404s. Capture straddled midnight; the 4 pages that landed in a 2026-06-05 dir were consolidated into 2026-06-04.
- **Credits:** 17 (1 map + 16 scrapes); logos fetches headed/free.
- **Couldn't get:** full dose/plan tiers (behind the questionnaire); BPC-157 price (quiz-gated); named physicians; provider count; Curexa contract terms.
- **Run profile:** Express invocation; +offerings (Tier-1 roster), +telehealth (cohort pack), +logos (2.5 module). No emphasis steer; standard page selection.
