# source_url capture stamp — backfill audit (2026-06-17)

One-shot migration paired with the forward fix (`fc.py source_stamp`). Closes the [BACKLOG](../../BACKLOG.md)
"captures don't store each page's source URL" weakness so Tier-B (`shoot.py`) reads the URL instead of
grepping body links (the functionhealth miss: grep pulled a `my.functionhealth.com` CTA, not `/pricing`).

## What ran

`backfill.py --apply` over `store/` (live captures, `_archive` skipped). Stamps the same HTML-comment
header `fc.py` now writes, recovered **only** from recorded `manifest.jsonl` data (last-wins
`name → sourceURL`, else `requested`) — no path reconstruction, since guessing the URL is the failure
the fix exists to kill.

| Result | Count |
|---|---|
| **Stamped** | **1270** (1258 git-tracked + 12 untracked new captures: linear-app, posthog-com) |
| Already stamped (skip) | 0 |
| Unrecoverable — name not in manifest | 77 |
| Unrecoverable — no surviving manifest | 16 |

## Verification

- **Pure prepend, zero body mutation:** `git diff --numstat` → every changed file = exactly 5 insertions, 0 deletions (6290 insertions / 1258 files).
- **Idempotent:** a second dry-run stamps 0 (all 1270 detected as already-stamped).
- **Bug case fixed:** `store/functionhealth-com/captures/2026-06-01/pricing.md` now carries `source_url: https://www.functionhealth.com/pricing`.

## The 93 unrecoverable (14 companies)

Early captures (2026-05-30/31, the 06-03 offerings-tournament variants) whose page names predate
manifest-recording, or date dirs whose manifest was pruned. Skipped, not guessed. The forward fix
stamps them on next `/research-company` capture; no action needed. Companies: apple-com (7), blueowl-com (7),
delighted-com (6), dovetail-com (6), eden-health (6), getpetermd-com (1), gong-io (9), hevahealth-com (1),
hims-com (14), honehealth-com (8), ivimhealth-com (1), maximustribe-com (19), nike-com (3), remedymeds-com (5).

`backfill.py` is a kept audit trail; the migration is one-shot and need not run again.
