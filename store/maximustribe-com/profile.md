---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: maximustribe.com
name: Maximus
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Gatsby SSG (___gatsby + /page-data/) on Sanity CMS — read framework from rawHtml; branding.designSystem reports 'custom' (wrong, per §5.4). Mega-nav + footer render in markdown fine. Map returns 337 URLs, ~70% /resources/ blog + /white-paper/ + LP-funnel noise (testosterone-protocol-*-LP, *-tiktok, *-fb) — the real catalog is in homepage links, not the map. Logo is inline data-URI SVG → favicon fallback. App lives on app.maximustribe.com (funnels: /testosterone-start, /weight-loss-start, etc.); help on support.maximustribe.com."
key_pages:
  testosterone: /testosterone
  weight_loss: /weight-loss
  labs: /labs
  growth_hormone_peptides: /growth-hormone-peptides
  hair_growth: /hair-growth
  oxytocin: /oxytocin-calming-cream
  about: /about-us
  blood_flow: /vardenafil-tadalafil-sildenafil-bloodflow
  multivitamin: /building-blocks
unverified_fields:
  - "Headcount, funding, revenue — not on the marketing site (deep-research job)."
  - "Per-protocol full price ladders (intake-gated past the public 'Starting at' anchors) — captured representative starting prices only."

description: "A DTC performance-medicine telehealth brand for men (now also women) that prescribes testosterone, GLP-1 weight-loss, peptide, hair, sexual, and lab-testing protocols online via licensed physicians and compounding pharmacies, on direct-pay monthly memberships."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://www.maximustribe.com/favicon-32x32.png   # branding.images.logo is an inline data-URI SVG; favicon fallback
brand_colors: { primary: "#0053C5", secondary: "#01429B", background: "#FFFFFF" }  # deep blue — confirmed against screenshot (CTAs, stat panels)
fonts: [Inter, Victor Serif]         # Inter body, Victor Serif headings
color_scheme: light
design_framework: gatsby             # ___gatsby + /page-data/ in rawHtml; content via Sanity CMS
---

## Overview

Maximus is a direct-to-consumer "performance medicine" telehealth company. Founded in 2020 by a doctor (CEO Dr. Cameron Sepah) on the thesis that "traditional medicine is focused on normalization, not optimization," it began by treating low testosterone in men and has since expanded into a multi-line men's-health (and now also women's) platform. The journey is fully online: free health questionnaire → video visit with a US-licensed physician → optional at-home labs → personalized protocol (medications, supplements, lifestyle guidance) shipped to the door, with ongoing doctor-led monitoring. Positions on clinical credibility — a urology-professor medical advisory board, in-house clinical research/white papers, and custom-compounded formulas. Claims **50k+ members**.

## What they offer

A genuine multi-line catalog, all subscription / direct-pay (no insurance). Testosterone is the flagship and origin line; the rest are explicitly badged **NEW** (mood, labs, peptides):

- **Testosterone (flagship):** multiple protocol formats: Enclomiphene, Oral Testosterone, Testosterone Cream, Injectable TRT, plus combination protocols (e.g. enclomiphene + tadalafil + testosterone). "Protocols start at $99.99/month… combination protocols… range from $149.99–$199.99/mo." Up to $299.99/mo seen.
- **Weight Loss:** GLP-1 / GIP: Semaglutide "Starting at $149.99" and Tirzepatide "Starting at $249.99."
- **Lab Testing (NEW):** Optimal Panel **$199.99/year**, Maximal Panel **$349.99/year** (up to 146+ biomarkers); At-Home Testosterone Test (10 markers, ~$99.99).
- **Growth Hormone Peptides (NEW):** Sermorelin / GHRH peptides, $199.99–$299.99/mo.
- **Mood & Stress (NEW):** patent-pending **Oxytocin Calming Cream**, "Starting at $99.99."
- **Hair Growth:** finasteride/dutasteride/minoxidil orals + All-in-One Gel, $24.99–$79.99/mo.
- **Blood Flow & ED:** vardenafil / tadalafil / sildenafil.
- **Prescription Multivitamin:** "Building Blocks."

New clients on a 12-month plan get **50% off their first month**; every protocol bundles doctor consults, monitoring, and 24/7 care-team messaging at no extra cost.

## How it works / model

Direct-pay subscription telehealth. Customer journey: free questionnaire → 100%-online physician visit → optional at-home lab work → personalized protocol shipped discreetly → ongoing care-team messaging and doctor-led adjustments. Revenue is recurring monthly membership per protocol (labs are annual). Fulfillment runs through vetted US-based, USP-compliant **licensed compounding pharmacies** sourcing APIs from FDA-registered manufacturers. Explicitly insurance-free / transparent direct-pay covering visits, meds, and support.

