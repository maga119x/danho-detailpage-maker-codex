# image-plan.md Template

Create this after the first HTML pass or when revising a visual direction.

## Template

```markdown
# Image Plan — [project]

## Decision Summary

| Type | Count | Meaning |
|---|---:|---|
| FULL_IMAGE | at least 2 | Complete generated section image replaces HTML layout; mandatory hero + final closing |
| HTML_MIXED | [as needed] | Editable HTML section with support image/components |
| HTML_ONLY | [as needed] | Editable HTML with no image because imagery is not needed |
| Total | [section count] | Must match section count; image count has no upper cap |

## Section Decisions

| # | section id | screen_role | visual_mass | type | output image | reference assets | source mode | HTML handling | reason |
|---:|---|---|---|---|---|---|---|---|---|
| 01 | hook | impact | image-dominant | FULL_IMAGE | ai-section-designs/01_hook.png | assets/inbox/product-front.png | GENERATE_WITH_REFERENCE | one image section | mandatory hero full image |
| 02 | fit-check | info | card-dominant | HTML_MIXED | fit-check-magnet-test.png | assets/inbox/product-front.png | GENERATE_WITH_REFERENCE | keep HTML + image | exact conditions |
| 03 | package | info | card-dominant | HTML_MIXED | assets/inbox/package.jpg | assets/inbox/package.jpg | USER_IMAGE_DIRECT | keep HTML + original image | original package photo is production-ready |
| 99 | final-cta | final CTA | image-dominant | FULL_IMAGE | ai-section-designs/99_final-cta.png | assets/inbox/product-front.png | GENERATE_WITH_REFERENCE | one image section | mandatory static closing image, no button UI |

If `REFERENCE_DESIGN_ANALYSIS.md` exists, do not list reference design files as product `reference assets`. Add a separate note such as `style anchors from REFERENCE_DESIGN_ANALYSIS.md` in the reason or prompt notes.

## Full-Image Sections

Use generated complete ecommerce section images. Image may contain short Korean typography.

`FULL_IMAGE` means a built-in `image_gen.imagegen` native output, not an HTML section exported as a bitmap. Do not plan browser screenshots, HTML/CSS/SVG/canvas drawings, CLI/API imagegen fallback, PIL/local composites, or placeholder graphics as full-image assets.

Every new detail page must include mandatory generated full-image sections:

- `01` hero/hook full-image section
- final static CTA/closing full-image section

These rows must be present in `image-plan.md`. If mutable legal, price, option, compatibility, or FAQ copy must remain editable, keep that copy in a neighboring `HTML_MIXED`/`HTML_ONLY` section and still generate the separate final closing `FULL_IMAGE`.

## HTML-Mixed Sections

Keep editable HTML. Add support image, checklist, quote card, comparison rows, current-price guidance panel, or FAQ bubbles.

## Validation

- [ ] Section ids match HTML.
- [ ] Screen roles and visual mass match the HTML storyboard.
- [ ] `FULL_IMAGE` count is at least 2 and includes the opening hero plus final static CTA/closing section.
- [ ] The mandatory hero and final closing rows have stable output filenames under `assets/generated/ai-section-designs/`.
- [ ] Dense content was split before image planning; images are not used to hide over-compressed sections.
- [ ] Every `SPARSE_SECTION_IMAGE_REQUIRED` section is assigned `FULL_IMAGE`, `HTML_MIXED` with a large support image, or merge handling; none remain `HTML_ONLY` because the copy is short.
- [ ] `FULL_IMAGE` and `HTML_MIXED` counts cover every section that needs story, proof, option, care, comparison, review, sparse-section, or opening-continuity visual support.
- [ ] No arbitrary image-count cap, fixed percentage, or forced full-image/HTML split was applied.
- [ ] Every generated image row uses `GENERATE_WITH_REFERENCE` or `GENERATE_NO_REFERENCE` and will be produced through the built-in Codex `image_gen.imagegen` native path.
- [ ] No generated image row depends on HTML rendering, browser screenshots, SVG/canvas drawing, CLI/API imagegen fallback, PIL, or local compositing.
- [ ] HTML-mixed sections retain exact factual copy.
- [ ] Support images contain no text.
- [ ] Direct numeric prices do not appear in images or visible HTML; current sale price is directed to the purchase channel/option area.
- [ ] Options, compatibility, and FAQ remain HTML.
- [ ] Generated Korean typography is visually checked.
- [ ] User-provided product images are used as references unless explicitly marked `USER_IMAGE_DIRECT`.
- [ ] Generated product images preserve the product identity from reference assets.
- [ ] Reference design files are used only through `REFERENCE_DESIGN_ANALYSIS.md` style anchors, not as product references or direct final assets.
```

## Decision Rules

Use `FULL_IMAGE` for emotional or visual-impact sections:

- mandatory hook/opening hero
- scene problem
- blocker
- answer
- no-damage proof
- daily use
- control moment
- low-copy result/value/reassurance/transition section that needs a complete designed impression
- mandatory final static CTA/closing impression

Use `HTML_MIXED` for editable and precise sections:

- fit check
- install flow
- height/compatibility adjustment
- material detail
- comparison
- review proof
- options/current-price guidance
- low-copy option, care/storage, value, reassurance, or fit sections that need visual length while keeping facts editable
- FAQ

Use `HTML_ONLY` only when an image adds no persuasive value and the section is not sparse. Do not use `HTML_ONLY` for a short centered text block, note-only screen, or 1-2 card option/care/value section.

## Source Modes

- `GENERATE_WITH_REFERENCE`: inspect `assets/inbox/` product images with `view_image`, use them through the built-in `image_gen.imagegen` context, and save new outputs to `assets/generated/`.
- `GENERATE_NO_REFERENCE`: generate from prompt only through the built-in `image_gen.imagegen` native path.
- `USER_IMAGE_DIRECT`: use the user-provided image directly because it is production-ready and intentionally approved.
- `HTML_ONLY`: no image.

## Naming Rule

Use only `FULL_IMAGE`, `HTML_MIXED`, and `HTML_ONLY` in new plans.
Do not introduce older role names in new files.
