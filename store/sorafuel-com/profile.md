---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: sorafuel.com
name: Sora Fuel
aliases: [Sora, Sora Fuel Corp.]
legal_entity: Sora Fuel Corporation
parent: []
owns: []
socials:
  linkedin: https://www.linkedin.com/company/sora-fuel/
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "Next.js/Vercel single-page marketing site. Map is tiny (home, legal, news); homepage carries the core IA and all main section anchors. No JSON-LD and no declared og:image. Header wordmark is an inline SVG; extracted to assets/wordmark.svg. Logo helper could not fetch square icons directly, but curl-verified apple-touch and Google s2 both measured 180x180; recorded the on-domain apple-touch icon."
key_pages:
  homepage: /
  contact: /contact
  terms: /terms-of-use
  round_14_6m: /news/sora-fuel-closes-14-6m-round-to-scale-air-to-jet-fuel-technology
  real_cost_saf: /news/the-real-cost-of-saf-why-the-unit-economics-of-feedstock-will-decide-which-approach-replaces-fossil-fuels
  offtake_loi: /news/future-energy-global-and-sora-fuel-sign-letter-of-intent-to-negotiate-e-saf-offtake-agreement
  eft_cooperation: /news/sora-fuel-corp-and-emerging-fuels-technology-inc-announce-a-technology-cooperation-agreement
unverified_fields:
  - "Commercial SAF/e-fuel pricing, buyer contract terms, and revenue model — not published on captured pages."
  - "Current production volume and commercial availability — captured pages describe a planned pilot production facility and future production/offtake milestones."

description: "Produces sustainable aviation fuel by converting ambient air, water, and renewable electricity into syngas through an integrated direct-air-capture electrolysis process."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Energy / Utilities, Industrial / Manufacturing]
portfolio_shape: Flagship + companions
business_model:
primary_industry: Energy & Utilities

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 140, h: 21 }
  logomark: { src: "https://www.sorafuel.com/images/apple-touch-icon.png", px: 180, transparent: false }
brand_colors: { primary: "#DBFAFF", accent: "#000000", background: "#000000" }
fonts: [Lettera Text, Lettera Mono]
color_scheme: light
design_framework: next.js
---

## Overview

Sora Fuel is a climate-tech / clean-fuels company producing sustainable aviation fuel (SAF) from air, water, and renewable electricity. Its core technology is a liquid bicarbonate electrolyzer that integrates direct air capture and conversion, turning captured CO2 and water into syngas for downstream fuel synthesis. The site frames the company around "Direct Air Conversion": air-sourced carbon as the feedstock, low-cost renewable electricity as the energy input, and drop-in aviation fuel as the target output.

The captured site is not a sales storefront. It presents a venture-stage industrial technology company moving toward pilot production, partnership, and future offtake: the April 2026 funding announcement says new capital will fund a pilot production facility intended to scale daily output from gallons to barrels, and the June 2025 Future Energy Global announcement describes a Letter of Intent to negotiate offtake tied to future e-SAF production.

## What they offer

- **Direct Air Conversion system:** Sora says it "make[s] jet fuel from just air, water, and renewable energy" by combining carbon capture and utilization in one process; no customer price or system-sale model is published `[on-request]`.
- **SAF and other e-fuels:** The Future Energy Global page describes Sora Fuel Corporation as "a company producing SAF and other e-fuels" and says Sora ultimately converts syngas into ASTM approved fuels; no published price or commercial availability terms `[on-request]`.
- **Future e-SAF offtake / environmental attributes:** Future Energy Global and Sora signed a Letter of Intent to negotiate an Offtake Agreement for environmental attributes of the "first 10 million gallons" of future e-SAF production; terms and price are not published `[on-request]`.
- **Technology cooperation around Fischer-Tropsch conversion:** The EFT agreement combines Sora's Direct Air Capture pathway with Emerging Fuels Technology's Fischer-Tropsch synthesis and upgrading capability, including anticipated new IP and cross-licensing; commercial licensing terms are not published `[on-request]`.

## How it works / model

The homepage diagrams the process as air -> CO2 + H2O via an air contactor -> energy into a liquid bicarbonate electrolyzer -> CO + H2 syngas -> Fischer-Tropsch reactor -> mixture of hydrocarbons -> fuel. Sora's claim is that integrating capture and conversion bypasses sorbent regeneration, reducing the energy, capital, and delivered-carbon cost of conventional DAC-to-fuels pathways.

The business model is not stated as a packaged sale, subscription, or tariff. The captured commercial signals are B2B partnerships and future offtake: contact-form categories include "Customer or Partner," the EFT announcement is a technology cooperation/cross-licensing agreement, and the FEG announcement is a Letter of Intent to negotiate environmental-attribute offtake for future production.

