---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: onemedical.com
name: One Medical
aliases: ["Amazon One Medical", "www.onemedical.com"]   # "Amazon One Medical" is the brand name on the health.amazon.com surface
legal_entity: "1Life Healthcare, Inc."   # ©2026 1Life Healthcare, Inc. (homepage footer)
parent: [amazon.com]                 # "On February 22, 2023 Amazon completed the acquisition of One Medical" (/about-us) — explicit ownership attestation
owns: []                             # acquired Iora Health (2021-09-01) — fully absorbed into the seniors line, no standalone site to key on (prose)
socials:
  facebook: https://www.facebook.com/amazononemedical
  x: https://twitter.com/onemedical
  instagram: https://www.instagram.com/amazononemedical/
  youtube: https://www.youtube.com/channel/UCVuDmERByiofU8ss3Nz_Odw/featured
  linkedin: https://www.linkedin.com/company/one-medical-group
external: {}                         # no JSON-LD on homepage; no third-party records linked (looked, none found)

# Capture meta
captured_at: 2026-06-15
capture_method: firecrawl
site_notes: "Two surfaces, one entity: the consumer site www.onemedical.com (Wagtail/Django — image renditions `*.fill-WxH.jpg`/`.original.png` under /media/images/; `data-block-key` StreamField marker; server WSGIServer/CPython; no Next/React/WP markers) AND the Amazon storefront health.amazon.com/onemedical + /prime (brand 'Amazon One Medical', under 'Amazon Health Services'; sells the same care + the per-visit On-Demand Care). Map is 478 URLs but ~90% noise — hundreds of /locations/<metro>/<office> + /providers/<name>; signal lives under /services/*, /membership, /sixty-five-plus, /business, /about-us, /virtual-care, /insurance, /kids (pull from homepage links, not the map). No JSON-LD on homepage; socials + legal entity (1Life Healthcare, Inc.) come from the footer. Pricing is split + multi-tier — see unverified_fields. Employer-client count drifts by page (8,500+ on /about & /business vs 11,600+ on homepage) — report both, don't reconcile. Stack: GTM, Sentry, Wistia, NICE inContact chat. Amazon surface scraped clean on BASIC proxy (no enhanced needed) despite a 405 on a bare HEAD request."
key_pages:
  membership: /membership/
  seniors: /sixty-five-plus/
  kids: /kids/
  business: /business/
  services: /services/
  mindset: /services/mindset/
  about: /about-us/
  virtual_care: /virtual-care/
  insurance: /insurance/
  faq: /faq/
  amazon_onemedical: https://health.amazon.com/onemedical
  amazon_prime: https://health.amazon.com/prime
unverified_fields:
  - "Consumer membership has THREE published prices: standard $199/yr (/membership, non-Prime); $99/yr OR $9/mo for Amazon Prime members; +$66/yr per additional family member (max 5). All verbatim; a '$69 first year then $99/yr' Prime intro promo ($30 off) is point-in-time."
  - "On-Demand Care (formerly Pay-per-visit): 'from $29' messaging-only / '$49' video, 'varies by state/condition' — self-pay, FSA/HSA eligible, no membership. Resolves the prior capture's unknown pay-per-visit fee."
  - "Employer-client count conflicts across pages: '8,500+' (/about-us, /business) vs '11,600+ companies' (homepage). Both verbatim, not reconciled."
  - "Footprint metrics differ by page/measure: 'nineteen major U.S. cities' (/about-us) vs '125+ offices' (/sixty-five-plus). Both verbatim."
  - "Per-visit copay/deductible amounts for scheduled (insurance-billed) visits — insurance-plan-dependent, not shown."

# Description — one sentence
description: "Membership-based primary care practice, owned by Amazon, that blends app-first 24/7 virtual care with in-office visits across U.S. cities; it charges an annual membership on top of billing your insurance per visit, and also sells the same care as an employer benefit, to Medicare seniors, and as one-off self-pay virtual visits through Amazon."

