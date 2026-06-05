---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: mylifeforce.com
name: Lifeforce
aliases: ["Lifeforce Digital, Inc."]
parent: []
owns: []
socials: { instagram: "https://www.instagram.com/lifeforce/", facebook: "https://www.facebook.com/lifeforce" }   # from footer anchors (no JSON-LD on this site); verified to this entity
external: {}                          # no third-party records exposed (no JSON-LD sameAs)

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js + Storyblok CMS (rawHtml /_next/, a.storyblok.com images), hosted on Vercel. Real IA lives under /pages/* (programs), /program/*, /collections/{supplements,pharmaceuticals,advanced-panels,all}, /health-goals, /about, /clinicians-coaches — bare /products, /hormone-therapy, /about-us return a real Next 404. Catalog: /collections/* grids carry product cards (clean 3600x3600 *_clp.png renders, NO prices); per-SKU prices live ONLY on /product/<slug> PDPs (loaded client-side, NOT in rawHtml; /products.json + /collections/all.json soft-200 the Next SPA shell, no Shopify registry). Supplements show published one-time + 'Save 15%' subscribe prices; Pharmaceuticals + Advanced Panels are tagged 'Members Only' and pharma PDPs gate on membership+diagnostic+clinician (price still shown). Five /product PDPs route but throw a client-side exception and are absent from every collection grid (orphaned/discontinued): peak-rise, zepbound, bpc-157, cjc-1295, ipamorelin. /product/peptide-telehealth is a membership-enrollment chooser, not a peptide SKU. Pharmacy: third-party — partners Tailor Made Compounding + Precision Pharmacy (/pharmacy-information). Mega-nav IS in homepage markdown + recoverable from <header> (fc.py signals). Pricing is promo-driven (struck-through enrollment $349->$199, $699->$599; 'new-year-hero' image assets persist into June; coupon-coded checkout URLs) — snapshot, not fixed. A/B: yes — seasonal promo modules + struck-through prices rotate run-to-run."
key_pages:
  membership: /pages/membership
  how_it_works: /pages/how-it-works
  one_time_diagnostic: /pages/one-time-diagnostic
  testosterone: /pages/testosterone-program
  weight_loss: /pages/weight-loss
  menopause: /pages/menopause-management
  cardiac_risk: /pages/cardiac-risk
  metabolic_health: /pages/metabolic-health
  brain_protection: /program/brain-protection
  supplements: /collections/supplements
  pharmaceuticals: /collections/pharmaceuticals
  advanced_panels: /collections/advanced-panels
  catalog_all: /collections/all
  clinicians: /clinicians-coaches
  about: /about
  pharmacy: /pharmacy-information
  quiz: /landers/start-now
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — membership/diagnostic run a persistent promo (struck-through enrollment $349->$199, Core Annual $699->$599; 'new-year-hero' assets) with coupon-coded checkout links; A/B/promo modules rotate."
  - "Founding year, funding, headcount, ownership structure — not stated on the marketing site."
  - "Medical advisory board member names — /about cites advisors from Harvard Medical School, BU, USC, and Brigham & Women's, but does not name them (the /clinicians-coaches page names treating clinicians + coaches)."
  - "503A/503B compounding lane — /pharmacy-information names partner pharmacies (Tailor Made Compounding, Precision Pharmacy) but does not state the 503A vs 503B designation."

description: "America's self-described largest longevity-medicine program: a membership pairing an at-home 50+ biomarker blood diagnostic with 1:1 board-certified clinician care, health coaching, and clinician-prescribed supplements, hormones, peptides, and GLP-1s."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against screenshot + logo files
logo_url: https://a.storyblok.com/f/130005/1969x475/f2a741a714/lifeforce_logo_black.png  # 2.5 canonical wordmark (black LIFEFORCE wordmark on Storyblok CDN); supersedes the prior favicon fallback
logos:
  wordmark: { src: "https://a.storyblok.com/f/130005/1969x475/f2a741a714/lifeforce_logo_black.png", w: 1969, h: 475 }  # transparent black wordmark (hasAlpha + rgba(0,0,0,0) corner)
  logomark: { src: "https://www.mylifeforce.com/apple-touch-icon.png", px: 180, transparent: false }  # three-overlapping-rings symbol in espresso; baked WHITE box (hasAlpha:no, white corner) — a colored square on a dark slide
  # og: omitted — no og:image declared (branding.images.ogImage null; true absence)
brand_colors: { primary: "#FDD17C", accent: "#26180F", background: "#F4F4EA", secondary: "#6E655C" }  # STRAIN: warm palette — amber/gold primary on cream, espresso text
fonts: [neue-haas-unica, Bradford LL]   # STRAIN: branding.fonts ranks generic sans-serif/serif first by count; the real brand faces are neue-haas-unica (sans) + Bradford LL (serif)
color_scheme: light
design_framework: next.js    # rawHtml /_next/ + Storyblok asset CDN; served via Vercel
---

## Overview

Lifeforce is a direct-to-consumer **longevity-medicine** program that bills itself as "America's largest longevity medicine program combining diagnostics, doctors, coaches, and science-backed longevity therapies." The wedge is a comprehensive **at-home blood diagnostic of 50+ biomarkers**; results are distilled into a proprietary **"Lifescore"** (plus a biological-age read) and reviewed in a 45-minute 1:1 telehealth consult with a board-certified clinician, who builds a personalized plan that can include lifestyle changes, clinical-grade supplements, and prescription treatments (TRT, peptides, GLP-1s, women's HRT, cardiometabolic and thyroid meds). Members re-test every 3–6 months to track progress. It is sold as a recurring membership and is co-founded by Tony Robbins and Peter Diamandis; mission: "extend the healthspan of humanity."

## What they offer

Flagship is the diagnostic-anchored membership; programs, supplements, and pharmaceuticals are the companions. Supplements sell à-la-carte at published prices; pharmaceuticals + advanced panels are members-only and clinician-gated. Per-SKU roster (≈39 SKUs) in [`offerings.md`](offerings.md).

- **Monthly Membership:** enrollment "~~$349~~$199" today, then "$149/month (cancel anytime)" — 4×/yr at-home blood draw (50+ biomarkers), 4×/yr clinical consults, prescription access, unlimited health coaching, 30% off supplement subscriptions, advanced panels + select peptides `[published]`
- **Core Annual Membership:** "~~$699~~$599" one-time — 2×/yr blood draws, 1×/yr consult, prescription access, personalized program, 30% off supplements `[published]`
- **Premium Annual Membership:** "$1449" annually — everything in Monthly Membership `[published]`
- **One-Time Diagnostic:** "$599" (or included with membership) — 50+ biomarkers, at-home draw, 45-min clinician consult, Lifescore + biological age, results in 5–7 days; HSA/FSA-eligible `[published]`
- **Supplements (clinical-grade, own-brand):** the "Peak" line + companions — e.g. Peak Healthspan **$120**, Peak NMN **$100**, Peak Rest **$110**, Omega **$70**, DHEA/Vitamin D+K/Methylation **$50**, CoQ10 **$40**; one-time + "Save 15%" subscribe, members save 30% `[published]`
- **Pharmaceuticals (Rx, members-only + clinician approval):** Hormone/TRT (testosterone injection/cream **$80**, Kyzatrex oral-T **$250**, clomiphene, anastrozole), Women's HRT (estradiol patch/cream, micronized progesterone, estriol face cream), Weight Loss (compounded semaglutide+B12 **$270**/25 days), Sexual Health (tadalafil, sildenafil cream, PT-141), Thyroid (levothyroxine/liothyronine), Cardiometabolic (rosuvastatin, ezetimibe, metformin), Peptides (sermorelin **$160**) — each price shown but gated `[partial]`
- **Advanced Panels (add-on diagnostics):** Brain Protection **$850**, Cardiovascular / Metabolic / Heavy Metals **$200** each `[partial]`
- **The Lifeforce Diagnostic:** the wedge — 50+ biomarkers across Hormones, Metabolic Health, Cardiovascular, Organ Health, Nutrients, and Inflammation `[published]`

