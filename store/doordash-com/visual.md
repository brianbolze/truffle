---
schema_version: "1.0"
domain: doordash.com
captured_at: 2026-06-16
source_capture: 2026-05-31
qa_status: recapture-used
---

## Visual & brand impression

DoorDash reads as a disciplined single-accent brand: one signature red drives every CTA, wordmark, and nav button [color_01]; each audience gets its own deliberate hero color — burgundy, yellow, lilac — while red stays the lone accent [color_02], and every sub-brand footer locks back to the same red band [color_03]. Finish peaks on the consumer/about pages: clean text/photo splits [layout_01], a tight 2x2 category grid [layout_02], and a crisp gift/package/convenience card trio [layout_06] over a custom flat-illustration system [iconography_01][iconography_03]. The B2B pages slip — all-caps headlines collapse the type ladder [typography_04][typography_06], a raw two-tone comparison table reads utilitarian [color_06], and dasher's numbered circles and generic spot icons feel placeholder-tier [iconography_04][iconography_05]. Footers dump ~40 uniform SEO links [layout_10].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage hero
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: The consumer homepage hero lands a clean three-step type scale — large bold sentence-case headline, smaller bold subhead, small regular body — that reads instantly without color or caps tricks.
  visible_tells:
  - '''Everything you crave, delivered.'' is visibly the largest, heaviest element in the text column'
  - '''Your favorite local restaurants'' sits at a distinctly smaller bold weight above the regular-weight body paragraph'
  - Each step drops clearly in size, so headline > subhead > body is unambiguous
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage category grid (Beauty, Flowers, Restock, Pets)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-03-y03660.png
  claim: The four-up category block flattens to roughly two type levels with little size gap between card heading and body, and no parent section label, so the four cards read as undifferentiated peers.
  visible_tells:
  - Card headings ('Beauty essentials from top brands', 'Flowers for any occasion') sit close in size to the body line beneath them
  - No overarching section heading sits above the four cards to anchor them as a group
  confidence: medium
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage footer SEO link block
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-05-y05504.png
  claim: In the dark footer, section headers ('Popular Categories', 'Get to Know Us') are only marginally bolder than the links beneath them at an identical small size, so grouping rests almost entirely on a slight weight shift.
  visible_tells:
  - '''Popular Categories'' / ''Get to Know Us'' / ''Let Us Help You'' / ''Doing Business'' are the same size as the links below, separated only by a faint weight increase'
  - The 40+ category links all render at one uniform small size with no sub-dividers
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: poor
  page_or_region: Merchant page hero
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-00-y00000.png
  claim: The merchant hero stacks an all-caps heavy display headline over an all-caps earnings subhead, so headline and data-callout sit at the same caps register and the tier distinction collapses into one shouting block.
  visible_tells:
  - '''SIGN UP FOR DOORDASH AND UNLOCK SALES'' is large all-caps heavy lettering on the dark hero'
  - '''YOUR BUSINESS AROUND CENTREVILLE COULD EARN...'' directly below is also all-caps, only smaller — same treatment, weaker step'
  - Contrasts with the homepage hero's sentence-case three-step scale
  confidence: high
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: Merchant page FAQ
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-05-y06100.png
  claim: The merchant FAQ uses one calm type level — every question at the same size and weight on a consistent baseline with generous row spacing — making the list scannable with no secondary heading clutter.
  visible_tells:
  - All ~10 questions ('What are the pricing plan differences?', 'How quickly will I get paid?') share identical size and weight
  - Each row is just question text plus a right-aligned red chevron, with even white space between rows
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Merchant / Business headings — split-color caps device
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-02-y02440.png
  claim: A recurring two-tone all-caps heading device (one word in red, the rest in black/white) carries brand personality but competes with hierarchy — the color split reads as decoration rather than a level cue, and it repeats across pages.
  visible_tells:
  - '''SUPPORT'' in red joined to ''WHEN YOU NEED IT'' in black on the merchant page'
  - 'Same device on the business hero: ''FUEL YOUR EMPLOYEES WITH'' white, ''DOORDASH FOR BUSINESS'' red/orange, both uppercase at similar size'
  - Color, not size, does the work, so the words don't resolve into a clear parent/child relationship
  confidence: medium
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/business/tile-00-y00000.png
- id: typography_07
  family: typography_hierarchy
  polarity: strong
  page_or_region: Dasher page hero
  tile_path: store/doordash-com/captures/2026-05-31/tiles/dasher/tile-00-y00000.png
  claim: The dasher hero shows the widest headline-to-body ratio in the set — a large dark-purple all-caps headline dominating the panel, then a clearly smaller cash-back line, then the smallest fine print — a legible multi-step ladder.
  visible_tells:
  - '''WORK WHEN YOU WANT. EARN WHAT YOU NEED.'' is by far the largest element on the tile'
  - '''10% cash back*'' sits visibly smaller and lighter beneath it'
  - Asterisk terms line at the bottom is the smallest, lightest text, completing the ladder
  confidence: high