# Classification
entity_type: Company
target_market: [B2C, B2B, B2B2C]
offering_category: [Services / Consulting]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — the live co-brand "amazon one medical" lockup, extracted inline <svg> from rawHtml (branding.images.logo empty); re-confirmed present in the 2026-06-15 rawHtml (viewBox 1083.2×168.9)
logos:                               # 2.5 module — co-brand lockup is the current primary mark; "amazon" smile-arrow in squid-ink + "one medical" in health-green
  wordmark: { src: assets/wordmark.svg, w: 1083, h: 169 }                                                          # rectangle "amazon one medical" lockup (viewBox 1083.2×168.9); CSS-token fills (#006B5D health-green, #0A2E2A squid-ink) inlined for portability
  logomark: { src: "https://www.onemedical.com/static/images/apple-touch-icon-180x180.png", px: 180, transparent: false }   # the 5-dot teal "+" mark on a BAKED WHITE square (beats the 152px google-s2; eyeballed — opaque ground; hasAlpha lies)
  og:       { src: "https://www.onemedical.com/media/images/240610_OM-Homepage-Open-Graph_1.2e16d0ba.fill-1200x630.png", w: 1200, h: 630 }   # declared og:image, verified 1200×630
brand_colors: { primary: "#006B5D", secondary: "#0A2E2A", background: "#FFFFFF" }   # deep teal/health-green identity (wordmark token #006B5D) over white; squid-ink #0A2E2A for the "amazon" mark + text
fonts: [Ginto, GT Super Display]     # branding ranked generic "sans-serif" first; real faces are Ginto (sans body) + GT Super Display (display serif headlines)
color_scheme: light
design_framework: wagtail            # Django/Wagtail — /media/images/*.fill-* + .original renditions + `data-block-key` StreamField marker in rawHtml; WSGIServer/CPython server header (no Next/React/WP markers); branding.designSystem ignored
---

## Overview

One Medical is a membership-based primary care practice — "a modern approach to primary care" built around same/next-day appointments, longer visits, calming offices, and an app that delivers 24/7 virtual care. Members pay an annual fee for the experience and access; actual scheduled visits are billed to insurance just like a normal doctor's office, so the membership sits *on top of* fee-for-service care rather than replacing it. The practice spans a direct-to-consumer membership, a large employer-benefits business, and a distinct value-based primary-care line for Medicare seniors (the Iora Health business it acquired in 2021). **Amazon completed its acquisition of One Medical on February 22, 2023**, making it Amazon's bricks-and-mortar primary-care arm under **Amazon Health Services** — sold on Amazon as **"Amazon One Medical,"** alongside Amazon Pharmacy and the per-visit On-Demand Care service.

## What they offer

One core service — membership primary care — sold to several buyer segments, with branded sub-programs as companions, plus an Amazon-channel per-visit option (bold lead-in, price + visibility token per line):

- **Consumer membership (Adults under 65):** annual membership for app-first primary care; works with your insurance. **"$199 a year"** standard (non-Prime) `[published]`; **"$9/mo or $99/yr for Prime members"** `[published]`; **"$66/year each"** per additional family member, max 5 `[published]` — /membership, homepage, health.amazon.com/onemedical
- **On-Demand Care (formerly Pay-per-visit):** one-time virtual visit for 30+ common conditions, **no membership, self-pay** — **"from $29"** (messaging only) / **"$49"** (video), "varies by state"; FSA/HSA eligible; accessed via Amazon.com `[published]` — health.amazon.com/onemedical/ppv
- **Seniors primary care (Adults 65+):** "relationship-based primary care for adults on Medicare" — the value-based Iora line; "works with your insurance (yes, including Medicare)." No separate membership fee shown `[on-request]` — /sixty-five-plus
- **One Medical for Business (employer benefit):** the same in-office + 24/7 virtual care sold to employers; enterprise pricing via "Get in touch" `[on-request]` — /business
- **Scheduled visits (in-office & video):** the fee-for-service layer **on top of** membership — "billed to you/your insurance; copays and deductibles may apply" `[on-request]` — /membership, /insurance
- **One Medical Kids:** pediatric & family care, included with membership `[on-request]` — /kids
- **Mindset by One Medical:** integrated mental health — assessments, coaching, therapy, behavioral-health screenings; bundled into membership / employer plans `[on-request]` — /services/mindset
- **Impact by One Medical:** chronic-condition management & prevention (diabetes, hypertension, obesity), eligibility-gated `[on-request]` — /services/chronic-conditions

Care breadth under **Services**: wellness & prevention, everyday care, chronic conditions, mental health, LGBTQIA+ care, urgent concerns, sexual health, the "Annual Wellness Visit," and **drop-in lab services** at offices. Per-program detail in `offerings.md`.

## How it works / model

