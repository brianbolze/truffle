---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: marquelongevitylab.com
name: The Marque Longevity Lab
aliases: ["The Marque", "Marque"]
parent: []
owns: []
socials: { instagram: "https://www.instagram.com/themarquelongevitylab" }
external: {}

# Capture meta
captured_at: 2026-06-10
capture_method: firecrawl
site_notes: "Webflow (data-wf-, website-files.com). Booking + memberships + all pricing live in a gated Zenoti webstore (themarque.zenoti.com) — NO prices anywhere on the marketing site. Real treatment menu is on /services (the #aesthetics/#hormone/#medical-weight-management/#recovery/#lab-testing anchors); the per-service detail pages (/services/<slug>) are UNBUILT STUBS — identical Lorem-Ipsum template with copy-pasted 'Bioidentical Hormone Therapy' cards, do not roster from them. Homepage JSON-LD is an unfilled placeholder ('Business Name'/'Logo Link'). Contact page main phone (555) 123-4567 is a placeholder; real per-location phones are on /contact. Two physical locations + telehealth in VA & FL."
key_pages:
  services: /services
  about: /about
  contact: /contact
  booking: https://themarque.zenoti.com/webstoreNew/services
  memberships: https://themarque.zenoti.com/webstoreNew/sales/membership/3ceb2777-2fc7-4f5a-ad7a-d17559fbe82b
unverified_fields:
  - "All pricing — no prices published on the site; booking, à la carte service prices, and membership tiers/cost all live behind the Zenoti webstore login."
  - "Membership tiers — site references tier-based perks ('exclusive savings, bundles, priority access, included services based on their tier') but enumerates no tiers or prices."
  - "Provider names/credentials — 'licensed clinicians and specialists' asserted; no named providers on the captured pages."
  - "Site is freshly launched / partially built — per-service detail pages are Lorem-Ipsum stubs; treat captured IA as a point-in-time snapshot, not fixed."

description: "A multi-location precision wellness and longevity clinic that integrates aesthetic medicine, hormone therapy, medical weight management, recovery therapies, and diagnostics into personalized, clinician-supervised programs."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 412, h: 148 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=marquelongevitylab.com&sz=256", px: 256, transparent: false }
  og:       { src: "https://cdn.prod.website-files.com/69612202b82f884faf677b72/697166a86d46ebb0e65aa0ca_Opengraph.png", w: 1200, h: 630 }
brand_colors: { primary: "#51481A", accent: "#F2C1CA", light: "#F4F4D0" }  # STRAIN: olive/bronze primary, dusty-rose + cream accents — vision-confirmed against screenshots
fonts: [Nb Architekt, Times New Roman]
color_scheme: light
design_framework: webflow
---

## Overview

The Marque Longevity Lab ("The Marque") is a precision wellness and longevity clinic that bundles aesthetic medicine, hormone optimization, medical weight management, recovery/performance therapies, and advanced diagnostics under one clinician-supervised model it brands **"Applied Wellness"** — coordinated, multi-disciplinary care rather than disconnected à la carte services. It operates two physical locations (Virginia Beach, VA and Jacksonville, FL) and extends care via telehealth in those two states, with at-home medications/peptides/supplements supplementing in-clinic visits. Positioning is upscale and editorial — "Where Hospitality Meets Holistic Health" — targeting consumers who invest in how they look, feel, and perform.

## What they offer

Five service lines, all clinician-supervised; **no prices are published anywhere on the site — booking and pricing are gated behind a Zenoti webstore**, so every line is `[on-request]`. Per-treatment depth is in `offerings.md`.

- **Aesthetics & Skin Treatments:** wrinkle relaxers, dermal fillers & bio-stimulators, body contouring, microneedling — "natural results" injectables + skin health `[on-request]`
- **Hormone & Longevity Optimization:** bioidentical hormone therapy (with hormone mapping + monitoring), peptides, NAD+, curated supplements/nutraceuticals (incl. **Thorne**) `[on-request]`
- **Medical Weight Management:** GLP-1 and peptide-assisted protocols when appropriate (semaglutide, tirzepatide; also tesofensine, phentermine, naltrexone), nutrition + lifestyle coaching, progress tracking `[on-request]`
- **Recovery & Performance Therapy:** red light therapy, hyperbaric oxygen therapy (HBOT), metabolic repletion / nutrient injections (B12, amino blends, taurine, L-carnitine, glutathione), IV infusion therapy `[on-request]`
- **Lab Testing & Diagnostics:** comprehensive biomarker panels (hormones, metabolism, inflammation, thyroid, micronutrients, lipids, recovery, longevity markers), body composition testing, bloodwork; many members repeat labs every 3–4 months `[on-request]`

