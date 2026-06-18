# Mobile Hybrid Layout Reference

Use this reference when building or revising the final ecommerce detail page.

## Current Direction

The final page should feel like a mobile-first vertical story, not a collection of fixed-ratio cards. It should also feel like a sequence of screen-sized purchase judgments, not a compressed brochure. Long pages are acceptable when each screen has one job.

Build the HTML detail-page layout before image generation. Generated section images should replace or support an already planned HTML section role. Generated section images must be native image-model outputs created through `danho-imageprompt-helper`; an HTML/CSS/SVG/canvas/PIL composition exported as a bitmap is still HTML/local drawing, not a generated image.

Do:

- In a final hybrid page, start with a full-image hero when a designed hero image exists. The first screen is the commercial first impression; do not make it a normal HTML text block when a full hero visual is available.
- End a final hybrid page with a full-image CTA when a designed final CTA image exists. The last screen is the closing purchase impression; do not make it a normal HTML CTA block unless mutable legal, pricing, or option content must remain editable.
- Use natural-height sections with enough top/bottom breathing room.
- Split one dense content point into multiple screens when needed: scene/result, question, mechanism/detail, proof, caveat/action.
- Keep sections vertically oriented: headline, large image, then proof or action element.
- Mix full-section generated images with HTML+image sections.
- Use images inside HTML sections when they help persuasion.
- Use speech bubbles, badges, checklists, quote cards, comparison rows, and product cards as designed HTML components.
- Use badges/kickers only when they add buying meaning. A badge should say what the buyer should notice, not the planner's category name.
- Use readable mobile typography. Mobile-first is not a fixed 413px canvas.

Do not:

- Force every section to 9:16 or 3:4.
- Set the page wrapper to a fixed phone width.
- Stretch a weak layout by only changing height.
- Shrink copy or cram more cards into one section to make the page shorter.
- Use the same section layout repeatedly.
- Separate text and image so far apart that the section feels unfinished.
- Show internal planning labels in the page.
- Waste badge space on taxonomy labels such as `문제 인식`, `자주 쓰는 재료`, `전환점`, `사용 장면`, `구매 전 FAQ`, or `추천 대상`. Rewrite the badge as a buyer situation, micro-claim, proof cue, or remove it.
- Generate final section images before the HTML structure and image-plan exist.
- Substitute final section images with browser screenshots, exported HTML, SVG/canvas drawings, PIL/local composites, or placeholder graphics when native image generation is unavailable.
- Leave a low-copy transition/result screen as sparse HTML. If the screen has only a headline and one short sentence, make it image-dominant or merge it with a nearby proof screen.
- Leave a low-copy option, care/storage, value, reassurance, or final decision screen as centered text-only or tiny 1-2 card HTML. Use `SPARSE_SECTION_IMAGE_REQUIRED`: add a large product/lifestyle/proof/option/care visual, convert to `FULL_IMAGE`/`IMAGE_STORY`, or merge it.
- Make sparse sections taller only with blank padding, empty dark bands, or decorative background space.

## Hybrid Image Quantity

When the user asks for hybrid, do not target a fixed split, fixed percentage, or maximum image count.

Use the number of images needed for the purchase journey:

- designed `FULL_IMAGE` sections for impact, story, proof, and final decision moments
- `HTML_MIXED` support images for editable factual sections that need visual proof or visual length
- `HTML_ONLY` only when text, cards, tables, or FAQ are genuinely enough

A page may be image-heavy when each image has a clear persuasive job and native generated-image provenance. Do not reduce image quantity to save generation calls or match a ratio. Keep mutable prices, options, specs, compatibility, FAQ, and policy as editable HTML when needed.

Use full-section images for:

- hook or opening hero
- lifestyle problem scene
- emotional blocker
- product answer or concept turn
- no-damage / rental reassurance
- daily-use lifestyle moment
- foot-control or tactile use moment
- final CTA

Use image-story sections for:

- low-copy tactile or result moments
- one-action demos such as crushing, transferring, folding, clipping, opening, pouring, or fitting
- emotional transition screens where a product/set image explains the point better than more text

