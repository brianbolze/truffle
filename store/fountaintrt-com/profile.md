---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: fountaintrt.com
name: Fountain TRT
legal_entity: "Fountain Wellness, LLC"  # Privacy Policy / Terms: "Fountain Wellness, LLC" operates the Platform
aliases: []
parent: []
owns: []
socials: {}                            # looked — no social anchors or JSON-LD sameAs on captured pages
external: { trustpilot: "https://www.trustpilot.com/review/fountaintrt.com" }  # assessment Trustpilot widget links here; rating in Credibility

# Capture meta
captured_at: 2026-06-20
capture_method: firecrawl
site_notes: "Compact one-page static marketing site (custom HTML/CSS/JS; no JSON-LD; no meaningful <nav> beyond header logo). Map returns only home, /terms, /consent-terms, and www duplicate. Homepage carries most positioning, workflow, price, state list, LegitScript link, and a deep full-page screenshot. /terms and /consent-terms are large legal/consent pages; /consent-terms names Quaker Ridge Medical, PLLC as a professional medical entity. Linked intake app at join.fountaintrt.com is a thin assessment funnel with broader product copy (Injection or Topical Testosterone, Oral Enclomiphene), Trustpilot widget, and 3,000+ member claim. No og:image is declared."
key_pages:
  homepage: /
  terms: /terms
  consent_terms: /consent-terms
  assessment: https://join.fountaintrt.com/?
unverified_fields:
  - "Named pharmacy partner, owned-pharmacy claim, pharmacy accreditation, and 503A/503B lane — not stated on captured pages."
  - "Compounded vs FDA-brand testosterone posture — site says testosterone cream/injections/oral enclomiphene but does not state compounded or brand-drug status."
  - "Exact evaluation fee / discounted intake price — assessment says '88%-off Discount' and money-back guarantee if not qualified, but no dollar amount captured."
  - "HSA/FSA eligibility, socials, founders beyond Doron Stember, headcount, funding, revenue — not on captured pages."

