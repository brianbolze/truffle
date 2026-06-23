# Wayback telehealth SKU repeat — June 11 vs June 8 pilot

Run date: 2026-06-11. Exact re-run of the
[June 8 pilot](../2026-06-08-wayback-telehealth-pilot/README.md)'s 11-command set — 6 tenure + 5 diff
captures over the same 6 SKU/category URLs, identical `--from/--to/--context-lines/--max-diff-lines`
parameters, via `tools/wayback.py`. No credits spent (Wayback is keyless).

> SERP results measure occupancy/visibility (shelf-crowding); traction results measure movement.
> Neither measures demand.

## 30-second skim — what moved in 3 days

**Nothing moved.** Across all 6 URLs, the Internet Archive recorded zero new snapshots since June 8:
`first_seen`, `last_seen`, `snapshot_count`, and `first_seen_confidence` are identical on every
tenure capture. All 5 diffs selected the same snapshot pairs and reproduced identical text hashes
(`text_sha256` match on every side), so the June 8 content-change findings stand unchanged. The only
field that differs anywhere is `tenure_days` (+3 uniformly) — that is clock arithmetic
(capture-time minus `first_seen`), not archive movement.

A 3-day gap is short relative to Wayback crawl cadence; "no new snapshots" means the Archive didn't
crawl these pages in the window, not that the live pages didn't change. This pass cannot see live-page
changes — that would be a different surface (live capture), deliberately not improvised here.

## Detail — per page

Every figure traces to the paired JSONs (same filenames here and in the pilot dir) and
`diff-vs-june8.json` (mechanical pair-diff, produced by `diff_wayback.py`).

| Page | Tenure (June 11) | vs June 8 | Diff re-run |
|---|---|---|---|
| Amble Sermorelin | 4 snaps, 2025-08-05 → 2025-12-15, measured | no movement | same selection + hashes |
| Amble NAD+ | 5 snaps, 2025-08-05 → 2026-03-11, measured | no movement | both ranges: same selection + hashes |
| TRT Nation Anti-Aging | 1 snap, 2026-02-03, provisional | no movement | not run — still single-snapshot (mirrors pilot) |
| Rex MD Sermorelin | 2 snaps, 2026-02-12 → 2026-03-12, measured | no movement | same selection + hashes |
| Hone Health NAD+ | 12 snaps, 2024-09-21 → 2026-04-10, measured | no movement | same selection; the 2026 side reproduces the same noisy/compressed extraction as the pilot |
| Brello Sermorelin | 1 snap, 2026-05-03, provisional | no movement | not run — still single-snapshot (mirrors pilot) |

The two "not run" diffs match the pilot's scope: it ran no diff where only one snapshot exists, and
that state is unchanged.

## Run notes

- 11/11 commands completed, all `ok: true`, `schema_drift: []` throughout.
- `joinamble-nad-diff-20250805-20260311` needed a third attempt: attempt 1 died on a transient
  pyenv shim error ("version 3.11 is not installed" — environment noise, not the tool), attempt 2 hit
  a Wayback 504. Attempt 3 succeeded. All other commands succeeded first try with `--timeout 120` on
  diff mode (the pilot's lesson).

## Files

- `*-tenure.json` ×6, `*-diff-*.json` ×5 — raw `wayback.py` envelopes, filenames mirror the pilot
- `diff-vs-june8.json` — mechanical pair-diff vs the pilot (`diff_wayback.py`)

Signals only — interpretation belongs to the launch-package run and Brian.
