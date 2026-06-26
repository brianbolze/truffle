---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: agentislongevity.com
name: Agentis Longevity
aliases: []
legal_entity: ""                     # JSON-LD carries no legalName; ©/footer state none
parent: [shorecp.com]                # STRAIN: JSON-LD parentOrganization "Shore Capital Partners" + "PE-backed by Shore Capital" + Business Wire "Shore Capital Partners Launches Agentis Longevity" — PE owner
owns: [arete-wellness.com, "BioDesign Wellness Center"]   # STRAIN: company's own press — "Acquires Arete Wellness", "acquires Florida-based BioDesign"; Mantality + the wider network are partnerships (affiliation, prose). BioDesign domain not captured → name-only, un-joinable
socials: { linkedin: "https://www.linkedin.com/company/agentis-longevity" }
external: {}

# Capture meta
captured_at: 2026-06-25
capture_method: firecrawl
site_notes: "Next.js on Netlify; bare www. is a canonical redirect (slug strips it). Homepage scrape returned a transient HTTP 500 once — a retry succeeded. Homepage JSON-LD Organization block carries HQ address, foundingDate 2024, numberOfEmployees 50+, and parentOrganization (Shore Capital) — richest identity source. Consumer PRICING ($149 LQ) lives ONLY on /boundless-protocols-v2, not /longevity-quotient or /services. DTC funnel sits on a subdomain (lq.agentislongevity.com) + /boundless-protocols-v2/start (map subdomains-off won't surface it). /about team tabs (Board of Directors, Medical Advisory Board) are JS-gated — only the Leadership Team renders; /locations renders only Arete's full address, the other 13 clinics JS-gated."
key_pages:
  about: /about-us
  services: /services
  longevity_quotient: /longevity-quotient
  boundless_protocols: /boundless-protocols-v2
  partners: /partners
  locations: /locations
  media: /media
  contact: /contact-us
unverified_fields:
  - "Patient count is inconsistent across pages: '20,000+' (about / partners / Boundless) vs '3,300+' (homepage / locations / footer band) — reported as a discrepancy, not reconciled."
  - "'Since 2012' (about-page stat band) conflicts with JSON-LD foundingDate 2024 / 'Shore Capital Launches Agentis Longevity' Dec-2024 — the 2012 likely reflects acquired clinics' heritage (e.g. Mantality), not Agentis itself."
  - "Boundless Protocols recurring tier and LQ membership pricing are not shown — only the one-time $149 LQ assessment is priced. 'Tiers and add-ons are separate', 'billed monthly'."
  - "Board of Directors + Medical Advisory Board member names are JS-gated and did not render in the scrape; only the Leadership Team rendered."
  - "Prices/promos are a point-in-time snapshot, not fixed — the $149 LQ assessment is shown with code AGENTIS15 applied (→ $126.65, 15% off)."

# Description — one sentence
description: "A Shore Capital-backed platform operating a network of physician-led longevity and men's-health clinics, anchored on its Longevity Quotient biomarker assessment that scores biological aging and feeds personalized peptide-and-supplement protocols, delivered in-clinic or by at-home telemedicine."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B2C, B2C, B2B]     # patients via partner clinics; direct DTC (Boundless/LQ); clinic-founder partnership/roll-up
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions   # the Longevity Quotient is the hero that gates everything; Boundless protocol + membership are companions
business_model: Subscription         # recurring care/membership + protocol refills; entered via a one-time assessment. PE clinic roll-up + services dimension noted in prose
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against screenshot
logo_url: https://www.agentislongevity.com/agentis-logo.svg
logos:
  wordmark: { src: "https://www.agentislongevity.com/agentis-logo.svg", w: 504, h: 207 }
  logomark: { src: "https://www.agentislongevity.com/agentisfavicon.png", px: 256, transparent: true }   # the "North Star" four-point mark, teal/spruce; og slot omitted (no og:image declared)
brand_colors: { primary: "#21544D", accent: "#112221" }   # spruce teal (North Star mark, links, accents) + dark spruce; cream "cotton ground" is the body background
fonts: [Plus Jakarta Sans, Space Grotesk]   # body / heading — from branding payload; IBM Plex Mono for mono
color_scheme: light                  # cream-dominant ground with dark-teal hero/footer sections
design_framework: next.js            # /_next/image paths throughout (rawHtml); branding.designSystem said "tailwind" (CSS layer, not the framework)
---

