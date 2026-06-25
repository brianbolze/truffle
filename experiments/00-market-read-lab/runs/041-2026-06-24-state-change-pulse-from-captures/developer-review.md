# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Evidence verification (adversarial pass on the read's load-bearing claims)

- **"State has no append-only home" (G1):** verified against `architecture.md:57,60,75` —
  `profile.md` = current snapshot; `signals/` = external source movement, timeline machinery
  deferred. Holds. Caveat surfaced: the read says company State has *no* append-only home;
  strictly, `signals/` *could* one day host it, but its documented scope today excludes
  company-intrinsic State. Read's wording ("no append-only home … today") is accurate.
- **"Capture-method noise dominates" (S1):** independently reproduced — belmar homepage diff
  is `www`/slash normalization + an expanded nav mega-menu, no price/offer line changed.
  This is the strongest claim and it survives scrutiny. **But n=1 same-page diff** — the run
  ran exactly one clean diff and generalizes from it. Flagged below as DR1.
- **"C6 dissolves" (S2):** verified — functionhealth 06-13 = render variants, 06-16 = tiles
  only. The clock-vs-folder signal genuinely fails to detect lag. Honest re-framing, not a
  walk-back of a real finding.

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | The dated-capture convention overloads one folder shape for three purposes (full / partial-deepen / visual-render) with no purpose/scope marker — so retained history isn't introspectable. | C2; functionhealth render-only folders | G2 · gap; W1 · wish |
| **Structure** | No versioned/append company-State grain — overwrite is the contract; change exists only as sparse prose (~7/145). State/Signals/Judgment line held cleanly by the read. | read.md Result(1); C4; architecture.md | G1 · gap |
| **Query / access** | "Which domains have a diffable history" is not a folder-count query — needs a content pass. Denominator (21) honestly named partial. | C1/C2 | G2 · gap |
| **Freshness / automation** | `captured_at` is per-profile freshness, not "newest store knowledge"; the two diverge whenever a visual/deepen folder is newer. A reader could over-trust the clock either direction. | C6; C1 | S2 · surprise |
| **Synthesis** | Read labeled State vs the persistence-boundary Judgment cleanly; C6 self-correction is a model of "say not-found, not not-there." | read.md C6 | — (strength) |
| **Guardrails** | Store-only respected; no scrape/mutation; receipts source-graded; absence language disciplined. Clean autonomous run. | exit check all pass | — (strength) |

## Lenses

**Steward** — System stayed honest. The read resisted the easy footgun (reporting belmar's
nav-menu expansion as a market change) and self-corrected the lag hypothesis. The one
exposure is generalizing the noise claim from a single diff (DR1).

**Dev Agent** — The repeated toil this run hit (hand-classifying folder purpose) is the same
shape as W1: a grep-verifiable per-folder purpose marker would remove it. Recorded as a
sighting only — not proposing the marker here.

**Founder** — The finding compounds the warm asset *negatively but usefully*: it tells the
roadmap not to build a State-diff/change-feed on top of `captures/` until both a consumer
and a folder-purpose marker exist. Avoids ontology gravity ("no new primitive needed" stays
live). The deferred Signals-timeline machinery is the natural home *if* company-State
change-pulse ever earns it — this run is a data point that it has not yet.

## Recommendation

- **No-op / keep as observation:** yes — clean gap-probe, no build. "No new primitive
  needed" is the honest disposition.
- **Watch for recurrence:** `freshness-monitoring` (first real probe of company-State change
  grain since 018/032), `coverage-caveat` + `denominator-reconciliation` (capture-history as
  a partial, purpose-mixed denominator). The "unreliable second channel" shape (prose-only
  change notes) now recurs with run-037 DR2 and run-039 G2 — note for a future pass.
- **Severe `risk-miss` to surface now:** none. The belmar-noise trap is a risk *avoided*,
  logged as S1, not shipped.

## Raw learning to preserve

Developer-review sightings added to `run-notes.md` Observations as **DR1** (the noise-
dominates claim rests on n=1 same-page diff — reproducibility-of-finding caveat) and the
strengths above. CR1 from consumer review and G1/G2/S1/S2/W1 from the read are lifted to
`learning/observations.md` below. No lesson proposed; `lessons.md`/`brian.md`/`passes/`
untouched.
