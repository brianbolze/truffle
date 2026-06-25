# Market Read

## Question

When the store's human-facing brief is generated via `scripts/render.py`, do the rendered
HTML briefs faithfully carry each profile's source-rigor flags — `unverified_fields`,
self-reported / honest-flag prose, the price-visibility token, and point-in-time / sale
price caveats — into the 5-second handoff surface, or does rendering launder them away?

**Mode:** gap-probe · **Evidence:** local-existing (ran `python scripts/render.py … --no-fetch`
over 6 flag-heavy profiles; diffed the generated HTML against `profile.md` and read the
renderer source `scripts/present/{model,brief}.py`). No external network, no spend, no
mutation.

**Panel (purposive, illustrative of flag types — not a census):** remedymeds-com,
henrymeds-com (self-reported rating + internally inconsistent member/Rx counts),
sorafuel-com (present-tense `description` over-claim + pilot-stage maturity),
euclidpower-com (page-conflicting metrics in `unverified_fields`), therabody-com
(sale-snapshot prices, large roster), etsy-com (house-of-brands GMS).

## Result

**The relay preserves flag *content* but inverts flag *salience*. It does not launder the
flags away — it de-prioritizes them below the 5-second reading path.** Two-part answer:

**(1) Content fidelity — GOOD (the laundering hypothesis is falsified at the artifact level).**
Every brief renders every `unverified_fields` entry verbatim as a "What we couldn't verify"
list, renders `site_notes` as "Field notes — read before trusting a number," renders the
self-reported proof prose (the `Credibility & proof` section), and renders the
price-visibility token as styled roster chips where `offerings.md` exists. Nothing is
dropped:

| Company | `unverified_fields` → brief `<li>` | self-reported proof prose | price-vis token in brief |
|---|---|---|---|
| remedymeds | 3 / 3 ✓ | present (collapsed) | 3 `published` + 3 `on-request` chips (tab 2) |
| henrymeds | 3 / 3 ✓ | present (collapsed) | chips (tab 2) |
| sorafuel | 2 / 2 ✓ | present (collapsed) | n/a (no `offerings.md`; entity carries no per-offer token) |
| euclidpower | 2 / 2 ✓ | n/a | n/a |
| therabody | 4 / 4 ✓ | present (collapsed) | 57 `published` chips (tab 2) |
| etsy | 4 / 4 ✓ | n/a | n/a |

So the markdown→HTML lens is faithful: the source-of-truth flags survive the relay. This is
a **positive** finding for the engine — the recurring relay-risk thread is *not* a content-drop
in the one rendered relay we ship.

**(2) Salience inversion — the actual failure, scoped precisely (corrected per VR1).** The
default brief view = the hero + tab 1 ("Profile"), and tab 1 auto-opens only `Overview` +
`Strategic read`; `Positioning`, `Model & monetization`, and **`Proof & trust signals` (where
the "self-reported" proof bullets live) render collapsed** (`<details>` without `open`).
Meanwhile:

- The **structured** trust surfaces are uniformly off the default path: `unverified_fields` and
  `site_notes` render **only in tab 4 ("Provenance & limits")** (`id="t-profile" checked`; flags
  three tabs over, C2); the price-visibility chips render **only in tab 2 (Offer architecture)**.
- The hero renders `description` at the **highest salience in the document** (`hero-desc`,
  29px display) with **no adjacent flag of its own**. For sorafuel the hero reads "**Produces
  sustainable aviation fuel** by converting ambient air…" (present-tense, maturity-blind — the
  run-042 G1/R1 over-claim); the structured guard — "captured pages describe a *planned* pilot
  production facility and future milestones" — sits in tab-4 `unverified_fields`. C1/C3.

**But the 5-second path is NOT flag-free** (this corrects the run's first framing). The default
Profile tab auto-opens `Overview` and `Strategic read`, and the **captor's prose there often
carries the caveat**: remedymeds' auto-open Strategic read says "Scale and outcome figures are
*self-reported and internally inconsistent across pages — treat as marketing, not audited
metrics*"; sorafuel's auto-open Overview/Strategic read say "*venture-stage… moving toward pilot
production… not a sales storefront… pre-commercial/pilot-stage… rather than operating
production*." So whether a fast reader sees a flag depends on **whether the captor wrote one into
an auto-open section** — present for remedymeds + sorafuel, but with **no structural guarantee**,
and absent beside the hero `description` itself.

**Net (corrected):** the *structured* flag surfaces (`unverified_fields`, `site_notes`, price-vis
chips) are uniformly tab-gated off the 5-second path; the hero `description` — the single most
over-claim-prone field — carries no flag of its own at peak prominence; and the only protection
that reaches the default path is **captor-prose-dependent** (a caveat written into Overview /
Strategic read), an *unreliable second channel* (run-037 DR2 shape) rather than a structural one.
The relay is faithful in content and **salience-inverted in structure**; on the default path it
protects the reader only as well as the captor's prose discipline does.

## Gap Map

- **Answered cleanly:** Does render.py drop flag content? **No** — all `unverified_fields`,
  `site_notes`, proof prose, and roster price-vis tokens render (table above). The naive
  "rendering launders the flags" hypothesis is falsified for the shipped relay.
- **The real gap (scoped per VR1):** the **structured** flag surfaces (`unverified_fields`,
  `site_notes`, price-vis chips) render at the **lowest salience** (tab 4 / tab 2) while the most
  flag-relevant field (`description`) renders at the **highest** (hero) with no flag of its own.
  The default path is *not* flag-free — the auto-open Overview/Strategic read carry a caveat **when
  the captor wrote one** (remedymeds, sorafuel both did) — but that protection is captor-prose-
  dependent, not structural. This is an **ordering / salience** property of
  `scripts/present/brief.py` plus a captor-prose-discipline dependency, not a content gap — and it
  sharpens the recurring "prose-grade, relay-dependent" relay-risk rows (038-R1, 042-S1/R1, 048-S3):
  the relay *preserves but de-prioritizes the structured flags, and falls back to the captor's prose
  for the default path.*
- **Internal-intent mismatch (minor):** `brief.py`'s own docstring says the trust surface is
  "rendered visibly as the product," but in practice it is tab-gated and collapsed — the stated
  intent and the salience disagree.
- **What would change the answer:** a brief that surfaced one flag token at hero grain (e.g. a
  "maturity: pre-revenue / pilot" or "figures self-reported" eyebrow beside `description`), or
  auto-opened the proof/limits sections, would move the protection onto the 5-second path. Not
  proposing it — n=6, single relay, and the fix is a Judgment for the presentation-layer owner.

## Evidence Used

Local-existing; all reproducible offline. No external/current claims, so no primary-vs-secondary
grading applies. Receipt: `receipts/C1-render-structure-audit.md`.

- **C1** — Hero renders `description` at top salience, unguarded. `_out/briefs/sorafuel-com.html`
  `hero-desc` = "Produces sustainable aviation fuel by converting ambient air, water, and
  renewable electricity…"; source `scripts/present/brief.py:381` (`hero-desc`, `--desc-size`
  29–21px); `store/sorafuel-com/profile.md:96-98` (the milestone/pilot guard).
