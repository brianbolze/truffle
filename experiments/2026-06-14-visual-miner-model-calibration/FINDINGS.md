# Visual-evidence miner model calibration — Sonnet vs Opus

Date: 2026-06-14

## Bottom line

**Sonnet miners hold Opus's calibration on the hardest case, so the plan is sound: default the four `/visual-evidence` miners to Sonnet and keep the judge on Opus.**

Tested on `goinfusive-com` — the dark purple-to-magenta gradient "seduction trap," the site most likely to bait a weaker model into reading gloss as quality. Ran the real `mine.workflow.js` twice on the **same 18 tiles**, identical args except `minerModel` (`sonnet` then `opus`); the judge inherited Opus in both runs. Compared the **raw miner cards** (pre-judge), because the constant Opus judge re-labels polarity and would mask miner differences if you only looked at accepted cards.

- **Sonnet did not get seduced.** On the gloss-exposed `color_brand_imagery` family it explicitly called the dark-overlay-on-stock-photo "a common shortcut," tagged stock photography mixed, and marked clashing product-UI / un-normalized logo strips poor. Its "strong" color cards are verifiable palette-discipline / accent-consistency claims, not gloss.
- **Sonnet ran slightly *more* conservative than Opus, not inflationary** — raw totals 14 strong / 24 mixed / 16 poor vs Opus 17 / 23 / 15. Both runs had exactly **one** true polarity-inflation rejection from the judge.
- **One caveat:** Sonnet over-generates near-duplicate cards, so the Opus judge does more merging (rejected 26/54 vs 18/55). Not an inflation problem — it's verbosity the judge absorbs. Worth one more company before defaulting if you want more than a single-case signal.

## Method

- **Change under test:** `skills/visual-evidence/mine.workflow.js` gained a `minerModel` arg that spreads `model:` onto the four miner `agent()` calls only; the judge call is untouched (arg omitted → miners inherit, original behavior). This arg is kept in the workflow as the plan's lever.
- **Tiles:** `python3 scripts/tile.py --slug goinfusive-com --pages homepage platform` → 18 tiles (8 homepage + 10 platform) under `store/goinfusive-com/captures/2026-06-09/tiles/` (gitignored; regenerate to reproduce).
- **Runs:** an A/B wrapper (`ab.workflow.js`) ran `mine.workflow.js` twice via `workflow()`, snapshotting `budget.spent()` between runs for clean per-run output-token attribution (sequential, shared pool).
- **Evidence captured:** `result.json` holds both runs' raw miner cards, per-family polarity tallies, and judge rejection lists.

## Results

### Raw miner polarity (strong / mixed / poor)

| family | Sonnet | Opus |
|---|---|---|
| typography_hierarchy | 4 / 5 / 4 | 4 / 6 / 4 |
| layout_composition_components | 3 / 7 / 4 | 5 / 5 / 4 |
| **color_brand_imagery** (gloss-exposed) | **6 / 6 / 2** | **5 / 6 / 3** |
| iconography_illustration | 1 / 6 / 6 | 3 / 6 / 4 |
| **total** | **14 / 24 / 16** (54) | **17 / 23 / 15** (55) |

Color is the only family where Sonnet leaned marginally more generous (6 vs 5 strong, 2 vs 3 poor) — exactly the seduction-exposed family — but the spot-check clears it. Sonnet was actually *harsher* than Opus on product-UI screenshots (Sonnet **poor**: "white/grey admin interface in hard contrast to deep-purple surfaces" vs Opus **strong**: "purple loupe callout ties the product shot back to brand accent"), and much tougher on iconography (1 strong vs 3).

### Judge pruning (Opus judge, constant both runs)

| run | raw | accepted | rejected | inflation rejects | duplicate/merge | overlap-or-unverifiable |
|---|---:|---:|---:|---:|---:|---:|
| Sonnet | 54 | 30 | 26 (48%) | 1 | 12 | 8 |
| Opus | 55 | 38 | 18 (33%) | 1 | 10 | 6 |

The extra Sonnet pruning is duplication and unverifiable cross-tile claims (e.g. "40/60 vs 50/50 split spans non-adjacent scroll positions"), **not** gloss-inflation. The one Sonnet inflation reject was a baseline typography claim ("a button bigger than a trust line is baseline"), not seduction by the gradient.

### Output tokens

| run | output tokens |
|---|---:|
| Sonnet (4 miners + Opus judge) | 36,225 |
| Opus (4 miners + Opus judge) | 42,705 |

Counts are close (~15% fewer) because the judge is a fixed Opus cost in both runs. The real credit lever is **price**, not count: the four miners' tokens bill at Sonnet's ~⅕ per-token rate. Output tokens are a proxy for per-company miner work; the cost saving lands on the miner share of every `/visual-evidence` run.

## Reproduce

```bash
# 1. regenerate the 18 tiles (gitignored)
python3 scripts/tile.py --slug goinfusive-com --pages homepage platform

# 2. temporarily re-expose raw miner cards: add `raw_cards: allCards` to the
#    return in skills/visual-evidence/mine.workflow.js (reverted post-experiment —
#    it was scaffolding, not part of the shipped contract). ab.workflow.js reads it.

# 3. run the A/B wrapper (background workflow); reads result from budget deltas
#    Workflow({ scriptPath: "experiments/2026-06-14-visual-miner-model-calibration/ab.workflow.js" })
```

## Decision / next

- **Go:** wire `minerModel: "sonnet"` as the default in the `/visual-evidence` caller; keep the judge on Opus.
- **Before fully trusting it:** one more company (Sonnet's duplicate-heavy output leans harder on the Opus judge's merge step — fine on one site, but a second case confirms the judge keeps absorbing it).
