---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: whoop.com
name: WHOOP
aliases: []
legal_entity: ""                     # site shows only "© 2026 WHOOP"; no legalName/Inc. attested on captured pages
parent: []
owns: []
socials: {}                          # footer social icons are JS-rendered with no hrefs in captured HTML — none verifiable
external: {}                         # no JSON-LD sameAs / third-party records on captured pages

# Capture meta
captured_at: 2026-06-24
capture_method: firecrawl
site_notes: "Next.js marketing site on /us/en/ locale prefix (geo-routed; whoop.com → www.whoop.com/us/en/). CMS is Contentful (images.ctfassets.net). Membership/tier prices are annual FLOORS ('Starts at $X/yr'); real checkout lives behind join.whoop.com (not on whoop.com, not captured). Accessories are a SEPARATE subdomain (shop.whoop.com) — not in this capture. Advanced Labs Specialized-Panel prices are app-only. Footer social icons render without hrefs — socials uncapturable from HTML."
key_pages:
  membership: /us/en/membership
  one: /us/en/one
  peak: /us/en/peak
  life: /us/en/life
  how_it_works: /us/en/how-it-works
  difference: /us/en/difference
  about: /us/en/about
  advanced_labs: /us/en/advanced-labs
unverified_fields:
  - "Membership prices are annual floors ('Starts at $199/239/359/yr'); the all-in checkout total is set at join.whoop.com (not captured). Point-in-time snapshot, not fixed."
  - "socials — footer icons are JS-rendered with no hrefs in captured HTML; none verifiable."
  - "legal_entity — site states only '© 2026 WHOOP'; no registered legal name on captured pages."
  - "Accessories/bands catalog and pricing live on shop.whoop.com (separate subdomain); WHOOP Unite/enterprise not on captured pages — neither enumerated."

# Description
description: "Sells a screen-free, always-on health and fitness wearable as a tiered subscription with the device included, pairing 24/7 biometric tracking with personalized coaching, longevity scores, and medical-grade heart insights."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Physical Products / Hardware, Software / SaaS]   # makes the wearable (hardware); the value/revenue is the app + insights sold as subscription software. # STRAIN: hybrid device-as-a-service
portfolio_shape: Flagship + companions   # flagship = WHOOP membership/wearable in 3 tiers; companions = Advanced Labs, bands/apparel
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://images.ctfassets.net/rbzqg6pelgqa/1yTHjaEgJ8iNXx0NGBSc0v/670fa3e14ab0be1cdbba478a8e3d0292/WHOOP_Logo_R_Black.png
logos:
  wordmark: { src: "https://images.ctfassets.net/rbzqg6pelgqa/1yTHjaEgJ8iNXx0NGBSc0v/670fa3e14ab0be1cdbba478a8e3d0292/WHOOP_Logo_R_Black.png", w: 1760, h: 288 }   # black "WHOOP" wordmark (JSON-LD logo, matches nav)
  logomark: { src: "https://www.google.com/s2/favicons?domain=whoop.com&sz=256", px: 48, transparent: false }   # white "W" on a black rounded square — baked background; under 128px (recorded per contract)
  og:       { src: "https://images.ctfassets.net/rbzqg6pelgqa/3CCQWI1KRdKsfMkGIgNfls/1db1bc98dbbca4f4c288cca02729e964/Not_a_whoop_member_image__1_.png", w: 1756, h: 2242 }   # declared og:image but PORTRAIT (app + band render), not a wide cover — recorded with true dims
brand_colors: { primary: "#000000", accent: "#41FF31" }   # monochrome black/white brand with a signature green data accent (green confirmed in app screenshots; payload secondary #41FF31)
fonts: [proxima-nova]
color_scheme: light
design_framework: next.js
---

## Overview

