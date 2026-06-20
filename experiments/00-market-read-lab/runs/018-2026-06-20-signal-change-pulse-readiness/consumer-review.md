# Consumer Review

Question: **Was the read itself valuable enough for a human or agent to trust, reuse, or act on?**

## Verdict

- **Valuable? Partly.** The readiness-verdict format is the right shape for this question and is genuinely informative — but the *data* it surfaces (Trustpilot velocity, Wayback archive-presence) is too proxy-confounded to act on as a market signal. The value is **system-diagnostic, not ingredient-delivery**.
- **Why:** This is the lab's first temporal/diff read; no prior run touched the freshness axis. The verdict is specific enough to drive an ops decision — "change-pulse is operable on two surfaces today, both as noisy proxies; the fix is capture-cadence-matched-to-refresh-rate + a `sec_edgar` branch; no new primitive." Reporting the raw deltas *without* that framing would be actively misleading (a "+66 reviews, +10/day" line reads as momentum but is paid-solicitation cadence).
- **What the consumer can do now:** Know exactly what a "trust the cache over time" read can and cannot deliver store-only today, and which 6 brands are the starting set for a cadence trial. Stop attempting SEC/SERP change-pulse until subject-identity + a delta branch exist.
- **What made it safer/better than generic Claude + web search:** Intrinsically store-only — no external tool can diff Truffle's own append-only snapshots. The differentiation test passes by construction.
- **Biggest limit:** Every delta-able metric is a proxy. Trustpilot `review_count` is `paid_profile`-confounded (solicitation, not sentiment) and the decision-grade surfaces (trust_score trend, review bodies) don't diff; Wayback's surface is archive re-crawl state, not page-content change, and 13/15 read delta=0. A Strategist can't do much with the outputs; a Pantry/steward can.
- **Human follow-up needed:** One steward decision — whether to stand up a light, per-source-tuned re-capture cadence for a small fixed subject set, and whether to add the `sec_edgar` delta branch. Both are ops/tooling, not schema.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Decision aid, not just a summary. | Yes — actionable readiness verdict + concrete next-step list (6 brands, the two tool/cadence gaps). |
| **Judgment-ready** | Fresh, cited ingredients to reason from. | Partial — deltas are cited & dated, but proxy-confounded; usable as system evidence, weak as market ingredient. |
| **Sourced & cited** | Claims trace to dated captures/receipts. | Strong — C1–C9, capture timestamps + gap_days on every delta; veto behavior documented; absence framed as "not found between captures." |
| **Deep enough** | Covers the intended set. | Now yes — after the Loop 2 wayback correction, all four signal types swept (the first pass missed Wayback). |
| **Fresh enough** | Capture dates / changed signals visible. | Yes — this run *is* the freshness probe; the refresh-rate-vs-cadence mismatch is the headline. |
| **Kept / reusable** | Warm files for the next ask. | Yes — receipt leaves the full diffable-subject map; the next freshness run starts from it. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Trust the cache over time** | Yes — delivered a calibrated verdict on exactly this job: operable as two proxy signals, not the decision-grade change a consumer wants. | A per-source cadence trial would convert the proxy into a real cross-cohort pulse. |
| **Build on top without re-capturing** | Partial — a downstream agent now knows what the signal layer can/can't diff, and what to avoid (SEC/SERP). | Subject-identity pinning before any SERP/SEC change-pulse. |

(Other jobs — cold-start, compare-a-field, five-second brief — not served; this is a system-readiness read, not a company/cohort read. Rows deleted.)

## Lens check

- **Strategist:** Lands plainly, but the *outputs* are thin for them — the 6-brand velocity spread can't support a momentum or competitive read while all six are `paid_profile`. The insight is the system diagnosis, not the numbers.
- **The Pantry / downstream system:** Strong. The run hands the next agent a clean "here's what's diffable, here's what to avoid, here's the confounds" map, with Truffle-side judgments (paid_profile = solicitation; onemedical −1 = API artifact) clearly labeled.
- **First Contact:** N/A — not a profile/offer read.

## Triage submissions

No new consumer-originated items. Endorses the developer-review submissions (new P2 freshness/cadence item; MRL-008 and MRL-001 Evidence Logs), which the developer pass sharpened. Consumer-specific note folded into the read: surface the 6 clean-velocity brands as the cadence-trial starting list (done in *What Would Change This Answer*).

**No graduation, no system change implemented.**
