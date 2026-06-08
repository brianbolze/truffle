---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: rugiet.com          # company key; each offering's slug (its relative url) is its key *within* Rugiet
captured_at: 2026-06-07     # own freshness; captures/2026-06-07/ holds the source pages
enumeration: indexed-complete   # all 4 category lines rostered at SKU grain from /all-treatments + per-category hubs, cross-checked vs /map
site_notes: "Catalog enumerated from /all-treatments + the /sex and /testosterone hubs (Next.js/Sanity SPA; no CMS REST backend). ALL commerce is on the start.rugiet.com quiz funnel — product PDPs carry NO price. The only public numbers: Ready's per-dose pricing lives ONLY on the /trimix SEM lander ($14–24/dose by strength, packs of 6); the TRT line shows '$69 lab + from $139/month' flat on the hub/PDP FAQs. The `-lander` SEM pages (go-long-lander, daily-boost-lander, recharge-lander) do NOT expose pricing. `/trimix` is a Rugiet Ready landing page, not a Trimix product — Rugiet sells no trimix. Promos rotate (15% off Ready, 'buy 2 months get 1 free') — prices are point-in-time."
---

## Portfolio overview

Rugiet is **Multi-product** but **heavily ED-anchored** — four co-equal category lines (**Sexual Performance, Testosterone, Sleep, Weight**), with the 3-in-1 ED troche **Ready™** as the clear flagship. **Ten buyable SKUs**, and the defining shape finding: **almost the entire catalog is compounded multi-drug formulation** — only **injectable testosterone cypionate** is FDA-approved. Each compounded SKU carries the *"compounded drugs are not approved by FDA"* disclaimer; the three TRT replacement forms add the controlled-substance disclaimer.

**Visibility rule (stated once, applied to every row).** Rugiet runs a **price-gated funnel**: numbers live behind the start.rugiet.com intake quiz, not on the PDPs.
- **`published`** — a real entry number is shown somewhere public. Hits only **Ready** (per-dose pricing, but *only* on the `/trimix` lander — see the deep block) and the **four TRT forms** (a single flat *"from $139/month"* + a *"$69"* lab fee, shown in the /testosterone and TRT-PDP FAQs).
- **`on-request`** — **no price anywhere public**; you must finish the quiz to see it. Hits **Go Long, Daily Boost, Grower, Recharge, Weigh In** — and even Ready's main PDP (its number is recoverable only from the lander).

So the pricing shape is **two patterns**: the **TRT line is one flat all-inclusive price** ($139/mo, every medication, labs + follow-ups included), and **everything else is quiz-gated**, with the flagship's per-dose price surfacing only on a paid-search lander.

**Prominence (calibrated).**
- **Ready is the lead, by a wide margin [HIGH]** — the homepage hero, the **"Best Seller"** badge, the only product with a (semi-)public price, the first card on every category surface, and the target of the brand's SEM spend (the `/trimix` lander + the "2 months free" / "15% off" promo rail all push Ready).
- **Company-stamped badges [HIGH] (within-line):** Ready = **"Best Seller"**; Go Long = **"Popular."**
- **Catalog order [MED]:** /all-treatments runs **Sexual Performance → Testosterone → Sleep, Weight & Hair** — sexual performance first and deepest (4 SKUs), TRT second (4 forms), sleep/weight/hair last (1 each).
- **Hair has no line of its own [MED]** — the footer "Hair" link points to **Grower**, an ED+hair combo filed under sexual performance.

## Roster