Membership + insurance, two revenue streams stacked. You pay the annual membership ($199/yr standard; $9/mo or $99/yr via Amazon Prime) → use the app for 24/7 virtual care (Video Chat / "Treat Me Now" / secure messaging) at no extra cost → book in-office or scheduled video visits, which are **billed to you/your insurance** (copays and deductibles apply). So One Medical earns the recurring membership fee *and* fee-for-service reimbursement on scheduled visits.

Three economics braid under one brand: the **consumer subscription** above; the **seniors** business on a different model — value-based / Medicare primary care inherited from Iora Health (47 offices across ten markets at acquisition); and the **employer** business, per-employee health benefits ("11,600+ companies" / "8,500+ organizations"). Post-acquisition, Amazon adds two distribution levers: the **Prime bundle** ($9/mo or $99/yr — "up to 50% savings" vs $199, Prime membership required) that funnels Prime's base into membership, and **On-Demand Care** ($29 messaging / $49 video, self-pay, FSA/HSA), a one-off virtual visit sold straight through Amazon.com to people who don't want or need the membership.

## Positioning & audience

Tagline: **"Fall in love with your doctor's office"** / "Comprehensive healthcare just got less painful." Targets consumers fed up with traditional primary care — appointments that start on time, longer visits "so you don't feel rushed," calming offices "near where they work, live, and shop," and an app-first experience. Positions on **human-centered design + technology + an exceptional team**, against both conventional PCP offices and lighter "wellness" telehealth. Buyer segments: individual consumers (under-65 membership), Medicare seniors, and employers — and, post-acquisition, Amazon's own customers via the Prime bundle and Amazon.com-sold On-Demand Care. It is now Amazon's primary-care surface, cross-sold with Amazon Pharmacy.

## Nav structure

```
onemedical.com (consumer site):
- Locations
  - Offices — /locations/
  - Virtual Care — /virtual-care/
- For You
  - Adults under 65 — /membership/
  - Adults 65+ — /sixty-five-plus/
  - Kids — /kids/  (also /services/kids/)
  - Medicare agents — /sixty-five-plus/medicare-agents/
- For Business
  - Overview — /business/
  - Results — /business/impact/
  - Mental Health — /services/mindset/
  - Small Business — /small-business/
  - For Consultants — /business/consultants/
  - Resource Center — /resource-center/
  - Get in Touch — go2.onemedical.com/get-in-touch
- Log in — app.onemedical.com/login-web
- Sign up — app.onemedical.com/registration/signup
- Search — /search/

Utility / footer:
- Office locations — /locations/ · Virtual Care — /virtual-care/ · Insurance — /insurance/
- Providers — /providers/ · Services — /services/ · Blog — /blog/ · Give a membership — /gift/
- Careers — careers.onemedical.com · Media center — /mediacenter/ · About — /about-us/
- Sponsored membership — /sponsored-membership/ · Contact us — /contact-us/ · FAQ — /faq/

health.amazon.com (Amazon Health Services sub-nav, where One Medical also lives):
- One Medical (Membership) — /prime · /onemedical
- On-Demand Care (formerly Pay-per-visit) — /onemedical/ppv
- Amazon Pharmacy — pharmacy.amazon.com
- Health AI — /health-ai · Health Benefits Connector / Health Condition Programs — /health-condition-programs
- FSA | HSA store — amazon.com/FSA-Store
```

## Credibility & proof

Self-reported metrics (verbatim, **not endorsed**):
- **NPS:** "90+ Net Promoter Score"
- **Employer clients:** "8,500+ Employer Clients" / "8,500+ organizations" (/about, /business); "11,600+ companies" (homepage)
- **Engagement:** "45% of members use One Medical's digital services every month"
- **Retention:** "9 of 10 clients renew"
- **Cost savings:** "8%+ savings in total cost of care"
- **Tenure / footprint:** "delighting people for the past 15 years"; "nineteen major U.S. cities" (/about); "125+ offices" (/sixty-five-plus)
- **Third-party study:** JAMA Network Open — "Virtual + in-office primary care model linked to 45% lower employer total cost"
- **Client logos:** Google, Instacart, Lyft, Nasdaq, John Hancock, Cooley, Georgetown University, Avenues, Airbnb, Allbirds
- **Accolades:** CB Insights, Fast Company Most Innovative Companies (2019), Great Place to Work (certified), MedTech Breakthrough (2019)
- **M&A markers:** acquired Iora Health (2021-09-01); acquired by Amazon (2023-02-22)

## Visual & brand impression

