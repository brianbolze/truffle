# Market Read

## Question

For the observability SaaS sub-market (anchor = Datadog), does a light public
listicle/SERP panel recover a competitor edge-set, and how does that external set compare
to (a) the store's prose-named rivals for Datadog and (b) which of those rivals are
actually captured in the store?

## Result

**Gap-probe answer: YES — the edges are trivially recoverable externally, and the store
cannot surface them structurally. The cheap thing is the edge; the missing thing is the
rival nodes.**

Three findings, leading with what Truffle could and could not support:

**(1) Store side — edges live in prose, point off-store, and 0/5 rival nodes are captured.**
Datadog's `profile.md` names its rivals in one body line (`store/datadoghq-com/profile.md:74`):
"**Competes with:** New Relic, Dynatrace, Splunk, Grafana, Elastic, plus cloud-native tools
and security point vendors" (plus a security-adjacency note — Wiz/CrowdStrike/Splunk — at
`:120`). There is **no structured `competes-with` / substitute relation** (frontmatter has
`parent: []` / `owns: []` only — the vertical axis). Of the 5 named rivals, **none are
captured** in the store (the only observability profile is `datadoghq-com`). So the edge
exists in State only as unstructured prose, and every endpoint dangles outside the store —
a direct confirmation of run-039 S1 (relation support is axis-asymmetric) and G2 (named
rivals are mostly off-store) on a fresh anchor.

**(2) External side — one search + one listicle fully recovered AND extended the store's
edge-set.** A single SERP query surfaced ≥5 independent Datadog-alternatives listicles; one
decision-grade scrape (SolarWinds "Top 14 alternatives for Datadog in 2026", published
2025-12-22, modified 2026-01-28, C2) named a ranked set that **contains all 5 of the store's
prose-named rivals** (Dynatrace, New Relic, Splunk Observability, Grafana, Elastic
Observability) and extends them with cloud-native (Amazon CloudWatch, Azure Monitor, Google
Cloud Operations), enterprise (IBM Instana, LogicMonitor, SolarWinds Observability), and
open-source (Zabbix, Nagios, Paessler PRTG) entrants. The core rival set is corroborated
at **snippet grade** across ≥2 *independent* listicle leads (dotcom-monitor, velodb,
uptrace; the New Relic blog is itself vendor-authored and is **not** counted as
independent) — decision-grade only for the single full-scraped SolarWinds set (C2). [corrected
per Loop-2 evidence verifier, VR1]

**(3) Roadmap read (the 039-W1 question) — the edge is the cheapest thing to source; the
endpoints are what's missing.** Because a directed competitor edge-set for a well-known SaaS
anchor is recoverable from a single public listicle, "the store can't see competitor edges"
is **not a discoverability problem** — it is a *node-coverage* problem: a stored
`competes-with` field for Datadog would point at 5 rivals the store hasn't captured, so it
would dangle today and fail engine-dev's "a cut you can fill reliably" bar (run-039 W1's
exact concern), even though re-deriving the edge live is nearly free.

## Gap Map

