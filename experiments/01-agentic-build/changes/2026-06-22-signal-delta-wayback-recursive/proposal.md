# Proposal: signal_delta Wayback Recursive Dir Loading

Date: 2026-06-22
Status: proposed
Source request: Brian asked to work on the Market Read Lab quick win: "`signal_delta` dir-glob should recurse for Wayback page-slug subdirs", using `agent-build-propose`.

## Required Fields

risk: medium
write_scope: `tools/signal_delta.py`, `tests/test_signal_delta.py`, `tools/signal_delta.md`, and `tools/BACKLOG.md` if the backlog item is closed or moved.
spend_stop: none. No live capture, network, Firecrawl, SerpAPI, SEC, or store mutation. Use synthetic test fixtures only.
acceptance_checks: `python3 -m pytest tests/test_signal_delta.py -q` passes; a new unit test proves `_load_envelopes()` loads JSON files recursively from nested Wayback page-slug directories while preserving deterministic sorted order; existing file-input and flat-dir behavior remains covered; docs mention recursive directory loading without changing the Signals contract.
escalate_if: implementation needs to change `scripts/signals.py` path conventions, alter `subject_of()` / Wayback subject identity, compare across pages as one aggregate, touch `store/` captures, or add source-specific CLI flags.

## Short Answer

Recommend the smallest viable fix: make `signal_delta.py`'s directory loader recurse for `*.json` files, add focused tests, and update the tool doc/backlog. This closes the known Wayback gap without adding a new comparator mode, path contract, or page aggregation layer.

The goal is simple: when a caller gives `signal_delta.py` two run directories that contain nested Wayback captures under `wayback/<page-slug>/<captured_at>.json`, the comparator should discover those captures and let the existing Wayback branch align by exact URL subject.

## Problem

`scripts/signals.py persist` now writes multi-URL Wayback captures under a nested path:

```text
store/<domain>/signals/wayback/<url-slug>/<captured_at>.json
```

`signal_delta.py` accepts a file or directory, but `_load_envelopes()` currently uses a non-recursive `path.glob("*.json")`. That means pairwise per-URL comparison works when the caller passes exact files, but a whole-domain run-vs-run comparison silently sees no nested captures. The tool backlog names this exact weakness.

This is not a Wayback comparison logic problem. The Wayback branch already aligns captures by `input.url`, keeps page grain, and emits per-page metrics. The defect is the generic loader failing to see valid envelopes in nested directories.

## Constraints / Non-Goals

- Do not change the Signals storage contract or Wayback page-grain subject identity.
- Do not aggregate multiple page URLs into a domain-level Wayback score or verdict.
- Do not special-case Wayback path names unless a generic recursive loader proves unsafe.
- Do not fetch, re-capture, or mutate `store/`.
- Do not broaden `signal_delta.py` into a discovery/indexing tool. It remains a local consumer over existing envelopes.

## Options

1. **Generic recursive loader.** Replace directory `glob("*.json")` with deterministic recursive discovery of `**/*.json`, while file input remains unchanged. Add tests with nested Wayback fixtures and at least one flat-dir fixture to guard existing behavior.

2. **Wayback-only recursive branch.** Detect directories containing `wayback/` and recurse only there, leaving flat behavior for other source types.

3. **Caller-side workaround.** Leave `signal_delta.py` unchanged and require callers to pass exact page files or pre-flatten run directories.

## Recommendation

Choose option 1.

It is the smallest change that fixes the real caller pain and matches the CLI's existing language that a directory is "a run = many captures." Recursive JSON discovery is source-agnostic, so it also helps any future nested source path without adding knobs. The comparator's alignment fence still prevents cross-source, cross-grain, and cross-subject false comparisons after load, so discovering more envelopes does not itself create blended or domain-level behavior.

Option 2 adds unnecessary path awareness to a generic loader. Option 3 preserves the footgun the backlog item exists to remove.

## Implementation Sketch

1. Update `_load_envelopes(path)` in `tools/signal_delta.py`:
   - file path: keep current single-file behavior;
   - directory path: load `sorted(path.rglob("*.json"))`;
   - keep the existing "holds no JSON envelopes" error for empty trees.

2. Add tests in `tests/test_signal_delta.py` using `tempfile.TemporaryDirectory()` or pytest/unittest temp paths:
   - nested Wayback run directories such as `runA/root/a.json` and `runA/sermorelin/b.json`;
   - prove `_load_envelopes()` returns both nested envelopes;
   - prove `compare(_load_envelopes(runA), _load_envelopes(runB))` produces separate page-grain Wayback rows by URL;
   - keep or add a flat-dir loader assertion so non-nested run inputs still work.

3. Update `tools/signal_delta.md` to state that directory inputs are recursive and can include nested page-grain captures.

4. Update `tools/BACKLOG.md` to close the recursive Wayback loader item, either by moving it to Graduated or trimming it from Tool hardening with a dated note.

## Review Notes

Risk is medium only because this changes committed tool behavior. The blast radius is intentionally small: no schema, no capture tool, no Signals path change, no live spend, and no store write.

The main review concern is whether recursive loading could unexpectedly pick up unrelated JSON files in a caller-provided broad directory. That is already partly true for flat directories, and the comparator fences by source type and subject after load. If proposal review thinks broad recursive input is too surprising, down-scope to option 2, but that should be a deliberate choice because it makes the loader more source/path-aware.
