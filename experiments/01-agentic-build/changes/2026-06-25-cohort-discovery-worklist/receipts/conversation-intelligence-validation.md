# Conversation Intelligence Validation Receipt

Date: 2026-06-25
Status: promising initial validation; product/workflow boundary issue carried into later decision surface

## Run Boundary

No store writes, no `/research-company`, no captures into `store/`.

Live captures:

- SerpAPI organic-only category queries: 3 credits.
- SerpAPI organic-only demand queries: 2 credits.
- Exa `/search` novelty query: USD 0.017.

Queries stayed within the approved cap.

## Source Panel

Category / listicle / direct-enumeration SERPs:

- `best AI meeting assistant tools 2026`
- `best conversation intelligence software 2026`
- `AI meeting notes apps Otter Granola Fathom 2026`

Demand-side SERPs:

- `Gong Clari alternatives conversation intelligence`
- `Otter Granola Fathom alternatives AI meeting notes`

Exa novelty:

- `AI meeting notes apps conversation intelligence software sales call analysis Gong Clari Granola Otter Fathom`

Useful source URLs surfaced:

- Avoma AI meeting assistants: https://www.avoma.com/blog/the-5-best-ai-meeting-assistants-notetakers
- Tana AI meeting assistants: https://tana.inc/blog/best-ai-meeting-assistants-2026
- Zapier AI meeting assistants: https://zapier.com/blog/best-ai-meeting-assistant/
- G2 conversation intelligence: https://learn.g2.com/best-conversation-intelligence-software
- AssemblyAI conversation intelligence: https://www.assemblyai.com/blog/conversation-intelligence-software
- Sybill conversation intelligence: https://www.sybill.ai/blogs/best-conversation-intelligence-tools
- Salesforce Gong alternatives: https://www.salesforce.com/compare/gong-alternatives/
- Cuebo Gong alternatives: https://www.cuebo.ai/blog/gong-alternatives
- Granola / Fireflies / Fathom / Otter pricing comparison: https://www.granola.ai/blog/meeting-note-tool-pricing-granola-vs-fireflies-fathom-otter

## Store Baseline

The store-first baseline matters here because several benchmark rows already resolve locally:

- Gong -> `gong-io`
- Clari -> `clari-com`
- Granola -> `granola-ai`
- Dovetail -> `dovetail-com`
- AlphaSense -> `alpha-sense-com`
- Notion -> `notion-com`
- OpenAI / ChatGPT -> `openai-com` / likely `openai-com`
- Apple -> `apple-com`

Not found in store under exact names:

- Loom
- Otter
- Zoom
- Microsoft / Copilot for Teams
- Fathom
- Claude / Anthropic
- Rewind
- Jamie AI

## Benchmark Recovery

External-source-only top-10 overlap: 7 of 10 after the WebSearch addendum.

External hits:

- Gong
- Clari
- Otter
- Granola
- Zoom AI Companion
- Microsoft Copilot for Teams
- Fathom AI

External misses:

- Loom
- Dovetail
- AlphaSense

Store-first union top-10 overlap: 9 of 10 after the WebSearch addendum.

Store-first union hits:

- Gong
- Clari
- Otter
- Granola
- Dovetail
- Zoom AI Companion
- Microsoft Copilot for Teams
- AlphaSense
- Fathom AI

Store-first union misses:

- Loom

Full core-list recovery is weaker because the benchmark intentionally includes products and workflows rather than only companies:

- OpenAI Whisper, ChatGPT transcript workflow, Claude transcript workflow, and Apple Voice Memos are product/workflow boundary rows.
- OpenAI and Apple resolve as company profiles, but the discovery panel did not rediscover the specific workflow use case.
- Claude / Anthropic did not resolve in store and did not surface in the external panel.

## Feeder Notes

| Feeder | Top-10 overlap | Useful novelty | Notes |
| --- | ---: | ---: | --- |
| Store baseline | 5/10 | n/a | Strong on captured enterprise/productivity companies; misses Loom, Otter, Zoom, Fathom, Microsoft. |
| Category/listicle SERP | 6/10 | medium | Best external feeder; cleanly finds meeting notetakers and sales CI names. |
| Demand SERP | 4/10 | medium | Good for Gong/Clari alternatives and Otter/Granola/Fathom comparisons. |
| Exa `/search` | 4/10 | medium | Very good for Gong, Clari, Otter, Fathom; adds long-tail tools such as Avoma, Goodmeetings, Grain, Fellow, Claap. |
| Store-first union | 8/10 | medium | Materially beats any single feeder. |

## Adjacent Pollution

The panel mostly separated adjacent transcription-dev tools from end-user meeting / CI tools.

Observed adjacent risk:

- Symbl.ai appeared in a conversation-intelligence list.
- AssemblyAI appeared as a publisher/source and also sits in Brian's adjacent transcription-dev benchmark.
- Fireflies, Avoma, Grain, Fellow, and Jiminny appeared repeatedly; these are plausible adjacent or core meeting/CI candidates, not hard pollution under the provided benchmark.

Not observed as core-promoted pollution in this run:

- Rev
- Deepgram
- ElevenLabs
- AWS Transcribe
- Nuance
- Verbit
- Descript

OpenAI Whisper did not surface externally, so the intended dual-list ambiguity was not exercised by this panel.

## Interpretation

This cohort validates the store-first union idea better than telehealth. Store baseline + external feeders recovered 9/10 of Brian's top-10 list after direct WebSearch was added, while no single feeder did.

The miss is conceptual, not just retrieval: the benchmark mixes companies, products, and workflows. A company-discovery engine can capture OpenAI or Apple, but it will not reliably discover "put a transcript in ChatGPT" or "Apple Voice Memos" unless the validation layer explicitly supports product/workflow targets.

Recommendation: keep this as positive evidence for the union approach, but revise the scoring model before any graduation decision:

- score company capture targets separately from product/workflow boundary rows;
- keep adjacent transcription-dev tools as boundary-labeled candidates, not hard pollution unless promoted as core;
- add a product/workflow discovery lane only if the engine is meant to propose non-company capture targets.