## Positioning & audience

Sora targets airlines, corporates using SAF Book and Claim, SAF market intermediaries, global energy companies, aviation OEMs, clean-fuels investors, and technology partners. Its positioning is feedstock economics: the site argues that most SAF pathways are constrained by scarce biological feedstocks, expensive green hydrogen, point-source CO2, or conventional DAC costs, while Sora's path uses ubiquitous air and water plus cheap renewable power. The company repeatedly claims its approach can make air-to-fuel economically credible, but those cost and timeline claims are company-reported projections, not independently verified by the capture.

## Nav structure

```
- Home — /
  - Science — /#science
  - Team — /#team
  - News — /#news
- Careers — https://jobs.polymer.co/sora-fuel-corporation
- Contact — /contact
- Footer
  - LinkedIn — https://www.linkedin.com/company/sora-fuel/
  - Privacy Policy — /privacy-policy
  - Terms of Use — /terms-of-use
  - Email — contact@sorafuel.com
  - Address — 750 Main St, Cambridge, MA 02139
```

## Credibility & proof

- **Legal/entity signal:** Terms of Use are entered into by "Sora Fuel, Corporation and its affiliates"; the FEG announcement names "Sora Fuel Corporation (Sora)."
- **Funding claim (self-reported):** Sora announced a "$14.6 million round" on Apr 8, 2026, co-led by Spero Ventures and Inspired Capital, with super pro-rata investments from Engine Ventures and Wireframe Ventures.
- **Pilot milestone (self-reported/projection):** The April 2026 announcement says the funding will support construction and operation of a pilot production facility intended to scale daily SAF production "from gallons to barrels" and reach that demonstration milestone within "18 to 24 months."
- **Cost claims (self-reported/projection):** Captured pages claim atmospheric CO2 capture "below $50 per ton," conventional DAC at "$600 - $1,000+ per metric ton," and a realistic pathway to SAF "under $5 per gallon."
- **Offtake signal:** Future Energy Global and Sora signed a Letter of Intent to negotiate an Offtake Agreement for environmental attributes of the "first 10 million gallons" of future e-SAF production, with an option to increase later.
- **Technology partner:** Emerging Fuels Technology signed a Technology Cooperation Agreement with Sora around combining Sora's Direct Air Capture / reactive carbon capture pathway with EFT's Fischer-Tropsch synthesis and upgrading capability.
- **Origin signal:** The FEG page says Sora was conceived within Engine Ventures based on research from the Berlinguette Research Group at the University of British Columbia.
- **Accelerator signals:** Homepage news cards state Sora was selected by IAG's accelerator program and by the Shell GameChanger Accelerator powered by NREL.

## Visual & brand impression

Sora's site feels like a polished industrial-science pitch, not a generic climate startup page. The first viewport is a soft pink-and-blue cloud hero with a tiny white Sora Fuel wordmark and the split headline "This is SAF" / "without constraints."; the science section then flips into black, pale lines, and diagrammatic process graphics. Pale cyan panels, monospaced labels, low-contrast technical diagrams, and a laboratory team photo create a calm, research-led look. The logo system is a white rectangular wordmark plus a black bird/wing-like logomark on a baked pale-cyan square.

## Strategic read

Sora is making a narrow bet: the scarce part of SAF is not conversion chemistry, it is cheap and scalable feedstock. That is why the site spends more time on air/water inputs, carbon cost, and renewable-energy siting than on fuel branding. The company is still framed as pre-commercial/pilot-stage, so the strongest captured signals are capital, technology partnerships, and LOI-style offtake interest rather than operating production or customer pricing.

## Provenance

- **Pages:** 7 captured pages via Firecrawl (`fc.py`, maxAge:0 + location:US + waitFor) — homepage rich pass, /contact, /terms-of-use, Apr 2026 $14.6M round, Apr 2026 SAF feedstock economics article, Jun 2025 FEG offtake LOI, and Nov 2024 EFT cooperation agreement; map returned 11 URLs.
- **Verify:** sourceURL match + md5-unique across all 7 scrapes; no junk soft-404s.
- **Credits:** 8 (1 map + 7 scrapes). Logo work reused the saved homepage payload and direct icon fetches; no Firecrawl credits.
- **Couldn't get:** Commercial SAF/e-fuel pricing, buyer contract terms, current production output, finalized offtake agreements, revenue model, independent verification of self-reported cost/funding/partner claims, or a declared og:image.
- **Run profile:** express — +logos module requested.
- **Structured layer:** ran `fc.py signals` on the persisted homepage rawHtml; no JSON-LD was present, and the static nav contained only Science, Team, News, Careers, and Contact.