## How it works / model

Four-step loop: **(1) Measure baseline** — a licensed phlebotomist visits the member's home (or a lab) to draw 50+ biomarkers; the member integrates wearables and completes an onboarding questionnaire. **(2) Interpret** — a proprietary algorithm computes the Lifescore + biological age; a clinician identifies priorities. **(3) 1:1 clinician consult** — a 45-minute scheduled telehealth (video) consult with a board-certified longevity-medicine clinician to review results and build the plan (supplements, hormones, peptides, pharmaceuticals, lifestyle); the member is matched with a health coach. **(4) Retest & refine** — repeat every 3–6 months, included in the membership. Revenue is the recurring membership ($149/mo, $599 Core Annual, or $1449 Premium Annual), the standalone $599 diagnostic, and add-on supplement/Rx/panel sales; delivery is fully remote (at-home draws + telehealth + shipped Rx/supplements). Pharmaceuticals are members-only, contingent on blood results + a clinician video consult, and limited to eligible states.

## Positioning & audience

Targets health-optimizing adults across both sexes — distinct men's "Testosterone Therapy" and women's "Menopause Management" tracks, both genders in testimonials — who want proactive, data-driven longevity care rather than reactive primary care. Claimed edge: the **most comprehensive at-home diagnostic** (50+ biomarkers) feeding **board-certified clinicians + coaches + science-backed therapies** as a single "all-in-one" membership — explicitly framed as the shift "away from sick care." A homepage comparison table positions Lifeforce above both a regular doctor and other longevity programs on breadth (diagnostics + FDA pharmaceuticals + coaching). Leans hard on founder star power (Tony Robbins, Peter Diamandis) and an elite clinician bar ("More Selective Than Harvard").

