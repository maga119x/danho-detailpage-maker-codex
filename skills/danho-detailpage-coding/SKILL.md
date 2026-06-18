---
name: danho-detailpage-coding
description: Build or revise static HTML/CSS for Korean ecommerce 상세페이지 projects from PLANNING.md, DESIGN.md, optional REFERENCE_DESIGN_ANALYSIS.md, image-plan.md, and generated assets. Use for HTML-first detail-page layout, adapting extracted reference-design layout essence without cloning, mobile-readable typography, final hybrid image/HTML pages, section splitting, color-system cleanup, image replacement, and visual validation.
---

# Danho Detailpage Coding

Create static, mobile-first ecommerce detail pages. Build the HTML layout first, then use image planning and generated images to replace or support selected sections.

## Inputs

- `PLANNING.md`
- `DESIGN.md`
- Optional `REFERENCE_DESIGN_ANALYSIS.md`
- `config.json`
- Optional `image-plan.md`
- Optional `assets/generated/` or `assets/inbox/`

## Build Modes

### Phase A: Text-First HTML

Use when image roles are not final.

- Include all copy in HTML.
- Build a finished ecommerce detail-page layout in HTML before any final image generation.
- Use placeholders, existing product images, or visual slots only after deciding their section role.
- Keep the page persuasive and visually structured without generated images.
- Do not output a generic landing page, simple centered web page, or desktop feature grid.
- For newly planned pages, do not start Phase A unless `PLANNING.md` records a PM planning review loop with final status `pass`.

### Phase B: Hybrid Final HTML

Use when image roles and assets exist.

- Require generated designed full-section images for the opening hero and final product/result closing impression.
- Use designed full-section images for high-impact visual/story sections.
- Use HTML+image mixed sections for editable factual sections.
- Avoid duplicated Korean copy between nearby HTML and full-section images.
- Preserve exact pricing, options, compatibility, and FAQ as HTML.
- Accept generated image assets only when they were produced through `danho-imageprompt-helper` using the built-in Codex `image_gen.imagegen` GPT Image 2.0 (`gpt-image-2`) native path, or when `image-plan.md` explicitly marks a user asset as `USER_IMAGE_DIRECT`.
- Do not create "generated" section images by rendering HTML, taking browser screenshots, drawing SVG/canvas, using CLI/API imagegen fallback, or locally compositing with PIL/other image libraries. If `image_gen.imagegen` is unavailable, stop after prompt/manifest preparation and report the block.

## Current Layout Rules

Read `references/html-first-detailpage-build.md` before starting a new page.
Read `references/mobile-screen-storyboarding.md` before translating `PLANNING.md` into HTML.
Read `references/proof-proximity-and-page-length.md` when deciding whether to split or merge sections.
Read `references/commercial-layout-components.md` when choosing the HTML pattern for each screen.
Read `../danho-detailpage-planning/references/reference-design-analysis.md` when `REFERENCE_DESIGN_ANALYSIS.md` or supplied reference design files exist.
Read `references/mobile-hybrid-layout.md` before major layout work.
Read `references/detailpage-typography.md` before writing CSS.
Use `../danho-detailpage-pm-reviewer/SKILL.md` before copywriter review for the PM planning loop, before Phase A when `PLANNING.md`/`COPY_REVIEW.md` section flow needs PM-level sequence review, and again after HTML exists when the rendered page feels fragmented, repetitive, AI-like, or when headline rhythm needs PM-level review.

Core rules:

- Do not force fixed 9:16 or 3:4 section ratios.
- Mobile detail-page QA means a canonical 860px-wide source page that remains readable when scaled down to a 438px phone preview. Do not validate by rendering the page at 393px/438px as the primary viewport and letting CSS reflow into a tiny webpage.
- Build screen-sized purchase judgments, not a short sequence of dense sections. One major content point may need several sections.
- In final hybrid pages, the first visible section must be a generated designed `FULL_IMAGE` hero. Do not start the final page with an HTML text hero.
- The bottom/final selling section must be a generated designed `FULL_IMAGE` product/result closing impression. Do not end a final hybrid detail page with a plain HTML action block. If legal, pricing, option, compatibility, or FAQ content must remain editable, split it into an adjacent HTML section and still keep the final full-image closing screen without purchase-action text.
- Detail pages are static image/HTML content. Do not add `<button>`, `.cta-button`, link buttons, purchase buttons, button-like rounded rectangles, or final-section button-equivalent text anywhere. Final closing sections should use product/result typography, use scene, brand tone, dividers, static labels, or quiet reassurance, not clickable-looking controls, purchase-action copy, or utility option/size guidance such as `옵션은 구매 영역에서 확인` and `사이즈와 구성은 주문 전 한 번 더 확인`.
- Each screen must have one dominant visual mass: image, type, proof, or cards. Do not give headline, paragraph, image, and cards equal weight in every section.
- If a section has three or more independent content points, split it before styling. If a section has only a headline and a short lead with no factual component, make it image-dominant (`FULL_IMAGE` or image-story HTML) rather than a sparse text/card screen.
- `SPARSE_SECTION_IMAGE_REQUIRED`: sections with a kicker/headline/short lead, one note box, or 1-2 small cards must not remain centered text-only or tiny card-only screens. Add a large product/lifestyle/proof/support image, convert to `FULL_IMAGE` or `IMAGE_STORY`, or merge with a neighboring proof/detail section.
- Apply the sparse-section rule to option, care/storage, value, reassurance, result, transition, and final decision sections. These often have little text but still need enough visual length in a detail page.
- Do not make a sparse section look longer by adding empty padding, oversized top/bottom gaps, or blank dark backgrounds. The vertical length must come from meaningful image, product, proof, review, comparison, option, or care content.
- Use tempo rhythm: low-density result/question screens, medium explanation/proof screens, and high-density info screens. Do not stack dense info screens before the buyer understands the main benefit.
- Keep strong claims near proof. If a claim and its proof are more than one mobile screen apart, split or reorder.
- If `REFERENCE_DESIGN_ANALYSIS.md` exists, adapt its transferable layout grammar: section rhythm, visual mass, spacing behavior, component style, typography contrast, image crop behavior, and transition patterns. Do not copy the reference page's brand, exact section order, exact pixel layout, product imagery, Korean copy, logos, badges, prices, or proprietary composition.
- Preserve the opening story bridge in HTML. Section 02 must look and read like the next beat after the hero: same buyer situation, object/action, emotional cue, or visual motif. Do not let the first two sections become two unrelated designed blocks.
- Keep a vertical mobile rhythm: top copy, large image/scene, then evidence card, quote card, speech bubble, checklist, or comparison.
- HTML sections may and often should contain images.
- Full-section images are valid when the image model designed the whole section with background, typography, cards, and icons.
- `image-plan.md` must contain at least two mandatory `FULL_IMAGE` rows: opening hero and final product/result closing. If they are missing, revise the image plan before Phase B instead of coding around the gap.
- If `image-plan.md` marks a section as `FULL_IMAGE`, final coding must preserve it as a full-section image. Do not downgrade it to `IMAGE_STORY`, `HTML_MIXED`, or textless image plus HTML overlay merely because Korean typography generation failed. Send it back for native regeneration/revision or mark the item blocked.
- Do not apply an image-count cap or fixed full-image/HTML ratio. Use as many `FULL_IMAGE` and `HTML_MIXED` support images as the story, proof, option, care, comparison, review, and sparse-section gates require. Image quantity is governed by the approved `image-plan.md` and visual QA, not by a maximum.
- Use consumer-facing labels only; internal planning labels must not appear.
- Badges/kickers must carry buying meaning, not section taxonomy. Do not use labels such as `문제 인식`, `전환점`, `사용 장면`, `구매 전 FAQ`, or `제품 디테일` unless the phrase itself helps the buyer decide. Rewrite as a micro-benefit, buyer situation, proof cue, or remove the badge.
- Head copy must vary by screen role. Mix fragments, questions, noun phrases, contrast, directives, and occasional declarative claims instead of ending every headline with the same `~합니다`, `~됩니다`, or `~좋습니다` pattern.
- Head copy must also vary visually. Do not manually split nearly every h1/h2 into the same `A<br>B` structure; use natural single-line wrapping, deliberate two-line heads, and occasional three-line tactile heads by screen role.
- Sections must connect as a persuasion journey. If adjacent sections could be swapped without changing the buyer's understanding, rewrite the heading/lead or reorder the sections.
- Do not expose sales channel names, channel-specific instructions, production warnings, proof markers, or review replacement markers in final HTML.
- Include a review/testimonial section in the HTML. If real reviews are missing, build replacement-ready mock review cards that still look like finished shopping-mall reviews: generic nickname/handle, star rating, highlighted quote, and detailed editable review copy. Replacement markers must stay in planning/review logs only, not visible text or final HTML comments.
- Use a restrained color system. Read `references/color-system.md`.

