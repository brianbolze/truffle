---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: marekhealth.com
name: Marek Health
aliases: ["Marek Health LLC"]        # JSON-LD legalName
parent: []
owns: ["marekdiagnostics.com"]   # "Diagnostic Labs" sibling brand on its own Shopify storefront (footer link + nav); same family, ownership not stated explicitly
socials: { instagram: "https://www.instagram.com/marekhealth", x: "https://twitter.com/marekhealth", youtube: "https://www.youtube.com/@marekhealth", facebook: "https://www.facebook.com/marekhealth/", linkedin: "https://www.linkedin.com/company/marek-health" }   # footer anchors (+youtube +linkedin vs prior capture)
external: { trustpilot: "https://www.trustpilot.com/review/marekhealth.com" }   # third-party review record the site links + cites

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js (rawHtml __NEXT_DATA__ + /_next/); homepage A/B-tests (cart_variant=new-home, sign-up-a/-b CTA splits) — IA/figures are a point-in-time snapshot. HOMEPAGE WAS REDESIGNED since 2026-05-31: client count 50k→'60,000+', new public price ladder ($0 free consult → $299 Protocol → $450 lab floor), labs now drawn at Quest/Labcorp (not at-home). Mega-nav is JS-walled — header items (Treatments/Diagnostic Labs/Education/Shop) collapse to the current page or /home in markdown; real offering taxonomy = the 10 goal/treatment pages reachable from any treatment page's 'Explore Other Treatment Options' grid, NOT the nav. Map: 417 URLs, ~80% /blog + single-word influencer/affiliate slugs (/derek,/mpmd,/syatt,/troponin…) + /apparel merch — treatment routes & key pages from homepage/treatment-page links. JSON-LD declares /assets/marek-logo.svg + /assets/marek-og-image.png but BOTH 404 (real assets live on images.marekhealth.com). Consumer per-treatment/per-SKU drug pricing sits behind the intake/login; only the $299 intake, $450 lab floor, and $80–200/mo ongoing-treatment figures are public. Labs are a separate Shopify store on sibling marekdiagnostics.com (published à-la-carte panel prices). Founder is 'Derek'/MPMD ('More Plates More Dates' YouTuber) — not named on captured pages; athletic/optimization slant throughout. A/B: yes."
key_pages:
  about: /about-marek
  testosterone: /testosterone
  weight_loss: /weight-loss
  sexual_health: /sexual-health
  performance: /performance
  hair_loss: /hair-loss
  look_younger: /look-younger
  think_sharper: /think-sharper
  sleep_better: /sleep-better
  heart_health: /heart-health
  fertility: /fertility
  faqs: /faqs
  diagnostic_labs: https://marekdiagnostics.com
  free_consult: /dc/form/discovery-intro
  sign_up: /sign-up
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — homepage A/B-tests (cart_variant/sign-up split); client count, hero copy, and the pricing module differ run-to-run."
  - "Per-treatment & per-drug consumer pricing — behind the intake flow/login; only the $299 intake, $450 lab floor, and the '$80–200/mo' (homepage) / '$135 yr-1, $70 after' (JSON-LD) ongoing-treatment figures are public (the two ongoing figures disagree — both quoted, not reconciled)."
  - "Specific Rx SKUs/doses per treatment — pages name molecules generically (semaglutide, tadalafil, finasteride, HCG, bempedoic acid…) but not doses/brands; the only dosed example is the homepage protocol mockup ('Testosterone Cypionate 80mg')."
  - "Ownership/legal relationship to marekdiagnostics.com — sibling Shopify storefront, relationship not stated; pharmacy 'ownership' marketing ('Marek Health's FDA-approved pharmacies') conflicts with the FAQ's '503A/503B compounding fulfillment partners… multiple companies'."
  - "Founder identity (Derek/MPMD) — not attested on any captured page; carried as prose context only."
  - "Headcount, funding, revenue — not on a marketing site (deep-research, not capture)."

