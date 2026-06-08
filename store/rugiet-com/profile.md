---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: rugiet.com
name: Rugiet
aliases: [www.rugiet.com, rugiethealth.com, "Rugiet Health"]   # rugiethealth.com 301s to www.rugiet.com (same entity, identical title); "Rugiet Health" is the operating-name used in legal/footer copy
parent: []                           # no parent shown; Rugiet Health operates independently on this site
owns: []
socials: { instagram: "https://www.instagram.com/rugiethealth/", facebook: "https://www.facebook.com/rugiethealth/", linkedin: "https://www.linkedin.com/company/rugiethealth/", x: "https://x.com/RugietHealth", tiktok: "https://www.tiktok.com/@rugiethealth" }   # footer anchors (JSON-LD carried no sameAs)
external: {}                         # none declared — homepage JSON-LD is a bare WebSite block (no sameAs/Organization)

# Capture meta
captured_at: 2026-06-07
capture_method: firecrawl
site_notes: "Next.js on Vercel, Sanity CMS for content/images (cdn.sanity.io/images/hgt43vn7/production). Marketing on www.rugiet.com; ALL commerce + intake on the start.rugiet.com quiz funnel (start.rugiet.com/products/<product>/pre_questionnaire), support on support.rugiet.com. PRICING IS QUIZ-GATED — product PDPs show no price; the only public numbers are Ready's per-dose pricing on the /trimix SEM lander ($14–24/dose) and the TRT line's $69 lab + 'from $139/mo' flat. `/trimix` is NOT a Trimix product — it's a paid-search landing page for Rugiet Ready ('alternative to penile injections like trimix'); Rugiet sells no trimix. The `-lander` pages (go-long-lander, daily-boost-lander, recharge-lander) are SEM variants that also hide pricing. Page <title> tags carry injected zero-width unicode (anti-scraping obfuscation) — strips clean in the markdown BODY but garbles title strings. branding.images.logo = inline data-URI SVG of the R+arrow monogram; the header carries a separate vertical 'RUGIET' wordmark SVG (extracted → assets/wordmark.svg). Almost everything is a compounded multi-drug formulation."
key_pages:
  all_treatments: /all-treatments
  sex: /sex
  testosterone: /testosterone
  science: /science
  reviews: /reviews
  ed_ready: /erectile-dysfunction/ready
  pe_go_long: /premature-ejaculation/go-long
  ed_daily_boost: /erectile-dysfunction/boost
  ed_grower: /erectile-dysfunction/grower
  trt_enclomiphene: /testosterone/enclomiphene
  trt_injectable: /testosterone/injectable-trt
  sleep_recharge: /sleep/recharge
  weight_weigh_in: /weight-loss/weigh-in
unverified_fields:
  - "Per-product all-in pricing for Go Long, Daily Boost, Grower, Recharge, Weigh In — gated behind the start.rugiet.com intake quiz, not submitted. Only Ready (via the /trimix lander) and the TRT line ($69 lab + from $139/mo flat) show public numbers."
  - "Pharmacy partner identity + 503A/503B compounding lane — site says 'FDA-regulated U.S. pharmacies' / 'partner pharmacies licensed at the state level,' but names no entity and states no lane."
  - "Founders, founding date, headcount, funding, corporate entity — not on the marketing site (a deep-research job, not capture)."
  - "Display typeface — branding.fonts exposes only an obfuscated 'mainFont' alias; the bold condensed grotesque is read from screenshots, not named."
  - "Self-reported user counts conflict — '500k+ men' (home/reviews) vs '400k+' (the /trimix lander); both are point-in-time marketing claims."

description: "A DTC men's 'performance medicine' telehealth brand that connects men to board-certified physicians for mostly-compounded prescription treatments — led by its 3-in-1 sublingual ED troche (Ready), plus TRT, premature-ejaculation, sleep, weight, and hair lines — shipped on subscription."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # clinician telehealth + (mostly compounded) prescription pharma
portfolio_shape: Multi-product       # four co-equal category lines (Sex, Testosterone, Sleep, Weight), ED-flagship-led
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — the vertical "RUGIET" lockup extracted from the header inline SVG
logos:                               # 2.5 module — measured by fc.py logos; the consumer applies the size bar
  wordmark: { src: assets/wordmark.svg, w: 98, h: 416 }                                                            # vertical lockup: R+up-arrow monogram over stacked U-G-I-E-T (portrait, mark+name)
  logomark: { src: "https://www.rugiet.com/IMGS/favicons/R.png", px: 1080, transparent: false }                   # white R+up-arrow monogram on a baked BLACK square (apple-touch-icon; beats the 256px google-s2)
  # og omitted — declared og:image is only 376px actual width (< 600 gate); no qualifying wide cover