## Overview

Agentis Longevity is the self-styled **"national platform for longevity medicine"** — a Shore Capital-backed company that acquires and partners with physician-led clinics, then equips them with diagnostics, protocols, and back-office infrastructure (finance, IT, marketing, HR, accounting, tax) so the clinics can focus on care. It launched out of Shore Capital Partners in December 2024 and is headquartered in Nashville, TN.

Two faces sit on one platform. **B2B/B2B2C:** a network of **14 partner clinics across 9 states / 10+ markets** — Arete Wellness (Nashville, acquired), BioDesign Wellness Center (4 Florida clinics, acquired), and Mantality Health (9 clinics, partner) — whose **"current state" core service is testosterone replacement therapy** ("Agentis specializes in a single service, delivering best-in-class testosterone replacement therapy"), with longevity as the stated expansion. **B2C:** a direct-to-consumer program anchored on the **Longevity Quotient (LQ)** — a 0–99 biological-aging score from a 60+-biomarker panel — that opens into the **Boundless Protocols**, a 12-week personalized peptide-and-supplement program, taken either in-clinic or via an at-home telemedicine path.

## What they offer

The consumer roster is small and flagship-led — the LQ assessment is the front door to everything (per-SKU detail in `offerings.md`):

- **Longevity Quotient (LQ) assessment:** one-time biomarker assessment → a 0–99 biological-aging score — **$149** (code AGENTIS15 → **$126.65**), HSA/FSA eligible, no commitment `[published]`. 60+ biomarkers across 8 body systems; five tests in a ~15-min visit (Comprehensive Blood Panel, COSEHC-17 Cardiometabolic Risk, Cognivue Clinical cognitive test, InBody composition, Functional Grip Strength).
- **Boundless Protocols:** a **12-week** personalized peptide-and-supplement protocol built on Ben Greenfield's Boundless Life program (12 video modules); physician-supervised, dispensed via a licensed compounding pharmacy; **recurring tier billed monthly, price not shown** `[on-request]`. Two paths — Path A in-clinic (Arete, Nashville) / Path B at-home "Concierge Telemedicine" (home phlebotomy booked in the Ultrahuman app).
- **LQ Membership:** recurring program — unlimited LQ scoring, quarterly retesting, comprehensive lab panels each cycle, wearable integration (Ultrahuman Ring + CGM), personalized protocols, concierge provider access — **price not shown** `[on-request]`.
- **Clinical service lines (delivered at partner clinics):** eleven service "pillars" — longevity medicine, detoxification, stress & resilience, gut health, hormone health, metabolic health, cardiovascular care, cognitive performance, inflammation management, sleep & recovery, personalized nutrition — **priced per-clinic, not on the Agentis site** `[on-request]`.
- **Clinic partnership / platform (B2B):** acquisition or partnership for clinic founders — shared protocols, national platform, and functional support (sales, marketing, HR, finance) — **proposal-based** `[on-request]`.

## How it works / model

**Consumer journey:** Book the LQ assessment (no referral, no membership required) → complete the five-component panel in one visit (or an at-home draw) → results synthesize into your Longevity Quotient in ~5–7 days → a provider reviews it and builds a personalized protocol → quarterly retesting tracks the LQ trend. "The test starts your plan."

**Clinic / platform model:** Agentis grows "through acquisitions and partnerships with best-in-class providers in strong markets," targeting **100 clinics in 3 years** (from 14 today). It centralizes back-office functions and clinical protocols across the network and reports **+84% average first-year revenue growth** and **20%+ same-store growth** at partner clinics. Money comes from clinic care revenue (TRT-led today), DTC LQ/Boundless memberships, and the underlying PE roll-up; the platform-economics split is not disclosed on the site.

## Positioning & audience

Positions as **"driving the standard in longevity care"** — the credentialed, physician-led, measurement-first operator ("the most credentialed longevity network in the country") versus both standalone clinics and lighter wellness brands. Heritage and current core are **men's health / TRT** (the partner network skews male; the flagship growth partnership with **Rob Gronkowski** is explicitly to "expand men's health platform"), while the LQ/Boundless front door is pitched gender-neutrally to "health-conscious individuals interested in longevity." Differentiators it claims: a proprietary single-number score, a physician-built protocol (not a self-serve report), and a 12-week program co-shaped by Ben Greenfield.

## Nav structure

