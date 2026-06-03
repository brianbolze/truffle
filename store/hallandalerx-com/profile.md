---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: hallandalerx.com
name: Hallandale Pharmacy
aliases: [hallandalepharmacy.com]      # hallandalepharmacy.com 301-redirects here (→ www.Hallandalerx.com → hallandalerx.com)
parent: []
owns: []
socials: {x: "https://x.com/hallandalerx", instagram: "https://instagram.com/hallandalepharmacy/", linkedin: "https://www.linkedin.com/company/hallandalepharmacy/"}   # from footer anchors (homepage JSON-LD carried no sameAs); each handle resolves to this entity
external: {}                           # JSON-LD sameAs absent; no third-party records declared on captured pages

# Capture meta
captured_at: 2026-06-02
capture_method: firecrawl
site_notes: "WordPress (custom theme 'hallandale-pharmacy'; wp-content/wp-json, no WooCommerce/Elementor). Nav + footer render in markdown (no JS-wall). Provider lead-gen routes to THREE different URLs across the site (drift, not error): nav/hero/footer CTAs → partner.hallandalerx.com/new-account-request-case (the full Salesforce-style intake form on the LifeFile/partner subdomain); mid-page section CTAs → info.hallandalerx.com/new-account-requests; mobile menu 'Register as a Provider' → hallandalerx.com/new-provider (a lighter WordPress form, different field set + therapeutic-area list). Provider login → host6.lifefile.net:40443/hallandalerx/doctor (LifeFile ERX portal). Product images on hrx-assets.s3.amazonaws.com / hrx-assets CDN. Homepage JSON-LD is generic Yoast (WebPage/WebSite/Breadcrumb only — no Organization, no sameAs)."
key_pages:
  about: /about/
  quality: /quality/
  products: /products
  new_provider_landing: /new-provider/
  new_account_request_form: https://partner.hallandalerx.com/new-account-request-case
unverified_fields:
  - "Per-product pricing not shown anywhere — this is a B2B prescriber catalog (provider account required to transact via LifeFile portal); 517 SKUs listed with strength/form only, no price."
  - "Founding year stated two ways across the site: 'Since 2003' (homepage footer) vs 'Since our establishment in 2004' (about) — site disagrees with itself; reported verbatim, not reconciled."

description: "A 503A compounding pharmacy that supplies custom and shortage-gap medications (hormones, GLP-1 weight-management, peptides, sexual wellness, dermatology) to a national network of 15,000+ licensed prescribers, gating purchase behind a provider account."

# Classification
entity_type: Company
target_market: [B2B]                   # sells to licensed prescribers/practices; patients only via a provider-routed refill portal
offering_category: [Biotech / Pharma Products, Services / Consulting]   # compounded drugs + the compounding-as-a-service relationship
portfolio_shape: Catalog               # 517 SKUs across 15 therapeutic categories — capture shape, not the list
business_model: Transactional / One-time   # per-prescription fulfillment to provider accounts; no membership/subscription surfaced
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload verified against homepage screenshot
logo_url: https://hallandalerx.com/wp-content/themes/hallandale-pharmacy/static/images/header-logo.svg
brand_colors: { primary: "#0870EB", secondary: "#DCECFF", background: "#FFFFFF", text: "#000000" }   # clinical blue on white, pale-blue tints; verified in screenshot (hero CTA, blue full-bleed partnership panel)
fonts: [Neue Haas Grotesk Display, Neue Haas Grotesk Text]   # heading / body — a true grotesk; branding.fonts + screenshot agree
color_scheme: light
design_framework: wordpress            # rawHtml: wp-content ×42, wp-json ×4, custom theme 'hallandale-pharmacy' (no Next/Gatsby/Shopify markers)
---

## Overview

