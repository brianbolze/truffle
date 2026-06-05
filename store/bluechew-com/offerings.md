---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: bluechew.com
captured_at: 2026-06-04
enumeration: indexed-complete    # all 8 distinct SKUs rostered at SKU grain; only leaf quantity/dose tiers sub-indexed (behind the /plans funnel) — no line omitted
site_notes: "One ED/sexual-health line; SKUs differ by FORM (chewable / sublingual / liquid shot) and molecule combo, not condition. Catalog is NOT in nav — PDPs at direct URLs (/sildenafil, /gold, /max, /energy, /daily-tad, /vardenafil-tadalafil-combo); /max and /sildenafil-tadalafil-combo are the SAME product (MAX). Each PDP shows a per-unit 'From $X/ea' floor; the FULL quantity-tier ladder is exposed only on /<product>/plan (captured /gold/plan: $79/$149/$215/$269). Molecule ladders sit behind the /plans;s=<code> funnel/app — floors only. Prices may run promo; re-check next run."
---

## Portfolio overview

A single category — men's ED / sexual performance — sold as a **flagship + companion roster** that differentiates on **delivery form and molecule combination**, not on treating different conditions. Every SKU is a compounded PDE5-inhibitor preparation; a buyer comparison-shops them as fast-vs-long-acting, single-vs-combo, chewable-vs-sublingual-vs-shot, as-needed-vs-daily.

Prominence (calibrated):
- **GOLD [HIGH]** — the company's own **"#1 Best Seller"** badge, a dedicated "The Gold Standard" homepage hero, and the only SKU with a `?product=gold` CTA. The current flagship push and the one proprietary-feeling formula (adds apomorphine + oxytocin for "brain + body").
- **SIL [MED]** — self-labeled "#1 Chewable in the USA" / "the original chewable with Sildenafil"; the legacy hero, now secondary to Gold.
- **MAX / VMAX / TAD / VAR / DailyTad / Energy [LOW–MED]** — companion forms/combos; surfaced via the quiz funnel and direct PDPs, not foregrounded on the homepage.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| GOLD | buyable | — | /gold | From: $7.30/ea · 6/12/18/24-pack: $79 / $149 / $215 / $269 /mo | published | Sildenafil + Tadalafil + Apomorphine + Oxytocin · sublingual, 4-in-1, 70/90/110 MG · monthly subscription; ready 15 min, lasts 24–36 hrs. Flagship "#1 Best Seller". |
| SIL | buyable | — | /sildenafil | From: $2.95/ea (plans "as low as $20/month") | partial | Sildenafil · chewable, up to 45 MG, berry flavor · subscription, as-needed; lasts 4–6 hrs. Full qty ladder behind /plans funnel. |
| TAD | buyable | — | /tadalafil | From: $3.58/ea | partial | Tadalafil · chewable · subscription, as-needed; longer-acting up to 24–36 hrs. Full qty ladder behind /plans funnel. |
| VAR | buyable | — | /vardenafil | From: $4.34/ea | partial | Vardenafil · chewable · subscription, as-needed; lasts 4–6 hrs. Full qty ladder behind /plans funnel. |
| MAX | buyable | — | /max | From: $5.63/ea | partial | 45 mg Sildenafil + 18 mg Tadalafil · sublingual, 2-in-1 · subscription; ready 15 min, lasts 24–36 hrs. Also served at /sildenafil-tadalafil-combo. Full qty ladder behind /plans funnel. |
| VMAX | buyable | — | /vardenafil-tadalafil-combo | From: $5.63/ea | partial | 14 mg Vardenafil + 18 mg Tadalafil · sublingual, 2-in-1 · subscription; ready 15 min, lasts 24–36 hrs. Full qty ladder behind /plans funnel. |
| DailyTad | buyable | — | /daily-tad | Starting at $100/EA | partial | Tadalafil (+ vitamins) · chewable · subscription, taken daily. "Plans starting as low as $100"; full ladder behind /plans funnel. |
| Energy | buyable | — | /energy | From: $4.50/ea | partial | 30 mg Sildenafil + 60 mg Caffeine · liquid shot, 2-in-1, 2 oz / 60 mL · subscription, as-needed; lasts 4–6 hrs. Full qty ladder behind /plans funnel. |

