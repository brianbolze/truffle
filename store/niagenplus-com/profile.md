---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: niagenplus.com
name: Niagen Plus
aliases: []
legal_entity: Niagen Bioscience, Inc.   # footer "© 2026 Niagen Bioscience" (operating entity on the storefront); confirmed by first-party SEC registered_name "Niagen Bioscience, Inc." (ticker CDXC, ex-ChromaDex). Niagen Plus is a brand/line, not separately incorporated per the site.
parent: [niagenbioscience.com]           # © 2026 Niagen Bioscience; footer "Niagen Bioscience" → niagenbioscience.com; rebrand blog "Niagen Plus is now part of Niagen Bioscience"; SEC CDXC (ex-ChromaDex)
owns: []
socials:
  facebook: https://www.facebook.com/people/Niagenplus/61556515014187/
  instagram: https://www.instagram.com/niagenplus/
  tiktok: https://www.tiktok.com/@niagenplus
  x: https://x.com/niagenplus
external: {}                             # JSON-LD sameAs carried only operated social channels — no third-party records

# Capture meta
captured_at: 2026-06-16
capture_method: firecrawl
site_notes: "Shopify storefront (prod-niagen-plus-mdi.myshopify.com; store id 76497125514). Catalog is tiny — /products.json lists ONLY the 2 at-home SKUs ($299 each, both available=True as of 2026-06-16; the Jun-03 capture had 'More stock coming soon'); the in-clinic Niagen IV + Niagen Shots line is NOT in the product registry (clinician-administered, no e-commerce price, accessed via clinic locator), so enumerate it from /collections/niagen-iv, not the registry. At-home prices include a $20 consult fee (inside the $299, not on top) and are Rx-gated (intake → physician review; approval not guaranteed). Nav is client-rendered (header region is a sign-in shell) — reconstruct from the footer/markdown, not the <header>. Every capture has a trailing 'ERR_BLOCKED_BY_CLIENT / www.niagenplus.com is blocked' overlay + a Klaviyo 'Unlock more Niagen Plus' email popup below the footer — capture-browser noise, not site content; ignore everything below the '© 2026 Niagen Bioscience' line. Not shipped to AL, CA, IA, MA, TX, WA, WV (the older May-20 blog cites only AL+CA — the 7-state list on the PDP/homepage/FAQ is current)."
key_pages:
  home: /
  at_home_kit: /products/niagen-at-home-injection-kit
  at_home_refill: /products/niagen-at-home-injection-kit-refill
  at_home_how_to: /pages/niagen-at-home-injection-kit-how-to
  in_clinic: /collections/niagen-iv
  about: /pages/niagen-plus-about-us
  faqs: /pages/niagen-plus-faqs
  news: /pages/niagen-plus-news                       # press releases + press coverage
  blog: /blogs/niagen-plus-blog
  clinic_locator: /pages/niagen-plus-clinic-locator   # noted, not scraped (store-finder)
  hcp_signup: /pages/healthcare-provider-sign-up       # B2B2C provider onboarding (linked from popups; not scraped)
unverified_fields:
  - "In-clinic Niagen IV / Niagen Shots per-treatment pricing — clinic-set, not published (on-request)."
  - "Exact dose & frequency — officially 'provider-set' (FAQ). But the kit physically holds 10× 1mL injection syringes + one (500 mg, per the kit photo) vial, and the how-to page calls it a 'daily injection routine' → a ~10-dose, daily-cadence at-home regimen is the implied shape, provider-titrated."
  - "Founding date, headcount, Niagen-Plus-line financials — not on the marketing site (parent is public: CDXC; line-level figures are off-site / deep-research)."

description: "Delivers pharmaceutical-grade Niagen® (nicotinamide riboside chloride, an NAD+ precursor) as a prescription at-home subcutaneous injection kit via telehealth, plus clinician-administered IV and intramuscular therapy at 1,200+ partner clinics — the clinical, Rx tier of the Niagen franchise from parent Niagen Bioscience (ex-ChromaDex)."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company                  # own Shopify cart + P&L, sells direct → Company even under a parent
target_market: [B2C, B2B2C]           # DTC at-home kit (B2C) + supplies 1,200+ administering clinics, with an HCP sign-up funnel (B2B2C)
offering_category: [Biotech / Pharma Products, Services / Consulting]   # compounded Rx Niagen® is the hero; telehealth/clinic administration is the service wrapper
portfolio_shape: Flagship + companions   # At-Home Kit is the buyable hero; Refill + In-Clinic IV/Shots are companions
business_model: Transactional / One-time   # $299/kit + paid refills; no on-site subscription/auto-ship captured
primary_industry: Healthcare & Life Sciences

