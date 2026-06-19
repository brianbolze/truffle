# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [query-time-grouping-enough, denominator-reconciliation, coverage-caveat]
```

> **Loop 2 outcome (2026-06-19):** Reviewed via a 3-pass adversarial workflow (evidence verifier +
> consumer + developer). The verifier caught one material aggregation error — **Kingsberg was
> miscategorized as fully gated** when its own captured file shows `partial` price ranges
> ($500–$1000/mo HGH, $70–$100/mo testosterone). Corrected in `read.md` + receipt: split moved
> **5/4/3 → 5/5/2 (~42/42/17)**, and the two-category-gater claim (C4) narrowed to **Defy + Marek
> (n=2)**. The headline finding C3 (price-posture tracks business model, not molecule) **survived
> scrutiny**. No new triage items; Evidence Log appended to MRL-002 and MRL-001.

## 30-second operator read

- **Did the run work?** Yes. Store-only, no spend, no mutation. First **State** read after three
  consecutive Signals reads (005/006/007), and a clean **recurrence test** of run 000's GLP-1
  price-visibility pattern on a different cohort.
- **What was awkward?** The cohort boundary. "Men's-health / TRT / hormone" has fuzzy edges —
  longevity/NAD brands (Hone, Lifeforce, getOpt) straddle, and enclomiphene/peptide sellers
  (Vitality, Sermorelin) publish a price but aren't selling *exogenous* TRT. Both forced a judgment
  call that moves the headline ratio. Denominator-reconciliation, again.
- **What the next agent should know:** the finding is strong and *generalizes* — price visibility
  tracks **business model, not molecule**. The same three brands (Defy, Marek, Kingsberg) gate fully
  in both GLP-1 and TRT. The `offerings.md` `Visibility` column carried this with zero re-capture;
  this is the cleanest demonstration yet that the captured-State layer answers price-posture reads
  off disk.

## What happened

Gated on the contract (scout-only → store-only → autonomous → approval:no, all pass). Re-derived the
cohort from `telehealth.md` frontmatter (`anchor_category` + `audience`) rather than porting run 001's
list → 12 men-first TRT/hormone-anchored brands. For each, read the `offerings.md` Roster
`Visibility` column + verbatim price on the **testosterone/hormone anchor row** + `site_notes`, and
classified the *therapeutic* price posture into publishes / membership-floor / gated. Built one
derived receipt ([`receipts/trt-price-visibility-panel.md`](receipts/trt-price-visibility-panel.md)),
pulled run 000's GLP-1 split for the recurrence comparison, and wrote the read keeping the
business-model claim (C3) and the two-category gater claim (C4) explicitly labeled as Judgments tied
to the per-brand State. No external fetch, no `store/` write.

## Inputs and scope

- `store/*/telehealth.md` frontmatter (54 packs) — cohort derivation via `anchor_category`/`audience`.
- `store/*/offerings.md` Roster `Visibility` + verbatim `Price` + `site_notes` for the 12 core brands
  (captures 2026-06-03…06-18); plus a 6-brand men-only ED/hair band inspected as a cross-check.
- `runs/000-.../read.md` for the GLP-1 split (prior-run *evidence*, not template).
- **Exclusions:** generalist all-gender TRT lines (henry, lifemd, invigor, strut) not scored;
  mdpep-com unscorable (bare dir); enclomiphene/peptide "publishers" flagged as not-exogenous-TRT.

## Friction log

- **Cohort boundary is hand-drawn every time.** Deciding TRT-vs-longevity and exogenous-T-vs-SERM
  was the only real labor — the same denominator-naming toil run 000/004 hit. The `Visibility`-column
  extraction itself was trivial (one grep per brand).
- Same **latest-capture / field-extract** loop as prior reads, but on a *State* field (`Visibility`)
  rather than a Signals dir — reinforces MRL-002's "State *and* Signals" recipe scope.

## Evidence limits

- **Partial denominator** — 12-brand working set, not a census; generalist all-gender brands carry
  unscored TRT lines that would move the 42/33/25 split. Said plainly in the read and receipt.
- **Boundary judgment** — including enclomiphene/peptide brands as "TRT publishers" inflates the
  publish band; excluding them sharpens "clinics gate testosterone" toward ~3/12 exogenous-T sellers.
- **A/B-volatile pricing** (Marek, Maximus `site_notes`) — numbers are a captured floor ≤16d old,
  not a live quote.
- C4 (two-category gaters) is an **n=3 two-category sighting**, not a proven law.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only` or `local-existing`: **pass** (store-only)
- `approval_needed: no`: **pass**
- No disallowed action happened: **pass** (no live fetch, no mutation, capture-gap vs intake-gate kept
  distinct, denominator flagged partial)
