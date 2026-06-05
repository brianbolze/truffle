---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: onemedical.com
name: One Medical
aliases: ["1Life Healthcare, Inc.", "Amazon One Medical", "www.onemedical.com"]   # ©2026 1Life Healthcare, Inc.; social handles use "amazononemedical"
parent: [amazon.com]                 # Amazon completed acquisition 2023-02-22 (/about-us)
owns: []                             # acquired Iora Health (2021) — fully absorbed into the seniors line, no standalone site
socials:
  facebook: https://www.facebook.com/amazononemedical
  x: https://twitter.com/onemedical
  instagram: https://www.instagram.com/amazononemedical/
  youtube: https://www.youtube.com/channel/UCVuDmERByiofU8ss3Nz_Odw/featured
  linkedin: https://www.linkedin.com/company/one-medical-group
external: {}                         # no JSON-LD on homepage; no third-party records linked (looked, none found)

# Capture meta
captured_at: 2026-06-02
capture_method: firecrawl
site_notes: "Map is 484 URLs but ~90% noise — hundreds of /locations/<metro>/<office> + /providers/<name>; signal lives under /services/*, /membership, /sixty-five-plus, /business, /about-us, /virtual-care, /insurance (pull from homepage links, not the map). No JSON-LD on homepage. Pricing is split: standard membership $199/yr lives on /membership; the $99/yr hero on the homepage is the Amazon Prime price. Employer-client count drifts by page (8,500+ on /about & /business vs 11,600+ on homepage) — report both, don't reconcile. Wagtail/Django backend (image renditions `*.fill-WxH.jpg`/`.original.png` under /media/images/); branding.designSystem.framework='unknown' (ignored). Stack: GTM, Sentry, Wistia, NICE inContact chat."
key_pages:
  membership: /membership/
  seniors: /sixty-five-plus/
  business: /business/
  services: /services/
  about: /about-us/
  virtual_care: /virtual-care/
  insurance: /insurance/
unverified_fields:
  - "Two membership prices both live: standard $199/yr (/membership) and Amazon Prime $99/yr (homepage) — captured verbatim, not reconciled."
  - "Employer-client count conflicts across pages: '8,500+' (/about-us, /business) vs '11,600+ companies' (homepage). Both verbatim."
  - "Footprint metrics differ by page: 'nineteen major U.S. cities' (/about-us) vs '125+ offices' (/sixty-five-plus) — different measures, both verbatim."
  - "Pay-per-visit (one-time virtual visit) flat fee not shown — gated to an Amazon pay-per-visit page not captured."

# Description — one sentence
description: "Membership-based primary care practice, owned by Amazon, that blends app-first 24/7 virtual care with in-office visits across U.S. cities; it charges an annual membership on top of billing your insurance per visit, and sells the same care as an employer benefit and to Medicare seniors."

# Classification
entity_type: Company
target_market: [B2C, B2B, B2B2C]
offering_category: [Services / Consulting]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — the live co-brand "amazon one medical" lockup, extracted inline <svg> from rawHtml (branding.images.logo empty)
logos:                               # 2.5 module — co-brand lockup is the current primary mark; "amazon" smile-arrow in ink + "one medical" in health-green
  wordmark: { src: assets/wordmark.svg, w: 1083, h: 169 }                                                          # rectangle "amazon one medical" lockup (viewBox 1083.2×168.9); CSS-token fills inlined for portability
  logomark: { src: "https://www.onemedical.com/static/images/apple-touch-icon-180x180.png", px: 180, transparent: false }   # the 5-dot teal "+" mark on a BAKED WHITE square (beats the 152px google-s2; hasAlpha lies)
  og:       { src: "https://www.onemedical.com/media/images/240610_OM-Homepage-Open-Graph_1.2e16d0ba.fill-1200x630.png", w: 1200, h: 630 }   # declared og:image, verified 1200×630
