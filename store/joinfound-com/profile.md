---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: joinfound.com
name: Found
aliases: ["Found Health, Inc.", "Found Health"]   # JSON-LD Organization name "Found Health, Inc."; footer "©2025 Found Health, Inc."
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/joinfound/
  tiktok: https://www.tiktok.com/@joinfound
  facebook: https://www.facebook.com/joinfoundhealth/
  linkedin: https://www.linkedin.com/company/joinfoundhealth/   # footer link; JSON-LD sameAs gives /company/foundhealth (alt)
  x: https://x.com/joinfoundhealth   # JSON-LD sameAs
external: {}   # no third-party records (crunchbase/wikipedia/etc.) in JSON-LD sameAs or footer

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow site (rawHtml: website-files.com ×317, data-wf- ×14, wf-page, 'Webflow' ×7; branding.designSystem says 'custom' — ignore per §5.4). All marketing imagery on cdn.prod.website-files.com (Webflow CDN); the org logo in JSON-LD points at Contentful (images.ctfassets.net/...avatar_-_circle.png) but the front-end is Webflow. Wordmark is an inline data-URI SVG in branding.images.logo (the lowercase 'found' logotype) → extracted to assets/wordmark.svg. App/clinic at clinic.joinfound.com (login + health-assessment-survey); pre-purchase survey at survey.joinfound.com; employer microsite at business.joinfound.com; help at support.joinfound.com. Pricing is LAYERED + insurance-dependent — three distinct figures: GLP-1 program '$149/mo with insurance / $199/mo with cash pay' (12-mo upfront; '$199/$299 monthly') on /plans-and-pricing; an insurance 'memberships starting at $17/month' floor on /insurance; compounded GLP-1s 'one flat price' (~$149/mo cash) on the PDPs. The $1100/$650 branded-drug figures in the toolkit slider are MARKET-comparison anchors, not Found's price. No JSON-LD AggregateRating; no Trustpilot/review aggregate on captured pages (a /reviews page exists, not captured). State availability gated behind a ~40-state picker (CA showed 'No plans available' in the on-page demo). Founding/funding not on-site (deep-research)."
key_pages:
  program: /program
  pricing: /plans-and-pricing
  business: /business
  health_plans: /health-plans
  insurance: /insurance
  medication_index: /medication
  microdosing: /microdosing
  about: /about
  reviews: /reviews
unverified_fields:
  - "Per-dose / per-plan medication prices are set in the intake flow (clinic.joinfound.com health assessment, not submitted) — captured prices are page-stated floors / 'starting at' figures and vary by medication, insurance, and coverage."
  - "Insurance pricing ('memberships starting at $17/month', 'copays as low as $0', 'save up to 90%') is in-network- and plan-dependent; the $17 floor and the $149 program price are different lines — exact all-in varies by state/plan."
  - "State availability is gated behind a ~40-state coverage picker; California showed 'No plans available for this state' in the on-page demo (point-in-time / likely a demo default)."
  - "Foundayo™ = orforglipron: the /foundayo page calls it 'a brand name for orforglipron … manufactured by Eli Lilly' yet the disclaimer lists Foundayo™ as a Lilly trademark Found is 'not affiliated with' — Found prescribes Lilly's drug under that name; whether the 'Foundayo' mark is Lilly's or Found's is ambiguous on-page."

description: "A weight-care telehealth program delivering GLP-1 and non-GLP-1 medication to U.S. adults via obesity-medicine clinicians on a personalized membership — billing insurance where in-network, across DTC, employer, and health-plan channels."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B2C, B2B]   # DTC core; employer-sponsored (/business); health plans (/health-plans)
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product   # one program + an enumerable ~16-medication toolkit
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against screenshots
logo_url: assets/wordmark.svg   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: assets/wordmark.svg, w: 90, h: 26 }                                                                          # lowercase "found" logotype, near-black (rgb 14,14,15); inline data-URI SVG from branding.images.logo
  logomark: { src: "https://cdn.prod.website-files.com/65d8ac86401a1ef9f1915fdb/665d4368ffc374213d2cd58a_file.png", px: 256, transparent: false }   # cream serif "f" on a BAKED deep-green square (apple-touch-icon); google-s2 favicon is the same mark, also 256px
  og:       { src: "https://cdn.prod.website-files.com/65d8ac86401a1ef9f1915fdb/66589a64b2c1ba62e57f44bd_Found%20OG%20Image.png", w: 1200, h: 630 }   # "Find your healthy weight with Found" — green bg, white serif, lifestyle photo
