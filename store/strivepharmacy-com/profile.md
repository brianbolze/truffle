---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: strivepharmacy.com
name: Strive Pharmacy
aliases: ["Strive Compounding Pharmacy", "strive-pharmacy"]
parent: []
owns: []
socials:
  linkedin: https://www.linkedin.com/company/strivepharmacy/
  instagram: https://www.instagram.com/strivepharmacy/
  facebook: https://www.facebook.com/strivepharmacy/
  youtube: https://www.youtube.com/channel/UCT1E6y8HvexQRZAiabUbuQw
  tiktok: https://www.tiktok.com/@strivepharmacy
  x: https://twitter.com/strivepharmacy
  pinterest: https://www.pinterest.com/strivepharmacy/
external:
  crunchbase: https://www.crunchbase.com/organization/strive-pharmacy
  yelp: https://www.yelp.com/biz/strive-pharmacy-gilbert

# Capture meta
captured_at: 2026-06-02
capture_method: firecrawl
site_notes: "Webflow (data-wf-*, website-files.com in rawHtml; branding.designSystem ignored per playbook §5.4). Cloudflare-fronted (301 strivepharmacy.com -> www.strivepharmacy.com; x-wf-region header). Mega-nav + footer render OUTSIDE markdown — recovered from rawHtml <header> via `fc.py signals` + homepage links. Nav splits Providers vs Patients into parallel trees (same service taxonomy, /providers/* vs /patients/* URLs). Commerce is multi-platform: marketing on Webflow, supplements shop on shop.strivepharmacy.com (Shopify), Rx ordering/refill on LifeFile (host5*.lifefile.net), orders on orders.strivepharmacy.com. JSON-LD = @type Pharmacy, HQ 1275 E Baseline Rd #104, Gilbert AZ 85233. No prices on any captured page (pricing gated to pricing@strivepharmacy.com / per-provider account). A persistent empty 'CART' template + 'Submit Form' newsletter Cloudflare-Turnstile block append to every page's markdown — noise."
key_pages:
  about: /about
  become_a_provider: /become-a-provider
  providers: /providers
  weight_management_providers: /providers/weight-management-medications
  higher_standards: /higher-standards
  find_a_provider: /find-a-provider
  partnership: /partnership
  patients: /patients
  medications: /medications
  faq: /faq
unverified_fields:
  - "No pricing anywhere on captured pages — pricing is per-provider-account / emailed (pricing@strivepharmacy.com). All offering lines are [on-request]."
  - "‘1,000 employees / new Mesa AZ HQ’ and ‘striving since 2018’ are self-reported (blog headline + homepage tag), not independently verified."
  - "Accreditations (PCAB/ACHC, NABP, LegitScript) are self-claimed on /higher-standards — verbatim, not third-party verified here."

description: "A compounding pharmacy that makes patient-specific, prescriber-ordered compounded medications across ~14 therapeutic categories (weight, hormones, sexual/skin/hair, mental health, longevity), routing to licensed providers via a clinic/telehealth partner network and to patients through a provider directory."

# Classification
entity_type: Company
target_market: [B2B2C, B2B, B2C]
offering_category: [Biotech / Pharma Products, Services / Consulting]
portfolio_shape: Catalog
business_model: Transactional / One-time
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against homepage screenshot.
logo_url: https://cdn.prod.website-files.com/67ae6add43dacf04f7579286/67ae6db233299da66d1ed5ab_favicon.png  # STRAIN: branding.images.logo is an inline data-URI SVG (brand-blue wordmark); favicon used as the storable URL fallback. JSON-LD `logo` is a google-form share JPG, not a brand mark — skipped.
brand_colors: { primary: "#1E64F0", accent: "#FF8C78", background: "#FCFAFA" }  # STRAIN: #1E64F0 (brand blue) is the dominant hue & logo/link color despite branding payload listing it as 'accent'; #FF8C78 (warm coral) is the secondary accent (vial caps, color blocks). branding 'primary' #FF8C78 is the inverted slot, §6.
fonts: [FeatureDisplay, Georgia, HafferXH]  # heading stack = FeatureDisplay -> Georgia -> sans (a display serif character); body = HafferXH (grotesque sans). Cartograph = mono accents.
color_scheme: light
design_framework: webflow
---

## Overview

