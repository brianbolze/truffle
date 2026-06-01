---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: getpetermd.com
name: PeterMD
aliases: ["PeterUncaged MD", "Peter Uncaged MD"]   # rebranded from PeterUncaged MD (see Strategic read)
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "WordPress + WooCommerce + Elementor (generator meta: Elementor 4.0.7). Full mega-nav renders in homepage markdown — no JS-wall, use homepage links for the offering taxonomy. Map returns 487 URLs but ~80% WooFunnels/sitemap/blog noise (wffn_*, wfacp_*, *-sitemap.xml, /post/*); product catalog is in the nav, not the map. Per-month pricing lives on product pages as plan tiers (monthly / bi-yearly / yearly), not on a single /pricing page; yearly is cheapest. Brand uses 'medication-name' slugs (/sildenafil, /tirzepatide, /mens-trt)."
key_pages:
  about: /about-us
  how_it_works: /how-it-works
  trt_flagship: /mens-trt
  trt_category: /buy-testosterone-therapy
  weight_loss: /pmd-weight-loss
  tirzepatide: /tirzepatide
  sexual_wellness: /sexual-wellness
  hair_loss: /hair-loss
  longevity: /live-longer
  bloodwork: /blood-work
unverified_fields:
  - "Legal/operating entity and ownership — site states 'family, and U.S.-owned' but names no LLC/Inc or parent."
  - "Per-SKU prices are a point-in-time snapshot, not fixed — captured tiers vary by plan term and dose (displayed per product page)."
  - "Headcount, funding, revenue — not on a marketing site (deep-research, not capture)."

description: "Delivers TRT, weight-loss, sexual-wellness, hair-loss and longevity treatments to men through licensed-clinician telehealth, shipping US-made prescription medications direct to the door on monthly subscriptions."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://getpetermd.com/wp-content/uploads/PeterMD-logo-1.svg
brand_colors: { primary: "#FFFF64", accent: "#57817E" }   # STRAIN: soft-yellow dominates CTAs + section blocks; muted teal is links/secondary (slots not semantically reliable — verified vs screenshot)
fonts: [GT America]
color_scheme: light
design_framework: wordpress   # WooCommerce + Elementor; rawHtml has wp-content×1544, woocommerce×151, elementor meta — branding.designSystem said "custom" (wrong, as usual)
---

## Overview

PeterMD is a DTC men's-health telehealth clinic. A free online consult with a licensed specialist leads to a personalized protocol, and US-made prescription medications ship to the patient's door on an auto-drafted subscription. It spans six care lines — testosterone, weight loss, sexual wellness, performance, longevity, and hair loss — plus standalone bloodwork. It claims to be "North America's largest online health optimization platform," "Trusted by 400K+ subscribers," with a 4.9/5 rating on 20k+ reviews and a 98% patient-satisfaction rate. The brand carries an explicit faith-based identity (named after the Apostle Peter) and positions on affordability ("America's most affordable provider").

## What they offer

Multi-product, all subscription, organized as named care lines (per-offering detail belongs in `offerings.md`):

