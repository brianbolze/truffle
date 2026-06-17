---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"
domain: kingsbergmedical.com
name: Kingsberg Medical
aliases: ["Kingsberg Medical Clinic"]
legal_entity: ""
parent: []
owns: []
socials: {}
external: {}
captured_at: 2026-06-17
capture_method: firecrawl
site_notes: "WordPress/WP Rocket site with a large SEO-style route set; the indexed product catalog lives at /product/ and the homepage repeats a medication detail carousel. Public product prices are sparse: treatment ranges live on cost/FAQ pages, not PDP buy boxes. Testosterone Cypionate, Propionate, and Enanthate nav URLs returned duplicate /testosterone-injections/ bodies, so keep one canonical injection page in active captures. JSON-LD logo URL is stale/404; wordmark is a verified header screenshot crop."
key_pages:
  homepage: /
  product_index: /product/
  about: /about-us/
  services: /services/
  get_started: /get-started/
  hormone_testing: /hormone-testing/
  growth_hormone: /growth-hormone/
  testosterone: /testosterone/
  testosterone_injections: /testosterone-injections/
  semaglutide: /product/semaglutide/
  sermorelin: /product/sermorelin/
unverified_fields:
  - "State-by-state availability list — site says services depend on physician licensure and state law, but does not enumerate states."
  - "Named pharmacy partners and 503A/503B lane — site says licensed US pharmacies, but names no pharmacy."
  - "Exact all-in per-patient treatment prices — ranges are public, final cost depends on prescription, dose, labs, and insurance."
  - "Legal entity — no site-derived legalName or footer entity found in the captured packet."
  - "Insurance billing posture — site says some costs may be covered by insurance, but does not state Kingsberg bills insurance."
