---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.4"

# Identity
domain: niagenplus.com
name: Niagen Plus
aliases: []
parent: [niagenbioscience.com]        # © 2026 Niagen Bioscience; footer "Niagen Bioscience" → niagenbioscience.com (ex-ChromaDex)
owns: []
socials:
  facebook: https://www.facebook.com/people/Niagenplus/61556515014187/
  instagram: https://www.instagram.com/niagenplus/
  tiktok: https://www.tiktok.com/@niagenplus
  x: https://x.com/niagenplus
external: {}                          # JSON-LD sameAs carried only operated social channels — no third-party records

# Capture meta
captured_at: 2026-06-03
capture_method: firecrawl
site_notes: "Shopify storefront (prod-niagen-plus-mdi.myshopify.com). Catalog is tiny — /products.json lists only the 2 at-home SKUs ($299 each); the in-clinic Niagen IV + Niagen Shots line is NOT in the product registry (clinician-administered, no e-commerce price, accessed via clinic locator). At-home prices include a $20 consult fee and are Rx-gated (intake → physician review; approval not guaranteed). Every capture has a trailing 'ERR_BLOCKED_BY_CLIENT / shop.app is blocked' overlay + a Klaviyo email popup below the footer — capture-browser noise, not site content; ignore below the © line. Not shipped to AL, CA, IA, MA, TX, WA, WV."
key_pages:
  home: /
  at_home_kit: /products/niagen-at-home-injection-kit
  at_home_refill: /products/niagen-at-home-injection-kit-refill
  in_clinic: /collections/niagen-iv
  about: /pages/niagen-plus-about-us
  faqs: /pages/niagen-plus-faqs
  clinic_locator: /pages/niagen-plus-clinic-locator   # noted, not scraped
unverified_fields:
  - "In-clinic Niagen IV / Niagen Shots per-treatment pricing — clinic-set, not published (on-request)."
  - "Dose & frequency for any format — provider-set, not published."
  - "Founding date, headcount, financials — not on the marketing site (deep-research, off-site)."

description: "Delivers pharmaceutical-grade Niagen® (nicotinamide riboside chloride, an NAD+ precursor) as prescription at-home subcutaneous injection kits via telehealth, plus clinician-administered IV and intramuscular therapy at partner clinics."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company                  # own Shopify cart + P&L, sells direct → Company even under a parent
target_market: [B2C, B2B2C]           # DTC at-home kit (B2C) + supplies 1200+ administering clinics (B2B2C)
offering_category: [Biotech / Pharma Products, Services / Consulting]   # compounded Rx Niagen® is the hero; telehealth/clinic administration is the service wrapper
portfolio_shape: Flagship + companions   # At-Home Kit is the buyable hero; Refill + In-Clinic IV/Shots are companions
business_model: Transactional / One-time   # $299/kit + paid refills; no on-site subscription/auto-ship captured
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload confirmed against the homepage screenshot
logo_url: https://www.niagenplus.com/cdn/shop/files/2.svg?v=1775209922   # JSON-LD `logo`, on-domain wordmark SVG
brand_colors: { primary: "#0C2A44", accent: "#F5EAD3" }   # deep navy + warm cream — matches screenshot (navy footer, cream canvas)
fonts: [Utile Display, DM Sans]       # display headings + sans body (branding payload, confirmed visually)
color_scheme: light
design_framework: shopify             # rawHtml: cdn.shopify.com + Shopify.theme + myshopify
---

## Overview

Niagen Plus is the prescription / clinical NAD⁺ line from **Niagen Bioscience** (the company behind patented Niagen®, formerly ChromaDex). It delivers pharmaceutical-grade Niagen® — nicotinamide riboside chloride (NRCl), an NAD⁺ precursor — in **injectable forms that bypass digestion**: a prescription **at-home subcutaneous injection kit** ordered through a telehealth program, and clinician-administered **Niagen IV** (intravenous) and **Niagen Shots** (intramuscular) at 1,200+ partner clinics nationwide. It positions as the clinical, evidence-backed tier of the Niagen franchise — explicitly distinct from sister brand **Tru Niagen®**, the oral, food-grade supplement.

## What they offer

One molecule (Niagen® / NR), three delivery formats across two channels — bold-led, price verbatim + visibility token. Per-SKU detail in [`offerings.md`](offerings.md).

- **Niagen At-Home Injection Kit:** prescription subcutaneous Niagen® (NRCl), telehealth-gated — **$299** (incl. a stated $20 consult fee) `[published]`
- **Niagen At-Home Injection Kit Refill:** reorder of the at-home kit — **$299** `[published]`
- **Niagen In-Clinic — Niagen IV:** clinician-administered intravenous NR infusion at partner clinics; price clinic-set — **not shown** `[on-request]`
- **Niagen In-Clinic — Niagen Shots:** intramuscular Niagen® injection (<15 min) at select clinics — **not shown** `[on-request]`

The At-Home Kit is the only buyable-online SKU and the site's hero; the in-clinic line is a co-equal second pillar but routes to a clinic, not a cart.

## How it works / model