- Required citations / receipts present and source-graded: **pass** (one derived receipt, 12 sources
  graded)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (every price ties
  to a dated capture; no current/news claims made)
- Absence language says "not found", not "not true": **pass** ("not scored", "not captured", "gated by
  the company per site_notes" — never "no price exists")

## Surprises

- **The split barely moved between molecules.** GLP-1 was 33/42/25; TRT is ~42/42/17 *(post-Loop-2
  correction)* — close enough that the *posture distribution* looks like a property of telehealth DTC
  itself, not the category.
- **The gaters are nearly identical across categories.** Defy and Marek gate fully in both reads
  (Kingsberg gates in GLP-1 but is partial in TRT — caught in Loop 2). Still the strongest single
  piece of evidence that posture = model.
- **Gaters publish labs loudly while hiding every drug.** The high-touch clinics aren't opaque — they
  publish a `$299–$450` lab/intake anchor and gate only the therapeutic. Price *is* the pitch for
  them too; it's just the consult that's priced, not the molecule.

## Pressure tags

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `query-time-grouping-enough` | The whole read was a grouping of existing `offerings.md` `Visibility` State; no durable "price-posture" category object is needed or wanted. | no-op — reinforces existing posture (MRL-002 recipe, not a stored taxonomy) |
| `denominator-reconciliation` | Cohort boundary (TRT-vs-longevity, exogenous-T-vs-SERM, generalist all-gender exclusion) was the only real labor and moves the headline ratio. | watch / strengthens MRL-001 |
| `coverage-caveat` | Generalist all-gender TRT lines unscored; mdpep bare; A/B-volatile pricing — all materially bound the completeness claim. | watch / strengthens MRL-001 + MRL-003 family |

No new tag needed. "No new primitive needed" is the honest outcome — this is a recurrence read.

## Triage submissions

No new items. This run **adds recurrence evidence** to existing queue items rather than opening new
ones; Loop 2 may append Evidence Log entries to:

- **MRL-002** (query recipes) — a *State* price-posture grouping recipe (latest-capture +
  `Visibility`-column read + business-model labeling) recurred cleanly; same family as the Signals
  recipe pressure.
- **MRL-001** (denominator reconciliation) — cohort-boundary labor recurred and is the load-bearing
  caveat; the "publish/gate split tracks model not molecule" finding *depends* on how the denominator
  is drawn.

No graduation, no implementation, no spike proposed.

## Next-run advice

- To close the denominator gap cleanly, a **store-only** follow-up could score the generalist
  all-gender TRT lines (henry, lifemd, invigor, strut) and re-test whether the 42/33/25 split holds —
  a tight recurrence probe, no spend.
- The "price-posture = business-model" thread is now a **two-category** pattern (GLP-1 + TRT). A third
  store-only category read (e.g. longevity/NAD or sexual-health) would test whether it's a telehealth
  law or a coincidence — high-leverage, cheap.
- Treat enclomiphene/SERM brands explicitly as a *distinct* sub-band next time; don't silently fold
  them into "TRT."
