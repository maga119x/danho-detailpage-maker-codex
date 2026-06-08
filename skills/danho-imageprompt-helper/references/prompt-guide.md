# Image Prompt Guide

Use concise natural-language prompts.

## Full-Section Ecommerce Design

Use this for `FULL_IMAGE` / designed section images.

```text
Create a complete Korean ecommerce product detail page section image, include content and design, not a plain photo. [Product/scene]. [Layout]. Korean text line 1 exactly: "...". Korean text line 2 exactly: "...". Use restrained commercial color system: deep navy key color, blue main accent, cool gray sub surfaces, only muted amber for warning if needed. Vertical mobile ecommerce composition. Premium clean layout, product photography integrated with typography and small UI cards. No clutter, no extra random text, no misspelled Korean.
```

If product reference images exist, add:

```text
Use the attached product reference image as the source of truth for the product. Preserve the same product shape, proportions, material, color, finish, and visible details. Generate a new ecommerce section design; do not copy the reference photo as-is and do not replace it with a generic object.
```

Use for:

- hook
- problem scene
- blocker
- answer
- no-damage
- daily use
- control
- final CTA

## Support Photo / Visual

Use this when HTML keeps the copy.

```text
Create a realistic product/lifestyle support image for a Korean ecommerce detail page. [Subject]. [Action]. [Setting]. [Composition]. Soft natural or studio light. Clean commercial product photography. Vertical mobile-friendly crop. no text, no Korean caption, no overlay text, no signage with letters, pure visual.
```

If product reference images exist, add:

```text
Use the attached product reference image as the source of truth. Preserve product identity while generating a new scene. Do not use the original photo as the final output without transformation.
```

## Korean Typography

- Keep Korean text short.
- Specify exact lines.
- Avoid long paragraphs, price tables, FAQ, or compatibility warnings in images.
- Verify visually after generation.
- If incorrect, shorten or move copy to HTML.

## Product References

- Treat user-provided product images as references by default.
- Do not simply place `assets/inbox/*` in the final page unless `image-plan.md` marks `USER_IMAGE_DIRECT`.
- Use the same canonical reference set across generated product/lifestyle images.
- Mention silhouette, proportions, material, color, finish, and distinctive details in prompts.
- Add `no generic stock object, do not alter product design, do not invent extra parts` to negative phrases when product consistency matters.

## Color

Keep prompt color restrained:

- Key: deep navy / charcoal
- Main: restrained blue
- Sub: cool gray / blue tint
- Exception: muted amber only for warning

Avoid asking for many accent colors in one image.

## Negative Phrases

Use as needed:

```text
no cheap infographic style, no cluttered layout, no random letters, no extra Korean, no cropped typography, no distorted product, no excessive colors
```
