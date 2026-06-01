---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: marekhealth.com
name: Marek Health
aliases: ["Marek Health LLC"]        # JSON-LD legalName
parent: []
owns: ["marekdiagnostics.com"]   # "Diagnostic Labs" sibling brand on its own domain (footer link); same family, ownership not stated explicitly
socials: { facebook: "https://www.facebook.com/marekhealth/", instagram: "https://www.instagram.com/marekhealth", x: "https://twitter.com/marekhealth" }   # JSON-LD sameAs (footer-verified)

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js (rawHtml __NEXT_DATA__ + /_next/). Mega-nav is JS-walled — header items (Treatments / Diagnostic Labs / Education / Shop) all collapse to '/' in markdown; the real offering taxonomy is the 10 homepage goal tiles, not the nav. Map returns 424 URLs but ~90% noise: single-word influencer/affiliate landing slugs (/troponin, /syatt, /mpmd, /mattchan…), /team-marek/* coach bios, /apparel/* merch — treatment routes come from homepage goal tiles. Consumer per-treatment & per-lab pricing sits behind the intake/login; only the $299 intake fee + $450 minimum lab-panel spend are public. Diagnostic labs live on sibling domain marekdiagnostics.com. Founder is 'Derek' / MPMD ('More Plates More Dates' YouTuber) — brand carries his audience + an athletic/bodybuilding optimization slant."
key_pages:
  about: /about-marek
  testosterone: /testosterone
  weight_loss: /weight-loss
  sexual_health: /sexual-health
  performance: /performance
  coaching_partnership: /cpp
  coaching: /team-marek
  faqs: /faqs
  testimonials: /testimonials
unverified_fields:
  - "Per-treatment & per-SKU consumer pricing — behind the intake flow/login; only the public $299 intake fee and $450 minimum lab-panel spend are quoted."
  - "Specific prescription SKUs per treatment area — product pages are goal/condition landing pages, not SKU lists; medications named only generically (TRT, GLP-1, ED, peptides)."
  - "Ownership/legal relationship to marekdiagnostics.com — sibling brand on its own domain, relationship not stated."
  - "Headcount, funding, revenue — not on a marketing site (deep-research, not capture)."

description: "A telehealth optimization platform pairing advanced diagnostic lab work with 1-on-1 health coaching and partnered-clinician prescriptions, delivering hormone, weight-loss, sexual-health and longevity protocols billed à la carte rather than as fixed subscriptions."

# Classification
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription   # STRAIN: recurring coaching check-ins + medication refills + repeat labs are subscription-like, BUT Marek explicitly rejects "set subscription plans" — bills à la carte (one-time $299 intake, then per-lab/per-treatment), cancel anytime
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://images.marekhealth.com/website_assets/homepage/marek-health-desktop-logo-dark.webp
brand_colors: { primary: "#BB433C", accent: "#BE433C" }   # STRAIN: a single red (≈#BB433C) carries both brand mark + CTAs over a near-black #151515 ground with white text — verified vs screenshot; the two "slots" are the same hue
fonts: [Montserrat, Inter]   # Montserrat headings, Inter body (branding payload)
color_scheme: dark
design_framework: next.js   # rawHtml has __NEXT_DATA__ + /_next/; branding.designSystem said "custom" (wrong, as usual)
---

## Overview

Marek Health is a telehealth **platform for health optimization** — explicitly *not* a clinic. It connects clients with partnered, "pragmatic" medical providers and assigns each a 1-on-1 health coach, building data-driven protocols off advanced diagnostic lab work. The flow centers on a branded **Guided Optimization®** program: an intake assessment, an in-depth lab panel, a provider consult, and clinician-prescribed treatments (hormones, peptides, GLP-1s, supplements) shipped to the door, with ongoing monthly coach check-ins. It spans ten consumer treatment goals plus a B2B white-label arm for coaches. The brand grew out of founder "Derek" (the MPMD / *More Plates More Dates* YouTube channel) and openly serves a performance/optimization audience — comfortable with "high-leverage therapeutics" that mainstream telehealth shies from. Claims **50,000+ clients transformed**.

## What they offer

Multi-product, organized as ten goal-oriented treatment areas (clinician-prescribed; per-SKU detail behind intake — defers to `offerings.md`). TRT is the origin and spine of the funnel:

- **Optimize your testosterone (TRT):** `/testosterone` — the flagship line; "Testosterone Replacement Therapy," the most-developed page.
- **Improve weight loss:** `/weight-loss` — body-recomposition + weight-loss protocols (GLP-1 class implied).
- **Increase your libido / sexual health:** `/sexual-health` — ED + sexual-health optimization.
- **Perform better:** `/performance` — athletic/peak-performance optimization ("Are you an elite athlete?").
- **Look younger:** `/look-younger` — aesthetic/longevity.
- **Hair loss prevention:** `/hair-loss`
- **Remove brain fog:** `/think-sharper` — cognitive health.
- **Sleep better:** `/sleep-better`
- **Better heart health:** `/heart-health`
- **Fertility:** `/fertility`

Plus the platform pillars and adjacent lines:

- **Diagnostic Labs:** advanced lab panels are the wedge — most journeys start here; run under sibling brand **marekdiagnostics.com**. Panels referenced: **Comprehensive ($455)** and **Complete ($855)** ("your cost" — coach-facing).
- **1-on-1 Health Coaching:** assigned coach ("health strategist") who builds and refines the protocol; the recurring core.
- **Coaching Partnership Program (CPP):** `/cpp` — **B2B white-label** lab testing + concierge coaching for fitness/health professionals; "You remain the expert in nutrition and training." Pitched as a revenue line for coaches ("net $5,000–$15,000 per month").
- **Shop / Apparel + supplements:** merch (`/apparel/*`) and targeted OTC supplements.

**Pricing (verbatim, public surface only):**
- **Guided Optimization intake — "$299":** intake assessment = coach session + in-depth lab analysis + 25-min licensed-provider consult + access to Marek's pharmacies/dispensaries + ongoing monthly care.
- **Lab panel minimum — "minimum $450 lab panel purchase required":** to unlock the discounted advanced lab testing at intake.
- **CPP panels — "$455 & $855 your cost":** Comprehensive and Complete lab panels (coach-facing wholesale).

## How it works / model

Four-step journey: **(1)** book a 1-on-1 video intake with a Marek Health Coach → **(2)** personalized diagnostic lab work (results in ~14 days with a written review) → **(3)** video consult with a partnered medical provider to set the treatment plan → **(4)** treatments shipped to the door, then monthly coach check-ins, refills, and follow-up labs. Revenue = the $299 intake + lab-panel sales + ongoing coaching + medication/supplement sales. Marek **explicitly rejects fixed subscription plans** ("we don't offer any set subscription plans and you can cancel whenever") — care is billed à la carte and adapted over time, though the monthly-check-in + refill cadence is economically subscription-like. Critically, Marek positions itself as a *connector platform*, not a provider: "Marek Health is not a healthcare clinic… a platform that connects clients with highly specialized healthcare providers." US residents only. No insurance billed (direct-pay; FSA/HSA accepted, no CPT/ICD codes provided).

## Positioning & audience

Targets self-directed "human optimization" seekers — people already researching peak performance on forums who want clinician oversight instead of guessing. Male-leaning and athletic/bodybuilding-coded (the testosterone page runs "Masculinity is in crisis"; recommenders are IFBB pros, UFC fighters, strength coaches), but **not men-only** — testimonials and before/afters include women. The claimed edge: a **comprehensive, labs-first, data-driven** approach (vs. "diagnose-and-offload-a-prescription" telehealth), partnered providers who are themselves optimizers and comfortable with "high-leverage therapeutics," and a real coaching relationship. Implicit competitive set is the DTC men's-health / optimization field (Hone, Maximus, PeterMD, Hims) — Marek differentiates on coaching depth, diagnostic rigor, and an unapologetic performance stance.

## Nav structure

Header mega-nav is JS-walled (items collapse to `/` in markdown); offering taxonomy reconstructed from the homepage goal tiles + footer.

```
- Treatments (mega-nav, JS-walled) — goal tiles:
  - Optimize your testosterone — /testosterone
  - Hair loss prevention — /hair-loss
  - Improve weight loss — /weight-loss
  - Look younger — /look-younger
  - Increase your libido — /sexual-health
  - Remove brain fog — /think-sharper
  - Sleep better — /sleep-better
  - Perform better — /performance
  - Better heart health — /heart-health
  - Fertility — /fertility
- Diagnostic Labs — marekdiagnostics.com
- Coaching — /team-marek
- Education (JS-walled)
- FAQs — /faqs
- Testimonials — /testimonials
- Shop / Apparel — /apparel/*
- Coaching Partnership Program (B2B) — /cpp
- Footer → Services:
  - Guided Optimization — /sign-up
  - Diagnostic Labs — marekdiagnostics.com
  - Partnership Program — coaching@marekhealth.com
```

## Credibility & proof

- **Scale claim:** "50,000+ Marek Health clients transformed"; 10-week before/after transformation grid on the homepage.
- **Founder/audience:** founded by Derek (MPMD / *More Plates More Dates*); "Featured On" logo wall of podcasts where staff appeared (Joe Rogan Experience, Jordan Peterson, Modern Wisdom, Impact Theory, Mark Manson, Power Project, etc.).
- **Recommenders:** named athlete/coach endorsers — Stan Efferding, Jordan Syatt, Sean Brady (UFC), Samson Dauda & Derek Lunsford & Keone Pearson (IFBB pros), Craig Jones (BJJ), Ali Gilbert.
- **Reviews:** long first-person 5-star testimonials across pages; dedicated `/testimonials` page.
- **Regulatory:** **LegitScript-certified** seal (verified telehealth/pharmacy); references licensed medical providers and Marek's "FDA-approved pharmacies."
- **Trust framing:** repeated "not your typical telehealth," labs-first, partnered-provider language.

## Visual & brand impression

Dark, premium, masculine. Near-black (#151515) ground, white type, and a single oxblood-red (#BB433C) accent on CTAs — confident and moody rather than clinical or wellness-pastel. Heavy use of high-production photography: muscular physiques, gym/athletic settings, before/after transformations, and a brick-wall founder portrait. Montserrat headlines over Inter body give a clean, modern, slightly editorial feel. The whole aesthetic reads as a serious "optimization for high performers" brand — closer to a supplement/athlete label than a soft DTC telehealth funnel. Polished and cohesive; clearly a mature Next.js build.

## Strategic read

- **Creator-origin moat:** built on Derek/MPMD's large optimization-focused audience — a built-in, high-intent acquisition channel most telehealth rivals would have to buy. The influencer/affiliate slug sprawl in the map (`/troponin`, `/syatt`, `/mpmd`…) is the affiliate machine made visible.
- **Platform, not clinic:** the explicit "we connect clients to providers, we are not a clinic" framing is both a compliance posture and a scalability lever — it offloads the medical entity and lets Marek own the coaching + diagnostics + commerce layer.
- **Labs + coaching as the wedge:** unlike script-first telehealth, Marek monetizes diagnostics and a human coaching relationship up front ($299 intake, $450 lab floor), then treatments — stickier and higher-LTV, and the basis of the **B2B CPP** white-label expansion into the coaching industry.
- **Deliberately not subscription:** rejecting fixed plans is a positioning choice (anti-"offload-a-prescription") even as the care cadence is recurring — a trust play in a category criticized for lock-in.
- **Performance stance as differentiator and risk:** openly embracing "high-leverage therapeutics" and an athletic/PED-adjacent audience is a sharp brand asset but a regulatory tightrope (hence the LegitScript seal and platform framing).

## Provenance

- **Pages:** homepage (full branding + screenshot), `/about-marek`, `/testosterone`, `/weight-loss`, `/sexual-health`, `/performance`, `/cpp` (7 unique pages) — all Firecrawl (`fc.py`, maxAge:0, location:US); offering taxonomy reconstructed from homepage goal tiles (mega-nav JS-walled); pricing quoted verbatim from the public surface only.
- **Verify:** all md5-unique, all sourceURLs matched — clean, no geo/cache contamination.
- **Credits:** 14 billed (1 map + 1 homepage + 6 key pages), but **6 were wasted**: a failed `| tail` pipe in the first key-page loop didn't abort `fc.py`, so the 6 key pages scraped twice — ~8 credits of useful work. Captures hold the latest version.
- **Couldn't get:** per-treatment/per-SKU consumer pricing (behind intake/login); named medication SKUs (goal landing pages, not catalogs); marekdiagnostics.com ownership detail; financials/headcount (out of scope).
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-05-31 rawHtml, hint-to-verify) — filled `socials` (fb/ig/x); `aliases` += legalName "Marek Health LLC"; JSON-LD `logo` lateral to the existing Marek logo — kept current. Re-stamped 2.0→2.2.