Clean, calm, premium-consumer healthcare aesthetic — deep teal / health-green (`#006B5D`) as the brand hue against generous white space, with a friendly editorial serif (GT Super Display) for headlines over a geometric sans (Ginto) for body. Illustration-led (soft human figures rather than clinical stock photography), warm and approachable rather than sterile. Reads as mature and well-funded — consistent with a 15-year-old brand now resourced by Amazon. Tone is professional but reassuring ("less painful," "fall in love with your doctor's office").

The **primary logo is the co-brand lockup "amazon one medical"** — "amazon" with its smile-arrow in squid-ink, "one medical" in health-green (extracted from the nav `<svg>`, viewBox 1083.2×168.9; re-confirmed in the 2026-06-15 rawHtml; see `assets/wordmark.svg`). The standalone square mark is the **5-dot teal "+" symbol** (apple-touch-icon, 180px, on a baked white ground). The Amazon co-brand sits *in the logotype itself*, not just the footer — a visible signal of how far the acquisition has folded the brand into Amazon Health. *(The blind, cited `visual.md` is the authoritative visual layer — this is the lightweight read.)*

## Strategic read

The interesting structure is the **double monetization**: a recurring membership fee layered on top of normal insurance billing — One Medical gets paid to be your front door *and* gets reimbursed for walking you through it. Post-acquisition, Amazon has bolted **two distribution rails** onto that base: the **Prime $99/yr (or $9/mo) bundle** — half the standard $199, aimed at converting Prime's enormous base into primary-care members at a price concierge medicine can't match — and **On-Demand Care** ($29/$49, self-pay, sold through Amazon.com), a no-membership, no-insurance front door that monetizes the people who'll never live near an office. The portfolio braids four payer models under one brand — consumer subscription, employer contracts, value-based Medicare (Iora), and Amazon-channel cash-pay per-visit — which is why "primary care" undersells it; the economics differ sharply by segment.

For a DTC telehealth comparison set, One Medical is the **bricks-and-mortar, insurance-integrated** end of the spectrum (offices, on-site labs, in-network billing), the opposite of cash-pay, ship-to-door compounded-Rx models — and now an Amazon-distributed one. The one place it *does* converge with the cohort is the new **On-Demand Care** line: a self-pay, FSA/HSA, async/video one-off visit looks much more like the rest of the cohort than One Medical's core membership does.

## Provenance

- **Pages:** 13 captured via Firecrawl across two hosts — onemedical.com: homepage (rich pass: markdown/html/rawHtml/links/branding/images/screenshot), membership, about-us, insurance, virtual-care, services, faq, sixty-five-plus, business, services/mindset, kids; health.amazon.com: /onemedical, /prime. Map returned 478 URLs (~90% /locations + /providers noise); key pages selected from homepage links.
- **Verify:** all 13 sourceURLs matched requested URLs; all 13 body md5s unique — no geo/cache contamination; no junk soft-404s.
- **Credits:** 14 (1 map + 13 scrapes), basic proxy throughout (incl. the two Amazon-host pages).
- **Couldn't get:** per-visit copay/deductible amounts (insurance-plan-dependent); enterprise/employer pricing ("Get in touch"); current authoritative employer-client count (8,500+ vs 11,600+ conflict). *(Prior run's "pay-per-visit flat fee" gap is now resolved — On-Demand Care is $29 messaging / $49 video.)*
- **Structured layer (schema 2.6):** no JSON-LD on the homepage (absent, not skipped); `socials` + `legal_entity` (1Life Healthcare, Inc.) read from the footer; nav hierarchy recovered from the `<nav>` region (`fc.py signals`) and validated against the homepage screenshot.
- **Run profile:** guided/express refresh (over a still-recent 2026-06-02/04 base, forced by the user) — full 13-page re-capture that **adds the health.amazon.com surface** (onemedical + prime) the prior run never processed, resolving the On-Demand Care pricing and surfacing the $9/mo + $66/yr-family tiers. +logos (co-brand wordmark re-confirmed against fresh rawHtml; logomark/og re-measured), +offerings.md, +telehealth.md, +visual.md (new this run). Re-stamped 2.5→2.6 (promoted `legal_entity` out of `aliases`). **Product-render images N/A** — One Medical is a service; pages carry only lifestyle/illustration, no clean isolated product shot.
- **Enriched (model knowledge):** parent Amazon = NASDAQ AMZN; One Medical founded 2007 by Tom Lee (founder not on captured pages; "past 15 years" on /about corroborates ~2007).