# Visual identity — confirmed against the homepage screenshot + og cover
logo_url: assets/wordmark-navy.svg    # canonical wordmark (2.5+ canonicalizes logo_url to the wordmark); committed text SVG, navy-on-light. Source: on-domain JSON-LD `logo` = cdn/shop/files/2.svg
logos:
  wordmark: { src: assets/wordmark-navy.svg, w: 617, h: 131 }   # serif "Niagen Plus", navy; inverse (white) saved as assets/wordmark-white.svg, footer variant as assets/wordmark-2026.svg (218×48)
  logomark: { src: assets/favicon.png, px: 48, transparent: false }   # serif "N+" white-on-navy square — baked navy background (a colored square on a dark slide); native 48px (sz=256 request ignored)
  og:       { src: assets/og-cover.jpg, w: 1200, h: 628 }   # "Welcome to Niagen Plus" kit-in-hand lifestyle cover (a 500 mg vial), not a clean mark
brand_colors: { primary: "#0C2A44", accent: "#F5EAD3" }   # deep navy + warm cream — vision-confirmed (navy footer, cream canvas); branding payload empty on this Shopify capture, carried from the Jun-03 vision read
fonts: [Utile Display, DM Sans]       # serif display headings + sans body (vision-confirmed; branding payload empty)
color_scheme: light
design_framework: shopify             # rawHtml: cdn.shopify.com + myshopify + Shopify store id 76497125514
---

## Overview

Niagen Plus is the prescription / clinical NAD⁺ line from **Niagen Bioscience** — the company behind patented Niagen® and, until its 2025 rebrand, known as **ChromaDex** (NASDAQ: **CDXC**; CEO **Rob Fried**). It delivers pharmaceutical-grade Niagen® — nicotinamide riboside chloride (NRCl), an NAD⁺ precursor and form of vitamin B3 — in **injectable forms that bypass digestion**: a prescription **at-home subcutaneous injection kit** ordered through a telehealth program, and clinician-administered **Niagen IV** (intravenous) and **Niagen Shots** (intramuscular) at 1,200+ partner clinics nationwide. It positions as the clinical, evidence-backed, higher-trust tier of the Niagen franchise — explicitly distinct from sister brand **Tru Niagen®**, the oral, food-grade supplement.

## What they offer

One molecule (Niagen® / NR), three delivery formats across two channels — bold-led, price verbatim + visibility token. Per-SKU detail in [`offerings.md`](offerings.md).

- **Niagen At-Home Injection Kit:** prescription subcutaneous Niagen® (NRCl), telehealth-gated; the kit ships one (500 mg) vial + a 2-piece mixing/reconstitution syringe set + **10× 1 mL injection syringes** + swabs + QR-code instructions — **$299** (incl. a stated $20 consult fee) `[published]`
- **Niagen At-Home Injection Kit Refill:** reorder of the at-home kit — **$299** `[published]`
- **Niagen In-Clinic — Niagen IV:** clinician-administered intravenous NR infusion at partner clinics; price clinic-set — **not shown** `[on-request]`
- **Niagen In-Clinic — Niagen Shots:** intramuscular Niagen® injection (on-the-go) at select clinics — **not shown** `[on-request]`

The At-Home Kit is the only buyable-online SKU and the site's hero; the in-clinic line is a co-equal second nav pillar but routes to a clinic locator, not a cart. (Press notes a 2024 **Niagen+ NAD⁺ test kit for HCPs** — a ChromaDex/practitioner product not sold on this storefront.)

## How it works / model

- **At-home (DTC telehealth):** purchase the kit → short medical intake questionnaire (after checkout) → licensed physician review → if prescribed, the kit ships from a licensed **503A pharmacy** (product compounded by a licensed **503B outsourcing facility**) with self-administration materials. Subcutaneous self-injection (abdomen is the common site); a **QR code** in the box walks through reconstitution + the **daily injection routine** (two how-to videos), and each order includes **direct chat access to the prescribing clinician**. Dose/frequency are provider-set, but the 10-syringe kit + "daily routine" framing imply a ~10-dose daily cadence. Approval isn't guaranteed — a full refund is issued if declined/ineligible/intake lapses; **once a prescription is issued the order is final**. Contraindicated for pregnancy/breastfeeding, prior/current cancer, liver or kidney disease, and children.
- **In-clinic (B2B2C):** patients find a participating clinic via the **clinic locator** (1,200+ premium locations nationwide); a licensed clinician administers Niagen IV or Niagen Shots. A separate **healthcare-provider sign-up** funnel onboards new administering clinics.
- **Money:** transactional product sales — $299 per at-home kit plus paid refills (no on-site subscription captured); the clinic channel supplies administering providers. Not shipped to AL, CA, IA, MA, TX, WA, WV.

