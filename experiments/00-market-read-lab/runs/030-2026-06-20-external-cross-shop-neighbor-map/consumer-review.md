# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable?** Partly — as a builder instrument with three concrete consumer-facing outputs. Not as a direct cross-shop roster.
- **Why:** The run's load-bearing output is a source-quality map: it reached outside the corpus, measured each external source's recall against run 017's known Hone tiering, and returned a decisive negative. Neither source tested delivers a clean cross-shop signal. That verdict is cited, reproducible, and non-obvious — exactly the kind of finding a downstream system would get wrong without it.
- **Where Truffle added value:**
  - **AI-safety guardrail.** Exa `/findSimilar` looks like a cross-shop signal; the receipts prove it isn't. Hone's top-25 recovered `hormonemd` only (1/16 run-017 neighbors); all four Tier-1 substitutes were absent (C2). Common-name anchors returned name-collisions and mirrors — `hims` → bit.ly / HMS Holdings; `ro` → Roon / ro.am; `notion` → notion.so / Notion Korea / OneNote (C3, O1, S1). A downstream agent that uses `exa_similar.py` as a competitor enumerator would import this junk silently. The run makes that dangerous use case receipted and avoidable.
  - **Run 017 corroborated, not overturned.** Comparison pages independently named 4 of 017's 16 Hone neighbors — including 2 of 4 Tier-1 (Lifeforce, Defy Medical) plus Maximus and Peter MD (C6, O3). The store-only read wasn't fabricated; it holds as the trustworthy substrate.
  - **Concrete capture worklist.** Five store-absent cross-shop nominees: Numan, Male Excel, Fountain TRT, Viking Alternative Medicine (Hone/TRT), Sesame (Ro/GLP-1) (C8, O2). Demand-side leads, not verified — but real names from real pages that can feed `/research-company` captures.
  - **Cross-vertical boundary on a dormant tool.** Exa quality tracks anchor-name distinctiveness, not market structure — `posthog` returned real rivals; `notion` returned mirrors (C4, S1). That boundary holds across both verticals and is the sharpest single generalizable finding.
  - **Numbers are verified.** The Loop-2 evidence verifier confirmed load-bearing counts (1/16, 36 store-absent hubs, 4/16, 0/5 nominees in store, ~$0.53 Exa spend) against the receipts; only two cosmetic wording fixes were needed.
- **Where Truffle added little or fell short:**
  - No clean "who does X actually cross-shop" answer a strategist can use in five seconds. The finding is "neither source works reliably" — a useful negative, but not a deliverable roster.
  - Comparison-page named sets are SEO-biased. Only 1 of 5 Hone result pages was a neutral third-party listicle; 3 were owned `/vs` pages; 1 was competitor-intel (C7, O3). Cross-source recurrence is the only usable filter.
  - The two weakest demand-side families were tested first. Neither review-platform "people also viewed" / search co-occurrence (W2) nor the owned-`/vs`-as-directed-edge (W1) — arguably the cleanest cheap signal observed — was exercised. The demand-side question is only partly answered.
  - 36 cross-anchor telehealth hubs (C5) are too aggregator/SEO-contaminated to serve as a roster without per-name inspection. No clean intermediate output.
  - The comparison-page recall (4/16) is a single calibration point on one anchor, not a distribution (G1 — no external source converts the substitute/adjacent judgment into a joinable fact).
- **What the consumer can do now:** trust run 017's store-only Hone tiering as the better substrate; treat Exa `/findSimilar` as a name-similarity signal only, use it only on distinctive-name anchors, always corroborate; queue the 5 nominees (C8) for human-approved `/research-company` captures; read comparison pages with the 3-of-5-owned-`/vs` self-selection caveat in hand.
- **What made it safer than generic Claude + web search:** the store baseline turned an open-ended "who competes with Hone" question into a falsifiable recall measurement. A naive web search would have reported the Exa neighbors and listicle names as "competitors"; this run could prove most were name-collisions and SEO self-selection because it had a cited ground-truth set to diff against.
- **Biggest limit:** the two untested cleaner sources (W1, W2) mean the verdict "no good external cross-shop signal" is provisional — it's "the two tested families are insufficient," not "none exist." Running W2 next is the cheapest way to close or extend the question.
- **Human follow-up needed:** decide whether to capture the 5 nominees (C8, O2); decide whether to fund W1 or W2 before concluding no clean demand-side cross-shop source exists.

