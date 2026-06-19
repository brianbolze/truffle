# Consumer Review — Run 007: SEC EDGAR Funding Footprint

## Evidence verification (adversarial pass)

An independent verifier re-derived the read's facts from raw JSON. **Verdict: evidence-sound after
2 corrections, both applied to `read.md` + receipt during Loop 2:**

- **C1 (bucket split 6/1/3/10=20), C4 (collision rows), C5 (Form-D dates) — PASS** as written.
- **C2 — corrected.** The CIK dedup (niagenplus + truniagen → one CIK `0001386570`) is correct. But
  the issuer name needed both labels: `state.registered_name` is "Niagen Bioscience, Inc." (current)
  *and* the Form-D filer string is "ChromaDex Corp. (CDXC)" — i.e. public company ChromaDex (ticker
  CDXC) renamed to Niagen Bioscience. The read now cites both; the dedup conclusion is unaffected.
- **C6 — corrected.** `amount: null` is universal (the load-bearing "presence, never amount" claim
  holds). But `existence_only` is *not* universal — it flags `form_d` events only; public periodic
  filings (hims, Niagen) carry `material_filing`. The read overstated flag universality; now fixed.

Net: the read's *answer and judgments are unchanged*; two precision errors in supporting language were
caught and corrected before review sign-off. Adversarial verification did its job.

## Verdict

- **Valuable? Yes** — with a hard-ceiling caveat that limits its decision weight.
- **Why:** It delivers something hard to produce without the engine — a clean, integrity-graded
  footprint across 20 brands in one pass, false-positive signals stripped, plus a real
  entity-resolution finding (one issuer behind two Niagen domains) the domain-keyed store can't see
  on its own. State/Signal/Judgment separation is clean. The ceiling: 20/54 captured packs carry a
  SEC signal and every funding line is `amount: null`, so it's a *yes/no presence map for a minority
  of the cohort*, not a sizing/conviction read.
- **What the consumer can do now:** triage 20 brands into four buckets; avoid the name-collision trap
  (`maximustribe` 45 hits = zero filings); read Eden's 3-filing trail as the only serial-raise
  pattern; know Niagen is one issuer behind two domains; treat "not found" as not "unfunded."
- **What made it safer than generic Claude + web search:** match-quality triage
  (`form_d.match`/`is_vehicle`/`distinct_ciks`) is captured and machine-readable — not re-derived on
  the fly. Every confound the scout named was held. (And the one place the read *did* drift on
  supporting detail was caught by the verification pass, not shipped.)
- **Biggest limit:** the 20/54 floor. Cohort-level funding claims are over this subset; the ~34
  uncaptured packs are unknown, not absent. The read says this plainly.
- **Human follow-up needed:** none mandatory. Optional: capture remaining packs' SEC signals to raise
  the floor; approval-gate a live Form-D body re-fetch to attach amounts.

## Value diagnostics

| Signal | Evidence / gap |
|---|---|
| **Useful** | Yes. The 4-bucket table is a real decision aid and prevents a concrete naive error ("maximustribe is funded"). |
| **Judgment-ready** | Yes. Clean State/Signal/Judgment split; an agent can consume C1–C6 without reopening JSON. |
| **Sourced & cited** | Yes. All six claims trace to specific JSON fields + capture dates; the amount/existence caveat travels with every funding statement. |
| **Deep enough** | Partly. Deep within the 20-domain set; the 34-pack gap is stated upfront as a captured-floor ceiling, not buried. |
| **Fresh enough** | Yes. Captures 1–4 days old; no stale-signal risk. |
| **Kept / reusable** | Yes. One receipt captures the bucket classification; the run advances two live triage gates with a concrete 3rd sighting each. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Make AI safe to delegate to** | Yes. Named the confounds (collisions, `existence_only`, filing-date ≠ brand age) a naive agent would trip on. | — |
| **Compare a whole field** | Partly. Covers the 20-domain SEC slice well; 34-brand gap limits cohort claims. | Capture remaining SEC signals, or accept as slice-relative. |
| **Build on top without re-capturing** | Yes. Receipt + claim IDs reusable; the sec_edgar × trustpilot 2x2 can proceed from here. | — |

## Lens check

- **Strategist:** lands fast. Bucket table is glanceable; the Niagen one-issuer/two-domain finding is
  genuinely novel; "funding footprint is a *minority* signal in DTC telehealth" is a real market-shape
  read that survives the 20/54 ceiling (the pattern is lumpy either way).
- **Pantry / downstream:** clean ingredients — dates, CIKs, match grades, confound flags all present
  and separated from Judgment. One small gap: the CIK dedup is a word in a cell, not a structured
  dedup artifact, so a domain-join consumer could still double-count Niagen without reading the note.
  Acceptable for now.
- **First Contact:** trustworthy. "Not found ≠ never raised" and "collision ≠ funded" are explicit;
  the evidence chain (JSON → receipt → claim IDs → assertions) is reconstructable. `no_issuer_form_d`
  on hims could read as a gap to a newcomer — the read explains it's correct for a public-market
  issuer, but that note is buried in a table cell; surface it if this goes into a brief.

## Triage submissions

No new items. MRL-002 and MRL-008 each have a credible 3rd sighting, already submitted accurately in
run-notes. The Niagen CIK dedup is correctly logged as a `denominator-reconciliation` watch item
(consistent with MRL-001's posture), not a new item. The two verification corrections are evidence
*for* the adversarial-review step's value, not a new triage candidate.