brand_colors: { primary: "#FFA200", accent: "#32C9B7", text: "#292524" }  # amber-orange is the signature brand color (footer, mark, accents); teal #32C9B7 = links only; near-black text. CTAs are pure black, square-cornered. Verified vs screenshot.
fonts: []                            # branding only exposes an obfuscated "mainFont" alias; display face is a bold condensed grotesque (see Visual) — left empty over a guess
color_scheme: light                  # white chrome (branding colorScheme: light), despite heavy dark editorial photography
design_framework: next.js            # rawHtml: /_next/ ×118 + Vercel headers; Sanity CMS backend (cdn.sanity.io). NOT read from branding.designSystem.
---

## Overview

Rugiet (operating name **Rugiet Health**) is a DTC **"Performance Medicine For Men"** telehealth brand. It connects men to board-certified physicians who review a short online intake and prescribe **mostly-compounded** treatments across five areas — sexual performance (ED + premature ejaculation), testosterone (TRT), sleep, weight, and hair — fulfilled on subscription and shipped discreetly from "FDA-regulated U.S. pharmacies." The wedge is its flagship **Ready™**, a proprietary **3-in-1 sublingual ED troche** (sildenafil + tadalafil + apomorphine, delivered via its "RD-37™" sublingual system). The pitch is next-generation multi-drug formulations over "decades-old" single-ingredient generics. Self-reported scale: **"500k+ men"** and **"over 10 million doses delivered."**

## What they offer

Four co-equal category lines (Sex · Testosterone · Sleep · Weight; Hair folds into an ED combo), all subscription, all starting from the intake quiz. **Pricing is overwhelmingly quiz-gated** — only Ready and TRT carry public numbers:

- **Ready™ (flagship / best-seller):** 3-in-1 sublingual ED troche — **sildenafil + tadalafil + apomorphine**, "RD-37™" delivery, ~15-min onset / up to 36 hrs. **From ~$10–24/dose, packs of 6** `[published]` *(price only on the /trimix SEM lander; the main PDP is quiz-gated)*.
- **Go Long:** 2-in-1 premature-ejaculation + ED — **paroxetine + tadalafil** — **price behind intake** `[on-request]`.
- **Daily Boost:** daily ED + testosterone support — **tadalafil + DHEA** — `[on-request]`.
- **Grower:** 2-in-1 ED + hair growth — **tadalafil + minoxidil** — `[on-request]`.
- **Testosterone (TRT):** four forms — Enclomiphene, Injectable (testosterone cypionate), Topical, Oral — **one flat all-inclusive price: $69 lab + from $139/mo** (labs required; live video consult) `[published]`.
- **Recharge:** compounded 3-in-1 sleep Rx — **ramelteon**-based ("up to 17× stronger than melatonin") — `[on-request]`.
- **Weigh In:** compounded oral weight treatment — **bupropion + naltrexone + metformin** (notably **not** GLP-1) — `[on-request]`.

Per-SKU detail (molecule · form · visibility) in `offerings.md`; telehealth cohort cuts in `telehealth.md`.

## How it works / model

Pick a treatment → **5-minute online questionnaire** (for TRT, add a **$69 at-home/lab blood test** measuring 12 biomarkers, which includes a clinician video call) → a **board-certified physician reviews** and, if appropriate, prescribes — **asynchronously** for ED/sexual/sleep/weight, but via a **live audio-video consult** for TRT (controlled substances) → if prescribed, medication ships in unmarked packaging in **4–7 days** from FDA-regulated U.S. partner pharmacies → subscription refills + **unlimited doctor follow-ups**. *"You're only charged if prescribed."* Money is made on **subscription + medication margin**. TRT uses **flat all-inclusive pricing** ("one flat price, every medication"; labs, follow-ups, and dose switches included).

## Positioning & audience

