---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: remedymeds.com
name: Remedy Meds
aliases: [RemedyMeds]
parent: []
owns: []
socials: { facebook: "https://www.facebook.com/groups/officialremedymeds" }
external: {}

# Capture meta
captured_at: 2026-06-01
capture_method: firecrawl
site_notes: "Next.js (Tailwind) SPA on Vercel; map returns only ~21 URLs (small single-funnel marketing site, all CTAs → /quiz). Published pricing lives on /medication/* product pages (comp-sema-inj $299/mo, comp-tirz-inj $399/mo); microdose + branded (Ozempic/Zepbound) are quiz-gated. /safety is a thin SPA hub linking /safety/<drug> sub-pages. /documents/getting-started is a 23-page PDF patient manual (23 credits — prime primary source for billing/labs/care-team). /quiz is an app shell (no static pricing). branding.colors returns gray UI chrome — the true accent is a periwinkle-indigo, confirmed via screenshot; branding.images.logo is an inline data-URI, so logo_url falls back to the on-domain footer SVG."
key_pages:
  semaglutide: /medication/comp-sema-inj
  tirzepatide: /medication/comp-tirz-inj
  quiz: /quiz
  safety: /safety
  patient_manual: /documents/getting-started
unverified_fields:
  - "Microdose plan + branded Ozempic/Zepbound pricing — quiz-gated, no published price."
  - "Member/prescription counts vary by page (250,000+ members / ~300,000 in disclaimers / 200,000+ on med page; 1,200,000+ vs 400,000+ prescriptions) — self-reported marketing figures, point-in-time, not fixed."
  - "States served, corporate parent/operator, founders, founding date — not on captured pages."

