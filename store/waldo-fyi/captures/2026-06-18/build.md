<!--
source_url: https://waldo.fyi/build
captured: 2026-06-18
-->

![](https://www.waldo.fyi/images/build/hero-ring.png)

![](https://www.waldo.fyi/images/build/hero-ring-labels.png)

Signals indexed8,123last sync · 0 min ago

![](https://www.waldo.fyi/images/build/hero-ring.png)

![](https://www.waldo.fyi/images/build/hero-ring-labels.png)

Build

# A unified brand intelligence layer for your agents & teams.

Track brand activity, monitor category trends, and keep

a pulse on your audience via direct API or MCP.

[Join the waitlist](https://www.waldo.fyi/build#get-key)

Case study

Case study

API

What hooks has Liquid Death been using over the past month?

GET /brands/brand\_ld/ads/active

TOP HOOK

“Murder your thirst" — performance variant

Running 47 days · 12 variants

scaling

RISING ANGLE

Healthcare-worker testimonial

New this week · 4 variants

new

LONGEVITY LEADER

Mountain-spring origin story

Running 112 days · steady

evergreen

Brand dataCategory dataAudience data

Enrichment

SentimentRelevancePerceptionProduct TypeTopic ClusteringReach

Structuring

NormalizationDeduplicationResolution

Owned media

Paid Media

Email & Newsletters

Mentions

Reviews & Ratings

Hiring & Org

Search & SEO

Website

reddit

tiktok

youtube

instagram

x.com

linkedin

meta ads

google ads

GWI

substack

trustpilot

glassdoor

API

Have any of our competitors changed their landing page recently?

GET /brands/brand\_poppi/lp-changes

HERO SWAP

Poppi · "Better for you" → "Functionally delicious"

2 days ago · headline + hero image

Detected

OFFER CHANGE

Olipop · 15% bundle → free shipping over $40

5 days ago · CTA + price block

Detected

FORM CHANGE

Athletic Greens · added quiz before checkout

1 week ago · funnel reroute

Detected

Brand dataCategory dataAudience data

Enrichment

SentimentRelevanceBrandProductTopic auto-clusteredReach

Structuring

NormalizationDeduplicationEntity resolution

Industry News

Trending Topics

Competitive Landscape

Channel & Format

Seasonality

Voice of Customer

Emerging Needs

Website

reddit

tiktok

youtube

instagram

x.com

linkedin

meta ads

google ads

open web

linkedin

trustpilot

glassdoor

google

API

Which brands do new parents trust most right now?

GET /audiences/new\_parents/brands

Top Brand · relevance 0.97

Honest Company

23k mentions · sentiment positive

Trusted

Rising Brand · relevance 0.84

Frida Baby

Gaining fast · 4 new products mentioned

Rising

Losing Trust · relevance dropping

Johnson & Johnson

Sentiment shift −0.31 · 30d

Declining

Brand dataCategory dataAudience data

Enrichment

SentimentRelevanceBrandProductTopic auto-clusteredReach

Structuring

NormalizationDeduplicationEntity resolution

Segments

Communities

Influencers

Conversations

Voice of Customer

Emerging Needs

Awareness

Website

reddit

tiktok

youtube

instagram

x.com

linkedin

meta ads

google ads

open web

linkedin

trustpilot

glassdoor

google

SELECT DOMAIN ↓

THREE DOMAINS

## All the brand, category, and audience data you need.In one place.

Brand

### Owned, paid, and earned media for any brand

Posts, ads, landing pages, website snapshots, mentions, and platform stats scanned daily.

GET

/brands/search

GET

/brands/{id}/ads/active

GET

/brands/{id}/website/analysis

GET

/brands/{id}/owned-media/posts

Audience

### What the people around a brand are saying & feeling

Audience segments derived from real followings, with top voices and the verbatim conversations they’re having.

GET

/audiences/search

GET

/audiences/{id}/insights

GET

/audiences/{id}/conversations

GET

/audiences/{id}/posts

Category

### What’s going on across the whole category

News, trending topics, common angles, creative — the competitive set as one, queryable surface.

GET

/category/{id}/trends

GET

/category/{id}/angle-library

GET

/category/{id}/ads/new

GET

/category/{id}/news

THREE ANALYSIS MODES

## Raw, aggregated, and/or analyzed data.

The same data, three different ways. Pull only what your team or agent needs to do its job.

![](https://www.waldo.fyi/images/build/analysis-raw.png)

Raw sources

### Data in its purest form

Posts, ads, engagement metrics, audience conversations— exactly as collected. Clean, structured data from the verbatim source material.

![](https://www.waldo.fyi/images/build/analysis-aggregated.png)

Aggregated

### Summaries & snapshots

Cadence, share-of-voice, spend estimates, distribution by platform, and more. A full “dashboard read”, from just one call.

![](https://www.waldo.fyi/images/build/analysis-analysis.png)

Analysis

### Expert insights

Tone, themes, creative scoring, audience sentiment, and more— from agents trained by brand experts. Proactive answers for fast loops.

BUILT FOR BUILDERS

## Some ways agents and teams are putting Build to work.

The API layer behind every agent, app, and workflow across brands, audiences, and categories.

Vibe MarketersBrand teamsAgenciesDevelopers

Illustrative examples

### Brief-writing agent

Point Claude at a brand and a category. It pulls the angle library, the active ads, the audience verbatims — and drafts the brief end-to-end. Edit at the end, not the start.

### Creative-fatigue auditor

A weekly cron hitting the brands you run. Pings you which creative is going stale before CTR craters.

/brands/{id}/lp-changes

### Side-by-side scouting in your chat

“Show me Liquid Death and Poppi's last week of ads, ranked by longevity.” Cards stream back into your Claude project — no tabs, no exports.

![AICPA SOC 2 attestation badge](https://www.waldo.fyi/images/build/secure.png)

## Secure and private.

SOC-2 Type II certified.

Your data is never shared or used to train AI models.

## Intrigued? Get your API key.

Build is in early access. Join our waitlist below, and we'll be in touch with next steps to get you access.

What are you building?

Join the waitlist →

Customer stories

"Waldo lets us move faster without sacrificing depth, freeing our people to focus on what truly matters: bold, creative thinking only humans can deliver."

Tracey Faux-Pattani

CEO

“Waldo helped us cut two-week research cycles to three days, eliminate $30K in redundant tools, and reclaim 100+ hours a month to focus on thinking, vs. stitching data together.”

[Case study](https://www.waldo.fyi/petermayer-case-study)

Michelle Edelman

CEO & CSO

"Speed-to-insight is an important factor for us, and with Waldo's workflows we can save thousands of hours of tedious desk research to get there faster."

Anita Schillhorn

Executive Director of Strategy

"Waldo helps ground us in _real_ consumer behavior — sentiment, competitive moves, trends. We move faster, create work that resonates more deeply, and drive stronger impact."

Leah Swalling

Director of Brand Management

## FAQs

What’s the difference between Waldo’s API vs. MCP server?

Same data and tools, two ways in. The API is for back-end jobs, schedulers, and your own agent runtimes to build anything you want. The MCP server is what you point Claude at when you want the data (or workflows) to show up inside a chat session. Same auth, same response shape, same endpoints. You can just pick whichever fits where the work is happening.

Can I enable this for my whole organization at once?

Of course! For Claude, an admin can install the MCP connector at the org level, and individual users sign in through the auth flow once to get access. For the API, you can issue scoped keys to different teams or environments. Credit pools are shared at the org level by default, and we can scope them by team if you want hard limits.

How fresh is the data?

Brand, audience, and category data is collected and scanned daily. Website snapshots, owned media, paid media, mentions, and category news all refresh on a 24-hour cycle. Enrichment endpoints (post lookups, profile lookups, video transcripts) and Discover endpoints hit the underlying platforms live at request time, so those are real-time.

What if the brand or audience I want isn’t tracked yet?

You have two paths: 1) use our Discover endpoints to query platforms live without indexing, which is great for one-off research, or 2) activate the brand, category, or audience and we’ll add it to the tracked index, with daily data collection going forward.

Will this conflict with other connectors I’m already running in Claude?

Not at all. Waldo is one MCP block in your mcp.json, and it sits alongside whatever else you’ve got connected — your first-party data, your CRM, your code, your design tool. Claude routes to whichever tool fits the question. The Waldo tools are clearly scoped to brand, category, and audience surfaces, so there’s no overlap with general-purpose connectors.

How is this different from a social listening tool?

Social listening tools are built for humans clicking through dashboards. Waldo is built for agents reading and reasoning over the source material. You get the raw posts, ads, snapshots, and verbatims, instead of just a sentiment chart. Your agents (or users) can pull an angle library for a brief, compare two competitors’ last week of creative, or mine audience language for copy. The same surface also returns analysis if that’s what you want. You pick the layer per call, and Waldo’s data and outputs are piped directly to you to view instantly, or power whatever you’re trying to build on top of it.

How does pricing work?

It’s credit-metered, so you pay for what you use, with volume discounts as you scale. Every call draws down from your pool based on what it’s doing. Raw list endpoints are inexpensive (1 credit per ~20 results), and analysis endpoints that do the reasoning for you cost more (typically ~5 credits). Activating a custom brand, category, or audience that isn’t already in our tracked index is an annual fee on top. This way, there’s no per-seat pricing, or per-brand minimums. If your team uses it heavily one month and lightly the next, you only pay for what you used.

## Want more? See how else Waldo can power everything your team needs.

### Strategize

Spar with Strategy Agent & launch one-click workflows.

[Get started](https://www.waldo.fyi/subscribe/strategize) [Learn more](https://www.waldo.fyi/strategize)

### Pitch

A winning pitch playbook, in an hour.

[Get started](https://www.waldo.fyi/quick-pitch) [Learn more](https://www.waldo.fyi/pitch)

### Monitor

Always-on intelligence briefs you can talk to.

[Book a demo](https://www.waldo.fyi/contact?what_are_you_looking_to_do=Monitor+brands+and+competitors) [Learn more](https://www.waldo.fyi/monitor)