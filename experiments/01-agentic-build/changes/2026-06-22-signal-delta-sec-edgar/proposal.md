# Proposal: signal_delta SEC EDGAR branch

Date: 2026-06-22
Status: implemented
Source request: Market Read Lab quick win #3 - add a narrow `sec_edgar` delta branch to `tools/signal_delta.py`.

## Required Fields

risk: medium
write_scope: `tools/signal_delta.py`, `tests/test_signal_delta.py`, `tools/signal_delta.md`, plus small references in `QUERYING.md` / `SIGNALS.md` if implementation changes the documented branch list.
spend_stop: none. Use inline fixtures only; no live SEC requests, paid APIs, web browsing, or store writes.
acceptance_checks: `python3 -m pytest tests/test_signal_delta.py -q`; `python3 -m py_compile tools/signal_delta.py tests/test_signal_delta.py`; `git diff --check` on touched files. If Ruff is available, run `python3 -m ruff check tools/signal_delta.py tests/test_signal_delta.py`. Fixture tests must prove: SEC subject alignment is scoped to `tool: "sec_edgar"` only; output does not surface `amount`, valuation, score, verdict, or cross-source reconciliation; capped-window churn is labeled as "not visible in this capture window" rather than negative movement; Form-D identity caveats from `form_d.match` survive even when no funding card is emitted. Test receipt lives in command output / implementation notes.
escalate_if: the branch needs live SEC fetches, a new Signal/card schema, amount/valuation inference, changes to `scripts/signals.py` persistence, or any cross-source funding reconciliation.

## Short Answer

Approve the smallest branch: teach `signal_delta.py` to compare two existing `sec_edgar.py` envelopes by issuer State and dated EDGAR event cards. Keep it factual, amount-free, verdict-free, and source-local. This closes the Market Read Lab gap without introducing a card layer, funding monitor, or new persistence shape.

## Problem

At proposal time, `sec_edgar.py` already emitted first-party funding Signals: ticker/exchange/CIK State, raw `form_d` identity-match data, `filings[]`, and factual `funding_signals[]` cards. But `signal_delta.py` had no source-aware branch for `tool: "sec_edgar"`, so repeat SEC captures fell through to the fallback: a named veto instead of useful movement.

The practical consequence was small but real. Market Read Lab runs could ask whether the Signals layer supported change-pulse or traction reads, but one of the free capital-signal sources could not at that point answer "what new dated SEC events became visible since the last capture?" That forced hand comparison or mislabelled the source as undiffable. The implementation receipt below records the shipped branch.

## Constraints / Non-Goals

- Do not fetch SEC data inside `signal_delta.py`; it remains a local comparator.
- Do not infer funding amount, valuation, round label, cap table, investor graph, or positive/negative traction.
- Do not reconcile SEC events with newsroom cards or other sources.
- Do not add a card schema, lint gate, SQLite lens, monitor, or stored derived delta object.
- Preserve the existing comparator shape: rows with `source_type`, `grain`, `subject`, `metrics`, `comparability_flags`, and `vetoes`.

## Options

1. **Small source-aware branch.** Add `sec_edgar` to the grain map and dispatch table. Align by stamped domain/subject, compare issuer State fields, compare `funding_signals[]` by factual content, and carry caveats for unconfirmed Form-D identity and capped newest-filings windows.
2. **Docs-only recipe.** Leave the fallback alone and document how to hand-compare two SEC envelopes. Lowest code risk, but it preserves the exact repeated manual comparison the comparator exists to remove.
3. **Broader funding/change layer.** Introduce durable funding cards or a cross-source funding delta over SEC + newsroom evidence. This may become useful later, but it crosses into schema/persistence/reconciliation and violates the quick-win scope.

## Recommendation

Choose option 1.

It is the smallest change that makes SEC EDGAR behave like the rest of the Signals comparator while preserving Truffle's evidence boundaries. The branch should report only axis-specific facts: State field changes, newly visible factual EDGAR cards, cards no longer visible in the capped capture window, latest visible event date, and Form-D match-state movement. Anything beyond that is a downstream Judgment or a separate, higher-risk packet.

Risk is `medium` because `signal_delta.py` is a committed tool future agents may trust, and a sloppy capital-signal delta would create false confidence. The risk is acceptable if fixture tests pin the no-amount/no-score boundary and the identity caveats travel with the row.

## Implementation Sketch

1. Add `sec_edgar: company` to `GRAIN`.
2. Update `subject_of()` only inside a new `if src == "sec_edgar"` branch to use `env["subject"]`, then `input.domain`, then `input.name`, canonicalized. Do not alter the fallback path for unknown tools.
3. Add helper functions that extract comparable issuer State and stable factual event summaries from `funding_signals[]`; explicitly omit `amount` and any verdict-like field.
4. Add `_level_sec_edgar()`, `_delta_sec_edgar()`, and `branch_sec_edgar()` following the existing Trustpilot/Wayback branch pattern.
5. Add fixture tests for:
   - new Form-D / filing card appears;
   - issuer State changes;
   - unconfirmed/multi-CIK Form-D caveats;
   - capped filings caveat;
   - Form-D identity caveats survive even when no attributed card is emitted;
   - no amount/valuation/score/verdict output appears in SEC delta event summaries;
   - unpaired SEC capture returns a level read.
6. Update docs only to reflect the branch and its boundaries.

## Review Notes

Proposal review focused on the right risks and found this approval-ready after narrow revision. The implementation reviewer should still check whether the event key is too strict or too loose: a strict factual-content key may show a re-parsed card as newly visible / no longer visible in this capture window if a citation or flag changes; a looser key may hide meaningful identity-match movement. Default to stricter output with clear caveats unless implementation review identifies a cleaner stable key.

Also confirm risk. If the reviewer believes adding any capital-signal branch changes Truffle's funding posture, revise or park; do not silently expand into a funding-monitor design.

## Implementation Receipt

Implemented 2026-06-22.

- Added the `sec_edgar` branch to `tools/signal_delta.py` with company grain, SEC-scoped subject alignment, issuer State comparison, dated EDGAR event comparison, Form-D identity caveats, capped-window caveats, and level-read support.
- Kept the branch source-local and amount-free: no live SEC fetches, no persistence changes, no card schema, no valuation/score/verdict output, and no cross-source funding reconciliation.
- Added fixture coverage for SEC subject alignment, new event/state movement, multi-CIK identity caveats without emitted cards, capped-window churn wording, amount/valuation/score/verdict exclusion, and unpaired level reads.
- Updated `QUERYING.md`, `SIGNALS.md`, `tools/signal_delta.md`, `tools/BACKLOG.md`, root `BACKLOG.md`, and the Market Read Lab notes that had named the branch as future work.

Verification:

- `python3 -m pytest tests/test_signal_delta.py -q` -> 23 passed
- `python3 -m pytest tests/test_signals.py tests/test_signal_delta.py -q` -> 34 passed
- `python3 -m py_compile tools/signal_delta.py tests/test_signal_delta.py` -> passed
- `git diff --check` on touched files -> passed
- `python3 -m ruff check tools/signal_delta.py tests/test_signal_delta.py` -> not run; Ruff is not installed in this environment.

Post-implementation review-change pass: no code changes requested beyond the revised-proposal guardrails. The remaining MRL-012 work is operational capture cadence and subject pinning; the SEC comparator branch itself is closed.