description: "A premium men's-leaning telehealth optimization platform that pairs advanced diagnostic lab work with 1-on-1 health coaching and partnered-clinician prescriptions, delivering hormone, weight-loss, sexual-health, and longevity protocols billed à la carte rather than as fixed subscriptions."

# Classification
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription   # STRAIN: monthly coach check-ins + med refills + semi-annual labs are economically subscription-like, BUT Marek emphatically rejects "set subscription plans" — bills à la carte (one-time $299 intake, then per-lab/per-treatment), "cancel anytime"
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://images.marekhealth.com/website_assets/homepage/marek-health-desktop-logo-dark.webp   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: "https://images.marekhealth.com/website_assets/homepage/marek-health-desktop-logo-dark.webp", w: 294, h: 44 }   # dark-mode (white) wordmark, the rendered homepage mark
  logomark: { src: "https://www.google.com/s2/favicons?domain=marekhealth.com&sz=256", px: 32, transparent: false }   # red rounded-square "M" shield; sz=256 served only 32px; baked red background (not transparent)
  # og: omitted — declared og:image (/assets/marek-og-image.png, 1200×630) 404s; no servable cover
brand_colors: { primary: "#BB433C" }   # STRAIN: a single oxblood red (≈#BB433C) carries both the brand mark (favicon shield) + all CTAs over a near-black ground with white type — the two "slots" are the same hue (verified vs screenshot + red favicon/stat graphics)
fonts: [Montserrat, Inter]   # Montserrat headings, Inter body
color_scheme: dark
design_framework: next.js   # rawHtml has __NEXT_DATA__ + /_next/; branding.designSystem said "custom" (wrong, as usual)
---

## Overview

Marek Health is a premium **telehealth platform for health optimization** — explicitly *not* a clinic ("Marek Health is not a healthcare clinic… a platform that connects clients with highly specialized healthcare providers"). It pairs **advanced diagnostic lab work** (130+ foundational biomarkers, 1,000+ add-ons, LC/MS testosterone assays) with a dedicated **1-on-1 health coach** and a **board-certified, partnered medical provider** who builds a precision protocol from the client's biomarkers — hormones, peptides, GLP-1s, and supplements shipped to the door, with monthly coach check-ins. The flow is the branded **Guided Optimization®** program. It spans ten consumer treatment goals plus a B2B partnership arm and a separately-branded labs storefront (**marekdiagnostics.com**). The brand grew out of founder "Derek" (the *More Plates More Dates* / MPMD YouTube channel) and openly serves a performance/optimization audience comfortable with "high-leverage therapeutics" that mainstream telehealth avoids. Claims **60,000+ clients** and a **4.9 Trustpilot** rating; HQ admin office in Pontiac, MI; US-only, all 50 states.

## What they offer

Multi-product, organized as ten goal-oriented treatment areas (clinician-prescribed; per-drug pricing behind intake — per-SKU detail in `offerings.md`). Molecules below are page-attested; the spine is the $299 → labs → protocol funnel. TRT is the origin and deepest line.

- **Optimize your testosterone (TRT):** `/testosterone` — flagship; injections (preferred) + topical cream; homepage protocol example "Testosterone Cypionate 80mg, subcutaneous" — **price behind intake** `[on-request]`
- **Improve weight loss:** `/weight-loss` — GLP-1 body recomposition; **Semaglutide, Tirzepatide** named `[on-request]`
- **Increase your libido / sexual health:** `/sexual-health` — ED + libido; **Tadalafil, Bremelanotide (PT-141)** named `[on-request]`
- **Hair loss prevention:** `/hair-loss` — **Finasteride, Dutasteride, Minoxidil** named `[on-request]`
- **Look younger:** `/look-younger` — aesthetic/skin via **BHRT** (bio-identical HRT) `[on-request]`
- **Better heart health:** `/heart-health` — cardiometabolic; **Bempedoic Acid** named `[on-request]`
- **Fertility:** `/fertility` — **HCG**, NAD+ named `[on-request]`
- **Remove brain fog:** `/think-sharper` — cognitive optimization (protocol-based, no molecule named) `[on-request]`
- **Sleep better:** `/sleep-better` — "Guided Sleep Optimization®" (protocol-based) `[on-request]`
- **Perform better:** `/performance` — athletic/peak-performance ("Are you an elite athlete?") `[on-request]`

