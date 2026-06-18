# Output Checklist

Run this before delivering a Danho detail page.

## Structure

- [ ] Page max width is 860px or less.
- [ ] Page does not use a fixed phone wrapper such as `width: 413px`.
- [ ] `box-sizing: border-box` applies globally.
- [ ] Main container has `overflow-x: hidden`.
- [ ] Every section has a unique id and an identifying HTML comment.
- [ ] Section split succeeds with `split_sections.py`.
- [ ] Phase A HTML looks like an ecommerce detail page before image generation.

## Hybrid Image/HTML

- [ ] `image-plan.md` or user instruction defines which sections are full images and which remain HTML.
- [ ] Generated image assets were produced through the built-in Codex `image_gen.imagegen` native path, with provenance recorded in `assets/generated/manifest.md`.
- [ ] No generated image asset is a browser screenshot, exported HTML section, HTML/CSS/SVG/canvas drawing, CLI/API imagegen fallback, PIL/local composite, or placeholder bitmap.
- [ ] If Codex showed a generated preview, saved-path exposure, `%USERPROFILE%/.codex/generated_images/` recovery, and `%USERPROFILE%/.codex/sessions/**/*.jsonl` `image_generation_end` recovery were checked before using `generated_export_blocked` or `native_preview_path_unavailable`.
- [ ] `codex-clipboard-*.png` or other screenshots of the conversation UI are not used as final generated assets; they are diagnostic evidence only unless the user supplies the actual generated image file.
- [ ] In the final hybrid HTML, the first section is a full-image hero when a designed hero image exists.
- [ ] In the final hybrid HTML, the bottom/final section is a full-image CTA when a designed final CTA image exists.
- [ ] No section uses `<button>`, `.cta-button`, link-button styling, purchase buttons, or button-like rounded CTA graphics; CTA is static copy/cue only.
- [ ] Designed full-section images use one `<section class="full-image-section"><img ...></section>`.
- [ ] Mandatory `FULL_IMAGE` sections were not downgraded to `IMAGE_STORY`, `HTML_MIXED`, textless imagery, or HTML overlay because Korean typography was difficult.
- [ ] If generated Korean typography failed in a mandatory `FULL_IMAGE`, the item was regenerated/revised through native `image_gen.imagegen` or marked `FULL_IMAGE_TEXT_QA_BLOCKED`; it was not silently shipped as a fallback.
- [ ] Low-copy result, action, transition, option, care/storage, value, reassurance, and final decision moments are handled as full-image, image-story, or image-supported sections, not sparse HTML card sections.
- [ ] Any `SPARSE_SECTION_IMAGE_REQUIRED` screen has a meaningful generated/user product, lifestyle, proof, option, care, or review visual, or was merged with adjacent detail/proof content.
- [ ] HTML sections can contain support images when useful.
- [ ] Image roles and counts match the approved `image-plan.md`; no arbitrary image-count cap, fixed percentage, or forced full-image/HTML split was applied.
- [ ] Image paths are valid.
- [ ] User-provided product images in `assets/inbox/` are used as generation references unless marked `USER_IMAGE_DIRECT`.
- [ ] Final HTML does not use `assets/inbox/` directly unless the section is explicitly approved for direct use.
- [ ] Generated images preserve the product silhouette, color, material, and distinctive details from reference assets.
- [ ] Generated Korean typography is visually checked.
- [ ] Long facts, limitations, and FAQ remain editable HTML.
- [ ] Direct numeric prices are not embedded in visible HTML or generated images; mutable benefits are handled through option/order-area cues only when needed.
- [ ] Visible HTML and generated images do not mention sales channel names such as `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, or `채널별 구성`.
- [ ] Review/testimonial section exists.
- [ ] If real reviews are unavailable, review-related HTML is framed as review-check criteria or neutral placeholder-safe cards, not fabricated testimonials.
- [ ] If reviews are placeholders, replacement markers stay in `PLANNING.md`/`COPY_REVIEW.md` internal logs only, not visible text or final HTML comments.

## Layout

- [ ] No forced global 9:16 or 3:4 section ratio.
- [ ] The page is planned as screen-sized purchase judgments, not one dense section per source bullet.
- [ ] First 3 mobile screens show product identity, core buyer result/benefit, and product difference or fit condition.
- [ ] First 2 mobile screens form a connected opening story: section 02 follows the hero promise with the same buyer moment, object/action, emotion, or visual motif.
- [ ] Every screen has a dominant visual mass: image, type, proof, or cards.
- [ ] Section badges/kickers add buyer meaning or are removed; they are not internal taxonomy labels.
- [ ] Headline endings vary across the page; most h1/h2 lines do not share the same `~합니다`, `~됩니다`, `~좋습니다`, or other repeated grammar.
- [ ] Headline visual shapes vary across the page; not every h1/h2 is manually split into the same `A<br>B` two-line rhythm.
- [ ] Adjacent sections connect as a purchase journey. If two neighboring sections can be swapped without changing meaning, revise the headline, lead, or order.
- [ ] Section 02 does not feel sudden after section 01. If it could sit under any other hero, revise it with more scene, bridge copy, or image continuity.
- [ ] The page reads as `friction -> answer -> use proof -> set/value -> fit/review/options -> final action`, not as independent slides.
- [ ] Reused generated images are cropped or placed differently when they represent different buyer actions.
- [ ] No card grid contains three or more independent buying ideas that should be separate screens.
- [ ] Key benefits, mechanisms, proof blocks, option systems, and FAQ/policy are split when needed instead of crammed into one viewport.
- [ ] Sparse screens with only a headline and short sentence, one note box, or 1-2 small cards are converted to image-dominant/image-supported sections or merged.
- [ ] No section gains vertical length only from blank padding, oversized empty bands, or decorative background space.
- [ ] Normal products are not artificially short; technical, high-consideration, reward-heavy, or option-heavy pages have enough screen depth.
- [ ] Strong claims have proof in the same screen or the next screen.
- [ ] HTML sections use vertical mobile rhythm: copy, large image, evidence/control.
- [ ] The page is not a generic landing page or simple centered web page.
- [ ] No section looks like empty height was added just to meet a ratio.
- [ ] Repeated sections do not all use the same layout.
- [ ] Cards are not nested inside cards.
- [ ] Text and image are visually connected.

## Typography

- [ ] Body copy is readable at phone widths, normally 16-18px.
- [ ] Lead copy is 17-22px and not oversized.
- [ ] Section headlines are strong but controlled, normally 28-44px.
- [ ] Ordinary visible text is 16px or larger, including labels, badges, captions, reviews, comparison rows, CTA text, and card copy.
- [ ] 14-15px is used only for exceptional legal/spec footnotes or non-persuasive metadata, never for selling-flow copy.
- [ ] Card body text is not oversized, normally 16-17px.
- [ ] Typography uses responsive min/max values such as `clamp()`.
- [ ] No heading wraps into awkward one-character or two-character lines.
- [ ] Head copy uses a mix of fragment, question, noun phrase, contrast, directive, and limited declarative forms.
- [ ] Head copy uses a mix of natural single-line wrapping, deliberate two-line heads, and occasional three-line tactile heads when appropriate.
- [ ] Section-level selling copy is centered by default.
- [ ] Structured components such as cards, comparison rows, option rows, FAQ, reviews, notices, and checklists are left-aligned for readability.

## Components

- [ ] Speech bubbles render with intentional tails or no tails.
- [ ] Stacked review cards use quote-card style, not broken bubble tails.
- [ ] Comparison is mobile-readable.
- [ ] Option/benefit guidance uses an editable component, not a fixed numeric price panel.
- [ ] Checklist icons are HTML/CSS/SVG elements, not raw `☐` or `□` characters.

## Color

- [ ] HTML elements follow Key/Main/Sub/Exception roles.
- [ ] General emphasis does not use many unrelated accent colors.
- [ ] Exception color appears only for warning, limitation, or unavailable-condition copy.
- [ ] Generated image palettes do not force adjacent HTML into noisy colors.

## Static Page

- [ ] No JavaScript.
- [ ] No `:hover` or `:focus` dependent styling.
- [ ] No `transition`, `animation`, or `@keyframes`.
- [ ] All design elements look complete in default static state.

## Mobile Render

Render at a mobile width such as 393px and verify:

- [ ] no horizontal overflow
- [ ] no broken images
- [ ] text does not overlap media
- [ ] text is readable without zooming
- [ ] pseudo-elements render correctly
- [ ] page rhythm alternates impact, information, proof, and action
- [ ] no visible `NEEDS_PROOF`, `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`
