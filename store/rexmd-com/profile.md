---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: rexmd.com
name: Rex MD
aliases: ["REX MD", "TestoRx"]        # TestoRx = the testosterone-program brand name (FAQ)
parent: [lifemd.com]                  # "Rex MD's parent company LifeMD" — FAQ (insurance routed to parent); LifeMD's own profile lists owns:[rexmd.com]
owns: []
socials: {}                           # looked — no social links in captured markup/JSON-LD (no JSON-LD on homepage)
external: {}                          # no third-party identity records surfaced (no JSON-LD sameAs)

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Custom PHP site (.php pages: faq/privacy/telehealth; hashed /assets/; NO JS-framework markers and NO JSON-LD on homepage). Per-SKU ED/hair/sleep/PE/herpes prices live on the master /our-medications/ index grid (dose+price cards) and as 'From $X per use' on category pages; TRT + WM are priced as BUNDLED PROGRAMS ($99 one-time + from $250/mo; $75) not per-SKU. Funnel subdomains: ed.rexmd.com (X1HRT ED LP), rx.rexmd.com (beta-blockers, sleep-ret, wm1), members.rexmd.com (member portal). Persistent 'Memorial Day Sale — Save Up To 95% Off ED Meds / $2 Per Tablet' promo banner sitewide → pricing is promo-driven snapshot. Map is ~90% /learn/* blog noise; select key pages from homepage links. Anxiety/beta-blocker line lives on rx.rexmd.com (not captured)."
key_pages:
  our_medications: /our-medications/
  ed: /our-medications/erectile-dysfunction/
  testosterone_program: /our-medications/testosterone-program/
  weight_management: /our-medications/weight-management/
  how_it_works: /how/
  about: /about/
  telemedicine: /telemedicine/
  reviews: /reviews/
  faq: /faq.php
unverified_fields:
  - "Prices/IA are a point-in-time snapshot, not fixed — a sitewide 'Memorial Day Sale, up to 95% off ED meds / $2 per tablet' promo drives ED pricing; per-SKU TRT/WM med costs are set within bundled programs after consult/labs."
  - "Anxiety / beta-blocker (propranolol) line lives on rx.rexmd.com/beta-blockers — not captured; price unverified."
  - "Finasteride monthly price disagrees across captured pages: '$13.50 per month' on /our-medications vs 'as low as $18 per month supply' in faq.php — both quoted, discrepancy unresolved."
  - "No aggregate numeric review score on captured pages — /reviews is self-reported '5-Star / 100% Verified', no Trustpilot/rating number shown."

description: "Delivers prescription men's-health treatments — ED, testosterone, GLP-1 weight loss, hair, sleep, PE — to U.S. men through licensed-clinician telehealth, shipping generic, brand, and compounded meds from partner pharmacies on cash-pay subscriptions."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company                  # runs its own P&L / storefront; owned by LifeMD (parent:)
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth = clinical service + prescription meds
portfolio_shape: Multi-product        # 8 distinct condition lines: ED, PE, weight, testosterone, hair, sleep, herpes, anxiety
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; confirmed against screenshot + wordmark SVG
logo_url: https://rexmd.com/assets/img/svg/rex-logo.svg          # canonical wordmark (navy "REX" + red "MD")
logos:
  wordmark: { src: "https://rexmd.com/assets/img/svg/rex-logo.svg", w: 167, h: 47 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=rexmd.com&sz=256", px: 64, transparent: false }   # 64px (under the 128 bar — recorded anyway); navy box baked behind "REX", not transparent
  og:       { src: "https://rexmd.com/assets/images/rexmd-og.webp?21", w: 1071, h: 662 }
brand_colors: { primary: "#0A1C2B", accent: "#B32025" }   # STRAIN: navy wordmark "REX" + signature red "MD"/crown/sale banners; bright mint #23F197 is the CTA-button accent (branding payload) — see Visual
fonts: [Campton, Root-Campton]
color_scheme: light
design_framework: custom              # rawHtml: hashed /assets/ only, .php pages, no __NEXT_DATA__/wp-content/framework markers (branding said "custom" — corroborated here, unusually)
---

## Overview

Rex MD is a direct-to-consumer **men's-health telehealth platform** (launched November 2019, owned by **LifeMD**) that connects U.S. men with licensed clinicians who prescribe and ship medication to the door. It began with — and still leads on — **sexual health / erectile dysfunction**, then expanded into a broad men's formulary: a testosterone program, GLP-1 weight loss, hair loss, premature ejaculation, sleep, herpes, and anxiety. The pitch is convenience + discretion + price: a free online intake, no in-person visit, free discreet shipping, free follow-ups, and cash-pay medication "without breaking the bank." Self-reported scale: **"over 475,000 patients."**

## What they offer

Eight condition lines, all sold as cash-pay subscriptions (bold lead-in, verbatim price + visibility token; per-SKU detail in `offerings.md`):

- **Erectile dysfunction (the anchor):** generic Viagra (sildenafil) **"From $6 per use"**, generic Cialis (tadalafil) **"From $6 per use"**, daily generic Cialis **"From $2 per use"**, branded Cialis® **"From $29 per use"**, branded Viagra® **"From $96 per use"** — promo "**$2 Per Tablet**" `[published]`
- **Testosterone Program ("TestoRx"):** cypionate injection (Schedule III), testosterone gel 1.62% CIII, Clomid® (clomiphene), sermorelin — **"$99"** one-time (lab panel + video consult), then **"as low as $250 per month"** `[partial]`
- **Weight management (GLP-1):** program **"starts at $75"**; branded meds via manufacturer cash-pay — Wegovy® (semaglutide) **"$499 per month"** via NovoCare®, Zepbound® (tirzepatide) **"$349 per month"** via Eli Lilly `[partial]`
- **Hair loss:** finasteride **"$13.50 per month"** (faq.php says **"$18 per month"**) `[published]`
- **Premature ejaculation:** sertraline (generic Zoloft) **"$27 per month"** `[published]`
- **Insomnia / sleep:** ramelteon **"$2.11 a dose"**, doxepin **"$1.70 a dose"** `[published]`
- **Herpes:** valacyclovir **"$27 per month"** (3-month supply) `[published]`
- **Anxiety:** beta-blocker (propranolol) — on rx.rexmd.com, not captured `[on-request]`

## How it works / model

Free online medical **intake form** → government-ID + face-photo identity check → a Rex MD-affiliated provider reviews and prescribes if appropriate → a **partner pharmacy** ships in discreet packaging, free, within ~2 days → ongoing care via the **member portal** (unlimited messaging; follow-ups free). Modality is **both asynchronous and synchronous** — "store-and-forward" intake for most, with a **video consult required** for controlled substances (testosterone) and where states mandate it. Revenue is recurring medication subscriptions; the testosterone ($99 + $250/mo) and weight ($75) lines are sold as **bundled programs**. **Cash-pay only** — "Rex MD does not accept insurance"; GLP-1 meds route to manufacturer cash-pay channels (NovoCare/Eli Lilly), and insurance-seeking patients are deflected to parent **LifeMD**.

## Positioning & audience

Targets **men only** ("Telemedicine for Men," "for use by MEN ONLY"), against Hims, Ro, Maximus, and other men's telehealth brands. Claimed edge: convenience and discretion versus the in-person clinic ("40% of men only see a provider when faced with a serious health concern"), plus affordability and breadth across men's daily-health conditions. The regal "Rex" (Latin for *king*) identity — crown motif, "take charge" language — frames the brand around male confidence; ED is the wedge ("475,000 men… take charge of their sexual health").

## Nav structure

```
- Sexual Health — /sexual-health/
  - Erectile Dysfunction — /our-medications/erectile-dysfunction/
    - Branded Viagra — /our-medications/erectile-dysfunction/branded-viagra/
    - Generic Viagra (sildenafil) — /our-medications/erectile-dysfunction/generic-viagra-sildenafil/
    - Branded Cialis — /our-medications/erectile-dysfunction/branded-cialis/
    - Generic Cialis (tadalafil) — /our-medications/erectile-dysfunction/generic-cialis-tadalafil/
    - Daily Generic Cialis (tadalafil) — /our-medications/erectile-dysfunction/daily-generic-cialis-tadalafil/
  - Premature Ejaculation — /our-medications/premature-ejaculation/
    - Sertraline — /our-medications/premature-ejaculation/sertraline/
- Weight Loss — /weight-management/
  - Semaglutide (GLP-1) — /our-medications/weight-management/semaglutide/  (Wegovy®; Zepbound®/tirzepatide + Saxenda® named in copy)
- Sleep — /sleep/  (Insomnia & Sleep — /our-medications/insomnia/)
  - Doxepin — /our-medications/insomnia/doxepin/
  - Ramelteon — /our-medications/insomnia/ramelteon/
- Testosterone — /testosterone/  (Testosterone Program — /our-medications/testosterone-program/)
  - Testosterone Cypionate — /our-medications/testosterone-program/cypionate/
  - Testosterone Gel — /our-medications/testosterone-program/testosterone-gel/
  - Clomid® — /our-medications/testosterone-program/clomid/
  - Sermorelin — /our-medications/testosterone-program/sermorelin/
- Hair — /hair-growth/
  - Finasteride — /our-medications/hair-loss/finasteride/
- Anxiety — https://rx.rexmd.com/beta-blockers/  (Beta blocker / propranolol — separate subdomain)
- Herpes Breakouts — /our-medications/herpes/
  - Valacyclovir — /our-medications/herpes/valacyclovir/
- Medications — /our-medications/   ·   Reviews — /reviews/   ·   How it Works — /how/   ·   Login — https://members.rexmd.com/
```

Homepage "Top Products" carries the brand's own prominence badges: **Featured** on Generic Viagra (Sildenafil), Branded Viagra by Pfizer, and Zepbound® Vial GLP-1; **Popular** on Ramelteon Sleep Aid.

## Credibility & proof

- **LegitScript Certified:** footer seal links to legitscript.com verification (seal #4418850) — "having undergone rigorous third-party reviews."
- **HIPAA:** "complies with all applicable HIPAA regulations"; discreet, nondescript packaging.
- **Scale (self-reported):** "Chosen by over 475,000 patients"; "about 90% of them said Rex MD helped raise their confidence"; "Over 90% of patients would recommend Rex MD to a friend."
- **Clinicians:** providers and nurse practitioners "board-certified," "U.S. state-licensed and U.S.-based"; Dr. Anthony Puopolo featured (the telehealth-visit face on homepage/PDPs). No standalone /physicians roster captured.
- **Reviews:** /reviews is "Rex MD® 5-Star Reviews," "100% Verified Reviews," "from real patients… verified purchases" — self-reported, no aggregate numeric score shown.
- **Compounding safety claim (verbatim):** "All ingredients in our partnered pharmacy's compounded medications are sourced from FDA registered manufacturers and are tested for impurities… To date, no third-party testing failures have been noted."

## Visual & brand impression

Confident, masculine, conversion-optimized DTC. Identity pairs a **deep navy** (`#0A1C2B`/`#121628`) with a **signature red** (`#B32025`) — the "MD" in the wordmark, the crown motif (Rex = king), and the ever-present red sale banner — over white, with a bright **mint-green CTA accent** (`#23F197`) doing the button work. Product photography splits two ways: warm lifestyle imagery (couples in bed, smiling middle-aged men) for the condition heroes, and clean isolated navy-label REX MD product renders (vials, bottles, the blue sildenafil tablets, branded Wegovy/Zepbound pens) on the PDPs. Typography is Campton (a geometric sans). The overall read is a mature, well-funded men's-health brand leaning hard on urgency/discount messaging.

## Strategic read

- **ED is the origin and the front door, but the formulary is now broad** — testosterone (a Schedule-III TRT program with real labs/video gating) and GLP-1 weight loss are the growth vectors, mirroring the category-wide pivot. Unlike Hims, the GLP-1 line is **FDA-brand-routed** (Wegovy via NovoCare, Zepbound via Lilly) now that the compounded-semaglutide shortage exemption has ended — Rex states plainly that "pharmacies can no longer compound semaglutide."
- **Parent LifeMD is a load-bearing relationship**, not a footnote: insurance-seeking and branded-GLP-1 patients are actively deflected to lifemd.com, so Rex functions as LifeMD's cash-pay men's-DTC front end.
- **Pricing is promo-engineered** — the "$2 per tablet / up to 95% off" ED hook is a persistent acquisition wedge, and the TRT/WM programs bundle the real cost behind a low entry fee. Treat any captured price as a snapshot.

## Provenance

- **Pages:** 14 analyzed via Firecrawl (maxAge:0, US geo) — homepage + /our-medications (rich index) + ED/TRT/WM/hair category pages + 3 flagship PDPs (sildenafil, cypionate, semaglutide, with images) + /how, /about, /telemedicine, /reviews, faq.php.
- **Verify:** all 14 sourceURLs matched; all body md5s unique (no §5.1 contamination).
- **Credits:** 15 this run (1 map + 1 homepage + 13 key-page scrapes; hero/logos/signals were free reads of persisted payloads).
- **Couldn't get:** anxiety/beta-blocker line (rx.rexmd.com — separate subdomain, not scraped); no aggregate review score on captured pages; no named-pharmacy entity or 503A/503B lane stated.
- **Run profile:** guided — emphasis "men's telehealth"; +offerings (per-SKU roster), +telehealth (cohort pack), +logos, +offerings hero images (3 flagship PDPs captured with --images, clean renders promoted to captures/2026-06-04/images/).
