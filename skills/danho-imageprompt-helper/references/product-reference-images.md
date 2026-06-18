# Product Reference Images

Use this whenever the user provides product photos, package shots, sketches, mockups, or brand assets.

## Core Rule

User-provided product images are product identity references by default.

Do not simply insert the provided image into the detail page unless `image-plan.md` explicitly marks the section as `USER_IMAGE_DIRECT`.

Default behavior:

1. Store user images under `assets/inbox/`.
2. Select one or more canonical product references.
3. Make those references visible with `view_image`, then use them through the built-in `image_gen.imagegen` GPT Image 2.0 (`gpt-image-2`) context for every generated product or lifestyle image.
4. Save the newly generated results under `assets/generated/`.
5. Use generated files in final HTML unless the plan explicitly says to use the original image directly.

## Asset Types

| type | meaning | allowed final use |
|---|---|---|
| `PRODUCT_REFERENCE` | user image used to preserve product shape, color, material, logo, package | reference input only |
| `DIRECT_USE` | user image is already production-ready and should appear as-is | final HTML allowed |
| `STYLE_REFERENCE` | mood, background, or composition reference | reference input only |
| `GENERATED_OUTPUT` | image model result created from prompts/references | normal final HTML image |

If the user only says "I attached product images", classify them as `PRODUCT_REFERENCE`, not `DIRECT_USE`.

## Product Consistency Lock

Before generation, write a short lock block in `prompts/banners.md` or `prompts/photos.md`:

```markdown
## Product Reference Lock

- canonical references:
  - assets/inbox/product-front.png
  - assets/inbox/product-side.png
- preserve:
  - exact product silhouette and proportions
  - visible material/finish
  - main color and accent color
  - logo/package marks when visible
  - distinctive components and accessories
- do not:
  - invent a different product model
  - change the colorway
  - add buttons, holes, labels, or parts not present in the reference
  - replace the product with a generic stock object
```

## Prompt Pattern

For native image generation, inspect the product image with `view_image` first. If the built-in runtime supports explicit attachment, use the visible image as the reference input. If no explicit attachment parameter is exposed, still call `image_gen.imagegen` through the GPT Image 2.0 (`gpt-image-2`) native path with this product-lock language:

```text
Use the attached product reference image as the source of truth for the product. Preserve the same product shape, proportions, material, color, finish, and visible details. Create a new ecommerce detail-page image for [section purpose]. Do not copy the reference photo as-is; generate a new scene/design while keeping the product consistent.
```

For support images:

```text
Use the attached product reference image as the source of truth. Generate a new realistic product/lifestyle support image showing the same product in [use situation]. Preserve product identity. no text, no Korean caption, no overlay text, no signage with letters, pure visual.
```

For full-section images:

```text
Create a complete Korean ecommerce product detail page section image, include content and design, not a plain photo. Use the attached product reference image as the source of truth for the product and preserve product identity. [layout and copy].
```

## image-plan.md Columns

When references exist, add columns:

```markdown
| section id | type | output file | reference assets | source mode | notes |
|---|---|---|---|---|---|
| hook | FULL_IMAGE | ai-section-designs/01_hook.png | assets/inbox/product-front.png | GENERATE_WITH_REFERENCE | preserve product silhouette |
| options | HTML_MIXED | assets/inbox/package.jpg | assets/inbox/package.jpg | USER_IMAGE_DIRECT | original package photo is production-ready |
```

Allowed `source mode`:

- `GENERATE_WITH_REFERENCE`
- `GENERATE_NO_REFERENCE`
- `USER_IMAGE_DIRECT`
- `HTML_ONLY`

## Validation

Before final HTML:

- No `PRODUCT_REFERENCE` file from `assets/inbox/` is used directly unless marked `USER_IMAGE_DIRECT`.
- Every generated product/lifestyle image lists reference assets in the manifest.
- Generated product still matches the reference silhouette, color, material, and key parts.
- If consistency is poor, regenerate with stronger reference language or use an HTML section with the original product image explicitly marked as `USER_IMAGE_DIRECT`.
