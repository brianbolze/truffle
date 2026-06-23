# Wayback improvement research

Run date: 2026-06-08

## Frame

Objective: decide the smallest practical capture pattern for historical SKU/category page tenure and page-change evidence across DTC telehealth pages.

Constraints: exact or locally attested URLs, polite Wayback usage, resumable captures, raw JSON preservation, bounded human-review diffs, no large sweep in this pass. Page-change evidence is archive-content evidence only.

Non-goals: no dashboard, no SKU ledger, no full runner build, no market-share or demand inference, no attempt to infer launch dates from first archived dates.

Open questions:

- How many candidate URLs are in the first real cohort: 20, 100, or 500?
- Do we need only one baseline, or a recurring monthly/quarterly refresh?
- Which pages deserve expensive diff review: every page with 2+ captures, or only high-priority category/SKU pages?
- What operator time is acceptable for manually reading noisy diffs?

Continue evidence:

- Tenure mode completes cleanly or returns explicit `insufficient` states for most exact URLs.
- Retry rate is low enough that a bounded manifest run can finish unattended.
- Diff output is readable on a sampled subset and preserves selected snapshot dates, hashes, replay URLs, and enough SKU-specific text to help a human review.
- Failures are recorded as measurement state, not interpreted as page absence.

Stop evidence:

- Replay fetches repeatedly time out or return compressed/binary/noisy bodies.
- Diffs are mostly nav, promo, A/B, consent, or boilerplate changes.
- Human review cannot extract SKU/category-specific facts faster than current-page capture plus tenure can.
- Any proposed workflow starts turning archived page changes into traction, demand, market share, launch proof, or movement.

## Bottom line

Use `tools/wayback.py tenure` as the default historical signal. Add a thin manifest/resumable runner only when the URL list becomes larger than a hand-run batch. Keep diff as optional human-review evidence for selected pages, not a column that implies traction.

Small hardening to the existing primitive is worth doing before a cohort run. Firecrawl is useful for current pages and forward monitoring, not for cleaning historical Wayback evidence at scale. A browser-rendered Wayback approach should stay a one-off escalation path.

## Local evidence

The pilot found that tenure is compact and interpretable: first archived, last archived, distinct-content snapshot count, status trail, and confidence label.

The same pilot found that diff can be useful but unreliable at cohort scale:

- Amble pages produced readable SKU/page changes, but diffs were nav-heavy and sometimes truncated.
- Rex MD produced a readable diff with mostly promo/boilerplate changes.
- Hone produced a `fetch_ok:true` replay body that extracted as compressed/binary-looking text.
- TRT Nation and Brello had only one exact-URL snapshot, so diff was not measurable.
- Several calls needed retries or longer timeouts.

That supports "optional evidence note", not "traction signal".

## External docs checked

