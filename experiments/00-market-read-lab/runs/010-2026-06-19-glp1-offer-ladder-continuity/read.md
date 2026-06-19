# Market Read

## Question

Across the store's GLP-1 cohort, what is the entry offer, what gets bundled, and which commitment/continuity terms (upfront multi-month charge, auto-renew cadence, membership floor, buy-first vs intake-gated) are becoming table stakes — and where is there still real differentiation?

## Direct Answer

For compounded GLP-1, **the entry offer is a subscription, not a purchase.** Across 19 GLP-1-anchored store brands `[C1]`, the near-universal shape is an **all-in recurring plan that bundles the clinician consult + medication + supplies + shipping into one price** `[C2]`. On top of that shared base, three continuity mechanics have become table stakes — and one of them is essentially a category-wide pricing illusion:

1. **The "$X/month" headline almost never equals what you actually pay** `[C4, J]`, for three distinct reasons that recur across the cohort:
   - it's a **multi-month total charged upfront, divided by N** (brello's "$X/Month" = 3-mo total ÷ 3, charged upfront auto-renewing every 10 weeks; ivyrx's "$199/mo" assumes a 12-month prepay; telolife's bundles *prepay* the same $199/mo rate);
   - it's **medication-only, with a mandatory separate membership stacked on top** (eden $39→$99/mo, hims weight-loss $39→$149/mo, ivim $74.99/mo program fee, ro Ro Body $39/$74/$149, medvi branded "$99 Membership + Medication Cost", shed Foundayo/Zepbound +$125/mo);
   - it's a **"starting at" dose floor** whose real number is set inside a gated intake (henry, mydrhank, joinfound, goodlife sexual-health/hair, ro's behind-expander ladders).

