# FINDINGS — Tier-B generic dismissal probe

Date: 2026-06-16 · Gate for [`_design/2026-06-16-tier-b-approach.md`](../../_design/2026-06-16-tier-b-approach.md) · Harness: [`probe.py`](probe.py)

## In plain English (start here)

**The problem.** When we screenshot a company's site to mine its design, popups get in the way — cookie banners, "get 10% off" modals — and they sit right on the hero, the most load-bearing evidence. We need to clear them to get a clean shot, *without* accidentally deleting real parts of the page. This only matters in **Tier B**: the case where we re-render a page in real Chrome (because Firecrawl's cached screenshot came back broken). That's the only tier with a live browser to interact with.

**What I tried — two ways to clear a popup:**
1. **Click it away like a person would** — press Escape, click the popup's own "No thanks" / "Reject" / "Close" button. (I called this *affordance-only*.)
2. **Hide it by force** — find floating elements in the page and blank them out with CSS. (This is what today's `shoot.py` and the `reshoot.py` prototype lean on. Two flavors tested: *naive* = hide everything floating; *constrained* = try to hide only "banner-shaped" ones.)

**The answer.** Click-it-away won cleanly. Hide-by-force is where all the damage came from — on real sites it deleted navigation menus and would have wiped a real hero image, because **code can't reliably tell a junk popup apart from real page furniture** (they share the same CSS tricks). So the recommendation is: switch to click-it-away *only*, and delete the force-hide code. It's less code and safer.

The rest of this doc is the evidence a future implementer needs: the exact test matrix, both directions of failure, and the limits the probe couldn't reach.

---

## Verdict

**GO on affordance-only (click-it-away); NO-GO on any structural CSS-hide (force-hide).** Across 8 live re-renders (4 telehealth + 4 non-telehealth across VC / aero / energy / consumer), affordance-only — Escape + clicking the page's *own* dismiss buttons *scoped to overlay-shaped elements* + a scroll-lock release — cleared **5/5** dismissable overlays and **never** touched real content. **Every** content-harm event in the probe came from the force-hide layer. The pick is therefore a **net simplification**: drop the vendor denylist (`CONSENT_MOUNTS`) *and* the broad `[class*=cookie]` attribute-hide; keep only the click-it-away path.

## What was tested

Each site rendered live 4 ways in fresh browser contexts (no cookie carryover). For each, the harness captured a first-viewport screenshot + a structural overlay signature + the scroll state:

- **faithful** — warm-scroll + settle, no dismissal. The comparison baseline (what a visitor sees as-served).
- **affordance** — Escape×2 → click dismiss-labels (negative-first: "no thanks" → "reject" → "accept" → "close"/×) *only inside fixed/sticky high-z elements* → release scroll-lock + verify. **No CSS-hide.**
- **constrained** — affordance + force-hide of elements the detector classed `banner` (edge-pinned partial; never a top-nav strip, never full-viewport).
- **naive** — affordance + force-hide of *every* detected overlay (the dumb version).

Overlay classifier (structural, no vendor strings): a top-pinned full-width short strip = `nav` (keep); cover ≥ 0.6 = `fullscreen` (modal backdrop *or* a real splash — can't tell which); else `banner`.

## The matrix (the core evidence)

✓ = correct outcome · ✗ = broke real content

| Site | cohort | faithful overlay(s) | affordance (pick) | constrained | naive |
|---|---|---|---|---|---|
| gethealthspan.com | telehealth | "10% off" modal, full-screen, **scroll-locked** | ✓ modal cleared (clicked *decline*), lock released, top reachable | ✓ same | ✓ same |
| joinfridays.com | telehealth | `#cookie-consent-dialog` (custom CMP) | ✓ cleared (*accept all*) | ✓ | ✓ |
| mydrhank.com | telehealth | bottom cookie strip **+ sticky nav** | ✓ cookie gone (*reject all*), **nav kept** | ✓ nav kept | ✗ **nav hidden** |
| functionhealth.com | telehealth | Ketch banner + `#nav` + `.burger` | ✓ Ketch gone, **hero copy revealed**, nav kept | ✗ **nav hidden** (misclass) | ✗ nav hidden |
| sequoiacap.com | VC | fullscreen splash + cookie + header, **scroll-locked** | ✓ real homepage shown, cookie gone, **header kept** | ✓ header kept | ✗ **header hidden** |
| electra.aero | aero | sticky nav only | ✓ no-op, nav kept | ✓ no-op | ✗ **nav hidden** |
| sorafuel.com | energy | none | ✓ no-op (0-char Δ) | ✓ no-op | ✓ no-op |
| warbyparker.com | consumer | none | ✓ no-op | ✓ no-op | ✓ no-op |

**Scoreboard:** affordance-only — cleared 5/5 dismissable overlays, **0/8 harm.** constrained — **1/8 harm.** naive — **4/8 harm.**

Side-by-side montages (faithful │ affordance │ naive): `_montage-{gethealthspan,functionhealth,sequoiacap,mydrhank}.png`. Per-site raw signatures + screenshots in `probe/<site>/`.

## Both failure directions, measured

A good mechanism has to do two things: clear the junk **and** leave the real page alone. We tested both.

**Direction 1 — does it clear overlays?** Affordance cleared every dismissable overlay: a centered newsletter **modal** (gethealthspan), three different **cookie banners** including two custom CMPs the vendor list misses (joinfridays `#cookie-consent-dialog`, mydrhank bottom strip), a **Ketch** consent card (functionhealth), and a **fullscreen splash + cookie** combo (sequoia). On functionhealth, dismissing the Ketch card *revealed* the "Check your health." hero copy it had been covering (page text rose 15.8k→16.2k chars — content surfaced, not lost).

**Direction 2 — does it ever hide real content?** This is where the design turns:

- **affordance: zero harm in 8/8.** It only presses Escape and clicks the page's own dismiss controls — it has no mechanism to hide content. Sticky navs survived on all 4 sites that have one. The two no-overlay controls (sorafuel, warbyparker) had byte-identical faithful/affordance text.
- **naive: harmed 4/8.** It hid the real sticky nav on mydrhank, electra, and sequoia (header), plus functionhealth. **z-index is useless as a guard** — sequoia's `header` nav and its cookie notice are *both* z=9999; functionhealth's nav is z=200, *higher* than mydrhank's cookie banner (z=100).
- **constrained: harmed 1/8.** The "only hide banner-shaped" guard still nuked functionhealth's top nav, because the classifier mis-tagged `#nav` (z=200) and `.burger` (cover 0.255) as `banner`. **A structural classifier safe enough to ship is exactly the brittle, over-fit surface the frame rejects** — and it cleared nothing affordance hadn't already.

The crown case is **sequoia**: its `ink__content fullscreen` (cover 1.0, z=9999) is the *actual* "Ad Astra, SpaceX" landing splash — real content, not an overlay. Affordance left it alone (the splash auto-completed to the real homepage; the cookie was clicked away; the header stayed). Naive would have classed any fullscreen high-z element as a backdrop and hidden it — the precise "silently hide real content on an unseen cohort" failure the frame names.

## What the probe could NOT see (honest limits — read before implementing)

1. **No tested site had a banner with no dismiss affordance.** Every overlay was cleared by clicking its own control. A banner with unrecognized button text *and* no Escape handler would slip affordance-only → it must **fail loud** (exclude/caveat that page), never silently-wrong. This is the intended safe ceiling, not a gap to patch with a denylist.
2. **The forced scroll-lock release was never exercised.** Both locked pages (gethealthspan, sequoia) unlocked themselves *when the overlay was dismissed* (`bodyOverflow: hidden → visible` followed the dismiss click). So the real scroll-lock fix is **"dismiss, then re-verify the existing detector"**; the explicit `overflow/position` reset stays an unproven belt-and-suspenders fallback for "locked but un-dismissable," which didn't occur here.
3. **Label list is English-only and finite.** A non-English locale or an off-list label ("Sounds good") would miss; partly covered by Escape + `aria-label*=close` / × matching, but a real boundary.
4. **Click side-effects are contained, not proven impossible.** functionhealth fired 3 `close(x)` clicks with no harm (overlay-scoping held), but a mis-scoped click could in principle navigate or submit. The kept-faithful-view + agent-compare safety net (not the mechanism's precision) is what makes this acceptable.
5. **Live ≠ capture-time.** functionhealth showed a Ketch banner live that the capture-time retro never saw (geo/UA/timing). The probe validates the *mechanism*, not that the same overlay appears at any given capture moment.

## Implication for the design

Affordance-only is **simpler, safer, and more generic** than the status quo (it cleared two custom CMPs the vendor list misses) — and it makes the force-hide layer's risk unjustified, since that layer cleared nothing extra. Promote affordance-only into `shoot.py` behind a `--dismiss` flag (faithful stays the default); keep both tile sets when an overlay is dismissed. Detail + the shoot.py diff: [`_design/2026-06-16-tier-b-approach.md`](../../_design/2026-06-16-tier-b-approach.md).
