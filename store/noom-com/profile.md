---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: noom.com
name: Noom
aliases: ["Noom, Inc."]
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/noom
  x: https://twitter.com/noom
  instagram: https://www.instagram.com/noom/
  youtube: https://www.youtube.com/c/NoomInc/
  linkedin: https://www.linkedin.com/company/noom-inc/
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress + Divi theme (Divi-child; tachyon/Photon image CDN, assets.noom.com + b2b-cdn.noom.com). Marketing host is large and blog/locale-heavy — /v2/map is swamped by /blog, /es, /de, /au, /research; select signal pages from homepage links + footer, not the map. Pricing is quiz-gated behind /ps/ + /survey funnels — only Med/Microdose prices surface, as homepage/PDP footnotes. Funnel routing params: ?route=clinical (Med), ?route=hrt (Menopause), feature=microdose / feature=tirzepatide. B2B arm lives under /health/*. design_framework reads WordPress (Divi) from rawHtml; branding.designSystem said 'custom' (wrong, as usual)."
key_pages:
  med: /med/
  microdose: /med/glp1-microdose/
  glp1_companion: /med/glp1-companion/
  glp1_transparency: /glp-1-access-and-transparency/
  lose_weight: /lose-weight/
  menopause: /menopause/
  about: /about-us/
  health_b2b: /health/
unverified_fields:
  - "Per-program pricing is quiz-gated — only Noom Med / Microdose floors are public (homepage + PDP footnotes); Noom Weight, Menopause/HRT, and B2B pricing not shown (intake/demo-gated)."
  - "Med pricing is a point-in-time snapshot, not fixed — 'New pricing for new accounts only effective as of March 31, 2026'; all-in medication cost varies by insurance vs. cash-pay."
  - "Founding year — 'research that began in 2008' (About) describes the founders' research, not an incorporation date; left to prose."

# Description — one sentence
description: "A digital-health company pairing a psychology-based weight-loss app with telehealth clinicians and prescription GLP-1 / HRT medications to help people lose weight and keep it off — sold direct-to-consumer and to employers and health plans."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B2C]            # DTC programs (Med/Weight/Menopause) + Noom Health sold through employers/plans/systems to their members
offering_category: [Software / SaaS, Services / Consulting, Biotech / Pharma Products]   # digital-health platform (core) + telehealth clinical care + Rx meds — a genuine 3-way hybrid
portfolio_shape: Multi-product         # several enumerable, co-equal lines: Med, Weight, Menopause/HRT, plus B2B programs
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against the homepage screenshot
logo_url: https://assets.noom.com/uploads/2022/09/Noom_Wordmark_Black.png   # canonical wordmark (JSON-LD `logo`)
logos:
  wordmark: { src: "https://assets.noom.com/uploads/2022/09/Noom_Wordmark_Black.png", w: 1860, h: 417 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=noom.com&sz=256", px: 192, transparent: true }   # coral "oo" ring + degree-dot; confirmed clean on a dark tile
  og:       { src: "https://www.noom.com/tachyon/2022/11/noom-logo-social-t.png", w: 1024, h: 512 }
brand_colors: { primary: "#2C3D49", accent: "#FB513B" }   # dark slate-navy + the signature coral (accent measured from the logomark; branding payload's #AA3521 is a darker UI red)
fonts: [Untitled Sans, BrownLLWeb]     # branding.fonts: body "Untitled Sans", heading "BrownLLWeb"
color_scheme: light
design_framework: WordPress (Divi)     # rawHtml: Divi ×59, wordpress ×40, wp-json ×4 (not branding.designSystem "custom")
---

## Overview

Noom is a consumer-led digital-health company built around a psychology-based behavior-change platform — the famous food-logging, daily-lessons, color-coded "Noom" app — that it has extended into telehealth clinical care and prescription medication. Co-founders Saeju Jeong and Artem Petakov began the research behind it in 2008; the company describes its mission as "empower everyone, everywhere to live better longer." Weight management remains the core, now delivered three ways to consumers — **Noom Weight** (app-only behavior change), **Noom Med** (GLP-1 / weight-loss medication via licensed clinicians), and **Menopause & HRT** — plus a B2B arm, **Noom Health**, that licenses the platform to employers, health plans, and health systems. As of this capture the homepage leads with medication ("Meds to lose the weight. Noom to keep it off."), reflecting a clear tilt toward the GLP-1 telehealth business while keeping behavior change as the wrapper ("Noom is *more* than medication").

## What they offer

Several co-equal lines; per-SKU/molecule depth (the full GLP-1 roster, doses, prices) lives in [`offerings.md`](offerings.md). Family lines, bold-led with price-visibility tokens:

- **Noom Med — GLP-1Rx Program:** telehealth weight-loss medication paired with the app + clinician care; access to brand-name GLP-1s (Ozempic®, Wegovy®, Zepbound®, Mounjaro®) plus compounded and generic GLP-1s — **"Initial 3 week subscription and 4 weeks of medication from $149 plus tax and $349 per month plus tax for 12 week subscription thereafter"** `[partial]` (program floor; medication cost varies by insurance vs. cash-pay).
- **Noom Microdose GLP-1Rx Program:** a lower-dose, lower-cost entry path — **"plans start at $79"** / "direct access to GLP-1s starting at $99… regardless of insurance, when prescribed" `[partial]`.
- **Noom GLP-1 Companion (with Muscle Defense™):** the digital layer that wraps the meds — SmartDose titration, AI nutrition/macro tracking, muscle-preserving workouts, AI Body Scan, Glucose Forecasting — **"included at no additional cost with a Noom plan for eligible members taking GLP-1 medication"** `[published]`; also sold B2B as a standalone companion.
- **Noom Weight:** the original psychology-based, app-only program (daily lessons, coaching, food/water/exercise logging, no medication) — **pricing quiz-gated**, "in most cases you can start with a free trial" `[on-request]`.
- **Menopause & HRT (HRTRx):** hormone replacement therapy for menopause (patches, creams, gels, sprays, pills — estrogen + bioidentical progesterone) bundled with the behavior program — **pricing quiz-gated** `[on-request]`.
- **Noom Health (B2B):** the platform licensed to employers / health plans / health systems — Weight Management, **CDC-recognized Diabetes Prevention** (Full Plus Recognition), Diabetes Management, Obesity Care (Noom Med), GLP-1 Companion, and **SmartRx** (a GLP-1 pharmacy cost carve-out that bypasses PBM intermediaries) — **enterprise / "Request Demo"** `[on-request]`.

## How it works / model

**Customer journey (Med):** take a brief online intake survey (health history, goals, identity verification, a required full-body photo) → a licensed clinician evaluates asynchronously and prescribes if clinically appropriate → medication is shipped (~7 days) or coordinated through a pharmacy → ongoing care, refills, and behavior support through the Noom app and unlimited clinician chat. Care is **asynchronous-first** ("access-maximizing asynchronous care pathways… in some programs, synchronous video visits are also available"). Noom does **not** operate its own pharmacy — it "partner[s] with U.S. Pharmacopeia (USP)-compliant, state-regulated pharmacies for plans that include medication."

**How they make money:** DTC subscriptions (a recurring program fee; for the compounded GLP-1 path medication is bundled into the price, while brand-name is membership + the medication's out-of-pocket cost via insurance) and B2B platform contracts with employers, plans, and systems. FSA/HSA-eligible; works with insurance to maximize coverage but also offers cash-pay.

## Positioning & audience

Noom positions against two adjacencies at once: pure-medication GLP-1 telehealth (it argues "medication alone is not enough" — most people stop GLP-1s and can lose up to 40% of weight as muscle without behavior change) and pure-behavior-change apps/programs (it now offers the meds those lack). Its claimed edge is the marriage of the two — "**Noom Med users lose 48% more weight in 6 months vs. those taking GLP-1 medications without Noom**" and "9 in 10 doctors recommend pairing GLP-1s with lifestyle changes." Audience is broad and all-genders for weight loss; the Menopause & HRT line targets women specifically. The "live better longer," metabolic-health, and microdose framing pushes toward a longevity/whole-health narrative under CMO Dr. Jeffrey Egler.

## Nav structure

```
- For Individuals
  - Noom Med — /med/
  - Lose Weight — /lose-weight/  (footer: /weight-loss/)
  - Menopause & HRT — /menopause/
  - Personality Quiz — /f/personality-quiz
  - Calorie Calculator — /f/calorie-deficit-calculator
  - Macro Calculator — /f/macro-calculator
- For Organizations — /health/
  - Employers — /health/employers/
  - Health Plans — /health/health-plans/
  - Health Systems — /health/health-systems/
  - Resources — /health/resources/
- Company
  - About Us — /about-us/
  - Careers — /careers/
  - Our Approach → Research — /research/
  - Press — /press-and-media/
  - Blog — /blog/
  - Investors — /noom-company-overview/
  - Noom Books — /book/
- Languages — EN / DE (/de) / ES (/es) / KR (ko-noom.com)
- Footer · Resources: Support — /support/ · GLP-1 Access & Transparency — /glp-1-access-and-transparency/ · GLP-1 Companion — /med/glp1-companion/ · HRT Safety — /menopause/hrt-safety-and-transparency/ · Brand Ambassadors — /creators-community/ · Investors — /noom-company-overview/
```

## Credibility & proof

- **LegitScript Certified** — footer seal linking to legitscript.com.
- **CDC recognition** — the Diabetes Prevention Program holds "Full Plus Recognition" from the CDC (B2B page).
- **Named clinical leadership** — CMO **Dr. Jeffrey Egler** (double board-certified, Family + Lifestyle Medicine); Executive Director of Women's Health **Dr. Julia Edelman** (gynecologist, menopause author); Medical Director **Dr. Karen Mann** (OB-GYN, obesity-medicine diplomate); Head of Healthcare/Pharmacy Operations **Dr. Yalda Olcott, PharmD**; a Science Advisory Board (Lindsey Connors PharmD, Pouran Faghri, Andrew Gostine MD).
- **Press logos (self-presented "As seen in"):** Forbes, The New York Times, Bloomberg, Fortune, Fast Company, Healthline, WebMD.
- **B2B customers named:** Mount Sinai, Brigham & Women's, Houston Methodist, CareFirst, US Venture, Gwinnett County.
- **Self-reported proof (verbatim, flagged self-reported):** "helped millions"; "**98% of Noomers say Noom helps change their habits and behaviors for good**"; "**Noom Med users lose 48% more weight in 6 months**" vs. meds alone (retrospective self-reported study); "**50+ peer-reviewed publications and 10+ academic medical research collaborations**" (B2B); "for over 15 years."
- **Medication disclaimer (verbatim):** "Medications included in Noom GLP-1Rx Program are produced in USP-compliant, state-regulated pharmacies but not reviewed by the FDA for safety, efficacy or quality… any compounded medications are not approved by the FDA."

## Visual & brand impression

Mature, well-resourced consumer-health brand. Warm, optimistic palette: a cream/off-white canvas, a signature vivid **coral (#FB513B)** accent, and a dark slate-navy (#2C3D49) for dark sections and type. The logomark is a friendly coral "oo" — a large ring plus a small circle with a degree-dot — that doubles as a standalone symbol; the wordmark is a lowercase rounded-geometric "noom" in near-black. Heavy use of circular-framed smiling member photos, app-screen mockups, and a four-pointed coral "sparkle/diamond" motif as a repeated brand marker. The overall feel is approachable wellness-tech, not clinical — friendly, habit-forming, mass-market — with clear conversion scaffolding (repeated "See if you qualify" / "Start your trial" CTAs, quiz funnels) typical of a high-spend DTC operation.

## Strategic read

The capture catches Noom mid-pivot: a behavior-change app company that has bolted on a full GLP-1 telehealth + pharmacy-coordination business and now leads with it. Three things stand out. (1) **"Bridge, not band-aid"** — Noom's whole differentiation narrative is that meds without behavior change fail (muscle loss, rebound, 71% stop by 12 months), positioning its app as the durable asset and the GLP-1 as the on-ramp; *Muscle Defense™* and the *Microdose* low-and-slow program operationalize that. (2) **Vertical breadth as a hedge** — weight, menopause/HRT, diabetes, and metabolic/longevity all run on the same behavior-change engine, letting Noom ride the GLP-1 wave without being only a GLP-1 router. (3) **SmartRx is a quietly distinct play** — a B2B GLP-1 cost carve-out that "bypass[es] PBM intermediaries," aiming Noom at the employer drug-cost problem, not just the consumer. Caveat: outcome stats are overwhelmingly self-reported retrospective analyses of Noom's own users — recorded here verbatim, not endorsed.

## Provenance

- **Pages:** 9 analyzed via Firecrawl (maxAge:0, US, waitFor) — homepage, /med/, /med/glp1-microdose/, /med/glp1-companion/, /glp-1-access-and-transparency/, /lose-weight/, /menopause/, /about-us/, /health/. Plus /v2/map (blog/locale-swamped; key pages selected from homepage links + footer). Structured layer via `fc.py signals` (JSON-LD Organization/WebSite/FAQ + nav).
- **Verify:** all 9 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 10 (1 map + 9 scrapes; all base 1cr, no proxy escalation).
- **Couldn't get:** per-program pricing for Noom Weight, Menopause/HRT, and B2B (all quiz/demo-gated); exact all-in medication costs (vary by insurance/cash-pay); the full GLP-1 SKU roster's per-SKU prices (PDP/quiz-gated — see offerings.md).
- **Run profile:** guided — emphasis "center on Noom Med"; +telehealth, +offerings, +logos. Page selection weighted to the Med/GLP-1 arm; universal profile contract still filled across all lines.
