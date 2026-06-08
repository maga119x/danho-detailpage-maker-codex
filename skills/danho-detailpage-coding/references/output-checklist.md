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
- [ ] Designed full-section images use one `<section class="full-image-section"><img ...></section>`.
- [ ] HTML sections can contain support images when useful.
- [ ] Full-section image count and HTML section count match the requested split.
- [ ] Image paths are valid.
- [ ] User-provided product images in `assets/inbox/` are used as generation references unless marked `USER_IMAGE_DIRECT`.
- [ ] Final HTML does not use `assets/inbox/` directly unless the section is explicitly approved for direct use.
- [ ] Generated images preserve the product silhouette, color, material, and distinctive details from reference assets.
- [ ] Generated Korean typography is visually checked.
- [ ] Long facts, price, limitations, and FAQ remain editable HTML.

## Layout

- [ ] No forced global 9:16 or 3:4 section ratio.
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
- [ ] Card body text is not oversized, normally 15-17px.
- [ ] Typography uses responsive min/max values such as `clamp()`.
- [ ] No heading wraps into awkward one-character or two-character lines.

## Components

- [ ] Speech bubbles render with intentional tails or no tails.
- [ ] Stacked review cards use quote-card style, not broken bubble tails.
- [ ] Comparison is mobile-readable.
- [ ] Price uses a dedicated price component, not a narrow stat card.
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