---

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer, decision aid, or next step. | Strong. Decisive do/don't on two named sources, the store-only read re-confirmed as trustworthy, a concrete capture worklist, and named untested sources for next step. |
| **Judgment-ready** | Fresh, rare, cited ingredients. | Strong. Every named set graded *secondary lead*, never truth. The AI-safety guardrail (S1, C2, C3) is receipted and immediately usable by an agent-workflow designer. |
| **Sourced & cited** | Claims trace to dated captures, receipts, or store files. | Strong. C1–C10 trace to `receipts/exa/*.json`, `receipts/analysis-output.txt`, `receipts/comparison-pages-2026-06-20.md`. All captures dated 2026-06-20. Loop-2 verifier pass noted. |
| **Deep enough** | Covers intended company/source set. | Partial. Exa ran on all 23 anchors; comparison-page family on 3 only (budget-scoped, disclosed). The 4/16 recall is a single calibration point — flagged in Missing/Stale Coverage. |
| **Fresh enough** | Capture dates visible where they matter. | Yes. All Exa calls and scrapes captured 2026-06-20. No stale cache used. |
| **Kept / reusable** | Warm files, receipts for next ask. | Strong. `receipts/exa/*.json` (24 envelopes), `analysis-output.txt`, `comparison-pages-2026-06-20.md`, `analyze.py` all present. A future run can replay calibration against a larger store baseline without re-spending on Exa. |
| **Shortfall mapped** | Names what Truffle could not support. | Strong. Gap Map names both untested cleaner families (W1/W2), the single-anchor comparison-page sampling limit, and the fact that no source converts substitute/adjacent judgment into a joinable fact (G1). |

---

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Make AI safe to delegate to** | Yes — clearest consumer win. The guardrail is specific, receipted, and non-obvious: don't let a downstream agent treat Exa `/findSimilar` as a competitor list (S1, C2, C3, O1). | The positive complement — when IS Exa safe to use — is roughed out (distinctive-name anchors, C4) but not fully characterized. |
| **Compare a whole field** | Partly — disproved two ways of building a cross-shop comparison, kept run 017's store-only field-compare as the trustworthy one. The field-compare stays store-only. | Clean external cross-shop source remains unfound. Test W2 before declaring that door closed. |
| **Build on top without re-capturing** | Partly — tells a downstream system not to ingest Exa or listicle named sets as competitor facts (G1); receipts and calibration numbers are stable and re-queryable; 5 capture leads for corpus growth (O2). | Cross-anchor orchestration had to be hand-built (F1); a future external-neighbor read needs a recipe, not a one-off script. |
| **Five-second brief input** | Minimal for strategist output. "Store-only positioning beats the external panel; here are 5 capture leads" is brief-ready for a builder, not a creative director. | Run 017 remains the brief-ready substrate for Hone competitive context. |

---

## Lens check

- **Strategist:** lands as a falsified intuition — "just ask Exa / the listicles who competes with X" is exactly what the receipts disprove, with numbers. Non-obvious and clean. Too much setup to be a five-second brief input; best as context before choosing a research approach or approving a capture worklist.
- **The Pantry / downstream system:** correctly refuses to promote the noisy external named sets to ingredient grade. What it does promote: the labeled capture worklist (C8, O2), the Exa-safety guardrail (S1, C3), and the store-only calibration verdict. State/Judgment boundary stays clean throughout.
- **First Contact:** a new agent or analyst could trust this run — it shows its work (receipts), states a recall fraction it can re-derive, and holds the "not found in this panel" / "not a competitor" distinction throughout. Loop-2 verify pass adds confidence.

---

## Optional triage evidence

No new consumer-only triage candidate beyond what run-notes already surfaces. The three candidates in `run-notes.md` Optional triage evidence (MRL-011, MRL-008, MRL-009) cover the territory: MRL-011 gains a demand-side second sighting (O1, O3, G1); MRL-008 gains two new external-source confound flavors (S1, O1, O3, O4); MRL-009 has a concrete 5-nominee worklist (O2). The consumer-facing AI-safety guardrail (S1) is the same evidence as the MRL-011 entry — no separate row needed.
