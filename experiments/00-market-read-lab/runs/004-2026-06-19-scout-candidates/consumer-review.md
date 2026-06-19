# Consumer Review

Question: **Was the read itself valuable enough for a human or agent to trust, reuse, or act on?**

Start with the produced read: would a real Truffle consumer be glad it exists? Delighted by the result?

Truffle is the farm, not the chef: it should provide trustworthy company ingredients for human or downstream-system judgment. Use the diagnostics below after the verdict, not as boxes to fill.

## Verdict

- **Valuable? Yes** (for the captured-cohort question it actually answers).
- **Why:** The headline isn't the obvious "GLP-1 is crowded" — it's the **bolt-on
  pattern**: 41/53 carry a buyable GLP-1 SKU but only 19 anchor on it, so 22 brands
  attach GLP-1 to a different front door. That is a corpus-derived structural insight
  (front-door ∩ breadth), not something generic Claude + web search produces. The two
  cuts agree and the divergence between them *is* the finding.
- **What the consumer can do now:** Treat GLP-1 as the cohort's attach-everywhere line,
  not just the loudest storefront; read the "crowded middle" (peptides/longevity/TRT/
  ED/hair/HRT, 22–30) as one shared shelf stocked by the same multi-line platforms
  rather than distinct specialist markets. Both are usable as 5-second brief inputs.
- **What made it safer / better than generic Claude + web search:** Counts are derived
  from actual captured rosters with a claim map and capture clocks, and the run *threw
  out* its own first (wrong) answer — whole-file grep gave TRT/labs 53/53; it switched
  to a roster-cell match. A web-search answer would give vibes, not 41/19/22 with a
  reproducible method.
- **Biggest limit:** "Crowded *in the captured store*," not "crowded market." The cohort
  skews hormone/weight/longevity, so the **mental-health floor (10) is plausibly a
  capture artifact**, not market truth — the read says this, but it caps any
  whitespace/thinness reading a consumer might want to act on.
- **Human follow-up needed:** None to trust the read. To extend it: capture telehealth
  brands outside the hormone/weight/longevity skew to test whether "mental health is
  thin" survives a broader cohort.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer, decision aid, or next step; not just a summary. | Verdict-first, two agreeing cuts, one sharp non-obvious finding (bolt-on). Not a summary. |
| **Judgment-ready** | Fresh, rare, cited ingredients a human or downstream system could reason from. | Front-door + breadth tables + the 22-brand spillover list are reusable ingredients; judgments labeled `[Judgment]` inline. |
| **Sourced & cited** | Claims trace to dated captures, receipts, or store files; uncertainty is visible. | Receipt graded `derived`, C1/C2/C3 claim map, capture clocks stated, mid-band softness flagged. |
| **Deep enough** | Covers the intended company/source set, not just plausible examples. | Full gated cohort; all 53 DTC packs had ≥1 roster row (no enumeration-floor zeros). |
| **Fresh enough** | Capture dates, stale assumptions, or changed signals visible where they matter. | Oldest ~20d (telehealth) / ~16d (offerings), stated; fine for roster composition, no price/news claims made. |
| **Kept / reusable** | Leaves behind warm files, state, or receipts that make the next ask cheaper. | Receipt records the molecule regexes + the whole-file-grep anti-pattern — directly reusable by the next category read. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Yes, within the captured cohort — distinct-brand density per category, two cuts. | An external denominator to make it "market," not "store." Out of scope here. |
| **Five-second brief input** | Yes — "GLP-1 is the gravity well; the middle is one shelf" lands fast and is brief-ready. | — |
| **Build on top without re-capturing** | Partly — front-door cut is clean/normalized/queryable; breadth cut is query-time-derived, not stored, so a downstream system can't query it without re-running the molecule match. | A reusable category-grouping recipe (see developer review → MRL-002). |

## Lens check

- **Strategist:** Lands plainly and fast; the bolt-on insight is the kind that's hard to
  get elsewhere because it needs the roster corpus. Front-door cut is the citable one;
  breadth is a directional corrective — the read says so.
- **The Pantry / downstream system:** Front-door `anchor_category` is stable, normalized
  state another agent can join on. The breadth table is *not* persisted as queryable
  state — it lives only in this read + receipt, so reuse means re-deriving it. That's the
  reusability gap, and it's the developer-side pressure, not a consumer trust problem.
- **First Contact:** Yes — the run shows its work, discards its own wrong first pass, and
  never overclaims ("thin" = "few captured brands," never "thin market").

## Triage submissions

No consumer-side triage item. The one reusability gap (breadth cut isn't persisted
queryable state) is a developer-review concern and routes to MRL-002, not a new item.
