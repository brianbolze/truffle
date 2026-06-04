---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: mydrhank.com
name: MyDrHank
aliases: []
parent: []
owns: []
socials: {}                          # no JSON-LD sameAs; footer carries only Privacy/Terms/Contact — looked, none found
external: {}

# Capture meta
captured_at: 2026-06-03
capture_method: firecrawl
site_notes: "Cloudflare-fronted custom React/Vite SPA (built on Lovable — og:image served from a lovable.app r2 bucket). The catalog is NOT a CMS: the product registry is a hard-coded `Ep=[{slug,name,category,…}]` array inside `assets/index-*.js`; `/products.json`, `/sitemap.xml`, `/wp-json` all 404 or return the SPA shell (soft-200). The catch-all serves HTTP 200 + HTML for ANY unmatched path — trust the bundle registry, never a guessed URL. One hidden SKU: `/products/hair-combo` is a live PDP filtered out of every menu (`Ep.filter(d=>d.slug!=='hair-combo')`). Every PDP shows a `From $X/mo` floor; the binding all-in is set inside the gated `join.mydrhank.com` intake. Prices are hard-coded in the bundle (stable per deploy), but `/glp/lp/v1–v3` + `/sermorelin/lp/v1–v2` landing variants + GTM A/B-test copy/IA. A/B: yes. No about/company page — Contact routes to `/reorder`."
key_pages:
  weight_loss: /weight-loss
  longevity: /longevity
  sexual_health: /sexual-health
  hair_growth: /hair-growth
  intake: https://join.mydrhank.com/start-online-visit/
  contact: /reorder
unverified_fields:
  - "Binding all-in price for every SKU — only `From $X/mo` floors shown; the real price (dose/plan/formulation) is set inside the gated join.mydrhank.com intake. All 16 SKUs are `partial`."
  - "Prices/IA are a point-in-time snapshot, not fixed — JS-bundle prices are stable per deploy, but GTM + /glp/lp & /sermorelin/lp landing variants A/B-test marketing copy and module order."
  - "Company background — no about/company page exists (Contact → /reorder); founding date, HQ, team, and legal entity are not on the marketing site."

description: "Delivers compounded weight-loss, longevity, sexual-health, and hair-loss prescriptions to consumers via a free online intake and U.S.-licensed provider review, then ships each medication to the door — no insurance or membership required."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://mydrhank.com/assets/logo-Dk6R4bNG.png   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: https://mydrhank.com/assets/logo-Dk6R4bNG.png, w: 400, h: 84 }                                                     # "MyDrHank" two-tone mark, transparent bg
  logomark: { src: "https://www.google.com/s2/favicons?domain=mydrhank.com&sz=256", px: 256, transparent: true }                      # cyan disc, knockout mark; transparent corners (judged on a dark tile)
  og:       { src: "https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/734e7d20-ee5c-471e-b7ac-95080cb89f71/id-preview-cd44094d--20838f16-0462-4222-ba38-f8398ff314cc.lovable.app-1779988038245.png", w: 1920, h: 1080 }   # auto-generated homepage preview (Lovable), not a designed share card
brand_colors: { primary: "#193367", accent: "#FAF8F5" }   # two-tone navy-on-cream; no bright accent (accent here is the cream ground)
fonts: [Manrope, Noto Serif]         # body Manrope (sans), headings Noto Serif (serif)
color_scheme: light
design_framework: react (vite SPA)   # rawHtml: /assets/index-*.js + id="root", no __NEXT_DATA__/_next — Vite React template; built on Lovable
---

## Overview

MyDrHank is a direct-to-consumer telehealth brand selling **compounded prescription medications** across five wellness lines — Weight Loss (GLP-1), Longevity (NAD+/glutathione), Sexual Health (ED), Hair Growth, and a one-product "Strength" line (sermorelin). The model is uniform: a free **~5-minute online intake** → **U.S.-licensed provider review within 48 hours** → ships from an **FDA-registered compounding pharmacy** in discreet packaging, with ongoing check-ins and unlimited messaging. GLP-1 weight loss is the hero — the homepage eyebrow calls it *"our most popular treatment."* There is **no insurance, no membership, and no consult fee** — patients pay only a per-month medication price.