Hallandale Pharmacy is a Fort Lauderdale–based 503A compounding pharmacy positioned as a B2B partner to licensed prescribers, not a consumer brand. It compounds custom and commercially-scarce medications — GLP-1 weight-management injectables (semaglutide, tirzepatide), hormone replacement, testosterone, peptides, IV/vitamin therapy, sexual wellness, dermatology — and sells them to a stated 15,000+ prescribing practitioners nationwide. The pitch to providers leans on quality/compliance (PCAB accreditation, USP 797 / cGMP, a 60,000 sq ft facility) and on solving drug shortages and "treatment gaps in commercial medications." Patients never buy directly; they reach the pharmacy only through a provider, via a patient-refill portal.

## What they offer

Catalog of **517 results** across 15 therapeutic categories (counts verbatim from /products filters); per-SKU listings show strength + dosage form only, **no price** (provider account gates transaction):

- **Weight Management:** GLP-1 injectables, hero of the homepage — e.g. Semaglutide Flex-Dose 1–4 mL (2.5 mg/mL), Semaglutide Double-Strength Flex-Dose 3 mL (5 mg/mL), Tirzepatide Flex-Dose 1–4 mL (10 mg/mL), Tirzepatide Forte Flex-Dose 4 mL (15 mg/mL) — all Injectable. 41 SKUs `[on-request]`
- **Women's Health:** largest category, 409 SKUs `[on-request]`
- **Men's Health:** 371 SKUs `[on-request]`
- **Hormone Replacement:** 209 SKUs incl. Depo Testosterone, Testosterone Cypionate (Wilshire) 200 mg/mL Injectable `[on-request]`
- **Injectable Supplies:** 69 SKUs `[on-request]`
- **Sexual Wellness:** 57 SKUs `[on-request]`
- **Dermatology:** 53 SKUs `[on-request]`
- **Thyroid:** 30 SKUs `[on-request]`
- **IV Therapy & Supplements:** 22 SKUs — e.g. Bioboost / Bioboost Plus (MIC/B-Complex), Glutathione, Ascorbic Acid (Ascor), Vitamin D3 50,000 IU/mL `[on-request]`
- **Peptide Therapy:** 10 SKUs `[on-request]`
- **Vitality:** 9 · **Fertility:** 8 · **Custom Compound:** 2 (custom strengths, any form) · **Nausea:** 2 · **Ophthalmology:** 2 `[on-request]`

Dosage forms span Cream (105), Capsule (98), Tablet (80), Injectable (68), Troche (43), plus oral drops, gels, ODT, shampoo/conditioner, foam, ointment, serum, eye drops, nasal/topical spray, lollipop. Brand split: Hallandale Pharmacy (348) vs Commercial (169).

## How it works / model

Provider-gated. A prescriber applies via the **New Account Request** form (partner.hallandalerx.com), is onboarded, then transmits prescriptions through LifeFile ERX / Surescripts / EMR-EHR API / fax, and logs into the LifeFile doctor portal (host6.lifefile.net) to manage orders. Patients are served only downstream — they submit refill requests through a patient portal, routed back to their provider. Revenue is per-prescription fulfillment; no subscription or membership surfaced.

## Positioning & audience