- **C2** — `unverified_fields` + `site_notes` render only in the 4th tab. `scripts/present/brief.py:190-222`
  (`_provenance_html` → "What we couldn't verify" / "Field notes"); tab order
  `brief.py:326-348` (trust tab is index 3; `id="t-profile" checked`). Verified per-brief
  `<li>` counts match `profile.md` `unverified_fields` length (3/3/2/2/4/4).
- **C3** — Default Profile tab collapses the proof section. `scripts/present/brief.py:259-263`
  (`_profile_panel` order: `overview`/`strategic read` `open_=True`; `credibility & proof`
  `open_=False`).
- **C4** — Price-vis token survives as a styled chip in the roster, tab 2.
  `scripts/present/brief.py:93-96` (`vis-{published|partial|on-request}`); therabody brief
  carries 57 `vis-published` chips, remedymeds 3 `published` + 3 `on-request`.

## Companies Seen

remedymeds-com, henrymeds-com, sorafuel-com, euclidpower-com, therabody-com, etsy-com
(6 profiles; 3 with `offerings.md` rosters: remedymeds, henrymeds, therabody). Panel was
selected to span the flag *types* surfaced in runs 038/042/046/048, not to sample the corpus.

## Missing / Stale Coverage

None blocking — every panel profile is captured and renders. Captures span 2026-05-31
(etsy) to 2026-06-24 (therabody); recency is not load-bearing for a structural relay audit.

## Source Gaps

None external. The read is bounded to the *shipped* relay (`scripts/present/`); a different
consumer surface (the comparison sheet `compare.py`, the index `index.py`, or a delegated
agent reading `profile.md` directly) could relay flags with different salience and was **not**
audited here — so "the relay preserves but de-prioritizes" is a claim about the single-company
HTML brief, not about every downstream consumer.

## Raw Learning to Preserve

See `run-notes.md` Observations — `S1` (content fidelity is good — laundering falsified),
`G1` (structured-flag salience inversion is the real relay failure), `S2` (hero `description` is
the peak-salience over-claim with no structured flag of its own), `G2` (proof/limits are tab-gated
+ collapsed vs. the docstring's "visible as the product"), `W1` (lightest path, held), `VR1`
(evidence-verifier correction: the default path is captor-prose-rescued, not flag-free).

## External Completeness Check

Not applicable — no external denominator; the "denominator" is the renderer's own code paths,
read in full (`model.py`, `brief.py`).

## Market Pattern

Not a market read. The system pattern: **the recurring "relay-dependent" relay-risk is a salience
property, not a content property, in the one relay Truffle actually ships.** Across 038/042/048 the
observations said flag protection "depends on the downstream reader carrying it." This run locates
*where* that dependency bites in the concrete artifact: not at content (the brief carries every
flag) but at reading-order — the *structured* trust surfaces are buried in tabs 2/4 and the
over-claim-prone `description` is the most prominent element with no flag of its own. The default
path is rescued only by **captor prose** in the auto-open Overview/Strategic read — an unreliable
second channel (run-037 DR2). "Relay-dependent" now has a mechanism: **preserve-but-bury the
structured flags; lean on captor prose for the default view.**

## What Would Change This Answer

- A second relay (comparison sheet / index / a delegated-agent prompt) showing the *opposite*
  salience would show this is a brief-specific layout choice, not a relay-wide pattern.
- A real 5-second-reader study showing readers do click to tab 4 / expand proof before acting
  would dissolve the salience concern (the flag would be "reachable enough").
- If the presentation-layer owner intends tab-4 placement as correct (flags are "limits," filed
  under Provenance by design), then this is a working-as-designed Judgment, not a gap — the run
  only shows the 5-second path is flag-free, not that the placement is wrong.