2. **Commitment laddering — longer prepay buys a lower per-month — is near-universal** `[C5]` (effecty 1/3/12-mo, tryshed 1/6/12-mo, amble's "12-mo cheapest → 1-mo dearest" table, ivyrx 12-mo, brello 3-mo, telolife/joinfound bundles). The differentiation hidden inside it: **whether the longer plan actually discounts or just prepays the same rate** — telolife's bundles divide to exactly the month-to-month $199/mo; the "savings" are a card/wallet discount and Cherry financing framing, not a lower plan rate.

3. **The membership wedge cleanly splits the cohort into two business models** `[C3, J]`: brands that **fold everything into one all-in price** (henry, mydrhank, fridays, effecty, directmeds, telolife, brello, remedy, goodlife-WL — many explicitly market "no membership / no hidden fees") vs. brands that **price the med separately and require a standalone membership** to access it (eden, hims-weight-loss, ro, ivim, medvi-branded, shed-Foundayo, found-brand-lane). This is the offer-structure analogue of runs 008/009's finding that **posture tracks business model, not molecule** — the same split shows up here in *how the offer is packaged*, not just whether the price is shown.

**Where there's still real differentiation / whitespace** `[C6, J]`: genuinely **published, no-intake-wall, all-in pricing is rare** — telolife and effecty show the full all-in without a quiz wall (telolife's `site_notes` calls this "unusual for compounded-GLP-1 telehealth"). **Buy-first** (brello: pay before intake) is a near-unique model. And **cross-line bundles that stack adjacent longevity SKUs** (brello's GLP-1 + NAD+ + sermorelin "Longevity Stack") are a differentiated upsell against single-line plays (telolife, remedy).

## Evidence Used

Store-only; no external/current claims. Receipt: [`receipts/glp1-offer-structure-panel.md`](receipts/glp1-offer-structure-panel.md) — the per-brand classification table and full source list (S1–S12). All offer-structure attributes were read **verbatim from captured `site_notes` / Portfolio / Visibility-rule fields**, not re-derived from marketing prose (009's field-fidelity lesson). Membership figures quoted as captured:

- **Eden** (S3): *"$39 for the first month, auto-renews at $99/month thereafter… Medication is not available without a membership."* (2026-06-03)
- **Hims** (S4): weight-loss **"Weight Loss Membership ($39 first month → $149/mo)"**, *"Medication is not available without a membership"* — the only `partial` line; other lines bundle the consult (2026-06-18).
- **Ro** (S5): **Ro Body membership $39/$74/$149** wrapping a separately-billed GLP-1 med roster (2026-06-18).
- **Ivim** (S6): med floor **+ separate $74.99/mo program fee + "membership required thereafter"** (2026-06-04).
- **Telolife** (S10): bundle totals divide to exactly **$199/mo** (3-mo $597 … 12-mo $2,388); *"DISCOUNTS PROVIDED AUTOMATICALLY WHEN UTILIZING CARD/WALLET"*; published, no quiz wall (2026-06-18).
- **Brello** (S2): *"No Intake Form Required Before You Pay"*; "$X/Month" = 3-mo plan ÷ 3, charged upfront, auto-renew "every 10 weeks" (2026-06-04).

## Companies Seen

**Core cohort (19, `anchor_category: GLP-1` + `offerings.md`):** brellohealth, directmeds, effecty, eden-health, goodlifemeds, hims, home-medvi, ivyrx, joinfridays, ivimhealth, henrymeds, joinfound, mydrhank, joinamble, ro, telolife, noom, tryshed, remedymeds.

**Business-model split (C3, Judgment):**
- *Med-included, single all-in price (≈9):* henrymeds, mydrhank, joinfridays, effecty, directmeds, telolife, brello, remedymeds, goodlifemeds (weight-loss line).
- *Med-priced + mandatory separate membership (≈7):* eden, hims (weight-loss only), ro, ivim, home-medvi (branded), tryshed (Foundayo/Zepbound), joinfound (brand/program lane).
- *Program-subscription, med inside (own flavor):* noom (3 program tiers; per-drug on-request).

## Missing / Stale Coverage

- **Promo/A-B-volatile prices** — flagged in nearly every `site_notes` (brello Deadline Funnel countdown, ro's own ro-experiments engine, hims struck-through heroes, goodlife SUMMER30, medvi countdown). Every figure is a **captured floor ≤ ~3 weeks old (2026-05-30…06-18)**, not a live quote.
- **Intake-gated dose ladders** — henry, mydrhank, joinfound, ro, noom show only a floor; the true per-dose all-in is set behind a quiz and is not captured.
- **Unenumerated lines** — tryshed women's-hair/longevity PDPs and several branded GLP-1 dose ladders (ro behind an unrendered expander) were not individually scraped.

## Source Gaps

- **No "what % churn / how punitive is the auto-renew" data** — the store captures the *cadence* (auto-renew every 10 weeks, month-to-month, 12-mo prepay) but not cancellation friction or refund terms beyond what a PDP states. A true continuity-lock-in read would want the cancellation/refund policy as a captured field — not present as structured State.
- **No cross-brand price-normalization** — comparing "$199/mo" across brands is unsafe because the denominators differ (med-only vs all-in vs upfront-total÷N). This is a *consumer-confusion* finding, but it also means the store can't answer "who is actually cheapest all-in" without per-brand manual normalization.

## External Completeness Check

Not run — completeness is **not** load-bearing for this read. The findings (offer-structure patterns, the "$X/month" illusion, the membership-wedge split) are **structural and hold within the captured cohort regardless of how many more GLP-1 brands exist**; they are not share/ranking claims that a fuller denominator would move. The partial-denominator caveat is stated plainly rather than papered over with a SERP panel (consistent with MRL-001's "external panels are a fallback, not the default denominator").

## Market Pattern

The compounded-GLP-1 cohort has converged on a **subscription-with-medication-inside** offer, and the competitive action has moved *off the sticker price and onto the offer structure*:

- **The sticker price is theater.** Three different mechanisms (upfront-÷-N, stacked membership, dose-floor) make the headline "$X/month" systematically lower than the real all-in. A buyer comparing two "$199/mo" brands is very likely comparing a med-only-plus-$99-membership number against an all-in-charged-upfront number. This is the single most decision-relevant, store-evidenced pattern.
- **The membership wedge is the business-model tell.** Whether a brand stacks a separate membership is a cleaner signal of "high-touch clinic vs. cash-pharmacy" than the molecule it sells — the offer-structure echo of 008's "price-posture tracks business model, not molecule." Several brands (henry, hank, fridays, medvi) actively *market against* the wedge ("no membership, no hidden fees") — making "no membership" itself a positioning claim.
- **Commitment is the real lock-in, not the membership.** The durable continuity mechanic is the **prepaid multi-month plan** (3/6/12-month, charged upfront), which front-loads revenue and raises switching cost more than a month-to-month membership does. The differentiation lever inside it — discount-vs-prepay — is invisible at the headline and only shows when you divide the bundle total (telolife's bundles don't discount; they prepay).
- **Whitespace:** fully transparent, no-wall, all-in pricing sits on a **small-n pole — only telolife and effecty** clearly deliver it (and telolife's "no wall" publishes a *prepay-flat* rate that looks discounted but isn't). On that thin evidence it reads as a differentiator rather than table stakes; a new entrant's cleanest attack would be "the real all-in, shown before you sign up, no membership" — but the ~2-of-19 base is too small to call it a proven gap rather than a captured-cohort artifact.

All four bullets are **Judgments `[J]`** built on the captured State in the receipt; none requires a current/news/policy claim.

## What Would Change This Answer

- A **live price re-capture** — prices are promo/A-B-volatile; the *structure* findings are durable but specific figures rot fast.
- **Scoring the generalist GLP-1 lines** (GLP-1 inside `multi/none` brands) — would test whether the membership-wedge split holds outside GLP-1-anchored brands or is an artifact of the anchor cut.
- A **captured cancellation/refund-terms field** — would turn the "commitment is the real lock-in" Judgment from a cadence inference into an evidenced claim.
- If a future entrant **published all-in, no-wall pricing at scale**, the C6 whitespace finding would flip from differentiation to table stakes.
