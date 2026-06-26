# WebSearch Addendum

Date: 2026-06-25
Status: direct WebSearch feeder added; later tested by iteration-2 and page-extraction probes

## Why This Was Added

The first scored validation collapsed "web search" into repeatable SerpAPI organic panels plus listicle snippets. That under-tested the archived bakeoff's strongest feeder: direct WebSearch / page enumeration.

This addendum treats WebSearch as its own feeder. It used live search plus opened result pages, not store data or Notion.

## Telehealth WebSearch

Queries used:

- `best online GLP-1 providers 2026`
- `best online erectile dysfunction treatment 2026`
- `best online NAD longevity telehealth providers 2026`
- `best online HRT menopause telehealth providers 2026`
- follow-up healthspan / longevity searches after the NAD query mostly returned supplement lists

Useful sources opened or surfaced:

- Forbes Health GLP-1 provider list: https://www.forbes.com/health/weight-loss/best-affordable-online-glp1-providers/
- WSJ on Amazon / One Medical GLP-1 program: https://www.wsj.com/health/pharma/amazon-com-to-offer-program-for-glp-1-weight-loss-drugs-72465385
- Policy Lab TRT comparison: https://policylab.us/testosterone-replacement-therapy/online-trt/
- PPARX TRT comparison: https://www.pparx.org/testosterone/best-online-trt-clinics/
- Vogue NAD supplement guide: https://www.vogue.com/article/best-nad-supplements
- New York Post NAD supplement guide: https://nypost.com/shopping/best-nad-plus-supplements-per-experts/
- Wikipedia / source aggregate for Juniper: https://en.wikipedia.org/wiki/Juniper_(telehealth_company)

Net effect on holdout scoring:

- Added One Medical as a recovered F4 holdout through WSJ.
- Did not recover Niagen Plus as a telehealth/care brand; NAD searches mostly returned supplement-commerce lists such as Tru Niagen, ProHealth, Thorne, Elysium, and Wonderfeel.
- Did not recover Rex MD; ED-provider WebSearch was unexpectedly poor in this environment and skewed toward counterfeit-drug news / generic ED material rather than DTC ED brand lists.
- Did not recover Lifeforce; healthspan / biomarker searches surfaced Function Health-style adjacent diagnostics more readily than the DTC therapeutics holdout.

Updated telehealth union recovery:

- F3/F4 must-hit recovery: 10/13, up from 9/13.
- F2 should-hit recovery: 5/15, unchanged.

Interpretation:

Direct WebSearch helps, but the broad telehealth cohort still fails. The missing set is not random: ED, NAD/longevity, and healthspan/labs need their own query families. This supports the revise/downscope recommendation rather than the original broad-cohort verb.

## Conversation Intelligence WebSearch

Queries used:

- `best AI meeting assistant tools 2026 Otter Granola Fathom Fireflies Zoom AI Companion Notion AI`
- `best conversation intelligence software 2026 Gong Clari Fathom Otter`
- `Gong alternatives conversation intelligence Clari Chorus Avoma 2026`
- `Granola Otter Fathom alternatives AI meeting notes 2026`

Useful sources opened:

- Avoma AI meeting assistants: https://www.avoma.com/blog/the-5-best-ai-meeting-assistants-notetakers
- Tana AI meeting assistants: https://tana.inc/blog/best-ai-meeting-assistants-2026
- Zapier AI meeting assistants: https://zapier.com/blog/best-ai-meeting-assistant/
- G2 conversation intelligence: https://learn.g2.com/best-conversation-intelligence-software
- AssemblyAI conversation intelligence: https://www.assemblyai.com/blog/conversation-intelligence-software
- Sybill conversation intelligence: https://www.sybill.ai/blogs/best-conversation-intelligence-tools
- TechRadar AI tools roundup: https://www.techradar.com/best/best-ai-tools
- The Times on AI meeting note-takers: https://www.thetimes.com/business/technology/article/ai-meetings-note-takers-work-g6vhhs3m8
- Wikipedia / source aggregate for Otter.ai: https://en.wikipedia.org/wiki/Otter.ai

Net effect on benchmark scoring:

- External-only top-10 overlap improves from 6/10 to 7/10.
- Store-first union top-10 overlap improves from 8/10 to 9/10.
- The remaining top-10 miss is Loom.
- WebSearch added explicit product/workflow evidence for Microsoft Teams Copilot and Notion AI Meeting Notes, which reinforces the need to separate company targets from product/workflow targets.

Updated interpretation:

Conversation intelligence now looks like a positive validation of the store-first union, with a scoring-model caveat. The union clearly beats any single feeder, but the benchmark must split company capture targets from product/workflow rows before the engine can graduate.

## Final Effect

The addendum does not change the lead recommendation:

- Telehealth: revise/downscope; broad cohort discovery is not ready.
- Conversation intelligence: promising; revise scoring around company versus product/workflow targets.
- Engine verb: do not graduate from this packet.

Follow-on note from Brian: the next attempt should first improve query construction over the same raw tools, not expand the tool surface. In particular, try SerpAPI/WebSearch/Exa queries generated from keywords and category language already present in the captured store profiles, with special attention to Exa `/search` prompts.
