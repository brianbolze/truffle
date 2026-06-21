# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Evidence verification (adversarial pass)

Re-derived the three load-bearing counts against the receipts before reviewing:

- **Exa 1/16 recall — CONFIRMED.** Hone's 25 Exa neighbors (`receipts/exa/honehealth-com.json`)
  intersect run-017's 16-brand set at exactly **one** domain (`hormonemd.com`, rank 4). All four
  Tier-1 substitutes (mylifeforce, gogeviti, gethealthspan, defymedical) are **absent** — the rest
  are name-alikes (honeyhealth.ai, honeybeehealth, hormonefitness, havenhealth, …). C2 holds.
- **Comparison-page 4/16 recall — CONFIRMED.** `comparison-pages-2026-06-20.md` Q1 names
  defymedical, getpetermd, maximustribe, mylifeforce as in-store **and** in run-017's set,
  incl. 2 of 4 Tier-1 (Lifeforce/mylifeforce, Defy). C6 holds.
- **Page-type breakdown — CONFIRMED (verifier-corrected wording).** Q1's five result pages: cbinsights
  (competitor-intel, 3rd-party), hims `/vs` (owned), policylab (affiliate listicle), honehealth `/vs`
  (owned), vikingalternative `/vs` (owned) → **3 owned `/vs` + 1 competitor-intel + 1 affiliate; only
  1 of 5 a neutral third-party.** C7 holds (the "self-selection biases the named set" point is intact;
  the prior "4 of 5 owned/self-publishing" phrasing was tightened per the Loop-2 verifier).
- **Store-absent nominees — CONFIRMED.** C8 names Numan, Male Excel, Fountain TRT, Viking Alternative
  Medicine, Sesame; `~$0.53` Exa spend confirmed against 24 calls × ~$0.022.

No discrepancies; no corrections needed in `read.md`. Two cosmetic wording fixes from the evidence
pass have been folded into `read.md` already.

## Bounded-live audit

Contract: `budget_class: expanded` — operator-approved by Brian 2026-06-20, logged in
`run-notes.md` live_evidence_plan. Not an unattended budget breach.

| Ceiling | Limit | Actual | Status |
|---|---|---|---|
| Source families | 3 allowed | 2 used (exa-neighbor-graph + comparison/relationship-pages) | Pass |
| Exa calls | 30 | 24 (23 anchors + 1 Hone smoke test) | Pass |
| SERP / Firecrawl searches | 20 | 3 `firecrawl_search` calls | Pass |
| Firecrawl scrapes | 25 credits | ~18 credits | Pass |
| Exa USD spend | ~$0.60 implied | ~$0.53 actual | Pass |

Every outside source logged in `live_evidence_used` with source_family, source_grade `secondary`,
captured_at, spend_note, and claim_ids. Depth-1 only; no store mutation; no durable primitive;
comparison-page family restricted to Hone/Ro/Notion (hub-focus stop rule, not all 23 anchors).
**PASS — no flag.**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture / external tools** | First market-read use of the dormant `exa_similar.py`. Sharp reusable boundary: the tool returns name/embedding-similarity neighbors, not cross-shop competitors. Quality tracks anchor-name distinctiveness (posthog → real rivals; hims/ro/notion → mirrors/link-shorteners/name-collisions). 1/16 recall on Hone's calibration set; all 4 Tier-1 substitutes missed. | C1–C4, S1–S2; `receipts/exa/*.json`; `analysis-output.txt` | O1, S1 — ready-for-triage. Document the name-bound limit as a usage caveat on `exa_similar.py` before any future caller reuses it without corroboration. |
| **Structure / relations** | State/Signals/Judgment boundary held: every external named set was labeled `secondary`, kept as demand-side leads, and the run refused to write a `competitors:` field. Reinforces MRL-011 with demand-side evidence — the external sources that would populate such a field are unreliable at the source (Exa 1/16; comparison pages 4/16 but SEO-biased). 017's supply-side + 030's demand-side together double-evidence "hold, do not build the field." | C2, C6, C7, G1; read.md Result / Gap Map | G1 — ready-for-triage (MRL-011 second sighting, demand-side). |
| **Query / access** | Cross-anchor orchestration (apex-fold mirrors, dedupe, store-match, hub-score) was hand-built in `receipts/analyze.py` because `exa_similar.py` is match-free by design. One sighting; mirrors the MRL-002 friction pattern on the external-neighbor grain. If a second external-neighbor run repeats this toil, name it as a documented recipe — not a helper, consistent with "conventions, not infra." | F1; `receipts/analyze.py` | Recur-watch — recipe-if-recurs. |
| **Freshness / automation** | No pressure. Point-in-time read; no monitoring or refresh claim made. | — | No-op. |
| **Synthesis** | The calibration-against-store-baseline read shape (measure external recall against a known store set) is a clean, reusable QUERYING pattern for "is this external source trustworthy?" — distinct from the coverage-radar recipe (MRL-002) in that it uses the store *as the denominator*, not as the thing being compared against an external panel. One sighting; pairs with the bounded-live coverage-radar family if it recurs. | read.md Result; Gap Map source-quality table | Recur-watch — note, do not name yet. |
| **Guardrails** | Source-rigor held under three external-source confound pressures, all correctly caught and labeled: (a) Exa similarity ≠ cross-shop — name-distinctiveness-bound, returns mirrors/link-shorteners on common-name anchors (C3, C4, S1); (b) owned-`/vs` SEO self-selection biases "alternatives to X" named sets toward whoever wrote the page — cross-source recurrence is the only usable filter (C7, O3); (c) GoodRx named drugs not platforms — a category-extraction confound recurrence of run-024 (C9, O4). Trap V1 (the per-anchor store-absent rate looks like a selection-bias measurement but is junk-denominator noise) was correctly identified and not over-claimed. | O1, O3, O4, S1, V1; C3, C7, C9 | O1, O3, O4 — ready-for-triage (MRL-008 additive flavors). |

