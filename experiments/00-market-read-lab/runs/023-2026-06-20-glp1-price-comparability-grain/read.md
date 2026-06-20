# Market Read

## Question

In the store's GLP-1 / compounded-semaglutide cohort, is the captured pricing actually
comparable across brands, or do the pricing units and structures (per-month vs per-dose vs
first-month-promo vs membership-inclusive vs dose-escalating tiers) differ enough that any
cross-brand "cheapest" ranking is false confidence — and what minimum normalization (unit,
cadence, what's-included) would make a cross-brand price compare decision-grade?

## Direct Answer

**The captured prices are honest but not comparable. Across the 19 GLP-1 brands the store
captures a price for every one of them `[C1]`, yet the number denominates at least five
different things `[C2]` — so a naive "$135 Amble is cheapest, $349 Noom is priciest" ranking
is false confidence, and the store already knows it: the `visibility: published/partial` flag
on each row is the load-bearing tell `[C5]` — it separates a price you can act on from a
gated/incomplete one, and the med-only-plus-mandatory-fee unbundle is its most decision-relevant
sub-case (the flag's `partial` value also covers dose-floors and intra-surface conflicts, so it
is a comparability *gate*, not solely a "cost-on-top" marker). The fix is a query-time
normalization rubric, not a new persisted price field.**

The entry "price" splits into incommensurable kinds:

- **All-in, self-contained (`published`):** the displayed number is the whole monthly cost —
  telolife `$199/mo`, remedymeds `$299/mo`, home-medvi `$179` first mo, effecty `$160/mo`,
  goodlifemeds `$149–297`, joinamble `$135–179/mo`, tryshed `$249` (1-mo) `[C5]`.
- **Med-only, mandatory fee billed separately (`partial`):** the headline excludes a
  membership/program fee that is *required* to buy the drug — hims `$149/mo` med **+ $149/mo
  membership** ("not available without a membership"), eden `$99/mo` **+ $99/mo membership**,
  ro `$149` med **+ $39/74/149 Ro Body membership**, ivim `$75/mo` **+ $74.99 program fee**,
  joinfound program `$149–299` with **med billed separately**, noom `$349/mo` program with
  **med variable** `[C3]`. For these, the displayed number is *not* the price of the thing.
- **A floor that moves with dose / hidden behind intake (`partial`):** henrymeds "starts at
  $179/month", mydrhank "From $171/mo", ivyrx "From $175 (4 doses/mo)" — a binding all-in is
  set inside gated intake `[C2]`.
- **Cadence-disguised totals:** brello shows "$133 Per Month" but bills `$399 every 3 months`
  upfront; joinamble's `$135` needs a **12-month** commitment vs `$179` month-to-month;
  tryshed/fridays/found all cheapen the per-month only on annual prepay `[C2]`.
- **Promotional / point-in-time:** ~8 of 19 captured entry prices are a struck-through, code-
  gated, or "SUMMER sale" number (brello, directmeds, effecty, goodlifemeds, home-medvi,
  ivyrx, ivim, joinfridays) `[C4]` — so even within one kind, the number isn't steady-state.

Two brands even capture **conflicting numbers across their own surfaces** (directmeds
`$179.10` listing vs `$347` PDP; tryshed `$299` card vs `$249` PDP) — the store faithfully
holds both rather than papering over the conflict `[C2]`.

**Why a ranking lies:** Eden's `$99` looks like the cheapest in the cohort, but the mandatory
membership makes the *effective* all-in `$99 + $99 = ~$198/mo` **[derived, J]** — above
telolife's genuinely all-in `$199`-ish and roughly at hims' `$149 + $149 = ~$298` **[J]**.
Amble's `$135` is real but buys a 12-month lock-in; Noom's `$349` is program-only and excludes
the drug entirely. Sorting the verbatim numbers ascending inverts the real cost order. (These
effective figures are **reconstructions, not published prices** — computing and showing them
*is* the failure mode this run was told to avoid; they appear only to demonstrate why the
naive sort is wrong.)

**Minimum normalization to make a compare decision-grade — four axes, all already latent in
captured State:**

1. **What's included** — all-in vs med-only-plus-mandatory-fee. (Already encoded by
   `visibility: published` vs `partial` + the membership line in `site_notes`.)