brand_colors: { primary: "#004D49", secondary: "#068466", accent: "#005450" }   # deep teal-green identity, white ground
fonts: [Ginto, GT Super Display]     # branding ranked generic "sans-serif" first; real faces are Ginto (sans) + GT Super Display (serif)
color_scheme: light
design_framework: wagtail            # Django/Wagtail — inferred from /media/images/*.fill-* + .original renditions in rawHtml (no Next/React/WP markers)
---

## Overview

One Medical is a membership-based primary care practice — "a modern approach to primary care" built around same/next-day appointments, longer visits, calming offices, and an app that delivers 24/7 virtual care. Members pay an annual fee for the experience and access; actual visits are billed to insurance just like a normal doctor's office, so the membership sits *on top of* fee-for-service care rather than replacing it. The practice spans both a direct-to-consumer membership and a large employer-benefits business, plus a distinct value-based primary-care line for Medicare seniors (the Iora Health business it acquired in 2021). Amazon completed its acquisition of One Medical on **February 22, 2023**, making it Amazon's bricks-and-mortar primary-care arm alongside Amazon Pharmacy and Amazon Health.

## What they offer

One core service — membership primary care — sold to several buyer segments, with branded sub-programs as companions (bold lead-in, price + visibility token per line):

- **Consumer membership (Adults under 65):** annual membership for app-first primary care; works with your insurance. **"$199 a year"** standard `[published]`; **"$99/year"** for Amazon Prime members `[published]` — /membership, homepage
- **Seniors primary care (Adults 65+):** "relationship-based primary care for adults on Medicare" — the value-based Iora line; "works with your insurance (yes, including Medicare)." No separate fee shown `[on-request]` — /sixty-five-plus
- **One Medical for Business (employer benefit):** the same in-office + 24/7 virtual care sold to employers; enterprise pricing via "Get in touch" `[on-request]` — /business
- **Virtual care:** 24/7 on-demand message/video care "included in Membership," plus a one-time **Pay-per-visit** virtual visit "for a flat fee" (Amazon pay-per-visit); flat fee not shown `[on-request]` — /virtual-care
- **One Medical Kids:** pediatric and family care `[on-request]` — /services/kids
- **Mindset by One Medical:** integrated mental health — assessments, coaching, therapy, behavioral-health screenings; bundled into membership / employer plans `[partial]` — /services/mindset
- **Impact by One Medical:** chronic-condition management & prevention program (diabetes, hypertension, obesity) `[on-request]` — /services/chronic-conditions

Care breadth under **Services**: wellness & prevention, everyday care, chronic conditions, mental health, LGBTQIA+ care, urgent concerns, sexual health, annual "Annual Wellness Visit," and **drop-in lab services** at offices.

## How it works / model

Membership + insurance, two revenue streams stacked. You pay the annual membership ($199/yr, or $99/yr via Amazon Prime) → use the app for 24/7 virtual care (Video Chat / "Treat Me Now" / secure messaging) at no extra cost → book in-office or scheduled video visits, which are **billed to you/your insurance** (copays and deductibles apply). So One Medical earns the recurring membership fee *and* fee-for-service reimbursement on scheduled visits. The **seniors** business runs on a different economic model — value-based / Medicare primary care inherited from Iora Health (47 offices across ten markets at acquisition). The **employer** business contracts per-employee health benefits ("11,600+ companies" / "8,500+ organizations"). The **Amazon Prime** channel ($99/yr) is the distribution lever post-acquisition, funneling Prime's membership base into One Medical.

## Positioning & audience

Tagline: **"Fall in love with your doctor's office"** / "Comprehensive healthcare just got less painful." Targets consumers fed up with traditional primary care — appointments that start on time, longer visits "so you don't feel rushed," calming offices "near where they work, live, and shop," and an app-first experience. Positions on **human-centered design + technology + an exceptional team**, against both conventional PCP offices and lighter "wellness" telehealth. Three audiences: individual consumers (under-65 membership), Medicare seniors, and employers buying it as a benefit. Post-2023 it is also Amazon's primary-care surface, cross-sold with Amazon Pharmacy.

