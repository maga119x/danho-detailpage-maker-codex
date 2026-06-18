# Image Prompt Guide

Use structured natural-language prompts for GPT Image 2.0 (`gpt-image-2`) through the built-in Codex `image_gen.imagegen` path.

This guide is tuned for Korean ecommerce 상세페이지 section images, not generic art prompts.

## Image Count Rule

Do not impose a maximum image count, fixed percentage, or fixed full-section/HTML split. Prompt every approved `FULL_IMAGE` and `HTML_MIXED` asset needed for the page's story, proof, option, care/storage, comparison, review, sparse-section, and final decision roles. If that results in many images, keep the queue and generate them in manageable independent native batches.

## Prompt Assembly Order

For every final prompt, write the brief in this order:

1. `Output purpose`: full-section detail-page artwork, support product photo, proof visual, comparison visual, or CTA artwork.
2. `Buyer screen role`: hook, problem, answer, proof, fit check, use scene, review support, options support, FAQ support, or final CTA.
3. `Main purchase judgment`: the one thing the buyer should understand from this image.
4. `Product / scene`: product identity, action, environment, props, and what must stay visually clear.
5. `Layout`: vertical mobile crop, hierarchy zones, negative space, safe margins, and where product/text/cards sit.
6. `Style`: commercial photo, editorial detail-page design, premium catalog, clean infographic, tactile proof scene, etc.
7. `Color / lighting`: use the page Key/Main/Sub/Exception system and avoid unrelated accent colors.
8. `Text contract`: exact short lines only for full-section images; no text for support images.
9. `Preserve / avoid`: product consistency, no random text, no extra labels, no fake marks, no watermarks.

Do not rely on vague adjectives such as `premium`, `modern`, or `high quality` alone. Pair them with concrete visual facts: surface material, lighting direction, camera angle, product placement, typography style, card count, spacing, and background behavior.

## Full-Section Ecommerce Design

Use this for `FULL_IMAGE` or designed `REPLACE` sections where the image model creates the complete section: background, product scene, Korean typography, cards, icons, and layout.

If a section is marked `FULL_IMAGE`, this is mandatory production work. Do not convert it to a textless support image or HTML overlay to avoid Korean typography risk. Incorrect Korean text means regenerate or revise the native full-section image.

### Base Template

```text
Create a complete Korean ecommerce product detail page section image, include content and design, not a plain photo.

Output purpose:
- full-section mobile detail-page artwork for [section id]
- screen role: [hook/problem/answer/proof/review/final CTA]
- main purchase judgment: [one clear buyer conclusion]

Product and scene:
- [product name and visible identity]
- [action/use/result scene]
- [props/background only if they support the buying point]

Layout:
- vertical mobile ecommerce composition
- strong first-glance hierarchy: [product / headline / proof card / result scene]
- safe margins on all edges; no cropped typography
- [product position], [text position], [supporting card/icon position]
- designed section, not a website screenshot and not a raw product photo

Korean text:
- render only these exact lines, verbatim, no extra characters:
  "[short line 1]"
  "[short line 2]"
- typography: clean bold Korean sans-serif, high contrast, generous line spacing

Style:
- [clean commercial / premium editorial / warm lifestyle / proof-board]
- restrained color system: Key [color], Main [color], Sub [color], Exception [color only if needed]
- product photography integrated with simple cards or proof cues

Constraints:
- no random Korean, no extra English, no lorem ipsum
- no direct numeric prices, no sales channel names
- no watermarks, no fake logos, no distorted product
```

### When Product References Exist

Add this block near the top:

```text
Use the attached product reference image as the source of truth for the product.
Preserve the same product silhouette, proportions, material, color, finish, logo/package marks when visible, and distinctive parts.
Generate a new ecommerce section design; do not copy the reference photo as-is and do not replace it with a generic object.
```

In these prompt snippets, "attached product reference image" means a product image already made visible in the Codex conversation context with `view_image` and then used through the built-in `image_gen.imagegen` GPT Image 2.0 (`gpt-image-2`) path. It does not mean an API file parameter or CLI input.

### Strong Candidates

Use full-section design images for:

- hook with product identity and outcome
- vivid problem scene
- product answer or mechanism reveal
- no-damage / safety proof moment
- emotional daily-use result
- comparison or value frame with very short labels
- low-copy result, value, reassurance, or transition section that would otherwise become a sparse text-only HTML block
- final CTA with short action text