| Sub-question | Truffle answer | Evidence | Verdict |
|---|---|---|---|
| Does the store carry Datadog's competitor edges? | Yes, but only as one prose line; no structured relation | datadoghq-com profile.md:74/120 | Partial — prose-grade, unstructured |
| Are the named rivals captured as nodes? | No — 0/5 (New Relic, Dynatrace, Splunk, Grafana, Elastic all absent) | `ls store/` (only datadoghq-com) | Clean gap — edges dangle off-store |
| Can a light external panel recover the edge-set? | Yes — 1 search + 1 listicle recovered all 5 + extended | C1/C2 | Clean recover |
| Is the external panel a trustworthy *denominator*? | No — vendor-authored listicles are self-serving; the core *set* survives cross-source, the *rank/inclusion* does not | C2 (SolarWinds ranks itself #1) | Caveated (L004) |
| Would a stored `competes-with` field be fillable? | Not today — endpoints uncaptured; would mostly dangle | run-039 W1; 0/5 nodes | No new primitive needed |

## Evidence Used

| Claim ID | Claim | Source | Grade | Capture date |
|---|---|---|---|---|
| C1 | ≥5 independent Datadog-alternatives listicles exist; core rivals (Dynatrace, New Relic, Splunk, Grafana, Elastic) recur across ≥2 independent ones | SERP (firecrawl_search), snippet leads + scraped C2 | direction-finding (snippets) + primary (C2) | 2026-06-25 |
| C2 | SolarWinds "Top 14 alternatives for Datadog in 2026" names a ranked 14-product set incl. all 5 store-named rivals + cloud-native/OSS extensions | https://www.solarwinds.com/blog/top-14-alternatives-for-datadog-in-2026 | primary (listicle, vendor-authored) | 2026-06-25 (page modified 2026-01-28) |
| C3 | Datadog's store profile names its 5 rivals in prose; no structured competes-with relation; 0/5 captured | store/datadoghq-com/profile.md:74/120; `ls store/` | primary (local store) | store clock 2026-05-31 |

External evidence lines up with `run-notes.md` `live_evidence_used`. Receipts: C1 (source
panel), C2 (external source), C3 (store query).

## Companies Seen

Anchor: Datadog (datadoghq.com, captured). Store-named rivals (all **uncaptured**): New
Relic, Dynatrace, Splunk, Grafana, Elastic. External panel adds (uncaptured): SolarWinds
Observability, Amazon CloudWatch, Azure Monitor, Google Cloud Operations, IBM Instana,
LogicMonitor, Zabbix, Nagios, Paessler PRTG, plus newer entrants named in snippets (VeloDB,
SigNoz, Uptrace, Prometheus).

## Missing / Stale Coverage

The entire observability competitor neighborhood except the anchor is uncaptured (0/5 named
rivals, 0/14 external-panel members). Datadog's own capture is 2026-05-31 and explicitly
does not transcribe the full pricing matrix — fine for this relation question.

## Source Gaps

The neutral-denominator source family is the gap: the recovering surface is **vendor-authored
alternatives listicles** (SolarWinds ranks its own product #1; New Relic's blog is a rival's
content marketing). Per L004 these are a fallback panel, not a neutral denominator — the
*set* of rivals corroborates across independent sources, but *rank and inclusion* carry
vendor bias. A neutral neighborhood denominator (analyst grids, G2/Gartner-style) was not in
the bounded panel and would be a broader, approval-class source need.

## Raw Learning to Preserve

See `run-notes.md` Observations: **G1** (no horizontal relation; 5 rivals dangle off-store —
039 confirmation), **S1** (external edge recovery is trivially cheap; the gap is node-coverage,
not discoverability — reframes 039 W1), **R1** (JSON-extraction scrape billed 5 credits,
invisible pre-call, near-breaching the 6-credit ceiling — `bounded-live-spend` recurrence,
new flavor vs run-040's PDF), **S2** (vendor-authored listicles are self-serving denominators —
L004 on the listicle axis), **W1** (lightest path is a query-time recipe, not a stored
`competes-with` field — the edge is cheap to re-derive but the endpoints dangle).

## External Completeness Check

Completeness of the *rival set* is load-bearing for the recover-claim. The store's 5 prose
rivals are a strict subset of the external panel's 14; the external panel was itself
corroborated across ≥2 independent listicles for the core 5. No claim of an exhaustive
observability census is made — "not found in this panel" ≠ "not a competitor."

## Market Pattern

Observability is a consolidation market with a stable, widely-agreed default rival set
(Datadog ⇄ Dynatrace / New Relic / Splunk / Grafana / Elastic) plus a long tail of
cloud-native, open-source, and challenger tools. The agreement *across independent listicles*
is exactly why the edge is cheap to recover and why a one-line prose capture already gets the
core right.

## What Would Change This Answer

- If the named rivals were captured as nodes, a stored `competes-with` relation would stop
  dangling and the fillable-cut objection (039 W1) would weaken — the decision hinges on
  node coverage, not edge discoverability.
- If a second anchor's rivals turned out **not** to be externally recoverable from a light
  listicle panel (e.g. a niche B2B tool with no "alternatives to X" content), the "edges are
  cheap" conclusion would narrow to well-known anchors only.
- A neutral analyst-grid denominator (approval-class) could change the *rank/inclusion*, but
  not the recovered core set.
