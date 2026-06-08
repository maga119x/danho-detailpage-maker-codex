# image-plan.md Template

Create this after the first HTML pass or when revising a visual direction.

## Template

```markdown
# Image Plan — [project]

## Decision Summary

| Type | Count | Meaning |
|---|---:|---|
| FULL_IMAGE | 8 | Complete generated section image replaces HTML layout |
| HTML_MIXED | 8 | Editable HTML section with support image/components |
| HTML_ONLY | 0 | Editable HTML with no image |
| Total | 16 | Must match section count |

## Section Decisions

| # | section id | type | output image | reference assets | source mode | HTML handling | reason |
|---:|---|---|---|---|---|---|---|
| 01 | hook | FULL_IMAGE | ai-section-designs/01_hook.png | assets/inbox/product-front.png | GENERATE_WITH_REFERENCE | one image section | first impression |
| 02 | fit-check | HTML_MIXED | fit-check-magnet-test.png | assets/inbox/product-front.png | GENERATE_WITH_REFERENCE | keep HTML + image | exact conditions |
| 03 | package | HTML_MIXED | assets/inbox/package.jpg | assets/inbox/package.jpg | USER_IMAGE_DIRECT | keep HTML + original image | original package photo is production-ready |

## Full-Image Sections

Use generated complete ecommerce section images. Image may contain short Korean typography.

## HTML-Mixed Sections

Keep editable HTML. Add support image, checklist, quote card, comparison rows, price panel, or FAQ bubbles.

## Validation

- [ ] Section ids match HTML.
- [ ] Full-image count matches user request.
- [ ] HTML-mixed sections retain exact factual copy.
- [ ] Support images contain no text.
- [ ] Prices, options, compatibility, and FAQ remain HTML.
- [ ] Generated Korean typography is visually checked.
- [ ] User-provided product images are used as references unless explicitly marked `USER_IMAGE_DIRECT`.
- [ ] Generated product images preserve the product identity from reference assets.
```

## Decision Rules

Use `FULL_IMAGE` for emotional or visual-impact sections:

- hook
- scene problem
- blocker
- answer
- no-damage proof
- daily use
- control moment
- final CTA

Use `HTML_MIXED` for editable and precise sections:

- fit check
- install flow
- height/compatibility adjustment
- material detail
- comparison
- review proof
- options/price
- FAQ

Use `HTML_ONLY` only when an image adds no persuasive value.

## Source Modes

- `GENERATE_WITH_REFERENCE`: use `assets/inbox/` product images as reference inputs and save new outputs to `assets/generated/`.
- `GENERATE_NO_REFERENCE`: generate from prompt only.
- `USER_IMAGE_DIRECT`: use the user-provided image directly because it is production-ready and intentionally approved.
- `HTML_ONLY`: no image.

## Mapping to Legacy Terms

- `FULL_IMAGE` corresponds to legacy `REPLACE`.
- `HTML_MIXED` often corresponds to legacy `SUPPORT`, but the support image can be inside the section.
- `HTML_ONLY` corresponds to legacy `NONE`.
