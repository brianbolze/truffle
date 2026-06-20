# Market Read

## Question

Which GLP-1 telehealth brands do third-party "best of 2026" listicles and SERPs repeatedly name as the
*default / best*, and how does that third-party named set compare to Truffle's captured GLP-1 universe
(the ~19 `anchor_category: GLP-1` brands)? Does the comparison reveal store coverage gaps, store
over-coverage, or a mismatch between market-default perception and the captured set?

## Direct Answer

**The store and the market's "default" set agree on the head and diverge on the tails — and the one
clean lesson is that a third-party listicle panel is a useful *coverage radar*, not a denominator.**

Two high-authority listicles (U.S. News, 23 providers, updated 2026-06-12; Forbes Health, 6 affordable
picks, audited 2026-06-10) overlap with the store on **~10 mid-market compounded-GLP-1 brands** — Ro,
Hims/Hers, Remedy Meds, Found, Eden, Ivim, MEDVi, Noom, Fridays, Henry Meds `[C1]`. Past that head, the
two sets pull apart in **opposite** directions:

- **The store is missing the big-brand / insurance-concierge tier.** ~11 listicle-named brands (excluding
  the GoodRx aggregator) are absent from the store; **Mochi is the single unambiguous gap — the only
  store-absent brand named by *both* authoritative listicles, captured nowhere** `[C2]`. Every other
  absentee (PlushCare, WeightWatchers, SkinnyRX, Amazon On-Demand Care, BetterMe Rx, Bodybuilding Health+,
  MyStart Health, Sprout Health, Sunlight, TrimRx) is named by only *one* authoritative listicle — a
  weaker, single-source nominee. The store's blind spot is the well-funded consumer-brand / insurance lane
  (Mochi, PlushCare, WeightWatchers, LifeMD-as-GLP-1) `[C3, J]`.
- **The store over-covers the long-tail compounding segment.** 9 store-anchored GLP-1 brands
  (brellohealth, directmeds, effecty, goodlifemeds, ivyrx, joinamble, mydrhank, telolife, tryshed) appear
  on *neither* authoritative listicle — the store holds more of the small compounding tail than the
  "market default" surface ranks `[C4]`.
- **The named set is affiliate-confounded: head-stable, tail-divergent.** The two authoritative sources
  agree on the head; two *low*-authority affiliate pages (HealingMaps, VaccineAlliance) name a completely
  disjoint tail (SkinnyRx, Embody, ShedRx, GobyMeds) that appears on neither `[C5]`. Listicle inclusion
  and order are partner/SEO artifacts, not an objective ranking `[J]`.

**Net for Truffle:** the store's *affordable/compounding* coverage is strong (5 of Forbes' 6 affordable
picks are already captured); its gap is the *brand-name/insurance* tier. The actionable output is a short
capture-candidate list led by **Mochi**, not a claim that either set is "complete."

## Evidence Used

All claims sourced in [`receipts/third-party-leaderboard-panel.md`](receipts/third-party-leaderboard-panel.md);
the `live_evidence_used` log in `run-notes.md` lines up with S1–S5 there.

- `[C1]` overlap-of-10 — U.S. News (S1) + Forbes (S2) named sets ∩ store anchored grep (S6). **State + secondary.**
- `[C2]` 11 absent (excl. GoodRx aggregator); only Mochi on both listicles, rest single-source — S1 ∪ S2 minus store universe (S6, S7). **Secondary; partial panel.**
- `[C3]` store blind spot = big-brand/insurance tier — S2 (affordable winners 5/6 captured) + S7 (LifeMD multi/none). **Judgment over State.**
- `[C4]` store over-covers compounding tail (8 anchored, listicle-unnamed) — S1/S2 vs S6. **State.**
- `[C5]` head-stable / tail-divergent — S1, S2 vs snippet-only S3, S4. **Secondary; S3/S4 direction-finding.**

No claim rests on a snippet alone: the two membership conclusions (C1–C4) rest on the two fully-scraped
authoritative listicles + the store grep; snippet-only S3/S4 support only the tail-divergence framing (C5).

