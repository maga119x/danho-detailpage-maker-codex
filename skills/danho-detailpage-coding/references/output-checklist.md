# Output Checklist

Run this before delivering a Danho detail page.

## Structure

- [ ] Page max width is 860px or less.
- [ ] Page is authored as an 860px source detail page, not a direct 393px/438px mini webpage or fixed phone wrapper.
- [ ] `box-sizing: border-box` applies globally.
- [ ] Main container has `overflow-x: hidden`.
- [ ] Every section has a unique id and an identifying HTML comment.
- [ ] Section ids/comments are sufficient for manual section splitting; `split_sections.py` is optional when Python is available.
- [ ] Phase A HTML looks like an ecommerce detail page before image generation.
- [ ] If `REFERENCE_DESIGN_ANALYSIS.md` exists, Phase A/Phase B visibly adapt its layout essence without copying the reference page.
- [ ] The HTML can be opened directly from the filesystem with relative asset paths; no Node/dev server, bundler, Playwright, Python runtime, or local HTTP server is required for ordinary viewing.

## Hybrid Image/HTML

- [ ] `image-plan.md` or user instruction defines which sections are full images and which remain HTML.
- [ ] Generated image assets were produced through the built-in Codex `image_gen.imagegen` native path, with provenance recorded in `assets/generated/manifest.md`.
- [ ] No generated image asset is a browser screenshot, exported HTML section, HTML/CSS/SVG/canvas drawing, CLI/API imagegen fallback, PIL/local composite, or placeholder bitmap.
- [ ] If Codex showed a generated preview, saved-path exposure, `%USERPROFILE%/.codex/generated_images/` recovery, and `%USERPROFILE%/.codex/sessions/**/*.jsonl` `image_generation_end` recovery were checked before using `generated_export_blocked` or `native_preview_path_unavailable`.
- [ ] `codex-clipboard-*.png` or other screenshots of the conversation UI are not used as final generated assets; they are diagnostic evidence only unless the user supplies the actual generated image file.
- [ ] `image-plan.md` includes at least two mandatory `FULL_IMAGE` rows: opening hero and final product/result closing.
- [ ] In the final hybrid HTML, the first section is a generated full-image hero.
- [ ] In the final hybrid HTML, the bottom/final selling section is a generated full-image product/result closing impression.
- [ ] No section uses `<button>`, `.cta-button`, link-button styling, purchase buttons, or button-like rounded CTA graphics.
- [ ] The final closing contains no CTA button, button-equivalent text, option/order prompt, benefit-check prompt, utility option/size guidance, or purchase-action wording such as `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `구성 확인`, `장바구니`, `주문`, `옵션은 구매 영역에서 확인`, or `사이즈와 구성은 주문 전 한 번 더 확인`.
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
- [ ] Direct numeric prices are not embedded in visible HTML or generated images; mutable benefits stay out of the final closing and are handled only in editable factual/options sections when needed.
- [ ] Visible HTML and generated images do not mention sales channel names such as `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, or `채널별 구성`.
- [ ] Review/testimonial section exists.
- [ ] The review/testimonial section looks like a shopping-mall review module: 3-5 cards or speech bubbles with nickname/handle, star rating, highlighted quote, and detailed review copy.
- [ ] If real reviews are unavailable, review cards are replacement-ready mockups using generic handles and benefit-based copy, with no `실제 구매자`, verified-buyer badge, dates, locations, review counts, purchase counts, or order numbers.
- [ ] If reviews are mockups, replacement markers stay in `PLANNING.md`/`COPY_REVIEW.md` internal logs only, not visible text or final HTML comments.

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
- [ ] The page reads as `friction -> answer -> use proof -> set/value -> fit/review/options -> final product/result closing`, not as independent slides.
- [ ] Reused generated images are cropped or placed differently when they represent different buyer actions.
- [ ] No card grid contains three or more independent buying ideas that should be separate screens.
- [ ] Key benefits, mechanisms, proof blocks, option systems, and FAQ/policy are split when needed instead of crammed into one viewport.
- [ ] Sparse screens with only a headline and short sentence, one note box, or 1-2 small cards are converted to image-dominant/image-supported sections or merged.
- [ ] No section gains vertical length only from blank padding, oversized empty bands, or decorative background space.
- [ ] Normal products are not artificially short; technical, high-consideration, reward-heavy, or option-heavy pages have enough screen depth.
- [ ] Strong claims have proof in the same screen or the next screen.
- [ ] HTML sections use vertical mobile rhythm: copy, large image, evidence/control.
- [ ] The page is not a generic landing page or simple centered web page.
- [ ] Reference design files are not cloned: no copied brand/logo/text/price/product image/exact layout/proprietary composition appears in final HTML or generated images.
- [ ] No section looks like empty height was added just to meet a ratio.
- [ ] Repeated sections do not all use the same layout.
- [ ] Cards are not nested inside cards.
- [ ] Text and image are visually connected.

## Typography

- [ ] Body copy is 32-36px at the 860px source and reads as about 16-18px in the 438px scaled preview.
- [ ] Lead/body-lg copy is 32-38px at source and reads as about 16-19px in the scaled preview.
- [ ] Section headlines are strong but controlled, normally 46-68px at source and about 23-35px in the scaled preview.
- [ ] Hero headlines are controlled, normally 56-84px at source; only the shortest opening display headline uses 64-96px.
- [ ] FAQ answers, card paragraphs, long leads, closing reassurance, and option guidance do not use display/h1/h2 sizing.
- [ ] Ordinary visible text scales to 16px or larger at 438px, including labels, badges, captions, reviews, comparison rows, closing text, and card copy.
- [ ] Micro text that scales to 13-15px is used only for exceptional legal/spec footnotes or non-persuasive metadata, never for selling-flow copy.
- [ ] Card body text is not oversized, normally 30-34px at source and about 15-17px in the scaled preview.
- [ ] Typography uses responsive min/max values such as `clamp()`.
- [ ] No heading wraps into awkward one-character or two-character lines.
- [ ] Head copy uses a mix of fragment, question, noun phrase, contrast, directive, and limited declarative forms.
- [ ] Head copy uses a mix of natural single-line wrapping, deliberate two-line heads, and occasional three-line tactile heads when appropriate.
- [ ] Section-level selling copy is centered by default.
- [ ] Structured components such as cards, comparison rows, option rows, FAQ, reviews, notices, and checklists are left-aligned for readability.

## Components

- [ ] Speech bubbles render with intentional tails or no tails.
- [ ] Stacked review cards use quote-card style, not broken bubble tails.
- [ ] Review cards show star visuals and reviewer handles at readable size, and the detailed copy remains editable HTML.
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

## Scaled Mobile Preview

Open or render the final HTML at 860px source width, then inspect that same source scaled to a 438px-wide phone preview. Do not use direct 393px/438px viewport reflow as the primary QA result. Playwright, Python, and a local HTTP server are optional helpers only; if unavailable, open the local file directly and run the visual checks manually.

- [ ] no horizontal overflow
- [ ] no broken images
- [ ] text does not overlap media
- [ ] text is readable without zooming
- [ ] pseudo-elements render correctly
- [ ] page rhythm alternates impact, information, proof, and action
- [ ] no visible `NEEDS_PROOF`, `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`