## Nav structure

Mega-nav captured from homepage markdown + recovered `<header>` region (fc.py signals), validated against the screenshot:

```
- How It Works — /pages/how-it-works
- Solutions (flyout: "SOLUTIONS")
  - Lifeforce Membership — /pages/membership
  - What We Test — /health-goals
  - Testosterone Therapy — /pages/testosterone-program
  - Menopause Management — /pages/menopause-management
  - Brain Protection — /program/brain-protection
  - Weight Loss — /pages/weight-loss
  - Cardiovascular Risk — /pages/cardiac-risk
  - Metabolic Health — /pages/metabolic-health
  - Add-On Panels — /collections/advanced-panels
- Supplements (flyout: "TOP HEALTH GOALS" → goal filters)
  - Hormone Health · Vitality · Cardiac Risk · Weight Loss · Brain Health · Sexual Health · Longevity — /collections/supplements/<goal>
  - Shop All — /collections/supplements
- Pharmaceuticals ("Members Only"; flyout: same goal set) — /collections/pharmaceuticals/<goal> · Shop All — /collections/pharmaceuticals
- About (flyout: "LIFEFORCE RESOURCES")
  - Clinicians & Coaches — /clinicians-coaches
  - Leadership — /about
  - Blog — /journal
- Login — /account/profile · Become a Member — /landers/start-now
- Footer: One Time Diagnostic /pages/one-time-diagnostic · Gift Card /product/gift-card · Health Goals · Military Discount /landers/military-discount · Help Center (Zendesk) · Careers (Lever) · Terms · Privacy · Shipping · Return · Pharmacy Information /pharmacy-information · Lifeforce Medical Notice of Privacy · Medical Patient Agreement · socials: Facebook, Instagram
```

## Credibility & proof

- **Outcome stats (self-reported):** ">2.5M biomarker results" used to formulate supplements; "85% of Lifeforce members report better quality of life in just three months"; "Over 25% of new members' initial biomarkers start in sub-optimal ranges"; diagnostic page cites improvement metrics for heart health, cognition, and hormone optimization (footnoted to "new members with sub-optimal biomarkers").
- **Clinician bar:** "We're More Selective Than Harvard"; clinicians with "board certifications in integrative medicine, endocrinology, functional medicine, sports medicine, and more"; named treating clinicians incl. **Dr. Cindy Tsai, MD** (Internal + Integrative Medicine; Johns Hopkins, Dartmouth) and **Dr. Russell Van Maele, DO** (Michigan State COM; Western Michigan U.); named health coaches (Serena Holtsinger, INHC; Patrick Doyle, NBHWC).
- **Science backing:** longevity model "developed with advisors from Harvard Medical School, Boston University, USC, and Brigham and Women's Hospital" (unnamed).
- **Founders / leadership:** Tony Robbins (Co-Founder), Peter Diamandis (Co-Founder), Dugal Bain-Kim (CEO).
- **Press logos:** Men's Health, Sports Illustrated, Newsweek, Forbes, Fortune, mindbodygreen, Fitt Insider, Garage Gym Reviews.
- **Trust / regulatory:** LegitScript-certified seal (footer, ID 12155851); supplements "Manufactured in cGMP-certified, FDA-registered facilities"; HSA/FSA eligibility; named member testimonials with ages/Lifescores. Pharmacy is third-party — "several licensed, NAPB-accredited pharmacies we partner with," named **Tailor Made Compounding** + **Precision Pharmacy** (/pharmacy-information). Friendly-PC structure: services by Lifeforce Medical NJ P.C., Lifeforce Medical KS P.A., Van Maele Medical P.C. (CA), and Lifeforce Medical P.A. elsewhere; Lifeforce Digital, Inc. is the non-clinical operating company.