## Positioning & audience

Targets ambitious, performance-minded adults — originally men optimizing testosterone, now broadened to women and to longevity/metabolic/mood. Tagline framing: *"The leading edge of personal performance medicine – treating people, not averages"* and *"It's not just hormones – it's the science of unlocking human potential."* The claimed edge is clinical rigor and proprietary formulations ("performance medicine protocols offered only at Maximus," custom formulas, in-house clinical research) — differentiating from both lighter wellness-telehealth brands and conventional in-person care. Competes adjacent to Hims, Hone Health, Function Health (it ships a `/labs/maximus-vs-function-health` comparison page).

## Nav structure

```
- Testosterone — /testosterone
  - Testosterone Cream — /testosterone/Testosterone-Cream
  - Injectable Testosterone — /testosterone/Injectable-TRT
  - Oral Testosterone — /testosterone/oral-testosterone
  - Enclomiphene — /testosterone/enclomiphene-only
  - At-Home Testosterone Test — /lab-tests
  - All Testosterone Treatments — /testosterone
- Weight Loss — /weight-loss
  - Tirzepatide — /weight-loss/tirzepatide-standard
  - Semaglutide — /weight-loss/semaglutide-standard
  - All Weight Loss Treatments — /weight-loss
- Mood & Stress (NEW) — Oxytocin Calming Cream — /oxytocin-calming-cream
- Lab Testing (NEW)
  - Comprehensive Lab Testing (up to 146 markers) — /labs
  - At-Home Testosterone Test (10 markers) — /lab-tests
- Growth Hormone Peptides (NEW) — /growth-hormone-peptides
  - Sermorelin Growth Hormone Therapy — /growth-hormone-peptides/sermorelin-growth-hormone-therapy
- More
  - Blood Flow — Vardenafil, Tadalafil, Sildenafil — /vardenafil-tadalafil-sildenafil-bloodflow
  - Prescription Multivitamins — Building Blocks — /building-blocks
  - Hair Growth — All-in-One Gel — /hair-growth/all-in-one-gel · All Treatments — /hair-growth
- Learn — Blog — /resources · Research & Clinical Studies — /science-all
- Company — About Us — /about-us · Partners — /partners · Careers — /careers · Contact — /contact
```

## Credibility & proof

- **Medical advisory board** of named urology professors/clinicians: Dr. Cameron Sepah (CEO, Harvard-educated clinical psychologist, ex-UCSF), Dr. Matt Coward (UNC Urology), Dr. Wayne Hellstrom (Tulane, Chief of Andrology), Dr. Justin Houman (Cedars-Sinai), Dr. Eugene Shippen (author, *The Testosterone Syndrome*).
- **"50k+ members"**, "As seen in" press logos, and a four-stat trust band (Performance medicine / Custom formulas / Clinical research / 50k+ members).
- In-house **white papers / clinical studies** (oral TRT liver-safety, enclomiphene protocol, oxytocin, topical dutasteride) under `/science-all`.
- **LegitScript-approved** seal (linked to verification). Stated US-licensed board-certified physicians + USP-compliant compounding pharmacy vetting.
- Oxytocin trial stats cited: 71% improved happiness, 69% improved sleep satisfaction, 51% reduced anxiety, +25 min sleep/night.

## Visual & brand impression

Premium, masculine, clinical-but-aspirational. White background with deep-blue (`#0053C5`) accents, CTAs, and data panels; serif display headlines (Victor Serif) over an Inter body set a confident, editorial-medical tone. Heavy use of high-production photography of fit, focused people and clean product renders. Animated stat callouts ("↑3.1x Free testosterone," "↓28% body fat") signal a data/results orientation. Reads as a mature, well-funded brand — closer to a polished consumer-health flagship than a scrappy DTC funnel, despite the aggressive paid-LP infrastructure underneath.

## Provenance

- **Pages:** homepage (rich: markdown+html+rawHtml+links+branding+screenshot), `/testosterone`, `/weight-loss`, `/labs`, `/growth-hormone-peptides`, `/hair-growth`, `/oxytocin-calming-cream`, `/about-us` (markdown+links+screenshot each) — 8 pages via Firecrawl (`fc.py`), 2026-05-31; map returned 337 URLs (mostly `/resources/` blog + `/white-paper/` + paid-LP funnel slugs); catalog reconstructed from homepage links.
- **Verify:** all sourceURLs matched, all bodies md5-unique (clean — no §5.1 geo/cache contamination).
- **Credits:** not recorded this run.
- **Couldn't get:** full pricing ladders (sit behind intake flow on `app.maximustribe.com`; public "Starting at" anchors only).