- **Increase Testosterone:** Injectable TRT (`/mens-trt`), Oral TRT / Enclomiphene (`/enclomiphene`), HCG. Category: `/buy-testosterone-therapy`. The founding line and still the spine of the funnel.
- **Lose Weight:** GLP-1 / semaglutide (`/glp1-b12`), Tirzepatide, B12 + MIC. Category: `/pmd-weight-loss`.
- **Sexual Wellness:** Sildenafil, Tadalafil, Mount Everest, Scream Cream, Cabergoline. Category: `/sexual-wellness`.
- **Enhance Performance:** Sermorelin, Thyroid Optimization, B12 + MIC. Category: `/enhance-performance`.
- **Live Longer:** Metformin, NAD+ (injection + capsule). Category: `/live-longer`.
- **Hair Loss:** Finasteride, Follicure RX, ReGenX Bundle. Category: `/hair-loss`.
- **Blood Work:** Comprehensive bloodwork / blood tests, sold standalone.
- **Supplements & Vitamins**, **Merch**, and a **For Her** (women's TRT) entry round out the catalog.

**Pricing (verbatim, point-in-time):**
- **TRT — Yearly ($79/Month):** "pricing starting as low as $79/month on the yearly plan"; "Regular price: $1668"; requires a 6-month minimum commitment.
- **TRT — Bi-yearly ($109 a month):** mid-tier plan.
- **TRT — Monthly ($139 a month):** month-to-month plan.
- **Tirzepatide:** "Get Started for $149" then "$249 per month • billed quarterly."
- **Sexual Wellness — Sildenafil ($62.50):** "Usually $358.00 for Viagra".
- **FAQ floor ($29/month):** "Our plans start from as little as $29 per month."

## How it works / model

Four-step journey: **Free Consultation** (online visit with a specialist) → **Personalized Plan** → **Begin Treatment** (meds shipped in discreet packaging) → **Ongoing Support** (24/7 access to the medical team, unlimited free consults). Subscription-based with payments auto-drafted on the purchase date; cancel anytime via the Member Account page (except TRT's 6-month commitment). All physicians hold state medical, controlled-substance, and individual-state DEA licenses; the site flags **Ryan Haight Act** compliance (controlled substances require an in-person visit first). Insurance does **not** cover products/medications, but PeterMD claims to be "the only national Men's Health clinic that allows patients to use their insurance for all lab work" (a $25 processing fee). Patients with recent labs (<6 months) can skip testing.

## Positioning & audience

Targets men seeking hormone, weight, sexual, and longevity optimization, framed around the claim that "testosterone levels have declined over 45% since 1989." Differentiates on **affordability + access** (most affordable provider, unlimited free consults, no hidden fees, upfront pricing) and a **faith-centered, family/US-owned** identity. Social-proof reach claim: used by "top CEOs, celebrities, T1 Special Operators, and athletes" as well as everyday Americans. Implicit competitive set is the broad DTC men's-health telehealth field (Hims, Hone, Maximus, etc.); the edge it leans on is price and breadth of catalog.

## Nav structure

```
- Increased Testosterone
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
- Sexual Wellness
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

- **Scale claims:** "Trusted by 400K+ subscribers," "North America's largest online health optimization platform," 98% patient-satisfaction rate.
- **Reviews:** "4.9/5 — Based on 20k+ Reviews," prominent across pages; long first-person testimonials on product pages.
- **Trust badges:** "FDA-regulated care providers," "U.S.-sourced medications," "100% online care," "Free, discreet delivery," "Simple, upfront pricing."
- **Licensing:** state medical + controlled-substance + DEA licensure asserted; Ryan Haight Act and HIPAA referenced.
- **Cause marketing:** the **BEARIT Foundation** supporting veterans and first responders (`/the-foundation`).
- **Safety:** detailed Important Safety Information (side-effect lists for testosterone, Clomid, Enclomiphene) on product pages.

## Visual & brand impression

Light scheme, illustration-heavy, built as a long stacked-section landing page where each care line gets its own pastel color block — peach, dusty pink, muted teal (#57817E), and a soft butter-yellow (#FFFF64) that also carries the CTAs. Rounded cards, friendly hand-drawn-style icons, and a clean geometric wordmark (GT America throughout) give a modern, approachable, consumer feel rather than a clinical one. The aesthetic reads as a polished but conversion-optimized DTC funnel (WooFunnels/Elementor) — lots of repeated trust strips, "Get Started" buttons, and plan-tier cards — more mass-market and busy than the minimalist premium look of higher-end men's-health brands.

## Strategic read

- **Rebrand:** previously "PeterUncaged MD," now "PeterMD" (a captured blog URL: `revealing-the-rave-reviews-peteruncaged-md-transforms-into-petermd`). The sanitized name and Apostle-Peter framing suggest a deliberate move from edgy/irreverent toward trust and mainstream legitimacy.
- **Price as the wedge:** unusually aggressive on cost (TRT from $79/mo, "America's most affordable provider," $29/mo floor) and breadth — it competes on being cheaper and carrying more lines than rivals, not on premium clinical positioning.
- **Faith + patriotism as identity:** the religious naming and BEARIT veterans foundation are distinctive brand assets in a category that's otherwise secular/performance-coded — a targeted appeal to a conservative, faith-and-service-oriented male demographic.
- **Insurance-for-labs** is a genuine, specific differentiator it claims no other national men's-health clinic offers.

## Provenance

- **Pages:** homepage (full mega-nav + branding + screenshot), `/about-us`, `/how-it-works`, `/mens-trt`, `/buy-testosterone-therapy`, `/pmd-weight-loss`, `/tirzepatide`, `/sexual-wellness` (9 pages) — all Firecrawl (`fc.py`, maxAge:0, location:US); offering taxonomy reconstructed from the homepage nav (map is mostly WooFunnels/sitemap noise); pricing quoted verbatim from product pages, point-in-time snapshot (plan tiers vary by term/dose).
- **Verify:** all md5-unique (verify passed, no geo/cache contamination — clean).
- **Credits:** not recorded this run.
- **Couldn't get:** per-SKU deep pages beyond the 9 captured; ownership/legal entity (not stated on the site); financials/headcount (out of scope).
