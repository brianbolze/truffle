---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: hydramed.com
name: HydraMed
aliases: []
parent: []
owns: []
socials: { instagram: "https://www.instagram.com/hydramediv/", facebook: "https://www.facebook.com/HydraMedIV/", linkedin: "https://www.linkedin.com/company/hydramediv/", x: "https://twitter.com/HydraMedIV" }  # JSON-LD sameAs (all handles "hydramediv")
external: {}   # JSON-LD sameAs also lists ~12 per-city Yelp pages + Google-Maps links — per-location, no single canonical brand record; presence noted in Credibility

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js (__NEXT_DATA__ + /_next/) with Storyblok CMS for media (a.storyblok.com). Full mega-nav serializes into the homepage markdown AND the <header> region — no flyout recovery needed. Map is ~63% local-SEO noise: of 252 URLs, 68 are /areas-served/<state>/<city> and ~90 are /blog/* — pull the catalog from homepage links + the /iv-therapy and /rx index pages, not the map. IV catalog lives at /iv-therapy/* (full menu sits behind a client-side 'Show All / Higher-Priced / Lower-Priced' filter — the /iv-therapy index markdown surfaces 19 priced 'Most Popular' drips; ~13 more specialty drips are named in nav/map but carry no captured price). Rx catalog at /rx/* with prices PUBLISHED on the /rx index (one-time vs monthly toggle). Pharmacy partners are NAMED on /faq (Olympia, Empower, Casa Pharma RX, Valiant). Two booking surfaces: /book (IV nurse visit) and /rx/telehealth (Calendly-style consult). Self-reported customer counts are inconsistent across /about-us (215k+ vs 75,000) and JSON-LD (ratingCount 8263)."
key_pages:
  iv_index: /iv-therapy
  rx_index: /rx
  about: /about-us
  faq: /faq
  compounded_policy: /compounded-medication-policy
  telehealth_consult: /rx/telehealth
  book: /book
  labs: /labs
  areas_served: /areas-served
  semaglutide: /rx/semaglutide
  testosterone: /rx/testosterone
unverified_fields:
  - "Self-reported customer/trust counts conflict: '215k+ Delighted Regular Customers' and 'over 75,000 people across the US trust HydraMed' (both /about-us) vs JSON-LD ratingCount 8263 — all self-reported, unreconciled."
  - "~13 specialty IV drips (beauty-glow, athletic-recovery, altitude-sickness, autoimmune-support, her-monthly, high-dose-vitamin-c, stress-relief, weight-loss, just-feel-better, custom-iv, energy-boost, covid-rescue/-max, you-pick-1) are named in nav/map but not individually priced — the full IV menu is behind a client-side filter."
  - "TRT (/rx/testosterone) shows 'Only available to Colorado Residents at this time' — geographic availability may shift run-to-run."
  - "Founding year, ownership/legal entity, headcount, funding, revenue — not on the marketing site (deep-research job)."

description: "A DTC wellness brand pairing nurse-administered at-home IV-drip therapy across 14 states with a nationwide telehealth 'Longevity Rx' line of compounded GLP-1s, TRT, peptides, and NAD+ prescribed online and shipped to the door."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Transactional / One-time   # STRAIN: IV (the #1-positioned hero) is pay-per-visit; the Longevity Rx line runs on subscription (monthly/annual) + one-time — see body
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — on-domain "HydraMed" header SVG (CorelDRAW export) committed to assets/
logos:                               # 2.5 module — measured from the SVG box + fc.py logos
  wordmark: { src: assets/wordmark.svg, w: 9313, h: 2709 }                                                              # navy IV-bag mark + "HydraMed" + "MOBILE IV + LONGEVITY RX" tagline (viewBox px; ~3.44:1)
  logomark: { src: "https://www.google.com/s2/favicons?domain=hydramed.com&sz=256", px: 256, transparent: false }      # navy rounded-square IV-bag + water-drop icon on a baked pale ground (judged on tile — not transparent)
  og:       { src: "https://a.storyblok.com/f/178208/1158x490/2b4be1c186/mobile-iv-therapy-at-home.webp", w: 1158, h: 490 }   # declared og:image — a lifestyle cover (nurse administering a home IV), not a branded mark
brand_colors: { primary: "#0D3186", accent: "#00A0E9", light: "#9FD8F6" }   # STRAIN: exact fills from the wordmark SVG — navy + cerulean + pale sky; branding.primary (#677489) was UI gray, branding.accent (#006EFF) a near-miss of the true cerulean
fonts: [Gilroy]                      # branding.typography.fontFamilies primary+heading = Gilroy
color_scheme: light
design_framework: next.js            # rawHtml: __NEXT_DATA__ + /_next/ (Storyblok-backed); branding.designSystem ignored per playbook
---

## Overview

HydraMed is a DTC health-and-wellness company built on two delivery engines under one "Live More, Age Smarter®" banner: **(1) mobile IV therapy** — licensed nurses administer vitamin/hydration drips in the patient's home, marketed as "Ranked #1 in Mobile IV since 2020" and served across **14 states**; and **(2) "Longevity Rx"** — a nationwide telehealth line where US-licensed providers prescribe compounded medications (GLP-1 weight-loss, TRT, peptides, NAD+, sexual-health, skincare) that ship free to the door. The about page frames it as "a smarter, modern alternative to traditional sick care," combining same-day IV care with longer-horizon "smarter aging." Chief Medical Director is **Dr. Thomas Paluska, MD** (Georgetown, board-certified Emergency Medicine, Navy veteran), licensed across 13 states.

## What they offer

Two distinct, separately-merchandised lines (per-SKU roster in `offerings.md`):

- **Mobile IV therapy:** ~30 nurse-administered drips, **$114–$494**, booked per visit (no travel fee), ~45 min. Priced flagships: **HydraMed Max $494**, **Cold & Flu Rescue Max / Immunity Boost Max $399**, **Myers' Cocktail Max $314**, **Original Myers' Cocktail $194**, **Hangover Rescue $199**, **NAD+ $199**, **IV Fluids Only $114** `[published]`. Customizable add-ins: Booster doses **$25 each** (17 options), extra fluid bag **$50**, NAD+ by mg **$100–$750** `[published]`.
- **Medical weight loss (GLP-1):** **Semaglutide from $199/mo** (one-time $249; dose ladder 1mg $199 → 12.5mg $499) and **Tirzepatide from $299/mo** (one-time $349), compounded `[partial]` (price moves materially with dose).
- **Men's hormone health (TRT):** **Testosterone (cypionate in MCT oil) $175/mo** ($150/mo on annual), compounded; requires labs ($99) + a video consult; **"Colorado residents only"** at capture `[partial]`.
- **Peptides & longevity:** Sermorelin injections **$199/mo** (one-time $249), NAD+ injections **$369**, NAD+ nasal spray **$190**, NAD+ 20% topical cream **$195**, GHK-Cu cream **$199**, VIP nasal spray `[published]`.
- **Sexual health:** PT-141 injection **$299**, PT-141 troche **$220**, Tadalafil troche **$180**, plus Trimix and Scream Cream `[published]`.
- **Other Rx:** Lipotropic B12 injections **$145** ($125/mo), bioidentical HRT (incl. women's), Rx skincare `[published]`.
- **Labs:** at-home/partner lab testing (`/labs`), priced **$99** on the TRT path `[published]`.

## How it works / model

Two journeys. **IV therapy:** book a date/time online (or call/text 800-801-8525) → a licensed nurse visits the home → ~45-min infusion; pay per visit, no membership. **Longevity Rx:** complete an online medical intake (ID + selfie verification) → a US-licensed provider reviews; **some states require a synchronous phone/video consult, others allow async secure messaging** → if approved, a compounded prescription is prepared by a partner pharmacy and shipped free, with unlimited virtual follow-ups. Money comes from **pay-per-visit IV bookings** (the hero engine) plus **per-product Rx priced one-time or as a monthly/annual subscription** (refills, "pause or adjust anytime"). HSA/FSA cards are explained and accepted; no insurance billing is mentioned.

## Positioning & audience

Targets convenience-seeking consumers — **men and women** — who want clinical care without a clinic visit ("We bring health home"). The IV line leans acute/lifestyle (hangover, immunity, energy, recovery, expectant-mother); the Rx line leans longevity/optimization (weight, hormones, peptides, skin). Positioned against (a) brick-and-mortar IV bars / urgent care — undercut on convenience ("easier than booking a hair appointment," no travel fee) — and (b) single-vertical DTC telehealth (Hims/Ro/Hone) — countered by bundling acute IV + longevity Rx under one brand. Differentiator claims: "no hidden fees," meds-included hangover drips "unlike competitors," and local nurses "who know your community." Trademarked tagline **"Live More, Age Smarter®"**.

## Nav structure

```
- Mobile IV Therapy — /iv-therapy
  - Most Popular IVs: Original Myers' Cocktail /iv-therapy/original-myers-cocktail · Myers' Cocktail Max
    /iv-therapy/myers-cocktail-max · Hangover Rescue /iv-therapy/hangover-rescue · HydraMed Max
    /iv-therapy/hydramed-max · Energy Boost Max /iv-therapy/energy-boost-max · Cold & Flu Rescue
    /iv-therapy/cold-flu-rescue · Immunity Boost /iv-therapy/immunity-boost
  - Immunity & Rescue IVs: Migraine Rescue /iv-therapy/migraine · Nausea Rescue /iv-therapy/nausea-rescue ·
    Food Poisoning /iv-therapy/food-poisoning · Cold & Flu Rescue (Max) · Immunity Boost (Max)
  - Wellness IVs: NAD+ /iv-therapy/nad
- IV Therapy Areas — /areas-served  (14 states: CO, AZ, IL, FL, KS, TX, TN, MO, GA, NV, VA, MD, DC, WY)
- Rx Shipped To You — /rx
  - Longevity & Performance /rx/longevity-performance · Lean Muscle Mass & Fat Loss
    /rx/lean-muscle-mass-fat-loss · Sexual Health /rx/sexual-health · Rx Skin Care /rx/skincare
  - Medical Weight Loss /rx/medical-weight-loss: Semaglutide /rx/semaglutide · Tirzepatide /rx/tirzepatide
  - Men's Hormone Health: TRT /rx/testosterone
  - Energy & Metabolism: Lipotropic Injections /rx/lipotropic-injections
  - Strength & Performance: Sermorelin /rx/semorelin/injections · VIP Nasal Spray /rx/vip
  - Peptide Therapy /rx/peptides: PT-141 /rx/pt141 · GHK-Cu /rx/ghk-cu
  - NAD+ Therapy /rx/nad: Injections · Nasal Spray · Topical Cream (20%)
  - Medical Care: Lab Testing /labs · Request Refill /refill · Free Consult & Pre-Screening /rx/telehealth
- About Us — /about-us
  - HydraMed: About /about-us · News & Updates (Blog) /blog · Careers /careers
  - Mobile IV Therapy: What is IV Therapy? /what-is-iv-therapy · IV Therapy Benefits
  - IV Treatments: Allergies /iv-treatments/allergies · Colds & Flu · Dehydration · Food Poisoning ·
    Hangovers · Migraines & Headaches · Nausea · Pregnancy & Morning Sickness
```

## Credibility & proof

- **Self-reported rating:** "Google Rating 5.0" (homepage) and JSON-LD `AggregateRating` **5 / 8,263** — verbatim, self-reported, not independently verified.
- **Self-reported scale:** "215k+ Delighted Regular Customers," "30+ US Areas Served," "200+ Medical Professionals," "24h Expert Care," and separately "over 75,000 people across the US trust HydraMed regularly" (all /about-us) — flagged self-reported and internally inconsistent.
- **Clinical governance:** Chief Medical Director **Dr. Thomas Paluska, MD** (named, with /rx/team/leadership bio + LinkedIn); "every HydraMed patient meets with a state-licensed medical provider"; HIPAA-compliance claimed for all staff.
- **Pharmacy quality (claimed):** partner pharmacies described as **PCAB-accredited, cGMP-compliant, 503A & 503B certified**, with LegitScript and NABP accreditations, USP 800 handling, third-party potency/sterility testing, and a COA per compounded batch (`/compounded-medication-policy`, `/faq`).
- **Reviews footprint:** ~12 per-city Yelp listings + Google-Maps profiles (JSON-LD `sameAs`); named-customer testimonials with city + role throughout the homepage and about page.
- **Required disclaimers:** "Compounded versions of Tirzepatide and Semaglutide are not FDA-approved"; services "have not been evaluated by the FDA" — surfaced on Rx pages and the compounded-medication policy.

## Visual & brand impression

Clean, friendly, consumer-wellness — not clinical-sterile. The identity is a deep **navy (#0D3186)** paired with a bright **cerulean (#00A0E9)** and pale sky (#9FD8F6), carried by the IV-bag logomark and the **Gilroy** geometric sans throughout. Photography is warm domestic lifestyle (nurses in scrubs administering drips to relaxed clients in living rooms), reinforcing the "care comes to your couch" promise. The homepage is dense and conversion-built: a live chat bubble, persistent Book/Call/Text CTAs, a large filterable IV-drip grid with per-card "What's Inside" dose tables, a 14-state area map, and a testimonial wall. Reads as a mature, well-merchandised DTC operation rather than an MVP, with heavy programmatic-SEO scaffolding (per-city + per-blog pages) underneath.

## Strategic read

A **hybrid local-services + telehealth-Rx** model: the mobile-IV arm is a geographically-bounded, nurse-delivered, pay-per-visit business (a logistics/ops moat in 14 states, grown via dense local SEO), while the Longevity Rx arm is an asset-light, nationwide, compounded-Rx subscription layered on top of the same brand and customer base — "alongside our mobile IV therapy." Fulfillment is **third-party compounding pharmacies** (Olympia, Empower, Casa Pharma, Valiant — all named), so HydraMed owns the brand, clinician network, and demand engine but not the pharmacy — the inverse of an owns-the-pharmacy integrator. The IV menu (meds-included rescue drips, "best price in America" add-ins) competes on price/convenience; the Rx menu mirrors the standard compounded-GLP-1/TRT/peptide catalog. Notable constraint: TRT is gated to Colorado residents at capture, suggesting state-by-state licensing rollout still in progress.

## Provenance

- **Pages:** homepage (rich: markdown/html/rawHtml/links/branding/images/screenshot), /iv-therapy + /rx (rich index passes), /about-us, /faq, /compounded-medication-policy, /rx/telehealth, /rx/semaglutide, /rx/testosterone — 9 pages, Firecrawl `maxAge:0`, `location:US`, `waitFor:3500`.
- **Verify:** all sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 11 (1 map + homepage + 8 key pages + 1 logomark/og asset fetch is free).
- **Couldn't get:** prices for ~13 specialty IV drips (behind a client-side filter); founding year, ownership/legal entity, headcount, funding (not on site); reconciliation of the conflicting self-reported customer counts.
- **Structured layer (schema 2.2):** `socials` (IG/FB/LinkedIn/X, all "hydramediv") and `logo` read from homepage JSON-LD via `fc.py signals`; JSON-LD `@type` includes LocalBusiness + MedicalOrganization + Brand (self-reported AggregateRating → Credibility); `sameAs` also carries per-city Yelp/Google records (noted, not promoted to `external` — no single canonical). No `alternateName`/`legalName` present.
- **Run profile:** guided — Express telehealth invocation; +offerings (Tier-1 per-SKU roster), +telehealth (cohort pack), +logos (2.5 module; wordmark extracted from the on-domain header SVG, committed to assets/wordmark.svg). Stamped schema_version 2.5.
