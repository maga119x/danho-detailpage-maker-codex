# Image Handling Reference

Use images according to their role, not a single rigid placement pattern.

Images come after HTML layout planning. Do not skip directly from `PLANNING.md` to generated images.

## Image Roles

| Role | Meaning | HTML treatment |
|---|---|---|
| `REPLACE` | designed image replaces the original HTML section | use one full-section `<img>` and remove duplicate HTML copy |
| `IMAGE_STORY` | low-copy section where the image carries the buying meaning | use a large image with minimal accurate HTML overlay or caption |
| `SUPPORT` | text remains, image supports comprehension | place image inside or near the HTML section |
| `NONE` | image adds little value | keep HTML only |
| `USER_IMAGE_DIRECT` | user-provided image is production-ready and explicitly approved for direct use | use `assets/inbox/` file directly |

User-provided product images are not automatically final page images. Treat `assets/inbox/` product photos as generation references unless `image-plan.md` marks `USER_IMAGE_DIRECT`.

User-provided reference 상세페이지 design files are different from product images. Store them under `assets/reference-designs/`, analyze them into `REFERENCE_DESIGN_ANALYSIS.md`, and use only their transferable layout/style essence. Do not use reference design files directly in final HTML or as product reference assets.

## Generation Provenance Gate

`FULL_IMAGE`, `REPLACE`, `IMAGE_STORY`, and generated `SUPPORT` assets must come from the built-in Codex `image_gen.imagegen` GPT Image 2.0 (`gpt-image-2`) native path through `danho-imageprompt-helper`.

Do not treat these as generated assets:

- HTML/CSS/SVG/canvas drawings
- browser-rendered screenshots or cropped page captures
- screenshots of the Codex conversation UI, including `codex-clipboard-*.png` captures that only show a generated preview thumbnail
- PIL, Photoshop, Figma, or local compositing outputs made to imitate generated images
- placeholder graphics derived from product photos
- API-script outputs
- CLI imagegen fallback outputs
- other image model outputs

If `image_gen.imagegen` is unavailable, prepare prompts and manifest rows, mark the image items as blocked or pending, and keep the affected section as HTML-first/HTML-mixed. Do not silently substitute a locally drawn bitmap, API output, CLI output, or older image-model output.

If a Codex generated preview is visible but the project has no copied file yet, pause Phase B insertion and run the image recovery procedure in `danho-imageprompt-helper`. The coding phase may accept only:

- a path exposed by Codex for the generated output,
- an `ig_*.png` recovered from `%USERPROFILE%/.codex/generated_images/`,
- a PNG decoded from `%USERPROFILE%/.codex/sessions/**/*.jsonl` `image_generation_end.result` and recorded as `SESSION_JSONL_NATIVE_OUTPUT`,
- or an actual generated image file explicitly supplied by the user and recorded as `USER_SUPPLIED_NATIVE_OUTPUT`.

A screenshot of the chat or a clipboard capture is diagnostic evidence only. It is not a valid `FULL_IMAGE` or generated `SUPPORT` asset by itself.

## Designed Full-Section Images

Use when the image model creates the complete section design: background, product, Korean typography, cards, icons, and layout.
The original section role must exist in the HTML-first layout before replacement.
If `image-plan.md` or the user marks the section as `FULL_IMAGE`, this replacement is mandatory. Do not downgrade it to `IMAGE_STORY`, `HTML_MIXED`, or textless HTML overlay just because Korean typography is difficult.

```html
<section id="answer" class="full-image-section">
  <img class="full-section-image" src="../assets/generated/ai-section-designs/04_answer.png" alt="...">
</section>
```

Good candidates:

- hook
- emotional scene/problem
- product answer
- lifestyle proof
- low-copy result, value, reassurance, or transition screen that needs a complete designed impression
- tactile use moment
- final CTA

The first section of a final hybrid detail page should be `REPLACE`/`FULL_IMAGE` when a designed hero exists. If the first section remains HTML, there must be an explicit reason in `image-plan.md` such as missing hero image or required mutable facts.

## Image-Story Sections

Use `IMAGE_STORY` when a section has too little editable information to justify a normal HTML card layout, but the moment is still important in the buying story.

Good candidates:

- one-action product demos
- tactile/result moments
- emotional transitions
- short set-value turns where a product or component image explains the point
- short care/storage/value/reassurance moments where a large visual can carry the section better than more copy

