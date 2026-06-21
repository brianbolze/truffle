# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Partly** — high *builder/strategist-calibration* value, modest *market-fact* value.
- **Why:** The run's headline ("the schema gates investors out correctly but offers no
  positive shape; `query-time-grouping-enough` is FALSE for the finance reader") is a
  genuine, decision-grade calibration a roadmap owner can act on. But as a *market read*
  ("how do these finance firms charge?") the answer is mostly already-known: VCs don't
  publish fees, stripe is usage-based, runway quote-gates — a finance-literate reader
  knew this. The reach is in the **schema-fit diagnosis**, not the market facts.
- **Where Truffle added value:** It made MRL-015 concrete and *two-sided* for the first
  time — the subtractive investor gate is solved and working (O1), the additive
  capital-allocator field set is the open gap (O2), and it's the **first vertical where
  prose-only fails a recognizable cross-entity cut** (O3, "all seed funds," "all >$1B").
  That is a real, novel frontier finding.
- **Where Truffle added little or fell short:** The market-fact layer restates analyst
  common knowledge (n=9, 5/7 early-stage VC). A reader wanting an *actual* finance market
  comparison (fees, AUM, returns) gets "not on the marketing site" for 5/7 — true and
  correctly flagged, but thin reach.
- **What the consumer can do now:** A roadmap owner can decide MRL-015's additive half
  (build a capital-allocator field set, or leave it as prose) with concrete evidence; a
  strategist gets a clean 2-subtype split (7 allocators + 2 fintech products) and the
  gate-type data point (O4).
- **What made it safer than generic Claude + web search:** The verdict is grounded in the
  *store's actual contract* (TAXONOMIES rules, the 8-value business_model set) and the
  *captured* disclosure state, not a guess about how finance firms behave — it answers
  "what can Truffle see about these 9," which web search cannot.
- **Biggest limit:** n=9 and subtype-skewed (5/7 early-stage VC); the "no positive shape"
  gap could be a VC-cohort artifact, not a finance-wide truth. A second, more diverse
  finance cohort (asset managers / PE / banks / fintech infra) is needed to harden O2.
- **Human follow-up needed:** A judgment call on MRL-015's additive half — does a real
  downstream finance-cut consumer exist? If not, the anti-sprawl call (W1: prose, no new
  field) stands.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Decision aid, not just a summary. | **Yes** — a clean MRL-015 build/no-build calibration + a 2-subtype market map. |
| **Judgment-ready** | Fresh, rare, cited ingredients. | **Partly** — the schema-fit verdict is rare + cited; the market facts are common knowledge. |
| **Sourced & cited** | Claims trace to dated captures / contract. | **Yes** — every claim → profile frontmatter (store clocks) + TAXONOMIES/SCHEMA lines; receipt C1–C7; verifier PASS. |
| **Deep enough** | Covers the intended set. | **Yes for the slice** (all 9), but the slice itself is thin/skewed — flagged honestly. |
| **Fresh enough** | Capture dates visible. | **Yes** — per-profile captured_at; fee/AUM absence framed as market norm, not staleness. |
| **Kept / reusable** | Warm files for the next ask. | **Yes** — the denominator/census receipt is a reusable finance-slice field map. |
| **Shortfall mapped** | Names where Truffle couldn't support the answer. | **Strong** — the Gap Map table is the core deliverable; separates schema-can't from firm-didn't (S1). |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Partly — clean 2-subtype split, but no fee/AUM comparison possible (off-site for 5/7). | A non-marketing source family (SEC ADV / Form D / PitchBook) for real finance comparison. |
| **Build on top without re-capturing** | Yes — names exactly which finance facts are greppable (entity_type, industry) vs prose-only (stage, AUM, thesis). | Decide whether the prose-only facts earn a structured cut (MRL-015 additive). |
| **Five-second brief input** | Partly — "the store's finance vertical is 7 allocators + 2 fintech products; allocator fees are structurally off-site" is a clean brief line. | Thin n; don't over-generalize to "finance." |

## Lens check

- **Strategist:** Lands quickly; the 2-subtype split + "the site isn't a pricing surface"
  gate-type insight is the non-obvious part. The market facts are not novel.
- **The Pantry / downstream system:** Could consume the read's verdict on *what's
  greppable vs prose* directly — a useful map for any agent building finance cuts. Truffle
  judgments (the subtype labels, the gate-type framing) are clearly labeled as Judgment.
- **First Contact:** Would trust it — every count is store-derived and independently
  re-verified (Loop-2 PASS), absence language disciplined.

## Optional triage evidence

No new queue candidate from the consumer lens. The builder-side evidence (MRL-015 two-sided
confirmation) is submitted via the developer review. Value-miss noted as V1 in the ledger:
a clean store-only confirmation of "the obvious" (VCs don't publish fees) is low
market-reach even when the schema-fit diagnosis around it is high builder-value — the same
calibration as run-033 V1 (watches) and run-034 V1 (ads).