## Image Role Rules

Read `references/image-handling.md` and `references/text-image-deduplication.md`.

- `FULL_IMAGE`: full-section image replaces the original HTML layout.
- `IMAGE_STORY`: short low-copy moment expressed by a large image plus minimal accurate HTML overlay.
- `HTML_MIXED`: HTML section remains and uses a textless image inside or near the section.
- `HTML_ONLY`: no image needed.
- Legacy plans may call these `REPLACE`, `SUPPORT`, and `NONE`; map them before coding.
- `FULL_IMAGE` and generated `HTML_MIXED` support images must be real `image_gen.imagegen` native outputs, not HTML/CSS/SVG/canvas/PIL/browser-rendered substitutes.
- If generated Korean typography is wrong in a mandatory `FULL_IMAGE`, do not fall back to textless image + accurate HTML overlay. Return it to `danho-imageprompt-helper` for native regeneration/revision. Only the user can approve a role change away from `FULL_IMAGE`.

## CSS Rules

- Max page/source width: 860px. Treat this as the production canvas for typography and spacing.
- Set `box-sizing: border-box`.
- Set page `overflow-x: hidden`.
- Use detail-page typography at the 860px source size: body 32-36px, lead/body-lg 32-38px, h2 46-68px, h1/hero 56-84px, and largest display hero only 64-96px unless the brand requires otherwise. At the 438px scaled preview this reads as about body 16-18px, lead 16-19px, h2 23-35px, h1 29-43px, and display 33-49px.
- Treat oversized headline rhythm as a QA failure. Compared with the previous Danho scale, the largest hero/display headline is about 1.5 steps smaller and headline-adjacent type is one step smaller; do not use display/h1/h2 sizing for FAQ answers, card paragraphs, long leads, or closing reassurance copy.
- Keep ordinary readable text at a source size that scales to 16px or larger at 438px, including labels, badges, card copy, reviews, comparison rows, closing text, and captions inside the selling flow.
- Use micro text that scales to 13-15px only for exceptional secondary text such as legal notes, spec footnotes, or non-persuasive metadata; never use it for core selling copy or scannable section content.
- Use `clamp()` for source-size type and spacing, but do not use a fixed phone wrapper or direct 393px/438px viewport as the main QA canvas.
- Default section copy alignment should be centered for ecommerce detail-page flow. Use left alignment inside structured components such as cards, comparison rows, option rows, FAQ items, review cards, notices, and checklists.
- Avoid JavaScript, `:hover`, `transition`, `animation`, and `@keyframes`.
- Cards and quote blocks must look complete in default static state.
- Do not use card-in-card layouts.
- Use stable image dimensions or responsive constraints so text and media do not overlap.
- Static HTML must work when opened directly from the filesystem. Do not require a Node/dev server, bundler, local HTTP server, Playwright, or Python runtime for ordinary viewing and manual QA. Use relative asset paths and CSS that works under `file://`.

## Validation

Before final response:

1. Check image paths and section counts.
2. Confirm the final HTML contains a designed review/testimonial card or speech-bubble section with reviewer handle, stars, highlighted quote, and detailed copy, and no visible sales channel names, `NEEDS_PROOF`, `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
3. Check `assets/generated/manifest.md` or the project manifest records built-in `image_gen.imagegen` GPT Image 2.0 (`gpt-image-2`) provenance for generated assets; reject locally drawn, screenshot, SVG/canvas, PIL, CLI/API, other-model, or HTML-rendered substitutes.
4. Section files:
   ```bash
   python skills/danho-detailpage-coding/scripts/split_sections.py <html> <output-dir>
   ```
   This script is an optional helper, not a hard dependency. If Python is unavailable, manually confirm unique section ids/comments and keep `build/sections/` unchanged or update it by hand when needed; do not block final HTML solely because Python is missing.
5. Render/open the page without adding infrastructure:
   - Primary QA: open or render the final HTML at 860px source width.
   - Mobile readability QA: inspect the same 860px source scaled to a 438px-wide phone preview (scale factor about `0.509`). Do not use a direct 393px/438px viewport as the primary test, because that checks a reflowed mini webpage instead of the ecommerce detail-page source image.
   - If Playwright/browser automation exists, it may automate screenshots, but it must follow the 860px source plus 438px scaled-preview rule.
   - If Playwright is unavailable, open the local HTML file directly in a browser or the Codex in-app browser via `file://` and use browser zoom/device scaling/manual screenshots. Do not start a Node temporary server for static HTML unless the user explicitly requests it or a real browser security limitation blocks a local asset.
   - If no browser is available, run the static checks and report that visual render QA was not executed.
6. Verify:
   - no broken images
   - no horizontal overflow
   - typography is readable in the 438px scaled preview and not oversized at the 860px source
   - first 3 screens show product identity, core benefit/result, and difference or fit condition
   - first 2 screens form a story bridge: section 02 visually and verbally follows the hero instead of starting a generic new topic
   - no key benefit, mechanism, option system, or proof block is over-compressed into one dense section
   - every screen has one dominant visual mass and a clear screen role
   - page length matches product complexity; normal pages should not be artificially shortened
   - the page looks like a product detail page, not a simple web page
   - `image-plan.md` contains the mandatory opening hero and final product/result closing `FULL_IMAGE` rows
   - the first visible section is a generated full-image hero
   - full-image/HTML split matches `image-plan.md`
   - the bottom/final selling section is a generated full-image product/result closing impression, without buttons, button-like graphics, option/order prompts, benefit-check prompts, utility option/size guidance, or purchase-action text
   - no `<button>`, `.cta-button`, link-button, button-shaped CTA control, or final-section button-equivalent text appears in HTML or generated images
   - no `SPARSE_SECTION_IMAGE_REQUIRED` screen remains as centered text-only, note-only, or tiny card-only HTML
   - sparse option/care/value/result/transition screens use a large image, full-section image, image-story, or merge; blank padding alone is not accepted
   - quote/speech-bubble pseudo-elements render correctly
   - HTML colors follow the role-based palette
   - h1/h2 endings do not repeat the same formal sentence ending across the page
   - h1/h2 visual line breaks do not all use the same manual two-line structure
   - the rendered sequence reads as one connected purchase flow, not standalone slides
   - section kickers earn their space as buyer meaning, proof cue, micro-benefit, or next information check

## References

- `references/mobile-hybrid-layout.md` - current layout and hybrid rules
- `references/html-first-detailpage-build.md` - mandatory HTML-first production workflow
- `references/mobile-screen-storyboarding.md` - screen roles, visual mass, tempo, and viewport-level storyboarding
- `references/proof-proximity-and-page-length.md` - claim/proof distance, dense-section splitting, and minimum page-depth gates
- `references/commercial-layout-components.md` - commercial screen patterns for comparison, result, mechanism, proof, reviews, options, and FAQ
- `references/detailpage-typography.md` - mobile-readable type and spacing scale
- `references/color-system.md` - commercial color system rules
- `references/image-handling.md` - image role and placement rules
- `references/design-patterns.md` - text-to-design patterns
- `references/output-checklist.md` - final validation checklist
- `references/static-design.md` - static page constraints