- Internet Archive's [Wayback CDX Server API](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server) documents exact URL matching by default, optional `matchType`, public fields such as `timestamp`, `original`, `mimetype`, `statuscode`, `digest`, `length`, bulk pagination/resumption, and collapsing.
- Firecrawl's [scrape API](https://docs.firecrawl.dev/api-reference/endpoint/scrape) supports multiple output formats including markdown, HTML, raw HTML, links, images, screenshots, branding, change tracking, and browser-like actions before capture.
- Firecrawl [billing](https://docs.firecrawl.dev/billing) is credit-based: scrape is 1 credit/page, map is 1 credit/call, enhanced mode and JSON extraction add credits, and HTTP error pages still consume credits.
- Firecrawl [change tracking](https://docs.firecrawl.dev/features/change-tracking) compares markdown from your team's prior scrapes of the same exact URL/tag. It is useful from the point you start monitoring; it is not a historical Wayback backfill.

## Path assessment

| Path | Solves | Cannot solve | Complexity | Runtime/cost | Failure modes | Evidence helped | Recommendation |
|---|---|---|---|---|---|---|---|
| 1. Improve existing Wayback primitive | Makes the one-URL primitive safer for diff review: better warning labels, clearer date selection, better fetch/text quality diagnostics. | Missing snapshots, Wayback replay latency, archived assets not captured, JS that was never stored, meaning/traction inference. | Low if limited to diagnostics; medium if adding render/extraction engines. | Free, but replay-bound. No new vendor cost. | Over-improving extraction can make archive noise look cleaner than it is; adding too many knobs makes the primitive less boring. | Historical evidence. | Continue, but only small hardening. |
| 2. Thin manifest/resumable batch runner | Polite scale: one URL/mode per output file, skip existing files, retry with backoff, bounded concurrency, run summary. | Does not improve replay quality or make weak diffs meaningful. Does not select/interpret SKUs. | Low to medium. Thin orchestration around `wayback.py`, not a new product surface. | Free source, but wall-clock heavy. Tenure can run with modest concurrency; diff should start lower and back off on timeouts, 429/503s, or rising latency. | Bad manifests, repeated timeouts, accidental aggressive loops, mixing failures with absence. | Historical evidence, especially tenure. | Continue when cohort size exceeds manual runs. This is the main next implementation candidate. |
| 3. Firecrawl or another scraping/rendering tool for cleanup | Current-page capture, screenshots, markdown cleanup, bot/JS handling, future change monitoring from our own baseline. | Does not create old snapshots. Does not fix Wayback's missing archived assets or prove historical content if scraping replay pages changes the replay surface. Firecrawl change history starts with our own scrapes. | Medium, plus vendor/API surface. | 1+ credits/page; enhanced/JSON add cost; errors still bill. Using it on archived URLs doubles dependency on Wayback plus Firecrawl. | Credit burn, cache/geo/body contamination, exact URL/tag mismatch, cleaner-looking but less auditable archive artifacts. | Current-page evidence and forward monitoring; weak for historical evidence. | Defer for historical Wayback. Use for current captures and forward monitoring only. |
| 4. Browser/rendered Wayback replay | Human-review screenshots of specific archived pages; may reveal rendered text hidden from raw HTML extraction. | Missing assets, broken replay JS, Wayback latency, bot/cookie overlays, unavailable captures, and interpretation risk. | Medium to high. Needs Playwright/browser harness, waits, screenshots, text extraction, visual QA, and throttling. | Free in vendor credits if local, but slow and fragile. Heavy on Wayback replay. | Blank/partial renders, replay rewrite errors, stalled pages, noisy screenshots, accidental heavy traffic to Wayback. | Historical evidence for isolated pages. | Defer. Use manually for a few important pages after tenure/diff flags them. |
| 5. Do nothing beyond tenure for now | Keeps the signal honest and cheap. Gets lower-bound page tenure into analysis without pretending to measure demand. | No content-change evidence except links to snapshots; misses useful page evolution facts. | None. | Fastest and lowest operator burden. | Underusing available archive evidence; reviewers may still overread first archived as launch date. | Historical tenure only. | Continue as default posture. Not enough if Brian wants human evidence notes on priority pages. |

## Recommended next step

Do two small things, in this order:

1. Harden `tools/wayback.py` diff diagnostics:
   - Add `selection.target_delta_days` for `--from` and `--to` so `--to 2026` visibly means nearest to 2026-01-01, not latest-in-2026.
   - Add text-quality warnings such as high replacement-character rate, suspicious binary/compressed-looking text, very low line count, non-HTML mimetype, or fetch status mismatch.
   - Keep the diff mechanical. Do not add semantic classification.

2. Add a thin runner only when there is a real manifest:
   - Input: CSV/JSONL with `id`, `company`, `url`, `mode`, optional `from`, `to`, and priority.
   - Output: one JSON file per row, plus a small run summary.
   - Behavior: skip existing outputs, bounded retries, sleeps/backoff, bounded/adaptive concurrency, diff lower than tenure, no matching or judgment.
   - Failure states: timeout, fetch_failed, no_snapshots, insufficient_snapshots, noisy_text, ok.

This is enough to run many URLs politely without building the ledger or dashboard.

## What to avoid

- Do not use Wayback diff as a traction, demand, market share, or launch proof signal.
- Do not scrape every archived replay page through Firecrawl just to make prettier markdown.
- Do not adopt Firecrawl change tracking as historical evidence. It is forward-looking from our first scrape.
- Do not add a SKU ledger, dashboard, or scheduler until a small manifest run proves the capture states are worth repeating.
- Do not hide failures. A timeout, binary replay, or one-snapshot page is a measurement state.
- Do not infer absence from no captures. It means not archived or not measurable at that exact URL.

## Decision

Continue with Wayback tenure. Continue with a tiny amount of primitive hardening. Add a thin manifest/resumable runner if the next step is a real telehealth URL cohort.

Defer Firecrawl for historical cleanup and defer browser-rendered Wayback at scale. Use Firecrawl for current-page evidence and possible forward monitoring from today's baseline; use browser rendering only for exceptional, high-value archived pages that a human actually needs to inspect.
