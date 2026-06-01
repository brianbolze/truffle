---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: mylifeforce.com
name: Lifeforce
aliases: ["Lifeforce Digital, Inc."]
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js + Storyblok CMS (rawHtml /_next/, a.storyblok.com images), hosted on Vercel. Real IA lives under /pages/* (programs), /program/*, /collections/{supplements,pharmaceuticals}, /health-goals, /about, /clinicians-coaches — bare /products, /hormone-therapy, /peptide-therapy, /about-us, /our-clinicians return a real Next 404 ('There is no page at...'). /diagnostic aliases to the membership landing page (byte-identical body). Mega-nav IS in the homepage markdown (no client-render wall here). Pricing is promo-driven (struck-through 'New Year' sale prices + coupon URLs) — snapshot, not fixed. Weight-loss funnel is a separate quiz app at quiz.mylifeforce.com (embeddables.com). A/B: yes — seasonal promo modules + struck-through prices rotate run-to-run."
key_pages:
  membership: /pages/membership
  one_time_diagnostic: /pages/one-time-diagnostic
  testosterone: /pages/testosterone-program
  weight_loss: /pages/weight-loss
  menopause: /pages/menopause-management
  brain_protection: /program/brain-protection
  cardiac_risk: /pages/cardiac-risk
  metabolic_health: /pages/metabolic-health
  supplements: /collections/supplements
  pharmaceuticals: /collections/pharmaceuticals
  health_goals: /health-goals
  clinicians: /clinicians-coaches
  about: /about
  quiz: /landers/start-now
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — homepage/membership run a seasonal 'New Year' promo with struck-through prices ($349→$199, $699→$599) and coupon-coded checkout links; A/B/promo modules rotate."
  - "Per-SKU supplement and pharmaceutical pricing — /collections pages are category-level only; individual product prices sit behind the catalog/quiz, not captured."
  - "Founding year, funding, headcount, ownership structure — not stated on the marketing site."
  - "Medical advisory board member names — /about cites 'leading physicians and researchers from top institutions' and advisors from Harvard Medical School, BU, USC, and Brigham & Women's, but does not name them."

description: "America's self-described largest longevity-medicine program: a membership pairing an at-home 50+ biomarker blood diagnostic with 1:1 board-certified clinician care, health coaching, and clinician-prescribed supplements, hormones, peptides, and GLP-1s."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://www.mylifeforce.com/favicon-32x32.png  # STRAIN: branding.images.logo null; favicon fallback (wordmark is an inline Storyblok PNG: lifeforce_logo_black.png)
brand_colors: { primary: "#FDD17C", accent: "#26180F", background: "#F4F4EA", secondary: "#6E655C" }  # STRAIN: warm palette — amber/gold primary on cream, espresso text
fonts: [neue-haas-unica, Bradford LL]   # STRAIN: branding.fonts ranks generic sans-serif/serif first by count; the real brand faces are neue-haas-unica (sans) + Bradford LL (serif)
color_scheme: light
design_framework: next.js    # rawHtml /_next/ + Storyblok asset CDN; served via Vercel
---

## Overview

Lifeforce is a direct-to-consumer **longevity-medicine** program that bills itself as "America's largest." The wedge is a comprehensive **at-home blood diagnostic of 50+ biomarkers** across six categories; results are distilled into a proprietary **"Lifescore"** and reviewed in a 45-minute 1:1 telehealth consult with a board-certified clinician, who builds a personalized plan that can include lifestyle changes, clinical-grade supplements, and prescription treatments (TRT, peptides, GLP-1s). Members re-test every 3–6 months to track progress. It is sold as a recurring membership and is co-founded by Tony Robbins and Peter Diamandis; mission: "extend the healthspan of humanity."

## What they offer

Flagship is the diagnostic-anchored membership; programs, supplements, and pharmaceuticals are the companions (all gated by the membership + clinician approval).

- **Monthly Membership:** "~~$349~~ $199" today, then "$149/month (cancel anytime)" — 4×/yr at-home blood draw (50+ biomarkers), 4×/yr clinical consults, prescription access, unlimited health coaching, 30% off supplements, advanced panels + select peptides. (Annual flavor "$1449" / yr.)
- **Core Annual Membership:** "~~$699~~ $599" one-time — 2×/yr blood draws, 1×/yr consult, prescription access, personalized program, 30% off supplements.
- **One-Time Diagnostic:** "$549 One-Time" (or included with membership) — 50+ biomarkers, at-home draw, clinician consult, personalized plan; results in 5–7 days. All plans HSA/FSA-eligible (Truemed).
- **The Lifeforce Diagnostic:** the wedge — 50+ biomarkers across Hormones, Metabolic Health, Cardiovascular, Organ Health, Nutrients, and Inflammation (homepage labels: Hormone Balance, Critical Nutrients, Metabolic Condition, Organ Health, Cardiovascular Health, Other Key Risk Factors).
- **Testosterone Therapy:** "Optimize your testosterone with personalized treatment plans" — TRT, peptides, and other hormone options; "not one-size-fits-all."
- **Weight Loss:** GLP-1 program — semaglutide, "same active ingredient as Ozempic® and Wegovy®," delivered to the door with a personalized plan.
- **Menopause Management:** hormone testing + treatment options + ongoing support for peri/menopause.
- **Brain Protection:** cognitive-health program.
- **Cardiovascular Risk** & **Metabolic Health:** goal-based programs off the diagnostic.
- **Supplements (clinical-grade):** Foundational Health, Hormone Support, Cognitive Health, Sleep & Recovery.
- **Pharmaceuticals (Rx, clinician approval):** Hormone Therapy, Weight Management (GLP-1), Sexual Health, Cognitive Health.

## How it works / model

Four-step loop: **(1) Measure baseline** — a licensed phlebotomist visits the member's home to draw 50+ biomarkers; the member integrates wearables and completes an onboarding questionnaire. **(2) Interpret** — a proprietary evidence-based algorithm computes the Lifescore (plus quality-of-life, risk-of-dying-early, and speed-of-aging reads); a clinician identifies priorities. **(3) 1:1 clinician consult** — 45 minutes of telehealth to review results and build the plan (supplements, hormones, peptides, pharmaceuticals, lifestyle); the member is matched with a health coach. **(4) Retest & refine** — repeat every 3–6 months, included in the membership. Revenue is the recurring membership ($149/mo or $599/$1449 annual), the standalone $549 diagnostic, and add-on supplement/Rx sales; delivery is fully remote (at-home draws + telehealth + shipped Rx/supplements).

## Positioning & audience

Targets health-optimizing adults (broad gender mix — distinct women's "Menopause" and men's "Testosterone" tracks, both sexes in testimonials) who want proactive, data-driven longevity care rather than reactive primary care. Claimed edge: the **most comprehensive at-home diagnostic** (50+ biomarkers) feeding **board-certified clinicians + coaches + science-backed therapies** as a single "all-in-one" program — explicitly framed as the shift "away from sick care." Positions above lighter wellness/telehealth and DTC supplement brands on clinical depth, and against primary care on convenience and breadth; leans hard on founder star power (Tony Robbins, Peter Diamandis) and an elite clinician bar.

## Nav structure

Mega-nav captured from homepage markdown (real, not reconstructed):

```
- Solutions
  - Lifeforce Membership — /pages/membership
  - What We Test — /health-goals
  - Testosterone Therapy — /pages/testosterone-program
  - Menopause Management — /pages/menopause-management
  - Brain Protection — /program/brain-protection
  - Weight Loss — /pages/weight-loss
  - Cardiovascular Risk — /pages/cardiac-risk
  - Metabolic Health — /pages/metabolic-health
  - Add-On Panels — /collections/advanced-panels
- Supplements (by goal: Hormone Health · Vitality · Cardiac Risk · Weight Loss · Brain Health · Sexual Health · Longevity) — /collections/supplements
- Pharmaceuticals (same goal set) — /collections/pharmaceuticals
- About
  - Clinicians & Coaches — /clinicians-coaches
  - Leadership — /about
  - Blog — /journal
- Login — /account/profile · Become a Member — /landers/start-now
- Footer: One Time Diagnostic /pages/one-time-diagnostic · Gift Card /product/gift-card · Health Goals · Military Discount · Help Center (Zendesk) · Careers (Lever) · Terms · Privacy · Shipping · Return · Pharmacy Information · Lifeforce Medical Notice of Privacy · Medical Patient Agreement
```

## Credibility & proof

- **Outcome stats (self-reported):** "2M+ biomarkers analyzed"; "90% Improved Hormone Balance\*"; "40% Lowered Cardiac Risk\*"; ">70% Reduced Cognitive Decline\*"; "85% of Lifeforce members report better quality of life in just three months"; "80% of members improve their Lifescore within the first 12 months."
- **Clinician bar:** "We're More Selective Than Harvard" — "<4% of clinician applicants accepted," "board certifications across 15+ specialties," "50,000+ telehealth visits completed"; clinicians trained at Cleveland Clinic, Johns Hopkins, UCLA, Georgetown, UIC.
- **Science backing:** longevity model "developed with advisors from Harvard Medical School, Boston University, USC, and Brigham and Women's Hospital."
- **Founders:** Tony Robbins (Co-Founder), Peter Diamandis (Co-Founder), Dugal Bain-Kim (CEO).
- **Press logos:** Men's Health, Sports Illustrated, Newsweek, Forbes, Fortune, mindbodygreen, Fitt Insider, Garage Gym Reviews.
- **Trust/regulatory:** LegitScript-certified seal; HIPAA / Lifeforce Medical Notice of Privacy; Truemed HSA/FSA eligibility; named member testimonials with ages and Lifescores. Friendly-PC structure: services delivered by Lifeforce Medical NJ P.C., Lifeforce Medical KS P.A., Van Maele Medical P.C. (CA), and Lifeforce Medical P.A. elsewhere; Lifeforce Digital, Inc. is the non-clinical operating company (HQ 1920 Olympic Blvd, Santa Monica, CA).

## Visual & brand impression

Warm, premium-editorial identity: an **amber/gold primary (#FDD17C) on a cream background (#F4F4EA)** with **espresso (#26180F)** text — earthy and aspirational rather than clinical-blue. Type pairs **neue-haas-unica** (clean grotesque sans) with **Bradford LL** (a literary serif), reinforcing a "science meets lifestyle" feel. Heavy, polished lifestyle photography (active 40–60-somethings), a recurring black Lifeforce wordmark, and data-viz motifs (Lifescore dials, biomarker graphs). `color_scheme: light`. Overall: a confident, high-production longevity brand that reads more like a wellness-luxury membership than a telehealth utility. *(Read from the branding payload + page structure; full-page screenshots were captured but the image files were not openable via the file tools this session.)*

## Strategic read

The diagnostic is both moat and funnel: a 50+ biomarker panel positioned as the most comprehensive at-home test is the mandatory entry point, and the resulting Lifescore + clinical relationship is the wrapper through which higher-margin recurring care and Rx (TRT, GLP-1, peptides) are sold. It's the now-standard longevity/men's-health playbook (cf. Hone Health and Lifeforce's deep-telehealth cohort peers) but differentiated on (a) **breadth** — multi-goal programs (hormones, weight, menopause, brain, heart, metabolic) under one membership, not a single hero drug — and (b) **brand equity** — celebrity founders (Robbins/Diamandis) and a "more selective than Harvard" clinician story doing heavy trust work. The two-tier pricing ($149/mo high-touch vs. $599 once-a-year light) plus a $549 à-la-carte diagnostic ladders entry points; heavy promo scaffolding (struck-through "New Year" prices, coupon checkout) signals aggressive, conversion-optimized DTC acquisition.

## Provenance

- **Pages:** 13 analyzed via Firecrawl (all-formats on homepage; markdown+links+screenshot on key pages) — homepage, /pages/membership, /pages/one-time-diagnostic, /pages/testosterone-program, /pages/weight-loss + the /landers weight-loss quiz, /pages/menopause-management, /program/brain-protection, /pages/cardiac-risk, /collections/supplements, /collections/pharmaceuticals, /about, /clinicians-coaches; plus a 1-call map.
- **Verify:** after cleanup, all sourceURLs match and all 13 bodies are md5-unique (exit 0). First pass hit two hazards: five guessed bare paths returned real Next **404s**, and **/diagnostic returned the /membership body** (§5.1-style duplicate) — those six junk captures were removed from the store and manifest before the rewrite.
- **Credits:** 21 spent this run (1 map + 20 scrapes @ 1cr, basic proxy) — 14 on the retained dossier pages, ~7 on discovering the correct path structure (the 404s, the /diagnostic alias, one duplicate homepage). ~1,626 credits headroom at pre-flight.
- **Couldn't get:** per-SKU supplement/Rx pricing (category-level catalog only); founding year, funding, headcount; named medical advisory board members; openable screenshots (PNGs captured but unreadable via the file tools this session).
