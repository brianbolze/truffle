# 2026-06-16 dogfood — synthesis (Tier-B rebuild)

Cross-cut of the 9 per-slug retros in this folder. The runs dogfooded the new `shoot.py`
(affordance-only `--dismiss`, `overview-480w`, clean/dirty labeling) shipped this date. The
[parent `2026-06-16-summaries.md`](../2026-06-16-summaries.md) is the *old*-pipeline counterpart;
this is the rebuild's.

## Verdict

**The rebuild holds, and the dogfood paid for itself: it exposed two ways Tier-B failed *silently* — both now fixed and live-validated.** Affordance dismissal cleared every overlay that had a reachable affordance (cookie banners, a custom CMP, a chat bubble) with zero content harm; the QA gate didn't over-escalate on clean captures. The two silent-fails were the whole reason to run it.

## Coverage — what each slug actually exercised

| Path | Slugs | Result |
|---|---|---|
| `--dismiss` cleared an overlay | joinfridays, mydrhank, stripe, doordash (business) | clean, nav kept, 0 harm |
| `--dismiss` **no-op** (silent) | goodlifemeds | shadow-root CMP unreachable → **now loud** |
| Bot-wall captured as page (silent) | doordash (www apex) | Cloudflare interstitial → **now loud** |
| Scroll-lock un-dismissable (already loud) | alange-soehne | forced reset fired live + failed → fell back to cached |
| Faithful Tier-B (no overlay) | ro-co | lazy-load recovery; surfaced orphan-tile bug |
| No Tier-B (QA restraint) | etsy, parlance | clean cache, correctly not escalated |

## Confirmed working

- **`overview-480w` emission** — every Tier-B run wrote it, 0 `magick` failures. Killed the montage hack.
- **Affordance dismissal generalizes** — cleared a custom CMP the old vendor list missed (joinfridays `#cookie-consent-dialog`), and confirmed the approach doc's open-call #2 bet on Intercom (stripe: proactive bubble dismissed via `×`, persistent launcher correctly left as a capture-fact).
- **Negative-first label priority** — mydrhank clicked *Reject all*, not Accept all.
- **QA-gate restraint** — etsy + parlance + ro-co's 4 clean pages did not escalate; faithful-first discipline held.
- **Loud scroll-lock** — alange's un-dismissable lock fired `scroll_locked` and the operator reverted to cached. The guard earned its keep.

## What broke — and where it landed

| Finding | Slugs | Status |
|---|---|---|
| Shadow-root CMP: `--dismiss` no-op, **no warning** | goodlifemeds | **Fixed** `94f1d9c` — `dismiss_cleared` footprint guard; validated: now warns |
| Cloudflare wall captured as page, **no warning** | doordash | **Fixed** `94f1d9c` — structural thin-page guard; validated: now warns |
| Forced scroll-reset framed as a fix; failed live | alange | **Fixed** `94f1d9c` + SKILL — reframed best-effort-flag, fall back to cached |
| Orphan tiles when re-rendering into an existing dir | ro-co, alange | **Fixed** `94f1d9c` — shoot.py clears its own artifacts first |
| Tier-B treated as auto-upgrade vs cached | alange | **Fixed** SKILL — Tier-B is a comparison; worse re-render → keep cached |
| Tile-dir `<today>` vs `source_capture` ambiguity | mydrhank, alange | **Fixed** SKILL — render into the dossier date dir |
| `python3` may lack playwright | joinfridays, ro-co | **Fixed** SKILL — call the interpreter that has it |
| Root tiler manifest vs per-page shoot manifest drift | ro-co, mydrhank, doordash | **BACKLOG** — reconcile half deferred (latent: nothing reads it yet) |
| `contrast_with` lint checks existence, not that the tile *shows* the contrast | parlance | **BACKLOG** — blind judge can mis-cite; single sighting |

## The one standing trade (your call, parked)

**goodlifemeds is now loud-but-unrecovered.** The new pipeline *detects* the closed-shadow-root CMP and tells the operator to fall back to cached — but it can't *clear* it the way the retired `CONSENT_MOUNTS` structural-hide could. That's the deliberate trade: loud-failure over a maintained vendor denylist (anti-Doro). The escape hatch — a narrow, opt-in structural-hide for the shadow-root class only — stays parked until a **second** sighting; one site isn't enough to re-introduce living infrastructure.

Minor, noted-not-urgent: a persistent fixed launcher repeats across *every* Tier-B tile (stripe), where Tier-A's single full-page crop shows it once. Miners treated it as a caveat; no harm. A "fixed element covers every tile?" check is a someday-maybe, not a need.