## What they offer

Five lines, all subscription, all compounded + Rx-gated. Every SKU shows a **`From $X/mo` floor** with the binding price set behind the intake, so all are `[partial]` (no flat published price anywhere on the site). 16 buyable SKUs total — per-SKU roster in [`offerings.md`](offerings.md).

- **Weight Loss (GLP-1):** oral + injectable semaglutide and tirzepatide (+ B-12) — **from $171–$240/mo** `[partial]` · the flagship, the only line whose category page shows prices, owns the homepage weight-loss calculator
- **Longevity:** NAD+ and glutathione, each as nasal spray + injection — **from $103–$155/mo** `[partial]`
- **Sexual Health (ED):** sildenafil, tadalafil (as-needed + daily), and MDH Drive (sildenafil + tadalafil rapid-dissolve, "works in 15 min") — **from $25–$45/mo** `[partial]`
- **Hair Growth:** minoxidil (oral), finasteride, Custom Hair Protocol (5-formulation quiz, female-safe options) + a hidden 3-in-1 combo SKU — **from $30–$52/mo** `[partial]`
- **Strength:** Sermorelin, "a growth hormone-releasing peptide" injectable — **from $137/mo** `[partial]`

## How it works / model

1. **Complete your intake** — short online medical questionnaire, *"~5 minutes,"* no waiting room, no insurance.
2. **Provider review** — *"A U.S.-licensed clinician reviews your case and writes your prescription within 48 hours."*
3. **Delivered to your door** — *"ships from an accredited compounding pharmacy in discreet packaging."*
4. **Ongoing clinical support** — check-ins, dose adjustments, unlimited messaging with the care team.

**Money:** subscription — patients pay a per-month medication price only. Free consultation, free delivery, no insurance, no membership tier, no separate consult fee. The displayed `From $X/mo` is an entry floor; the all-in (dose, plan, formulation) is set inside the gated `join.mydrhank.com` intake. Everything dispensed is **compounded** — including the "FDA-approved active ingredient" SKUs (minoxidil, finasteride).

## Positioning & audience

Skews male but not exclusively — Sexual Health is ED (male) and Sermorelin is "Strength," while Weight Loss and Longevity copy is gender-neutral and the Custom Hair Protocol offers *"female-safe formulations."* The hero positions broadly: *"Personalized care for weight, longevity & sexual wellness."* Claimed edge is **clinician-led personalization over algorithmic/cookie-cutter telehealth** — *"Your doctor, not an algorithm"*, *"a treatment plan built from scratch"*, *"Ongoing, not transactional."* The pricing pitch is friction-light: *"No insurance required · Free consultation · Transparent pricing · Free delivery."* Competes in the DTC men's-health/telehealth space against Hims, Hone, Ro and similar — but distinguishes on the absence of a membership/consult-fee stack.

## Nav structure

```
- Weight Loss — /weight-loss
  - Oral Semaglutide — /products/oral-semaglutide
  - Compounded Semaglutide — /products/compounded-semaglutide
  - Compounded Tirzepatide — /products/compounded-tirzepatide
- Longevity — /longevity
  - NAD+ Nasal Spray — /products/nad-nasal-spray
  - NAD+ Injection — /products/nad-injection
  - Glutathione Nasal Spray — /products/glutathione-nasal-spray
  - Glutathione Injection — /products/glutathione-injection
- Sexual Health — /sexual-health
  - MDH Drive — /products/2-in-1-rdt
  - Generic Sildenafil — /products/sildenafil
  - Generic Tadalafil — /products/generic-tadalafil
  - Daily Tadalafil — /products/daily-tadalafil
- Hair Growth — /hair-growth
  - Custom Hair Protocol — /products/custom-hair-protocol
  - Minoxidil — /products/minoxidil
  - Finasteride — /products/finasteride
- Strength (dropdown, no category page)
  - Sermorelin — /products/sermorelin
- Contact — /reorder
```
*The hidden `/products/hair-combo` (3-in-1 Hair Combo, From $52/mo) is a live PDP filtered out of every menu — see [`offerings.md`](offerings.md).*