Do not use full-section images for dense specs, price tables, option matrices, compatibility rules, long FAQ, policy text, or any mutable facts. Keep those in HTML.

## Support Photo / Visual

Use this when HTML keeps the copy and the image supports comprehension.

```text
Create a realistic product/lifestyle support image for a Korean ecommerce detail page.

Output purpose:
- support visual for [section id]
- screen role: [detail/proof/use/comparison/review support/FAQ support]
- main visual job: [show installation / show scale / show material / show result / show fit]

Subject and action:
- [product or component]
- [specific action or static product detail]
- [hand/context/setting if useful]

Composition:
- vertical mobile-friendly crop
- product clearly visible and not cropped
- clean negative space for editable HTML copy
- [close-up / overhead / straight-on / 45-degree / matched comparison framing]

Photography:
- clean commercial product photography
- [soft daylight / studio side light / neutral shadow / tactile close-up]
- realistic scale, natural reflections, believable contact shadows

Constraints:
- no text, no Korean caption, no overlay text, no signage with letters, pure visual
- no watermarks, no fake labels, no distorted product
```

If product references exist, add:

```text
Use the attached product reference image as the source of truth. Preserve product identity while generating a new scene. Do not use the original photo as the final output without transformation.
```

## Detail-Page Section Patterns

Use these patterns to avoid generic stock-like images.

| section role | prompt focus | avoid |
|---|---|---|
| hook | product identity + buyer outcome + large first-glance hierarchy | abstract mood image with tiny product |
| problem | real use friction, one moment, visible inconvenience | staged suffering or exaggerated mess |
| answer | product mechanism in action, before/after implied | feature list floating in space |
| proof | close detail, material, installation, measurable-looking cue without fake numbers | unsupported certifications or fake test labels |
| comparison | matched framing, two clear states, minimal labels if full image | many columns or dense text |
| review | replacement-safe review mood, checking points, product-in-use context | fake names, stars, dates, or "real buyer" claims |
| options | components laid out cleanly, editable option facts left to HTML; use as a large support visual when option copy is short | fixed prices or mutable availability |
| care/value | storage, cleaning, durability, or value scene that gives a short section enough visual length | empty lifestyle mood or text-only note box |
| FAQ | one visual clarification for a common doubt | text-heavy answer image |
| final CTA | product/result + one static closing or option-area cue + confident ending | two competing CTA messages, buttons, link-button shapes, rounded CTA controls |

## Opening Pair Prompting

When section 01 and section 02 are both generated or image-supported, prompt them as a pair even though each image is generated in an independent native call.

Section 01 prompt should define:

- product/category identity
- desired result or sharp promise
- strongest first-glance visual hierarchy

Section 02 prompt should continue:

- same buyer situation, product, action, place, color motif, or emotional cue
- a closer lived moment, repeated friction, current workaround, or first doubt caused by the hero promise
- enough visual substance for empathy: person/action, product scale, surrounding context, or before-state

Do not make section 02 a generic problem photo that could follow any hero. It should feel like the next frame in the same detail-page story while still carrying a different purchase judgment.

Add a continuity note to both prompts when useful:

```text
Opening pair continuity:
- This image should visually connect to section 01/02 through [shared product/action/location/color motif].
- Keep the buyer journey continuous, but avoid duplicating the exact same crop or headline.
```

## Korean Typography Contract

GPT Image 2.0 is stronger with text than older image models, but 상세페이지 production still needs a strict text contract.

For full-section images:

- Use 1-2 short Korean lines by default.
- Put exact lines in quotes.
- Say `render only these exact lines, verbatim, no extra characters`.
- Specify text placement and typographic role: headline, short badge, proof label, or CTA.
- Keep large safe margins and high contrast.
- Avoid small body copy, FAQ copy, direct prices, option terms, long compatibility caveats, or policy text.
- Do not ask for button UI, purchase buttons, link-button shapes, rounded CTA controls, or button-like labels. Use static typography, non-clickable labels, dividers, product composition, and option-area cue text instead.

For support images:

- Always require: `no text, no Korean caption, no overlay text, no signage with letters, pure visual`.
- If text appears anyway, retry with stronger no-text wording or move to an image crop where signs/labels are not plausible.

Retry ladder for Korean text:

1. Remove every nonessential word.
2. Reduce to one headline line or two short fragments.
3. Increase text size and simplify background.
4. Regenerate the native full-section image with the shorter exact text.
5. If mandatory `FULL_IMAGE` text still fails, mark `FULL_IMAGE_TEXT_QA_BLOCKED` instead of silently shipping HTML overlay or textless imagery.

Do not solve failed Korean typography by rendering HTML as an image, making a browser screenshot, drawing SVG/canvas, or compositing text locally.
Do not solve mandatory `FULL_IMAGE` typography failure by removing the text from the image. That is a role change and requires explicit user approval.

## Product Consistency

When reference images exist, make product consistency more important than scene creativity.

Include these locks when relevant:

```text
Preserve exact product silhouette and proportions.
Preserve material, finish, main color, accent color, logo/package marks when visible, and distinctive components.
Do not invent extra buttons, holes, labels, accessories, seams, ports, or package variants.
Do not replace the product with a generic stock object.
```

For catalog-like product visuals:

- ask for centered product, crisp silhouette, clean edge, no halo/fringing
- use opaque plain background unless the final asset is meant to be a lifestyle scene
- request light polish and realistic contact shadow, not restyling

For lifestyle scenes:

- keep the product large enough to inspect
- show one clear use action
- describe the setting with practical detail, not mood words only

## Layout Quality Rules

Full-section image prompts must behave like a mobile art-direction brief:

- one screen, one purchase judgment
- one dominant visual mass: product, result scene, type, proof card, or comparison
- 2-4 supporting elements maximum
- clear top/middle/bottom reading order
- negative space where HTML may need to sit near the image
- product appears within the first visual glance unless the screen intentionally delays reveal
- no repeated layout skeleton across consecutive generated sections
- no button UI or button-like rounded rectangles in any generated 상세페이지 section
- sparse section support images must be visually substantial: product, hand/use scene, option/component layout, care/storage scene, proof/comparison, or review context should occupy the main visual area
- do not create small decorative thumbnails for `SPARSE_SECTION_IMAGE_REQUIRED` sections

For tall mobile detail-page sections, ask for a vertical composition. When the runtime does not expose size controls, express the crop in the prompt, for example:

```text
vertical mobile ecommerce composition, tall portrait crop, designed to read on a 393px-wide phone screen
```

## Color

Use the page color roles:

- Key: dark anchor or brand base
- Main: main accent
- Sub: quiet surface, tint, or neutral
- Exception: warning or urgency accent only when needed

Avoid asking for many accent colors in one image. If the project has a `DESIGN.md`, map exact color names into the prompt.

## Negative Phrases

Use concise negative phrases. Overloading negatives can make the prompt noisy.

Recommended:

```text
no cheap infographic style, no cluttered layout, no random letters, no extra Korean, no cropped typography, no distorted product, no fake logos, no watermarks, no excessive colors
```

For support images:

```text
no text, no Korean caption, no overlay text, no signage with letters, pure visual
```

For reference-based product images:

```text
no generic stock object, do not alter product design, do not invent extra parts
```

## Prompt QA Before Generation

Before calling `image_gen.imagegen`, check:

- Is this a full-section design image or support visual?
- Does the prompt state one buyer judgment?
- Are product identity and preservation instructions explicit?
- Is the layout described as a mobile section, not a vague poster?
- Does the prompt separate scene, layout, style, text, and constraints?
- Is Korean text short enough to verify?
- If the item is mandatory `FULL_IMAGE`, does the prompt still request a complete designed section with exact image-rendered Korean text?
- If this is section 01 or 02, does the prompt preserve the opening story bridge with a shared scene/action/motif and a distinct buyer judgment?
- If the item is `SPARSE_SECTION_IMAGE_REQUIRED`, does the prompt create enough product/lifestyle/proof visual substance to lengthen the section without blank padding?
- Does the image queue include every approved visual asset, without dropping items for an assumed count limit or fixed split?
- Are mutable facts, direct numeric prices, channel names, and long instructions kept out?
- Does the prompt avoid fake reviews, fake proof, fake badges, and unsupported authority?
- Does the prompt explicitly avoid button UI and button-like CTA graphics?

## Manifest Notes

In `assets/generated/manifest.md`, record the production path and QA result:

```text
Codex built-in image_gen, GPT Image 2.0/gpt-image-2, source ig_*.png from %USERPROFILE%/.codex/generated_images/<session-id>/, prompt-guide structured section brief, Korean text checked/no-text checked, product consistency checked
```
