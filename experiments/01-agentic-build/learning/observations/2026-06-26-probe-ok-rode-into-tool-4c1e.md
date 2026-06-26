---
date: 2026-06-26
run: changes/2026-06-26-source-page-tool
kind: risk-miss
---

**Saw.** Reviewing the source-page-tool proposal, the plan lifts the probe's
`ok = (200 <= status < 400) and bool(parsed.text)` rule and its
`body.decode("utf-8", errors="replace")` / `Accept-Encoding: identity` posture into a
durable generic `tools/` entry unchanged. Acceptance check #3 tests `text_chars > 5000`
externally, but the tool's own `ok` encodes no floor and no binary/encoding guard — a 200
empty-JS-shell, a gzip body the parser garbles, or a non-utf-8 page would all still emit
`ok:true`. The probe's `ok` was only ever a relevance-eval signal ("did this move
P@10"), not a per-capture trust signal, and that semantic gap rode along into the
graduation unflagged in the proposal.

**Not claiming.** Not claiming permissive `ok` is wrong for a capture tool, nor that
probe→tool graduations generally drag stale semantics — one sighting on one extraction.
The pressure was to treat the probe's `ok` as load-bearing when it had only ever been an
eval convenience.