## How it works / model

Journey: **personalized consultation → clinical review & diagnostics (labs/biomarkers, baselines) → treatment selection & customization → ongoing oversight & dose adjustment**. Care is sold both **à la carte** ("all individual services are available à la carte") and via **memberships** (Zenoti) that add "exclusive savings, bundles, priority access, and included services based on their tier." After an initial in-center consult, many clients use a mix of clinic treatments, at-home meds/peptides/supplements, and digital tools. **No insurance billed; HSA/FSA may apply to certain medical services; itemized receipts available.** Partnered compounding pharmacy: **Olympia Pharmaceuticals** (Orlando, FL). Telehealth offered in **Virginia and Florida**.

## Positioning & audience

Targets discerning B2C consumers ("people who care deeply about how they live and feel in their body") seeking integrated, data-driven longevity care — positioned against both single-service med spas and lighter "wellness" telehealth by combining aesthetics + hormones + metabolic + recovery + diagnostics in one supervised system. Claimed edge: **"Applied Wellness"** — disciplines coordinated so "decisions are informed, progress is easier to sustain," with a hospitality-grade in-clinic experience.

## Nav structure

```
- Services — /services
  - 01 Aesthetics & Skin Treatments — /services#aesthetics
  - 02 Hormone & Longevity Optimization — /services#hormone
  - 03 Medical Weight Management — /services#medical-weight-management
  - 04 Recovery & Performance Therapy — /services#recovery
  - 05 Lab Testing & Diagnostics — /services#lab-testing
  - Explore all services — /services
- About — /about  (incl. FAQ — /about#faq)
- Locations — /contact#locations
- Contact — /contact
- Memberships — themarque.zenoti.com/webstoreNew/sales/membership/...
- Book a consultation — themarque.zenoti.com/webstoreNew/services
```
*(Per-service detail pages exist at `/services/<slug>` but are unbuilt Lorem-Ipsum stubs; the live nav routes to the `/services` anchors.)*

## Credibility & proof

- **LegitScript certified:** verified-approval seal in the footer (links to legitscript.com website checker for marquelongevitylab.com).
- **Licensed-clinician oversight:** repeatedly asserted — "all optimization, injections, hormones, and peptides are prescribed, monitored, and overseen by licensed providers."
- **Named pharmacy partner:** Olympia Pharmaceuticals (Orlando, FL) — disclosed in the FAQ.
- **Testimonials:** five 5-star reviews quoted verbatim (e.g. "Top to bottom a lovely experience… a delightfully well-trained staff…") — site-curated, unattributed, no source/aggregate rating.
- **Self-reported member outcomes** (flagged self-reported): "improved daily energy and stability," "enhanced skin quality," "better weight control and body composition," "reduced stress and faster recovery."

## Visual & brand impression

Polished, editorial luxury-wellness aesthetic with clear design maturity. Dark hero with confident, fitted-wardrobe models on black gives way to sections in a muted earth palette — olive/bronze (`#51481A`), cream/ivory (`#F4F4D0`), dusty rose/mauve (`#F2C1CA`), and sage. Typography pairs a distinctive condensed display ("Nb Architekt") with serif body copy. The brand mark is a bracketed-"M" monogram (used as logomark/og) plus a stacked "THE MARQUE / LONGEVITY / LAB" wordmark. Overall read: aspirational, calm, clinical-but-warm — "hospitality meets health."

## Provenance

- **Pages:** homepage, /services, /services/{aesthetics-skin-treatments, hormone-longevity-optimization, medical-weight-management, recovery-performance-therapy, lab-testing-diagnostics}, /about, /contact — 9 pages, Firecrawl (maxAge:0, location US, waitFor). The 5 per-service detail pages were unbuilt Lorem-Ipsum stubs (no real content); the treatment menu was read from /services anchors + /about FAQ.
- **Verify:** all sourceURLs matched; all 9 bodies md5-unique; no junk soft-404s.
- **Credits:** 10 (1 map + 1 homepage + 8 key pages); logos module added no credits (reused cached payload + headed fetches).
- **Couldn't get:** any pricing (Zenoti-gated), membership tiers/cost, named providers — see unverified_fields.
- **Run profile:** express — emphasis "logos and offerings"; +logos, +offerings.
