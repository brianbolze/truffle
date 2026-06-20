# Market Read

## Question

Across the 34 captured telehealth brands that have a `visual.md` visual-evidence layer,
how does brand/design *presentation* cluster, and does presentation posture track
positioning (`anchor_category`) or price-transparency? Surface **cited cross-brand
presentation patterns — not a quality score or ranking** (the visual layer parks scoring
by contract; `modules/VISUAL.md`).

This is also a system-test: **the first lab read to consume `visual.md` as a
cross-company ingredient.** Every prior run used `telehealth.md` / `offerings.md` /
`profile.md` / signals. So the design payload is: *does a Judgment-dense per-company layer
aggregate into a trustworthy cross-brand read, and at what grain?*

## Direct Answer

**Three findings, in confidence order.**

1. **The category shares one visual signature: a controlled, owned core that frays at the
   borrowed edges.** Across ~32 of 34 brands the impression follows the *same arc* —
   disciplined where the brand **owns** the asset (palette tokens, type system, product
   renders, custom data-viz, repeatable components/grids) and weakest where it **borrows**
   (stock photography, off-the-shelf icons, manufacturer/UGC imagery) or drops into
   **utility pages** (footers, legal, reviews/quiz). This is near-verbatim across
   independent per-company captures: gethealthspan "strongest on what it owns, shakiest on
   what it borrows" [gethealthspan color_03↔color_07]; eden "imagery breaks art direction
   wherever it isn't owned" [eden iconography_02↔color_06]; joiandblokes "owned art over
   stock" [joiandblokes color_01↔iconography_03]; agelessrx, hone, hims, functionhealth,
   marek, gogeviti, rugiet, truniagen all repeat it. **The competitive read: component
   systems are table stakes; owned imagery/illustration is the only real visual moat; the
   borrowed-asset layer is where the *entire category* is weak** (148 `poor` cards, ~15%
   of all cards, concentrate in the `color` imagery and `iconography` families).

2. **Presentation splits into three characters** (a cited clustering, *not* a ranking):
   - **Editorial-premium** — serif/roman-italic display systems, art-directed photography,
     1–2 token restraint: hims, honehealth, functionhealth, gethealthspan, gogeviti, ro,
     remedymeds, niagenplus, rugiet, maximustribe, marekhealth (flagship), goodlifemeds,
     joinamble, truniagen, telolife, agelessrx.
   - **Functional-catalog** — componentized, scan-first, "template discipline more than
     distinct identity": directmeds, getpetermd, sermorelin, trtnation, struthealth, ivyrx,
     mydrhank, lifemd, henrymeds, nurx, onemedical, eden, effecty, joinfridays, tryshed.
   - **Budget/dated** — one clear outlier: kingsbergmedical, "an older medical SEO site …
     type hierarchy and nav feel dated" [kingsberg layout_01][typography_01].
   - **Emerging premium type signature:** a roman-lead + **italic-serif** headline device
     recurs as a deliberate brand motif across honehealth, gogeviti, joinamble,
     remedymeds, maximustribe, telolife, mydrhank, and functionhealth's rust-italic
     emphasis word — an identifiable category convention, not an accident.

3. **Soft correlation with positioning; none claimable with price-transparency.**
   Editorial-premium skews to **longevity/NAD** (gethealthspan, gogeviti, agelessrx,
   honehealth, truniagen, niagenplus), premium-**TRT** (maximus, marek), and **well-funded
   incumbents** (hims, ro, remedymeds). Functional-catalog skews to **commodity-GLP-1
   compounders** (directmeds, goodlifemeds, telolife, ivyrx, mydrhank, henrymeds) and
   **legacy men's-health** (kingsberg, trtnation, sermorelin). *Soft and confounded* —
   eden/remedymeds are polished GLP-1 brands; it is a supply-side impression cut, not a
   measured relationship (**J1**). **Price-transparency: declined on scope grounds.** The
   `offerings.md` `visibility` value (a structured `| Visibility |` table column with
   `published` / `partial` / `on-request` values) is in fact parseable for all 34 brands —
   so this is *not* a "can't extract" decline (an earlier quick `visibility:` prose-grep
   under-counted to n=0 for 21/34 by matching the wrong form; **the data was always
   readable** — Loop 2 evidence-verifier catch). The cut is declined because a
   **price-transparency-vs-visual-character correlation is not a well-formed metric**:
   collapsing a brand's per-SKU visibility *mix* into one "transparency" scalar and
   correlating it with an interpreted visual-character label would manufacture a
   relationship, not measure one. **Not assessed ≠ no relationship.**

**System-test payload (the design point):** `visual.md` **does** aggregate into a
trustworthy cross-brand read — **but only at the prose/impression grain, not the
structured-`polarity` grain.** See *Market Pattern*. No durable "visual-cluster" object or
score rollup is needed (`query-time-grouping-enough`).

## Evidence Used

All evidence is local store State — no external/current/pricing claims, no snippets, no
spend. The `visual.md` layer is itself **Judgment-dense** (cited "visible tells" + a
synthesized impression); my cross-brand clustering is a **Judgment-on-Judgments** and is
labeled as such. Claim IDs map to the receipt.

- **C1** — 34 telehealth domains have both `visual.md` and `telehealth.md` (the panel).
- **C2** — per-brand polarity tally (strong/mixed/poor) and card-total spread (9–51).
- **C3** — the per-brand impression paragraphs (the owned-vs-borrowed pattern, the three
  characters, the italic-serif signature).
- **C4** — `anchor_category` per brand (positioning cross-tab).
- **C5** — `offerings.md` `visibility` is a parseable `| Visibility |` table column for all
  34 brands; price-transparency cut declined on **scope** grounds (not extractability).

