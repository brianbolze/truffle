# Findings — Probe 0: does `profile.md` enrichment defer `offerings.md`?

> **Verdict: defer `offerings.md`; adopt only the cheap piece.** Enriching `profile.md`'s *What
> they offer* with verbatim per-line **price** changed almost nothing for the consumer — two cold
> agents (baseline vs. enriched) returned the **same answer with the same hand-derivation**, and
> **both independently concluded the cohort is not sortable from any single field**. The one durable
> win was the per-line **`price_visibility` token** (`published | partial | on-request`): the enriched
> agent classified "can I even get a price?" off a **one-line read**, where the baseline agent had to
> infer it from `unverified_fields` + `site_notes` + Provenance "Couldn't get". Net: the sortable-price
> win that originally motivated `offerings.md` is delivered by **neither** profile-enrichment **nor**
> the drafted (verbatim-price) `offerings.md` — it needs the structured `{value,unit,cadence}` the
> design deliberately punts project-side, and **no live consumer demands it**. So the minimal,
> evidence-backed move is a `price_visibility` convention in `profile.md`; `offerings.md` stays parked.

*2026-06-01. The de-risking probe proposed in the [offerings design review]. Tests the anti-additive
alternative — enrich what exists — before activating a new module.*

## Method

A/B on the telehealth cohort (9 GLP-1/weight-loss brands; Function Health excluded, 0 GLP-1 hits).

- **Two sandboxes**, both stripped of `CLAUDE.md`, `_design/`, `experiments/`, `BACKLOG.md` (no
  design/answer leakage): **baseline** = current store; **enriched** = the 9 cohort profiles with
  *What they offer* rewritten to a consistent convention — bold-led family lines carrying the
  **verbatim price** + a `` `[published|partial|on-request]` `` token, grounded strictly in each
  profile's body + a capture spot-check (no invention).
- **Same flagship query** to each: *"which brands sell a GLP-1/weight-loss program, what does each
  charge to start, sort by price, flag the gated ones, cite sources."* Plus a forced **process-notes**
  section (files opened, greps run, per-brand "single line vs. pieced-together").
- **Harness caveat — honest.** The cold `claude -p` harness from the prior consumption probes **hangs
  when nested inside a running Cowork session** (collides on the stdio permission handshake; 0 output,
  killed after ~50 min). Pivoted to two independent `Agent`-tool subagents, each pinned to its sandbox,
  read-only, no web. Trade-off: subagents inherit this project's *orientation* (read-order, principles)
  — so this is **not** a cold-*discovery* test (that was already proven in the 2026-05-31 probes). It
  tests the **answer-quality delta**, and the inherited orientation is **identical across both arms**,
  so it cancels in the A/B.

## Findings

**1. Enriching *tightened* the profiles, didn't bloat them.** 8 of 9 sections got **smaller**
(Marek −985 B, Lifeforce −885 B, AgelessRx −812 B); only price-less Eden grew (+100 B). Net ≈ −4.3 KB
across 9. The convention *replaced* drift already in the corpus — PeterMD and Marek had each grown an
ad-hoc `**Pricing (verbatim):**` sub-block; others inlined prices inconsistently in prose. **The "a
multi-product section can't hold per-offering pricing → needs its own doc" worry — the core case for
`offerings.md` — did not appear at the family altitude.**

**2. Verbatim-price enrichment = low marginal value for the consumer.** The prices were *already* in
the bodies; the existing bold-led-line convention (QUERYING Recipe 4) already lets an agent locate
them. So the enriched arm produced the **same table, same ordering caveats, same per-brand
hand-derivation** as the baseline (Eden/Hims membership-stack, PeterMD promo-vs-recurring,
AgelessRx multi-SKU floors, Healthspan program-vs-SKU). Effort did not drop (both ran ~7 greps; neither
opened `captures/`). Adding *more* price structure to `profile.md` bought nothing the body convention
didn't already give.

**3. The `price_visibility` token *was* the real, cheap win.** It is the one place the arms diverged.
Enriched agent, on the gated brands: *"line 58: 'No public price' `[on-request]` — determined from the
explicit profile statement."* Baseline agent reached the same gated calls, but **by inference** from
`unverified_fields` + `site_notes` + the Provenance "Couldn't get" line. The token turns *"can I even
get a price?"* — the axis common to SaaS sales-gating, telehealth quiz-walls, luxury price-on-request —
into a **one-line, greppable read** (`rg '\[on-request\]'`). And it lives fine as a per-line token in
`profile.md`; it does **not** need a separate doc.

**4. Neither approach makes the cohort sortable by price — by design.** Both agents concluded a script
**could not** `ORDER BY` a single field, because the *value* fragments by unit even within one
telehealth cohort (med-only vs. membership-stacked vs. program-entry vs. billed-quarterly). That is
exactly the heavy normalization the design **already punts project-side, per messy vertical**. Crucial
implication: the drafted `offerings.md` (verbatim `price` + `price_visibility`, **no** `{value,unit,
cadence}` struct) would **not** have beaten the enriched profile on this query. The thing that *would*
close sortability is the structured price the design deliberately dropped — so activating
`offerings.md` now buys little the cheap token doesn't, at far higher cost.

## Scope caveat — the unprobed grain

This tested a **family-level cohort-price** query (the flagship P2 shape). It did **not** test a
**per-SKU** query ("cheapest Zepbound *vial* specifically across brands") — which a `profile.md`
family line genuinely cannot hold (one line per family, not per SKU), and where `offerings.md`'s
per-SKU roster + deep blocks would earn their keep. But there is **no live consumer at that grain**
either — so it stays a *future* trigger, not a *now* one. If/when a per-SKU comparison becomes a real
query, re-open activation; until then, the family altitude is what consumers hit, and the token covers
it.

## Decision

- **Adopt:** a per-offering **`price_visibility`** convention (`published | partial | on-request`) on
  the bold-led lines of `profile.md`'s *What they offer* — the one universal axis, proven cheap and
  load-bearing here. Tiny SCHEMA edit (guidance + a one-line grep recipe in QUERYING). **Keep verbatim
  prices exactly as the body rule already requires — the token *wraps* the snippet, never replaces it.**
- **Defer:** `offerings.md` activation. It remains a settled, parked schema. Re-trigger on a **live
  per-SKU offering-comparison consumer** (the same bar that parks rung-3 SQLite) — not before.
- **Backlog hygiene:** the corpus already drifted (ad-hoc pricing sub-blocks; 0 profiles mark
  visibility). The `price_visibility` convention + a light cleanup pass closes the drift.

---

<sub>**Artifacts:** [`_out/prompt.txt`](_out/prompt.txt) (the shared query); [`_out/baseline-answer.md`](_out/baseline-answer.md)
+ [`_out/enriched-answer.md`](_out/enriched-answer.md) (the two cold-agent answers, verbatim);
[`_out/byte-delta.txt`](_out/byte-delta.txt) (enrichment size deltas). Sandboxes were throwaway under
`/tmp/wr-probe0-*`. Authored 2026-06-01.</sub>
