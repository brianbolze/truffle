---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: hims.com
name: Hims
aliases: [www.hims.com, "hims & hers", "for hims", forhims]   # JSON-LD alternateName (parent/combined brand + legacy names)
legal_entity: "Hims & Hers Health, Inc."   # 2.6 — site-derivable from the © footer ("© 2026 Hims & Hers Health, Inc."); trademarks held by "Hims, Inc." (footer) — prose
parent: ["Hims & Hers Health, Inc."]   # NYSE: HIMS; men's brand of the public co. No distinct corporate domain (investors.forhims.com is a subdomain). forhers.com is the sister women's brand.
owns: []
socials: { x: "https://twitter.com/wearehims", facebook: "https://www.facebook.com/wearehims", linkedin: "https://www.linkedin.com/company/hims-&-hers", pinterest: "https://www.pinterest.com/forhims/", youtube: "https://www.youtube.com/channel/UCH5P78PeOn_5mnbDK-tl8mw", flickr: "https://www.flickr.com/photos/155294893@N08", instagram: "https://www.instagram.com/hims/", tiktok: "https://www.tiktok.com/@hims" }   # JSON-LD sameAs + footer (TikTok is footer-only, not in sameAs; footer now uses x.com/wearehims)
external: { bloomberg: "https://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapId=542604862", glassdoor: "https://www.glassdoor.com/Overview/Working-at-Hims-EI_IE2090877.11,15.htm", crunchbase: "https://www.crunchbase.com/organization/hims", bbb: "https://www.bbb.org/greater-san-francisco/business-reviews/health-and-medical-products/hims-inc-in-san-francisco-ca-880029" }   # JSON-LD sameAs — third-party records

# Capture meta
captured_at: 2026-06-18
capture_method: firecrawl
site_notes: "Custom in-house React SPA — hashed webpack bundles named `hims.us.legacy.*` (NOT Next/Gatsby/Shopify); Cloudinary for images, Stripe checkout, GTM, reCAPTCHA, Transcend consent. Mega-nav is client-rendered (not in markdown) — reconstruct category hierarchy from the homepage product grid + footer. The footer 'Explore' rail now lists EIGHT lines (Weight Loss · Labs · Sexual Health · Testosterone · Hair Regrowth · Mental Health · Skin · Everyday Health) — 'Everyday Health' is new since the 2026-05-30/06-03 captures (no dedicated page captured this run; likely a supplements/OTC line). Category pages show 'Starting at $X/mo' / 'From $X/mo' per SKU; full out-the-door price is gated behind the per-condition intake quiz. Weight-loss membership is billed SEPARATELY from medication ($39 first month, auto-renews $149/mo); advertised drug prices are medication-only. Proprietary tech: MedMatch (AI/ML decision-support surfaced to providers) + an in-house EMR. Care is async-first (secure messaging; some states live audio/video). Investor/financial data lives at investors.forhims.com (was investors.hims.com); support at support.forhims.com, press at news.hims.com. NYSE: HIMS."
key_pages:
  weight_loss: /weight-loss
  sexual_health: /sexual-health
  erectile_dysfunction: /erectile-dysfunction
  premature_ejaculation: /premature-ejaculation
  hair_loss: /hair-loss
  testosterone: /testosterone
  mental_health: /mental-health
  psychiatry: /psychiatry
  labs: /labs
  skin_care: /skin-care
  how_it_works: /about/how-it-works
  about_company: /about/the-company
unverified_fields:
  - "Out-the-door / total prices — only 'starting at' per-SKU teasers are public; real cost is behind each condition's intake quiz, not submitted."
  - "'Everyday Health' line — new in the footer Explore nav this run; no dedicated page captured, so its SKUs/pricing are unverified (likely supplements/OTC)."
  - "Real-time financials (revenue, subscriber count beyond the dated 2.4M figure, margins) — at investors.forhims.com (NYSE: HIMS), not on the marketing site; a deep-research job, not capture."
  - "Full mega-nav taxonomy — client-rendered and absent from the captured markdown; nav below is reconstructed from the homepage category grid + footer."

description: "The men's half of NYSE-listed Hims & Hers — a DTC telehealth platform connecting men to licensed clinicians for prescription sexual-health, hair-loss, weight-loss, testosterone, and mental-health care, delivered as an async-first monthly membership with at-home labs and AI-assisted (MedMatch) provider tooling."