- **At-home (DTC telehealth):** purchase the kit → medical intake questionnaire → licensed physician review → if prescribed, the kit ships from a licensed **503A pharmacy** (product compounded by a licensed **503B outsourcing facility**) with self-administration materials. Subcutaneous self-injection, "Provider-led care." Approval isn't guaranteed — a full refund is issued if declined, ineligible, or intake lapses (30 days); once a prescription is issued the order is final.
- **In-clinic (B2B2C):** patients find a participating clinic via the **clinic locator** (1,200+ premium locations nationwide); a licensed clinician administers Niagen IV or Niagen Shots.
- **Money:** transactional product sales — $299 per at-home kit plus paid refills (no on-site subscription captured); the clinic channel supplies administering providers. Not shipped to AL, CA, IA, MA, TX, WA, WV.

## Positioning & audience

Targets consumers pursuing **"cellular health," healthy aging, and longevity** through NAD⁺ restoration. Claimed edge: patented **Niagen® (NRCl)** over generic NAD⁺ IV — the brand argues NR crosses the cell membrane where intact NAD⁺ cannot, and backs it with its *own* clinical data (below). It draws a sharp line vs. sister brand Tru Niagen® ("food-grade dietary supplement taken orally") by being **pharmaceutical-grade, prescription-only, clinician-directed**. Tagline motif: *"Pharmaceutical-grade cellular health support, from the global leaders in NAD+ research"* and *"Cellular health science meets world-class hospitality."*

## Nav structure

```
- Niagen At Home — /collections/niagen-at-home-injection-kit
- Niagen In Clinic — /collections/niagen-iv
- About Us — /pages/niagen-plus-about-us
- (footer) Resources: Clinic Locator · In the News · FAQs · Blog · Contact / Help Desk
- (footer) Related brands: Niagen Bioscience (niagenbioscience.com) · Tru Niagen (truniagen.com)
```

## Credibility & proof

- **Own clinical studies (cited; quoted, self-presented):**
  - Randomized, double-blind, placebo-controlled pilot — a single **500 mg** Niagen™ IV infusion produced a *"more than 20% peak increase in blood NAD+ levels at 3 hours post-infusion, with 75% less infusion time compared to NAD+ IV"* (Hawkins et al., 2024, **medRxiv preprint — "not yet been peer-reviewed"**).
  - Peer-reviewed retrospective tolerability study — *"Niagen IV averaged 37 minutes per session versus 97 minutes for NAD+ IV,"* with no clinically significant blood-chemistry/inflammatory changes at 30 days (Reyna et al., 2026, **Frontiers in Aging**).
- **Ingredient track record (self-reported):** Niagen® *"featured in 75%+ of published peer-reviewed clinical studies on oral nicotinamide riboside and backed by 25+ years of research"*; *"40+ published human clinical studies in oral form."*
- **Manufacturing:** compounded under **cGMP** standards by a federally registered, **FDA-inspected 503B outsourcing facility**; third-party purity/potency verification claimed. Standard FDA disclaimer present (*"not been evaluated by the Food and Drug Administration… not intended to diagnose, treat, cure, or prevent any disease"*).
- **Partner / KOL:** testimonial from **Dr. Rachele Pojednic, Chief Scientific Officer at Restore Hyper Wellness**; *"1200+ premium locations nationwide."*
- **Payments:** American Express, Mastercard, Visa.

## Visual & brand impression

High design maturity — a **clinical-luxury / wellness-hospitality** aesthetic, closer to a premium longevity clinic than a supplement DTC. Warm cream canvas (`#FBF8F3`), deep-navy footer (`#0C2A44`), serif display headlines (Utile Display) over clean DM Sans body, and editorial photography (vials cradled in hand, warm skin tones, soft focus). Restrained, confident, science-forward; the "on your terms" copy and hospitality framing aim at an affluent, health-optimizing buyer.

## Strategic read

A **pharma-grade line extension** of the Niagen franchise: ChromaDex/Niagen Bioscience climbing from the oral Tru Niagen supplement into prescription, clinically-gated NAD⁺ (injectable + IV) — a higher-trust, higher-margin tier on the *same* patented molecule. The structure is two-channel: **DTC telehealth** (the $299 at-home kit) and a **B2B2C clinic network** (1,200+ locations, incl. Restore Hyper Wellness; events at Equinox Hotel NY per the blog). The differentiator — and the moat against the loosely-regulated NAD⁺-IV drip market — is **proprietary clinical evidence** comparing NR-IV to conventional NAD⁺-IV (faster, better-tolerated), which legitimizes a premium price for what competitors sell as an unbranded drip.

## Provenance

- **Pages:** homepage, at-home kit (PDP), at-home refill (PDP), in-clinic Niagen IV collection, about, FAQs — analyzed; Firecrawl, 2026-06-03. Clinic-locator noted but not scraped (a store-finder, low profile signal).
- **Verify:** all 6 sourceURLs matched; all bodies md5-unique (no geo/cache contamination).
- **Credits:** 7 (1 map + 1 homepage + 5 key pages).
- **Couldn't get:** in-clinic IV/Shots per-treatment pricing (clinic-set, on-request); dose/frequency (provider-set); founding/financials (off-site, deep-research).
- **Enriched (model knowledge):** Niagen Bioscience = former ChromaDex — used only to resolve parent identity, not for any claim about what the company does or sells.
- **Run profile:** guided — emphasis "science & ingredients"; +offerings.
