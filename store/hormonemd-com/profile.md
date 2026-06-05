---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: hormonemd.com
name: HormoneMD
aliases: [HMD]
parent: []
owns: []
socials:
  facebook: https://facebook.com/hormonemds
  x: https://x.com/hormone_md
  linkedin: https://linkedin.com/company/hormonemd
  instagram: https://instagram.com/hormonemd
external:
  crunchbase: https://www.crunchbase.com/organization/hormonemd

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Astro static marketing site (generator: Astro v5.14.5) — no JS wall / geo trap, clean serial capture. Signup + patient portal live on app.mdportal.org (white-label 'MDPortal' platform; every 'Get started' → app.mdportal.org/hmd, 'Log in' → app.mdportal.org/login). Pricing is a FLAT PLATFORM MEMBERSHIP on /pricing ($84/mo billed annually · $99/mo monthly), NOT per-treatment — every treatment PDP repeats the same '$84/mo including regular lab work'; medications billed separately at unquoted 'low rate pharmacy prices.' /llms.txt is a rich self-authored AI brief and lists a 7th protocol (Rapamycin, /rapamycin) with NO live page (absent from nav + two map passes incl. a --search rapamycin). Homepage ships a full MedicalOrganization JSON-LD graph (founder/HQ/socials/6-therapy roster) — self-authored, treated as hint-to-verify."
key_pages:
  pricing: /pricing
  testosterone: /testosterone
  estrogen: /estrogen
  semaglutide: /semaglutide
  sermorelin: /sermorelin
  metformin: /metformin
  dhea: /dhea
  states_served: /states-served
  llms: /llms.txt
unverified_fields:
  - "Founding year (2023) + founder (Matt Sessa, Las Vegas NV HQ) — from homepage JSON-LD only; no on-page about/history corroboration."
  - "Rapamycin — listed as a longevity protocol in /llms.txt but has no live page (not in nav or two map passes); not counted as a live offering."
  - "All-in medication cost — membership ($84–$99/mo) is published, but per-medication prices are not; meds billed at unquoted 'low rate pharmacy prices.'"
  - "Member/patient counts, funding, headcount — not disclosed on the marketing site."

# Description — one sentence: [what they do] + [how] + [focus/differentiator].
description: "A 100% online telehealth platform delivering hormone therapy (TRT, BHRT), GLP-1 weight loss, and longevity medications to US adults on a flat monthly membership that bundles licensed-provider consults, lab work, and discreet shipping."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — Firecrawl branding is a hint to verify; confirmed against screenshot + logo SVGs.
logo_url: https://imagedelivery.net/X2fm99A2m4ExYgx0B_biNQ/2951b56c-5574-45d4-c533-92edf85dae00/public
logos:
  wordmark: { src: "https://imagedelivery.net/X2fm99A2m4ExYgx0B_biNQ/2951b56c-5574-45d4-c533-92edf85dae00/public", w: 1112, h: 107 }   # "HormoneMD" SVG wordmark, stable Cloudflare-Images URL
  logomark: { src: "https://www.hormonemd.com/app_icon_192x192.png", px: 192, transparent: true }                                      # three-bar motif, on-domain PNG, alpha verified (corner α=0)
  og:       { src: "https://imagedelivery.net/X2fm99A2m4ExYgx0B_biNQ/6805b02c-0433-4f9f-d972-1b18c3b96700/public", w: 1160, h: 768 }   # declared og:image — a lifestyle stock photo (couple at-home yoga), not a branded cover
brand_colors: { primary: "#32B5D2", accent: "#FF0000" }   # teal #32B5D2 across UI (payload accent + link); logo SVG also carries bright cyan #00FFFF + red #FF0000 on dark #212121
fonts: [Poppins]
color_scheme: light
design_framework: Astro
---

## Overview

HormoneMD (HMD) is a 100% online, cash-pay telehealth platform for hormone optimization, weight loss, and longevity medicine. It connects US patients with state-licensed providers who — after a lab panel and a 30-minute virtual consultation — prescribe and ship treatment in discreet packaging: TRT for men, bioidentical HRT for women, compounded GLP-1s, a growth-hormone peptide, and off-label longevity drugs. Care runs on a flat monthly membership that bundles unlimited consultations, regular lab work, and shipping; medications are ordered separately at "low rate pharmacy prices." The patient experience itself runs on a third-party white-label platform, MDPortal (`app.mdportal.org`). Per the homepage JSON-LD, the company was founded in 2023 (founder Matt Sessa) and is based in Las Vegas, NV.

## What they offer

Six prescription treatment lines, all delivered under one platform membership (per-SKU grain in [`offerings.md`](offerings.md)). The membership price is published; the all-in cost is gated because medications bill separately, so each treatment line is `[partial]`:

- **Membership (the access product):** **$84/mo billed annually ($1,008/yr)** *(Popular, free initiation, 60-day med supply/order)* or **$99/mo monthly** *(Intro, $99 one-time initiation, 30-day supply)* — bundles unlimited virtual consultations, regular lab work, and discreet shipping `[published]`. Medications ordered separately at "low rate pharmacy prices, no upcharges or hidden fees."
- **Testosterone (TRT, men):** testosterone — injections, creams, or pills; "**$84/mo** including regular lab work" `[partial]`
- **Estrogen (BHRT, women):** bioidentical estrogen/progesterone/testosterone — injections, creams, pills, patches, or suppositories; "**$84/mo**" `[partial]`
- **Semaglutide (GLP-1 weight loss):** *compounded* semaglutide — weekly injections or capsules; "**$84/mo**" `[partial]`
- **Sermorelin (natural HGH / peptide):** sermorelin (GHRH peptide) — injections, nasal sprays, or pills; "**$84/mo**" `[partial]`
- **Metformin (metabolic / longevity):** metformin (off-label) — daily pills; "**$84/mo**" `[partial]`
- **DHEA (hormonal balance):** DHEA — oral pills or topical cream; "**$84/mo**" `[partial]`

