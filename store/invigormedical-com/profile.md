---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: invigormedical.com
name: Invigor Medical
aliases: ["Invigor Medical LLC"]      # legalName (JSON-LD)
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/invigormedical1/
  instagram: https://www.instagram.com/invigormedical/
  linkedin: https://www.linkedin.com/company/invigor-medical
  youtube: https://www.youtube.com/@InvigorMedical
  x: https://twitter.com/invigorm
  pinterest: https://www.pinterest.com/InvigorMedical/
external: {}                          # JSON-LD sameAs carried only owned channels; no 3rd-party records found

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress + WooCommerce + Breakdance page builder; FunnelKit checkout + Stripe; PostHog/Segment/Clarity/Zoho analytics. Catalog = /plans/<sku> PDPs grouped under /function/{weight-loss,longevity,sexual-health} categories. PRICES: the full SKU set + prices render on the HOMEPAGE carousels (the price source) — /function category pages omit prices, PDPs show one price each. Map is ~470 URLs, mostly WP content-marketing noise (/articles, /author/*, /contributor/*, /topics/*, /learn/*, /category/* — filter out). All Rx compounded via named partner pharmacies; no membership. About-page hero carries leftover 'courier service' template lorem filler (ignore). MedicalClinic JSON-LD: HQ 5226 Outlet Dr, Pasco WA; founded 2018-07-26; phone 1-888-966-4854."
key_pages:
  homepage: /
  about: /about-invigor/
  weight_loss: /function/weight-loss/
  longevity: /function/longevity/
  sexual_health: /function/sexual-health/
  plans_index: /plans/
  quiz: /quiz/personalized-health-quiz/
  trt: /plans/testosterone-replacement-therapy-injection/
unverified_fields:
  - "Customer/review counts are self-reported and inconsistent across pages (homepage '35,000+ Happy Customers', '1,000+ 5-Star Reviews', '4.7 Average Rating'; embedded widget '4.9 rating of 1155 reviews'; /about '4,000+ Reviews') — recorded verbatim, none independently verified."
  - "pay_model — no HSA/FSA/insurance/cash-pay language found across 11 captured pages; payer rail genuinely unstated (Stripe checkout, per-med pricing imply cash-pay but the site does not say so)."
  - "Prices/IA are a point-in-time snapshot, not fixed — homepage carousels rotate and TRT runs a '$49 get-started' promo; re-check before trusting a number."
  - "Micro-dose GLP-1, GLP-1+GIP micro-dose, and ReGrow appear in nav but no price rendered on captured pages."

# Description — one sentence
description: "A direct-to-consumer telehealth clinic that prescribes GLP-1 weight-loss, TRT, sexual-health, and longevity/peptide treatments to U.S. adults through 100%-online consultations, fulfilled by partnered compounding and retail pharmacies."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against screenshot
logo_url: https://invigormedical.com/wp-content/uploads/invigor-logo-navbar.webp   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: "https://invigormedical.com/wp-content/uploads/invigor-logo-navbar.webp", w: 200, h: 65 }                              # "im" monogram + "Invigor MEDICAL" — the real navbar brand mark
  logomark: { src: "https://www.google.com/s2/favicons?domain=invigormedical.com&sz=256", px: 192, transparent: true }                   # circular blue "im" wave monogram; transparent corners (it's a disc, no baked rectangle)
  og:       { src: "https://invigormedical.com/wp-content/uploads/social-share.jpg", w: 1000, h: 650 }                                   # declared og / JSON-LD primary image; caption "Online Women's and Men's Health Clinic"
brand_colors: { primary: "#2E4787", accent: "#3F71F4" }   # navy + bright blue; brand hue is blue (wordmark + CTAs), confirmed on screenshot
fonts: [Oswald, Open Sans]            # Oswald (condensed headings) + Open Sans (body) — branding.fonts roles, verified against screenshot headings
color_scheme: light
design_framework: wordpress           # rawHtml: wp-content, WooCommerce, Breakdance builder (NOT a custom SPA)
---

## Overview

Invigor Medical (legal entity **Invigor Medical LLC**) is a direct-to-consumer **telehealth clinic** founded in 2018 and headquartered in Pasco, Washington, billing itself an **"Online Women's and Men's Health Clinic"** that is **"50 States Licensed."** Its JSON-LD self-describes it as a clinic *"dedicated to optimizing health, performance, and longevity through physician-guided treatments and evidence-based care."* The model is the standard DTC-Rx funnel: a customer picks a treatment (or takes a quiz), completes an online medical intake, a licensed clinician reviews and prescribes if appropriate, and a **partner pharmacy ships** the medication. Care is **"100% online"** with no membership — *"Flexible, no-commitment treatment plans."*

The catalog spans **three co-equal pillars — Weight Loss, Longevity, and Sexual Health** — totalling ~27 prescription treatments. Most are **compounded** medications (GLP-1, peptides, NAD+, Trimix, PT-141) produced by named partner compounding pharmacies; a minority are generic oral molecules (sildenafil, tadalafil, finasteride). A TRT injection line was recently added (a persistent sitewide **"Now Offering Testosterone Replacement Therapy"** banner).

## What they offer

Three co-equal lines, all prescription, mostly compounded. Prices below are verbatim from the homepage carousels (the price surface); per-SKU detail in [`offerings.md`](offerings.md). "Starting at …" reads as a dose/tier floor `[partial]`; a flat price reads `[published]`.

- **Weight Loss** (`/function/weight-loss/`): compounded **GLP-1 Treatments — "Starting at $225"** `[partial]` and **GLP-1 + GIP Treatments — "Starting at $350 per Month"** `[partial]` (semaglutide/tirzepatide implied by the GLP-1-vs-GLP-1+GIP split, not page-named), plus micro-dose variants, **Lipo B12 — "Starting at $110"** `[partial]` and **LDN Boost — "Starting at $180"** `[partial]`.
- **Longevity** (`/function/longevity/`): the deepest line — cellular health (**NAD+ Injections "Starting At $340 per Month"** `[partial]`, Oral NAD+, Glutathione, Methylene Blue), vitality (**Sermorelin "Starting At $220"** `[partial]`, Oral Sermorelin, **B12 Injections "$90 per Month"** `[published]`, **Enclomiphene "$75 per Month"** `[published]`, **TRT — "Get Started For $49"** `[partial]`), and hair/skin (Finasteride, Oral GHK-Cu, Follicle Fuel, ReGrow).
- **Sexual Health** (`/function/sexual-health/`): ED (**Sildenafil / Tadalafil — "Starting at $100 per Month"** `[partial]`), resistant ED (**Trimix Injections — "$229 per Vial"** `[published]`, **Passion+ — "$300 per month"** `[published]`), and libido (**PT-141 — "$280 per Month"** `[published]`, **Oxytocin — "$220 per Month"** `[published]`, Oxytocin Nasal Spray).

Cohort-specific classification is in [`telehealth.md`](telehealth.md); the full per-SKU roster (27 SKUs, prices, molecules, hero renders) in [`offerings.md`](offerings.md).

## How it works / model

Self-described 4-step flow (homepage): **Step 1 Enroll** (pick a treatment / fill medical forms) → **Step 2 Provider Review** (*"One of our doctors will contact you to talk about your health goals"*) → **Step 3 Receive Treatment** (*"The pharmacy will ship your prescribed items directly to you"*) → **Step 4 Achieve Results**. A **"Personalized Health Quiz"** ("our algorithm will help tailor a treatment plan") is the alternate front door. The consult is **"100% online"** with an *"online consultation"*; no scheduled video visit is advertised (modality of the provider "contact" is unspecified). **Revenue:** à-la-carte sale of individual treatments, mostly recurring monthly (some one-time, e.g. Trimix "per Vial"); checkout via WooCommerce + FunnelKit + Stripe. **No membership / subscription gate** on the catalog.

## Positioning & audience

Targets **U.S. adults of both sexes** ("Women's and Men's Health Clinic") seeking age-/wellness-related optimization — the homepage frames it around aging concerns: *"stubborn weight,"* *"declining libido,"* *"feeling drained,"* *"losing muscle tone."* Tone is **clinical-but-accessible**, leaning into legitimacy: *"Reignite Confidence — Your Health. Your Terms."* and *"Elevate your health. Clinically guided. Results that last."* Sexual-health (Trimix, PT-141, ED) and the new TRT banner skew male, while weight-loss and longevity read gender-neutral. A prominent **clinical-policy disclaimer** distinguishes it from gray-market peptide sellers: *"We do not prescribe medications for bodybuilding, athletic performance, or cosmetic purposes… only addressed when tied to clinically recognized conditions."* Competes with the broad DTC men's/women's-health field (Hims/Hers, Hone, Maximus, and the peptide/longevity wave).

## Nav structure

Complete mega-nav (homepage flyouts), three category columns + a quiz CTA:

```
- Weight Loss — /function/weight-loss/
  - GLP-1 Agonists — /function/weight-loss/glp-1-agonists/
    - GLP-1 Treatment — /plans/glp-1-treatments/
    - GLP-1 + GIP Treatment — /plans/glp-1-gip-treatments/
    - GLP-1 Micro-Dosing — /plans/micro-dose-glp-1-treatments/
    - GLP-1 + GIP Micro-Dosing — /plans/micro-dose-glp-1-gip/
  - Weight Loss Support — /function/weight-loss/weight-loss-support/
    - Lipo B12 Injections — /plans/buy-lipo-b12/
    - LDN (Low Dose Naltrexone) — /plans/low-dose-naltrexone/
  - See All Weight Loss Services — /function/weight-loss/
- Longevity — /function/longevity/
  - Cellular Health — /function/longevity/cellular-health-longevity/
    - NAD+ Injections — /plans/buy-nad-injections/
    - Oral NAD+ — /plans/buy-oral-nad/
    - Glutathione Injections — /plans/buy-glutathione/
    - Oral Glutathione — /plans/oral-glutathione/
    - Methylene Blue — /plans/buy-methylene-blue/
  - Vitality — /function/longevity/vitality-longevity/
    - Sermorelin Injections — /plans/buy-sermorelin/
    - Oral Sermorelin — /plans/oral-sermorelin/
    - B12 Injections — /plans/buy-vitamin-b12/
    - Enclomiphene — /plans/buy-enclomiphene/
    - Testosterone Replacement Therapy — /plans/testosterone-replacement-therapy-injection/
  - Hair & Skin — /function/longevity/hair-loss-longevity/
    - Finasteride — /plans/buy-finasteride/
    - Oral GHK-Cu — /plans/oral-ghk-cu/
    - Follicle Fuel — /plans/follicle-fuel/
    - ReGrow — /plans/regrow/
  - See All Longevity Services — /function/longevity/
- Sexual Health — /function/sexual-health/
  - Erectile Dysfunction — /function/sexual-health/erectile-dysfunction/
    - Tadalafil — /plans/buy-tadalafil/
    - Sildenafil — /plans/buy-sildenafil/
  - Resistant ED — /function/sexual-health/resistant-ed/
    - Trimix Injections — /plans/buy-trimix/
    - Passion+ — /plans/buy-passion/
  - Libido — /function/sexual-health/libido/
    - Oxytocin — /plans/buy-oxytocin/
    - Oxytocin Nasal Spray — /plans/buy-oxytocin-nasal-spray/
    - PT-141 — /plans/buy-pt-141/
    - Passion+ — /plans/buy-passion/
  - See All Sexual Health Services — /function/sexual-health/
- Find a Treatment (quiz) — /quiz/personalized-health-quiz/
```

## Credibility & proof

All trust signals below are **self-reported** unless noted — recorded verbatim, not endorsed.

- **LegitScript-certified:** footer carries a LegitScript certification seal (`legit-script.webp`) — the meaningful third-party health-merchant signal.
- **Licensing:** *"50 States Licensed"*; *"Prescribed by U.S. Doctors, 100% online."*
- **Named clinicians:** *"Meet Our Dedicated Experts"* names **Andrew Hamilton, DO** and **Stephen Jones, MD** (with photos); no dedicated `/physicians` roster page found.
- **Named partner pharmacies:** /about lists **Strive Pharmacy, Tailor Made, Belmar Pharma Solutions, Olympia Pharmacy, and Gogomeds** as "Partnered Pharmacies" — the four compounders + a retail/mail pharmacy.
- **Volume / ratings (self-reported, inconsistent):** homepage *"35,000+ Happy Customers," "1,000+ 5-Star Reviews," "4.7 Average Rating"*; an embedded review widget *"4.9 rating of 1155 reviews"*; /about *"4,000+ Reviews."* Numbers disagree across pages — none verified.
- **"As seen in" press wall:** homepage shows ~20 outlet logos (Forbes, Fox News, NBC, ABC, Yahoo, Business Insider, Healthline, HuffPost, Washington Post, Associated Press, Inc, Benzinga, Parade, Bustle, Livestrong, Deseret News, Medium, HowStuffWorks, Choosing Therapy, Barchart) — a content-citation/"as seen in" wall, self-asserted, links are dead (`/#`).
- **Compliance posture:** "HIPAA-compliant, secure platform"; a clinical-policy disclaimer restricting prescriptions to clinically-recognized conditions (no bodybuilding/cosmetic use).

## Visual & brand impression

Clean, modern, **trust-forward clinical** aesthetic: a medium-blue (#2E4787 navy → #3F71F4 bright blue) and white palette, generous whitespace, condensed Oswald headlines over Open Sans body. The product imagery is a standout — **consistent isolated 3D vial renders, color-coded by molecule** (green GLP-1, blue NAD+/Trimix, coral PT-141, orange Sermorelin), each a clean studio shot on white, frequently "hand-holding-vial" framing. Category sections pair a lifestyle photo (bearded man, older man, smiling couple) with the render cards. A big "im" wave monogram anchors the brand. Overall it reads as a credible, well-resourced DTC telehealth operation rather than a thin dropship storefront — polished but template-built (WordPress/Breakdance), with a few rough edges (leftover "courier service" lorem on the /about hero; duplicated press-logo rows; dead `/#` links).

## Strategic read

- **Compounding-pharmacy router, not a vertically-integrated pharmacy.** Invigor explicitly *"does not supply FDA-approved branded medications. Instead, compounded alternatives… prepared by licensed 503A pharmacies,"* and names five external partner pharmacies. The moat is the clinician network + funnel + brand, not fulfillment — the same structural position (and regulatory exposure) as the compounded-GLP-1/peptide cohort.
- **Peptide-and-longevity-forward.** Beyond the table-stakes GLP-1/ED/TRT, the catalog leans hard into the **longevity/peptide** wave (NAD+, sermorelin, GHK-Cu, methylene blue, glutathione, PT-141) — a wider peptide menu than most DTC men's-health peers, fenced by an explicit "clinical conditions only, no performance/cosmetic use" policy.
- **Generalist with no single front door.** Three co-equal pillars and a rotating hero (GLP-1 + Trimix cards under a TRT banner) — it markets breadth, not a wedge. Good for cross-sell, weaker for a single sharp positioning.
- **Established, not a 2024 startup.** Founded 2018 with a real WA clinic address and a 35k-customer claim — older and more built-out than much of the recent compounded-GLP-1 entrant wave.

## Provenance

- **Pages (11, all `captures/2026-06-04/`, firecrawl):** `homepage` + 3 category pages (`cat-weight-loss`, `cat-sexual-health`, `cat-longevity`, all rich `--homepage`) + `about` + 6 flagship PDPs with `--images` (`pdp-glp1`, `pdp-trt`, `pdp-trimix`, `pdp-pt141`, `pdp-nad`, `pdp-sermorelin`). Map (`/v2/map`, ~470 URLs) used for catalog discovery only.
- **Verify:** all 11 sourceURLs match; all bodies md5-unique. No geo/cache contamination.
- **Credits:** 12 (1 map + 1 homepage + 3 categories + 1 about + 6 PDPs). 565 remaining.
- **Couldn't get:** prices for micro-dose GLP-1 variants + ReGrow (in nav, no rendered price); payer rail (HSA/FSA/insurance) — unstated sitewide; provider-contact modality (phone vs message vs async) — unspecified.
- **Run profile:** guided — emphasis "offerings.md, telehealth cohort pack, logos, product page images"; +offerings (27-SKU roster), +telehealth, +logos, +hero product renders (5 flagship vials promoted to `captures/2026-06-04/images/`).
- **Structured layer:** JSON-LD (MedicalClinic + Organization + WebSite + Person) read — seeded `socials` (sameAs: facebook/x/pinterest/youtube; footer added instagram/linkedin), `aliases` (legalName "Invigor Medical LLC"), HQ address, founding date, phone; `external` empty (no 3rd-party records in sameAs). `logo` JSON-LD pointed at the square `invigor-logo-1.png` (a logomark); wordmark sourced from the navbar mark instead.