Receipt: `receipts/visual-layer-cross-brand-sweep-2026-06-20.md` (S1–S4).

## Companies Seen

34 brands with `visual.md` **and** `telehealth.md`: agelessrx, bluechew, directmeds, eden,
effecty, functionhealth, gethealthspan, getpetermd, gogeviti, goodlifemeds, henrymeds,
hims, honehealth, ivyrx, joiandblokes, joinamble, joinfridays, kingsbergmedical, lifemd,
marekhealth, maximustribe, mydrhank, niagenplus, nurx, onemedical, remedymeds, ro, rugiet,
sermorelin, struthealth, telolife, trtnation, truniagen, tryshed.

## Missing / Stale Coverage

- **Visual coverage is a floor: 34 of 54 `telehealth.md` brands have `visual.md` (63%).**
  The 20 telehealth brands without a visual layer are not "lower quality" — the layer is
  opt-in (`modules/VISUAL.md`: written only when a consumer needs a visual read). Absent ≠
  poor.
- **Capture depth varies 5×** (9 cards kingsberg → 51 joinfridays), so card counts are a
  function of mining depth, not site complexity alone.
- **2 brands carried QA exclusions** (`qa_status: exclusions-noted`): remedymeds (one
  animation-artifact card dropped), kingsbergmedical (one lazy-load band dropped);
  joinfridays used Tier-B `recapture-used`. None empty; all usable.
- Capture clocks span **2026-06-15 → 2026-06-18** — tight, no staleness concern this run.

## Source Gaps

- **The `polarity` field is not a cross-brand quality metric.** It is confounded two ways:
  (a) **capture depth** — more cards = more raw `strong`s available, so absolute counts
  rank depth, not quality; (b) **rater compression** — `%poor` ranges 0–56% but on thin
  files (kingsberg 56% of *9* cards) it is noise. The contract already parks scoring
  because `weak` failed calibration; this run confirms the *instance* polarity (`poor`,
  187 cards / 15%) is real but **not aggregatable into a ranking**. *(Operator caution
  worth recording: my own first parse miscounted the polarity vocabulary as `weak` and read
  it as "never fires" — wrong; the negative pole is `poor` and fires 15% of the time. The
  field is fiddly enough to misread, which is itself evidence against leaning on it.)*
- **No demand-side or live evidence** — presentation *character* is a supply-side read of
  owned pages; "premium" here means visual control, not market outcome.

## External Completeness Check

Not run — completeness is not load-bearing for a presentation-pattern read, and the panel
is explicitly framed as a 34/54 floor of an opt-in layer. An external "best-designed
telehealth sites" listicle panel would be the bounded-live way to corroborate the
character clustering demand-side (cf. run 012's listicle-as-coverage-radar finding).

## Market Pattern

**The headline market pattern** (J2, a Judgment grounded in C3): DTC telehealth has
**converged on component-system discipline** — nearly every brand has a clean, repeatable
card/grid/accordion/PDP kit; that is now *table stakes*, not differentiation. Visual
differentiation has moved to **two axes**: (a) **owned production** — custom product
renders, branded packaging, bespoke data-viz/illustration (the brands that own this read
premium: hims, functionhealth, gethealthspan, agelessrx, rugiet, truniagen, joiandblokes);
(b) a **restrained editorial type system**, increasingly the roman + italic-serif device.
The **universal weakness is the borrowed layer** — stock photography, library icons,
manufacturer/UGC imagery — and **utility pages** (footers/legal/reviews), where even the
most disciplined brands (hone, hims, functionhealth) visibly drop. A brand-builder's
takeaway: *you cannot win on components anymore; you win on owned imagery/illustration, and
nobody has solved the borrowed-asset/utility-page layer.*

**The system-test pattern** (J3, the design payload — what this teaches Truffle):

- **The visual layer aggregates at the *impression/prose* grain, not the *polarity-field*
  grain.** The cross-brand signal came from reading 34 impression paragraphs and finding
  *independent* convergence on the same owned-vs-borrowed language — which is *evidence the
  layer captures something real*, since the per-company miners did not coordinate. The
  structured `polarity`/`family` fields, by contrast, do **not** roll up into a usable
  cross-brand discriminator (depth + rater confounds above).
- **Consequence:** if cross-brand visual reads recur, the reusable helper is an
  **impression-concatenation recipe** (glob `visual.md`, pull the `## Visual & brand
  impression` block, join `anchor_category`) — *not* a polarity-score rollup and **not** a
  durable "visual-cluster" category object. This is `query-time-grouping-enough` for the
  visual layer, extending the MRL-002 recipe family to a **fifth source surface**
  (`visual.md`) after price/positioning/offer/access State.
- **The no-score boundary held and was workable** — a genuinely useful creative-director
  category read ("owned moat, borrowed weakness, three characters") was produced **without
  any score, grade, or leaderboard.** Evidence that `modules/VISUAL.md`'s parked-scoring
  line does not block cross-brand consumption.

## What Would Change This Answer

- A **second cross-brand visual read** on a different cohort that found the polarity field
  *did* discriminate (e.g. after a depth-normalized re-mine) would reopen the
  prose-vs-polarity-grain finding.
- **Demand-side corroboration** (bounded-live "best-designed" listicle / owned "vs" pages)
  could confirm or break the three-character clustering and the soft positioning
  correlation.
- A **depth-normalized** polarity capture (fixed cards-per-page) would test whether `%poor`
  becomes a usable signal once the capture-depth confound is removed.
- Extending the panel toward the missing 20 telehealth brands could shift the
  character-cluster proportions (current split is a 34/54 floor).