description: "Sells men's Low T / TRT care direct to consumers through an online assessment, partner-lab blood testing, specialist telehealth visits, and testosterone treatment shipped on an all-inclusive membership."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth care + Rx hormone therapy
portfolio_shape: Single              # one core Low T / TRT program; intake page exposes form variants, not separate public lines
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint, confirmed against screenshot + measured SVG/favicon
logo_url: "https://fountaintrt.com/images/logo.svg"
logos:
  wordmark: { src: "https://fountaintrt.com/images/logo.svg", w: 193, h: 47 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=fountaintrt.com&sz=256", px: 101, transparent: true }  # under 128px deck bar; recorded per schema
brand_colors: { primary: "#3EC9CC", navy: "#030728", slate: "#313451", aqua: "#D7FFF3" }  # teal CTA + deep navy sections; confirmed against screenshot
fonts: [Franklin Gothic ATF]
color_scheme: light
design_framework: custom             # rawHtml: custom static page with image assets under /images/; no Next/Gatsby/Webflow/WordPress markers
---

## Overview

Fountain TRT is a **direct-to-consumer men's Low T / TRT telehealth brand**. The public flow is assessment -> partner-lab blood test -> Fountain doctor review -> scheduled real-time video visit -> prescription if appropriate -> monthly testosterone treatment delivered to the door. The homepage leads with **topical testosterone cream** and a $199/mo all-inclusive membership floor; the assessment funnel broadens the kit language to **"Injection or Topical Testosterone, or Oral Enclomiphene"** for qualified members. Legally, **Fountain Wellness, LLC** operates the platform/admin layer; clinical care is delivered by independent licensed Providers, with Quaker Ridge Medical, PLLC named in the telehealth consent.

## What they offer

One public offering family: men's Low T / testosterone optimization. Form-level detail is intake-gated, so no `offerings.md` roster was written.

- **TRT / Low T membership:** Fountain says it helps men raise testosterone to a healthy level, with online doctor's visits, partner-lab blood testing, prescription decisioning, and monthly treatment delivery. Public price: **"as low as $199 per month--All Inclusive"**; includes **medication, video visits and ongoing medical support**, follow-up visits every 3-6 months, and no hidden fees `[partial]`
- **Personalized TRT Kit:** the assessment page says providers customize **"Injection or Topical Testosterone, or Oral Enclomiphene"** to labs, symptoms, and goals; evaluation/payment details are behind the assessment, with a money-back guarantee if the user does not qualify `[on-request]`

## How it works / model

The homepage describes three steps: **(1) Take the Low T assessment**, created by a board-certified urologist; **(2) Get a blood test** at partner labs so a Fountain doctor can review exact testosterone levels; **(3) Schedule a video visit** to discuss Fountain TRT, after which a prescription may be written and testosterone cream shipped to the doorstep. Terms say Fountain provides administrative/platform services and contracts with independent Providers; it collects/remits payments for services from Providers and pharmacies that work with the platform. The payment model is recurring membership / automatic recurring payments; legal terms also say Fountain is not enrolled with third-party payors and users choose cash-basis care outside insurance, though lab providers may bill a plan or bill the user directly.

## Positioning & audience

Targets **men with symptoms of Low T** who want to avoid the friction of traditional TRT clinics: offices, waiting rooms, non-specialist physicians, injections, pharmacy trips, and insurance hassles. The emotional promise is youthful performance: gym, work, bedroom, confidence, energy, mental clarity, and being a better partner/father/brother. Trust is anchored on Doron Stember, MD -- co-founder, board-certified urologist, and men's-health specialist -- rather than a broad provider directory.

## Nav structure

```
- Low T Assessment — https://join.fountaintrt.com/?
- One-page anchors:
  - What is Low T? — /#holding
  - How can TRT help? — /#breakfree
  - How Fountain works — /#how
  - A simple topical cream — /#product
  - Fountain vs others — /#vs
  - Men's Health Experts — /#certified
  - Membership — /#cost
  - FAQ — /#faq
- Legal / footer:
  - Privacy Policy — /consent-terms/
  - Terms & Conditions — /consent-terms/#terms
  - TRT risks / terms — /terms/#terms
  - Blog — https://blog.fountaintrt.com/
  - Contact — support@fountaintrt.com / support@fountain.net
  - LegitScript verification — https://www.legitscript.com/websites/?checker_keywords=fountaintrt.com
```

## Credibility & proof

- **Named clinician:** **Doron Stember, MD**, co-founder, board-certified urologist; site says he has treated **"thousands of men"** with testosterone deficiency and has 10 years of experience in the field.
- **Health credential:** LegitScript certification link in the footer; recorded as a page-attested credential, not independently adjudicated here.
- **Reviews / scale:** assessment funnel embeds Trustpilot **4.5 / 293 reviews** and claims **"Join 3,000+ Fountain members"**; both are self-displayed, recorded verbatim.
- **Availability:** homepage FAQ lists current operating states: Alabama, Arizona, California, Colorado, Connecticut, Florida, Georgia, Illinois, Indiana, Michigan, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Tennessee, Texas, Virginia, Washington, and Wisconsin.
- **Guarantee:** assessment page says **"Money-Back Guarantee - If you don't qualify, get a full refund of evaluation fee"**; legal terms say medication/treatment costs are final and non-refundable once rendered/dispensed.
- **Not found:** no named pharmacy partner, no PCAB/ACHC/NABP pharmacy accreditation, no broad physician directory, no social channels.

## Visual & brand impression

Polished, whimsical DTC men's-health funnel with a strong illustrative system. The page alternates bright white/aqua sections with deep navy panels, uses teal pill CTAs, aquatic/leaf motifs, a stylized fountain/droplet mark, and clean product renders of the Fountain kit/cream. Typography is **Franklin Gothic ATF** throughout, with oversized bold headings and simple rounded CTA buttons. The tone is clinical enough to feel medical, but the art direction is softer and more animated than the typical testosterone clinic: mountains, waves, leaves, scans, product cutaways, and a founder portrait section carry most of the visual trust.

## Strategic read

Fountain is narrowly **TRT-first** and unusually focused for the telehealth cohort: no public GLP-1, peptide, hair, or broad longevity catalog on the main site. The commercial wedge is a specialist-led, all-inclusive membership for men who want TRT without clinic/pharmacy friction. The only expansion signal in the capture is the assessment app's broader kit copy -- injections, topical testosterone, and oral enclomiphene -- while the main marketing page still sells the simple topical-cream story. That split is worth preserving: the homepage is a polished single-product funnel; the intake surface is where product variants appear.

## Provenance

- **Pages:** homepage (rich pass: markdown/html/rawHtml/links/branding/images/screenshot), /terms, /consent-terms, and linked assessment app at `join.fountaintrt.com/?` — 4 scrapes + 1 map. Firecrawl `maxAge:0`, `location:US`, `waitFor:3500`.
- **Verify:** all 4 sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 5 (1 map + 4 scrapes). Logos rode the cached homepage payload plus headed mark fetches; no Firecrawl credit.
- **Couldn't get:** named pharmacy / ownership / accreditation; compounding vs FDA-brand posture; exact intake evaluation fee; HSA/FSA eligibility; social profiles; company financials/headcount/funding.
- **Structured layer (schema 2.6):** no JSON-LD on homepage; slim `<header>` region only carried the logo link, so nav was reconstructed from homepage markdown + screenshot. `external.trustpilot` came from the assessment Trustpilot widget, not JSON-LD.
- **Run profile:** express invocation — `+telehealth.md` cohort pack and `+logos` brand-mark module enabled; no `offerings.md` roster (public catalog not enumerated cleanly). Wordmark = hostable `https://fountaintrt.com/images/logo.svg` (193x47); logomark = google-s2 favicon (101px, transparent, under deck bar); og omitted on true absence.