- id: typography_08
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Dasher page FAQ heading
  tile_path: store/doordash-com/captures/2026-05-31/tiles/dasher/tile-03-y03660.png
  claim: The dasher 'FREQUENTLY ASKED QUESTIONS' heading is rendered in large bold dark-purple all-caps that rivals a hero title in weight, dwarfing the regular-weight question rows below rather than reading as a subordinate section label.
  visible_tells:
  - '''FREQUENTLY ASKED QUESTIONS'' is a heavy, oversized purple display heading'
  - The question rows underneath are much smaller regular-weight black text, an abrupt jump with no mid-tier
  confidence: medium
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-05-y06100.png
- id: typography_09
  family: typography_hierarchy
  polarity: strong
  page_or_region: About page product feature cards
  tile_path: store/doordash-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
  claim: The about-page feature trio runs a tight two-level card type system — bold sentence-case heading then regular body — applied identically across all three cards, with parallel body offsets.
  visible_tells:
  - '''The gift that always delivers'', ''Save time with Package Pickup'', ''Convenience in your neighborhood'' are bold mid-size headings'
  - Body copy under each is the same smaller regular weight and begins at the same vertical offset across cards
  confidence: high
- id: typography_10
  family: typography_hierarchy
  polarity: mixed
  page_or_region: About page inline feature sections
  tile_path: store/doordash-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
  claim: The about-page alternating image/text rows use headings ('Whatever you need, when you need it', 'Your order delivered with care') only marginally heavier than their body paragraphs, with no caps or color reinforcement, so the heading-to-body distinction nearly collapses.
  visible_tells:
  - '''Whatever you need, when you need it'' is just slightly bolder and barely larger than the sentences beneath it'
  - No uppercase, color, or rule reinforces the heading; the step is weight alone
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage hero split + alternating modules
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: The homepage opens on a clean text-left / photo-right split and then repeats an alternating two-column image/text rhythm beneath it with consistent column proportions and implicit color-band dividers.
  visible_tells:
  - 'Hero: left text column on a shared margin, lifestyle photo filling the right half flush to the edge'
  - DashPass band below flips to image-left / text-right at a similar split
  - Section breaks are background-color changes rather than ruled lines, keeping the rhythm clean
  confidence: high
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage four-up category grid
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-03-y03660.png
  claim: The category promotion block resolves to a strict 2x2 grid of equal cells, each with heading and a red pill CTA at a matching position, with consistent column widths and row gutters.
  visible_tells:
  - Four cells (Beauty, Flowers, Restock the minibar, Pets) share uniform left margins
  - Each red CTA pill sits at the same offset below its heading; row and column spacing are even
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage neighborhood link grid
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-05-y05504.png
  claim: The 'Get more from your neighborhood' block is a tidy multi-column link grid with a precise tab-underline control (Top Cities / Top Cuisines / Top Chains) and city columns sharing one baseline grid.
  visible_tells:
  - Active tab marked by a clean underline rule, not a filled highlight
  - City links (New York, Houston, San Francisco...) align on a shared left edge and even line spacing across all columns
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: Merchant page hero signup form + 3-up product cards
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-00-y00000.png
  claim: The merchant hero seats a multi-field white signup card flush within the left text column without spilling into the photo bleed, and the 'Explore DoorDash Products' row below is three equal-height cards with matching image/label/CTA placement.
  visible_tells:
  - Rounded, shadowed form card sits left of the center divide; the photo bleeds only on the right
  - Marketplace / Commerce Platform / Reservations cards share identical height with color-differentiated header bands and CTAs at the same vertical position
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: Merchant page FAQ accordion
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-05-y06100.png
  claim: 'The merchant FAQ is one full-width accordion component repeated faultlessly across ~10 rows: even hairline dividers between items, uniform left text indent, right-aligned caret on every row.'
  visible_tells:
  - Thin rule dividers evenly spaced edge-to-edge within the content column
  - Red caret chevrons consistently right-edge aligned across all rows
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: About page 3-up feature card grid
  tile_path: store/doordash-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
  claim: The about-page gift/package/convenience trio is the tightest component finish in the set — equal rounded-rect cards, centered illustration in identical whitespace zones, headline and body starting at the same offsets, matching padding.
  visible_tells:
  - All three card borders and corner radii are visually identical
  - Each illustration is centered in an equal whitespace band; body copy begins at the same vertical offset in every card
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: Merchant page webinar 3-up card row
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-03-y03660.png
  claim: The webinar row keeps a 3-column grid but the cards carry unequal content weight — long versus short titles produce different text-block heights beneath the image area, undercutting the grid's implied equality.
  visible_tells:
  - Each card has a full-bleed image, but the headline lengths differ markedly (e.g. multi-line vs short), so the text blocks below land at different heights
  - The three cards therefore don't bottom-align cleanly despite sharing the grid
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: About page alternating text/image modules
  tile_path: store/doordash-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
  claim: The about-page alternating pairs are structurally sound but their column splits drift — one pair gives the image more room, the next gives the text more — so the rhythm reads approximate rather than grid-locked.
  visible_tells:
  - First pair (image left, 'Whatever you need...' text right) weights toward the image with a small square photo and wide empty text column
  - Second pair ('Your order delivered with care' left, image right) shifts the proportion, so the two rows don't share one ratio
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: Dasher page pay explainer section
  tile_path: store/doordash-com/captures/2026-05-31/tiles/dasher/tile-01-y01220.png
  claim: The 'How does Dasher pay work?' block floats a segmented Base Pay / Promotions / Tips pill control with no container or connector tying it to the text and screenshot below, so the control-to-content relationship is ambiguous from layout alone.
  visible_tells:
  - Pill tab row sits on open background with no anchor line or card linking it to the 'Base Pay' copy beneath
  - Large whitespace separates the tabs, the text block, and the product image with no containment grouping them
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: Homepage dense footer link block
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-05-y05504.png
  claim: The footer 'Popular Categories' area is a 4-column dump of ~40 links with no hierarchy between groups — every link identical in size, weight, and line height — reading as a flat wall of SEO text.
  visible_tells:
  - All ~40 link texts render at one size and weight with no subgroup headings or dividers inside the columns
  - Even inter-item spacing only reinforces the flatness rather than introducing legibility
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Across pages — single red on all interactive elements
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: One signature red governs every interactive element with discipline — primary CTA pills, the wordmark, and the nav Sign In button all share the same red, with no competing accent.
  visible_tells:
  - Red 'Find restaurants' CTA pill in the hero
  - Red 'Sign In' pill top-right in the nav
  - Red DoorDash wordmark and red 'Get Started' button on the DashPass band all match the same hue
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: Audience-segmented hero backgrounds (merchant / dasher / about)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-00-y00000.png
  claim: Each audience gets its own deliberate hero background — deep burgundy for merchants, warm yellow for dashers, pastel lilac for about/consumer — while red stays the sole CTA accent, showing controlled palette segmentation rather than reused backdrops.
  visible_tells:
  - Merchant hero is a deep wine-red full bleed; consumer homepage hero is light blush/white by contrast
  - Dasher hero is a warm yellow panel; about page is pastel lilac — yet the red CTA pill and logo are unchanged in every case
  confidence: high
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/dasher/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: Sub-brand footers (merchant / business / dasher)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-05-y06100.png
  claim: Every sub-brand footer resolves to the same bright red band with a white-reversed wordmark lockup, locking the parent identity regardless of the audience color context above it.
  visible_tells:
  - Solid red footer with white 'DOORDASH for Merchants' lockup on the merchant tile
  - Same red footer band with white 'DOORDASH for Business' / 'for Dashers' lockups on the business and dasher tiles
  confidence: high
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/business/tile-05-y06100.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Merchant page product cards (Marketplace / Commerce Platform / Reservations)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-00-y00000.png
  claim: The three product cards use red, teal, and purple header bands — a tri-color set introduced only here, with no secondary palette elsewhere on the site to ground it, so the hues read as assembled for differentiation rather than systemic.
  visible_tells:
  - Leftmost card red header, center teal/green, right purple/plum
  - No matching secondary-color system appears on other tiles to justify these three
  confidence: medium
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Merchant page photography
  tile_path: store/doordash-com/captures/2026-05-31/tiles/merchant/tile-02-y02440.png
  claim: Merchant-page photography mixes a dark warm-toned kitchen testimonial shot with a brighter daylit portrait below it, without a shared color grade, so the section reads as assembled from separate shoots rather than one merchant brief.
  visible_tells:
  - Dark, warm kitchen/testimonial image in the upper band
  - Brighter, cooler-exposed portrait below it — different color temperature and framing, no unifying grade
  confidence: medium
- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: Business page comparison table
  tile_path: store/doordash-com/captures/2026-05-31/tiles/business/tile-01-y01220.png
  claim: The DoorDash vs DoorDash for Business comparison is a plain white card beside a solid dark-red card with no icon, illustration, or graphic device — a raw two-tone block that reads as a utilitarian spec sheet rather than a designed brand moment.
  visible_tells:
  - Left 'DoorDash' column is an untreated white card; right 'DoorDash for Business' column is a flat dark-red card
  - Both columns are checkmark-text lists with no embellishment carrying brand language into the comparison
  confidence: medium
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Business page comparison table — column height imbalance
  tile_path: store/doordash-com/captures/2026-05-31/tiles/business/tile-01-y01220.png
  claim: Within the same comparison block, the dark-red 'for Business' column carries many more checklist items than the white 'DoorDash' column, so the two columns terminate at very different heights and the shorter one floats without a shared baseline.
  visible_tells:
  - Left white column ends well above the bottom of the right red column
  - The red column's longer list leaves the white column's bottom edge ungrounded
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: About page category cards (Restaurants / Grocery / Convenience)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
  claim: The three about-page category cards run a custom flat-illustration system with consistent geometric language, flat fills, and a warm accent palette tied to brand red — not clip-art.
  visible_tells:
  - Purple-blue fork-and-knife rendered as a flat paired silhouette
  - Banana-and-carton and snack-bag illustrations share the same flat-fill discipline and a red-orange accent matching brand red
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: About page feature cards (gift envelope / box / DashMart storefront)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
  claim: Two of the three feature illustrations show branded craft (DoorDash-logo envelope, red DashMart storefront with the brand mark) but the central package is a generic 3D shaded box in a different rendering style, breaking the flat-illustration language.
  visible_tells:
  - 'Center card: orange-brown box drawn with 3D shading, unlike the flat flanking illustrations'
  - Left envelope uses flat purple fill with the red D-mark; right storefront is flat red with the brand asterisk — both on-system
  confidence: high
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: Business page product carousel (Meal Budgets / Catering / Meal Manager)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/business/tile-00-y00000.png
  claim: The business page deploys a cohesive custom flat-people illustration set — figures with warm fills, consistent limb/head proportions, no outline stroke, and a shared palette with red accents — indicating a purpose-built library rather than stock.
  visible_tells:
  - 'Meal Budgets card: figure with shopping bags in ochre and muted red, flat limb geometry'
  - Catering and Meal Manager cards reuse the same proportions and fill discipline with consistent red accent clothing
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: Dasher page requirements section (Age / Vehicle / Documentation)
  tile_path: store/doordash-com/captures/2026-05-31/tiles/dasher/tile-02-y02440.png
  claim: The requirements row carries no real iconography — just three red numbered circles (1, 2, 3) acting as sequence markers, with the labels doing all the work and no icon distinguishing the categories.
  visible_tells:
  - Three red filled circles with white numerals above 'AGE', 'VEHICLE', 'DOCUMENTATION'
  - No illustrative or category-specific icon accompanies any of the three
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: Dasher page value-prop spot icons
  tile_path: store/doordash-com/captures/2026-05-31/tiles/dasher/tile-00-y00000.png
  claim: The three dasher value-prop spot icons are tiny low-detail silhouettes with a single accent color, generic enough to be interchangeable with any gig-economy competitor's set — a step down from the custom illustration on the business page.
  visible_tells:
  - '''Work When You Want'' icon is a small plain person silhouette with no distinctive form'
  - All three sit at near-identical small square sizes with one accent color and no iconographic craft at that scale
  confidence: medium
  contrast_with: store/doordash-com/captures/2026-05-31/tiles/business/tile-00-y00000.png
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage footer social and app-store badges
  tile_path: store/doordash-com/captures/2026-05-31/tiles/homepage/tile-05-y05504.png
  claim: Footer social icons (X, Facebook, Instagram, LinkedIn) and the App Store / Google Play badges are off-the-shelf third-party assets with no attempt to bring them into the site's brand register or palette.
  visible_tells:
  - Standard monochrome social glyphs on the footer strip, unmodified
  - Default-styled 'Available on the App Store' and 'Google Play' badge lockups, not adapted to the brand palette
  confidence: high
