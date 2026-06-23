# Blind review rubric

Score `Model A` and `Model B` independently, then compare pairwise.

## Scoring

| Dimension | Weight | What to evaluate |
|---|---:|---|
| Evidence faithfulness | 30 | Unsupported claims, exact volatile values, provenance discipline, correct `unverified_fields` |
| Coverage | 20 | Offering breadth, pricing visibility, model, audience, nav, credibility, visual read |
| Schema compliance | 15 | Valid frontmatter, exact closed-set values, required sections, module contract obedience |
| Synthesis quality | 20 | Concise, useful, reconciles pages, no generic filler, meaningful visual/strategic read |
| Page/capture judgment | 10 | If page-selection notes are present: good page choices, no guessed paths, durable site notes |
| Downstream usefulness | 5 | A consumer can answer practical questions from the artifact without re-reading raw evidence |

Use a 0-5 score per dimension, then multiply by weight.

## Hard Penalties

Apply after weighted score:

- -25 for any invented price, offer, founder, date, certification, or named partner.
- -15 for taxonomy values outside closed sets.
- -15 for a volatile claim with no packet-traceable source.
- -10 for hiding uncertainty that should be in `unverified_fields`.
- -10 for writing canonical `store/` files instead of candidate outputs.

## Mechanical pre-checks (not the judge's job)

Schema validity, required sections, and closed-set values are deterministic — `scripts/check_candidates.py` owns them, so the judge never spends attention (or bias) there. Both V1.1 sets currently pass clean, so the −15 closed-set penalty is informational unless a re-run regresses.

## Review Method

Judges read from `_out/blind/<sample_id>/A/` and `B/` only — never the `_out/<model>/` dirs (those names de-blind). Per sample:

1. Read only the candidate artifact first. Note what it appears to claim.
2. **Claim-trace (this is the faithfulness audit — do it exhaustively, not by impression).** Build a table: one row per *volatile* claim (price, date, count, certification, named partner, founder, ownership/pharmacy-model claim). Columns: `claim | packet source (file + line/quote) | supported? (yes / weak / UNSUPPORTED)`. A claim that can't be traced to packet text is `UNSUPPORTED` — it triggers the −25 fabrication penalty even if it "looks right." This table is the deliverable that survives stylistic un-blinding; do not skip it.
3. **Edit-burden list (counted — this is what the decision rule turns on).** List the concrete edits a human would make before promoting this candidate into `store/`, each tagged `severe` (fabrication, wrong closed-set value, misclassification) / `moderate` (missing supported offering, wrong visibility token) / `cosmetic` (prose/format). Report the counts. Fewer-and-lighter edits is the win condition, not prettier prose.
4. Score each dimension 0–5.
5. Run `DOWNSTREAM_QUERY_TEST.md` from the candidate only.
6. Decide per sample: `clear win` / `narrow win` / `split` / `no decision`.

## Required judge output (per sample)

For each sample emit: the A and B claim-trace tables, the A and B edit-burden lists with counts, the six dimension scores ×weight for each, hard penalties applied with the offending claim quoted, and the per-sample label. Keep it greppable — this feeds the aggregation below.

## Aggregation & judge self-bias (run after BOTH judge passes)

Two judges score the same blind pairs (one GPT, one Claude). After scoring, de-blind via `model_map.json` and compute, **per judge**, the mean (GPT-side total − Claude-side total) across samples.

- If both judges favor the *same* model, that model genuinely won — trust it.
- If **each judge favors its own model** (GPT-judge prefers the GPT candidate, Claude-judge prefers the Claude candidate), the split is self-preference bias, not signal. The honest estimate is the **average of the two judges**, and the gap is the bias magnitude — report it, don't resolve it by taste.
- **Adjudicate (Brian) only the disagreements that do NOT line up with judge identity** — those are the real contested calls. A disagreement that exactly tracks "each judge picked itself" is predicted bias, not a judgment call; don't spend a human read on it.
- Always hand-inspect: every `UNSUPPORTED`/−25 claim, and any candidate one judge scores high while flagging suspicious.

The headline number is **edit-burden (severe + moderate counts), not weighted score** — the weighted score is the tie-breaker, and `FINDINGS.md` reports winner *by dimension*, not just overall.

## Decision Labels

- `clear win` - one model needs materially fewer corrections before promotion.
- `narrow win` - better, but close enough that taste or downstream consumer may decide.
- `split` - one model is more faithful, the other more useful; identify the safer default.
- `no decision` - artifacts or packet quality prevent a fair read.