brand_colors: { primary: "#193231", accent: "#147D57" }   # STRAIN: deep pine green (#193231 — hero/footer bg, logomark square, body text) + brighter green CTA (#147D57); branding 'primary' #A8BEB7 is the sage tint, not the dominant hue
fonts: [Greycliff CF, Quincy CF]   # Greycliff CF sans (body/UI) + Quincy CF serif (display headings); branding listed Arial/Georgia as fallbacks
color_scheme: light
design_framework: webflow   # rawHtml: website-files.com, data-wf-, wf-page, "Webflow" (designSystem payload says "custom" — wrong per §5.4)
---

## Overview

Found (legal entity **Found Health, Inc.**) is a DTC telehealth program for **medical weight care** — GLP-1-anchored but explicitly broader, marketing a "wide, affordable medication toolkit" of 10+ drugs. A member completes a 10–15 minute online health assessment; a board-certified clinician trained in obesity medicine reviews it asynchronously (typically 1–2 days) and, if eligible, prescribes from a toolkit spanning **compounded** GLP-1s (semaglutide, tirzepatide, liraglutide), **FDA-brand** GLP-1s (Ozempic, Wegovy, Zepbound, Mounjaro, Rybelsus, Saxenda, Victoza, Trulicity, and Foundayo/orforglipron), and **non-GLP-1 orals** (metformin, Contrave, topiramate, zonisamide). Medication ships to the door; care continues with monthly check-ins. Its sharpest differentiator versus cash-pay telehealth peers: Found-affiliated clinicians are **in-network with major insurers**, so members can run clinical care as insurance claims. Personalization is branded **MetabolicPrint™** (a proprietary engine sorting members into four metabolic profiles); an AI nutrition concierge is branded **Aimee**. Found also sells the same program B2B — to **employers** (cost-containment benefit, claimed 5.1x ROI) and **health plans**.

## What they offer

One program, sold across channels; a ~16-medication toolkit underneath it. Bold lead-in, verbatim price + visibility token (per-SKU depth in `offerings.md`):

- **GLP-1 Program (DTC membership):** clinical care + personalized plan + GLP-1s + Aimee — **"starting at $149/mo with insurance / $199/mo with cash pay"** (12-mo upfront; footnote: "Monthly plans start at $199/mo for insurance and $299/mo for cash-pay") `[partial]` — medication cost varies separately by drug/insurance
- **Insurance membership floor:** **"Weight loss memberships starting at $17/month"** ("Save up to 90% … with insurance," "Copays as low as $0") — in-network/plan-dependent `[partial]`
- **Compounded GLP-1s (semaglutide · tirzepatide · liraglutide):** weekly injections, "one flat price" with "No separate membership" — **~$149/mo** cash, multi-month plan `[partial]`
- **Foundayo™ (orforglipron):** once-daily oral GLP-1 pill (Eli Lilly; FDA-approved 4/1/2026) — **"Starting cash price ~$149/mo"** `[partial]`
- **FDA-brand GLP-1s (Ozempic · Wegovy · Zepbound · Mounjaro · Rybelsus · Saxenda · Victoza · Trulicity):** prescribed/coordinated, often via insurance; toolkit shows market refs ("Ozempic® $1100/mo," "Wegovy®/Zepbound® from $650/mo+") `[on-request]`
- **Non-GLP-1 orals (metformin · Contrave® · topiramate · zonisamide):** lower-cost adjuncts in the toolkit — no per-drug price shown `[on-request]`
- **Microdosing program:** low-dose compounded semaglutide for "preventive metabolic care" (PCOS, peri/menopause, prediabetes) — "Lower starting weights now accepted" `[on-request]`
- **For business / For health plans:** the same program as an employer benefit (claimed **5.1x ROI**, "embedded cost containment") and a health-plan offering — "Contact sales" `[on-request]`

