# Site presentation quality v4 — targeted cue detection (DESIGN)

Date: 2026-06-10 · Status: **designed, not launched** (Brian gate: fill
[`brian-cue-labels.md`](brian-cue-labels.md) before outputs are read)

## The pivot from v3

v1–v3 tested *rating* (bucket assignment) and failed on calibration: agents price
template slop 1–2 buckets high, and rule-tightening hit its ceiling. But v3's
evidence split cleanly into two layers: **perception mostly worked** (raters named
"clip-art iconography", "off-the-shelf vendor template" — then priced them wrong)
with one true perception failure (Jinfiniti's amateur charts went unmentioned by
all three raters; downsampling suspected). v4 stops testing judgment entirely and
tests the layer that might actually work: **can a model reliably detect specific,
named defects?**

If yes → the tool becomes *detect cues (model) + score (deterministic code with
Brian's weights)* — auditable, retunable without re-running models, ~free per site.
If no, even at native resolution → the blind spot is perceptual; record it as a
store convention and stop spending here. Decisive either way.

## Cue taxonomy (8 binary cues)

Each cue: `present | absent | cant-tell` + concrete evidence (which screenshot,
which region, what). **No overall quality verdict anywhere** — an evaluator that
outputs a rating has failed the protocol.

| # | Cue | Detection criteria |
|---|---|---|
| 1 | `amateur-charts` | Charts/graphs/diagrams/illustrations that read Excel-default, clip-arty, pixelated, or style-mismatched with the brand |
| 2 | `clipart-icons` | Generic clip-art icons; mixed icon families (stroke weights/styles/fill conventions); emoji-as-icons |
| 3 | `grid-violations` | Misaligned columns, inconsistent gutters/section padding, elements visibly off-grid, no consistent spacing scale |
| 4 | `stock-cliches` | Generic stock heroes (couple-in-field, handshake, smiling-doctor-with-clipboard), obviously unowned imagery |
| 5 | `template-slop` | Recognizable off-the-shelf theme (Wix/Squarespace/vendor), incl. dark-SaaS gradient aesthetic ("AI-startup" look) |
| 6 | `typography-issues` | >2 typefaces without system, default/system fonts in branded surfaces, cramped or loose leading, broken heading scale |
| 7 | `color-incoherence` | Clashing palette, inconsistent accent usage, low-contrast/unreadable sections |
| 8 | `duplicated-blocks` | Verbatim-reused section blocks/card grids across pages (the Mills tell) |

Cues 1–3 are Brian's named targets (2026-06-10); 4–8 come from documented v1–v3
evidence quotes.

## Sample — 16 sites, stratified from the 6/10 ground-truth snapshot

Ratings from [`../2026-06-10-design-rating-ground-truth/ratings.csv`](../2026-06-10-design-rating-ground-truth/ratings.csv)
(scorer-side only — **never shown to evaluators**).

- **Known cue-bearing (5):** Jinfiniti 3 · Anazao 2 · Mills 4 · Infusive 2 ·
  Pepti 6 — Brian's defect descriptions already on record (seed labels in the
  answer sheet).
- **Fresh low band (6):** Kingsberg 2 · MaleMD 3 · Defy Medical 3 · HormoneMD 4 ·
  Brello Health 4 · Strut Health 4 — defects expected dense; tests recall.
- **Mid control (1):** Amble 7 — v3's upward-miss case; tests whether cue detection
  stays clean on a site whose *pricing* seduced raters.
- **High controls (4):** Function 10 · Healthspan 10 · Hims 9 · Hone 8 — defects
  expected absent; tests precision (false-positive guard).

All 16 verified present in the store with non-archived capture PNGs (checked
2026-06-10). Zero Firecrawl.

## Conditions — downsampling arm folded in

- **A (default):** existing full-page screenshots, read as-is (v3 method).
- **B (native-res tiles):** full-page PNGs sliced into viewport-height tiles
  (~1080px, 10% overlap) by a deterministic Python step before the run — a
  1920×10k full-page PNG downscales ~7× in the vision pipeline, which is exactly
  where charts and icons vanish.
- B runs on 4 sites only: **Jinfiniti** (the missed-charts case), **Infusive**
  (the +2.5 miss), **Strut Health** (fresh low-band, dense pages), **Function**
  (clean high-res control). 16 A + 4 B = **20 evaluator calls**.

## Evaluators

One **Sonnet** agent per site×condition (v3: Sonnet ≥ Opus here, and this is
perception, not judgment). No rater redundancy — v3 already proved inter-rater
agreement (max 1-bucket spread); re-proving it was the bonfire. Blinding inherits
v3's hard rules: no `profile.md`, no `experiments/` reads, no web/Notion/Firecrawl,
no prior-knowledge use — plus new: no ratings CSV, no overall verdict, identical
cue checklist for every site (no per-site steering).

Output schema per evaluator (YAML): per cue → `verdict`, `evidence`
(file + region + what), `confidence`. Nothing else.

## Ground truth & metrics

**Brian's answer sheet** ([`brian-cue-labels.md`](brian-cue-labels.md)): 16 sites ×
8 cues, tick present/absent/unsure — pre-filled where v1–v3 quotes exist (marked,
confirm don't inherit). Must be completed **before reading any agent output**
(~10 min). Scoring is a deterministic Python script (auditable, re-runnable):

- **Per-cue precision/recall** vs the answer sheet (`cant-tell` reported separately).
- **Discrimination (free check):** mean detected-defect count, low band (≤4) vs
  high controls (≥8) — should separate cleanly.
- **Downsampling delta:** cues B finds that A missed on the 4 dual sites,
  validated against the answer sheet.

## Pass bars & decision rules (set before the run)

1. **A cue graduates** at precision ≥ 0.8 AND recall ≥ 0.6, with ≥ 4
   Brian-positive examples in sample. Below that = unreliable; failing even in
   condition B = **blind** (recorded, so future sessions stop pretending to see it).
2. **Tiles become standard** if B surfaces ≥ 1 Brian-confirmed cue that A missed
   on ≥ 2 of the 4 dual sites.
3. **Experiment-level:** ≥ 3 cues graduate → v5 builds the deterministic scorer
   (Brian-weighted cue counts → quality read; validate against the remaining ~108
   rated sites cheaply). < 3 graduate → fall back to the v3 design-frame option:
   evidence-only capture, bucket left to the consumer; stop model-rating work.

## Cost shape (stated per the 6/10 right-sizing rule)

1 deterministic tile step (no agents) → **20 Sonnet evaluator calls** (each ~10–25
images + small YAML out) → deterministic scoring script → 1 short synthesis in the
lead session. No Fable subagents anywhere. Roughly an order of magnitude under
v3's 24-full-evaluator run; $0 Firecrawl.

## Not testing (scope fence)

Bucket calibration (v3 closed it), inter-rater agreement (v3 proved it), anchored
placement (superseded by this decomposition — revisit only if cue detection works
and the scorer still needs a holistic term), copy quality, IA/navigation clarity.
