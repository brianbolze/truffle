# Market Read

## Question

For captured brands that retain 2+ dated raw captures under `store/<domain>/captures/`,
can a reader reconstruct what market-relevant **State** (pricing, offers, positioning)
*changed* between two captures — and does the synthesized `profile.md` preserve that
change, or does snapshot-overwrite erase it? Sub-check (C6): do any domains carry a newer
raw capture than their `profile.md` `captured_at` (synthesis lag)?

This is a **gap-probe** of the **persistence boundary** and the value job *trust the cache
over time* ("what's new since last look"). Evidence mode: **store-only**.

## Result

**No — a returning reader cannot reliably reconstruct market-State change from retained
store substrate today, and the snapshot does erase it by design.** The gap is clean and
has three independent causes, each verified below.

**(1) State overwrites; the append-only layer doesn't cover company State.**
The architecture is explicit: `profile.md` is **State — the current snapshot**, and the
**Signals** layer (`signals/`, dated + append-only) is for *external source* movement —
funding, review/visibility, traffic — with its timeline machinery **deferred** "until a
card/query consumer earns it" (`_design/2026-05-30-architecture.md:57,60,75`). So a
company's *own* pricing / offers / positioning has **no append-only home at all**: when a
profile is re-synthesized, the prior State is overwritten, not versioned. There is no
structured before/after anywhere in the store.

**(2) The only retained prior-State substrate — `captures/<date>/` — is purpose-co-mingled
and page-misaligned.** 21 of 145 domains carry 2+ top-level dated capture folders
(receipt C1). But the dated-folder convention silently mixes three *different* capture
purposes with no marker of which is which:
- **full market captures** (e.g. belmar 06-02 and 06-13, both 4 real pages),
- **partial `deepen-offerings` fetches** (different page counts per date — agelessrx 8→59, eden-health 6→25),
- **visual-evidence re-renders** (functionhealth 06-13 = `homepage_lazyload`/`inject_hero_poster` variants; 06-16 = a `tiles/` dir only — **zero** market pages; receipt C2).

After excluding render-only folders, only **~10 of 21** domains have 2+ dates that each
hold ≥1 real market page (receipt C2 `[DIFFABLE]` rows), and even those rarely capture the
**same page set** twice — so a clean same-page diff is the exception, not the rule.

**(3) Where a same-page diff *is* possible, capture-method noise dominates the genuine
market signal.** Belmar is the cleanest case in the store: identical 4-page set on both
dates, 11 days apart. Three of four pages diff trivially (a footer `Email→LinkedIn` swap,
the capture-date line). The fourth, `homepage.md`, diffs **289 lines** — but on inspection
that is almost entirely **capture-method/scrape-depth noise**: `source_url` normalized
`belmarpharmasolutions.com → www.belmarpharmasolutions.com/`, plus a fully-expanded nav
mega-menu the earlier capture never rendered (receipt C3). Belmar did **not** add a "Weight
Management" category on 06-13; the 06-02 capture just didn't render the submenu. Isolating
real State change from this noise requires per-line human judgment the store does not
encode.