## Nav structure

```
- Locations
  - Offices — /locations/
  - Virtual Care — /virtual-care/
- For You
  - Adults under 65 — /membership/
  - Adults 65+ — /sixty-five-plus/
  - Kids — /services/kids/
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
- Providers — /providers/ · Services — /services/ · Blog — /blog/
- Give a membership — /gift/ · Careers — careers.onemedical.com
- Media center — /mediacenter/ · About — /about-us/ · Sponsored membership — /sponsored-membership/
- Contact us — /contact-us/ · FAQ — /faq/
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

Clean, calm, premium-consumer healthcare aesthetic — deep teal-green (`#004D49`) as the brand hue against generous white space, with a friendly editorial serif (GT Super Display) for headlines over a geometric sans (Ginto) for body. Illustration-led (soft human figures rather than clinical stock photography), warm and approachable rather than sterile. The design reads as mature and well-funded — consistent with a 15-year-old brand now resourced by Amazon. Tone is professional but reassuring ("less painful," "fall in love with your doctor's office").

The **primary logo is now the co-brand lockup "amazon one medical"** — "amazon" with its smile-arrow in dark ink, "one medical" in health-green (extracted from the nav `<svg>`, viewBox 1083.2×168.9; see `assets/wordmark.svg`). The standalone square mark is the **5-dot teal "+" symbol** (apple-touch-icon, 180px, on a baked white ground). The Amazon co-brand sits *in the logotype itself*, not just the footer — a visible signal of how far the acquisition has folded the brand into Amazon Health.

## Strategic read

The interesting structure is the **double monetization**: a recurring membership fee layered on top of normal insurance billing — One Medical gets paid to be your front door *and* gets reimbursed for walking you through it. That, plus the **Amazon Prime $99/yr bundle**, is the post-acquisition growth engine: convert Prime's enormous membership base into primary-care members at a price (halved from $199) that traditional concierge medicine can't match. The portfolio actually braids three different payer models under one brand — consumer subscription, employer contracts, and value-based Medicare (Iora) — which is why "primary care" undersells it; the economics differ sharply by segment. For a DTC telehealth comparison set, One Medical is the **bricks-and-mortar, insurance-integrated** end of the spectrum (offices, labs, in-network billing), the opposite of cash-pay, ship-to-door compounded-Rx models — and now an Amazon-distributed one.

## Provenance

- **Pages:** 8 captured via Firecrawl (homepage + membership, sixty-five-plus/seniors, business, services, about-us, virtual-care, insurance); map returned 484 URLs (~90% /locations + /providers noise), key pages selected from homepage links.
- **Verify:** all 8 sourceURLs matched requested URLs; all 8 body md5s unique — no geo/cache contamination.
- **Credits:** 9 (1 map + 8 scrapes), basic proxy throughout.
- **Couldn't get:** Pay-per-visit flat fee (gated to /amazon/pay-per-visit/, not captured); current authoritative employer-client count (8,500+ vs 11,600+ conflict); per-visit copay amounts (insurance-dependent).
- **Run profile:** guided/express — +logos (2.5: extracted the live **"amazon one medical"** co-brand wordmark to `assets/wordmark.svg`, measured logomark/og from the 2026-06-02 homepage payload — no re-scrape); +offerings.md and +telehealth.md cohort pack, both off a reused 2026-06-02 base capture plus 4 new program-page scrapes on 2026-06-04 (mindset, chronic-conditions, kids, lab-services → `captures/2026-06-04/`). Profile body itself not re-captured (2-day-warm). **Product-render images requested but N/A** — One Medical is a service; pages carry only lifestyle/illustration (exam rooms, phlebotomist, family), no clean isolated product shot to capture.
- **Enriched (model knowledge):** parent Amazon = NASDAQ AMZN; One Medical founded 2007 by Tom Lee (founder not on captured pages; "past 15 years" on /about corroborates ~2007).