## Lenses

**Steward** — The system stayed honest. Absence language throughout says "not found in this
panel," never "not a competitor" — see read.md External Completeness Check. All live evidence
is graded `secondary`. The run used 017's store-only tiering as the *trusted substrate* and
measured the external panel against it, rather than letting the noisier outside sources overturn
it. V1 (the per-anchor store-absent rate as false selection-bias) is the false-completeness guard
working exactly as designed.

**Dev Agent** — The recurring toil is real but a single sighting on this grain: every caller
of the match-free `exa_similar.py` must rebuild the same fold/dedupe/store-match layer. A
**documented recipe** is the right future artifact — not a helper or stored neighbor object
(consistent with "conventions, not infra"). The lighter primitive the run names but does not
build — owned `/vs` page as a directed edge (W1) — is the most promising next probe before
anything on the demand-side relation surface graduates.

**Founder** — The run compounds the warm asset without adding ontology gravity: it produces a
negative result (two external sources fail differently and neither is graduation-grade) plus a
5-name capture worklist, and creates zero new primitive, field, or stored object. The
calibration only *worked* because run 017's cached tiering existed — exactly the "cite the
warm store, don't rebuild from scratch" posture the engine wants.

## Recommendation

- **No-op / keep as observation:** calibration-against-baseline synthesis shape (recur-watch,
  one sighting); untested cleaner sources W1 / W2.
- **Watch for recurrence:** Exa name-distinctiveness boundary (S1, S2) — document as usage
  caveat on `exa_similar.py`; directed-`/vs`-edge source idea (W1); cross-anchor
  orchestration toil (F1) — recipe-if-recurs.
- **Submit triage evidence (mature, three items):**
  - MRL-011 — second sighting, demand-side (O1, O3, G1).
  - MRL-008 — two new external-source flavors + one category-extraction recurrence (O1, O3, O4, S1).
  - MRL-009 — 5 store-absent cross-shop nominees, propose-only, NOT autonomous-safe (O2).

## Optional triage evidence

For the steward to weigh (do not graduate):

- **MRL-011** (competitive/substitute relation as Judgment) — second sighting, now demand-side.
  Run 017 inferred the substitute set supply-side from store State; run 030 reached outside and
  found the demand-side sources that would feed a `competitors:` field (Exa 1/16; comparison
  pages 4/16 but only 1 of 5 a neutral third-party) are too noisy to be joinable-fact grade. Strengthens
  "hold, do not build the field" — now double-evidenced. Pointer: read.md Result / Gap Map;
  run-notes.md O1, O3, G1.

- **MRL-008** (source-rigor / confound family) — two new external-source confound flavors:
  (a) Exa `/findSimilar` similarity is name-distinctiveness-bound — mirrors/link-shorteners on
  common-name anchors (`hims`→bit.ly/HMS Holdings, `ro`→Roon/ro.am, `notion`→notion.so/OneNote),
  real rivals only on distinctive names (`posthog`); guard: never use as a competitor/cohort
  enumerator without corroboration; (b) owned-`/vs` SEO self-selection: only 1 of 5 "Hone alternatives"
  result pages was a neutral third-party (3 owned `/vs`, 1 competitor-intel, 1 affiliate) → cross-source
  recurrence is the only usable filter on a demand-side named set. Plus a recurrence of the run-024 category-extraction confound: GoodRx
  named drugs (Qsymia/Contrave/Orlistat/Phentermine), not platforms. Pointer: read.md C3, C4, C7,
  C9; run-notes.md O1, O3, O4, S1.

- **MRL-009** (write-back / capture worklist) — demand-side nominees (lower-confidence than the
  listicle worklists from runs 022/024, sourced from SEO/owned/affiliate pages): Numan, Male Excel,
  Fountain TRT, Viking Alternative Medicine (Hone/TRT); Sesame (Ro/GLP-1). Each requires a
  `/research-company` capture to confirm it front-doors as a real cross-shop peer before counting
  as corpus growth. NOT autonomous-safe (Firecrawl spend → human approval). Pointer: read.md C8 /
  Missing/Stale Coverage; run-notes.md O2.