Platform pillars & adjacent lines:

- **Diagnostic Labs (marekdiagnostics.com):** the wedge — a separate Shopify storefront with **published à-la-carte** panel pricing. **Total Health Panel — "$595" (Comprehensive; 80+ biomarkers)**, also Complete/Executive tiers; individual markers from **"$9"** (CMP, Lipid, CBC) and **"$55"** (Total + Free Testosterone); genetic tests **"$500"** (Androgen Receptor CAG), **"$200"** (APOE), **"$225"** (MTHFR); build-your-own from 100+ markers. Drawn at Quest (2,000+ partner locations). `[published]`
- **Guided Optimization intake — "$299":** 45-min coach intake + health-history review + custom lab-panel strategy; then **"Lab panel — starting at $450"** + provider consult + treatments. `[partial]` (drugs/labs billed separately on top)
- **Free Discovery Call — "$0" / 30-min:** top-of-funnel consult to assess fit. `[published]`
- **1-on-1 Health Coaching:** assigned coach ("health strategist") + partnered provider — the recurring core; ongoing treatment **"averages $80–200/month"** (homepage) / **"$135/month in year one and $70/month thereafter"** (JSON-LD). `[partial]`
- **Partnership Program (B2B):** white-label coaching/labs for health professionals — footer routes to `coaching@marekhealth.com` (the prior `/cpp` landing page is retired). `[on-request]`
- **Shop / Apparel:** branded merch (`/apparel/*` — tees, flannel, trucker hat); supplements dispensed within protocols. `[published]`

## How it works / model

