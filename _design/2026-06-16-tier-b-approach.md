# APPROACH — Tier-B capture hygiene: generic dismissal + labeling (v1)

Date: 2026-06-16 · Status: **design + probe complete; shoot.py change proposed, NOT merged.** Answers the [Tier-B frame](2026-06-16-tier-b-frame.md)'s open Qs #1–#4. Gated by an 8-site live probe — [`experiments/2026-06-16-tier-b-dismissal/FINDINGS.md`](../experiments/2026-06-16-tier-b-dismissal/FINDINGS.md). Out of scope (frame): the two-pass cost model (#5, sketched only), the mistakes-log (#6), the `source_url` upstream fix (#7, paired note only).

> **Synthesis note.** The frame's prototype ([`reshoot.py`](../experiments/2026-06-16-tier-b-dismissal/reshoot.py)) and today's `shoot.py` both clear overlays by *hiding* them — a vendor denylist (`CONSENT_MOUNTS`) plus a broad `[class*=cookie]` CSS hide. The probe says that hiding layer is exactly where the danger is: it caused **every** content-harm event and cleared nothing the safe path didn't. So v1 goes the *opposite* way — dismiss overlays through the page's **own** affordances (Escape + its dismiss buttons), hide nothing, and lean on the kept-faithful-view + agent-compare as the safety net. The result is **less** code than either prototype, and it drops a maintained denylist (an anti-Doro win).

## 30-second skim — the calls

- **#1 Dismissal → affordance-only.** Escape → click the page's own dismiss controls *scoped to overlay-shaped elements* → release any scroll-lock. **No structural CSS-hide, no vendor list.** Probe: 8 live sites (4 telehealth + VC/aero/energy/consumer), **cleared 5/5 dismissable overlays, 0/8 content harm.** The structural-hide alternatives harmed real navigation on 4/8 (naive) and 1/8 (even the "constrained" classifier) — including nuking Sequoia's actual hero splash and Function Health's top nav. z-index is no guard (Sequoia's nav and its cookie banner are both `z=9999`).
- **#4 Overview → ship it, it's free.** `shoot.py` emits an `overview-480w.png` like `tile.py` does. Kills the montage hack that *manufactured* a false double-render defect (functionhealth retro). Independent of everything else; lowest-risk win here.
- **#3 Scroll-lock → dismiss-then-reverify is the real fix.** In **both** locked cases the lock released itself the moment the overlay was dismissed (`bodyOverflow: hidden→visible`). So the fix is: dismiss, then re-run today's top-reachability check; only flag loud if it's *still* locked. An explicit `overflow/position` reset stays a guarded fallback — honest caveat: the probe never had to fire it.
- **#2 Labeling → reuse what exists; no tile-doubling on the common case.** A dismissed render is still `qa_status: recapture-used` + a `## Provenance` line naming the page; the manifest gains one `dismissed: bool`. The faithful comparison baseline is the **cached Tier-A payload** the QA gate already holds — so the common overlay-on-a-fine-page case needs **one** Tier-B render, not two. Two tile sets only when WebGL/lazy *also* broke the cached shot (rare).
- **Promote → GO, behind a `--dismiss` flag (faithful stays the default).** The change is a net simplification of `shoot.py`. Proposed as a diff/plan below; **not merged** — your review gates it.

**The through-line:** clear overlays the way a *visitor* would (Escape, "No thanks", "Reject"), never by guessing which fixed boxes are junk; keep the faithful view and let a sighted agent catch the rare miss. Dismiss, don't hide — and fail loud past the edge, never silently-wrong.

---

## #1 — The dismissal mechanism (the build)

### Going wide — the candidates

| # | Mechanism | Generic? | Clears | Risk to real content | Verdict |
|---|---|---|---|---|---|
| A | **Vendor-id denylist** (`CONSENT_MOUNTS`, status quo) | No — maintained list, over-fit to telehealth | Known vendors only | Low | **Reject** — failed 3 runs on custom CMPs; living-infra (anti-Doro) |
| B | **Escape-only** | Yes | Keyboard-aware modals | ~None | Keep as **layer 1** — necessary, insufficient (banners ignore Escape) |
| C | **Dismiss-label click**, scoped to overlays | Yes | Modals + banners with a button | Low *if* scoped; a stray click can mutate/navigate | **Core of the pick** (layer 2) |
| D | **Generic structural CSS-hide** (detect fixed/high-z, hide) | Yes | Anything overlay-shaped | **High** — hides nav/splash; no reliable structural guard | **Reject** — all probe harm came from here |
| E | **Affordance hybrid = B + C + scroll-release** | Yes | Everything in the probe | **None observed** | **PICK** |

The frame's safety reframe is what lets E win without being perfectly precise: *"bias to over-clean… safe because the faithful original is kept and an agent compared."* E barely needs that latitude — it only ever presses keys and clicks the page's own buttons, so it has **no mechanism to delete content**. D spends the entire over-clean budget on a guess (which fixed box is junk?) that the probe shows is unwinnable: nav, cookie banner, and real fullscreen splash are structurally indistinguishable (shared z-index, shared `position:fixed`, overlapping coverage).