# Classification
entity_type: Company                 # runs its own P&L / sells directly under a public parent → Company, not Brand (per SCHEMA example)
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # clinician telehealth + prescription pharma
portfolio_shape: Multi-product       # seven-to-eight co-equal, separately-positioned condition lines
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — inline data-URI SVG from branding.images.logo, extracted (white-fill, built for the dark hero)
logos:                               # 2.5 module — measured by fc.py logos; the consumer applies the size bar
  wordmark: { src: assets/wordmark.svg, w: 404, h: 139 }                                                          # lowercase "hims" serif; WHITE-fill (built for the dark hero — invisible on white)
  logomark: { src: "https://www.google.com/s2/favicons?domain=hims.com&sz=256", px: 180, transparent: false }     # black "h" on a baked tan square (re-confirmed by looking, 2026-06-18)
  og:       { src: "https://cloudinary.forhims.com/image/upload/Hims-Home-Share", w: 1200, h: 630 }               # lifestyle hero (man, tan ground) — real share cover
brand_colors: { primary: "#C79B85", accent: "#FFC671", text: "#453421" }  # warm tan + amber-gold on dark-brown text, verified against screenshot. branding's secondary "#0000EE" is default-link chrome — dropped.
fonts: [Sofia Pro]                   # branding.fonts[0], role:body
color_scheme: light
design_framework: custom React SPA   # hashed webpack bundles (hims.us.legacy.*) in rawHtml — NOT branding.designSystem
---

## Overview

Hims is the men's-facing telehealth brand of Hims & Hers Health, Inc. (NYSE: HIMS; founded November 2017 by Andrew Dudum, Jack Abraham, and Hilary Coles; Dudum is co-founder/CEO). It connects men with licensed healthcare providers who review a digital intake and, where appropriate, prescribe treatment — spanning weight loss, sexual health, hair loss, testosterone, mental health, and at-home labs — fulfilled and refilled on a monthly membership. Care is **asynchronous-first** ("secure, back-and-forth messaging rather than a live video or phone call… In some states, visits happen via live audio or video"). The pitch is convenience, discretion, and affordability versus in-person care: "we meet customers where they are — digitally, discreetly, and on their own time." The platform reports **more than 2.4 million subscribers as of June 30, 2025** and access to **400+ U.S.-licensed providers in all 50 states**. Hers (forhers.com) is the sibling women's brand under the same public company.

## What they offer

Six-to-seven separately-positioned condition lines (an eighth, "Everyday Health," newly surfaced in nav this run), all subscription, most starting from a digital intake:

- **Weight loss:** the current hero. A "holistic program" (nutrition + app tracking + meds) gating a wide **GLP-1 lineup**: Wegovy® Pill from $149/mo, Wegovy® Pen from $199/mo, Ozempic® Pill from $149/mo, Foundayo™ (orforglipron) from $149/mo, Zepbound® KwikPen® / Vial $299/mo, plus full-price brand cards (Mounjaro®, Zepbound® at $1,899/mo) — *medication-only prices; a separate Weight Loss Membership is $39 first month, then $149/mo*. Compounded and brand-name options coexist.
- **Sexual health:** the original franchise: ED (sildenafil/"generic Viagra," tadalafil/Cialis, branded Cialis®), premature ejaculation (sertraline for PE, benzocaine wipes), a slate of "Sex Rx +" daily bundles, and an OTC sexual-wellness shelf (rings, vibrators, condoms, lube). Floors from $19–$39/mo for generics; brand-name SKUs run far higher (brand Viagra® $543/mo, brand Cialis® daily $958/mo).
- **Hair loss:** finasteride, minoxidil, topical finasteride sprays/serums, multi-active chews, combo kits; starting $15–$60/mo.
- **Testosterone:** enclomiphene-based "Testosterone Rx+" (works on the body's own T production, *not* synthetic TRT), from ~$99/mo (10-month plan paid upfront), plus T-boosting supplements and at-home T labs. Synthetic TRT (injectable cypionate, oral undecanoate) is still marked **"Coming in 2026"** — not buyable today.
- **Mental health / psychiatry:** async SSRIs/SNRIs + adjuncts (sertraline, escitalopram, citalopram, fluoxetine, duloxetine, venlafaxine, bupropion, buspirone, propranolol) from $49/mo. No controlled substances.
- **Labs:** a Quest Diagnostics blood draw — first panel 75+ biomarkers (130+ available, twice-yearly; 6-month retest 55+), ~$349/yr (struck from $499) — plus the Galleri® multi-cancer early-detection add-on; results + a doctor-built "Action Plan" surfaced in-app.
- **Skin care:** men's derm via the Apostrophe acquisition — custom Rx creams (intake-gated) + OTC basics ($15–$33).

## How it works / model

Customer journey: pick a condition → complete a dynamic **digital intake** (symptoms, history, goals) + identity verification → a licensed provider reviews and, at their independent clinical judgment, prescribes → medication is filled by a **partner pharmacy** (plus a company-opened Ohio-affiliated facility) and ships to the door → ongoing **unlimited secure messaging** with a care team, dosage adjustments, and refills. Care is delivered **asynchronously** by default, with live audio/video in some states. Two proprietary systems anchor the model: **MedMatch** (an AI/ML layer that surfaces treatment options to providers from millions of de-identified interactions, "in addition to their independent clinical judgment") and an in-house **EMR**. Money is made on recurring **subscription/membership** revenue plus medication margin; the weight-loss line explicitly splits a recurring membership fee from medication cost. An in-app experience (iOS/Android) anchors tracking, labs, and care-team contact.

## Positioning & audience

Targets men who'd otherwise avoid or delay care (ED, hair loss, weight, low T, anxiety), positioning as a clinical, doctor-led, data-driven alternative to both in-person clinics and lighter "wellness" telehealth. Claimed edge: breadth of access (especially the FDA-approved GLP-1 catalog), affordability/transparency ("name brand medication, no price markups"), a named bench of specialist clinicians, MedMatch-assisted personalization, and an app-centric, always-on care relationship. The weight-loss testimonials skew squarely to **men in their 40s** (Drew 47, Adam 46, Roland 43, Zack 44). Deeper voice/positioning work belongs in `brand.md` if enabled.

## Nav structure

Reconstructed from the homepage category grid + footer (mega-nav is client-rendered, not captured). The footer "Explore" rail lists eight lines:

```
- Weight Loss — /weight-loss
  - Wegovy Pill/Pen, Zepbound KwikPen/Vial, Ozempic Pill/Ozempic, Foundayo, Mounjaro — /weight-loss/<sku>
  - The science — /weight-loss/science · Membership — /weight-loss/membership · FAQ — /weight-loss/faq
- Sexual Health — /sexual-health  (homepage entry: /g/i/sh)
  - ED: sildenafil, tadalafil, Cialis, Hard Mints — /erectile-dysfunction/<drug>
  - Premature ejaculation: sertraline/sildenafil/tadalafil for PE, benzocaine wipes — /premature-ejaculation/<sku>
  - OTC sexual-wellness: rings, vibrators, condoms, lube — /sexual-health/<sku>
- Hair Loss / Hair Regrowth — /hair-loss  (homepage entry: /c/hl)
  - finasteride, minoxidil, topical finasteride, sprays/serums/chews, kits — /hair-loss/<drug>
- Testosterone — /testosterone  (homepage entry: /g/i/tt)  · Learn — /learn/testosterone
- Mental Health — /mental-health
  - psychiatry: sertraline, escitalopram, + 7 more — /psychiatry/<drug>
- Labs — /labs
  - What we test (biomarkers) — /labs/biomarkers · Multi-cancer (Galleri) — /labs/cancer-test
- Skin — /skin-care  (custom Rx creams + OTC basics)
- Everyday Health — (NEW; no page captured this run)
- About — /about
  - The company — /about/the-company · How it works — /about/how-it-works (also /how-it-works)
  - Clinical excellence — /about/clinical-excellence · Innovation — /about/innovation
  - Medical experts — /our-medical-experts · Quality & Safety — /quality-and-safety · Hims Benefits — /benefits
- Tools — /tools/{bmi,tdee,calorie-deficit,protein,water-intake}-calculator
- Drugs — /drugs/compare · /drugs/info
```

## Credibility & proof

- **Public company**: Hims & Hers Health, Inc., NYSE: HIMS; founded Nov 2017; went public via SPAC in 2021; HQ 340 Bryant St, Floor 3, San Francisco, CA 94107; customer line +1-800-368-0038. Now in retail (Target, since 2020).
- **Scale claims (verbatim, /about/the-company):** "more than 2.4 million subscribers as of June 30, 2025"; "an extensive network of more than 400 U.S.-licensed healthcare providers in all 50 states."
- **Leadership bench** (/about/the-company): CEO/co-founder Andrew Dudum (ex-Atomic Labs); CFO Yemi Okupe (ex-Uber/eBay/PayPal/Google); CCO Mike Chi (since Apr 2021); CMO Patrick Carrol, MD (ex-Vida/WHOOP/Walgreens); CLO Soleil Boughton (since 2018, ex-Google Cloud Healthcare/Jones Day); CDO Dan Kenger (since Mar 2020); **CTO Mo Elshenawy (since May 2025, ex-President & CTO of Cruise)**; **CPO Dheerja Kaur (since Jun 2025, ex-Robinhood VP Product)**.
- **Named clinical bench** on the homepage: Dr. Craig Primack (Head of Weight Loss, obesity medicine), Dr. Peter Stahl (Head of Men's Sexual Health & Urology), Dr. Brian Williams (Head of Medical Affairs), Dr. Alicia Warnock (Endocrinology Advisor, ex-Walter Reed), Dr. Deepak L. Bhatt (Cardiology Advisor).
- **LegitScript-certified** pharmacy seal in the footer; "Verified review" testimonials throughout.
- Heavy, consistent **regulatory disclaiming**: GLP-1 trademark/affiliation notices ("Hims, Inc. is not affiliated or endorsed by Eli Lilly and Company"), "compounded products are not FDA-approved," cancer-test false-positive/negative caveats, "not available in all 50 states," NEJM + Lancet citations for the 25%-body-weight claim — a notably compliance-forward presentation.

## Milestones (from /about/the-company)

- **2017** — Hims launches (Nov), men's health (ED, hair loss, anxiety).
- **2018** — Hers launches (women's health: birth control, hair regrowth, skincare).
- **2020** — all 50 states; Ohio-affiliated pharmacy facility opens; retail debut at Target; first health-system partnership (Ochsner Health); expands into mental health.
- **2021** — goes public via SPAC (NYSE: HIMS); acquires **Apostrophe** (skincare) and **Honest Health** (UK platform).
- **2023** — expands sexual health (Hard Mints), heart health (cardiovascular), and weight loss (holistic program); launches **MedMatch** (AI/ML).
- **2025** — industry-shaking Super Bowl ad; **acquisitions for at-home lab testing** and **European expansion**.

## Visual & brand impression

Premium, editorial, lifestyle-catalog feel. A warm earthy palette — sand, cream, terracotta, and amber-gold backgrounds with dark-brown/near-black type — set against soft studio photography of real men. The oversized lowercase "hims" wordmark closes the page. Clean geometric sans (Sofia Pro), generous whitespace, restrained motion, product cards with hover states. Reads as a mature, well-funded DTC brand that wants to feel like a modern men's-grooming/wellness label rather than a clinic — confident, calm, and aspirational, not clinical-sterile. (A blind, cited visual-evidence read lives in `visual.md`.)

## Strategic read

The capture catches Hims well into its pivot from sexual-health/hair-loss origins to a **weight-loss-led, GLP-1-centric** company: the homepage hero, the "GLP-1 pill is here" banner, and the breadth of branded + compounded GLP-1 SKUs dominate. Two adjacent bets are visible and hardening — **at-home labs** (Quest panels + Galleri cancer screening, an "optimization"/longevity wedge that also feeds the testosterone and weight lines, backed by a 2025 lab-testing acquisition) and a heavy **AI/infra** signal now staffed at the top: a CTO from Cruise (Mo Elshenawy) and a CPO from Robinhood (Dheerja Kaur), with MedMatch as the proprietary AI layer. The roadmap is explicit and large — a stated "$6.5B" target, with expansion into **low testosterone, menopause, sleep, and preventive health**, plus going global. The membership-separate-from-medication pricing structure and dense regulatory disclaiming reflect both the compounding-GLP-1 scrutiny of this market and Hims's posture as the compliance-forward, clinician-fronted incumbent.

## Provenance

- **Pages (20 + map, all `captures/2026-06-18/`, Firecrawl `fc.py`, `maxAge:0`, `location:US`):** homepage (+ rawHtml/branding/screenshot); 10 rich category/index pages (weight-loss, sexual-health, erectile-dysfunction, premature-ejaculation, hair-loss, testosterone, mental-health, psychiatry, labs, skin-care); 9 lean PDPs/about (weight-loss/wegovy-pen, ed/sildenafil, ed/cialis, labs/biomarkers, labs/cancer-test, weight-loss/meal-replacement, premature-ejaculation/sertraline-for-pe, about/how-it-works, about/the-company). Map returned 201 URLs (heavy blog/guides/news noise; catalog confirmed stable vs. prior).
- **Verify:** all 20 sourceURLs matched, all bodies md5-unique, no junk soft-404s (clean — no geo/cache contamination).
- **Credits:** 21 Firecrawl credits (1 map + 20 scrapes, all 1cr — no enhanced-proxy escalations).
- **Couldn't get:** per-condition all-in pricing past the "starting at" teaser (behind intake quizzes); the client-rendered mega-nav; the new "Everyday Health" line's SKUs/pricing (no page); real-time financials (investor site).
- **Structured layer (schema 2.6):** read this capture's homepage JSON-LD via `fc.py signals` ($0, hint-to-verify) — confirmed `socials`/`external` (sameAs) + `aliases` (alternateName: hims & hers / for hims / forhims); JSON-LD `logo` was again the 3rd-party Zendesk theme asset (`zdassets.com`) — rejected, kept wordmark; `legal_entity` set from the © footer ("Hims & Hers Health, Inc."), not JSON-LD (no `legalName` present); TikTok added to `socials` from the footer (not in sameAs).
- **Run profile:** Express (telehealth-brand verb) — +offerings (deep, Direct competitor=Yes / Importance=Highest per Notion) · +telehealth.md cohort pack · +logos (re-confirmed). Fresh re-capture forced over a warm capture per explicit "fresh capture" arg. Re-stamped 2.5→2.6 (added `legal_entity`).