The toolkit's *breadth* is the pitch: "Found-affiliated clinicians can prescribe from a toolkit of 10+ medications … enabling access regardless of formulary coverage."

## How it works / model

A **4-step, async-first** journey (per /program): **(1) Assessment** — a 10–15 min online questionnaire on health history, prior attempts, and routine; **(2) Provider review** — "a board-certified clinician evaluates your assessment" within ~1–2 days (asynchronous review, not a scheduled live visit); **(3) Personalized medication** — a plan informed by **MetabolicPrint™**, medication shipped if eligible, plus nutrition/lifestyle guidance and "support navigating insurance coverage"; **(4) Ongoing care** — monthly provider check-ins, easy refills, 24/7 on-demand support, and a members-only community. Revenue is a **membership subscription** (the clinical-care fee), with medication billed separately and its cost varying by drug, plan selection (monthly vs 12-month upfront), and **whether insurance covers it**. The model's hinge is the insurance rail: "Found-affiliated clinicians are in-network with top insurers … enabling employers to run clinical consults as claims, lowering the cost of the Found program." Self-pay (cash) and HSA/FSA are alternatives.

## Positioning & audience

A **general-population (all-genders)** weight-care brand — testimonials span men and women (Colleen, Jessica, Malcolm, Hank, Lupe). H1: "Proven weight loss, the affordable way"; title: "Found | Weight Loss Medication Personalized for You." It positions against both expensive brand-GLP-1 retail pricing and cash-pay-only telehealth: the wedge is **affordability via insurance** ("one of the only telehealth weight care providers partnering with many medical insurance carriers") plus a **broad, clinician-chosen toolkit** rather than a single hero drug ("Leave behind one-size-fits-all programs that rely only on expensive medications"). Clinical credibility is foregrounded — "designed by leading doctors in obesity medicine," Senior Medical Advisor Dr. Rekha Kumar. Brand values (about): *Led by science*, *Committed to access*, *Judgment-free care*.

## Nav structure

```
- Program — /program
- Medication ▾ (flyout)
  - All medications — /medication
  - Compounded Tirzepatide — /medication/compounded-tirzepatide
  - Compounded Semaglutide — /medication/compounded-semaglutide
  - Metformin — /medication/metformin
  - Ozempic® — /medication/ozempic
  - Mounjaro® — /medication/mounjaro
  - Zepbound® — /medication/zepbound
  - Foundayo™ — /medication/foundayo
  - Microdosing — /microdosing
- Pricing — /plans-and-pricing
- Reviews — /reviews
- For organizations ▾ (flyout)
  - For business — /business
  - For health plans — /health-plans
  - Resource center — /resource-center
- Log in — https://clinic.joinfound.com/login
Footer — Medication (full toolkit): Compounded Semaglutide, Compounded Tirzepatide, Compounded Liraglutide,
         Contrave®, Foundayo™, Metformin, Mounjaro®, Ozempic®, Rybelsus®, Saxenda®, Topiramate, Trulicity®,
         Victoza®, Wegovy®, Zepbound®, Zonisamide
       Partner with us: For business · For health plans · Resource center
       Company: About us (/about) · Careers · Press (/press-releases) · Contact us · Help center (support.joinfound.com)
       Legal: Terms · Refund Policy · Payment & Billing Consent · Telehealth Consent · Privacy · State-Privacy
              Addendum · Notice of Privacy Practices · SMS Terms
       Social: Instagram · TikTok · Facebook · LinkedIn
```
*(Top-level + Medication/For-organizations flyouts confirmed from the `<nav>` region; footer toolkit list is the full 16-medication set.)*