Targets **men only** ("Performance Medicine For Men"; no women's line). Positions as premium, results-driven men's optimization — **next-generation multi-drug compounded formulations** (especially the apomorphine-containing 3-in-1 ED troche) versus commodity single-ingredient generics ("modern science, not decades-old solutions"). Voice is editorial, masculine, aspirational: *"Make your 20's jealous,"* *"the science of never settling."* ED (Ready) is the front door; TRT and the metabolic/sleep lines are the expansion. Deeper voice work belongs in `brand.md` if enabled.

## Nav structure

Top nav is shallow (mega-nav client-rendered); the footer carries the fuller map:

```
- All Treatments — /all-treatments
- Sex — /sex
  - Ready™ (ED 3-in-1) — /erectile-dysfunction/ready
  - Go Long (PE) — /premature-ejaculation/go-long
  - Daily Boost (daily ED + T) — /erectile-dysfunction/boost
  - Grower (ED + hair) — /erectile-dysfunction/grower
- Testosterone — /testosterone
  - Enclomiphene — /testosterone/enclomiphene
  - Injectable TRT — /testosterone/injectable-trt
  - Topical TRT — /testosterone/topical-trt
  - Oral TRT — /testosterone/oral-trt
- Sleep — /sleep/recharge  (Recharge)
- Weight — /weight-loss/weigh-in  (Weigh In)
- Hair — /erectile-dysfunction/grower  (footer label → the Grower ED+hair combo)
- Science — /science  ·  Reviews — /reviews  ·  Sex Score — /sex-score  ·  Refer a Friend — /refer
- Get the Rugiet App — /rugiet-app  ·  Log in / Get Started — start.rugiet.com
```

## Credibility & proof

- **LegitScript Certified** + **HIPAA Compliant** seals in the footer (LegitScript badge links to legitscript.com verification for rugiet.com).
- **Trustpilot "EXCELLENT," 4.3 / 5** (widget links to trustpilot.com/review/rugiet.com); the Ready PDP shows a product rating **"Reviews (1,208) · 4.3."**
- **Named, board-certified medical advisory board** (urology-led): **Justin Houman, MD** (urologist, men's health), **Nicholas Farber, MD** (urologist), **Vipul Khanpara, MD** (Chief Medical Officer; emergency medicine), **Asim Roy, MD** (neurologist / sleep medicine), **Andrew Y. Sun, MD** (urologist). Homepage/blog also cite Parth Shah, MD and Eric Miller, MD among others.
- **Press logos:** Men's Health, Esquire, Forbes, Inc., Innerbody.
- **Self-reported, flagged:** *"500k+ men choose Rugiet"* / *"Over 10 million doses delivered"* (the /trimix lander says *"Over 400k men"* — inconsistent); *"80% of men prefer Rugiet to other ED treatments"* (survey, n=114, May 2025); *"85% of men report feeling more confident."*
- **Compliance-forward disclaiming:** every compounded SKU carries *"compounded drugs are not approved by FDA…"*; TRT carries the controlled-substance live-consult disclaimer; testimonials are all labeled *"Verified Patient."*

## Visual & brand impression

Dark, editorial, unmistakably masculine — closer to a men's-lifestyle magazine than a clinic. Burgundy and near-black photographic grounds, gritty black-and-white and color photography (boxing, muscular and shirtless men, couples), with **amber-orange (#FFA200)** as the signature accent and **pure-black, square-cornered (0px-radius) CTAs**. Display type is a **bold condensed grotesque**; the brand mark is the distinctive **"R" + up-arrow monogram** (and a vertical "RUGIET" wordmark in the header). Confident, premium, and aspirational; product shots are clean troche/pill renders on dark grounds.

## Strategic read

ED is the wedge and the best-seller: **Ready™** — a compounded 3-in-1 troche whose differentiator is **apomorphine** (a brain/arousal agent) stacked on the standard PDE5 pair, delivered sublingually — anchors the whole catalog and is the only product whose price is even semi-public. Around it Rugiet has built the full men's-optimization stack (TRT, sleep, weight, hair). Two things stand out: (1) it is **almost entirely a compounding play** — the lone FDA-approved item is injectable testosterone cypionate; everything else (the ED combos, enclomiphene, topical/oral T, sleep, weight) is compounded, which is both the differentiation and the regulatory exposure; and (2) the **weight line is deliberately NOT GLP-1** — an oral bupropion/naltrexone/metformin stack — a contrarian stance in a GLP-1-dominated market. Pricing is engineered as a conversion funnel: numbers live behind the quiz, with only the flagship's lander and the flat TRT price exposed.

## Provenance

- **Pages:** homepage (+ rawHtml/branding/screenshot), /all-treatments (--homepage), /sex, /testosterone, /science, /reviews, /erectile-dysfunction/ready, /premature-ejaculation/go-long, /erectile-dysfunction/boost, /erectile-dysfunction/grower, /trimix (Ready SEM lander), /testosterone/{enclomiphene, injectable-trt, topical-trt, oral-trt}, /sleep/recharge, /weight-loss/weigh-in, /go-long-lander, /daily-boost-lander, /recharge-lander (**20 pages**) — all Firecrawl (`fc.py`, `maxAge:0`, `location:US`). Map returned 147 URLs (blog/author-heavy; catalog pulled from /all-treatments + homepage links).
- **Verify:** all 20 sourceURLs matched, all bodies md5-unique, no junk soft-404s (clean — no geo/cache contamination).
- **Credits:** 21 (1 map + 20 scrapes), manifest-attributed.
- **Couldn't get:** per-product all-in pricing past Ready/TRT (quiz-gated); the pharmacy partner's identity + 503A/503B lane; founders/funding/entity (not on-site).
- **Structured layer (schema 2.2):** homepage JSON-LD is a bare `WebSite` block — no `sameAs`, `logo`, or `Organization`. `socials` filled from footer anchors (instagram/facebook/linkedin/x/tiktok, all `rugiethealth`); `external` empty (none declared); `aliases` += rugiethealth.com (301 → canonical) + "Rugiet Health." `branding.images.logo` = inline data-URI SVG of the R+arrow monogram; the wordmark was extracted from the header's vertical "RUGIET" inline SVG → `assets/wordmark.svg`.
- **Run profile:** Express invocation — +`telehealth.md` cohort pack, +`offerings.md` roster, +`logos` (2.5). Wordmark extracted from the header inline SVG; logomark/og measured by `fc.py logos` (`transparent: false` judged on the rendered black square; og omitted at 376px < 600).