```
- About — /about-us
- Services — /services
- Locations — /locations
- Partners — /partners
- Press — /media
- Partner With Us (CTA) — /contact-us
```
*(Consumer LQ/Boundless funnel is not in the top nav — it lives at /longevity-quotient, /boundless-protocols-v2, and the lq.agentislongevity.com subdomain.)*

## Credibility & proof

Self-reported unless noted; recorded verbatim, not endorsed:

- **Scale:** "14 partner clinics" · "10+ markets" / "9 states" · **"3,300+ patients served"** (homepage/footer) vs **"20,000+ Patients Served / Treated"** and "since 2012" (about / partners / Boundless) — *inconsistent across pages; see `unverified_fields`*.
- **Backing:** "Backed by Shore Capital" / "PE-backed by Shore Capital" · **"$17M+ committed capital behind the platform"** · "Shore Capital Partners Launches Agentis Longevity" (Business Wire, Dec 2024).
- **Partner performance:** "+84% avg. year one" revenue growth · "20%+ Same-Store Growth" · "250+ provider partners."
- **Brand partner:** **Rob Gronkowski** ("Brand Partner") — testimonial + a men's-health expansion partnership (Feb–Mar 2026).
- **Named third-party validation in tests:** Cognivue Clinical (FDA-cleared cognitive test) · COSEHC-17 (NIH-validated cardiometabolic questionnaire) · InBody · Ultrahuman.
- **Press:** 17 articles listed (AL.com, Nashville Post, PR Newswire, Business Wire, Authority Magazine, Healthcare Business Today, CityBiz, Shore Capital) — including acquisition announcements for Arete (Jan 2026) and BioDesign (Feb 2026).
- **Patient testimonials:** named first-name/city quotes (Michael T. — Nashville; Brody S. — Des Moines; Maria E. — Tampa) + clinic-founder quotes (Kevin Meuret/Mantality; Adam Bobo/Arete).

## Strategic read

A **PE-built longevity roll-up wearing two hats.** The investor-and-operator DNA is explicit: CEO **Jimmy St. Louis** scaled Laser Spine Institute to "$48M EBITDA" and founded Franchise123 and AliRx (press also bills him a former NFL tight end); the leadership bench is M&A/finance-heavy (a dedicated **VP of M&A**, an ex-Tend SVP Finance), and the stated plan is acquire-and-standardize to 100 clinics. The clinical substance today is **TRT/men's health** (the acquired Mantality footprint, the Gronkowski tie-up), with "longevity" as the brand and growth vector — the Longevity Quotient is the unifying intelligence layer and consumer wedge that lets a TRT network re-platform as proactive longevity care. The DTC Boundless funnel (at-home telemedicine, compounding-pharmacy peptides, Ben Greenfield content) is a national, asset-light complement to the physical-clinic roll-up. Watch the patient-count inconsistency (3,300+ vs 20,000+) — likely the gap between Agentis-era patients and the acquired clinics' cumulative panel.

## Visual & brand impression

Premium, calm, medical-luxury. A **spruce-teal + cream ("cotton ground")** palette with a recurring **four-point "North Star"** motif, large sans-serif display type (Space Grotesk headings / Plus Jakarta Sans body), and heavy editorial photography (athletes, nature, science macro) plus product/app mockups. Reads modern, well-funded, and design-mature — closer to a longevity-startup brand than a clinic chain. *(A blind, cited read is in `visual.md` via `/visual-evidence`.)*

## Provenance

- **Pages:** homepage, /about-us, /services, /longevity-quotient, /boundless-protocols-v2, /partners, /locations, /media, /contact-us — captured via Firecrawl 2026-06-25 (all-formats, US geo), plus the homepage JSON-LD + nav structured layer and the homepage `branding` payload.
- **Verify:** `fc.py verify` — all 9 sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 11 (1 map + 9 scrapes + 1 homepage retry after a transient 500).
- **Run profile:** guided — emphasis "include offerings.md, telehealth cohort pack, and visuals"; +offerings.md, +telehealth.md (visual.md runs separately via `/visual-evidence`).
- **Couldn't get:** Board / Medical Advisory Board member names (JS-gated tabs); 13 of 14 clinic addresses (JS-gated on /locations); Boundless recurring-tier + LQ-membership pricing (not shown); BioDesign clinic domain (not in captured pages).
- **Enriched (model knowledge):** none — Shore Capital parent and all relations are page/JSON-LD-attested.
