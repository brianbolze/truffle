# SERP intent panel — June 11 repeat vs June 8 baseline

Run date: 2026-06-11 (captures 17:40–17:41Z). Same 4 buyer-intent queries × same 11-brand cohort as
[the June 8 smoke](../2026-06-08-serp-intent-telehealth-smoke/FINDINGS.md). 4/4 captures clean, no
schema drift, 5 SerpAPI credits spent.

> SERP results measure occupancy/visibility (shelf-crowding); traction results measure movement.
> Neither measures demand.

## 30-second skim — what moved in 3 days

- **The AI Overview disappeared from the TRT query.** June 8 had an AIO citing Hims, Hone Health, and
  TRT Nation across 6 references; today the AIO block is absent entirely. The organic shelf barely
  moved (Hims #1, Hone #2 held; TRT Nation 5→4). Per the venture invariants, AIO is non-deterministic
  and rotates within hours — absence is data, not a ranking loss; organic is the stable channel.
- **Brello had the best 3 days.** Its tirzepatide page rose #2→#1, and it picked up a brand-new AIO
  reference on the sermorelin query. It lost a third-party listicle mention on tirzepatide.
- **Organic ranks are otherwise sticky.** No cohort brand entered or dropped out of any top-10. All
  movement among own pages was ±1–2 positions; sermorelin and NAD shelves are near-identical.
- **AIO references churned on every query that kept an AIO** — new refs (Ro on tirzepatide, Brello on
  sermorelin), dropped refs (Brello on tirzepatide), and reshuffled indices. Consistent with AIO
  reference order being unstable run-to-run.
- **Query labels unchanged**: sermorelin still the only `clean` query; the rest still `noisy`.

## Detail — per query

Every figure below traces to `captures/*.json` (raw SerpAPI envelopes), `panel-live.json` (panel
rows), and `diff-vs-june8.json` (mechanical diff, produced by `diff_panels.py`). Baseline =
[`panel-calibrated.json`](../2026-06-08-serp-intent-telehealth-smoke/panel-calibrated.json), verified
byte-stable pre-run in `baseline-verification.json`.

### TRT online prescription

- Own pages: hims@1 (held), hone-health@2 (held), trt-nation 5→4.
- Third-party mentions: peter-md@4 and hone-health@4 dropped (the position-4 listicle slot changed).
  Organic top-10 match count 5→3 reflects those two lost mention-rows, not own-page losses.
- AIO: present→**absent**. All 6 June 8 cohort references (hims ×2, hone-health ×3, trt-nation ×1)
  gone with the block. Not a rank movement — the surface itself didn't render.
- Off-cohort top-10: webmd.com left; drb.ai and innerbody.com entered. Off-cohort count 6→7.

### sermorelin online prescription

- Own pages: agelessrx@1, strut-health@4+@10 held; hone-health 9→8, hydramed 8→9 (adjacent swap).
- AIO (present both runs): **new** reference for brello-health; strut-health references 3→2;
  agelessrx@ref0 and hone-health@ref1 held exactly.
- No mentions either run; labels stay `clean`; off-cohort steady at 5.

### NAD injection online

- Own pages: agelessrx@3 and hone-health@6 held; hydramed 8→9. No entries/drops.
- AIO (present both runs): same two brands cited, indices reshuffled — hone-health ref2→ref7,
  agelessrx ref7→refs 5+6.
- Off-cohort steady at 7; still the noisiest shelf. No movement beyond the above.

### compounded tirzepatide online

- Own pages: brello-health 2→**1**, ivim-health 8→**6** — both cohort pages moved up.
- Mentions: ro@5 held; brello-health@9 mention dropped (top-10 match count 4→3).
- AIO (present both runs): ro **new** as a reference; brello-health reference dropped;
  ivim-health ref3→refs 8+9.
- Off-cohort steady at 6.

## Run notes

- First live-fetch attempt hit a SerpAPI read timeout after writing 2 of 4 captures (exit 2);
  the rerun resumed from existing captures and fetched the remaining 2 cleanly. No duplicate spend.
- AIO `ranked_brands` was 0 in both runs on all queries — same as June 8; cohort AIO evidence rides
  on `reference_matches` only.

## Files

- `captures/` — 4 raw `serpapi.py` envelopes (2026-06-11)
- `panel-live.json` / `panel-live.md` — today's panel
- `diff-vs-june8.json` — mechanical diff vs June 8 calibrated panel (`diff_panels.py`)
- `baseline-june8-cached-current.json|md`, `baseline-verification.json` — pre-run proof the June 8
  baseline still reproduces from its cached captures

Signals only — interpretation belongs to the launch-package run and Brian.
