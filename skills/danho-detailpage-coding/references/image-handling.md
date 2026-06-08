# Image Handling Reference

Use images according to their role, not a single rigid placement pattern.

Images come after HTML layout planning. Do not skip directly from `PLANNING.md` to generated images.

## Image Roles

| Role | Meaning | HTML treatment |
|---|---|---|
| `REPLACE` | designed image replaces the original HTML section | use one full-section `<img>` and remove duplicate HTML copy |
| `SUPPORT` | text remains, image supports comprehension | place image inside or near the HTML section |
| `NONE` | image adds little value | keep HTML only |
| `USER_IMAGE_DIRECT` | user-provided image is production-ready and explicitly approved for direct use | use `assets/inbox/` file directly |

User-provided product images are not automatically final page images. Treat `assets/inbox/` product photos as generation references unless `image-plan.md` marks `USER_IMAGE_DIRECT`.

## Designed Full-Section Images

Use when the image model creates the complete section design: background, product, Korean typography, cards, icons, and layout.
The original section role must exist in the HTML-first layout before replacement.

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
- tactile use moment
- final CTA

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
- price/options
- comparison visuals
- FAQ support

If the support visual is generated from a user product photo, use the generated file from `assets/generated/`, not the original `assets/inbox/` reference.

## Text Policy

- Full-section `REPLACE` images may contain short Korean typography.
- Support images must contain no text, captions, signage, or labels.
- Long Korean sentences, prices, compatibility, limitations, and FAQ should remain HTML.
- If generated Korean text is wrong, shorten/retry or move the copy back to HTML.

## Paths

From `projects/<project>/build/page.html`, use:

```html
<img src="../assets/generated/file.png" alt="...">
```

Use `../assets/inbox/file.png` only for sections explicitly marked `USER_IMAGE_DIRECT`.

## Validation

- Check every `src` exists.
- Check no broken images in a real browser.
- Check the HTML-first layout existed before `FULL_IMAGE` replacement.
- Check `assets/inbox/` images are not used directly unless marked `USER_IMAGE_DIRECT`.
- Check duplicate Korean copy near full-section images.
- Check mobile layout: image and related text must feel connected.