Strive Pharmacy is a 503A compounding pharmacy positioning itself as "More Than Medicine" — a people-first alternative to mass-produced "one-size-fits-all" pharma. It compounds patient-specific prescriptions (only on a provider's order; explicitly does **not** dispense in-office stock) across roughly 14 therapeutic categories, and routes two audiences in parallel: **providers** (a clinic/telehealth partner network they recruit via "Become a Provider") and **patients** (who are pushed to find a partnered provider, refill, or shop OTC supplements). Founded 2018; self-reports crossing 1,000 employees and a new Mesa, AZ headquarters in Dec 2025, plus a 2025 acquisition of a 503B manufacturing facility in Alachua, FL (signaling a move toward outsourced-facility scale). HQ in Gilbert, AZ.

## What they offer

Compounded medications organized by therapeutic category (each category page lists named formulations; no prices shown anywhere — pricing is per-provider-account, so every line is `[on-request]`):

- **Weight Management:** Semaglutide/Glycine/B12, Tirzepatide/Glycine/B12, Amlexanox, LDN Flex-Dose Tablet, Phentermine HCl (Commercial) `[on-request]`
- **Hormone Support:** Testosterone Cypionate, Elevate-T, Kyzatrex (Commercial), Oxandrolone, Gonadorelin, Progesterone, Sermorelin, Nature Throid (Compound), Testosterone Topical, Test Booster `[on-request]`
- **Sexual Wellness:** Olympus Peak, Vaginal Rejuv S, Estriol Vaginal Cream, Euphoria Cream O, Trimix, Olympus + `[on-request]`
- **Skincare:** Radiance, Luminance, Flawless, Anti-Aging 2 S, Cashmere, Vitality Plus, Calming, Stella+ `[on-request]`
- **Hair Health:** Men's / Women's Scalp Solution, Ivy Hair Tablet, Follicle Fix, GHK-Cu, Cedar / Willow Hair Tablet `[on-request]`
- **Mental Health:** Methylcobalamin (Synapsin), NAD+, Methylene Blue, Sermorelin, Progesterone, LDN, VIP, Ketamine `[on-request]`
- **Longevity / Anti-Aging:** GHK-Cu, NAD+, Methylene Blue, Sirolimus, Sermorelin, Glutathione, Stella+ `[on-request]`
- **Immune Wellness (auto-immune):** Glutathione, NAD+, VIP, LDN `[on-request]`
- **Pain Management:** VIP, LDN, Ketamine `[on-request]`
- **Physical Performance:** Sermorelin, Oxandrolone, Testosterone Cypionate, NAD+ `[on-request]`
- **Digestive / Gut Support:** VIP, LDN `[on-request]`
- **Nutrient / Vitamin Replacement:** Methylcobalamin (Synapsin), Vita Complex `[on-request]`
- **Veterinary Services** (listed as a provider specialty; pet compounding) `[on-request]`
- **Strive Supplements (OTC):** retail supplements line sold on shop.strivepharmacy.com (Shopify), the only non-prescription, directly-purchasable product family `[on-request]`

Catalog-shaped: a large, un-enumerable medication list surfaced through category × named-formulation cards.

## How it works / model

Two-sided routing off one site. **Providers:** "Become a Provider" → a 4-step practice-onboarding form (contact, practice/platform info, billing model, business profile) → Strive account → provider prescribes via LifeFile e-prescribing → Strive compounds patient-specific and ships. Strive recruits both **clinic partners** and **telehealth partners** (separate sub-pages) and offers a **Partnership** track for telehealth platforms. **Patients:** can't buy Rx directly — funneled to "Find a Strive Provider" (a searchable directory), to refill an existing Rx (LifeFile), or to buy OTC supplements. Money is made selling compounded Rx (billed either to office or patient — a form-selected billing model) plus OTC supplement retail and a wholesale program. 503A model = patient-specific scripts only, no office stock.

## Positioning & audience

Targets licensed providers (aesthetic, hormone/regenerative, functional/integrative, telehealth) as the buyer, with patients as the demand they activate. Claimed edge is twofold: **personalization** ("we reject the one-size-fits-all approach"; custom dose/form/ingredient, allergen removal) and **quality rigor that beats industry minimums** (weekly potency testing vs. annual; ±3% potency variance vs. ±10% accepted; sterility/endotoxin testing every batch; FDA-registered + GLP-1 Green List sourcing; PCAB/ACHC, NABP, LegitScript accreditations). Heavy provider-education motor: "Strive Sessions" webinars + a deep provider-facing blog. A recurring activist frame — "Personal medicine is under attack. We're fighting back." / "Defend Personal Medicine" — positions them against regulatory/big-pharma threats to compounding.

## Nav structure

Mega-nav splits Providers vs Patients into parallel service trees (identical category set, different URL roots). Recovered from rawHtml <header> + homepage links:

```
- Providers
  - Our Services (provider): Weight Management, Hormone Support, Mental Health, Sexual Wellness, Longevity, Hair Health, Pain Management, Digestive Support, Immune Wellness  — /providers/<category>-medications
  - View All Services — /providers
  - Become a Provider — /become-a-provider
  - Partnerships (telehealth) — /partnership
  - Provider tools: Join Our Provider Network — /become-a-provider
- Patients
  - Services (patient): Weight Management, Hormone Support, Mental Health, Sexual Wellness, Longevity, Hair Health, Pain Management, Skincare, Immune Wellness — /patients/<category>-medications
  - View All — /patients
  - Prescriptions: Refill Prescription (LifeFile), Contact Customer Care (go.strivepharmacy.com), Track Your Order (orders.strivepharmacy.com)
  - Find a Strive Provider — /find-a-provider
  - Patient Resources / Instructional Guides — /instructional-guides
- Resources
  - Popular Topics: Trimix / Intramuscular / Subcutaneous Self-Injection Guides — /instructional-guides/<guide>
  - View All Guides — /instructional-guides
  - FAQs / Help Center — /faq
  - Strive Blog — /blog ; Sessions — /sessions
- Company
  - Our Story — /about ; Our Team — /team ; Careers — /careers
  - Blog & Articles — /blog ; News & Press — /news-and-press
  - Strive Locations — /locations ; Contact — /contact
- Products
  - Medications — /medications
  - Supplements — shop.strivepharmacy.com (Shopify)
  - Strive Merch — strivemerch.com
  - Wholesale Program / Application / Catalog — myshopify wpdapp
- Top-level CTAs: FIND A PROVIDER — /find-a-provider ; Become a Provider — /become-a-provider ; My Account (LifeFile doctor login) ; Get Rx Refill (LifeFile patient)
- Utility bar: Find a Strive Location, Need Help? We've Got You (Contact), New in Shop: Strive Supplements, Track Your Strive Rx Order
```

## Credibility & proof

All self-reported (verbatim, flagged):

- **Accreditations (claimed):** "PCAB/ACHC Accreditation — We voluntarily pursue one of the toughest accreditations in the industry." · "NABP Accreditation" · "LegitScript Certification — Trusted verification of our legitimacy online."
- **Sourcing claims:** "Every ingredient we use comes from FDA-registered facilities." · GLP-1 ingredients "sourced exclusively from FDA-official 'GLP-1 Green List' facilities." · "Each ingredient shipment arrives with a Certificate of Analysis (COA)."
- **Testing rigor (the headline proof):** "Potency Testing: Weekly, Not Yearly" — "The industry standard? Once-a-year. The Strive standard? Randomized batches tested multiple times every week." · "Strive aims for a ±3% variance—far tighter than the ±10% that's widely accepted." · "Every single sterile batch is tested for sterility and endotoxins… Our 99.9%+ pass rate."
- **Licensing:** "We're licensed in every state where our medications are dispensed."
- **503A compliance line (on the provider form):** "As a 503a pharmacy, Strive Pharmacy only fills patient specific prescriptions and does not dispense in-office stock."
- **Scale (self-reported, blog):** "A Milestone Week at Strive: 1,000 Employees, a New Headquarters" (Dec 2025); "Striving Since 2018"; 2025 acquisition of a 503B manufacturing facility in Alachua, FL.
- No third-party testimonials, customer-count badges, or press logos on captured pages. Provider/patient trust is carried by accreditation claims + a large provider-education content library ("Strive Sessions" webinars, provider blog) rather than named quotes.

## Visual & brand impression

Premium, editorial, "soft-clinical." Light-first (#FCFAFA off-white) over expansive blue gradient fields (#1E64F0 brand blue), warmed by a coral/peach accent (#FF8C78) on product caps and color blocks. Headlines set in a display serif (FeatureDisplay → Georgia) with an italic emphasis word in the brand voice ("Tailored medicine for *powerful* outcomes."; "Personalize every *plan.*"); body in a clean grotesque sans (HafferXH). Photography is the differentiator: real, sun-lit people (families, athletes, older adults) shot in a warm documentary style, intercut with macro product/texture shots (vials, capsules, oil-on-water, gel "squiggles"). Square-cornered components (0px radius), generous whitespace, big type scale (h1 ~84px). Signature motion device: per-character animated reveals — pull-quotes and section labels render one letter at a time ("We approach compounding from the conviction that life isn't one-size-fits-all, and neither is medicine."), plus a repeating "STRIVE FOR MORE" marquee. Reads more like a wellness/lifestyle brand than a pharmacy — deliberately.

## Strategic read

The interesting move for a B2B distributor reference: Strive sells a *regulated, gated* product (compounded Rx, no prices, provider-only) but wraps it in *consumer-grade brand warmth* and an *activist mission* ("Defend Personal Medicine"). Trust is manufactured through transparency theater done well — concrete, quantified quality claims (±3% vs ±10%, weekly testing, 99.9% pass, named accreditations) rather than vague "trusted by." The provider-onboarding form is a qualification funnel disguised as a contact form (it scores Rx volume, provider count, states licensed, billing model) — high-signal for any B2B medical lead-gen. The provider-education content engine (Sessions + blog) is the real moat and the patient-side directory is the demand-capture loop.

## Provenance

- **Pages:** 6 analyzed via Firecrawl (maxAge:0, US, waitFor) — homepage, /about, /become-a-provider, /providers, /providers/weight-management-medications, /higher-standards. Map returned 194 URLs. Mega-nav/footer recovered from rawHtml <header> (`fc.py signals`) since they fall outside markdown.
- **Verify:** all 6 sourceURLs matched; all 6 body md5s unique (no §5.1 contamination).
- **Credits:** 7 (1 map + 6 scrapes). 1174 remaining post-run.
- **Couldn't get:** any pricing (per-provider-account, emailed); third-party verification of accreditation/scale claims; the live provider-directory data and the LifeFile/Shopify sub-apps (out of marketing-site scope).
- **Enriched (model knowledge):** none — identity resolved from the site + JSON-LD.