### The mechanism (E), in order

1. **Escape ×2** — closes keyboard-aware modals. Near-zero content risk.
2. **Click dismiss-affordances inside overlays.** Find buttons/links/`[aria-label*=close]`/`×` whose text matches a negative-first label set (`no thanks` → `reject all` → `accept all` → `close`), **but only when an ancestor is `position:fixed|sticky` with `z≥1` or >4% coverage and is not a top-nav strip.** Click the first; re-detect; repeat ≤4×; stop when overlays clear. The overlay-scope is the guardrail `reshoot.py` lacked (it clicked matching text anywhere — a footer "Accept Terms" was fair game).
3. **Release scroll-lock + verify.** `scrollTo(0,0)`; if it doesn't land near the top (or `body{overflow:hidden}` / `position:fixed`), force `overflow/position/top` to their unlocked values, re-verify, and only `WARNING` to stderr if *still* locked.

Dropped vs. status quo + reshoot: the vendor-id list, the `[class*=cookie i]` attribute-hide, the always-on "Accept" click. The one arguable keep — a 1-line Intercom/chat-widget hide — I'd **also drop** (a chat bubble is a faithful capture-fact; the close-`×` match catches dismissable ones), but it's the cheapest thing to re-add if a run wants it.

**The safe ceiling (fail loud, not silently-wrong).** Affordance-only clears overlays that *have* a dismiss path. A banner with unrecognized button text *and* no Escape handler will not clear — and the right answer is the frame's: **exclude or caveat that page, loudly**, never reach for a denylist or a blunt hide. No probe site hit this, so it's an unmeasured edge, not a covered one (FINDINGS limit #1). English-only labels are the same kind of edge (#3).

---

## #2 — Clean/dirty provenance (the labeling, made hard to get wrong)

The frame calls this make-or-break, and the failure history (niagenplus dangle, truniagen frontmatter) is about *path/label discipline*. v1 minimizes new surface rather than adding a parallel labeled tile-tree:

- **No new `qa_status` value.** A dismissed render is Tier-B → `qa_status: recapture-used` (unchanged closed set). The `## Provenance` note already says "Tier-B re-render for pages X, Y"; it gains "…overlay dismissed on X (newsletter modal)." Dismissal is a **capture-fact**, exactly as the frame says — recorded in provenance/manifest, never a design card, never seen by the blind miners.
- **One manifest field.** `shoot.py`'s manifest adds `dismissed: true|false` beside the existing `source: "shoot"` and `scroll_locked`. That's the airtight which-is-which: a tile dir's manifest states whether dismissal ran.
- **The faithful baseline is usually free.** For the common case — a page that *renders* fine but carries an overlay — the **cached Tier-A payload is the faithful view** (it shows the overlay), and the QA gate already read its `overview-480w`. So: one `--dismiss` render → clean tiles in `tiles/<page>`; baseline for the agent's compare = the cached overview. **No second tile set, no doubling.**
- **Two sets only when contamination is combined.** WebGL/lazy broke the cached shot *and* an overlay is present → the cached payload can't be the baseline. Then render twice into sibling dirs: `tiles/<page>` (faithful, no flag) + `tiles/<page>__dismissed` (`--dismiss`). Cards cite the `__dismissed` tiles; the faithful set is the kept comparison view. `visualcheck.py` rule 2 already fails any card citing a missing/excluded path, so a dangle can't ship silently.

Why not always emit both (one browser session, faithful-tile then dismiss-then-tile)? It's tempting (atomic pairing, one page-load) but doubles tiles on **every** Tier-B render — including the WebGL-only majority where dismissal is a no-op (proven on functionhealth/sorafuel). The conditional above pays the doubling only on the rare combined case. *(This is the one call I'd most welcome your steer on — see go/no-go.)*

---

## #3 — Scroll-lock release

Today `shoot.py` only **detects** (`scroll_locked` in the manifest) and warns. The probe's finding upgrades the fix cheaply: **dismissal releases the lock.** Both locked sites — gethealthspan's modal, Sequoia's splash — went `bodyOverflow: hidden→visible` the instant the overlay was dismissed, so `tile-00` is the true top again. The change:

1. Run the affordance dismissal (which releases most locks for free).
2. Re-run the existing top-reachability probe.
3. If still locked, force the unlock (`overflow/position/top` reset) and re-verify.
4. `scroll_locked: true` in the manifest now means **"locked and release failed"** — a genuine loud flag for QA, not a tripwire that fires on every modal.

Honest caveat: step 3 never fired in the probe (dismissal always sufficed), so the forced reset is unproven belt-and-suspenders, not a validated path.

---

## #4 — Overview emission

