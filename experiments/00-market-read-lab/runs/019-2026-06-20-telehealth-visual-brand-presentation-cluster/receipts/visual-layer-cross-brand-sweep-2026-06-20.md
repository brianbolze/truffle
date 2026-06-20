# Receipt - visual-layer cross-brand sweep

Supports the cross-brand presentation read: the panel definition, the polarity/depth
spread, the impression-paragraph corpus, the positioning cross-tab, and the declined
price-transparency cut.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/visual.md` ∩ `store/*/telehealth.md` (34 domains) | visual.md capture 2026-06-15→06-18 | local-store | derived | none | no | C1 |
| S2 | `polarity:` + `family:` fields across the 34 `visual.md` | same | local-store (Judgment-dense) | derived | none | no | C2 |
| S3 | `## Visual & brand impression` block of each `visual.md` | same | local-store (Judgment-dense) | derived | none | no | C3 |
| S4 | `anchor_category` (`telehealth.md`); `visibility` (`offerings.md`) | telehealth clock 2026-06 | local-store | derived | none | no | C4, C5 |

## Method

- **Panel (C1):** `comm -12` of `ls store/*/visual.md` and `ls store/*/telehealth.md`
  basenames → 34 domains with both. (Store-wide: 135 domains, 44 `visual.md`, 54
  `telehealth.md`.)
- **Polarity/depth (C2):** regex `polarity:\s*(['"]?\w+['"]?)` per file, strip quotes,
  tally strong/mixed/poor. **Vocabulary note:** the third pole is **`poor`**, not `weak`
  (an early parse used `weak` and wrongly read 0 — corrected). Card totals 9–51; the
  34-brand panel = 485 strong / 366 mixed / 148 poor = 999 cards (15% poor). (Store-wide
  across all 44 `visual.md`: 618 strong / 450 mixed / 187 poor.)
- **Impressions (C3):** extracted the `## Visual & brand impression` paragraph from each of
  the 34 files; read all 34; coded for the owned-vs-borrowed arc, character, and type
  signature. Full corpus persisted in the run transcript.
- **Positioning (C4):** `anchor_category` frontmatter per `telehealth.md`.
- **Price-transparency (C5):** the `offerings.md` `visibility` value is a structured
  `| Visibility |` table column (`published` / `partial` / `on-request`) **parseable for all
  34 brands** (Loop 2 evidence-verifier independently re-parsed all 34). An earlier quick
  `visibility:` prose-grep matched the wrong form and under-counted to n=0 for 21/34 — a
  parse error, not a data gap. The cut is **declined on scope grounds**: a
  price-transparency-vs-visual-character correlation is not a well-formed metric (collapsing
  a per-SKU visibility mix to one scalar to correlate with an interpreted visual label would
  fabricate a relationship). Declined, not inferred.

## Evidence

**Polarity / depth spread (C2), selected rows (strong / mixed / poor / total):**

| brand | s | m | p | total | %poor |
|---|---|---|---|---|---|
| hims | 26 | 13 | 3 | 42 | 7% |
| joinfridays | 24 | 19 | 8 | 51 | 16% |
| gethealthspan | 20 | 12 | 8 | 40 | 20% |
| marekhealth | 17 | 13 | 11 | 41 | 27% |
| trtnation | 9 | 7 | 8 | 24 | 33% |
| kingsbergmedical | 0 | 4 | 5 | 9 | 56% |
| onemedical | 7 | 6 | 2 | 15 | 13% |

Range: total 9–51 (5× depth spread); %poor 0% (ivyrx, sermorelin) → 56% (kingsberg, n=9).
The spread tracks **capture depth + rater**, not a defensible quality ordering.

**Owned-vs-borrowed arc (C3), verbatim convergence across independent captures:**

- gethealthspan: "strongest on what it owns, shakiest on what it borrows."
- eden: "imagery breaks art direction wherever it isn't owned."
- joiandblokes: "controlled, premium men's-health system — owned art over stock."
- agelessrx: "Its strongest asset is owned craft … It frays at the seams: third-party
  packshots…"
- functionhealth: "weak points cluster in utility zones … assembled third-party imagery."
- hims / honehealth / marek / gogeviti / rugiet / truniagen: same arc (owned core →
  borrowed/utility weakness).

**Positioning cross-tab (C4):** editorial-premium ∋ longevity/NAD {gethealthspan, gogeviti,
agelessrx, honehealth, truniagen, niagenplus}, premium-TRT {maximus, marek}, incumbents
{hims, ro, remedymeds}. functional-catalog ∋ commodity-GLP-1 {directmeds, goodlifemeds,
telolife, ivyrx, mydrhank, henrymeds}, legacy men's-health {kingsberg, trtnation,
sermorelin}.

## Limits

- The `visual.md` layer is **Judgment-dense** (synthesized impression + interpreted "visible
  tells"); the cross-brand clustering is a **Judgment-on-Judgments**, not captured State.
  Its trust rests on *independent convergence* of separately-mined captures, not on any one
  rater.
- **Polarity counts cannot rank brands** — depth + rater confounds (above).
- Panel is **34/54 of telehealth brands** (opt-in layer); absent ≠ poor.
- Price-transparency correlation **not computable** from this sweep; not claimed.
- Supply-side only — "premium" = visual control, not market performance.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 34 brands have both visual.md + telehealth.md (the panel) | S1 | floor of 54 telehealth brands |
| C2 | polarity spread (9–51 cards; 15% poor) is depth/rater-confounded, not a ranking | S2 | `poor` is the negative pole, not `weak` |
| C3 | universal owned-core/borrowed-frays arc + 3 characters + italic-serif signature | S3 | Judgment-on-Judgments; independent-convergence basis |
| C4 | soft skew: editorial-premium↔longevity/incumbents; functional↔commodity-GLP-1/legacy | S4 | soft, confounded, supply-side (J1) |
| C5 | price-transparency cut declined on scope grounds | S4 | visibility column IS parseable (all 34); declined as not-well-formed, not unextractable; not assessed ≠ no relationship |
