# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable?** Partly — valuable as a calibration that cleanly maps a real limitation; not a value-read for a downstream consumer.
- **Why:** The run answered its own question cleanly ("discipline yes, queryable surface no") and named the structural cause. That's the right outcome for a gap-probe. But the primary deliverable is builder insight, not consumer ingredients — a Strategist or downstream agent cannot take "confidence is fragmented across five destinations" and act on a company.
- **Where Truffle added value:** The census (130/130 non-empty, 424 items, mean 3.26) and the six-kind taxonomy together give a builder a concrete map of what the honesty layer actually is versus what a reader might assume it is. The verbatim exemplars (alange inferred parent; blueowl self-reported AUM; gogeviti $399/$349 conflict; beta 188k/188.5k sq ft) show the high-value confidence signals *are* present, honestly written, and genuinely rare — they won't appear anywhere else.
- **Where Truffle added little or fell short:** A consumer asking "can I trust field X before delegating to an agent?" gets a structural answer — not actionable per-field guidance. The taxonomy is a derived heuristic Judgment layered on top of the store, not a captured field; a downstream reader still cannot grep "retrieve all inferred values" or "flag every conflict."
- **What the consumer can do now:** Know to read `unverified_fields` prose (not just check its presence) before delegating a captured fact. Know that "point-in-time snapshot, not fixed" is greppable but "inferred" and "conflict" are not. Know that absence of a caveat ≠ verified.
- **What made it safer / better than generic Claude + web search:** The census over 130 profiles is exact and local — no hallucination risk on counts, no latency, no spend. The verbatim exemplars are primary-source quoted, not paraphrased from search. The SCHEMA contract cross-reference (what each surface is *contracted* to mean) grounds the interpretation.
- **Biggest limit:** The taxonomy is a derived Judgment, not a captured field. The bucket shares (~48% completeness, ~12% inconsistency, ~11% inferred) are keyword-classifier estimates, not queryable store attributes — so the read's evidence for *why* confidence isn't queryable is itself not queryable. A second analyst running the same classifier would move bucket edges, though the headline claim (no greppable token for inferred/conflict) is robust.
- **Human follow-up needed:** None from this run alone. The deferred bounded-live follow-up (spot-check whether `unverified_fields` caveats have decayed since capture) remains out-of-scope and spend-gated. No triage graduation warranted until a real downstream consumer needs cross-store confidence filtering.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer, decision aid, or next step. | Yes for a builder: "no queryable confidence surface; point-in-time is the sole greppable token." Not actionable for a Strategist. |
| **Sourced & cited** | Claims trace to dated captures, receipts, or store files. | Strong — C1–C7 all cite local paths; receipt method is reproducible. Taxonomy shares correctly labeled as derived Judgment throughout. |
| **Shortfall mapped** | Names where Truffle could not support the answer. | Clean — the composability gap is named, the five fragmented destinations (C6) are listed, the one greppable precedent (C3) is held up as the template for any fix. |
| **Judgment-ready** | Fresh, rare, cited ingredients a human or downstream system could reason from. | Weak for a consumer: the read is *about* the trust metadata, not about companies. No company-level ingredient is produced. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Make AI safe to delegate to** | Partly — the read audits the substrate this job depends on. Conclusion: an agent delegating to the store today must read full `unverified_fields` prose per profile; it cannot filter by confidence at query grain. | A prefix-token convention on `inferred:` / `conflict:` lines (W1) would close the gap; not graduated. |
| **Build on top without re-capturing** | Partly — a downstream system now knows which confidence signals exist (prose), which are greppable (point-in-time literal), and which require full-prose parse (inferred/conflict). That's a routing map, not queryable ingredients. | Confidence grain must be treated as per-profile prose read until W1 or equivalent graduates. |

## Lens check

- **Strategist:** Does not land as a company read — it's a meta-read about the engine. A strategist gets no novel company ingredients from this run. Value is entirely for the builder-facing roadmap.
- **The Pantry / downstream system:** Gets a clear routing map: "point-in-time" is greppable; "inferred" and "conflict" are prose-only; absence-of-caveat ≠ verified; five confidence destinations to check, not one. Useful to know before building a confidence-filtering query.
- **First Contact:** The run is traceable — census method is explicit, exemplars are verbatim-quoted, taxonomy limitations are flagged as derived. A new agent could reproduce the headline claim with the same grep/parse approach.

## Optional triage evidence

**Routing decision (Loop 1 deferred to Loop 2):** submit an Evidence Log entry to **MRL-008** (tag: `source-rigor`), not a new standalone item. Rationale: this is the meta-generalization of MRL-008's run-026 "bare field isn't self-describing" finding — the same structural gap now confirmed at whole-layer scope, not per-field. A new item for `confidence-grain` is warranted only after a second sighting (a downstream read that actively needs cross-store confidence filtering). Single sighting → hold at Evidence Log level, do not graduate.

The W1 prefix-token convention remains a recur-watch wish. No implementation proposed.