description: "Runs a Fort Lauderdale hormone-replacement clinic that routes adults through consultation, lab testing, and prescriptions for HGH, testosterone, sermorelin, semaglutide, and hormone panels."
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Transactional / One-time
primary_industry: Healthcare & Life Sciences
logo_url: assets/wordmark.png
logos:
  wordmark: { src: assets/wordmark.png, w: 340, h: 120 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=kingsbergmedical.com&sz=256", px: 32, transparent: true }
brand_colors: { primary: "#3D5B35", secondary: "#EDF9E5", accent: "#49A942", background: "#FFFFFF" }
fonts: [Bloger, "Fira Sans", Georgia]
color_scheme: light
design_framework: wordpress
---

## Overview

Kingsberg Medical is a hormone-replacement and longevity-oriented clinic based in Fort Lauderdale. The site focuses on adult growth hormone deficiency, low testosterone, sermorelin, semaglutide, and hormone testing, with a funnel that starts online or by phone and then routes through labs, physical exam, physician review, and prescriptions where appropriate.

The page-attested compliance posture is state-limited: services are available only where the physicians are licensed and the service is permitted. The pharmacy statement is also narrow: "All prescriptions from Kingsberg Medical are filled by licensed US pharmacies."

## What they offer

- **Growth hormone therapy:** HGH evaluation and prescriptions, with Omnitrope, Zomacton, Genotropin, Norditropin, Humatrope, and Saizen surfaced in the medication carousel; public range says "$500.00 to $1000.00 or more per month" `[partial]`
- **Testosterone therapy:** Low-testosterone diagnosis and TRT, including testosterone injection pages and references to cypionate, propionate, enanthate, Depo Testosterone, and Watson Testosterone; public range says "$200.00 to $350.00 per month" `[partial]`
- **Sermorelin:** Compounded injectable secretagogue line, positioned as a growth-hormone-related therapy; no price on captured PDP `[on-request]`
- **Semaglutide:** Compounded injectable GLP-1 weight-loss medication routed through pre-screening and virtual consultation; no price on captured PDP `[on-request]`
- **Hormone testing:** Super and Complete male/female panels through LabCorp, with results typically in "24-72 business hours"; no panel price captured `[on-request]`
- **Consultation / intake:** Get Started form, medical history form, and phone/contact path before lab review and physician prescription `[on-request]`

Per-SKU detail, images, and price-source anchors live in `offerings.md`.

## How it works / model

- **Intake:** Users fill out a form, medical history, or call; the get-started page asks for a ZIP code.
- **Testing:** Kingsberg says it schedules blood testing and a physical exam near the patient's home or office.
- **Prescription:** If lab work indicates growth hormone deficiency or low testosterone, "one of our local doctors" prescribes hormone replacement therapy.
- **Fulfillment:** Prescriptions are filled by licensed US pharmacies, with dispensing limited to states where the pharmacies are authorized to operate.

## Positioning & audience

The site targets adults, both men and women, seeking hormone optimization rather than a narrow men's-health-only offer. Its own proof language emphasizes specialization in hormone replacement therapy, "more than 14,000 men and women," and a decade-plus patient-experience claim. Growth hormone and testosterone are co-led in the hero, nav, and medication carousel; semaglutide appears as a newer product-card addition rather than the core front door.

## Nav structure

- **Primary:** Home, About Us, Services, Growth Hormone, Testosterone, Hormone Testing, Get Started, contact.
- **Growth Hormone:** growth hormone overview, injections, cost pages, brand/PDP routes for Omnitrope, Zomacton, Genotropin, Norditropin, Humatrope, Saizen, and related how-to/FAQ articles.
- **Testosterone:** low-testosterone overview, testosterone injections, testosterone therapy cost, insurance, cypionate/propionate/enanthate article routes, and related doctor/how-to pages.
- **Sermorelin:** product PDP plus benefits, prescription, comparison, and combination/FAQ article routes.
- **Product index:** Semaglutide; Super Male Panel; Super Female Panel; Complete Male Panel; Complete Female Panel; Sermorelin; Saizen; Humatrope; Norditropin; Genotropin; Zomacton; Omnitrope.

## Credibility & proof

- **Patient claim:** "Over the past 10 years we have helped more than 14,000 men and women" — self-reported on About/Homepage, not independently verified.
- **Named clinicians:** The captured pages name Dr. Paul Calise and Dr. Gordon J. Crozier.
- **Labs:** Hormone panel pages say Kingsberg uses LabCorp and emails results or provides a patient-portal path.
- **Pharmacy:** The site claims prescriptions are filled by licensed US pharmacies; no named pharmacy partner or accreditation surfaced.

## Visual & brand impression

The June 17 homepage screenshot shows an older green-and-white WordPress clinic presentation: mountain/doctor stock hero imagery, dense nav, green CTA buttons, and long medical explainers. It is content-rich and clearly medical-service oriented, but visually dated and template-heavy; the homepage medication carousel section captured as a dark-green band with lazy/blank product media in places. The blind visual layer in `visual.md` supersedes this lightweight read.

## Provenance

- **Pages:** Firecrawl map plus 29 active scrapes: homepage, product index, about/services/get-started/intake pages, growth hormone/testosterone/hormone-testing pages, 12 PDPs/panel pages, and 6 cost/insurance pages.
- **Verify:** Active scrape ledger passed sourceURL, md5 uniqueness, and junk soft-404 checks before writing; duplicate testosterone ester alias pages were probed and excluded because they returned the same body as `/testosterone-injections/`.
- **Credits:** Active packet records 30 Firecrawl credits in the manifest (1 map + 29 active scrapes); 3 extra duplicate-alias probes were performed then excluded from the active ledger.
- **Couldn’t get:** Exact all-in treatment pricing, state coverage list, named pharmacy partners, legal entity, or external verification of physician/patient claims.
- **Structured layer:** Homepage JSON-LD described a MedicalBusiness with areaServed US, `priceRange: "$$"`, HRT/endocrinology keywords, and an empty `sameAs`; its logo URL was stale/404, so logos were resolved from the header screenshot and Google S2 favicon.
- **Run profile:** guided — full `/research-company` scope requested with cohort pack, logos, offerings, and visual evidence.