Complete at the indexed level (Rugiet's own product cards) across all four lines. Price quoted verbatim with its on-page markers; **molecule/form page-attested only** (never inferred from a name — see the molecule audit under Verbatim anchors). A slug here is an attested URL from a captured page.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Sexual Performance** | family | — | `/sex` | — | — | ED + premature-ejaculation Rx + an ED/hair combo; compounded, async intake, self-contained subscriptions. |
| Ready™ | buyable | Sexual Performance | `/erectile-dysfunction/ready` | `Low Strength:$14/dose` · `Medium Strength:$17/dose` · `High Strength:$20/dose` · `Max Strength:$24/dose` ("as low as about $10 per dose"; packs of 6) | published | sildenafil + tadalafil + apomorphine · sublingual troche, as-needed · compounded; **price shown only on the `/trimix` lander, not this PDP**. "Best Seller," product rating 4.3 (1,208). |
| Go Long | buyable | Sexual Performance | `/premature-ejaculation/go-long` | (no price on page — quiz-gated) | on-request | paroxetine + tadalafil · oral · compounded; 2-in-1 premature-ejaculation + ED. "Popular." |
| Daily Boost | buyable | Sexual Performance | `/erectile-dysfunction/boost` | (no price on page — quiz-gated) | on-request | tadalafil + DHEA · oral, daily · compounded; daily ED + testosterone support. |
| Grower | buyable | Sexual Performance | `/erectile-dysfunction/grower` | (no price on page — quiz-gated) | on-request | tadalafil + minoxidil · oral, daily · compounded; 2-in-1 ED + hair growth (the footer "Hair" line). |
| **Testosterone (TRT)** | family | — | `/testosterone` | — | — | Four forms at **one flat all-inclusive price**; labs required; live audio-video consult (controlled substances, except enclomiphene). |
| Enclomiphene | buyable | Testosterone | `/testosterone/enclomiphene` | `Plans start at just $139/month` (+ `$69` lab) | published | enclomiphene · oral, daily · compounded; needle-free, fertility-preserving; **not scheduled**; labs required. |
| Injectable TRT | buyable | Testosterone | `/testosterone/injectable-trt` | `Plans start as low as $139/month` (+ `$69` lab) | published | testosterone cypionate · injection, 1–2×/week · **FDA-approved controlled substance**; live video consult; labs required. |
| Topical TRT | buyable | Testosterone | `/testosterone/topical-trt` | `from $139/month` (+ `$69` lab) | published | testosterone · daily cream · **compounded controlled substance**; live video consult; labs required. |
| Oral TRT | buyable | Testosterone | `/testosterone/oral-trt` | `from $139/month` (+ `$69` lab) | published | testosterone · oral · **compounded controlled substance**; live video consult; labs required. |
| **Recharge** | buyable | Sleep | `/sleep/recharge` | (no price on page — quiz-gated) | on-request | ramelteon (+ 2 ingredients not named) · oral, nightly · compounded; "3-in-1" sleep Rx, "up to 17× stronger than melatonin." |
| **Weigh In** | buyable | Weight | `/weight-loss/weigh-in` | (no price on page — quiz-gated) | on-request | bupropion + naltrexone + metformin · oral, daily · compounded; **not a GLP-1** — a personalized oral metabolic stack. |

### Verbatim anchors

The footnotes the Price column points at, plus the molecule/form audit. Quoted exactly from the captured pages.

- **Ready price lives on the `/trimix` lander, not the PDP (the misattribution trap):** the `/erectile-dysfunction/ready` PDP shows **no price**; the only public numbers are on `/trimix` (a Rugiet Ready SEM lander) — *"Standard pricing for doses is: Low Strength:$14/dose … Medium Strength:$17/dose … High Strength:$20/dose … Max Strength:$24/dose,"* with *"doses starting as low as about $10 per dose. Each strength comes in a pack that contains 6 doses"* and *"Price shown with 3 month shipping option."* So Ready is **`published`** — but the price is cited to `/trimix`, not the PDP it describes.
- **TRT flat pricing (all four forms → `published`):** *"Plans start at just $139/month"* (`/testosterone` + `/testosterone/injectable-trt` FAQ; injectable phrases it *"Plans start as low as $139/month"*) and *"$69 gets you accurate testosterone testing and a video call with a licensed physician"* (`/testosterone/injectable-trt`). The line is sold as *"One flat price, every medication … No games, no tiered pricing schemes,"* with *"ongoing lab fees included in plan."*
- **Molecule sourcing (page-attested-only, audited):**
  - **Ready → sildenafil + tadalafil + apomorphine** (`/erectile-dysfunction/ready`: *"combines three proven medications (Sildenafil, Tadalafil and Apomorphine)"*; the `/trimix` lander repeats *"a combination of three ED medications - sildenafil, tadalafil, and apomorphine"*). *(Note: the Ready PDP's "Tadalafil" caption contains a stray phrase "as paroxetine moderates the arousal signal" — a copy-paste leak from Go Long; Ready's attested molecules are the three above, no paroxetine.)*
  - **Go Long → paroxetine + tadalafil** (`/premature-ejaculation/go-long`, which carries a *"What is paroxetine?"* section).
  - **Daily Boost → tadalafil + DHEA** (`/erectile-dysfunction/boost`; the /sex FAQ: *"Daily Boost provides consistent erection support plus DHEA to support testosterone production"*).
  - **Grower → tadalafil + minoxidil** (the /sex FAQ: *"Grower combines tadalafil with minoxidil for a 2-in-1 solution"*; `/erectile-dysfunction/grower` foregrounds minoxidil + tadalafil).
  - **Injectable TRT → testosterone cypionate** (`/testosterone/injectable-trt`: *"Testosterone cypionate that helps replace what your body's no longer producing"*). **Topical / Oral TRT → "testosterone"** only — the pages name the form (cream / oral) and the controlled-substance + compounded status but **don't specify the ester**, so recorded "testosterone," not inferred.
  - **Recharge → ramelteon** (`/sleep/recharge`: *"Recharge contains ramelteon… up to 17x the potency of melatonin"*); described as a 3-in-1 of "three ingredients" but **only ramelteon is named** → the other two are "not stated."
  - **Weigh In → bupropion + naltrexone + metformin** (`/weight-loss/weigh-in`: *"bupropion and naltrexone are used together to help reduce appetite and curb cravings, while metformin helps regulate blood sugar"*; Quick Facts: *"Bupropion, naltrexone, and metformin"*).
- **Compounded vs FDA-approved (the lane split):** every SKU except injectable TRT carries *"[Product] is a compounded drug product… Compounded drugs are not approved by FDA."* **Injectable TRT carries the controlled-substance disclaimer but NOT the compounded one** → it is the lone FDA-approved item (testosterone cypionate). Topical and Oral TRT carry **both** disclaimers (*"a compounded drug product, and controlled substance"*).

## Deep blocks

Two earned blocks: the flagship (whose price hides on a different URL than its PDP) and the TRT line (whose FDA-vs-compounded lane split and flat pricing a single roster row flattens).

### Ready™ — the flagship, and the price-on-a-different-URL trap (`/erectile-dysfunction/ready`)

- **Parent:** Sexual Performance · **price:** `$14–$24/dose` by strength (packs of 6) · **visibility:** `published` (via the `/trimix` lander) · **form:** sublingual troche

The PDP teaches the whole sexual-performance line's anatomy — **hero scroller → "Quick Facts" → "What is / How to take / How is it different / side effects" accordion → compounded disclaimer → results stats → "RD-37™" delivery explainer → "Three medications, one formula" (the molecule cards) → "Great sex starts in the brain" → reviews → cross-sell.**

> **H1:** "Ready™" · **tag:** "3-IN-1 BRAIN AND BODY PRESCRIPTION ED TREATMENT™" · **rating:** "Reviews (1,208) · 4.3"
> **Quick Facts (verbatim):** "3-in-1 ED treatment · Works in 15 minutes* · Effects last 36 hours* · Proprietary RD-37™ delivery system."
> **What is it (verbatim):** "A fast-acting ED treatment that combines three proven medications (Sildenafil, Tadalafil and Apomorphine) to help you get hard faster and stay hard longer."
> **The differentiator (verbatim):** "In addition to PDE5 inhibitors, Rugiet Ready includes apomorphine, an ED treatment that works directly on the brain to boost arousal signals."
> **Compounded disclaimer (verbatim):** "Ready™ is a compounded drug product and requires a prescription. Compounded drugs are not approved by FDA…"

**Why it earns a block:** the load-bearing pricing fact is **not on this page** — the PDP is `on-request`, and the per-dose numbers ($14/$17/$20/$24, packs of 6) live only on the `/trimix` paid-search lander. A cross-brand ED-price comparison that reads the PDP alone would record "no price"; the real, published number is one URL over. The molecules are page-attested (sildenafil + tadalafil + apomorphine); the stray "paroxetine" in a caption is a copy leak, not an ingredient.

### Testosterone (TRT) — one flat price, four forms, one FDA exception (`/testosterone`)

- **Parent:** — (family) · **price:** `from $139/month` + `$69` lab · **visibility:** `published` · **forms:** oral (enclomiphene), injection, cream, oral

The TRT line breaks Rugiet's price-gating pattern: it's the **one line with a public, flat, all-inclusive price**, and the **one place FDA-approved and compounded products sit side by side.**

> **Flat-pricing pitch (verbatim):** "One flat price, every medication … Every medication option at one flat price means you can focus on finding what works for your body, not what works for your budget. No games, no tiered pricing schemes."
> **The $69 gate (verbatim):** "$69 gets you accurate testosterone testing and a video call with a licensed physician to review your results together. No obligation to start treatment."
> **Lane split (verbatim):** Injectable TRT — *"a controlled substance … requires a live audio-video online consultation"* (testosterone cypionate, **FDA-approved**, no compounded disclaimer). Topical/Oral TRT — *"a compounded drug product, and controlled substance."* Enclomiphene — compounded, **not** scheduled, *"preserves fertility."*
> **Availability (verbatim):** "Enclomiphene: All states, excluding Louisiana. TRT: Not currently available in [15 states incl. Alabama, Georgia, Pennsylvania, North Carolina…]."

**Why it earns a block:** four roster rows share **one** price ($139/mo flat) and **one** lab gate ($69), but split three ways on regulatory lane — FDA-approved cypionate (injectable), compounded controlled substances (topical/oral), and a compounded non-scheduled alternative (enclomiphene). That structure is the cohort's whole "compounding posture / controlled-substance" question in one line, and a flat per-row price would hide that they're the same plan.

## Provenance

- **Sources reconciled (this run, all `captures/2026-06-07/`):**
  - **Backbone:** `/all-treatments` (`--homepage`, for card order + prominence) + the `/sex` and `/testosterone` category hubs — the three surfaces that enumerate every product card. Cross-checked against the Firecrawl `/map` (147 URLs, blog/author-dominated) and homepage links; the catalog set agrees across all three.
  - **PDPs (10):** ed-ready, pe-go-long, ed-daily-boost, ed-grower, trt-enclomiphene, trt-injectable, trt-topical, trt-oral, sleep-recharge, weight-weigh-in.
  - **Pricing sources:** `/trimix` (the Rugiet Ready SEM lander — sole source of Ready per-dose pricing); `/testosterone` + TRT PDP FAQs (the $69 + $139/mo TRT pricing). The `/go-long-lander`, `/daily-boost-lander`, `/recharge-lander` SEM pages were captured **specifically to chase per-product pricing and confirmed to carry none** — those SKUs are genuinely quiz-gated.
  - **Verify:** `fc.py verify` — all 20 sourceURLs match, all bodies md5-unique (no §5.1 geo/cache contamination).
- **Completeness verdict — HIGH confidence the roster is complete at the indexed level.** `/all-treatments` shows every product card; the per-category hubs and the map agree; 10 buyable SKUs across 4 lines. `enumeration: indexed-complete`. Sub-indexed detail intentionally not rostered: per-strength/dose tiers beyond Ready's four (TRT doses are clinician-set; not card-enumerated), and the quiz-gated configuration/quantity options on start.rugiet.com.
- **Couldn't reach / not enumerated:** all-in pricing for Go Long, Daily Boost, Grower, Recharge, Weigh In (quiz-gated — `on-request`); the pharmacy partner identity + 503A/503B lane; the two unnamed ingredients in Recharge's "3-in-1."
- **Credits:** part of the 21-credit `profile.md` run (shared capture; this module added no separate scrapes beyond the three pricing landers).
- **Point-in-time snapshot, not fixed:** Rugiet runs rotating promos (*"Try 2 months of Ready™, get 1 free,"* *"Claim 15% off Ready"*) and all pricing is behind the quiz — re-capture before trusting a price as current. This module's own `captured_at` + a short TTL are the guard.
- **Run profile:** Express invocation with the offerings module on. Captured the three `-lander` SEM pages specifically to hunt per-product pricing (it wasn't there); no hero-image / PDP-anatomy archetype requested.
