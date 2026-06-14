---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: hellopepti.com
name: Pepti
aliases: [pepti LLC]
parent: []
owns: []
socials: { instagram: "https://www.instagram.com/hellopepti", x: "https://twitter.com/hellopepti", tiktok: "https://www.tiktok.com/@hellopepti" }
external: {}

# Capture meta
captured_at: 2026-06-09
capture_method: firecrawl
site_notes: "Vercel/Next.js; curl 429s, Firecrawl fine. Direct CDN image fetch 429s (bot-defended) — logo-email.png/pepti-circle not retrievable. Homepage '## All treatments & products' grid is JS-TABBED: renders only the active tab (Weight Loss, 6 cards); declares '40 products across 11 categories' but the other ~34 cards live on /category/<slug> pages, which DO render all cards server-side (name + slug + $/mo + 'Popular' badge + descriptor). 40 base PDPs at /peptide/<slug>; each also has 50 /peptide/<slug>/<state> availability variants (roster noise — strip). Wordmark is CSS text '[pepti]' (Space Grotesk), no standalone asset; brand mark is the green circular roundel. Self-reported treatment counts conflict: homepage '40 products' (enumerated) vs about '90+ peptide therapies' vs press '50+ treatments'."
key_pages:
  treatments_all: /#all
  category: /category/{anti-aging|cognitive|gh-support|hormones|immune|intimacy|mens-hormones|recovery|skin-hair|weight-loss|womens-hormones}
  pdp: /peptide/{slug}
  how_it_works: /how-it-works
  providers: /providers
  about: /about
  press: /press
  for_physicians: /for-physicians
  blood_testing: /blood-testing
unverified_fields:
  - "Treatment count — site states three different figures ('40 products', '90+ peptide therapies', '50+ treatments'); roster enumerates 40 distinct PDPs."
  - "Wordmark logos slot — no standalone wordmark asset (CSS text '[pepti]'); logomark + og recorded, wordmark omitted."
  - "'FDA Cleared' homepage trust badge — self-reported; compounded peptides are explicitly NOT FDA-approved per the site's own disclaimers (badge likely refers to lab-testing devices, unverified)."

# Description — one sentence
description: "A DTC telehealth brand selling doctor-prescribed compounded peptide and wellness therapies — GLP-1 weight loss, TRT/hormones, recovery, longevity, sexual wellness, skin — across 11 categories, via async physician review and FDA-registered 503A/503B partner pharmacies."

# Classification — closed sets
entity_type: Company
target_market: [B2C]
offering_category: [Biotech / Pharma Products, Services / Consulting]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: "https://www.google.com/s2/favicons?domain=hellopepti.com&sz=256"   # no standalone wordmark asset; roundel logomark is the recognizable mark
logos:
  logomark: { src: "https://www.google.com/s2/favicons?domain=hellopepti.com&sz=256", px: 256, transparent: true }   # green circular roundel, "[pepti]" in a band; corners transparent
  og:       { src: "https://hellopepti.com/opengraph-image?c4912c5196d2b032", w: 1200, h: 630 }                      # roundel on baked BLACK background
brand_colors: { primary: "#97C3B4", secondary: "#F9FBEA", accent: "#101828" }   # sage green / cream / near-black, verified vs screenshot
fonts: [Inter, Space Grotesk]   # body Inter; headings Space Grotesk (Unbounded once for display)
color_scheme: light
design_framework: next.js
---

## Overview

Pepti is a direct-to-consumer telehealth brand for doctor-prescribed **compounded peptide and wellness therapy**. It pitches itself as the legitimate, physician-supervised alternative to the grey-market peptide world — *"sketchy grey-market websites, bro-science forums, and zero medical oversight"* (about). A patient takes a free 5-minute assessment, pays a **$99 one-time onboarding fee** that covers a US-licensed physician's review, and — if approved — gets a compounded medication shipped monthly from an FDA-registered 503A/503B partner pharmacy. The defining move is **breadth**: where most telehealth brands pick one lane, Pepti runs the *"full stack"* — **40 treatments across 11 categories** (weight loss, hormones/TRT, recovery, longevity, intimacy, skin & hair, cognitive, immune). Legally it frames itself as a *"technology platform"* that connects patients to independent physicians and pharmacies, not a practice or pharmacy. Founded **2026**; HQ Dallas/Frisco, TX; legal entity **pepti LLC** (Delaware).

