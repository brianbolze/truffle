---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: getopt.com
name: Opt Health
aliases: [OptHealth]                  # handed-in name; the brand styles itself "Opt Health" (footer ©), domain is getopt.com
parent: []
owns: []
socials: { facebook: "https://www.facebook.com/GetOptHealth", instagram: "https://www.instagram.com/opt_health/", linkedin: "https://www.linkedin.com/company/opt-health/", youtube: "https://www.youtube.com/@opt_health" }  # footer anchors (no JSON-LD on homepage)
external: {}                          # no JSON-LD sameAs / third-party records found on the captured pages

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress on WP Engine (rawHtml: wp-content + wp-json; footnote assets served from opthealth2.wpenginepowered.com; branding.designSystem said 'bootstrap' — ignored). No JSON-LD on the homepage (socials came from footer anchors); no og:image declared. SPA-ish hydration: /how-it-works and /faq return thin markdown (content is in the screenshot, not the md). Pricing: the 3 membership tiers render server-side and clean on /memberships; treatment/medication pricing is gated (in-app at app.getopt.com, or 'contact us to inquire' for peptides). Men's site is getopt.com root; a parallel WOMEN'S vertical lives under /women/* (own how-it-works, memberships, medical-experts, protocols). Commerce + member app on app.getopt.com (signup/dashboard). City landing pages: /los-angeles /austin /dallas /tampa /orlando. At-home nurse blood draws limited to SF, LA, San Diego, NYC; elsewhere 2,000+ partner labs."
key_pages:
  memberships: /memberships
  how_it_works: /how-it-works
  about: /about-us
  medical_team: /medical-team
  trt: /learn/protocols/testosterone-replacement-therapy
  ed: /learn/protocols/erectile-dysfunction
  peptides: /learn/protocols/peptide-therapy
  faq: /faq
  women: /women
  women_memberships: /women/memberships
unverified_fields:
  - "Treatment/medication pricing (TRT meds, peptides, ED, weight-loss/semaglutide) — gated in-app or 'contact us to inquire'; only the 3 membership-tier prices are public."
  - "Medical-director title varies by page: Jeremie Walker, MD is 'Medical Director' on the men's homepage but 'Opt Health Physician' on /medical-team; Graham Simpson, MD is 'Medical Director' on /women and /about (he is not on the /medical-team roster). Likely men's- vs women's-track leads."
  - "Self-reported impact stats — '+5k Patients served,' '99% Satisfaction,' '+15k Telehealth consultations,' 'Customers rate us 5.0' (/about-us, homepage) — company-stated, unverified."
  - "Women's-vertical membership pricing not separately captured (/women/memberships not pulled); the women's line is assumed to mirror the men's 3 tiers, unverified."
  - "Founder, founding date, headcount, funding, HQ entity beyond '595 Pacific Ave, Floor 4, San Francisco, CA 94133' — not on the marketing site (deep-research job)."

description: "A concierge telehealth membership delivering longevity and hormone-optimization care to adults — led by men's health — pairing 55+ biomarker lab panels with video physician consults to personalize TRT, peptides, and meds shipped from its own pharmacy."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — "opt health" logotype, extracted from the inline data-URI SVG in branding.images.logo
logos:                               # 2.5 module — measured by fc.py logos; the consumer applies the size bar
  wordmark: { src: assets/wordmark.svg, w: 118, h: 24 }                                                            # "opt health" logotype, single-color brand-blue #273DFF (invisible on a blue ground)
  logomark: { src: "https://getopt.com/wp-content/uploads/2024/07/opt-brand-300x300.jpg", px: 300, transparent: false }  # lowercase "opt" mark w/ pixel-cross on the 't', blue on WHITE (JPG → baked opaque box)
  # og: omitted — no og:image declared on the homepage (true absence)
brand_colors: { primary: "#273DFF", background: "#FFFFFF" }  # STRAIN: electric/royal blue #273DFF is the verified brand hue (hero card, CTA pills, footer band, the wordmark itself); occasional red accent arrows
fonts: [Saans]                       # Saans (headings + body), Arial fallback — branding.fonts[0]
color_scheme: light
design_framework: wordpress          # rawHtml: wp-content + wp-json (WP Engine); branding.designSystem said "bootstrap" (ignored per the always-wrong rule)
---

## Overview

Opt Health (getopt.com) is a **concierge, membership-based telehealth clinic** for health optimization and longevity — "personalized healthcare to get into the best shape of your life." It sells a **tiered annual-style membership** (billed monthly) in which a dedicated **Opt Health physician** reviews a **pro-athlete-level blood panel of 55+ biomarkers**, builds a 1:1 personalized plan, and ships prescribed medications, peptides, and supplements to the member's door, with quarterly retesting and an app-tracked **Opt Performance Score** (a composite across six pillars: sleep, stress, hormones, exercise, inflammation, nutrition). The brand leads with **men's hormone optimization** (TRT is the flagship treatment) but runs a full **parallel women's vertical** (`/women`) for peri/menopause HRT and longevity. Framing is longevity-first — "Be 55. Feel 35.," "healthcare, not sick care," and a stated **"4-P's of Proactive Medicine: Personalized, Predictive, Preventative, Participatory."** HQ: 595 Pacific Ave, Floor 4, San Francisco, CA 94133 (©2026 Opt Health). Founder/founding date are not on the site.

## What they offer

A 3-tier membership is the priced core; specific treatments are **personalized and gated by tier** (or à-la-carte at additional in-app fees). Bold-led lines, prices verbatim + a price-visibility token:

- **Membership — Foundation:** **$95/month** (after a one-time intake + lab fee of **$195**) — 55+ biomarker labs, a 60-min physician consult + plan, up to 2 supplements shipped 4×/yr, 2×/yr follow-up labs, the Performance Score dashboard + app chat; access to *order* medications (peptides, hair-loss, ED, etc.) at additional fees `[published]`
- **Membership — Optimization:** **$245/month** (after **$195** intake + lab fee), "MOST POPULAR" — everything in Foundation + up to 3 supplements and **2 membership medications**, and **specialized prescriptions included** (hormone imbalances, fatigue, sleep/energy, weight loss, fertility), 4×/yr follow-up labs `[published]`
- **Membership — Longevity:** **$645/month** (after **$695** intake + lab fee) — everything in Optimization + 65+ biomarkers and **epigenetic / biological-age testing** (2×/yr), a 90-min consult, discounted CAC/cognitive/leaky-gut/heavy-metal tests `[published]`
- **Hormone optimization / TRT (flagship):** testosterone as injection, oral, or topical cream; "offered… as part of our Optimization and Longevity plans, **starting at $245 per month plus a $195 initial lab fee**" — molecule stated only as "testosterone" (ester not stated) `[partial]`
- **Peptide therapy:** "over a dozen peptides," page-named — **Sermorelin, PT-141 (nasal spray), Semaglutide (GLP-1), Oxytocin, GHK-Cu, VIP, Pinealon, Hexarelin, 5-amino-1MQ** (+ Ipamorelin/CJC-1295/Kisspeptin/Thymosin-α1/Epithalon in body copy); injection, nasal spray, or oral; **"contact us to inquire about pricing"** `[on-request]`
- **Erectile dysfunction:** PDE5-inhibitor medications (specific molecule not stated), diagnosed and prescribed online `[on-request]`
- **Weight loss:** Semaglutide (GLP-1) + metabolic support, framed under the "Weight Loss" / "Improve Body Composition" program goals `[on-request]`
- **Supplements & micronutrients (included by tier):** Vitamin D3, D3+K2, Omega-3, DHEA, Zinc, Magnesium, Clomiphene, Thyroid (T3/T4), Testosterone appear in the treatment grid — Foundation includes up to 2, Optimization up to 3 `[partial]`
- **Women's vertical (`/women`):** a parallel membership for peri/menopause — Hormone Replacement Therapy (HRT), Longevity Medicine, Peptide Therapy, across 8 program goals (radiant skin, improved physique, longevity, sleep, weight loss, sexual well-being, bone strength, hair loss); pricing not separately captured `[on-request]`

Per-SKU/per-molecule roster + tier-gating detail in `offerings.md`; telehealth-specific cuts in `telehealth.md`.

## How it works / model

A four-step concierge journey: (1) **Discover your baseline** — an at-home or partner-lab blood draw of 55+ biomarkers (65+ on Longevity); (2) **Pick your membership** and meet 1:1 by **video** with an Opt physician (HIPAA-compliant telemedicine) who reviews labs and builds a personalized plan; (3) **Get your treatments** — medications, peptides, and supplements shipped quarterly "from our pharmacy"; (4) **Live better, longer** — every 3–4 months retest + a focused consult to adjust, with 24/7 care-team chat and an app-tracked Performance Score (updated bi-weekly, integrates Apple Watch/Garmin/Fitbit). Revenue is **subscription** (the membership), with medication/treatment/extra-diagnostic fees on top; **membership is required to receive treatment** ("our memberships ensure continuity of care").

## Positioning & audience

Targets health-conscious, higher-income adults (broadly 40+) who want proactive optimization rather than reactive "sick care" — "Be 55. Feel 35." The wedge is **comprehensive diagnostics + a dedicated physician relationship** (55+ biomarkers, 1:1 non-rushed consults, a longevity/anti-aging treatment stack), positioned against both rushed in-person primary care and lighter DTC "wellness" telehealth. **Men's health is the front door** (TRT, ED, peptides; testimonials and hero skew male), with a fully built **women's** track for menopause/HRT. Explicit outreach to **military / veterans / first responders** (a dedicated discount page) and a **California Police Chiefs Association** partnership. Concierge tone: "elite healthcare, made personal."

## Nav structure

```
- [Men / Women toggle]  — default Men (getopt.com); Women switches to /women/*
- How it Works — /how-it-works
- Memberships — /memberships
- Medical Experts — /medical-team
- Program Goals — (flyout)
  - More Energy — /program-goals/more-energy  ("hormone therapy, peptides, and personalized meds")
  - Improve Body Composition — /program-goals/improve-body-composition
  - Lower Biological Age — /program-goals/lower-biological-age
  - Better Sleep — /program-goals/better-sleep
  - Weight Loss — /program-goals/lose-weight
- Learn — /learn  (flyout)
  - Protocols — /learn/protocols
    - TRT — /learn/protocols/testosterone-replacement-therapy
    - Erectile Dysfunction — /learn/protocols/erectile-dysfunction
    - Peptide Therapy — /learn/protocols/peptide-therapy
  - Healthy Living — /learn/healthy-living
  - Medically Reviewed — /learn/medically-reviewed
  - Patient Journeys — /learn/patient-journeys
- Get Started — app.getopt.com/signup   ·   Goto Dashboard — app.getopt.com/dashboard
- Call for a free consultation: 855-409-7235
Footer — Popular: TRT, Peptides, Get Started, Medical Experts · About: About Us /about-us,
  Military Veteran/First Responder /military-veteran-first-responder, Careers /careers,
  Reviews /reviews, Privacy /privacy-policy, Terms /terms-of-use · Program Goals (as above) ·
  Learn (as above) · Contact: Need Help /contact-us, FAQs /faq
Women's vertical (/women) mirrors: /women/how-it-works, /women/memberships, /women/medical-experts,
  /women/waitlist, + women's protocols (HRT /learn/protocols/hrt, radiant-skin, bone-strength,
  sexual-well-being, woman-hair-loss) and program goals (women-longevity, women-weight-loss, …)
City landing pages: /los-angeles · /austin · /dallas · /tampa · /orlando
```

## Credibility & proof

- **Named, credentialed medical team:** a full `/medical-team` page with 7+ physicians and detailed bios — **John Tidwell, MD** (CMO; orthopaedic trauma surgeon, BHRT-L1 cert from the Academy of Preventive & Innovative Medicine, A4M training), **Jeremie Walker, MD, MBA**, **Anna Fleytman-Pope, DO** (integrative medicine), **Danny Molinar, MD** (family medicine, EN/ES), **Alejandro Arenas, MD**, **Samuel Sarmiento, MD, MPH, MBA** (contributor), **Vinay Bhamidipati, MD, MPH**; **Graham Simpson, MD** leads the women's track. A strong trust signal for a prescribing telehealth brand.
- **Physician certification (verbatim):** physicians hold "advanced training accredited by the prestigious **ABHRT Certification** program."
- **Self-reported metrics (flagged self-reported):** "**+5k** Patients served," "**99%** Satisfaction," "**+15k** Telehealth consultations" (/about-us); "Customers rate us **5.0**" (homepage/women).
- **Platform / compliance:** "HIPAA-compliant telemedicine platform"; care team "available 7 days a week" / "24/7" via the app.
- **Testimonials:** named first-name + last-initial "Verified user" quotes (men on the main site, women on /women), plus a named public figure (sales coach Ian Koniak).
- **Segments / partnerships:** Military/Veteran/First-Responder program; California Police Chiefs Association.
- *No LegitScript seal or pharmacy accreditation (PCAB/NABP) was observed on the captured pages — absence on these pages, not proof of none.*

## Visual & brand impression

Polished, modern health-tech — confident and well-funded, not an MVP. The identity rides a single **electric/royal blue (#273DFF)** against generous white space: a blue hero card ("Opt into a Better You") over an aspirational lifestyle photo, blue pill CTAs, and a full-width deep-blue footer carrying the **"opt health"** wordmark in white. The mark is a lowercase, geometric **"opt"** with a pixel-cross motif on the "t" (a subtle data/tech cue), and the wordmark logotype is the same brand blue. Typography is a clean geometric sans (**Saans**), reinforcing a precise, data-driven feel; recurring **Opt Score** dashboard cards (e.g. "89/100") and biomarker UI mockups sell the quantified-self proposition. Tone reads premium-clinical-meets-lifestyle — closer to a longevity-tech startup than a sterile clinic.

## Provenance

- **Pages:** homepage (rich pass: markdown/html/rawHtml/links/branding/images/screenshot) + memberships (rich pass), how-it-works, about-us, medical-team, faq, /learn/protocols/{testosterone-replacement-therapy, erectile-dysfunction, peptide-therapy}, women (10 pages total) — Firecrawl `maxAge:0`, `location:US`, `waitFor:3500`.
- **Verify:** all 10 sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 11 (1 map + 10 scrapes; all base, no proxy escalation).
- **Couldn't get:** treatment/medication pricing (gated in-app / "contact us"); women's-vertical membership pricing (/women/memberships not pulled); founder/founding/headcount/funding (not on site); per-protocol pages for weight-loss & hair-loss (characterized from the treatment grids + peptides page).
- **Structured layer (schema 2.2):** no `application/ld+json` on the homepage → `socials` taken from footer anchors, `external` empty, `aliases` not enriched from `alternateName`. Nav region (`<nav>`) sliced via `fc.py signals` and validated against the homepage screenshot.
- **Run profile:** Express invocation (intent pre-carried; step-2.5 question batch skipped). +offerings, +telehealth, +logos — all three opt-in modules. Logos: wordmark extracted from the inline data-URI SVG in `branding.images.logo` (committed to `assets/wordmark.svg`, single-color brand blue); logomark measured by `fc.py logos` (`transparent: false` — JPG with a baked white box); og slot omitted (no `og:image` declared). Stamped 2.5.