```

## Provenance

- **Tiles mined — 27 active across 5 pages** (`captures/2026-05-31/tiles/`):
  - **homepage** (consumer, `www.doordash.com`): tiles 01–05 · *tile-00 excluded* — sign-in modal + dark scrim cover the hero.
  - **merchant** (`get.doordash.com`): tiles 00–05 · *tile-06 excluded* — site-wide cookie banner over the footer legal strip.
  - **business** (`work.doordash.com`): tiles 00–06 · **Tier-B `--dismiss` re-render** — the cookie banner was cleared via the page's own affordance (top nav kept); manifest `dismissed: true`, `scroll_locked: false`.
  - **dasher** (`dasher.doordash.com`): tiles 00–03 · *tile-04 excluded* — cookie banner over the footer.
  - **about** (`www.doordash.com/about/`): tiles 00–04 · *tile-05 excluded* — cookie banner over the footer.
- **QA — `recapture-used`:** the business page supplied its tiles from a `scripts/shoot.py --dismiss` browser re-render (real Chrome), which cleared the bottom cookie consent banner. A Tier-B `--dismiss` re-render of the consumer **homepage** — intended to recover the modal-covered hero — was **blocked by a Cloudflare "verify you are human" interstitial**: `www.doordash.com` walls headless Chrome (the `work./get./dasher.` marketing subdomains do not), so the homepage falls back to its cached Tier-A tiles with the modal hero excluded.
- **Exclusions — 4 tiles:** 1 sign-in modal (homepage hero, unrecoverable behind the bot wall) + 3 site-wide cookie banners (merchant / dasher / about footers). The cookie banner is a faithful capture-fact; it was dismissed only on the business Tier-B render, and on the cached pages it sits over the low-value footer legal strip, so the tile is dropped rather than mined.
- **Snapshot caveat:** evidence reflects tiles captured **2026-05-31** (business page re-rendered **2026-06-16**). DoorDash's marketing pages change often and are audience-segmented — this is a point-in-time read, and note that the consumer homepage hero (the most load-bearing tile) is *absent* from the evidence, lost to the modal + bot-wall.