*Rapamycin is listed as a longevity protocol in `/llms.txt` but has no live page — not counted here (see `unverified_fields`).*

## How it works / model

- **Journey:** free online assessment ("only a few questions") → if eligible, matched to a licensed provider in your state → lab work at one of "10,000+ lab partners nationwide" (in-person partner draw, not at-home kits) → 30-minute virtual consultation to personalize the protocol → medications shipped to the door in discreet packaging → ongoing unlimited consults, regular labs, and dose adjustments.
- **Money:** subscription — a flat monthly ($99) or annual-prepay ($1,008/yr ≈ $84/mo) membership; medications billed separately at pharmacy prices. **No insurance** ("Nope! HormoneMD does not require insurance… transparent pricing") — cash-pay / direct-care.
- **Delivery / platform:** signup and the patient portal run on `app.mdportal.org` (MDPortal), a white-label telehealth platform; HormoneMD is the consumer-facing brand on top.

## Positioning & audience

US adults seeking hormone optimization, weight loss, and "anti-aging / longevity," served both head-on — TRT-for-Men and BHRT-for-Women are parallel, co-equal hubs. Self-described as "a digital health platform that is making modern wellness affordable," leaning on transparent, all-inclusive, insurance-free, 100%-online access. Implicitly positioned against in-person hormone/anti-aging clinics and other DTC telehealth brands (the TRT + GLP-1 + longevity menu overlaps Hone, Maximus, Hims). Claimed edge: one all-inclusive membership (unlimited consults + labs + shipping), nationwide lab access, and discreet delivery.

## Nav structure

```
- Treatments
  - TRT for Men — /testosterone
  - BHRT for Women — /estrogen
  - Semaglutide — /semaglutide
  - Sermorelin — /sermorelin
  - Metformin — /metformin
  - DHEA — /dhea
- Pricing — /pricing
- Log in — https://app.mdportal.org/login
- Get started — https://app.mdportal.org/hmd
Footer:
  - Privacy Policy — /privacy-policy
  - Terms of Service — /terms-of-service
  - States Served — /states-served
```

## Credibility & proof

- **LegitScript-certified:** footer seal links to LegitScript ("Verify LegitScript Approval for www.hormonemd.com") — the meaningful health-merchant trust mark.
- **Medical advisory board:** "Our clinical protocols are developed by an expert Medical Advisory Board… updated based on the latest comprehensive clinical research (as of 2025)" — referenced but **not named** (no /physicians or clinician-bio page).
- **PubMed citations:** each treatment's JSON-LD links a supporting PubMed study (e.g. TRT → pubmed.ncbi.nlm.nih.gov/32068334) — an evidence gesture, self-selected.
- **Self-reported stats (verbatim, self-reported — not endorsed):** "40% of men over 50 suffer from low testosterone"; "85% of users lose meaningful weight" (semaglutide); "95% of patients produced more sex hormones" (DHEA); "80% of physicians are not trained in HRT" (estrogen).
- **Testimonials:** 3 per page, all unattributed and labeled "Verified HMD member."
- **Trust badges:** "Board-Certified Care · 10,000+ Lab Locations · Discreet Delivery."

## Visual & brand impression

Clean, modern, conversion-tuned DTC health aesthetic. Near-white canvas (#FAFAFA), Poppins type, a recurring soft "wave" graphic at section tops, and bright lifestyle photography (people in nature, yoga, active couples). The brand mark is the "HormoneMD" wordmark plus a three-bar cyan logomark motif; the logo SVG carries bright cyan (#00FFFF) and red (#FF0000) on near-black, while the UI settles on a softer teal (#32B5D2) for headlines, links, and buttons. Light scheme throughout, with "Get started" CTAs to `app.mdportal.org` repeated on every screen. Design maturity reads competent mid-tier — polished and credible, but template-clean rather than distinctive.

## Strategic read

The shape points to a lean, fast-to-market DTC telehealth operation: it runs entirely on a third-party platform (MDPortal), prices a single all-inclusive membership rather than per-drug, and casts a wide net across hormones + GLP-1 + longevity under one roof. The small footprint (7 states, "expanding soon") reads early-stage. Two tells of an aggressive SEO/AI-surface play ahead of full buildout: a hand-tuned `/llms.txt` that even instructs AI agents how to describe the company ("a regulated medical service, not a supplement store"), and a Rapamycin protocol advertised in that brief before its page exists.

## Provenance

- **Pages:** 10 captured via Firecrawl (homepage, /pricing, 6 treatment PDPs, /states-served, /llms.txt) + 2 map passes (base + `--search rapamycin`). Analyzed every captured `.md`, the homepage screenshot, and the homepage JSON-LD + nav (`fc.py signals`).
- **Verify:** `fc.py verify` — all 10 sourceURLs match, all bodies md5-unique; clean.
- **Credits:** ~12 (1 map + 1 homepage + 9 page scrapes + 1 rapamycin map-search; logos rode the homepage payload + free curl fetches).
- **Couldn't get:** per-medication prices (membership-only pricing); founder/founding corroboration beyond JSON-LD; a live Rapamycin page (none exists).
- **Run profile:** guided — +telehealth; +offerings; +logos (no emphasis).
