---
schema_version: 1

# ⚠️ DOMAIN-KEY COLLISION (flag, not a redirect): the brand markets as "Healthspan" but its canonical
#   domain is gethealthspan.com (→ www.gethealthspan.com). The bare healthspan.com is a SEPARATE LIVE
#   ENTITY (resolves 200 to its own www.healthspan.com — the UK consumer-supplement company, NOT this
#   telehealth clinic). So healthspan.com is NOT an alias and must NOT be keyed here. Store folder is
#   `gethealthspan-com`, NOT the brief's `healthspan-com`.

# Identity
domain: gethealthspan.com            # primary key — the live canonical host for THIS telehealth brand
name: Healthspan
aliases: []                          # deliberately empty: healthspan.com is a different company (see collision note above)
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "firecrawl-only (heavy SPA). Strapi-headless CMS + Vercel-deployed Next.js (rawHtml has /_next/ + vercel; CMS assets on *.media.strapiapp.com). branding.designSystem.framework='custom' — WRONG (§5.4): it's Next.js. VWO (Visual Website Optimizer) HEAVILY instruments the site — the homepage markdown contains a large inline VWO campaign blob (A/B test config); treat it as noise, and expect pricing/IA flicker between runs (e.g. Rapamycin PDP $64↔$65, homepage Goals-grid present/absent). Product detail pages anchor on gethealthspan.com (apex) but signup/checkout is app.gethealthspan.com (#/product/signup/<id>). KNOWN un-walkable: /treatments/testosterone-replacement-therapy markdown SPA-blanks across many runs even with waitFor (skip or walk signup flow) — NOT walked here. /v2/map at limit:500 ~494 URLs dominated by a huge /research/article/* SEO surface (~250+). Influencer-affiliate landing pattern: /programs/longevity/<creator-slug> (e.g. jlaw = Jordan Lawley, promo JLAW). No §5.1 contamination (6 bodies unique, sourceURLs matched; maxAge:0 + location:US + waitFor:4000 + serialized). DO NOT confuse with healthspan.com (UK supplement co — see collision note)."
key_pages:
  longevity_program: /programs/longevity-optimization-core   # flagship membership ($99/mo); was -program, now -core
  mens_hormone: /programs/mens-hormone-health                # men's hormone membership ($99/mo)
  rapamycin: /treatments/rapamycin                          # signature longevity treatment
  our_company: /our-company                                 # founder + advisory board
  how_it_works: /how-it-works
  bioage: /bioage                                           # BioAge+ biological-age tracking (mega-nav primacy)
  labs_metabolic: /labs/metabolic-pro-panel
unverified_fields:
  - "TRT page (/treatments/testosterone-replacement-therapy) SPA-blanks reliably — testosterone Rx pricing not captured (per prior runs; not re-attempted)."
  - "VWO A/B instrumentation makes some pricing flicker between runs (e.g. Rapamycin Protocol $64 vs $65) and toggles homepage modules (Goals grid) — single-capture values are point-in-time."
  - "Full standalone-treatment + lab pricing matrix (Longevity Pro / Prime Longevity / hormone panels) partially captured; many SKUs not deep-walked."
  - "Headcount / revenue / funding / ownership — not on the marketing site (deep-research job)."

# Description — one sentence
description: "A self-described digital longevity clinic delivering membership-based, biomarker-driven longevity care for men and women — rapamycin and metabolic protocols, hormone therapy, GLP-1s, expert coaching, and biological-age (BioAge+) tracking — on a $99/mo membership plus per-treatment subscriptions."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # longevity-clinic membership/coaching + the compounded/Rx protocols
portfolio_shape: Multi-product       # Longevity Optimization, Men's Hormone, Women's HRT, GLP-1 Care, Metabolic Health programs + standalone treatments/labs
business_model: Subscription         # $99/mo membership + per-treatment monthly subscriptions
primary_industry: Healthcare & Life Sciences

