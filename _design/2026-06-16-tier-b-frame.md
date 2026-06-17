# FRAME — Tier-B capture hygiene for visual-evidence

Date: 2026-06-16 · Status: problem frame (not design) — hand-off to a fresh session. Solution shape deliberately out of scope. From a Brian wallow (this date) over the 06-15/06-16 dogfood retros.

## Short answer

Tier-B (`shoot.py`) re-renders a page in a real browser when the cached Firecrawl shot is unfaithful — grey WebGL hero, unloaded lazy media, mid-animation. It's also where nearly every rough run, and the one total failure, happened. The real problem isn't "handle cookie banners"; it's:

> **Reliably get a faithful, uncontaminated, correctly-indexed rendering of an adversarially-dynamic page — across any site — without ever silently emitting wrong tiles.**

The spine we landed on (Brian's calls, this date):

- **Faithful-first, clean-on-demand.** Render as-served; a *sighted agent* looks; clean *only* the pages it sees are contaminated — never preemptively.
- **Keep both views, labeled airtight.** As-experienced and cleaned tiles both persist; which-is-which must be unambiguous in filenames, `manifest.json`, and card `tile_path`.
- **Bias to over-clean, not over-exclude** — safe *because* the faithful original is kept and an agent compared.
- **Zero-touch.** No Brian per run, no per-site hand-tuned selectors; agents run the checks; Brian samples + we log what they catch.

## Why it matters

- Tier-B is the reliability bottleneck — the consent / scroll-lock / no-overview friction and the sandbox total-failure all live here.
- The hero is the most load-bearing visual evidence, and overlays sit right on it — so excluding contaminated pages discards the best evidence. Recovering it cleanly is the win.
- It's on the path to less human involvement: a Tier-B that's trustworthy-or-loud is what lets runs stop needing a babysitter.

## What makes it hard

- **"Clean" is a judgment, not a fact.** A cookie banner *is* what a visitor sees — evidence-vs-noise is a call made by the sighted look, not hardcoded.
- **Generic vs. safe.** Vendor-id lists and per-modal rules are brittle and over-fit to telehealth; generic mechanisms (blunt CSS hides, Escape-spam) risk *silently* hiding real content on unseen cohorts (energy / VC / aero). How generic can dismissal get before it harms?
- **Silent-wrong is the recurring villain.** A scroll-lock mislabeled tiles; a missing overview forced a montage hack that *manufactured* a false defect; blind miners can't catch a plausible misread. First duty: never *look* clean when it isn't.
- **Labeling is load-bearing, and we're bad at it.** Doubling the tile sets (clean + dirty) multiplies the path/label discipline that already bit us (niagenplus dangle, truniagen frontmatter). "Make this impossible to get wrong" is a primary design problem, not a detail.

## Non-goals

- Not 100% auto-coverage of every site — handle the cohorts in scope, **fail loud** beyond.
- Not a maintained vendor denylist (living infra; anti-Doro).
- Not pixel-perfect — "good enough for blind design mining."
- Not a design *card* for "ugly cookie banner" — that's a **capture-fact** in provenance / manifest. The sighted step records it; the blind miners never see it (blinding stays intact).
- Not replacing the blind-mining model — the sighted agent does QA / clean / spot-check; the *miners* stay blind and read only the clean tiles.

## Scope

Holistic — the whole capture → clean-tiles → evidence loop (`tile.py` overview, the QA gate, the exclude/caveat call, how it lands in `visual.md`) — but **`shoot.py` is where most of the change lands.**

## Open questions — for the design session (the "how")

1. **The generic dismissal mechanism + its probe.** [`reshoot.py`](../experiments/2026-06-16-tier-b-dismissal/reshoot.py) (Escape + dismiss-labels + attribute-hide, applied *before* tiling) worked on gethealthspan — but N=1. Validate across ≥3 diverse sites incl. a non-telehealth cohort before promoting into `shoot.py`. How generic, and what's the safe ceiling?
2. **The clean/dirty provenance schema.** The label convention across tile filenames, `manifest.json`, `visual.md` cards, and `qa_status`. The make-or-break detail.
3. **The scroll-lock fix.** Today's stopgap only *detects* + warns (`scroll_locked` in the manifest). The real fix needs to understand the mechanism (`scrollTo(0,0)` returned `y=12684`) and safely release the lock.
4. **`shoot.py` overview emission.** Give it the `overview-480w` `tile.py` already makes, so QA isn't blind on re-rendered pages (and the montage hack dies).
5. **The two-pass trigger + cost.** How the sighted look decides "clean this page," and the ~2× render cost on contaminated pages (only they pay it).
6. **Instrumentation.** Log what the agent flags / cleans / excludes (the mistakes-log) so zero-touch is *audited*, not assumed.
7. **Upstream dependency.** Captures don't store page `source_url` ([BACKLOG](../BACKLOG.md)) — Tier-B needs it; pair the fix. — **Resolved 2026-06-17:** `fc.py source_stamp` stamps each cleaned `.md`; Tier-B reads it.

Separate, parallel track (not this session): widen the spot-check scope; build the mistakes-log itself.

---

*This is the FRAME — problem-space only. The design pass (going wide on the mechanism, with a probe) is a separate session.*

<sub>**Sources** — the 06-15 / 06-16 dogfood retros ([`_design/retro/visual-evidence/`](retro/visual-evidence/)) · [`reshoot.py`](../experiments/2026-06-16-tier-b-dismissal/reshoot.py) (the gethealthspan dismissal prototype — experiment-grade, not committed code) · [`scripts/shoot.py`](../scripts/shoot.py) + [`scripts/tile.py`](../scripts/tile.py) · the module contract [`modules/VISUAL.md`](../modules/VISUAL.md) + skill [`skills/visual-evidence/SKILL.md`](../skills/visual-evidence/SKILL.md) · [`BACKLOG.md`](../BACKLOG.md) (page-`source_url` gap; overlay items). Authored 2026-06-16 from a Brian wallow.</sub>