WHOOP makes a screen-free, always-on health-and-fitness wearable (a wrist band with no display) and sells it as a **subscription membership with the hardware included** — you don't buy the device, you join. The band streams 24/7 biometrics (heart rate, HRV, skin temp, blood-oxygen) into the WHOOP app, which turns them into daily Sleep, Strain, and Recovery scores plus personalized coaching. The 2026 positioning has shifted heavily toward **health and longevity** — "Healthspan / WHOOP Age," medical-grade heart features (ECG, AFib, blood-pressure beta), and an Advanced Labs bloodwork add-on — alongside the original fitness/recovery pitch. Founded by CEO **Will Ahmed**, a former collegiate athlete who "read 500 medical papers" on heart-rate variability; headquartered at One Kenmore Sq, Boston. Mission line: *"unlock human performance and Healthspan."*

## What they offer

Three subscription **membership tiers** (each bundles a device + bands + charger, 12-month term, lifetime warranty, 24/7 support — all HSA/FSA-eligible via Truemed), plus a bloodwork add-on:

- **WHOOP One:** **"Starts at $199/yr"** `[partial]` — WHOOP 5.0 device, Basic Charger (wired), CoreKnit Jet Black band. Sleep/Strain/Recovery, coaching, VO2 Max & HR zones, Women's Hormonal Insights. *"Professional-grade fitness insights at our best price."*
- **WHOOP Peak:** **"Starts at $239/yr"** `[partial]` — WHOOP 5.0, Wireless PowerPack, SuperKnit (Onyx) band. Everything in One **plus** Healthspan & Pace of Aging, Health Monitor, real-time Stress Monitor. Free trial available.
- **WHOOP Life:** **"Starts at $359/yr"** `[partial]` — WHOOP **MG** device, Wireless PowerPack, SuperKnit Luxe (Titanium) band. Everything in Peak **plus** Heart Screener with ECG, on-demand AFib Detection, Daily Blood Pressure Insights (beta). *"medical-grade health & performance insights."*
- **Free trial:** **"1-month free trial"** of Peak with a **certified pre-owned** WHOOP 5.0 device `[published]`.
- **WHOOP Advanced Labs:** clinician-reviewed blood testing (122+ biomarkers, powered by Quest), an **add-on requiring active membership**. Comprehensive Panel: **"$199"** (1 test/yr) · **"$349"** (2/yr, "$175 per test", *MOST POPULAR*) · **"$599"** (4/yr, "$150 per test") · **"$899"** (6/yr) `[published]`. Five Specialized Panels (Heart/Performance/Metabolic/Women's/Men's) are **purchase-in-app only** `[on-request]`. Uploading past labs is free with membership.

Prices are annual floors ("Starts at…"); checkout is gated behind join.whoop.com. Per-tier and per-panel detail in [`offerings.md`](offerings.md).

## How it works / model

Device-as-a-service: a low (often $0) upfront cost in exchange for a recurring membership — the company's own stated rationale is "a lower-cost way for customers to try the most advanced wearable… without a high upfront cost," funding continuous feature delivery on hardware you already own. Membership starts when you pair/activate the device (or 30 days after the strap ships); 30-day full-refund return window; switch tiers anytime (prorated, new device on upgrade to Peak/Life). The band is worn 24/7 (wrist or off-wrist via WHOOP Body apparel), charged on-body via a waterproof PowerPack so data never stops; the app calibrates a personal baseline over the first ~30 days, then coaches behavior changes from 140+ trackable habits. Advanced Labs layers periodic in-person Quest blood draws onto the daily data, returned as a clinician-reviewed report + action plan in 7–10 business days.

## Positioning & audience

Direct-to-consumer, aimed at performance-minded users from elite athletes to everyday health optimizers ("Whether you're #1 in the world or on day 1"). Claimed edges: a **distraction-free, screen-free** design that auto-detects activity; **"over 99% heart rate and HRV tracking accuracy and gold-standard sleep tracking"**; the only wearable you can charge while wearing (14+ day battery); and the "tells you what's next" coaching framing vs. trackers that "tell you what you did." Competes with Apple Watch, Oura, Garmin, and Fitbit — differentiating on subscription-included hardware, screen-free 24/7 wear, and a deepening medical/longevity feature set.

## Nav structure

