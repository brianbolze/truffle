---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: eden.health
name: Eden
aliases: [tryeden.com]            # intake/funnel + portal domain; Trustpilot listed under tryeden.com. Legal entity: Eden Health International Inc.
parent: []
owns: [edenhealthclubs.com, edenpharmacy.com]   # sub-brands linked in footer ("More from Eden"); Eden Meals lives at meals.tryeden.com
socials: { facebook: "https://www.facebook.com/TryEdenHealth", instagram: "https://www.instagram.com/tryedennow", tiktok: "https://www.tiktok.com/@tryeden", linkedin: "https://www.linkedin.com/company/tryeden/", youtube: "https://www.youtube.com/@TryEden" }   # JSON-LD sameAs (all verified as footer anchors)

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Webflow site (cdn.prod.website-files.com, data-wf-*); branding.designSystem reports 'custom' (wrong). Mega-nav + footer render in markdown — full category nav captured. Map returns 486 URLs but ~85% is SEO blog (/post/*) + /creator,/author,/blog-categories; real catalog is the /treatment/* set, reachable from homepage nav. Pricing lives on product pages (e.g. /treatment/glp-1-treatments), not a /pricing page; membership terms are in the price footnote. Intake/checkout flows live on app.eden.health and www.tryeden.com. /find-your-treatment/* is a goal-selector quiz SPA (thin markdown). branding.colors are unreliable here (returned cyan #4EEAFF + red link); true palette read from screenshot."
key_pages:
  about: /about
  glp1_flagship: /treatment/glp-1-treatments
  goal_quiz: /find-your-treatment/global
  faq: /frequently-asked-questions
  reviews: /reviews
  safety_info: /safety-info
  blog: /blog
unverified_fields:
  - "Brand-color hex — branding payload returned cyan/red (link/hover artifacts); accent green and near-black wordmark read from screenshot, exact hex not captured."
  - "Per-product pricing beyond GLP-1 (NAD+, sermorelin, hair, MIC+B12) seen on homepage/nav as 'from' prices; full tier tables sit behind intake quizzes on app.eden.health / tryeden.com (not submitted)."
  - "Funding, headcount, revenue, founding year — not on the marketing site."

description: "A DTC telehealth platform connecting U.S. consumers with licensed providers and a network of compounding pharmacies to prescribe and ship compounded GLP-1s, peptides, NAD+, hormones, and hair treatments on a monthly membership."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://cdn.prod.website-files.com/676eb86a8ca7187507487da6/678a7c93763d80c5ef6ea922_edn-favicon.png  # branding.images.logo is an inline data-URI SVG wordmark; favicon used as the hostable fallback
brand_colors: { primary: "#1D1D1F", accent: "#2E6B4F" }  # STRAIN: primary = near-black wordmark (logo SVG fill rgb(29,29,31)); accent = forest green read from screenshot — branding payload's cyan/red are artifacts
fonts: [Satoshi Variable]
color_scheme: light
design_framework: webflow
---

## Overview

Eden is a direct-to-consumer telehealth brand (legal entity Eden Health International Inc.) that sells personalized prescription wellness programs entirely online. It connects consumers with licensed providers for a remote consultation, and — if prescribed — ships medication from a network of U.S. state-licensed compounding pharmacies, with 24/7 care-team messaging and ongoing dose management. The business leads with weight loss (compounded GLP-1s) but spans six treatment categories. It claims **127,000+ members** and serves all 50 states + Washington, D.C.

## What they offer

Six enumerable, separately-positioned treatment lines, all delivered as online consult → prescription → recurring shipment:

- **Weight Loss (flagship):** compounded semaglutide & tirzepatide, branded GLP-1s (Ozempic®, Wegovy®, Zepbound®, Mounjaro®), and a Custom Weight Loss Kit (oral metformin/bupropion/topiramate/B12/naltrexone blends).
- **Strength:** Sermorelin (injections + sublingual tablets), Vardenafil + Tadalafil.
- **Anti-Aging:** NAD+ (injections, nasal spray, face cream), Glutathione, plus a non-Rx "Cell Theory™" NAD+ supplement.
- **Hair Growth:** Finasteride, Minoxidil, GHK-Cu foam, Custom Hair Growth Kits (separate men's / women's variants).
- **Mood:** MIC+B12, Methylene Blue.
- **Hormones & Intimacy:** Hormone Therapy for Women (estradiol/progesterone); daily essentials (Everyday+).

Most products are prescription (ᴿˣ) and compounded. A large SEO blog (~250+ `/post/*` articles) and free tools (BMI/BMR/TDEE/calorie/protein/carb calculators) front the funnel.

## How it works / model

Customer journey: pick a health goal (or product) → free online intake form + telehealth consult with a licensed provider → if eligible, a custom prescription is dispensed by a partner pharmacy and shipped free/expedited to the door → ongoing 24/7 provider messaging, dose adjustments, and an in-app shot tracker via the member portal (`app.eden.health`).

**Revenue = subscription, two-part:** an **Eden Membership** ($39 first month, auto-renews at **$99/month**) is mandatory and unlocks access, *plus* the medication subscription priced separately:
- **Compounded Semaglutide ($99/mo*):** compounded GLP-1
- **Compounded Tirzepatide ($199/mo*):** compounded GLP-1
- **Ozempic® / Zepbound® / Mounjaro® ($1,399/mo); Wegovy® ($1,695/mo):** branded GLP-1s
- **Other lines (homepage "from" prices):** NAD+ from $119 first month; Sermorelin from $126 first month; Hair Kit from $83/mo; MIC+B12 from $73 first month

*"\*Price includes medication only, if prescribed. An active Eden Membership is required ($39 for the first month, auto-renews at $99/month thereafter). Membership does not include or guarantee a prescription."* Differentiator: a **"Same Price at Every Dose" guarantee** — flat pricing regardless of dose escalation, no long-term contracts, cancel anytime, FSA/HSA eligible, no insurance needed. Buy-now-pay-later via Klarna & Afterpay. Affiliate/creator program runs through CJ.

## Positioning & audience

Targets U.S. health-conscious adults seeking accessible, cash-pay metabolic, longevity, and aesthetic care without insurance friction. Tagline framing: *"Quality care, made simple"* and *"Look, feel and perform your best every day."* Positions against insurance-gated clinics and other DTC telehealth players — the blog directly publishes "Eden vs Hims/Hers, Ro, Noom, Calibrate, Found, LifeMD" comparison pages, signaling it benchmarks against the full GLP-1 telehealth cohort. Edge claims: flat per-dose pricing, no contracts, 24/7 provider access, and a "harmony of science and nature" wellness framing (cruelty-free / eco-friendly / paraben-, silicone-, sulphate-, gluten-free badges).

## Nav structure

```
- Weight Loss
  - GLP-1 Treatments ᴿˣ — /treatment/glp-1-treatments
  - Custom Weight Loss Kit ᴿˣ — /treatment/custom-weight-loss-kits
  - Ozempic® / Zepbound® / Wegovy® / Mounjaro® ᴿˣ — /treatment/{ozempic,zepbound,wegovy,mounjaro}
- Strength
  - Sermorelin Injections ᴿˣ — /treatment/sermorelin
  - Sermorelin Tablets ᴿˣ — /treatment/sermorelin-odt
  - Vardenafil + Tadalafil ᴿˣ — /treatment/vardenafil-tadalafil
- Anti-Aging
  - NAD+ Injections / Nasal Spray / Face Cream ᴿˣ — /treatment/{nad,nad-nasal-spray,nad-facial-cream}
  - Glutathione ᴿˣ — /treatment/glutathione
  - Cell Theory™ NAD+ Supplement (non-Rx) — /treatment/cell-theory
- Hair Growth
  - Men: Finasteride / Minoxidil / GHK-Cu Foam / Custom Hair Growth Kit ᴿˣ — /treatment/{finasteride-for-men,minoxidil-for-men,ghk-cu-for-men,hair-growth-kits-for-men}
  - Women: Minoxidil / GHK-Cu Foam / Custom Hair Growth Kit ᴿˣ — /treatment/{minoxidil-for-women,ghk-cu-for-women,hair-growth-kits-for-women}
- Mood
  - MIC+B12 ᴿˣ — /treatment/mic-b12
  - Methylene Blue ᴿˣ — /treatment/methylene-blue
- More
  - Daily Essentials: Glutathione, Everyday+ — /treatment/everyday-plus
  - Hormones & Intimacy: Hormone Therapy for Women ᴿˣ — /treatment/hormone-kit-for-women
  - Skin: NAD+ Face Cream — /treatment/nad-facial-cream
  - (also grouped by molecule class: Antioxidants, Peptides, Coenzymes)
  - Tools: BMI / BMR / TDEE / Calorie / Protein / Carb calculators — /calculators/*
- Footer — Company: About /about · Blog /blog · Community /community · Reviews /reviews · FAQs /frequently-asked-questions · Press /press · Careers /careers
- Footer — More from Eden: Eden Health Club (edenhealthclubs.com) · Eden Pharmacy (edenpharmacy.com) · Partner with Eden /partner-with-eden · Certified Trainers /trainer-directory · Eden Meals (meals.tryeden.com)
```

## Credibility & proof

- **Scale claims:** 127,000+ members; 1,000+ reviews; **Trustpilot 4.5/5 "Excellent"** (tryeden.com profile); "98% of members reported weight loss during treatment" (self-reported, n=4,633).
- **Named medical team:** Dr. Halland Chen, M.D. (Chief Medical Innovation Officer); Dr. Rebecca Emch, PharmD (VP of Pharmacy Operations); Medical Advisory Board: Dr. Matthew Bennett, M.D., Dr. William Lee, M.D. Credentialing schools shown (Miami, Einstein, Cornell, Pittsburgh, Mercer, Upstate, Columbus State).
- **Leadership named:** Adam McBride (CEO, Cofounder), Josh Khan (President, Cofounder), Daniel Dietz (COO, Cofounder), Jonah Hescock (CFO), Jared Widseth (CAO & General Counsel).
- **Pharmacy network + accreditations:** partner pharmacies GoGoMeds (KY), Precision (NY), Enovex (CA), AbsolutePharmacy (FL); badges for NABP, PCAB (compounding), ACHC, and LegitScript certification; "US-licensed 503A pharmacies."
- **Trust framing:** FSA/HSA eligible, free & discreet shipping, FDA-registered labs, same-day visits, no-contract cancel-anytime.
- **Regulatory disclosure (verbatim):** *"Compounded medications are not approved by the FDA and have not been reviewed for safety, effectiveness, or quality."* — repeated site-wide; dedicated `/safety-info` page.

## Visual & brand impression

Clean, premium-clinical DTC aesthetic on a light/white canvas. The signature accent is a **forest/emerald green** (hero cards, eco/"science and nature" badges, CTAs), paired with warm-neutral product photography — frosted vials and injector pens shot against terracotta, sand, and sage backdrops that lean "apothecary/wellness" rather than cold pharma. Lifestyle imagery features smiling, healthy-looking adults and white-coated providers on video calls. The wordmark "eden" is a lowercase, near-black (#1D1D1F) custom logotype. Typography is **Satoshi Variable** throughout (large 48px H1s), giving a modern, confident, slightly editorial feel. Overall the visual language signals approachable medical legitimacy — softer and more lifestyle-forward than a pure clinic, more clinical than a supplement brand.

## Strategic read

Eden is a broad-catalog GLP-1-led telehealth roll-up: weight loss is unmistakably the wedge (every promo banner, the BMI calculator, before/after sliders, and the bulk of the SEO blog point at it), but it has bolted on five adjacent compounded/peptide categories to widen LTV per member. The mandatory **membership ($99/mo) decoupled from cheap medication ($99 semaglutide)** is the core monetization mechanic — the membership, not the drug margin, is the recurring annuity, and the "same price at every dose" guarantee is the sharpest competitive hook against rivals that raise prices with titration. Heavy reliance on **compounded** (not FDA-approved) medications is both the cost advantage and the regulatory exposure — a risk that compresses if/when GLP-1 shortages end and compounding allowances tighten. The aggressive comparison-content strategy (dozens of "Eden vs [competitor]" articles) shows an SEO-led, performance-marketing growth model. Adjacent properties (Eden Health Club, Eden Pharmacy, Eden Meals, Certified Trainers) hint at an ambition to become a broader wellness ecosystem rather than a single-category pill shipper.

## Provenance

- **Pages:** homepage, `/about`, `/treatment/glp-1-treatments`, `/find-your-treatment/global`, `/frequently-asked-questions`, `/reviews` — 6 scrapes + 1 map (486 URLs, mostly blog); Firecrawl, 2026-05-30, location US, maxAge:0, via `fc.py`; visual identity read from full-page homepage screenshot + `branding`/`metadata` payloads.
- **Verify:** all sourceURLs matched, all body md5s unique (clean).
- **Credits:** not recorded this run.
- **Couldn't get:** per-product full pricing tiers (behind intake quizzes on app.eden.health / tryeden.com); the goal-selector quiz (`/find-your-treatment/*`) renders thin in markdown (links-only SPA); corporate financials/founding year (not on the marketing site).
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-05-30 rawHtml, hint-to-verify) — filled `socials` (fb/ig/tiktok/linkedin/youtube, footer-verified); JSON-LD `logo` sits on a different Webflow project bucket (possibly stale) so kept the current favicon; no `external`. Re-stamped 2.0→2.2.