Targets licensed medical providers (the form's "Applicant Title" options run Owner/Prescriber, Pharmacy Liaison, etc.; "How do you see your patients?" = in medical office / telehealth / both). Claimed edge: pharmaceutical-grade quality + compliance ("As a 503A designated pharmacy, we are held to the standards of USP. Exceeding these standards is our commitment"), speed ("delivering tailored prescriptions in the shortest amount of time"), and a shortage/treatment-gap wedge. Tone is premium-clinical and partner-framed ("Where health and partnership meet").

## Nav structure

```
- Products — /products
  - All Products — /products
  - Women's Health — /products/?_product_categories=womens-health
  - Men's Health — /products/?_product_categories=mens-health
  - Hormone Replacement — /products/?_product_categories=hormone-replacement
  - Sexual Wellness — /products/?_product_categories=sexual-wellness
  - Dermatology — /products/?_product_categories=dermatology
  - Weight Management — /products/?_product_categories=weight-management
  - IV Therapy & Supplements — /products/?_product_categories=iv-therapy-supplements
  - Peptide Therapy — /products/?_product_categories=peptide-therapy
  - Fertility — /products/?_product_categories=fertility
  - Vitality — /products/?_product_categories=vitality
  - Custom Compound — /products/?_product_categories=custom-compound
  - Ophthalmology — /products/?_product_categories=ophthalmology
  - Nausea — /products/?_product_categories=nausea
- About — /about/
- Quality — /quality/
- Licenses — /licenses/
- Support — /support/
- Careers — /careers/
- Patient Refill — partner.hallandalerx.com/patient-refill-request
- (utility) New Provider — partner.hallandalerx.com/new-account-request-case
- (utility) Login — host6.lifefile.net:40443/hallandalerx/doctor
- (footer also) News — /news/
```

## Credibility & proof

All self-reported (record, don't endorse):
- **PCAB accreditation:** "we hold accreditation from PCAB (Pharmacy Compounding Accreditation Board)" — logo in header badge + footer.
- **503A / USP 797 / cGMP:** "As a 503A designated pharmacy, adhering to USP 797 standards is fundamental… we go beyond compliance"; "the incorporation of notable cGMP practices."
- **Facility scale:** "State of the art facilities totalling to 60,000 square feet"; "6000 sq ft cleanroom… adhere to CGMP standards… touchless door technologies… Constant 24-hour monitoring."
- **Network stats (about page):** "15,000+ Prescribing Practitioners", "450+ Employees and growing", "60,000 Square-foot facility".
- **Personnel:** "a former FDA cGMP quality inspector serving as our Quality Auditor"; microbiologists, facility engineers, formulation team.
- **API sourcing:** "We collaborate exclusively with FDA-registered API manufacturers… verify the Certificate of Analysis (COA) internally."
- **Testimonial (single, repeated site-wide):** "Working with Hallandale is super easy. They always have the prescriptions my patients need and their customer service is amazing." — Dr. James Patterson, Central Medical Group / Seattle, WA. (Name spelled "Patterson" in body; image file is "dr-james-paterson.jpg".)

## Visual & brand impression

Premium-clinical / medical-device end of the spectrum — confirmed against the homepage screenshot. A true grotesk type system (Neue Haas Grotesk Display/Text), large left-aligned headline ("Where wellness is mastered, not managed."), generous white space, and one art-directed product still per fold (a hand holding a blue-labeled pill bottle on a soft gradient). Identity color is a single clinical blue (#0870EB) on white with pale-blue (#DCECFF) tints; CTAs are fully-pill-shaped (border-radius 9999px) blue buttons. Distinctive devices: (1) a **mid-page full-bleed black interstitial** carrying a single rotating action verb with a cursor/arrow glyph; (2) an **action-verb marquee word-strip** — "Live well ◣ Refine Prescribing ◣ Feel supported ◣ Wait less ◣ Experience more" with arrow separators; (3) a **full-bleed blue "Where health and partnership meet" panel** as the provider-CTA band; (4) a dark footer with a vertical logo lockup, a literal barcode SVG, an "RX Only" mark, and "Since 2003". Numbered value props (01 Proven expertise → 04 Digitally different). Reads expensive, restrained, and built to signal regulatory seriousness to clinicians.

## Provenance

- **Pages:** homepage, /about/, /quality/, /products, /new-provider/, partner.hallandalerx.com/new-account-request-case — all firecrawl, markdown + links + fullPage screenshot (homepage also html/rawHtml/branding/images).
- **Verify:** all 6 sourceURLs matched; all 6 body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 7 (1 map + 6 scrapes), 1174 remaining.
- **Couldn't get:** per-SKU pricing (B2B, account-gated — not published anywhere); Organization JSON-LD / sameAs (Yoast block is generic). Two unverified_fields: account-gated pricing; founding-year self-contradiction (2003 vs 2004).
- **Enriched (model knowledge):** none — all facts trace to captured pages.