**Change reconciliation exists only in prose, sparsely.** The one place change is ever
recorded is hand-written profile prose ("On-Demand Care … *Resolves the prior capture's
unknown pay-per-visit fee*", onemedical `unverified_fields`). Only **~7 of 145** profiles
carry any explicit prior-capture reference (receipt C4) — an ad-hoc, unstructured,
un-greppable-by-default channel, not a change-pulse a reader can query.

**Sub-check C6 (synthesis lag) — dissolves on inspection.** Nearly every multi-capture
domain shows `profile.md captured_at` *earlier* than its newest capture folder (receipt
C1), which looked like stale synthesis sitting on newer evidence. It is **not**: the newer
folders are the visual-renders and partial deepens from cause (2), not market re-captures.
The capture clock is honest about the profile it describes; the divergence is the
`captures/` directory mixing purposes under one dated convention. **"Not synthesis lag,"
not "no lag exists"** — a true lag can't be ruled out without a per-folder purpose marker,
which is exactly what's missing.

## Gap Map

| Sub-question | Store answered? | Evidence |
|---|---|---|
| Which domains retain 2+ prior captures? | **Clean** | 21/145, enumerated (receipt C1) |
| Is the State/Signals overwrite-vs-append contract knowable? | **Clean** | architecture.md:57,60,75 |
| Can a reader diff market State between two captures? | **No — structural** | overwrite (cause 1); no append-only State layer |
| If they fall back to raw captures, is that a usable diff source? | **Rarely & unreliably** | ~10/21 diffable; page-misaligned; noise-dominated (C2, C3) |
| Is there any structured before/after? | **No** | change lives only in prose, ~7/145 (C4) |
| Is `captured_at` a trustworthy freshness signal? | **For the profile, yes; as "newest store knowledge," no** | C6 — newer folders are non-profile captures (C1, C2) |

For a gap-probe, the clean gap map **is** the result: change-pulse for company State is not
a query the store can answer, and the retained substrate is too purpose-co-mingled and
noise-dominated to back-fill it by hand reliably.

## Evidence Used

All local, store-only. Receipts in `receipts/`.

- **C1** — 21/145 domains with 2+ top-level dated capture folders; per-domain dates;
  profile `captured_at` vs newest folder. `receipts/C1-capture-history-enumeration.md`.
- **C2** — per-date count of *real* market pages (excluding `homepage_*` render variants,
  `tiles/`, `.payloads`); only ~10/21 are diffable on ≥2 dates.
  `receipts/C2-diffable-substrate.md`.
- **C3** — belmar same-page diff 06-02 vs 06-13: footer/date triviata + a 289-line
  homepage diff that is `www`-normalization + expanded nav, not market change.
  `receipts/C3-belmar-samepage-diff.md`.
- **C4** — ~7/145 profiles carry an explicit prior-capture prose reference (the only
  change channel). `receipts/C4-prose-change-notes.md`.

No external/current claims; no snippets used as evidence.

## Companies Seen

21 multi-capture domains (C1): agelessrx, belmarpharmasolutions, blueowl, eden-health,
functionhealth, gethealthspan, getopt, gogeviti, goodlifemeds, hellopepti, hydramed,
joinfridays, keeps, maximustribe, millspharmacy, mydrhank, redantler, remedymeds,
standishspring, vitalityrx, warbyparker. Deep-diffed: belmarpharmasolutions (clean 4/4
page set), functionhealth (render-only newer folders). Denominator treated as **partial**:
this counts top-level dated folders only and excludes `_archive/` and signals captures.

## Missing / Stale Coverage

Not a coverage gap in the usual sense — the *companies* are captured. The missing thing is
a **temporal grain**: the store keeps one current snapshot per company and an external-
signals append log, but no versioned company-State history a diff could run against. The
raw `captures/` folders are an accidental, not designed, history (kept for re-synthesis and
visual work, not for diffing).

## Source Gaps

No external source family would fix this — it is an internal persistence/grain boundary,
not a source-panel shortfall. The two things a trustworthy State change-pulse would need
are both internal: (a) a **capture-purpose / scope marker** on each dated folder (full vs
partial-deepen vs visual-render) so a reader can tell which folders are even comparable;
(b) some **structured before/after** for the handful of fields a returning reader cares
about (price, offer terms, availability). Both are noted as boundaries, not proposed builds.

## Raw Learning to Preserve

See `run-notes.md` Observations: **G1** (no append-only home for company State change),
**G2** (capture-purpose co-mingling makes the substrate un-diffable without a marker),
**S1** (capture-method noise dominates even the cleanest same-page diff), **S2** (C6
synthesis-lag dissolves — capture clock honest, divergence is purpose-mixing), **W1**
(lightest-path note, held).

## External Completeness Check

N/A — store-only gap-probe; no outside denominator is load-bearing for a persistence-
boundary finding. The internal denominator (21/145) is named partial.

## Market Pattern

Not a market-content pattern — a **store-capability** pattern, and it sharpens three live
lessons. It is the change-pulse complement to **L004** (denominators are partial, say "not
found"): here the *temporal* denominator is partial — the store can say what a company is
*now*, not what *changed*, and must not let a raw-capture diff masquerade as a change feed.
It is also a fresh instance of **L005**'s corollary — an empty/auto-accumulated structured
surface (the `captures/` history) is a *byproduct*, not a queryable market fact. And it
echoes the "unreliable second channel" shape (run-037 DR2 STRAIN; run-039 G2 prose
competitors): change reconciliation lives only in sparse prose, so it can't be relied on.

## What Would Change This Answer

- A **capture-purpose/scope marker** per dated folder (full-capture vs partial-deepen vs
  visual-render) would make the substrate at least *selectable* for diffing — turning "~10
  diffable" into a knowable set rather than a manual inspection each time.
- A real **returning-reader consumer** asking "what changed since last look" for a specific
  field (price, offer terms) would move this from a noted boundary toward earning the
  deferred Signals-timeline machinery — *for company State*, which today's `signals/` scope
  explicitly excludes.
- Until both exist, **"no new primitive needed" stays live**: the honest read is that
  change-pulse for company State is out of scope by design, and a hand-diff of raw captures
  is noise-dominated and not trustworthy enough to publish as a change feed.
