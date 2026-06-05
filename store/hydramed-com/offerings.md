---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: hydramed.com
captured_at: 2026-06-04
enumeration: indexed-complete   # both lines rostered at the index-surfaced grain; un-captured leaf PDPs (specialty IV drips, a few Rx SKUs) named in the scope note
site_notes: "IV catalog at /iv-therapy/* — the full menu sits behind a client-side 'Show All / Higher-Priced / Lower-Priced' filter, so the /iv-therapy index markdown surfaces 19 priced 'Most Popular' drips; ~13 more specialty drips are named in nav/map but unpriced in capture (re-run with the filter expanded, or /deepen-offerings, to price the tail). Rx prices ARE published on the /rx index (one-time vs monthly toggle) and repeated on each PDP. IV per-card 'What's Inside' dose tables live in the homepage + /iv-therapy markdown. Add-in pricing ($25/dose, $50 fluid bag, NAD+ by mg) is on the homepage. Pharmacy partners named on /faq."
---

## Portfolio overview

Two separately-merchandised lines under one brand:

- **Mobile IV therapy** (`/iv-therapy`) — ~30 nurse-administered, in-home drips, **$114–$494**, bought **per visit** (no membership, no travel fee). Pricing scales with dose count: base drips (Original Myers' $194, Hangover Rescue $199, NAD+ $199) → "Max" upgrades ($294–$494). A distinctive shape: **rescue drips bundle the Rx meds in at no extra charge** ("includes meds for headaches, nausea, and more—no extra charge, unlike competitors!"), and any drip is customizable via a **$25/dose add-in** menu of 17 vitamins/meds. Prominence `[HIGH]`: the homepage + index lead with a "Most Popular IVs" rail (Original Myers', Myers' Max, Hangover Rescue, HydraMed Max, Energy Boost Max, Cold & Flu Rescue, Immunity Boost) and an explicit "Higher-Priced / Lower-Priced" sort.
- **Longevity Rx** (`/rx`) — compounded telehealth meds shipped free, **prices published** ($145–$499), bought **one-time or as a monthly/annual subscription**. Prominence `[HIGH]` (own-label "Most Popular Treatments" grid): Testosterone, Semaglutide, Tirzepatide, Lipotropic B12, Sermorelin, PT-141, GHK-Cu, NAD+ (three forms), Tadalafil. The GLP-1s are **dose-laddered** (a published floor that climbs with strength → `partial`); TRT is gated to Colorado residents and requires $99 labs (→ `partial`).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Mobile IV Therapy | family | — | /iv-therapy | — | — | Nurse-administered in-home IV drips · 14 states · per-visit |
| Original Myers' Cocktail | buyable | /iv-therapy | /iv-therapy/original-myers-cocktail | $194 | published | IV fluids+electrolytes · vit C · B12 · B-complex · magnesium · zinc · calcium · in-home IV |
| Myers' Cocktail Max | buyable | /iv-therapy | /iv-therapy/myers-cocktail-max | $314 | published | Myers base at higher doses + glutathione ×2 · in-home IV |
| HydraMed Max | buyable | /iv-therapy | /iv-therapy/hydramed-max | $494 | published | "Most Premium" · vit C ×8 · glutathione ×5 · Mg · Ca · Zn · B12 · B-complex · taurine · L-carnitine · D3 · in-home IV |
| Energy Boost Max | buyable | /iv-therapy | /iv-therapy/energy-boost-max | $254 | published | vit C · B12 · taurine · MIC Lipo (IM) · L-carnitine · B-complex · in-home IV |
| Hangover Rescue | buyable | /iv-therapy | /iv-therapy/hangover-rescue | $199 | published | fluids · nausea med · headache/pain med · Mg · B-complex · vit C · glutathione (meds included) · in-home IV |
| Hangover Rescue Max | buyable | /iv-therapy | /iv-therapy/hangover-rescue-max | $294 | published | Hangover Rescue + 2nd fluid bag + higher Mg/B-doses · in-home IV |
| Immunity Boost | buyable | /iv-therapy | /iv-therapy/immunity-boost | $254 | published | vit C ×4 · glutathione · zinc · D3 (IM) · B-complex · in-home IV |
| Immunity Boost Max | buyable | /iv-therapy | /iv-therapy/immunity-boost-max | $399 | published | vit C ×8 · glutathione ×5 · zinc · D3 · Mg · B-complex · B12 · taurine · in-home IV |
| Cold & Flu Rescue | buyable | /iv-therapy | /iv-therapy/cold-flu-rescue | $284 | published | fluids · nausea med · headache/pain med · vit C · D3 · glutathione · zinc · Mg · B-complex · in-home IV |
| Cold & Flu Rescue Max | buyable | /iv-therapy | /iv-therapy/cold-flu-rescue-max | $399 | published | Cold & Flu Rescue at higher doses (vit C ×8, glutathione ×3) · in-home IV |
| Migraine Rescue | buyable | /iv-therapy | /iv-therapy/migraine | $194 | published | fluids · headache/pain med · migraine nausea med · Mg ×2 · Benadryl · in-home IV |
| Nausea Rescue | buyable | /iv-therapy | /iv-therapy/nausea-rescue | $194 | published | fluids · nausea med · Mg · vit C · B-complex · in-home IV |
| Food Poisoning | buyable | /iv-therapy | /iv-therapy/food-poisoning | $254 | published | fluids · nausea med · Pepcid · headache/pain med · vit C · glutathione · zinc · B-complex · B12 · in-home IV |
| NAD+ | buyable | /iv-therapy | /iv-therapy/nad | $199 | published | NAD+ (dose tiers ×1–×10) + IV fluids · "DNA Repair" · in-home IV |
| Expectant Mother | buyable | /iv-therapy | /iv-therapy/expectant-mother | $194 | published | fluids · vit C · B-complex · zinc · nausea med* · in-home IV |
| IV Fluids Only | buyable | /iv-therapy | /iv-therapy/iv-fluids-only | $114 | published | IV fluids with electrolytes · in-home IV |
| You Pick 2 Add-Ins | buyable | /iv-therapy | /iv-therapy/you-pick-2 | $149 | published | IV fluids + 2 chosen add-ins (of 17) · in-home IV |
| You Pick 3 Add-Ins | buyable | /iv-therapy | /iv-therapy/you-pick-3 | $169 | published | IV fluids + 3 chosen add-ins · in-home IV |
| You Pick 4 Add-Ins | buyable | /iv-therapy | /iv-therapy/you-pick-4 | $189 | published | IV fluids + 4 chosen add-ins · in-home IV |
| IV Add-Ins | family | /iv-therapy | /iv-therapy (add-ins) | $25/dose; +$50 bag; NAD+ $100–$750 | published | Booster dose $25 (17 vitamin/med options) · extra fluid bag $50 · NAD+ by mg ($100/250/450/700/750) · IM injection $25 |
| Longevity Rx | family | — | /rx | — | — | Compounded telehealth meds · prescribed online · shipped free · one-time or subscription |
| Semaglutide | buyable | /rx | /rx/semaglutide | $249 (one-time) · $199/mo | partial | semaglutide (compounded) · GLP-1 receptor agonist · subcut. injection · intake→provider review; dose-laddered (see anchors) |
| Tirzepatide | buyable | /rx | /rx/tirzepatide | $349 (one-time) · $299/mo | partial | tirzepatide (compounded) · GLP-1/GIP · injection · intake→provider review; dose-laddered like semaglutide (PDP not captured) |
| Testosterone (TRT) | buyable | /rx | /rx/testosterone | $175/mo · $150/mo annual | partial | testosterone cypionate in MCT oil (compounded) · IM injection · Colorado-only; +$99 labs required (see anchors) |
| Sermorelin Injections | buyable | /rx | /rx/semorelin/injections | $249 (one-time) · $199/mo | published | sermorelin (compounded) · growth-hormone-releasing peptide · injection · intake→provider review |
| PT-141 Peptide | buyable | /rx | /rx/pt141/injections | $299 (one-time) | published | PT-141 / bremelanotide (compounded) · peptide · injection · sexual health |
| PT-141 Troche | buyable | /rx | /rx/pt141/troche | $220 (one-time) | published | PT-141 / bremelanotide (compounded) · sublingual troche · sexual health |
| Tadalafil Troche | buyable | /rx | /rx/tadalafil/troche | $180 (one-time) | published | tadalafil (compounded) · troche · sexual health |
| NAD+ Injections | buyable | /rx | /rx/nad/injections | $369 (one-time) · $299/mo | published | NAD+ (compounded) · injection · longevity |
| NAD+ Nasal Spray | buyable | /rx | /rx/nad/nasal-spray | $190 (one-time) · $175/mo | published | NAD+ (compounded) · nasal spray · longevity |
| NAD+ 20% Topical Cream | buyable | /rx | /rx/nad/topical-cream-20-percent | $195 (one-time) · $175/mo | published | NAD+ 20% (compounded) · topical cream · skin/longevity |
| GHK-Cu Topical Cream | buyable | /rx | /rx/ghk-cu/topical-cream | $199 (one-time) | published | GHK-Cu copper peptide (compounded) · topical cream · skin |
| Lipotropic B12 Injections | buyable | /rx | /rx/lipotropic-injections | $145 (one-time) · $125/mo | published | lipotropic (MIC) + B12 (compounded) · injection · energy/metabolism |

## Verbatim anchors

- **Semaglutide dose ladder** (/rx/semaglutide, "Semaglutide Monthly Online Prescriptions"): "**1mg Total** – Strength: 1mg/mL (1mL Vial) – **$199**. · **2.5mg Total** – 1mg/mL (2.5mL Vial) – **$299.00** · **5mg Total** – 5mg/mL (1mL Vial) – **$399.00** · **12.5mg Total** – 5mg/mL (2.5mL Vial) – **$499.00**." Headline "$199/Monthly" is the entry-dose floor → `partial`. Mechanism page-attested: "Compounded Semaglutide injections are a distinguished member of the glucagon-like peptide-1 (GLP-1) receptor agonist class."
- **Testosterone** (/rx/testosterone): "**$175/Monthly**, **$150/Annually**"; "Only available to Colorado Residents at this time"; "Lab work is crucial; acquire it through us for a mere **$99**, or you're welcome to provide your own." Formulation: "Testosterone Cypionate in MCT Oil… administered via intramuscular injection." → `partial` (mandatory $99 labs on top of the med).
- **IV add-ins** (homepage): "Booster IV Add-ins—**$25** each… 17 in total"; "Extra bag of IV fluids—**$50**"; "NAD+ starting at **$100**… 100mg - $100 · 250mg - $250 · 500mg - $450 · 750mg - $700 · 1000mg - $750."
- **Tirzepatide** (/rx/tirzepatide on the /rx index): "Tirzepatide Injections **$349/One Time**, **$299/Monthly**." Disclaimer (/faq): "Compounded versions of tirzepatide are not associated with Eli Lilly… not FDA-approved."
- **Molecule sourcing audit:** semaglutide + testosterone molecules are PDP-attested (quoted above). Tirzepatide, sermorelin, PT-141, NAD+, GHK-Cu, tadalafil, lipotropic/B12 molecules are taken from the **product names on the captured `/rx` index** (e.g. "Tirzepatide Injections", "Sermorelin Injections", "GHK-Cu Topical Cream") — page-named, not inferred from the brand. "Compounded" is attested for the Rx line by `/compounded-medication-policy` + `/faq` (503A), not asserted per individual PDP for the un-captured ones.

## Deep blocks

- **The IV pricing architecture (a portfolio-level shape).** HydraMed's IV line isn't a flat menu — it's a **base → "Max" ladder + à-la-carte add-in** system. Each named drip has a base price; a "Max" variant roughly +50–100% adds dose multiples and glutathione; and any drip can be tuned with **$25/dose** add-ins (17 options incl. meds like Benadryl/Pepcid) or an **extra $50 fluid bag**. The "rescue" drips (Hangover, Cold & Flu, Food Poisoning, Migraine, Nausea) explicitly **bundle prescription meds at no extra charge** — "includes meds… no extra charge, unlike competitors!" — a deliberate price-transparency wedge vs. IV bars that upcharge for anti-nausea/anti-inflammatory shots. Reading one rescue drip's "What's Inside" table teaches the whole IV catalog's structure.
- **None earned per-SKU** — the roster + Verbatim anchors carry the per-product detail; no single SKU has an ambiguity a row can't hold.

## Provenance

- **Pages read:** homepage (rich), `/iv-therapy` (rich index), `/rx` (rich index), `/rx/semaglutide`, `/rx/testosterone`, `/compounded-medication-policy`, `/faq` — all 2026-06-04 captures under `captures/2026-06-04/`.
- **Scope note (leaf omissions, not lines):** both lines (IV + Rx) are rostered at the index-surfaced grain → `indexed-complete`. Not individually priced this run (leaf detail, behind a client-side filter or an un-captured PDP): **IV** — beauty-glow, athletic-recovery, altitude-sickness, autoimmune-support, her-monthly, high-dose-vitamin-c, stress-relief, weight-loss, just-feel-better, custom-iv, energy-boost (non-Max), covid-rescue/-max, you-pick-1 (~13 drips); **Rx** — trimix injection (/rx/trimix-injection), scream cream (/rx/scream-cream), VIP nasal spray (/rx/vip), bioidentical HRT incl. women's (/rx/bioidentical-hormone-replacement-therapy), Rx skincare (/rx/skincare), and the longevity-performance / lean-muscle-mass bundles. To price the tail: re-run with the IV filter expanded or use `/deepen-offerings hydramed`.
- **Point-in-time caveat:** prices and TRT's Colorado-only gating are a 2026-06-04 snapshot; the Rx line runs promos and per-state availability shifts.
- **Run profile:** Express telehealth invocation — `offerings.md` + `telehealth.md` + `logos` all enabled alongside the standard `profile.md`. Vanilla roster columns (no project-local additions).