Use HTML+image sections for:

- fit check and compatibility
- install steps
- height or size guidance
- material details
- comparison
- reviews that must stay editable
- current-price guidance and options
- FAQ

## Section Structure

Use this vertical sequence for HTML sections:

```html
<section id="fit-check" class="detail-section">
  <div class="copy">
    <span class="tag">consumer-facing label</span>
    <h2>headline</h2>
    <p class="lead">short setup</p>
  </div>
  <div class="visual">
    <img src="../assets/generated/fit-check.png" alt="...">
    <div class="image-note">short visual proof</div>
  </div>
  <div class="card">checklist / quote / comparison / current-price guidance</div>
</section>
```

For designed full-section images:

```html
<section id="hook" class="full-image-section">
  <img class="full-section-image" src="../assets/generated/ai-section-designs/01_hook.png" alt="...">
</section>
```

Do not use this editable-section structure for every screen. Some screens should be image-dominant, some type-dominant, some proof-dominant, and some card-dominant. See `mobile-screen-storyboarding.md`.

## Density And Sparseness Gate

Before finalizing each mobile screen, classify it:

| Screen state | Required action |
|---|---|
| More than 2 card paragraphs or 3 independent subtopics | Split into multiple sections |
| A label, headline, and one short sentence only | Convert to full image or image-story section |
| One note box or 1-2 small cards with lots of surrounding blank space | Add a large support image, convert to full/image-story, or merge |
| Low-copy option/care/value/reassurance section with no product or lifestyle visual | Mark `SPARSE_SECTION_IMAGE_REQUIRED` and create image support |
| Dense catalog/list plus no visual proof | Split catalog from proof image |
| Key transition but no image | Use type-dominant dark declaration only if the sentence is strong enough; otherwise use image-story |

Example: a `자주 쓰는 재료` section with 고기, 대파/양파, 마늘, 재료 이동 should not be one four-card screen. Split it into a broad friction screen, a 고기/채소 screen, and separate image-story screens for 마늘 and 재료 이동.

For sparse sections, the acceptable added length is meaningful content: generated product/lifestyle imagery, option/component visuals, care/storage scenes, comparison/proof images, review mood, or a merged proof/detail block. Empty padding is not content.

## Component Guidance

- Kicker/badge text should pass the "buyer meaning" test: if removed, would the buyer lose useful context? If not, remove it. If yes, write it as a short claim such as `칼 때문에 시작이 막힌다면`, `무뎌질 때 바로 관리합니다`, or `받는 구성을 먼저 봅니다`.
- Use speech bubbles for customer thoughts, short questions, or quick FAQ.
- Use quote cards for reviews. Do not put generic speech-bubble tails between stacked cards; they can render like broken diamonds.
- Use a left accent rule and a subtle quote watermark for dark review cards.
- Use comparison rows instead of dense tables on mobile.
- Use product images in current-price guidance/options sections when the buyer is close to purchase. Do not hard-code numeric prices.

## Text Alignment

Use centered text as the default for section-level selling copy: kicker, headline, lead, hero, image-story overlays, and CTA blocks.

Use left alignment inside structured information components:

- cards with paragraph copy
- comparison rows and option rows
- FAQ items
- review cards
- notices and safety/care notes
- checklists

Do not let the entire page default to left alignment unless the design is a dense admin/spec sheet. Most ecommerce 상세페이지 sections should feel editorial and centered, while detailed evidence stays left-aligned for readability.

## Visual Checks

Render at 393px and optionally 413px mobile width and verify:

- no horizontal overflow
- body copy is 16-18px or equivalent readable size
- headings are large enough to sell but not so large that they wrap awkwardly
- all images loaded
- generated images have native image-generation provenance in the manifest
- first and final sections are full-image sections when their designed images exist
- image roles and counts match the approved plan
- no arbitrary image-count cap, fixed percentage, or forced full-image/HTML split was applied
- pseudo-elements such as speech-bubble tails and quote marks render intentionally
- section rhythm alternates between image impact and editable information
- no key claim, mechanism, option set, review proof, or FAQ/policy block is over-compressed into one viewport
