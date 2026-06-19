# Consumer Review

Question: **Was the read itself valuable enough for a human or agent to trust, reuse, or act on?**

## Verdict

- **Valuable? Yes.** One of the cleaner runs in the lab. It answers a question a strategist actually
  asks ("does price transparency behave like GLP-1 here?"), grounds every price in a dated capture,
  and surfaces a cross-category pattern (price-posture = business-model, not molecule) more useful
  than the original question. Adversarial Loop 2 review *strengthened* trust rather than eroding it:
  the one material error (Kingsberg miscategorized as fully gated) was caught and corrected from the
  brand's own captured file, and the headline finding (C3) survived.
- **Why:** The `offerings.md` `Visibility` column carried the whole read off disk — no re-capture, no
  spend — and the publish/gate posture reconciles independently with run 000's GLP-1 read.
- **What the consumer can do now:**
  - Quote the corrected **42 / 42 / 17** split (publishes / membership-floor / gated) in a brief, with
    the explicit caveat that generalist all-gender TRT lines (henry, lifemd, invigor, strut) are
    unscored and would move the ratios.
  - Treat **Defy + Marek** as a "high-touch clinic, intake-gated pricing" business-model tag — they
    gate the drug in *both* GLP-1 and TRT while publishing labs/consults loudly.
  - Use the "gaters publish labs, hide the drug" insight as a positioning angle for anyone entering
    clinical optimization.
  - Stage the men-only **ED/hair band** (price-forward) as a 30-minute store-only follow-up.
- **What made it safer / better than generic Claude + web search:**
  1. **Dated primary captures, not snippets** — every price ties to a named `offerings.md` with a
     2026-06-03…06-18 capture clock; source grade is "derived from captured company pages," not model
     memory or a live snippet.
  2. **Capture-gap vs intake-gate was enforced, not asserted** — the gaters are confirmed company-
     gated because their `site_notes` say so; and the one brand where that distinction was *fuzzy*
     (Kingsberg, prices live off-PDP on FAQ pages) got reclassified rather than rationalized.
  3. **Cross-run corroboration** — the two-category gater finding requires two independent reads of
     the same brands, which only a persistent store enables.
- **Biggest limit:** the denominator is a **12-brand working set, not a census**. A consumer skimming
  the "42%" headline could miss that generalist all-gender TRT lines are unscored. C3 (model-not-
  molecule) is the durable finding; the exact percentages are provisional. Secondary: the "publishes"
  band includes enclomiphene/SERM sellers (Vitality, Sermorelin) that aren't selling exogenous TRT —
  exogenous-T-only publishers are closer to ~3/10.
- **Human follow-up needed:** (a) score the generalist TRT lines to test whether the split holds;
  (b) decide whether enclomiphene/SERM brands get their own sub-band so future agents don't re-debate
  it; (c) confirm Marek/Maximus pricing isn't stale (A/B-volatile, but ≤16d).

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer, decision aid, or next step; not just a summary. | Yes — stratified answer + cross-category pattern + named brands by posture. |
| **Judgment-ready** | Fresh, rare, cited ingredients a human or system could reason from. | C3/C4 labeled as Judgments; everything else is State extraction. Labeling is clean. |
| **Sourced & cited** | Claims trace to dated captures / receipts. | Yes — per-brand file + capture date in the receipt; claim map ties each claim to source IDs. |
| **Deep enough** | Covers the intended set, not just examples. | For a first pass, yes; ED/hair band and generalist all-gender lines are acknowledged open gaps. |
| **Fresh enough** | Capture dates / stale assumptions visible. | Yes — captures ≤16d; A/B-volatile flagged for the two volatile brands. |
| **Kept / reusable** | Warm files that make the next ask cheaper. | Yes — the receipt is re-queryable; the three-gater (now two-gater) set and C3 are durable. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Yes — a cited price-posture cut across a cohort, reconciled to a second cohort. | Score the generalist all-gender TRT lines to close the denominator. |
| **Build on top without re-capturing** | Yes — `Visibility`-column grouping is shown to work off disk; downstream recipes can grep it. | Resolve/tag the enclomiphene-vs-exogenous-T edge so a downstream agent doesn't double-count. |
| **Five-second brief input** | Yes — the bottom-of-`read.md` market pattern is the right length and verbatim-priced. | Carry the denominator caveat on first use of the 42/42/17 figure. |

## Lens check

- **Strategist:** Gets exactly the second-cohort read they came for, with a falsifiable cross-category
  claim. Lands plainly; the percentages need a denominator caveat on first use.
- **The Pantry / downstream system:** Confirms `offerings.md`'s `Visibility` field carries price-
  posture reads without re-capture — a reusable ingredient. The enclomiphene/SERM ambiguity is the one
  edge a downstream agent needs tagged to avoid double-counting.
- **First Contact:** Readable, scannable receipt table; caveats present and not buried. The visible
  Loop 2 self-correction *increases* trust — it shows the pipeline catches its own errors.

## Triage submissions

No new items. Adds recurrence evidence to **MRL-002** (a State price-posture grouping recipe recurred
cleanly — `Visibility`-column read + business-model labeling) and **MRL-001** (cohort-boundary labor
recurred; the "model not molecule" finding depends on how the denominator is drawn). Evidence Log
entries appended to both in `triage.md`. No graduation, no implementation.