## Verbatim anchors

- **GOLD full ladder** (/gold/plan, the one SKU with the quantity ladder exposed) — Strength: **70 MG / 90 MG / 110 MG**. Quantity: *"6 Pack $79/mo"* · *"12 Pack SAVE 6% EA $149/mo"* · *"18 Pack SAVE 9% EA $215/mo"* (radio-checked, **"Most Popular"**) · *"24 Pack SAVE 15% EA $269/mo"*. *"Delivered every 30 days · Pause or Cancel Anytime."*
- **Entry floor** (/sildenafil FAQ) — *"BlueChew plans start as low as $20/month. The exact cost depends on which active ingredient you choose (SIL, TAD, or VAR), the dosage strength, and the number of tablets…"*
- **DailyTad** (/daily-tad) — *"Starting at $100/EA"*; *"With plans starting as low as $100, BlueChew can fit into anyone's budget. Plus, there's no commitment — easily cancel or switch plans anytime."*
- **Molecule sourcing (all page-attested, no `not stated`):** GOLD 4-in-1 "Sildenafil + Tadalafil + Apomorphine + Oxytocin" (/gold); MAX "45 mg of Sildenafil and 18 mg of Tadalafil" (/sildenafil-tadalafil-combo); VMAX "14 mg of Vardenafil and 18 mg of Tadalafil" (/vardenafil-tadalafil-combo); Energy "30 mg of sildenafil / 60 mg of caffeine" (/energy); SIL "up to 45 MG" Sildenafil (/sildenafil).

## Deep blocks

- **MAX vs VMAX — the combo naming, disambiguated** (a roster row can't carry the URL aliasing). BlueChew's two sublingual combos are both "X-MAX":
  - **MAX** = Sildenafil + Tadalafil (45 mg / 18 mg). It is served at **two URLs** — `/max` and `/sildenafil-tadalafil-combo` — both render the identical "# MAX" PDP. The `/max` page foregrounds the CTA and omits the inline price; the `/sildenafil-tadalafil-combo` page carries *"From: $5.63/ea"*. Same product, one canonical key (`/max`).
  - **VMAX** = Vardenafil + Tadalafil (14 mg / 18 mg), served at `/vardenafil-tadalafil-combo` (title "# VMAX"), also *"From: $5.63/ea"*.
  - Both are the long-acting (24–36 hr) sublingual 2-in-1 tier above the single-molecule chewables, priced identically; the only difference is the fast-acting molecule (sildenafil vs vardenafil).

  *No per-SKU deep-dive earned beyond this — the roster + verbatim anchors carry the rest. No PDP-template anatomy block (not requested).*

## Provenance

- **Pages read:** /gold, /gold/plan, /sildenafil, /tadalafil, /vardenafil, /daily-tad, /max, /sildenafil-tadalafil-combo, /vardenafil-tadalafil-combo, /energy (captures/2026-06-04/). Every `$` price above is greppable in a cited capture.
- **Scope note:** All **8 distinct SKUs** enumerated at SKU grain (GOLD, SIL, TAD, VAR, MAX, VMAX, DailyTad, Energy) — `enumeration: indexed-complete`. **Leaf** detail sub-indexed (lives in `## Provenance`, never sets `lines-omitted`): the full quantity × dosage monthly ladder for the 7 non-Gold SKUs sits behind the `/plans;s=<code>` funnel/app — only per-unit floors captured; Gold's ladder is the one exposed (/gold/plan). No product line omitted.
- **Point-in-time caveat:** pricing may run promo / vary by dosage strength and pack size chosen in the funnel; treat floors as a snapshot.
- **Run profile:** express — roster + telehealth + logos on. Vanilla roster columns; no hero-image capture, no PDP-anatomy block.
