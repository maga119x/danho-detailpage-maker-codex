# Mobile Screen Storyboarding

Use this before building or revising HTML. The page should be designed as a sequence of mobile screens, not as a list of identical sections.

## Core Rule

One visible screen should complete one purchase judgment.

Bad:

- headline, paragraph, image, feature cards, comparison, and caveat all in one section
- every section uses the same `eyebrow -> h2 -> lead -> image -> card` skeleton
- one source bullet becomes one dense section

Good:

- split a major content point into multiple screen units
- decide the visual lead for each screen
- alternate image, type, proof, and information density
- keep claim and evidence close

## Opening Pair Storyboard

Storyboard the first two screens together before building section HTML.

| Screen | Visual job | Copy job |
|---|---|---|
| 01 | product/result promise, strong first-glance identity | name the product/use case and desired change |
| 02 | same scene continued, closer crop, before friction, or buyer hesitation | make the buyer recognize why the promise matters |

Rules:

- Section 02 must share a visual or verbal anchor with section 01: product, object, action, place, color motif, or emotion.
- Section 02 should have enough substance to create empathy: a scene image, 2-3 short beats, a quote/checklist, or a before/current workaround visual.
- Do not build section 02 as a generic centered problem statement that could follow any hero.
- If the first two screens feel disconnected in the browser screenshot, revise section 02 before inspecting later sections.

## Screen Unit Types

| Screen role | Job | Primary element | Common pattern |
|---|---|---|---|
| `impact` | stop scroll and define the frame | result image, comparison, bold claim | comparison hook, result-first hero |
| `question` | open the next idea | short question or declaration | vertical line, wide space, type-dominant |
| `explainer` | make a mechanism understandable | diagram, detail, parts | callout map, spec pair, simple arrows |
| `result` | show the desired outcome | product-in-use or after-state | large photo + one-line result |
| `proof` | make a claim credible | review, certificate, number, measurement | proof board, review highlight, graph |
| `compare` | make the choice obvious | winner vs alternative | color vs gray comparison |
| `catalog` | show range without long copy | grid or stacked examples | 2-column visual grid |
| `info` | organize buyable facts | cards, rows, FAQ, specs | option cards, compatibility notes |
| `policy` | provide operational facts | calm long text | quiet policy zone |

## Visual Mass

Every screen must have one dominant mass.

| Visual mass | Use when | Screen composition |
|---|---|---|
| `image-dominant` | emotion, result, use, lifestyle | image 55-80%, text 10-25% |
| `type-dominant` | question, declaration, chapter turn | text 30-45%, space 35-55% |
| `proof-dominant` | certificate, review, measurement, graph | proof 45-70%, title 15-25% |
| `card-dominant` | options, specs, FAQ, components | cards/rows 60-80% |

If all elements have similar visual weight, the screen will look weak.

## Sparse Section Image Gate

Use `SPARSE_SECTION_IMAGE_REQUIRED` when a screen has too little content to earn a standalone HTML section:

- kicker + headline + one short lead only
- one note box below the headline
- 1-2 small cards with short option, care, value, or reassurance copy
- a transition/result/value screen with no product, lifestyle, proof, or review visual

Required fixes:

- convert it to `FULL_IMAGE` when the whole screen should be a designed image section
- convert it to `IMAGE_STORY` when one large product/use/result image can carry the meaning with minimal HTML copy
- keep it as HTML only when it gains a large `HTML_MIXED` support image or merges with adjacent proof/detail content

Do not fix sparse screens by adding blank height, oversized padding, or a dark background. Vertical length must come from meaningful visual content.

## Tempo

Control information density across the page.

| Tempo | Meaning | Examples |
|---|---|---|
| `low` | one message, much space, fast understanding | result image, question, declaration |
| `medium` | one claim plus supporting detail | feature proof, usage scene, short comparison |
| `high` | multiple facts for decision | option cards, FAQ, specs, reward summary |

Rules:

- Do not place two high-tempo screens back to back unless the second is final FAQ/policy.
- Do not place three low-tempo screens back to back unless they are an intentional opening sequence with strong images.
- Insert a low or medium screen between dense option/spec/FAQ screens when the page is not yet at the end.

## Content Expansion

For each key claim, choose the necessary screen chain.

### Core Benefit Chain

```text
result screen -> question screen -> mechanism/detail screen -> proof screen
```

Use when the benefit is central to purchase.

### Problem/Solution Chain

```text
problem scene -> current workaround friction -> product answer -> after-state
```

Use when empathy or behavior change matters.

### Technical Claim Chain

```text
desired result -> principle diagram -> part/spec close-up -> measured/certified proof -> buyer gain
```

Use for technical, material, or functional products.

### Option/Reward Chain

```text
overview -> item cards -> set summary -> mutable price/order guidance -> compatibility/FAQ
```

Use for sets, reward pages, bundles, subscriptions, or any product with many variants.

## Surface Roles

Background should signal the screen's job.

| Surface role | Use for |
|---|---|
| `paper` | normal product, use, feature, and explanation screens |
| `warm-lifestyle` | gift, home, lifestyle, emotional screens |
| `dark-proof` | authority, awards, results, contrast, launch proof, final confidence |
| `accent-declaration` | short strong statement or chapter break |
| `policy-quiet` | FAQ, legal, shipping, AS, long caveats |

Avoid five or more consecutive `paper` sections unless the later screens are quiet policy.

## Proof Proximity

Strong claims need nearby evidence.

- If the screen says "strong", "safe", "different", "easy", "premium", "fast", "lasting", or "special", place proof in the same screen or the next screen.
- Proof can be photo, measurement, certificate, review, comparison, spec, or clear use scene.
- If proof is unavailable, soften the copy and mark `NEEDS_PROOF` only in internal planning logs.

## Crop Strategy

Images should be cropped for the screen role.

- `result`: product and outcome both visible; result should be visually appetizing/clear.
- `usage`: hands or context included for scale and action.
- `detail`: close-up crop, enough negative space for nearby labels.
- `comparison`: matched crops and equal framing; winner receives stronger color treatment.
- `catalog`: consistent ratio, short labels, no long text inside the image.
- `mood`: larger negative space, product still recognizable.

Do not insert images as decoration. Every image needs a persuasive job.

## HTML Build Rule

Build screen classes by role and mass, then place content inside.

```html
<!-- Core Result Screen -->
<section id="rice-result" class="detail-screen screen-result image-dominant paper tempo-low">
  ...
</section>

<!-- Mechanism Screen -->
<section id="heat-mechanism" class="detail-screen screen-explainer proof-dominant paper tempo-medium">
  ...
</section>
```

Use these classes as design intent markers. They do not replace semantic IDs or comments.

## QA Checklist

At 860px source width and in the 438px scaled phone preview:

- first 3 screens show identity, benefit/result, and difference or fit condition
- first 2 screens form a connected opening pair, not a hero plus abrupt second slide
- every screen has one primary visual mass
- no key benefit is compressed into one dense screen
- no `SPARSE_SECTION_IMAGE_REQUIRED` screen remains centered text-only, note-only, or tiny card-only
- no three screens in a row share the same layout skeleton
- claim and proof are within one screen of each other
- dense information appears later or is split into multiple screens
- options, compatibility, FAQ, policy, and prices remain editable HTML

Do not use a direct 393px/438px viewport as the primary storyboard QA, because it checks a reflowed mini webpage instead of the 860px ecommerce detail-page source scaled for phone viewing.