## Credibility & proof

All self-reported unless noted; recorded verbatim, not endorsed:
- **Scale:** "300K+ members served"; "1.4M pounds lost by Found members"; "1 Million+ Clinical consults completed since 2019" (/business — implies operating since 2019).
- **Outcomes:** "83% of members sustain results for one year"; "In 1 year, Found users lost an avg. of 12% body weight" (n=1,773 users, weekly self-report); compounded tirzepatide "12.1% weight loss in 6 months," compounded semaglutide "up to 16%" — all "self-reported member data," flagged.
- **Clinical authority:** "Found's program is designed by leading doctors in obesity medicine"; **Dr. Rekha Kumar, Senior Medical Advisor** (named, /author/rekha-kumar-md-senior-medical-advisor); care from "board-certified clinicians trained in obesity medicine," Registered Dietitians, certified health coaches.
- **LegitScript-certified:** footer seal (static.legitscript.com/seals/7792020.png → legitscript.com verification).
- **Insurance partners (logos):** BlueCross BlueShield, UnitedHealthcare, Aetna, Cigna, Anthem, Highmark, Wellmark; "in-network clinicians for 1 in 3 Americans," "120M+ lives covered through in-network capabilities."
- **Employer ROI:** "proven 5.1x ROI" within year one (/business) — self-reported.
- **Compounding safety:** "partners exclusively with 503A-licensed pharmacies"; compounded meds "third-party tested for potency, purity, and sterility."
- **Press:** "Found weight loss drugs on CBS," Goop podcast mention (blog) — self-cited.
- Standard FTC/Rx disclaimers; "not affiliated or endorsed by Novo Nordisk / Eli Lilly."

## Visual & brand impression

High design maturity, warm and premium — closer to a lifestyle-wellness brand than a clinic. The identity is a **deep pine-green** (#193231) used full-bleed on the hero and footer and as the logomark square, offset by a soft **sage** (#A8BEB7), **buttercream** pale-green, and white content areas; a brighter green (#147D57) carries the CTAs. Typography pairs a **serif display** (Quincy CF — the looped-descender "f" is the logomark) with a clean **sans** (Greycliff CF). Imagery is bright, diverse, real-people lifestyle photography (before/afters, candid smiles) and rounded "pill" shapes. The wordmark is a quiet lowercase "found" logotype. Overall: approachable, science-but-human, deliberately de-clinicalized — a polished Webflow build.

## Strategic read

Two things separate Found inside the GLP-1 telehealth pack. First, **the insurance rail**: where Hims/Ro/Henry are cash-pay-first, Found leads with in-network clinical care ("memberships starting at $17/month," "copays as low as $0") and routes clinical consults as claims — a structurally different cost/affordability story, and the spine of its employer pitch. Second, **toolkit breadth over a hero drug**: 16 medications including non-GLP-1 orals, framed as "access regardless of formulary coverage" and a hedge for employers managing GLP-1 utilization. The B2B motion (employers + health plans, 5.1x ROI, MetabolicPrint, 120M lives) is unusually prominent for a DTC brand — Found is as much a metabolic-care *benefit* as a consumer storefront. Watch: the on-page demo showed California with "No plans available," and per-drug economics are insurance-gated, so the headline prices are floors, not the all-in.

## Provenance

- **Pages:** 12 captured via Firecrawl (homepage; medication index [rich]; about, program, plans-and-pricing, business, insurance; PDPs: compounded-semaglutide, compounded-tirzepatide, compounded-liraglutide, foundayo, microdosing). Synthesized across all + screenshots + branding/rawHtml/JSON-LD.
- **Verify:** all 12 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 13 (1 map + 12 scrapes).
- **Couldn't get:** intake-gated per-dose/per-plan prices; enumerated state list; /reviews aggregate; founding date/funding (deep-research; "since 2019" inferred from the consults claim).
- **Run profile:** Express — all three modules (+telehealth, +offerings, +logos); no emphasis.