```
- Memberships — /us/en/membership
  - WHOOP One — /us/en/one
  - WHOOP Peak — /us/en/peak
  - WHOOP Life — /us/en/life
  - Explore all memberships — /us/en/membership
  - Gifts — /us/en/gifting
  - One month free trial — /us/en/whoop-trials
  - Family Plans — /us/en/family-membership
  - Upgrade to 5.0/MG — join.whoop.com/upgrade
- How it works — /us/en/how-it-works
- Trial WHOOP — /us/en/whoop-trials
- Why WHOOP — /us/en/difference
- Accessories — shop.whoop.com   (separate storefront subdomain)
- Advanced Labs — /us/en/advanced-labs
- [CTAs] Gift WHOOP · Join Now — join.whoop.com
```

## Credibility & proof

- **Athlete/team partners** (homepage roster): Cristiano Ronaldo, Rory McIlroy, Patrick Mahomes, Sha'Carri Richardson, Virgil van Dijk, Diplo; **Paris Saint-Germain** and **Scuderia Ferrari HP** branded *"Official Health & Fitness Wearable" / "Team Partner."*
- **Self-reported outcome claim** (asterisked): daily WHOOP wear "linked to **91 more minutes of weekly activity, 2.3 more hours of sleep per week, and over 10% higher HRV**." *(Verbatim, self-reported — recorded, not endorsed.)*
- **Accuracy claim:** *"over 99% heart rate and HRV tracking accuracy and gold-standard sleep tracking."* *(Self-reported.)*
- **Guarantees:** lifetime device warranty (active membership, bought direct), 24/7 member support, 30-day full-refund return, HSA/FSA eligibility.
- **Clinical posture:** Advanced Labs results clinician-reviewed, testing "powered exclusively by Quest®" (2,000+ US locations); medically-regulated features (ECG/IHRN) carry FDA-style use restrictions footnoted across the site.

## Visual & brand impression

A confident, premium, **monochrome** brand — black-and-white typography (Proxima Nova) with a single signature **electric-green** data accent (the Healthspan orb, score rings). Marketing pages are bright/light with large editorial photography of athletes mid-activity; the app and product renders are near-black, leaning into a sleek, clinical "instrument" feel that matches the screen-free, data-first product. Polished, well-resourced, design-mature — reads like a category leader, not a startup. Heavy use of celebrity-athlete imagery signals aspirational performance positioning.

## Strategic read

The capture shows a company mid-pivot from **fitness-recovery wearable → continuous-health / longevity platform**: the tier names (One/Peak/**Life**), the "Healthspan/WHOOP Age" language, the MG "medical-grade" device, and the Quest-powered Advanced Labs bloodwork all push WHOOP toward the medicalized longevity market (overlapping Function Health, Superpower, Hone) rather than just competing with Apple Watch/Oura on fitness. The membership-included-hardware model is the structural moat — it converts a one-time device sale into recurring revenue and a data relationship, and lets WHOOP ship new "features on hardware you already own." Watch items a marketing capture can't see: actual all-in checkout pricing (gated), churn/retention, and how much of the medical feature set is cleared vs. "beta/wellness-only" (the heavy footnote disclaimers suggest regulatory caution).

## Provenance

- **Pages:** homepage, /membership, /one, /peak, /life, /how-it-works, /difference, /about, /advanced-labs (9 pages) — all via Firecrawl, /us/en/ locale.
- **Verify:** all sourceURLs matched, all bodies md5-unique, no junk soft-404s (`fc.py verify` clean).
- **Credits:** 10 (1 map + 9 scrapes).
- **Couldn't get:** live all-in checkout prices (behind join.whoop.com); accessories/bands catalog (shop.whoop.com, separate subdomain); WHOOP Unite/enterprise; operated social channels (footer icons JS-rendered, no hrefs).
- **Run profile:** guided — +offerings.md (membership tiers + Advanced Labs roster); no emphasis.
- **Enriched (model knowledge):** none — Will Ahmed / Boston HQ / mission all read from captured /about + homepage JSON-LD.