description: "A DTC telehealth platform delivering compounded GLP-1 weight-loss medication (semaglutide, tirzepatide) to U.S. consumers via licensed clinicians on a month-to-month membership, with labs, shipping, and unlimited care included."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Single        # STRAIN: one vertical (GLP-1 weight loss); sema/tirz/microdose/branded are variants of one offering
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; hues below estimated from the screenshot (payload returned gray text chrome)
logo_url: https://remedymeds.com/remedymeds/images/remedy-logo-white.svg   # canonical wordmark (on-domain SVG)
logos:                               # 2.5 module — measured by fc.py logos; the consumer applies the size bar
  wordmark: { src: https://remedymeds.com/remedymeds/images/remedy-logo-white.svg, w: 105, h: 30 }                  # italic "Remedy" serif (Playfair); WHITE-fill (built for the navy hero — invisible on white)
  logomark: { src: "https://www.google.com/s2/favicons?domain=remedymeds.com&sz=256", px: 256, transparent: false } # white "R{+}" on a baked navy (#1E2950) square
  og:       { src: "https://remedymeds.com/remedymeds/og-image.jpg", w: 1600, h: 900 }                              # "Remedy Meds" weight-loss share card (app + vials) — real cover
brand_colors: { primary: "#1E2950", accent: "#6C7DC4" }   # STRAIN: navy section bg + periwinkle-indigo serif accent, screenshot-estimated
fonts: [Playfair Display, Inter, Figtree]                 # Playfair (italic serif) for emphasis headings, Inter/Figtree sans for body
color_scheme: light
design_framework: next.js
---

## Overview

Remedy Meds is a direct-to-consumer telehealth weight-loss brand built around compounded GLP-1 medication. A 90-second quiz routes prospects to a licensed clinician who builds a personalized plan; the patient pays a flat month-to-month fee that bundles the medication, unlimited clinician/care-team access, lab work, and shipping from U.S. compounding pharmacies. The entire site is a single conversion funnel — every CTA points to `/quiz` — with no men's-health, TRT, or non-weight-loss lines. Messaging and imagery skew strongly female (postpartum, perimenopause, "food noise," weight-cycling), framing obesity as a biological/medical condition rather than a willpower problem.

## What they offer

One vertical — medical weight loss via compounded GLP-1 — sold as plan variants of a single subscription. Prices are all-in (medication + care + labs + shipping); the company markets "No Memberships or Hidden Fees" even though the patient manual calls the recurring charge a "membership" billed every 28 days.

- **Compounded Semaglutide:** once-weekly GLP-1 injection, "best first step" — **$299/month** `[published]`
- **Compounded Tirzepatide:** dual GIP + GLP-1 injection, "strongest compounded option," marketed "64% of members use this" — **from $399/month** ("Less than $13/day") `[published]`
- **Microdose plan:** "same medication — half the dose, twice a week," micro-titration for easier starts / side-effect-sensitive users — **price not shown** `[on-request]`
- **Branded GLP-1 (Ozempic®, Zepbound®):** name-brand option labeled "Retail Pricing" — **price not shown, quiz-gated** `[on-request]`

Add-ons bundled at no stated extra cost: free lab work, free/discreet shipping, syringes + alcohol pads (injectables), unlimited clinician messaging + video, monthly expert sessions, and a 10,000+-member community.

## How it works / model

Quiz (≈90 sec, free) → within 24h a licensed clinician builds a personalized dose plan → ships within 2–3 days direct from licensed U.S. compounding pharmacies → refills every 28 days with a monthly clinician check-in and dosing titration. Labs (TSH, A1C, CMP, lipid panel) are covered and ordered through Quest Diagnostics, LabCorp, or Bioreference (NY/NJ → Bioreference); prior labs within 24 months accepted. **Revenue model:** flat subscription auto-billed every 28 days, month-to-month, cancel anytime — **but no refund once a prescription has been written.** Cash-pay; HSA/FSA accepted; insurance not required/used.

## Positioning & audience

Targets U.S. adults (heavily female-coded) who have cycled through diets and want clinician-supervised GLP-1 treatment without in-person clinics. Claimed edge vs. "Others": personalized/titrated dosing (vs. fixed plans), included education + community + unlimited clinician access (vs. "no follow-up after your prescription ships"), guaranteed supply (ships within 48h, "never a gap"), and an outcome guarantee. Competes against both retail GLP-1 telehealth (Hims, Ro, etc.) and local clinics.

## Nav structure

Single-funnel site — no product/marketing top nav. Header carries only the care-team phone line and Sign In; the footer holds the real link set.

```
- Header
  - Care team phone — tel:+1 (551) 239-9025
  - Sign In — /auth/sign-in
- Primary CTA (sitewide) — Get my personalized plan / Take the Quiz — /quiz
- Footer
  - Legal & Consent
    - Telehealth Consent — /legal/telehealth-consent
    - Terms of Service — /legal/terms-of-service
  - Privacy & Data
    - Consumer Health Data Privacy Policy — /legal/consumer-health-data-privacy-policy
    - Privacy Policy — /legal/privacy-policy
    - Your Privacy Choices — /#your-privacy-choices
  - Support & Resources
    - Facebook Group — facebook.com/groups/officialremedymeds
    - Customer Support Center — help.remedymeds.com
    - Patient Manual — /getting-started
    - Safety Information — /safety  (→ /safety/zepbound, /safety/ozempic, /safety/compounded-semaglutide, /safety/compounded-tirzepatide)
    - Careers — /careers
    - Referral Program — /referral-program
- Product pages (not nav-linked; reachable via funnel)
  - Semaglutide — /medication/comp-sema-inj
  - Tirzepatide — /medication/comp-tirz-inj
```

## Credibility & proof

- **Press / badges (self-displayed):** "Forbes Best of 2026" badge; press strip — Forbes, Yahoo, USA Today, Axios, Expertise, "Best Weight Loss Meds."
- **Trustpilot:** "Excellent 4.7" shown via badge image (self-reported, rating not independently verified in capture).
- **LegitScript certified:** verification seal #145059 linking to legitscript.com — a third-party pharmacy/telehealth legitimacy certification.
- **Scale claims (self-reported, vary by page):** "1,200,000+ prescriptions written," "250,000+ members" (homepage); med page header states "200,000+ users, 400,000+ prescriptions"; disclaimers cite "~300,000 Remedy Meds members."
- **Outcome claims (self-reported, flagged):** "8 out of 10 members lose 14+ lbs in 90 days"; "94.6% lose ≥5% body weight"; "91% stay past 90 days"; "2x faster than industry average"; member-reported avg "-14 lbs within 90 days"; testimonials (Kala -40, Morgan -36, Chris -42, Noelle -29 lbs) — members "were compensated for their testimonials."
- **Guarantee:** "365-Day Money-Back Guarantee" / "Weight Loss Warranty" — "Lose weight or get refunded, no returns required" (Terms apply).
- **Named care team (patient manual):** Mohit Joshipura — Chief Medical Officer; Jordan Cobb — Clinical Education Director; Rebecca Aaron — Clinical Quality Director.
- **Regulatory disclosure (verbatim posture):** "compounded GLP-1s exclusively from U.S. pharmacies … the FDA has not evaluated the medications for safety, quality, or efficacy," with the standard thyroid C-cell tumor / MTC warning. Quality framing: "every batch passes four independent tests" — Potency, Sterility, pH, Endotoxicity.

## Visual & brand impression

Premium, editorial, and notably calmer than category norms. Clean white/light canvas, near-black slate body text, deep-navy full-bleed section blocks, and a warm peach/cream accent band — with a distinctive **periwinkle-indigo serif accent**: emphasis words ("with Remedy," "Get refunded") set in italic **Playfair Display**, paired with **Inter/Figtree** sans for body. The serif-led, magazine-style treatment reads more like a wellness/lifestyle brand than the clinical-blue sameness most GLP-1 telehealth sites adopt. High design maturity: consistent component system, animated hero/marquee, before-after photography, and trust-badge furniture throughout. Light scheme, generous whitespace, soft 6px radii.

## Strategic read

A high-volume, single-vertical compounded-GLP-1 weight-loss funnel — no insurance, cash-pay, all-in pricing ($299 sema / $399 tirz per month) that folds the "membership" into the med fee while advertising "no membership fees." The wedge is bundling (med + unlimited care + free labs + community) plus an aggressive outcome guarantee (365-day money-back) and supply-continuity promise. Distinctively female-skewed positioning (postpartum/perimenopause/food-noise) and an upmarket editorial brand identity differentiate it in a crowded, clinical-looking field. Compounded-only posture ("FDA has not evaluated") is the structural risk and the price-advantage source simultaneously. Scale and outcome figures are self-reported and internally inconsistent across pages — treat as marketing, not audited metrics.

## Provenance

- **Pages:** homepage, /medication/comp-sema-inj, /medication/comp-tirz-inj, /safety, /documents/getting-started (23-pg PDF patient manual), /quiz — all Firecrawl scrape (all-formats, US geo), plus homepage screenshot for the visual read.
- **Verify:** sourceURLs match; all 6 bodies md5-unique. /safety (295c) and /quiz (644c) are thin SPA shells — bodies trusted (status 200, content legible), not re-scraped.
- **Credits:** 29 this run (1 map + homepage + 4 page scrapes at 1 each + getting-started PDF at 23). ~1,327 remaining.
- **Couldn't get:** microdose/branded pricing (quiz-gated); states served, corporate operator/parent, founders/founding date (not on captured pages); independent verification of Trustpilot rating and scale/outcome claims (all self-displayed).
- **Run profile:** +logos — 2.5 logos module added 2026-06-04 over the existing capture (cached homepage payload, no re-scrape); marks measured by `fc.py logos`, `transparent` judged on a checker tile. Re-stamped 2.3→2.5.