Do not stretch these into sparse card sections. Prefer:

```html
<section id="transfer" class="image-story-section">
  <img src="../assets/generated/transfer.png" alt="...">
  <div class="story-copy">
    <span class="story-kicker">consumer-facing label</span>
    <h2>short headline</h2>
    <p>one clear sentence</p>
  </div>
</section>
```

## Support Images Inside HTML Sections

HTML sections may include images. This is often better than a separate image slot when the section needs editable text and visual proof together.

```html
<section id="install-flow" class="detail-section">
  <div class="copy">...</div>
  <div class="visual">
    <img src="../assets/generated/magnetic-install.png" alt="...">
  </div>
  <ol class="step-list">...</ol>
</section>
```

Use for:

- installation
- compatibility checks
- material detail
- current-price guidance/options
- low-copy option, care/storage, value, reassurance, or fit sections that would otherwise look like centered text or 1-2 tiny cards
- comparison visuals
- FAQ support

If the support visual is generated from a user product photo, use the generated file from `assets/generated/`, not the original `assets/inbox/` reference.

## Sparse Section Image Gate

Mark `SPARSE_SECTION_IMAGE_REQUIRED` when an HTML section has only:

- kicker/headline/short lead
- one note box
- 1-2 small cards
- a short option, care, value, reassurance, result, or transition message with no visual proof

Resolve it before final HTML:

- `FULL_IMAGE`: use when the section should become a complete designed image section.
- `IMAGE_STORY`: use when one large product/result/lifestyle image can carry the point with minimal HTML copy.
- `HTML_MIXED`: use when editable text must remain but a large textless support image provides visual length and proof.
- `merge`: use when the section cannot justify its own screen.

Do not resolve sparse sections with empty padding, blank dark bands, decorative backgrounds, or small cards made larger without new buying information.

## Text Policy

- Full-section `REPLACE` images may contain short Korean typography.
- Mandatory `FULL_IMAGE`/`REPLACE` images must contain the planned short Korean typography when the plan requires it. If the generated text is wrong, regenerate or revise the native image; do not move the same copy to HTML as a silent fallback.
- Support images must contain no text, captions, signage, or labels.
- Long Korean sentences, compatibility, limitations, and FAQ should remain HTML. Direct numeric prices should not appear in generated images or visible HTML; direct users to the purchase channel for current sale price.
- If generated Korean text is wrong in a non-mandatory image-story/support visual, shorten/retry or move the copy back to HTML. If it is mandatory `FULL_IMAGE`, shorten/retry/regenerate and keep the role unchanged unless the user explicitly approves a role change.

## Paths

From `projects/<project>/build/page.html`, use:

```html
<img src="../assets/generated/file.png" alt="...">
```

Use `../assets/inbox/file.png` only for sections explicitly marked `USER_IMAGE_DIRECT`.

## Validation

- Check every `src` exists.
- Check every generated `src` has manifest provenance from built-in `image_gen.imagegen` GPT Image 2.0 (`gpt-image-2`), or is explicitly marked `USER_IMAGE_DIRECT`.
- If provenance is `SESSION_JSONL_NATIVE_OUTPUT`, check that the manifest records the session path or call id and that the copied file was decoded from `image_generation_end.result`.
- If provenance is `USER_SUPPLIED_NATIVE_OUTPUT`, check that it is the actual saved/generated image file, not a screenshot of the Codex conversation showing the thumbnail.
- Check no broken images in a real browser.
- Check the first final section is a full-image hero when a designed hero image exists.
- Check no mandatory `FULL_IMAGE` was accepted as `IMAGE_STORY`, `HTML_MIXED`, textless imagery, or HTML overlay because of Korean typography errors.
- Check the HTML-first layout existed before `FULL_IMAGE` replacement.
- Check low-copy screens are not left as empty-looking HTML cards; use `FULL_IMAGE`, `IMAGE_STORY`, `HTML_MIXED` support images, or merge.
- Check `SPARSE_SECTION_IMAGE_REQUIRED` screens contain meaningful image/proof/option/care/review content rather than blank vertical space.
- Check `assets/inbox/` images are not used directly unless marked `USER_IMAGE_DIRECT`.
- Check duplicate Korean copy near full-section images.
- Check mobile layout: image and related text must feel connected.
