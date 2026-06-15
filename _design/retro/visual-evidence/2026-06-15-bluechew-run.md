# Retro — BlueChew visual-evidence run (2026-06-15)

Second `/visual-evidence` run ([`store/bluechew-com/visual.md`](../../../store/bluechew-com/visual.md), lint exit 0). Output is good and the two-mode read (disciplined dark homepage/PDP vs. template-grade reviews/about) is sharp. Mostly this run *confirmed* the [Blokes retro](2026-06-15-blokes-run.md) lessons rather than surfacing new ones — which is itself the useful signal.

## Confirmed — trust the blind layer on overlays (Blokes Lesson 1)

A site-wide cookie banner sat on the lower edge of every hero tile (homepage, sildenafil, about, reviews). Last run's lesson said: don't escalate to Tier-B for cosmetic overlays the blind protocol already discounts. So I **kept the hero tiles** (the load-bearing evidence sits clean above the banner) and skipped Tier-B entirely. It worked exactly as designed — the judge rejected precisely the two cards whose tell fell *inside* the banner zone (about-hero section-break, about-hero orbiting-dots) and kept everything else. No detour this time. The lesson holds across a second company.

## New — exclude vs. caveat is a real distinction

`gold-plan` was the one genuine exclusion: it captured as a plan-selector **modal over a dimmed/greyed page** — no readable layout behind the scrim. That's categorically different from a cookie banner on an otherwise-rendered page. The rule that emerged: **caveat-and-keep** when evidence sits clean and the overlay is local; **exclude the page** when the overlay leaves no page to read. Worth a line in the QA-gate section of SKILL.md.

## Recurring — the judge still under-prunes (Blokes Lesson 2)

Same gap, second data point: **51 raw → 36 accepted**, against a contract target of 8–14. The "prune/merge" pass kept ~70%. Two runs now (Blokes: 50→42; here: 51→36) both land 2.5–3× over target. This is no longer a one-off — the judge prompt needs a **hard count ceiling**, not soft "prune and merge."

One divergence from Blokes: I did **not** hand-curate to 14. I treated the judge as the pruning authority and the cards as an audit trail (the impression is the 5-second deliverable). Both choices are defensible, but they can't both be right across runs — either the human curates to the contract count, or the judge enforces it. Picking one is the real open question, and it's a prompt/experiment decision, not an authoring-time judgment call. Flagging for the judge-ceiling experiment.

## Smaller note

- **Path duality recurred** (absolute paths for miner reads, repo-relative for authoring + lint). Already logged in the Blokes retro; still unfixed. The fix is the same one-liner in SKILL.md about launching from the Web Research repo.

## Net

Output: good, lint-clean. Process: zero new detours (the Tier-B discipline paid off), one new useful distinction (exclude vs. caveat), and the judge-ceiling gap is now confirmed across two runs — overdue for the experiment.
