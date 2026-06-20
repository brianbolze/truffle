# Developer Review — Run 013
# Sexual Health Access & Identity Map

**Verdict: valuable**

The run did something the lab hasn't done before: it answered a market question almost entirely from discrete enum fields (not prose `site_notes`, not pricing), and it self-audited the coverage gap inline rather than burying it. The question of whether the structural frontmatter cuts could carry a read is now answered — they can, with the field-fill-rate sub-caveat nailed precisely.

---

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | `pay_model: unclear` for 2/6 brands (bluechew, keeps) is a concrete depth-backfill gap. Not new capture-type pressure — just missing fill for an existing field. | Note as a depth-backfill candidate; do not build a scraper. |
| **Structure** | The State/Judgment boundary was largely clean — cells quoted verbatim, correlations and white-space explicitly labeled Judgment. One edge case: the "ED-franchise" 3rd tier (hims/keeps/ro) was a hand-drawn boundary, not a store field, and that judgment leaked into the denominator before being labeled. | Consider whether a `category_origin` note in `anchor_category` inline comments could surface franchise lineage more explicitly — but this is a minor ergonomic observation, not a triage item. |
| **Query / access** | The 3→24 anchored-vs-all-offerers under-count is now on a **third cohort** (GLP-1 in 012, sexual-health here), and the cohort-derivation recipe (anchor grep → ED-term grep → hand-draw 3 tiers) had to be invented fresh. This is the highest-signal system pressure this run produces. | Append to MRL-001 as third-cohort recurrence; the "anchored-only grep silently under-counts" finding is now pattern-level. |
| **Freshness / automation** | Structural cells (pay_model/modality/compounding_posture/access_model) are explicitly durable and low A/B-volatility. Freshness is less urgent here than on pricing/hero copy. | No action needed. |
| **Synthesis** | The "confidence gated by field fill-rate, not reasoning" sub-caveat for structural reads is genuinely new and generalizable. It is different in kind from the "quote, don't re-derive" guard (runs 009/010) — that guard was about cognitive error; this is about store completeness as the binding limit. | Append to MRL-002 Evidence Log as a new structural-read flavor with fill-rate sub-caveat. |
| **Guardrails** | The "quote don't re-derive" guard (MRL-002/009/010) was trivially satisfied on discrete enum cells — this run validates the guard by showing it's easiest to uphold when cells are discrete. No new guardrail pressure. | No action. |

---

## Key questions

### (a) Did the read cross cleanly from State into Judgment?

Largely yes. The two Judgment calls are both labeled: the access↔anchor correlation ("Judgment — a clean correlation across 6 brands, not a law") and the white-space claim. The verbatim-frontmatter evidence table is clean.

One rougher edge: the "ED-franchise" tier (hims/keeps/ro) is itself a judgment that sits upstream of the evidence table — it determines which 6 brands appear. The receipt documents this honestly ("the 'ED-franchise' tier is a hand-drawn judgment"), but the read treats those 6 brands as the "cohort" without consistently labeling the boundary as a Judgment in the body. It's disclosed; it's just not labeled at the load-bearing site. This is a minor presentation issue, not a system failure — the transparency is there, the framing is slightly soft.

**Steward call:** the boundary labor should eventually be supported by a store field (or at minimum a documented recipe), not re-derived in every access-map run. That's the MRL-001 punch.

### (b) Does this strengthen MRL-002, and is the fill-rate sub-caveat real and generalizable?

Yes to both. This is the fourth distinct State-read surface documented in MRL-002 (after price-posture/008, positioning/009, offer-structure/010). Each prior surface added a new recipe flavor:

- 008: Visibility-column extract
- 009: `access_model`/`Credibility` frontmatter, "quote don't re-derive" guard
- 010: narrative `site_notes` prose-surface variant + ambiguous-cell flag
- 013 (this run): **discrete enum cells**, trivially verifiable + the **fill-rate sub-caveat** as the new failure mode

The fill-rate sub-caveat is generalizable: any structural read on discrete fields has its confidence ceiling set by the fraction of cells filled, not by the quality of reasoning. At 67% fill for `pay_model`, the access claim is confident for 4/6 — period. This is different from "quote don't re-derive" (that's about what you do with what's there); this is about whether the field exists at all. Real distinction, worth a one-line addition to MRL-002.

### (c) Is the anchored-vs-all-offerers under-count a fair MRL-001 recurrence?

Yes. Third cohort (GLP-1 → sexual-health) with the same mechanical finding: `anchor_category: sexual-health` grep returns 3; the ED-selling set is 24. Same recipe as run 012's `anchor_category: GLP-1` returning 19 while LifeMD/Nurx/Wisp fell out. The pattern is real and predictable for any multi-service cohort where brands can offer without anchoring.

