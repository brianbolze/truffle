# Site presentation quality v3 — bottom-heavy calibration

Date: 2026-06-09

## Objective

First test of the scale's floor. v1/v2 calibrated on a sample whose lowest Brian rating was 4; the stated purpose of the convention (downgrade clearly weak/amateur sites) had never been tested. v3 ran 8 companies — 5 fresh bottom-heavy captures (no profile.md existed, so zero prose contamination) + 3 known-range controls — with 3 independent blind raters each (2 Opus + 1 Sonnet), reading raw capture artifacts directly (no lead-built packets, addressing a v2 limitation). 24 evaluators total, via a background workflow. No Firecrawl credits; no schema/profile changes.

Pass bar (from the design frame, Brian-agreed): every Brian ≤4 site reads basic-or-below · zero 2+-bucket misses · inter-rater spread ≤ adjacent.

## Result: FAIL — and the most informative run of the three

1/8 exact bucket matches (v1/v2: 6/9 each). Four severe (≥2-bucket) misses, all upward: Amble, Belmar, Mills, Infusive. Per-company detail: [`blind-ratings.md`](blind-ratings.md), [`comparison-to-notion.md`](comparison-to-notion.md), raw outputs in `agent-outputs/`.

The two criteria that *did* pass:
- **Inter-rater agreement** — max 1-bucket spread on every company. The raters agree with each other; they are collectively shifted, not noisy.
- **Relative ordering** — the blind median ordering (Function > Amble/Infusive > Belmar/Mills > Jinfiniti > Anazao/Kingsberg) is close to Brian's ordering except for Infusive. The scale *discriminates*; its anchors are wrong.

## The headline finding: a systematic ~1–2 bucket upward offset

23/24 individual ratings landed at or above Brian's bucket. `weak` was never issued — not once, including on two sites Brian rates 2. The failure is not random disagreement; it's a calibration offset: **agents anchor "coherent professional template" at `strong`, where Brian anchors it at `basic`.** Agents appear to rate against the universe of all websites (where a working template site beats the median); Brian rates against the contemporary DTC/health-brand bar.

The evidence text proves the agents SEE the right things — they just price them wrong:
- Anazao raters correctly identified "generic Wix-style template", "stock couple-in-a-field hero", "clip-art level iconography", a copy typo — and still said `basic`/`solid`, not `weak`.
- Mills raters correctly identified "off-the-shelf vendor template (Storey Marketing)", verbatim-reused card grids — and still said `strong`.
- The v2-derived calibration traps were quoted back in the cap notes ("coherent-but-generic is solid at most") and still failed to pull ratings down far enough. **Rule-tightening has hit its ceiling; the anchors themselves need recalibration.**

## The Infusive miss (+2.5, one `excellent`) — a new failure mode

Brian: 2.5, "really really poor aesthetics." Agents: excellent/strong/strong. All three were seduced by a *coherent dark-purple-gradient SaaS-template aesthetic* — sonnet even named it ("recognizable dark-SaaS/agency template aesthetic") and still said `strong`. This is v1's Pepti failure (distinctive-looking ≠ well-executed) at higher amplitude: a slick template system reads as art direction to a model, while a human with taste reads it as slop. Dark-gradient/"AI-startup" template aesthetics are now a known seduction pattern, distinct from the stock-photo/Wix pattern (which agents catch).

Secondary hypothesis, untested: full-page screenshots (~1920×8–12k px) get heavily downsampled at read time, hiding exactly the execution flaws Brian cites (Jinfiniti's "really amateur charts + illustrations" went unmentioned by all three raters). Native-resolution tiles might surface them.

## Other findings

- **Sonnet beat Opus on calibration** (mean +0.8 vs +1.6/+1.7 buckets) — uniformly ~1 bucket more conservative, which fit this bottom-heavy sample but undershot the top control. Both `excellent` false positives came from Opus raters. Cheaper ≠ worse here; conservatism ≈ calibration on this sample.
- **Raw-artifact reads (no packets) likely made things worse**: Amble went strong (v2, packets) → excellent×2 (v3, raw); Belmar solid → strong. The v2 lead-built packets, flagged then as a steering risk, may actually have been doing useful work — naming defects the evaluators otherwise under-weight.
- **Brian's prior ≠ Brian's rating**: he described the batch as "pretty crappy" but rated Jinfiniti 3 and initially banded two sites solid before settling at 3/2 — even the calibration target moves on re-look. Bucket-level, adjacent-tolerant remains the right precision claim; exact-match never was the bar.

## Recommendation

**Do not graduate.** No frontmatter field, no capture-workflow convention, not even the prose-line convention yet — an instrument that reads `basic` as `strong` would actively mislead the depth-gate use case (it would auto-deepen on template slop like Infusive).

**Next smallest experiment — anchored comparison instead of absolute rating ($0, same artifacts):** stop asking "rate this site" and ask "place this site against these anchors." Give evaluators 2–3 reference screenshots with fixed labels from Brian's own ratings (e.g. Function = excellent, Mills = basic, Anazao = weak) and ask comparative placement. Comparative judgment is more reliable than absolute for both humans and models, and the anchor set is a convention (a few image paths + labels), not infrastructure. Optionally A/B a native-resolution-tiles condition on Jinfiniti/Infusive to test the downsampling hypothesis.

If anchored comparison also fails to kill the offset, the honest fallback is the evidence-only output shape from the design frame: record the observable cues (which v3 proved agents produce accurately) and leave the bucket to the consumer.

## Limitations

- Brian's ratings for Infusive/Jinfiniti/Kingsberg were given mid-session (before seeing agent output, but after describing the batch as "pretty crappy" — his own prior was primed).
- Desktop full-page screenshots only; downsampling hypothesis untested in this run.
- One Sonnet rater per company — the Sonnet-calibration read is n=8 from a single rater slot.
- The 2.5 (Infusive) sits on the weak/basic boundary; its delta is counted conservatively as +2.5 against `strong`.