## What they offer

Eleven categories, one flat catalog of individually-priced compounded Rx + cosmetic/supplement SKUs, all subscription (verbatim card price + visibility token; **a mandatory $99 one-time onboarding fee precedes every monthly price**). Per-SKU depth in [`offerings.md`](offerings.md):

- **Weight loss / GLP-1:** Semaglutide **$349/mo**, Tirzepatide **$399/mo**, oral variants $299–349, Lipo-B $99, L-Carnitine $119 `[published]` — the foregrounded line; brand-name GLP-1s (Zepbound/Wegovy/Mounjaro/Ozempic) offered separately via an insurance **/coverage-check**, not cash-pay.
- **Hormones / TRT:** Testosterone Cypionate **$149/mo**, TRT+Anastrozole $179, TRT cream/low-dose, plus women's BHRT (Bi-Est, progesterone, estradiol, low-dose T) and fertility (HCG, gonadorelin, clomiphene, enclomiphene) — 15 SKUs `[published]`. TRT = Schedule-III controlled substance.
- **GH support / longevity:** Sermorelin **$229/mo**, Hexarelin, NAD+ injection $279 / oral $159, Glutathione, GHK-Cu `[published]`.
- **Intimacy:** PT-141 **$279/mo**, Trimix, Sildenafil/Tadalafil troches, Oxytocin `[published]`.
- **Skin & hair:** GHK-Cu topical, tretinoin+GHK-Cu, hydroquinone, clarity (acne), luminous gel, melanotan I — 12 SKUs `[published]`.
- **Cognitive / immune / supplements:** Methylene Blue, NAD+ oral, Methylcobalamin (B12), Natural Desiccated Thyroid `[published]`.

Prices are a single clean monthly med figure (shown on every card and PDP), with 3-month (−10%) and 6-month (−15%) prepay tiers. Some skin/supplement SKUs are cosmetic/dietary, not Rx, per the site's own disclaimer.

## How it works / model

Four steps, **async**, no video visit: (1) free 5-min assessment (goals, history, meds); (2) **$99 one-time onboarding fee** covering the physician evaluation; (3) a board-certified MD/DO reviews the intake **within 24h** and, if clinically appropriate, writes the Rx and routes it to a partner FDA-registered compounding pharmacy; (4) compounded medication ships free (temperature-controlled, 5–7 days first order), then auto-refills monthly — cancel anytime. Revenue = the $99 onboarding + recurring monthly per-medication subscription. *"Just two costs"* — onboarding + transparent monthly med price; "no insurance games, no hidden fees." HSA/FSA accepted. Supply side is a **1099 physician network** (/for-physicians claims 120+ network physicians, 45 states, "$8K–$25K/mo" earnings).

## Positioning & audience

**All-genders**, parallel men's and women's hormone hubs (men's TRT + women's BHRT), broad weight-loss/wellness appeal — not gendered in brand or hero. Core wedge, stated verbatim in press: *"Where most telehealth companies pick a single lane — weight loss, or hair, or hormones — Pepti offers the full stack of modern peptide and wellness medicine under one platform."* Positions against (a) grey-market/research-peptide sellers on **legitimacy** (real physicians, FDA-registered pharmacies, no bro-science) and (b) single-category telehealth brands (Hims, Hone, single-lane GLP-1 shops) on **breadth**. Price framing leans hard on the compounded-vs-brand delta (e.g. tirzepatide *"$399 vs $1,429… ~72% less"*).

## Nav structure