## Visual & brand impression

Warm, premium-editorial identity confirmed against the full-page screenshot: an **amber/gold primary (#FDD17C) on a cream background (#F4F4EA)** with **espresso (#26180F)** text — earthy and aspirational rather than clinical-blue. The hero Lifescore renders as a glowing amber-gradient dial. Type pairs **neue-haas-unica** (clean grotesque sans) with **Bradford LL** (a literary serif), reinforcing a "science meets lifestyle" feel. Heavy, polished lifestyle photography (active 40–60-somethings, couples), a black LIFEFORCE wordmark, and a three-overlapping-rings logomark in espresso. `color_scheme: light`. Overall: a confident, high-production longevity brand that reads more like a wellness-luxury membership than a telehealth utility.

## Strategic read

The diagnostic is both moat and funnel: a 50+ biomarker panel positioned as the most comprehensive at-home test is the mandatory entry point, and the resulting Lifescore + clinical relationship is the wrapper through which higher-margin recurring care and Rx (TRT, GLP-1, peptides, women's HRT) are sold — the now-standard longevity/men's-health playbook (cf. Hone, Maximus, and the deep-telehealth cohort), differentiated on (a) **breadth** — a single membership spanning hormones, weight, menopause, brain, heart, metabolic, thyroid, and sexual health, not one hero drug — and (b) **brand equity** — celebrity founders (Robbins/Diamandis) and a "more selective than Harvard" clinician story doing heavy trust work. A laddered price stack ($149/mo high-touch · $599 once-a-year Core · $599 à-la-carte diagnostic) widens the funnel; heavy promo scaffolding (struck-through enrollment, coupon checkout) signals aggressive, conversion-optimized DTC acquisition. The catalog is unusually deep for a longevity brand — ~22 prescription SKUs across seven categories — but Lifeforce owns no pharmacy (third-party compounders), so its integration is clinical (diagnostics + clinicians) rather than fulfillment.

## Provenance

- **Pages:** 53 analyzed via Firecrawl (all-formats on homepage + 4 collection grids; markdown+links+screenshot on key pages + 39 product PDPs) — homepage, /pages/{membership, how-it-works, one-time-diagnostic, testosterone-program, weight-loss, menopause-management}, /about, /clinicians-coaches, /pharmacy-information, /collections/{supplements, pharmaceuticals, advanced-panels, all}, and 39 /product/* PDPs; plus a 1-call map.
- **Verify:** all 53 sourceURLs match and all 53 bodies are md5-unique (exit 0). Five /product PDPs returned a client-side-exception shell and were removed before write (peak-rise, zepbound, bpc-157, cjc-1295, ipamorelin — all absent from every collection grid, i.e. orphaned/discontinued).
- **Credits:** 54 attributed this run (1 map + 53 retained scrapes @ 1cr, basic proxy); +10 spent on the 5 broken-PDP discovery (each retried once) = 64 billed total. ~848 credits headroom at pre-flight (677 after); logos + product-render fetches were headed (no credits).
- **Couldn't get:** prices for the 5 orphaned/erroring PDPs (client-side exception); founding year, funding, headcount; named medical advisory board members; 503A/503B pharmacy lane.
- **Structured layer (schema 2.5):** ran `fc.py signals` on the 2026-06-04 homepage rawHtml — no `application/ld+json` present (consistent with the prior run), so no JSON-LD fields; `socials` seeded from footer anchors (Facebook, Instagram). Nav recovered from the `<header>` region and validated against the screenshot.
- **Run profile:** express — refresh forced over a still-warm (2026-05-31) capture; +offerings.md (≈39-SKU roster), +telehealth.md cohort pack, +logos:{} module, +flagship product-render images (10 own-brand supplement `_clp.png` shots → captures/2026-06-04/images/). Migrated 2.2→2.5 (full re-capture, not a rule-rewrite).