## Credibility & proof

- **"10,000+ patients treated":** homepage hero, beside three patient avatars — **self-reported**, no source.
- **LegitScript certified:** a LegitScript verification seal in the footer links to `legitscript.com/websites/?checker_keywords=mydrhank.com` — third-party pharmacy/telehealth certification (verifiable, not self-asserted).
- **Clinical-trial efficacy claims:** *"Up to 20.9% body weight loss in clinical trials"* (Tirzepatide, SURMOUNT-1, NEJM 2022) and ~15% (Semaglutide, STEP 1, NEJM 2021) — cited to the trials, with an explicit disclaimer that *"Data reflects FDA-approved formulations. The compounded medications dispensed by MyDrHank are not FDA-approved."*
- **Provider + pharmacy claims:** *"U.S.-licensed providers review every case"*; medication *"ships from an accredited compounding pharmacy" / "FDA-registered U.S. pharmacy."*
- **Compliance disclaimer site-wide:** every page carries *"Compounded medications are not FDA-approved and have not been evaluated by the FDA…"* — a regulatory honesty signal, not a trust badge.

## Visual & brand impression

Polished, modern DTC-telehealth aesthetic. A disciplined **two-tone palette — deep navy (#193367 / #001D57) on warm cream (#FAF8F5)**, no bright accent — reads clinical but premium. **Serif headings (Noto Serif) over a sans body (Manrope)** lend an editorial, trustworthy tone over what is functionally a storefront. A consistent product-card system (uniform blue vial/pill renders) and warm lifestyle photography (men, a couple) signal approachable, masculine-leaning wellness. Design maturity is high and consistent — though the `og:image` is served from a **`lovable.app` preview bucket**, indicating the site was built on Lovable (the AI app builder), consistent with the hand-rolled Vite/React SPA.

## Strategic read

- **The catalog is a JS bundle, not a CMS.** A lightweight, builder-made (Lovable/Vite) storefront rather than Shopify/WordPress — fast to ship, low engineering surface, but no real product API; the hard-coded `Ep` registry *is* the source of product truth.
- **Friction-light pricing is the structural wedge.** Unlike cohort peers Hims/Hone (whose `med + membership` stacks drive their pricing), MyDrHank has **no membership, no consult fee, no drug-bought-elsewhere** — just a per-month medication floor. Cleaner pitch, but the binding price still hides behind the intake.
- **Heavy reliance on compounding.** Everything — even the FDA-approved-ingredient hair SKUs — is dispensed as a compounded product, carrying meaningful regulatory exposure amid tightening scrutiny of compounded GLP-1s.
- **One hidden SKU** (`hair-combo`) is live but filtered from every menu — likely a funnel-/legacy-only PDP superseded by the visible Custom Hair Protocol.

## Provenance

- **Pages:** 21 pages analyzed (homepage + 4 category + 16 PDP), all in `captures/2026-06-03/`, plus the `/map` census and the JS-bundle product registry; method `firecrawl` (all-formats, US, maxAge:0).
- **Verify:** all 16 PDPs returned unique content md5s — no geo/cache contamination (prior run); profile lint re-run post-write.
- **Credits:** 0 this run — `profile.md` synthesized from the warm 2026-06-03 capture; that capture spent 22 credits (1 map + 1 homepage + 4 category + 16 PDP). No new spend.
- **Couldn't get:** binding all-in prices (gated `join.mydrhank.com` intake); company background (no about page — Contact → `/reorder`), so founding/HQ/team/legal entity are unavailable from the site.
- **Run profile:** `profile.md` back-filled from the warm 2026-06-03 capture (a prior run wrote `offerings.md` but no Tier-0 profile); no re-capture. +offerings module already present; +logos added (wordmark from `logo_url`, logomark via google s2, og = declared Lovable preview). 0 credits.