```
- Treatments (mega-menu) — /#all
  - Categories: Weight Loss, Anti-Aging, Hormones, Skin & Hair, Recovery,
    Intimacy, Cognitive, GH Support, Immune, Men's Hormones, Women's Hormones
    — /category/{slug}
  - PDPs — /peptide/{slug}  (40 base; + /{state} availability variants)
- Blood Testing — /blood-testing
- Biomarkers — /biomarkers
- Learn — /learn   (blog at /blog)
- Free Tools — /free
- Creator Partnerships — /partners
- Pepti Gives — /pepti-gives
- How it works — /how-it-works
- Account — /account
- Footer: About /about · Providers /providers · Press /press · For Physicians
  /for-physicians · Coverage Check /coverage-check · ~25 /legal/* policy pages
```

## Credibility & proof

- **Named clinicians** (/providers): Dr. Gene Lee, MD (Medical Director, Family Medicine, "Licensed in 23 states"); Dr. Laeeq Butt, MD, MBA (CMO, Internal Medicine, "Licensed in 8 states"). Claim: *"No nurse practitioners, no algorithms — real doctors."*
- **Trust badges** (homepage, self-reported): *"HIPAA Compliant," "CLIA Certified," "CAP Accredited," "FDA Cleared"* — the last is flagged (compounded peptides are not FDA-approved per the site's own disclaimers; badge likely refers to lab-testing).
- **Pharmacy:** *"FDA-registered 503A or 503B compounding pharmacy"* — independent partner pharmacies, not owned.
- **Guarantee:** money-back guarantee; *"Not approved? Your medication is fully refunded"*; no charge if Rx denied; cancel anytime; free shipping.
- **Network claims** (/for-physicians, self-reported): "120+ Network physicians," "45 States covered," "treating tens of thousands of patients."
- **Outcome charts** (homepage): patient-reported 12-week weight/skin/recovery/strength graphs, flagged *"Patient-reported… Results vary… Not a guarantee."*

## Visual & brand impression

Clean, modern, well-funded-looking DTC build on a light cream (`#F9FBEA`) ground with **sage-green** (`#97C3B4`) accents and near-black (`#101828`) type — Space Grotesk display headings (96px H1), Inter body, fully rounded pill inputs. The logo is a deliberate **Pepsi-style green roundel** with "[pepti]" set in a horizontal band — playful, consumer-CPG coded, signaling "as easy as ordering vitamins" rather than clinical. Lifestyle/fitness hero imagery, animated outcome charts, credential seals. Reads as a serious, design-led brand, not a thrown-together compounding storefront.

## Strategic read

Pepti is a **near-exact archetype of the Teleprescribe play**: a broad, physician-supervised, compounded-peptide DTC brand routing to 503A/503B pharmacies, monetizing a low-friction onboarding fee + monthly subscription, founded 2026 (i.e. a fresh entrant, not an incumbent). Direct competitor. Two things stand out: (1) the **"one platform, every category"** thesis is their explicit wedge — the opposite of single-lane Hims/Hone — and the same breadth-vs-focus question Teleprescribe faces; (2) the **$99-onboarding + transparent-monthly** model is a clean, copyable funnel with no recurring membership wall. Watch items for a 2031 data room: the aggressive *"FDA Cleared"* badge over compounded product, and three inconsistent self-reported SKU counts (40 / 50+ / 90+) — both are credibility/quality-of-earnings flags worth noting in any competitive teardown.

## Provenance

- **Pages** (Firecrawl, all-formats homepage + markdown/screenshot key pages): homepage, /about, /how-it-works, /providers, /press, /for-physicians (2026-06-07); /category/{hormones, anti-aging, skin-hair, gh-support, intimacy, cognitive, recovery, immune} + PDPs /peptide/{tirzepatide, semaglutide, trt-cypionate, pt-141, sermorelin, methylcobalamin} (2026-06-09). Map + JSON-LD signals read.
- **Verify:** all sourceURLs matched, all body md5s unique, no junk soft-404s.
- **Credits:** 14 this run (2026-06-09: 8 category + 6 PDP) atop the 2026-06-07 base capture (~9).
- **Run profile:** guided — telehealth-brand wrapper; +offerings (Deep, direct competitor) +telehealth +logos.
- **Couldn't get:** direct CDN image fetch 429s (logo-email.png, pepti-circle, hero renders); reconciled SKU count discrepancy left as `unverified_fields`.
- **Enriched (model knowledge):** none — all facts page-attested.
