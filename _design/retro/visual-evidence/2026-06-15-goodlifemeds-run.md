# Retro — Good Life Meds visual-evidence run (2026-06-15)

Second `/visual-evidence` run on a cached company (`goodlifemeds-com`). Landed clean: [`store/goodlifemeds-com/visual.md`](../../../store/goodlifemeds-com/visual.md), 16 cards, lint exit 0. Notable because it's the **mirror image** of the [Blokes run](2026-06-15-blokes-run.md) on the two open questions.

## Lesson 1 — Tier-B *was* the right call here (refining Blokes)

Blokes concluded Tier-B is overreach for cosmetic stitching artifacts the blind layer already discounts. True there — wrong rule to generalize. This capture had a **site-wide Transcend consent overlay** ("Your Privacy Choices") stamped into the corner of *every* tile and over real content (a homepage testimonial card). That's not a cosmetic band the miners shrug off — it's a recurring covered-content artifact on most tiles, so exclusion would gut the capture and mining-through risks the blind agents reading it as design. Tier-B re-render of all four pages came back clean; the artifact is gone, animations settled.

**The real discriminator** (both runs now agree): not "is there an artifact" but **does the contamination destroy evidence the page depends on, across enough tiles that exclusion isn't viable?** Blokes = no (one cosmetic band, cached fine). Good Life = yes (consent wall, every tile). The cached-vs-live tradeoff Blokes flagged still holds — but here the live re-render was *cleaner*, not worse, because the fix was to **kill the overlay**, not pray it didn't fire.

## Lesson 2 — click-dismissal loses to modern consent widgets

`shoot.py` already tried clicking consent buttons. It failed: the Transcend widget mounts a **closed shadow root** and **duplicates itself**, so `get_by_text` can't reach the button and a single click wouldn't dismiss both. The label I'd have needed (`Don't Allow`) also uses a curly apostrophe — `exact=True` would miss it anyway. Clicking is brittle. **Hiding the known vendor mount** (`#transcend-consent-manager` + OneTrust/Cookiebot/Didomi/etc.) via CSS is robust and generic. Shipped it to `shoot.py` — a capture-hygiene fix, not a signal change.

## Confirms two Blokes findings

- **Judge under-prunes (2nd data point).** 47 raw → judge accepted **38** (~81%), same as Blokes' 84%. Contract target is 8–14. I curated to 16 by hand again. Two runs, same gap — the soft "prune/merge" prompt needs a hard count ceiling. Worth the experiment now, not later.
- **Path duality (recurs).** Even launching from the Web Research repo, the workflow runs in the project cwd, so miners need **absolute** tile paths; rewrote to repo-relative when authoring. Belongs in SKILL.md.

## Net

Output: good, calibrated (color/packaging strengths cleanly split from below-fold finish slips). Process: Tier-B earned its keep this time and left `shoot.py` stronger. The judge ceiling is now a confirmed pattern — stop hand-curating, fix the prompt.
