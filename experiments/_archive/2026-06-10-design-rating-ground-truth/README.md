# Web design rating — ground-truth snapshot (2026-06-10)

Frozen export of Brian's `Web design rating` from the Notion Organizations DB,
taken 2026-06-10 ~22:20 after Brian rated the complete set. **Notion is the live
home; this file is a point-in-time experiment artifact — don't edit, re-export.**

- [`ratings.csv`](ratings.csv) — all 125 orgs (name, rating, website, notion_id),
  124 rated; the only unrated row is Our Venture (Bolze LLC). Exported via the
  notion skill CLI right after its pagination fix (the CLI silently truncated at
  100 rows until this evening — earlier counts in session logs are floors).
- Distribution: 2:8 · 3:11 · 4:20 · 5:16 · 6:25 · 7:26 · 8:13 · 9:3 · 10:2.
  Bucket mapping from the v1–v3 experiments: excellent 9–10 · strong 7–8 ·
  solid 5–6 · basic 3–4 · weak 1–2.

## What it's for

Ground truth for **site-presentation-quality v4** (anchored placement — the next
experiment recommended by [v3 FINDINGS](../2026-06-09-site-presentation-quality-v3/FINDINGS.md)):
split into anchor set + blind holdout, with enough rated rows (124) to measure
calibration instead of eyeballing n=8. Also the drift reference — Brian's ratings
move on re-look (Amble was 6 in the v1–v3 controls, 7 in this snapshot), which is
exactly why experiments pin a snapshot instead of reading Notion live mid-run.

## Caveats that bind

- Single rater by design — the scale *is* Brian's taste against the contemporary
  DTC/health bar, not an objective quality measure.
- Most ratings were entered in one evening sweep (2026-06-10); a handful predate
  it (v1–v3 era). Re-look drift of ±1 is normal; bucket-level adjacent-tolerant
  remains the right precision claim (v3 finding).