`shoot.py` emits viewport tiles only; QA on re-rendered pages is blind-flying, and the hand-rolled montage workaround double-rendered a footer and *manufactured* a false defect (functionhealth retro). Fix: after tiling, `page.screenshot(full_page=True)` → `magick -resize 480x → overview-480w.png` (the recipe-time `magick` shell-out `tile.py` already uses; no new pip dep). One overview per page dir, matching Tier-A's shape, so the QA gate scans re-rendered pages the same way it scans cached ones. Smallest, most independent win — shippable even if #1 is deferred.

---

## The shoot.py change (proposed — review before merge)

A net **simplification**: remove the denylist + always-on consent click; add the affordance path (flag-gated), the overview, and the smarter scroll-lock. Sketch, not a merged patch:

```
# remove:  CONSENT_LABELS, CONSENT_MOUNTS, the for-label click loop, the intercom/CONSENT_MOUNTS add_style_tag
# add CLI: --dismiss (store_true, default False)  → faithful render stays the default

def dismiss(page):                       # affordance-only; only runs under --dismiss
    for _ in range(2): page.keyboard.press("Escape"); page.wait_for_timeout(180)
    for _ in range(4):                   # click dismiss-buttons scoped to overlays, re-detect, stop when clear
        t = page.evaluate(FIND_DISMISS_TARGETS, DISMISS_LABELS)   # see probe.py — overlay-scoped finder
        if not t: break
        page.mouse.click(t[0]["x"], t[0]["y"]); page.wait_for_timeout(350)

def release_scroll_lock(page) -> bool:   # dismiss-then-reverify; force reset only if still locked
    if reachable_top(page): return True
    page.evaluate(RELEASE_SCROLL_LOCK); return reachable_top(page)

# in capture(): if args.dismiss: dismiss(page)
#               scroll_locked = not release_scroll_lock(page)         # true => loud flag
#               ... tile ...; emit overview-480w via magick
# manifest gains: "dismissed": args.dismiss
```

`FIND_DISMISS_TARGETS` / `RELEASE_SCROLL_LOCK` / the overlay classifier are written and proven in [`probe.py`](../experiments/2026-06-16-tier-b-dismissal/probe.py) — promotion is porting them into `shoot.py` and meeting [`.claude/rules/python.md`](../.claude/rules/python.md) (type hints, why-first docstrings; `shoot.py` is the one sanctioned `playwright` import).

**Paired doc edits** (same change, propose-don't-write): SKILL.md step 2 — the "hides known consent vendors (OneTrust/Transcend/…)" line is now false; it becomes "faithful-first; on overlay contamination re-run with `--dismiss` (Escape + the page's own dismiss buttons); keep both views." VISUAL.md — one line that overlay dismissal is a Tier-B sub-mode logged in Provenance + manifest `dismissed:`, under `qa_status: recapture-used`. `source_url` upstream (#7) pairs with the same touch. *(Done 2026-06-17 — `fc.py source_stamp`; see [BACKLOG](../BACKLOG.md) history.)*

---

## Go / no-go

**GO** — promote affordance-only dismissal into `shoot.py` behind `--dismiss` (faithful default), add `overview-480w` emission, and upgrade scroll-lock to dismiss-then-reverify. The probe validated the mechanism across the required diversity (≥3 sites incl. non-telehealth), in both failure directions, and the pick is *simpler* than what's there now.

**The narrower safe subset, if you'd rather stage it:** #4 (overview) and #3 (scroll-lock re-verify) are independently shippable and near-zero-risk — land them first, gate #1 on a second look. I don't think #1 needs it (the evidence is clean), but it's the separable path.

**Two open calls for you** (neither blocks the GO):
1. **Dual-render trigger (#2).** I default to "cached payload = faithful baseline; emit two tile sets only on combined WebGL+overlay contamination." The alternative — always emit both in one session — is simpler to reason about but doubles tiles on every Tier-B. My pick avoids the doubling; your call if the atomic-pairing simplicity is worth the cost.
2. **Intercom/chat 1-liner.** I'd drop it (faithful capture-fact; `×`-match catches dismissable ones). Easy to re-add if a run misses one.

<sub>**Method** — design went wide on five candidate mechanisms, then an 8-site live probe ([`probe.py`](../experiments/2026-06-16-tier-b-dismissal/probe.py), [`FINDINGS.md`](../experiments/2026-06-16-tier-b-dismissal/FINDINGS.md)) gated the pick: 4 telehealth (gethealthspan / joinfridays / mydrhank / functionhealth) + 4 non-telehealth (sequoiacap VC / electra aero / sorafuel energy / warbyparker), four mechanism variants each, both failure directions, screenshots + montages retained. **Sources** — [Tier-B frame](2026-06-16-tier-b-frame.md) · [06-16 retros](retro/visual-evidence/2026-06-16-summaries.md) · [`scripts/shoot.py`](../scripts/shoot.py) + [`scripts/tile.py`](../scripts/tile.py) · [`modules/VISUAL.md`](../modules/VISUAL.md) + [`skills/visual-evidence/SKILL.md`](../skills/visual-evidence/SKILL.md) · [`.claude/rules/engine-dev.md`](../.claude/rules/engine-dev.md). Drafted 2026-06-16.</sub>
