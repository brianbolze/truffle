# GPT-5.5 visual quality example mining

Date: 2026-06-13

## Objective

Test whether GPT-5.5 can mine **specific, inspectable examples** of strong and poor
marketing-site visual presentation from cached Web Research screenshots.

This is not another absolute site-rating pass. v1-v3 showed that models often saw
the right visual defects but priced them too generously. This run tests the more
useful layer: whether the model can retrieve concrete visual tells that support a
calibrated visual-quality rubric.

## Method

- Use cached store screenshots only.
- Treat screenshot health as part of the experiment. Contaminated screenshots are
  recaptured or excluded before model evaluation.
- Do not read `profile.md`, live websites, Notion, Firecrawl, or company prose.
- Slice selected full-page screenshots into native-resolution tiles.
- Give GPT-5.5 agents PQR-style dimensions and calibration rules:
  - default down when uncertain
  - generic/template competence is not high quality
  - one visible tell per claim
  - distinctiveness and finish are separate from mere effort
- Fan out agents by evidence family:
  - iconography / illustration
  - typography / hierarchy
  - layout / composition / component finish
  - color / brand system / imagery

## Pass Bar

- At least two strong and two poor usable examples for each major evidence family.
- Every example cites a screenshot or tile path and a visible region.
- No vague claims such as "premium", "modern", or "professional" without a tell.
- Known traps are handled explicitly:
  - coherent B2B template does not equal strong design
  - distinctive-looking long pages can still be unfinished
  - dark-gradient SaaS/AI-style surfaces can be template slop
- Output should become a reusable taste-calibration library, not a score table.

## Screenshot Health Notes

- The first agent run was aborted because several screenshots were visibly
  contaminated by failed media or overlays.
- Function Health homepage was excluded from the clean tile manifest after multiple
  Firecrawl recapture attempts rendered the real hero media as a flat grey block.
  Function pricing/scans remain in scope.
- A later follow-up found a patched Firecrawl workaround for Function's homepage:
  inject the site's own hero poster when Firecrawl hides the WebGL canvas. See
  `FIRECRAWL-WORKAROUND.md`. This was not part of the final agent evidence set.
- Belmar, Amble, and Pepti were recaptured on 2026-06-13 with targeted actions to
  dismiss CookieYes, Transcend, and custom cookie UI respectively.
- Current agent evidence should cite paths under `tiles-clean/`, not the original
  `tiles/` folder.

## Files

- `raw/build_tiles.py` - deterministic crop builder
- `tile-manifest.json` - machine-readable tile inventory
- `tile-manifest.md` - human-readable tile inventory
- `AGENT_PROTOCOL.md` - instructions given to GPT-5.5 evidence agents
- `agent-outputs/` - agent final outputs captured by the lead session
- `FINDINGS.md` - final synthesis
