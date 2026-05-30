# Experiment: query affordance (rung 2)

> **Question.** The Frame bets that *queryability is the product* — and that agent-workflows' real failure was tooling + discoverability, not storage. Does a **thin query affordance** (one script that consolidates the relevant slice across brands) actually let an agent answer a cross-brand question better/cheaper than grepping ~30 files from scratch?

If yes → rung 2 is the foundation and the SQLite index (rung 3) stays parked. If no → aggregation pulls rung 3 forward.

## Fixture

The existing **competitive-intel snapshots** (77 brands, dated markdown + YAML frontmatter + `## Products` / pricing sections). A real corpus, zero capture cost. Read-only — we never write back.

Canonical query: **"How do brands describe + price Sermorelin?"** — 30 brands mention it. (Also try Tirzepatide=40, Semaglutide=42, TRT=31.)

## Variants compared

| Variant | What the agent does | Proxy cost |
|---|---|---|
| **A — baseline** | Open each brand's latest snapshot from scratch, read, extract | ~30 file reads, large token load, easy to miss brands |
| **B — thin affordance** | Run `digest.py "Sermorelin"` → one consolidated markdown digest, read once | 1 call + 1 read |
| **C — (later)** | Same, but backed by a derived index (rung 3) | — only if B is too lossy |

## Run

```bash
python3 digest.py "Sermorelin"            # consolidated cross-brand digest to stdout
python3 digest.py "TRT" --snapshots PATH  # override fixture location
```

`digest.py` is deliberately dumb: per brand, take the **latest** snapshot, pull any `###` section whose title matches the term (falling back to price-bearing lines), emit one markdown doc. No index, no deps.

## What we're judging

- **Completeness** — does B surface all ~30 brands, or silently drop some?
- **Fidelity** — is the extracted slice good enough to answer from, or does the agent still need to open files?
- **Cost** — 1 read vs. ~30.
- **Where it breaks** — what does a heuristic section-grab miss that a real schema/index would catch?

See [`FINDINGS.md`](FINDINGS.md).