Four-step Guided Optimization® journey: **(1)** complete a health-history questionnaire + book a **45-min video intake** with a dedicated health coach ($299) → **(2)** coach builds a custom panel; client gets labs drawn at **any Quest/Labcorp location** (4,000+ nationwide; "starting at $450"), results in ~5–14 days → **(3)** coach reviews every result on a live video call, then a **board-certified partnered provider** prescribes the protocol → **(4)** medications/peptides/supplements ship from licensed pharmacies, then monthly coach check-ins, refills, and labs every 6 months. Revenue = $299 intake + lab sales + ongoing coaching + medication/supplement sales. Marek **emphatically rejects fixed subscriptions** ("we don't offer any set subscription plans and you can cancel whenever") — care is billed à la carte, though the refill/check-in cadence is economically subscription-like. It positions as a *connector platform*, not a provider, and fulfills medications through **503A/503B FDA-approved compounding pharmacies as fulfillment partners** (the FAQ describes "multiple departments at multiple companies," conflicting with marketing's "Marek Health's FDA-approved pharmacies"). **Program requirements:** an annual in-person physical (telehealth compliance), provider follow-ups at 6–12 weeks then every 6 months, and labs every 6 months. US-only; no insurance billed (direct/cash-pay; FSA/HSA accepted; no CPT/ICD codes).

## Positioning & audience

Targets self-directed **"human optimization"** seekers — people already researching peak performance who want clinician oversight instead of forum guesswork. Male-leaning and athletic/bodybuilding-coded (the testosterone page runs "Masculinity is in crisis"; recommenders are IFBB pros, UFC fighters, and strength coaches), but **not men-only** — the hero shows a man *and* a woman, panels come in male/female, and testimonials/blog content address women's hormone health. Claimed edge: a **comprehensive, labs-first, data-driven** approach (130+ biomarkers, LC/MS testosterone — "the gold standard most clinics skip") vs. "cookie-cutter panel, hand you a prescription, and move on" telehealth; partnered providers who are themselves optimizers and comfortable with "high-leverage therapeutics"; and a real coaching relationship. Implicit competitive set is the DTC men's-health / optimization field (Hone, Maximus, Hims) plus mass labs (the diagnostics arm undercuts on price — "lab prices down 33%"). Differentiates on coaching depth, diagnostic rigor, and an unapologetic performance stance.

## Nav structure

Header mega-nav is JS-walled (items collapse to the current page / `/home` in markdown); offering taxonomy reconstructed from each treatment page's "Explore Other Treatment Options" grid + footer.

```
- Treatments (mega-nav, JS-walled) — 10 goal/treatment pages:
  - Optimize your testosterone — /testosterone
  - Improve weight loss — /weight-loss
  - Increase your libido — /sexual-health
  - Hair loss prevention — /hair-loss
  - Look younger — /look-younger
  - Remove brain fog — /think-sharper
  - Sleep better — /sleep-better
  - Perform better — /performance
  - Better heart health — /heart-health
  - Fertility — /fertility
- Diagnostic Labs — marekdiagnostics.com (separate Shopify storefront)
- Coaching — /team-marek
- Education (JS-walled)
- FAQs — /faqs
- Testimonials — /testimonials
- Shop / Apparel — /apparel/*
- CTA: Get Started / Start your journey — /sign-up · /sign-up-b
- Free consultation — /dc/form/discovery-intro
- Footer → Services:
  - Guided Optimization — /sign-up
  - Diagnostic Labs — marekdiagnostics.com
  - Partnership Program (B2B) — coaching@marekhealth.com
- Footer → Legal: Cancellation & Refund Policy — /cancellation-refund-policy
- Contact: info@marekhealth.com · 1 (877) 572 2582 · Pontiac, MI (admin only)
```

## Credibility & proof

- **Scale claim:** "Trusted by 60,000+ clients" / "60,000+ clients optimized"; 10-week before/after transformation grid on the homepage.
- **Ratings (self-reported, flagged):** "4.9 on Trustpilot" / "4.9 out of 5 on Trustpilot"; JSON-LD `AggregateRating` **"ratingValue": "4.9", "reviewCount": "900"** — links to trustpilot.com/review/marekhealth.com (record not independently verified here).
- **Stats cited (verbatim, self-presented):** "130+ biomarkers," "1,000+ additional biomarkers available," "500+ available therapies (TRT, GLP-1s, & Peptides)," "4,000+ lab locations," "LC/MS testosterone assays."
- **Recommenders ("The pros trust Marek"):** Stan Efferding, Jordan Syatt, Emily Hayden (IFBB Pro), Sean Brady (UFC), Samson Dauda (IFBB Pro), Craig Jones (BJJ), John Jewett (IFBB Pro), Phil Daru, Derek Lunsford (IFBB Pro), Keone Pearson (IFBB Pro), Bill Maeda, Ali Gilbert.
- **"Discussed on" podcasts:** Joe Rogan Experience, Impact Theory, Power Project, Modern Wisdom, Brett Cooper Show, Forbes (treatment pages add Elite FTS, Generation Iron, The Drive, RxD, Mark Manson, Jordan Peterson).
- **Regulatory:** **LegitScript-certified** seal (footer); references board-certified medical providers, 503A/503B FDA-approved/audited compounding pharmacies, and annual-physical compliance.
- **Founder/audience:** founded by Derek (MPMD / *More Plates More Dates*) — not named on captured pages; built on his optimization-focused audience (the affiliate-slug sprawl in the map is the channel made visible).

## Visual & brand impression

Dark, premium, cinematic, masculine. Near-black ground, white type, and a single oxblood-red (≈#BB433C) accent on CTAs and the shield logomark — confident and moody rather than clinical or wellness-pastel. The treatment pages lean on **dramatic chiaroscuro editorial photography** (a rim-lit man, a father and newborn, an anatomical heart, a backlit couple, a silhouetted athlete) — evocative condition imagery, *not* product shots; the only product-like render anywhere is a low-res vial-and-syringe on the TRT page. Montserrat headlines over Inter body read clean and slightly editorial. The whole aesthetic is a serious "optimization for high performers" brand — closer to a supplement/athlete label than a soft DTC telehealth funnel. Polished, cohesive, mature Next.js build; the sibling marekdiagnostics.com is a cleaner, lighter Shopify storefront.

## Strategic read

- **Creator-origin moat:** built on Derek/MPMD's large optimization audience — a built-in, high-intent acquisition channel rivals would have to buy. The influencer/affiliate slug sprawl (`/derek`, `/mpmd`, `/syatt`, `/troponin`…) is the affiliate machine made visible.
- **Platform, not clinic:** the explicit "we connect clients to providers, we are not a clinic" framing is both a compliance posture and a scalability lever — it offloads the medical entity and lets Marek own the coaching + diagnostics + commerce layers.
- **Two-front commerce — care and labs:** the 2026 redesign reframes the front door as **labs-first / data-first** ("We turn your data into results"), and the spun-out **marekdiagnostics.com** Shopify store sells labs à la carte at aggressive prices ("down 33%") — a separate, lower-friction wedge that feeds the higher-LTV Guided Optimization funnel.
- **Deliberately not subscription:** rejecting fixed plans (now "No subscription required," "Cancel anytime" on every CTA) is a positioning choice against lock-in-criticized telehealth, even as the care cadence is recurring.
- **Performance stance as differentiator and risk:** openly embracing "high-leverage therapeutics" and a PED-adjacent athletic audience is a sharp brand asset but a regulatory tightrope (hence the LegitScript seal, platform framing, annual-physical requirement, and NY/NJ/RI lab restrictions on the diagnostics side).

## Provenance

- **Pages:** homepage (full branding + screenshot), `/about-marek`, `/faqs`, all 10 treatment pages (`/testosterone`, `/weight-loss`, `/sexual-health`, `/performance`, `/hair-loss`, `/look-younger`, `/think-sharper`, `/sleep-better`, `/heart-health`, `/fertility`), and sibling `marekdiagnostics.com` (15 unique pages) — all Firecrawl (`fc.py`, maxAge:0, location:US); offering taxonomy from treatment-page "Explore Other Treatment Options" grids (mega-nav JS-walled); pricing quoted verbatim from public surfaces only.
- **Verify:** all 15 md5-unique, all sourceURLs matched — clean, no geo/cache contamination.
- **Credits:** 16 billed (1 map + 1 homepage + 13 marekhealth pages + 1 diagnostics; logos/hero reads were free off cached payloads).
- **Couldn't get:** per-treatment/per-drug consumer pricing (behind intake/login); specific Rx SKUs/doses; marekdiagnostics.com ownership detail; financials/headcount (out of scope).
- **Run profile:** guided — full module run: `+offerings` (per-treatment roster), `+telehealth` (cohort pack), `+logos`, `+offerings hero images` (treatment-page heroes — note: no isolated SKU renders exist; Marek sells a service). Forced refresh over a still-warm (2026-05-31) capture because the homepage was redesigned and the modules are new.
- **Structured layer (schema 2.5):** homepage JSON-LD (`MedicalBusiness` + `FAQPage` + `Service` + `HowTo`) read via `fc.py signals` — confirmed `aliases` "Marek Health LLC", address Pontiac MI, `AggregateRating` 4.9/900 (→ Credibility, flagged self-reported), the $299 `Offer`; `socials` from footer (+youtube +linkedin vs prior); `external` trustpilot. JSON-LD `logo`/`og:image` both 404 → fell back to the rendered wordmark.
- **Migrations:** none (re-captured, not rule-rewritten); prior 2.2 capture archived to `captures/_archive/2026-05-31/`.