## Companies Seen

- **Store-anchored GLP-1 (19, S6):** brellohealth, directmeds, eden-health, effecty, goodlifemeds,
  henrymeds, hims, home-medvi, ivimhealth, ivyrx, joinamble, joinfound, joinfridays, mydrhank, noom,
  remedymeds, ro, telolife, tryshed.
- **Named by an authoritative listicle AND store-anchored (10):** Ro, Hims/Hers, Remedy Meds, Found,
  Eden, Ivim, MEDVi, Noom, Fridays, Henry Meds.
- **Named by an authoritative listicle, NOT in store (11; only Mochi on both):** Mochi (×2 listicles —
  the one strong gap), PlushCare, WeightWatchers, SkinnyRX, Amazon On-Demand Care, BetterMe Rx,
  Bodybuilding Health+, MyStart Health, Sprout Health, Sunlight, TrimRx (each ×1 listicle). (GoodRx =
  aggregator, excluded.)
- **Store-captured but not GLP-1-queryable (2):** LifeMD (`multi/none`), altRx (no `telehealth.md`, MRL-003).

## Missing / Stale Coverage

- **Capture candidates (concrete, propose-don't-write):** **Mochi** is the one strong candidate — named by
  *both* authoritative listicles and absent. The rest (PlushCare, WeightWatchers, SkinnyRX, …) are
  single-listicle nominees: weaker signal, worth a capture only if a second authoritative source names them.
  LifeMD's GLP-1 line is a separate case (captured but multi/none-anchored). These mark the store's
  brand-name/insurance-tier blind spot.
- **In-cohort depth gap (existing MRL-003):** altRx is GLP-1-led but lacks `telehealth.md`/`offerings.md`,
  so it silently drops out of every cohort grep — it is in the store yet invisible to this exact read.
- Store captures span 2026-05-30…06-18; not stale for this structural read.

## Source Gaps

- **No store field captures "third-party default standing."** Whether a brand is named on the major
  listicles is a real market signal (traffic, trust, ad budget) with no per-domain home — it would be a
  *Signal*, not State. One sighting; not a primitive proposal.
- **Listicles are affiliate-confounded** and cannot be used as a clean denominator — only as a radar that
  nominates capture candidates and confirms head coverage.

## External Completeness Check

This run *is* the external completeness check for the GLP-1 cohort: the third-party panel was the outside
denominator held against the store-derived set. Result — the store is **not** a superset of market-default
(misses Mochi/PlushCare/WeightWatchers) and **not** a subset either (holds 9 listicle-unranked compounding
brands). The two surfaces measure different things: listicles rank consumer-brand prominence; the store
captures a deeper compounding long-tail. Neither is "the" denominator; reconciling them is the MRL-001 job.

## Market Pattern

- **"Default" in GLP-1 telehealth is two markets.** A consumer-brand head (Ro, Hims/Hers, Mochi,
  WeightWatchers, Noom) that listicles rank, and a compounding long-tail (directmeds, effecty, telolife,
  ivyrx, …) that the store captures but listicles ignore. A strategist asking "who's the default?" gets a
  different answer depending on which surface they trust.
- **The head is stable; the tail is bought.** Authoritative sources converge on ~5 head brands; affiliate
  pages invent disjoint tails. Cross-source *recurrence* is the only trustworthy ranking signal here.
- **Mochi is the conspicuous market player the store hasn't captured** — the clearest single action.

## What Would Change This Answer

- A wider authoritative panel (3rd/4th high-authority listicle) that repeatedly names a store-absent brand
  would promote that brand alongside Mochi as a capture priority.
- Capturing Mochi + LifeMD's GLP-1 line would close most of the named head-gap and let a future run test
  whether the store then *is* a superset of market-default.
- If a future run found the same store-absent brands named across *many* surfaces (ads, Reddit, SERP), the
  "third-party default standing" signal would cross from one-sighting curiosity toward a real coverage Signal.