2. **Billing cadence & commitment** — effective monthly cash outlay *and* the lock-in length
   it requires (month-to-month vs 3-mo-upfront vs 12-mo prepay).
3. **Steady-state vs promo** — strip first-month/code/countdown prices to the recurring rate.
4. **Binding price vs floor** — is the number the price, or a "from/starting at" that moves
   with dose inside intake?

A compare that holds those four axes constant is decision-grade; one that sorts the verbatim
strings is not.

## Evidence Used

All per-brand price rows, units, and flags are in
[`receipts/glp1-price-comparability-panel.md`](receipts/glp1-price-comparability-panel.md),
read verbatim from each `store/<domain>/offerings.md` (store-only; captures 2026-06-03 →
2026-06-18). Claim IDs:

- `[C1]` every one of the 19 GLP-1-anchored brands carries a captured entry price — **State**,
  S1 (store grep) + S2 (run 012 cohort).
- `[C2]` ≥5 incommensurable price denominations + cadence-disguise + intra-brand conflicts —
  **State**, S1 verbatim rows.
- `[C3]` ~6/19 exclude a mandatory membership/program fee billed separately — **State**, S1.
- `[C4]` ~8/19 entry prices are promotional/point-in-time — **State** (capture-date bound), S1.
- `[C5]` the existing `visibility: published/partial` field already gates actionable-vs-gated
  prices (`partial` spans both the fee-unbundle and dose-floor/conflict cases) — **State**, S1.
- Effective-monthly figures (eden ~$198, hims ~$298) — **Judgment/derived**, computed in-read
  from S1, explicitly *not* captured State.

No claim rests on a snippet; all rest on captured store files read verbatim.

## Companies Seen

19 GLP-1-anchored brands: brellohealth, directmeds, eden-health, effecty, goodlifemeds,
henrymeds, hims, home-medvi, ivimhealth, ivyrx, joinamble, joinfound, joinfridays, mydrhank,
noom, remedymeds, ro, telolife, tryshed.

## Missing / Stale Coverage

- **Entry-offer only.** Each brand's leading/lowest GLP-1 price; dose ladders and longer-plan
  tiers were not exploded into per-dose rows (intake-gated for ~half the cohort). A full
  per-dose price matrix is **not found** in captured State, not proven absent from the sites.
- **Capture spread.** 2026-06-03 → 2026-06-18; the 8 promotional prices are point-in-time and
  several brands flag "subject to change," so a comparison built on them is freshness-bound.
- **Intra-brand conflicts** (directmeds, tryshed) are captured but unresolved — which surface
  actually bills is **not found** in State.

## Source Gaps

No external source needed or used — this is a meta-audit of the store's own pricing State.
Resolving the intra-brand conflicts or the intake-gated floors would require live capture
(out of scope, would change evidence_mode).

## External Completeness Check

Not load-bearing. The finding is structural — *units differ within the captured cohort* — and
holds regardless of how many more GLP-1 brands exist. A larger denominator would add more
brands to each kind, not collapse the kinds into one comparable unit. No external denominator
panel run (consistent with MRL-001: external panels are a fallback, not the default).

## Market Pattern

Compounded-GLP-1 pricing has fragmented into **two pricing architectures wearing the same
"$X/mo" costume**: a genuinely all-in subscription (telolife, remedy, amble, effecty) and a
**med-plus-membership unbundle** (hims, eden, ro, ivim, found, noom) where the headline is a
loss-leader and the recurring fee is where the margin lives. The unbundled model lets a brand
advertise a low med price (eden `$99`, ivim `$75`) that is structurally below the all-in floor
of honest single-price brands — a pricing-optics arms race the verbatim number can't referee.
This is the same "$X/month illusion" run 012 flagged on continuity terms, now seen on the
*unit itself*.

## What Would Change This Answer

- A captured per-dose / per-plan price matrix (would let a normalized compare go deeper than
  the entry tier).
- Re-capture stripping the 8 promo prices to steady-state (would firm up axis 3).
- Live resolution of the directmeds / tryshed intra-brand conflicts.
- A decision that the store *should* persist a derived effective-monthly field — which this
  read argues **against**: it is point-in-time, judgment-laden, and would rot; the
  `published/partial` flag + verbatim string + a query-time rubric is the lighter, truer
  substrate. **No new durable primitive needed.**