# Visual identity — lifted from Firecrawl `branding` (homepage), confirmed against screenshot
logo_url:                            # no favicon set (metadata.favicon null); wordmark is "Healthspan" in black. Left empty per the fallback chain rather than guess.
brand_colors: { primary: "#FEF38E", secondary: "#81B1E2", background: "#FFFFFF", text: "#000000", link: "#81B1E2" }   # branding.colors. Screenshot read: a muted scientific palette — pale-yellow #FEF38E accent blocks + light-blue #81B1E2 tints on white, with dark hero/section bands and microscopy imagery. Yellow is a soft accent here (paler than Hone/PeterMD), not a saturated brand hue.
fonts: [Suisse Intl, Soehne Mono]    # branding.fonts: Suisse Intl=body, Soehne Mono=monospace labels (data/science feel)
color_scheme: light                  # branding.colorScheme; white base with dark section bands
design_framework: next.js            # rawHtml /_next/ + vercel; CMS = Strapi. branding.designSystem said "custom" — wrong (§5.4).
---

## Overview

Healthspan positions itself as "the **1st digital longevity clinic**" — "Transform your quality of living through the science of aging." It delivers **biomarker-driven, membership-based longevity care** to both men and women: advanced lab panels + wearable physiology feed personalized protocols built around rapamycin, metabolic agents (metformin, acarbose, SGLT2), hormone therapy, GLP-1s, and expert coaching, with **BioAge+** (biological-age tracking) as the signature engagement loop. Founded by Daniel (after his wife Dr. Elana Miller's lymphoma relapse exposed how inaccessible advanced care was), the brand's mission is "longevity science available beyond a wealthy few." ~12,000 patients.

> **⚠️ Not to be confused with `healthspan.com`** — that bare domain is a *different live company* (the UK consumer-supplement brand). This telehealth clinic's canonical key is **gethealthspan.com**. (See the collision note in frontmatter; flagged for the store's domain-key convention.)

## What they offer

Membership programs + a deep standalone treatment/lab catalog (a future `offerings.md` would enumerate):

- **Programs (memberships):** Longevity Optimization (Core) "$99/mo," Men's Hormone Health "$99/mo," Women's HRT ("Starting at $99/month"), GLP-1 Longevity Care, Metabolic Health. All include "**BioAge+ · Coaching · Personalized Protocols**."
- **Standalone treatments (per-month, + membership):** The Rapamycin Protocol $64/mo (the signature), Topical Rapamycin Skin $115 / Hair $140, SGLT2 Protocol $99, Methylene Blue $99, Oxytocin (Troche) $135, Cellular Renewal $105, Autophagy $56, Metformin $27, Acarbose $25, LDN $40, Enclomiphene $60, plus Wegovy®/Zepbound®/compounded semaglutide GLP-1s.
- **Labs:** Longevity Starter Panel ($55 one-time), Rapamycin Bioavailability Panel ($25), Metabolic Pro Panel (~$120/mo), Complete Male/Female Hormone Panels, Prime/Longevity Pro.

**`portfolio_shape: Multi-product`** — multiple distinct membership programs *and* a large à-la-carte treatment/lab catalog a customer chooses among.

## How it works / model

A **membership + protocol** longevity-clinic model: join ($99/mo) → advanced biomarker panel + wearable/physiology data → clinician + coach design a personalized protocol (rapamycin/metabolic/hormone/GLP-1) → ongoing BioAge+ tracking and protocol adjustment. Money is the **$99/mo membership** plus **per-treatment monthly subscriptions** (medication billed separately). Heavy editorial/SEO surface (250+ `/research/article/*`) and an influencer-affiliate channel (`/programs/longevity/<creator>` with promo codes) feed acquisition; VWO runs continuous A/B tests.

## Positioning & audience

- **Who:** B2C longevity-minded adults, "Designed for men 35–65" framing plus a full women's hormone/HRT track.
- **Against:** other longevity/hormone players (Hone is the closest — both biomarker-led) and the broad telehealth field — Healthspan's wedge is **"longevity clinic" credibility + science depth** (rapamycin, autophagy, cellular-renewal protocols; "follow the science").
- **Claimed edge:** "1st digital longevity clinic," "Labs 3X More Comprehensive," "70+ Biomarkers Tracked / 9 Biological Systems," "150+ published works," PhD-level performance coaching, and BioAge+ biological-age tracking.

## Nav structure