## Positioning & audience

Targets consumers pursuing **"cellular health," healthy aging, and longevity** through NAD⁺ restoration ("NAD⁺ levels in tissues decline by up to 65% between ages 30 and 70"; NAD⁺ is "involved in over 500 cellular processes"). Claimed edge: patented **Niagen® (NRCl)** over generic NAD⁺ IV — the brand argues NR is the precursor of choice and backs it with its *own* clinical data (below), and leans hard on **sterility/pharmaceutical-grade quality** as the moat ("the FDA has already issued recalls of injectable NAD⁺ products… injections bypass one of your body's primary defenses"). It draws a sharp line vs. sister brand Tru Niagen® ("food-grade dietary supplement taken orally") by being **pharmaceutical-grade, prescription-only, clinician-directed**. Brand voice is clinical-luxury: *"The science of cellular health, on your terms,"* *"Pharmaceutical-grade cellular health support, from the global leaders in NAD⁺ research,"* and a celebrity/affluent halo (Kathy Hilton wellness parties, an Equinox Hotel NY debut, "longevity vacation" press).

## Nav structure

```
- Niagen At Home — /collections/niagen-at-home-injection-kit
- Niagen In Clinic — /collections/niagen-iv
- About Us — /pages/niagen-plus-about-us
- (footer) Resources: Clinic Locator · In the News · FAQs · Blog · Contact Us · Help Desk (support.niagenplus.com)
- (footer) Related: Niagen Bioscience (niagenbioscience.com) · Tru Niagen (truniagen.com)
- (popups) Healthcare-provider sign-up · Terms of Use · Privacy
```

## Credibility & proof

- **Own clinical studies (cited; self-presented):**
  - Randomized, double-blind, placebo-controlled pilot — a single **500 mg** Niagen™ IV infusion produced a *"more than 20% peak increase in blood NAD+ levels at 3 hours post-infusion, with 75% less infusion time compared to NAD+ IV"* (Hawkins et al., 2024, **medRxiv preprint — "not yet peer-reviewed"**).
  - Retrospective tolerability study — *"Niagen IV averaged 37 minutes per session versus 97 minutes for NAD+ IV,"* with no clinically significant blood-chemistry/inflammatory changes at 30 days (Reyna et al., 2026, **Frontiers in Aging**, peer-reviewed; PMC12907335).
  - **New (2026): first published clinical safety data on injectable NR** — two first-of-their-kind pilot trials (subcutaneous + intramuscular routes in humans), run by **Niagen Bioscience, the Nutraceuticals Research Institute, and Impact Health Medical**; generally well-tolerated (no serious treatment-related AEs), and **at-home self-injection shown feasible** (Study 2: a 3-day in-clinic phase, then self-administered sub-q injections **3×/week for 90 days**). Preliminary signals (modest ↓ systolic BP, hsCRP, fasting glucose) flagged hypothesis-generating; surfaced via an AboutNAD breakdown and described as preprint, not yet peer-reviewed.
- **IP / moat:** Niagen Bioscience **secured a US patent for NR IV and injectable formulations** (2026 — Longevity.Technology, Nutraceutical Business Review).
- **Ingredient track record (self-reported):** Niagen® backed by *"25+ years of research"* and *"40+ published human clinical studies in oral form."*
- **Manufacturing:** compounded under **cGMP** by a federally registered, FDA-inspected **503B** outsourcing facility; ships from a **503A** pharmacy. Standard FDA disclaimer present (*"not evaluated by the FDA… not intended to diagnose, treat, cure, or prevent any disease"*).
- **Partner / KOL:** testimonial from **Dr. Rachele Pojednic, Chief Scientific Officer at Restore Hyper Wellness**; *"1,200+ premium locations nationwide"* (press cites an earlier "900 clinics" milestone → network growth).
- **Press coverage (own "In the News" page):** Forbes, NY Post, Inc., People, Allure, Town & Country, Business Insider, Oprah Daily, Bustle, US News, Glossy, Athletech News ("Most Innovative Fitness & Wellness Companies of 2025"); plus ChromaDex/Niagen Bioscience investor press releases.
- **Payments:** American Express, Mastercard, Visa.

