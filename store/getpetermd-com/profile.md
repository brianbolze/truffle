---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: getpetermd.com
name: PeterMD
aliases: ["PeterUncaged MD", "Peter Uncaged MD", "Peter Holdings"]   # rebranded from PeterUncaged MD (see Strategic read); operating entity "Peter Holdings" (about-us team bios)
parent: []
owns: []
socials: { facebook: "https://www.facebook.com/getpetermd/", instagram: "https://www.instagram.com/peter_uncagedmd/", linkedin: "https://www.linkedin.com/company/peter-md" }   # JSON-LD sameAs lists BOTH facebook/getpetermd (current) + facebook/peteruncagedmd (legacy) — kept current-brand FB; IG/LinkedIn still legacy handles
external: { trustpilot: "https://www.trustpilot.com/review/getpetermd.com" }   # JSON-LD sameAs — third-party record

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress + WooCommerce + Elementor (generator meta: Elementor 4.0.7; rawHtml wp-content×1550, woocommerce×153). No JS-wall: full mega-nav + JSON-LD render in the homepage payload — use homepage links/`fc.py signals` for the offering taxonomy. No A/B tool fingerprinted (no VWO/Optimizely); pricing read stable run-to-run. CATALOG BACKBONE: the public, unauthenticated WooCommerce Store API `GET /wp-json/wc/store/v1/products?per_page=100` returns the full priced catalog (145 products, 2 pages) as JSON — the cheapest authoritative roster source (persisted to captures/<date>/wc-catalog.md + .payloads/wc-store-products.json). Map returns ~471 URLs but ~80% WooFunnels/sitemap/blog noise (wffn_*, wfacp_*, *-sitemap.xml, /post/*); catalog is in the nav + WC API, not the map. Per-month pricing lives on product pages as plan tiers (monthly / bi-yearly / yearly), yearly cheapest; many catalog SKUs sit behind a 'NEEDS PORTAL INVITE' WooCommerce category (consult-gated purchase) but still show a price. Brand uses generic-medication slugs (/sildenafil, /tirzepatide, /mens-trt). LegitScript-certified seal in footer (legitScript.webp → legitscript.com verify)."
key_pages:
  about: /about-us
  how_it_works: /how-it-works
  trt_flagship: /mens-trt
  trt_category: /buy-testosterone-therapy
  weight_loss: /pmd-weight-loss
  tirzepatide: /tirzepatide
  sexual_wellness: /sexual-wellness
  sildenafil: /sildenafil
  hair_loss: /hair-loss
  longevity: /live-longer
  bloodwork: /blood-work
  wc_store_api: /wp-json/wc/store/v1/products?per_page=100
unverified_fields:
  - "Pharmacy ownership/fulfillment — meds ship 'from a licensed pharmacy' (verbatim, /sildenafil ISI); no named pharmacy, captive-affiliate, or owned-facility claim on captured pages. Recorded as third-party in telehealth.md."
  - "Per-SKU prices are a point-in-time snapshot, not fixed — captured tiers vary by plan term (monthly/bi-yearly/yearly) and dose; intro 'Get Started' prices differ from ongoing (e.g. Tirzepatide $149 start vs $249/mo)."
  - "Headcount, funding, revenue — not on a marketing site (deep-research, not capture)."

description: "Delivers TRT, weight-loss, sexual-wellness, hair-loss and longevity treatments to men through licensed-clinician telehealth, shipping US-made prescription medications direct to the door on monthly subscriptions, with a faith-based, affordability-first brand."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://getpetermd.com/wp-content/uploads/PeterMD-logo-1.svg   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: "https://getpetermd.com/wp-content/uploads/PeterMD-logo-1.svg", w: 1613, h: 316 }   # hostable SVG, the real brand wordmark (branding.images.logo)
  logomark: { src: "https://www.google.com/s2/favicons?domain=getpetermd.com&sz=256", px: 256, transparent: false }   # "PMD™" monogram; sips hasAlpha:no → baked white background (apple-touch-icon Favicon-PMD.svg is only 26px)
  # og: omitted — no og:image declared on the homepage (true absence)
brand_colors: { primary: "#FFFF64", accent: "#57817E" }   # STRAIN: soft-yellow dominates CTAs + section blocks; muted teal is links/secondary (branding.colors confirmed vs screenshot)
fonts: [GT America]
color_scheme: light
design_framework: wordpress   # WooCommerce + Elementor 4.0.7 (rawHtml: wp-content×1550, woocommerce×153, generator "Elementor 4.0.7") — branding.designSystem said "custom" (wrong, as usual)
---

## Overview

PeterMD is a DTC men's-health telehealth clinic operated by **Peter Holdings**. A free online consult with a licensed specialist leads to a personalized protocol, and US-made prescription medications ship to the patient's door on an auto-drafted subscription. It spans six care lines — testosterone, weight loss, sexual wellness, performance, longevity, and hair loss — plus standalone bloodwork and a women's ("For Her") line. It claims to be "North America's largest online health optimization platform," "Trusted by 400K+ subscribers," with a 4.9/5 rating on "20k+ Reviews" and a 98% patient-satisfaction rate. The brand carries an explicit faith-based identity (named after the Apostle Peter) and positions on affordability ("America's most affordable provider"). Founder lineage traces to "the first compliant national HRT clinic in 2014."

## What they offer

Multi-product, all subscription, organized as named care lines. PeterMD is unusually **price-transparent** — prices show on product pages *and* via a public WooCommerce catalog — so family lines tag `[published]`; per-SKU depth lives in `offerings.md`:

- **Increase Testosterone:** Injectable TRT (`/mens-trt`, **$79–$139/mo** by plan term, reg "$1668"), Oral TRT / Enclomiphene (`/enclomiphene`, "$278/BIMONTHLY"), HCG (`/hcg`, "$147.00"). Category: `/buy-testosterone-therapy`. `[published]` — the founding line and spine of the funnel.
- **Lose Weight:** GLP-1 / semaglutide (`/glp1-b12`, "$270.00" sub), Tirzepatide (`/tirzepatide`, "$149" start → "$249 per month"), B12 + MIC (`/b12-mic`, "$79.00"). Category: `/pmd-weight-loss`. `[published]`
- **Sexual Wellness:** Sildenafil ("$62.50"–"$180.00"), Tadalafil ("$72.50"–"$210.00"), Mount Everest ("$50.00"–"$300.00"), Scream Cream ("$107.00"), Cabergoline ("$97.75"). Category: `/sexual-wellness`. `[published]`
- **Enhance Performance:** Sermorelin (`/sermorelin`, "$211.65"–"$585.00"), Thyroid Optimization ("$88.00"), B12 + MIC. Category: `/enhance-performance`. `[published]`
- **Live Longer:** Metformin ("$60.00"–"$160.00"), NAD+ injection ("$369.00") + capsule ("$125.65"–"$310.00"). Category: `/live-longer`. `[published]`
- **Hair Loss:** Finasteride ("$60.00"/"$90.00"), Follicure RX / minoxidil ("$70.00"/"$140.00"), ReGenX Bundle ("$130.00"). Category: `/hair-loss`. `[published]`
- **Blood Work:** standalone panels — Testosterone Labs In-Person ("$45.00"), Thyroid Panel ("$55.00"), comprehensive bloodwork. `[published]`
- **For Her (women's):** Women TRT ("$198.00"), Women's HRT à-la-carte ("$188.00") / 1-hormone ("$447.00"/qtr) / all-inclusive ("$567.00"/qtr). Plus **Supplements & Vitamins** and **Merch**. `[published]`

## How it works / model

Four-step journey: **Free Consultation** (online visit with a specialist) → **Personalized Plan** → **Begin Treatment** (meds shipped in discreet packaging) → **Ongoing Support** (24/7 access to the medical team, unlimited free consults). Subscription-based with payments auto-drafted on the purchase date; cancel anytime via the Member Account page, **except TRT's 6-month commitment**. All physicians hold state medical, controlled-substance, and individual-state DEA licenses; the site flags **Ryan Haight Act** compliance (controlled substances require an in-person visit first, re-implemented "As of May 11, 2023"). Insurance does **not** cover products/medications, but PeterMD claims to be "the only national Mens Health clinic that allows patients to use their insurance for all lab work" (a "$25 processing fee"), and plans are "FSA, HSA Eligible With All Plans." Patients with recent labs can skip testing.

## Positioning & audience

Targets men seeking hormone, weight, sexual, and longevity optimization, framed around the claim that "testosterone levels have declined over 45% since 1989." Differentiates on **affordability + access** (most affordable provider, unlimited free consults, no hidden fees, upfront/published pricing) and a **faith-centered, family/US-owned** identity. Social-proof reach claim: used by "top CEOs, celebrities, T1 Special Operators, and athletes" as well as everyday Americans. Implicit competitive set is the broad DTC men's-health telehealth field (Hims, Hone, Maximus, etc.); the edge it leans on is price, price-transparency, and breadth of catalog. A women's "For Her" line is present but secondary (men-first).

## Nav structure

```
- Increase Testosterone (top nav anchor; mega-nav "Increased Testosterone")
  - Injectable TRT — /mens-trt
  - Oral TRT (Enclomiphene) — /enclomiphene
  - HCG — /hcg
  - View All — /buy-testosterone-therapy
- Lose Weight
  - GLP1 — /glp1-b12
  - B12 + MIC — /b12-mic
  - Tirzepatide — /tirzepatide
  - View All — /pmd-weight-loss
- Enhance Performance
  - B12 + MIC — /b12-mic
  - Sermorelin — /sermorelin
  - Thyroid Optimization — /thyroid-treatment
  - View All — /enhance-performance
- Improve Sexual Function (top nav; mega-nav "Sexual Wellness")
  - Sildenafil — /sildenafil
  - Tadalafil — /tadalafil
  - Mount Everest — /mount-everest
  - Scream Cream — /scream-cream
  - Cabergoline — /cabergoline
  - View All — /sexual-wellness
- Hair Loss
  - Finasteride — /finasteride
  - Follicure RX — /follicure-rx
  - ReGenX Bundle — /finasteride
  - View All — /hair-loss
- Live Longer
  - Metformin — /metformin
  - NAD+ — /nad
  - NAD+ Capsule — /nad-capsule
  - View All — /live-longer
- Blood Work
  - Comprehensive Bloodwork — /blood-work
  - Blood Tests — /blood
- Supplements & Vitamins — /supplements-vitamins
- For Her — /women-trt-product
- The Company
  - About — /about-us
  - Contact — /contact-us
  - Merch — /merch
  - Careers — /careers
  - Testimonials — /our-positive-reviews
  - Health Insights (blog) — /blog
```

## Credibility & proof

- **Scale claims (self-reported, verbatim):** "Trusted by 400K+ subscribers" / "over 400,000 patients served," "North America's largest online health optimization platform," "The Largest Online Healthcare Clinic in North America" (title tag), "98% patient satisfaction rate."
- **Reviews (self-reported):** "4.9/5 — Based on 20k+ Reviews," prominent across pages; long first-person testimonials on product/about pages.
- **LegitScript-certified:** footer seal (`legitScript.webp`) linking to legitscript.com verification for getpetermd.com — a health-merchant trust signal.
- **Named clinicians / leadership:** Exec team — **Bryan Henry** (President, Peter Holdings; former Family Nurse Practitioner, Endocrinology; "founded the first compliant national HRT clinic in 2014"), **Sarah Henry** (Co-Founder, COO), **Mike Staples** (Chief Compliance Officer, ex-Ohio Medical Board investigator), **Luke Ward** (CGO/growth). Advisory board — **Dr. Kirk Parsley** (MD, ex-Navy SEAL), **Dr. Carrie Carda** (MD, board-certified anti-aging), **Micheal Sarraille** & **Nick Kush** (retired SOF).
- **Trust badges:** "FDA-regulated care providers," "U.S.-sourced medications," "100% online care," "Free, discreet delivery," "Simple, upfront pricing," "Unlimited provider access."
- **Licensing:** state medical + controlled-substance + DEA licensure asserted; Ryan Haight Act and HIPAA referenced.
- **Cause marketing:** the **BEARIT Foundation** supporting veterans and first responders (`/the-foundation`).
- **Safety:** detailed Important Safety Information (side-effect lists for testosterone, Clomid, Enclomiphene) on product pages.

## Visual & brand impression

Light scheme, illustration-heavy, built as a long stacked-section landing page where each care line gets its own pastel color block — peach, dusty pink, muted teal (#57817E), gold, and a soft butter-yellow (#FFFF64) that also carries the CTAs. Rounded cards, friendly hand-drawn-style icons, and a clean geometric "PMD" wordmark (GT America throughout) give a modern, approachable, consumer feel rather than a clinical one. A press-logo wall (GQ, SF Post, Time, Forbes, CEO Weekly) and repeated trust strips/reviews reinforce credibility. The aesthetic reads as a polished but conversion-optimized DTC funnel (WooFunnels/Elementor) — lots of "Get Started" buttons and plan-tier cards — busier and more mass-market than the minimalist premium look of higher-end men's-health brands.

## Strategic read

- **Ownership resolved:** operated by **Peter Holdings**, a family/US-owned company; **Bryan Henry** (President, ex-FNP/Endocrinology) and **Sarah Henry** (Co-Founder, COO) lead it — founder lineage to "the first compliant national HRT clinic in 2014." (The prior capture couldn't name the entity.)
- **Rebrand:** previously "PeterUncaged MD," now "PeterMD" (legacy `peteruncagedmd` handles still in JSON-LD `sameAs`; a captured blog URL: `revealing-the-rave-reviews-peteruncaged-md-transforms-into-petermd`). The sanitized name and Apostle-Peter framing suggest a deliberate move from edgy/irreverent toward trust and mainstream legitimacy.
- **Price as the wedge — and price-transparency:** unusually aggressive on cost (TRT from $79/mo, "America's most affordable provider," $29/mo floor) *and* on showing prices — a public WooCommerce Store API exposes the entire priced catalog, where quiz-walled rivals (Hims, Ro) hide prices behind intake. It competes on being cheaper, more transparent, and broader than rivals, not on premium clinical positioning.
- **Faith + patriotism as identity:** the religious naming ("thriving in Christ," John 15:5 in the founder's note) and BEARIT veterans foundation are distinctive brand assets in a category that's otherwise secular/performance-coded — a targeted appeal to a conservative, faith-and-service-oriented male demographic.
- **Insurance-for-labs** is a genuine, specific differentiator it claims no other national men's-health clinic offers.

## Provenance

- **Pages:** homepage (full mega-nav + branding + JSON-LD + screenshot), `/about-us`, `/how-it-works`, `/mens-trt`, `/tirzepatide`, `/sildenafil` (6 Firecrawl scrapes, `fc.py`, maxAge:0, location:US), plus the public **WooCommerce Store API** (`/wp-json/wc/store/v1/products`, 145 products → `captures/2026-06-04/wc-catalog.md`, free curl). Offering taxonomy from the homepage nav + WC API (map is mostly WooFunnels/sitemap noise); pricing quoted verbatim from product pages + the WC catalog, point-in-time snapshot.
- **Verify:** all 6 scrapes md5-unique, sourceURLs matched (verify passed — no geo/cache contamination).
- **Credits:** 7 Firecrawl credits this run (1 map + 6 scrapes); WC catalog + hero images fetched free (public endpoints). ~870 remaining.
- **Run profile:** express — +offerings.md (per-SKU roster, WooCommerce Store API backbone) · +telehealth.md cohort pack · +logos:{} (wordmark + logomark; og absent) · +offerings hero images (6 flagship product renders, one per care line → `captures/2026-06-04/images/`).
- **Couldn't get:** pharmacy ownership/fulfillment lane (no claim on captured pages — third-party in telehealth.md); financials/headcount (out of scope).
- **Structured layer (schema 2.5):** homepage JSON-LD via `fc.py signals` — `socials` (facebook/getpetermd current + legacy peteruncagedmd noted, instagram, linkedin) + `external` (trustpilot); JSON-LD `logo` = PeterMD-logo-sml.svg (lateral to the wordmark — kept the canonical PeterMD-logo-1.svg). Re-stamped 2.2→2.5 (logos module added).