Next.js mega-nav (BioAge+ promoted to top-level):

```
- Treatments (mega) — All Treatments / Medications / Programs / Labs / Supplements
- Programs (mega) — Longevity Optimization (/programs/longevity-optimization-core) · GLP-1 Longevity Care (/programs/glp1-care) · Women's Health / HRT · Men's Hormone Health (/programs/mens-hormone-health)
    sub-lockup: "All Programs Include: BioAge+ / Coaching / Personalized Protocols"
- BioAge+ — /bioage (top-level)
- About (mega) — Our Company (/our-company) · Our Mission (/our-mission) · How it Works (/how-it-works)
- Research — /research (250+ articles)
- Log in → app.gethealthspan.com
```

## Credibility & proof

- **Trust:** "4.9/5 Trustpilot Review," "Trusted by **12,000+ Patients**," "1st digital longevity clinic," "20+ avg. yrs of experience," "150+ published works."
- **Team:** named founder (Daniel, molecular-biology background) + a **medical advisory board** (e.g., Dr. Scott Sanderson — board-certified Emergency Medicine, certified Anti-Aging Medicine, clinical faculty at John A. Burns School of Medicine); PhD-level coaches.
- **Compliance:** CLIA-certified labs; "Membership-gates-Rx" language; "Modify or cancel anytime"; HSA/FSA eligible; LegitScript-certified-pharmacy badge on some PDPs. (Notably, **no** HIPAA/LegitScript badge on the homepage and no per-state availability list — lighter compliance surfacing than PeterMD/Hims.)
- **Featured-in** press strip + a first-party Discourse community (community.gethealthspan.com).

## Visual & brand impression

A deliberately **scientific, data-forward** light-mode aesthetic — the most "lab/research" of the cohort. White canvas with **pale-yellow `#FEF38E`** accent blocks and **light-blue `#81B1E2`** tints, punctuated by dark hero/section bands and **microscopy/cellular imagery** ("follow the science"). Typography is the tell: **Suisse Intl** body with **Soehne Mono** monospace labels (biomarker readouts, "PERSONALIZED PROTOCOL: 5 mg/week Rapamycin," "BIOLOGICAL AGE: 31") — a quantified-self, clinical-data feel rather than warm-lifestyle (Hims) or bold-consumer (Hone). Reads premium and rigorous. (Note: this is the cohort's **third yellow-forward brand** — pale `#FEF38E` vs Hone `#F8F93F` vs PeterMD `#FFFF64` — though Healthspan's is a muted accent, not a dominant hue.)

## Strategic read

Healthspan is the **science/longevity-clinic** play: it competes on rigor and biomarker depth rather than price (PeterMD) or brand scale (Hims). The durable state worth recording: a membership-led ($99/mo) digital longevity clinic monetizing a separable platform fee + per-protocol subscriptions across both genders, with rapamycin/metabolic protocols and BioAge+ tracking as the differentiators, and an unusually heavy editorial/SEO + influencer-affiliate + VWO-optimized acquisition machine. Two store-level signals: (1) the **healthspan.com namespace collision** — a clean case where domain-as-key works only if you key on the *resolved canonical* (gethealthspan.com), since the "obvious" domain belongs to an unrelated company; and (2) the VWO A/B instrumentation means single-capture pricing/IA is point-in-time, not stable.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30):** homepage (`/`, rich pass: markdown + html + rawHtml + links + branding + images + full-page screenshot), `/programs/longevity-optimization-core`, `/programs/mens-hormone-health`, `/treatments/rapamycin`, `/our-company`, `/how-it-works` — each markdown + links + full-page screenshot. Site inventory via `/v2/map` (limit 500).
- **Capture mechanics:** `maxAge:0` + `location:{country:US}` + `waitFor:4000` + serialized; all 6 bodies unique + sourceURLs matched (no §5.1 contamination). **7 credits**, clean run. Skipped the reliably-SPA-blank TRT page per prior-run guidance.
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned markdown: `captures/2026-05-30/*.md`.
- **Couldn't get:** TRT-page pricing (SPA-blank); full lab/treatment matrix; stable pricing (VWO flicker). See `unverified_fields`.