## Visual & brand impression

High design maturity — a **clinical-luxury / wellness-hospitality** aesthetic, closer to a premium longevity clinic than a supplement DTC. Warm cream/beige canvas, deep-navy footer (`#0C2A44`), serif display headlines (Utile Display) over clean DM Sans body, and editorial photography in warm golden light (a vial cradled in hand, IV bags, soft skin tones). The og/share cover is on-brand: a navy "Welcome to Niagen Plus" box with a hand holding a 500 mg vial, "Injection Vials / Patient Instructions / Swab Pads." Restrained, confident, science-forward; the "on your terms" copy and hospitality framing aim at an affluent, health-optimizing buyer. *(Deep, falsifiable visual layer: [`visual.md`](visual.md).)*

## Strategic read

A **pharma-grade line extension** of the Niagen franchise: ChromaDex — rebranded **Niagen Bioscience** in 2025 — climbing from the oral Tru Niagen supplement into prescription, clinically-gated NAD⁺ (injectable + IV), a higher-trust, higher-margin tier on the *same* patented molecule. The structure is two-channel: **DTC telehealth** (the $299 at-home kit, now newly self-administered after the at-home pilot) and a **B2B2C clinic network** (1,200+ locations incl. Restore Hyper Wellness, with an HCP onboarding funnel). The differentiators — and the moat against the loosely-regulated NAD⁺-IV drip market — are **proprietary clinical evidence** (NR-IV faster + better-tolerated than conventional NAD⁺-IV; the first injectable-NR safety data) and a **US patent on NR IV/injectable formulations**, which together legitimize a premium price and the sterility/quality argument for what competitors sell as an unbranded drip. A celebrity/affluent marketing halo (Kathy Hilton, Equinox Hotel) does the demand-gen work.

## Provenance

- **Pages:** homepage, at-home kit (PDP), at-home refill (PDP), at-home how-to, in-clinic Niagen IV collection (rich), about, FAQs, In-the-News, blog index — analyzed; Firecrawl, 2026-06-16 (forced cold re-scrape; logos/offerings assets carried from the 2026-06-15 capture, not re-pulled). Clinic-locator + HCP sign-up noted, not scraped.
- **Verify:** 9 page bodies — all sourceURLs matched, all bodies md5-unique (no geo/cache contamination), no junk soft-404s.
- **Credits:** 10 (1 map + 1 homepage + 8 key pages) on the 2026-06-16 re-scrape; the 2026-06-15 build that produced the logos block + offerings images spent 11.
- **Couldn't get:** in-clinic IV/Shots per-treatment pricing (clinic-set, on-request); exact dose/frequency (provider-set; kit-contents shape inferred); founding/line-financials (off-site; parent is public, CDXC).
- **Enriched (model knowledge):** "ChromaDex" as Niagen Bioscience's former name — corroborated this run by the rebrand blog ("now part of Niagen Bioscience"), the ChromaDex-bylined investor press releases, and the captured SEC signal (registered_name "Niagen Bioscience, Inc.", ticker CDXC); Rob Fried as CEO is from the site's own news-page interview link.
- **Signals captured this run** (separate layer, `signals/`): Trustpilot, SEC EDGAR (CDXC, confirmed 8-K 2026-05-06), Wayback (root), Google Trends ("Niagen Plus" near-zero except a 2026-06-08 spike), SERP (#1 organic for "Niagen Plus" +AIO; #6 for "at home NAD+ injection"; absent from "prescription NAD+ injection"), Exa neighbors (skew to NAD⁺ IV lounges, not Rx-telehealth peers).
- **Run profile:** guided — full refresh of the 2026-06-03 capture (Brian-approved re-scrape); +offerings (carried), **+logos**, deepened with news/blog/how-to. Schema 2.4 → **2.6** (added `legal_entity`, `logos:{}`).
- **2026-06-16 re-capture (cost-benchmark, variant F "warm forced full"):** forced cold re-scrape of all 9 signal pages 1 day after the 2026-06-15 build, freshness overridden. Every volatile fact re-confirmed unchanged — $299 (incl. $20 consult), 7-state exclusion (AL, CA, IA, MA, TX, WA, WV), exactly 2 at-home SKUs both available in /products.json, JSON-LD identity. No content drift; this run re-stamped `captured_at` only.
