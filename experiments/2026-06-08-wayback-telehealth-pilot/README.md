# Wayback telehealth SKU pilot

Run date: 2026-06-08

Follow-on decision note: [`../2026-06-08-wayback-improvement-research/README.md`](../2026-06-08-wayback-improvement-research/README.md) assesses whether to improve the primitive, add a thin runner, use Firecrawl/browser rendering, or stop at tenure-only. Short version: tenure is the default signal; diff stays optional human-review evidence, not traction.

## Frame

Objective: test whether the existing `tools/wayback.py` tenure and diff modes produce cautious, mechanical evidence of SKU/category page content changing over time.

Constraints: exact or locally confirmed URLs only, serial Wayback calls, one saved JSON output per successful command, bounded diffs, no scoring, no demand/traction inference.

Non-goals: no SKU ledger implementation, no dashboard, no cleaner, no launch-date inference, no sales/market-share claim.

Pilot URL set:

| Company | URL used | Local URL note |
|---|---|---|
| Amble Sermorelin | `https://joinamble.com/sermorelin-injections` | `store/joinamble-com/offerings.md` confirms `/sermorelin-injections`. |
| Amble NAD+ | `https://joinamble.com/nad-injections` | `store/joinamble-com/offerings.md` confirms `/nad-injections`. |
| TRT Nation Anti-Aging | `https://trtnation.com/anti-aging/` | `store/trtnation-com/offerings.md` confirms no per-SKU PDPs; anti-aging products are cards on this category page. |
| Rex MD Sermorelin | `https://rexmd.com/our-medications/testosterone-program/sermorelin/` | `store/rexmd-com/offerings.md` confirms this slug. |
| Hone Health NAD+ | `https://honehealth.com/longevity/nad` | `store/honehealth-com/offerings.md` confirms `/longevity/nad`. |
| Brello Sermorelin | `https://www.brellohealth.com/product/compounded-sermorelin` | Local capture uses the `www` exact URL. |

Continue evidence: readable multi-snapshot diffs that show page-content changes, with dates and selected snapshots preserved.

Stop evidence: one-snapshot pages, unreadable replay bodies, noisy/truncated boilerplate diffs, or changes limited to promotions/navigation.

## Results

| Page | Tenure result | Diff selection | Mechanical finding | Label |
|---|---:|---|---|---|
| Amble Sermorelin | 4 snapshots, 2025-08-05 to 2025-12-15, all 200 | `2023/2026` resolved to 2025-08-05 -> 2025-12-15 because no 2023 or 2026 captures existed | 2025-08 text already had the Sermorelin page and synthetic-peptide description. By 2025-12, the diff shows expanded anti-aging navigation and a plan table: 6 month `$135`, 3 month `$149`, 1 month `$159`. Diff is truncated and nav-heavy, but the SKU price-table change is readable. | usable |
| Amble NAD+ | 5 snapshots, 2025-08-05 to 2026-03-11, all 200 | Initial `2023/2026` selected 2025-08-05 -> 2025-12-15 because `2026` means Jan. 1. Corrected diff uses 2025-08-05 -> 2026-03-11. | 2025-08 text already had the NAD+ page. By the later snapshot, the diff shows expanded anti-aging navigation and a plan table: 12 month `$125`, 6 month `$167`, 3 month `$183`, 1 month `$199`. Diff is truncated and nav-heavy, but SKU price-table content is readable. | usable |
| TRT Nation Anti-Aging | 1 snapshot, 2026-02-03, 200 | no diff run | Exact category page is archived once only. Live local roster shows anti-aging product cards, but Wayback diff cannot compare this URL yet. | not enough snapshots |
| Rex MD Sermorelin | 2 snapshots, 2026-02-12 to 2026-03-12, all 200 | Adjusted to `--from 20260212 --to 20260312`; plain `--to 2026` would have selected the same February snapshot | Readable diff, but changes are mostly boilerplate: Valentine's Day promo became St. Patrick's Day promo; lab-work copy added an at-home lab-test-kit option. No SKU-specific sermorelin change appears in the bounded diff. | usable, low signal |
| Hone Health NAD+ | 12 snapshots, 2024-09-21 to 2026-04-10, all 200 | `2023/2026` selected 2024-09-21 -> 2026-01-04 | First side is readable NAD+ injection page text with membership/pricing copy. The 2026 side extracted as compressed/binary-looking text despite `fetch_ok: true` and `text/html`; the diff is not trustworthy for content comparison. | noisy |
| Brello Sermorelin | 1 snapshot, 2026-05-03, 200 | no diff run | Exact product page is archived once only. Tenure is provisional; diff not measurable yet. | not enough snapshots |

## Command outputs

Saved JSON:

- `joinamble-sermorelin-tenure.json`
- `joinamble-sermorelin-diff-2023-2026.json`
- `joinamble-nad-tenure.json`
- `joinamble-nad-diff-2023-2026.json`
- `joinamble-nad-diff-20250805-20260311.json`
- `trtnation-anti-aging-tenure.json`
- `rexmd-sermorelin-tenure.json`
- `rexmd-sermorelin-diff-20260212-20260312.json`
- `honehealth-nad-tenure.json`
- `honehealth-nad-diff-2023-2026.json`
- `brellohealth-sermorelin-tenure.json`

Failed/retried commands:

- First sandboxed Wayback call failed with DNS/network blocking; rerun with approved network access.
- `joinamble-sermorelin` diff timed out once at default timeout; rerun with `--timeout 120` succeeded.
- `joinamble-nad` tenure timed out once; immediate retry succeeded.
- `rexmd-sermorelin` tenure timed out once; immediate retry succeeded.
- `joinamble-nad-diff-2023-2026.json` is retained as a date-target caveat: it selected Dec. 2025 as nearest to Jan. 1, 2026. The corrected first-to-latest comparison is `joinamble-nad-diff-20250805-20260311.json`.

## Runtime implication

Wayback is not a fast interactive signal at cohort scale. In this 6-URL pilot, several calls took tens of seconds, and three commands needed one retry after timeout. The runtime bottleneck is especially visible in `diff` mode because it fetches raw replay bodies, not just CDX metadata.

Follow-on read: start with tenure as the default baseline, not a scheduled diff workflow. If the next step is a real cohort manifest, add only a thin resumable runner around `tools/wayback.py`: save one JSON per URL/mode as it completes, skip existing outputs, record failures as measurement states, and use bounded/adaptive concurrency. Tenure can likely run with modest concurrency because CDX metadata is lighter; diff should start lower because replay fetches are heavier, then back off on timeouts, 429/503s, or rising latency. Inspect only selected diffs after capture, and keep them as human-review evidence rather than traction.

Do not add scheduling until repeated captures have a clear consumer. A scheduler would help recurring monitoring, but this pilot only proves that page tenure is cheap enough to baseline and that diff is occasionally useful, slow, and noisy.

## Decision

Use Wayback tenure in the SKU ledger. It is compact and consistently interpretable: `first_seen`, `last_seen`, `snapshot_count`, and `first_seen_confidence`.

Do not make Wayback diff a traction column. Keep it as an evidence-status field or note, e.g. `wayback_diff_status` plus selected snapshot dates and a short `wayback_diff_note`. This pilot found useful content-change evidence on Amble, but also one-snapshot pages, a binary/noisy replay, truncated nav-heavy diffs, and low-signal promo copy. That is enough to justify optional human-review evidence, not a movement or demand signal.