The run's own language — "the cohort boundary had to be hand-drawn into 3 tiers" — is correct, and the derivation receipt documents the inclusion rule cleanly. MRL-001's proposed convention ("name both the external inclusion rule and the internal anchored-only vs all-offerers cut") is now confirmed as the right fix.

**Biggest limit on the under-count claim:** the 24-brand "ED-selling" count is a recall-net floor (molecule-term grep), not a precision count. The receipt says so. Fair.

---

## Lenses

**Steward** — System is honest. `pay_model: unclear` is reported as the store's own captured value, not inferred. The 6→24 gap is named. The 3-tier boundary is disclosed. Capture clocks are per-row. The one honesty gap is that the "ED-franchise" tier judgment flows into the evidence table without a consistent inline label at the table's heading — a minor fix if this run gets published, but not a data integrity issue.

**Dev Agent** — Three straight cohorts (GLP-1, sexual-health, and implicitly TRT in 008) have forced the same multi-tier cohort derivation recipe: anchor grep → term grep → hand-draw franchise/straddler split → name the inclusion rule. The mechanical steps are identical. A one-page QUERYING recipe section documenting this pattern would remove the re-invention without building a helper. That's the marginal MRL-002 contribution from this run. The fill-rate sub-caveat belongs there as a one-liner ("structural confidence ceiling = filled cells / total cells; report the fraction").

**Founder** — The structural access-map cut (pay_model/modality/compounding_posture/access_model) is a genuinely reusable query surface — it works, it's cheap, it's store-only, and it found the odd-one-out (ro as clinical/insurance/all-genders outlier) the same way the structural cut found One Medical in the prior GLP-1 work. That's an asset being compounded cheaply. The white-space observation (no premium-clinical, sexual-health-first brand for men in the store) is a useful Strategist output, even from a 6-brand sample. The run earns its cycle.

The under-count pattern (3 vs 24) is not a major finding — it's a known friction that's been named. The more interesting open question this run surfaces is whether the "straddler tail" (TRT shops that list sildenafil) is a market signal worth a read of its own, or whether it's just noise in the grep. That's a Scout decision, not a system one.

---

## Recommendation

- **No-op / keep as observation:** Structural cells are durable; no freshness monitoring needed. The "ED-franchise" boundary softness is presentational; no new primitive needed.
- **Watch for recurrence:** The 3-tier cohort derivation recipe has now been invented three times (008 TRT, 012 GLP-1, 013 sexual-health). If a fourth run re-invents it, that is the moment to write a short QUERYING recipe, not before.
- **Submit triage candidates:** Two Evidence Log appends, both additive (no graduation):
  1. MRL-001: third-cohort recurrence of the anchored-only under-count
  2. MRL-002: fourth State-read surface (discrete enum cells) + fill-rate sub-caveat

---

## Triage submissions

### Append to MRL-001 Evidence Log

**2026-06-19 · Third-cohort recurrence of anchored-only under-count (run 013):** The sexual-health access read is the third cohort where `anchor_category:<cohort>` grep silently under-counts the actual offerers — `anchor_category: sexual-health` returns 3 (rugiet, rexmd, bluechew) while an ED-term grep returns 24. Same pattern as GLP-1 (run 012: 19 anchored vs LifeMD/Nurx/Wisp falling out) and TRT (run 008: cohort boundary required hand-drawn straddler calls). Cohort derivation required a 3-tier hand-draw (anchored / ED-franchise / straddler) each time. MRL-001's proposed convention — name both the external inclusion rule and the internal anchored-only vs all-offerers cut — is now confirmed as the right fix across three cohorts. Recurrence strengthens the case for a documented QUERYING recipe covering multi-tier cohort derivation.

### Append to MRL-002 Evidence Log

**2026-06-19 · Fourth State-read surface: discrete enum cells + fill-rate sub-caveat (run 013):** The sexual-health access-identity map is the fourth distinct State-read surface (after price-posture/008, positioning/009, offer-structure/010). New flavor: the load-bearing cut is entirely on **discrete enum fields** (`pay_model`/`modality`/`compounding_posture`/`access_model`), not pricing prose or narrative `site_notes`. The "quote, don't re-derive" guard (from 009/010) was trivially satisfied — discrete cells have nothing to paraphrase. The new, generalizable sub-caveat is the **fill-rate ceiling**: a structural read's confidence is bounded by `filled cells / total cells` for the load-bearing field, not by reasoning quality. Here `pay_model` was ~67% populated (4/6), capping the access claim at 4/6 regardless of reasoning. Addends to the recipe: (a) always report the fill-rate fraction for the load-bearing structural field; (b) "unclear" is a store-captured value, not an inference — report it as such.
