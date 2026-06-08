# Codex Native Image Generation

Default to Codex native image generation for Danho detail pages.

## Do Not Use by Default

- `OPENAI_API_KEY`
- `.env`
- curl API calls
- `scripts/generate_banner.py`

Use API fallback only when the user explicitly requests it.

## Output Folders

- User-provided reference images: `assets/inbox/`
- Full-section designed images: `assets/generated/ai-section-designs/`
- Support photos/visuals: `assets/generated/`
- Manifest: `assets/generated/manifest.md`

## User-Provided Product Images

Treat images in `assets/inbox/` as product identity references unless `image-plan.md` explicitly marks them as `USER_IMAGE_DIRECT`.

When product references exist:

- attach the reference image(s) to native image generation for each product/lifestyle output
- include a product consistency instruction in every prompt
- generate new outputs into `assets/generated/`
- do not use the inbox image directly in final HTML unless the plan says `USER_IMAGE_DIRECT`

Read `references/product-reference-images.md` for classification and validation rules.

## Full-Section Design Images

Use for complete ecommerce section images.

Prompt must include:

- `complete Korean ecommerce product detail page section image`
- `include content and design`
- `not a plain photo`
- reference image instruction when `assets/inbox/` product images exist
- product/scene description
- exact short Korean text lines, if any
- restrained page color system
- vertical mobile ecommerce composition

Verify:

- Korean text is correct enough to use.
- Layout looks like a designed detail-page section, not a raw photo.
- Text is not cropped.
- It matches the section's persuasion role.

## Support Images

Use for images inside HTML sections.

Prompt must include:

`no text, no Korean caption, no overlay text, no signage with letters, pure visual`

If product references exist, also include:

`Use the attached product reference image as the source of truth. Preserve the same product shape, proportions, material, color, finish, and distinctive details. Generate a new image, do not copy the reference photo as-is.`

Verify:

- No visible text or labels.
- Product or scene directly supports the HTML copy.
- It does not duplicate nearby Korean copy.

## Korean Text Fallback

If the image model repeatedly produces wrong Korean:

1. Shorten the Korean line and retry.
2. Remove the text from the image and keep accurate HTML overlay/copy.
3. Reclassify the section from full image to HTML mixed.

Prices, compatibility limits, FAQ, and long instructions should normally stay HTML.

## Parallel Batch Workflow

Use parallel generation after the planning and prompt stages are complete.

Required preconditions:

- `image-plan.md` is approved.
- `prompts/banners.md` and `prompts/photos.md` are complete.
- every row has a final filename.
- the shared color system and product description are locked.
- product reference images are selected and locked when user images were provided.

Recommended batches:

| batch | image type | suggested size | reason |
|---|---:|---:|---|
| A | support images with no text | 4-8 at once | low typography risk |
| B | full-section images without Korean text | 3-5 at once | medium layout risk |
| C | full-section images with Korean typography | 2-3 at once | needs visual text QA |

Operational rules:

- Create all prompts first, then generate.
- Keep each image independent; do not make one section depend on the previous section's generated output unless the user explicitly wants a visual series.
- Do not modify the prompt template or color system while a batch is running.
- Do not swap product reference images mid-batch unless the section intentionally uses a different product variant.
- Record each item as `queued`, `generated`, `accepted`, `retry`, or `fallback_html` in the manifest.
- Retry only failed items. Do not regenerate accepted images just because another section failed.
- After every typography batch, verify Korean spelling, cropped text, and random extra letters before continuing to final HTML.

## Manifest

```markdown
# Generated Image Manifest

| file | type | source | prompt_file | references | status | batch | notes |
|---|---|---|---|---|---|---|---|
| ai-section-designs/01_hook.png | FULL_IMAGE | image-plan.md#hook | prompts/banners.md#hook | assets/inbox/product-front.png | accepted | C1 | Korean text checked, product consistent |
| magnetic-install.png | HTML_MIXED | image-plan.md#install-flow | prompts/photos.md#install-flow | assets/inbox/product-front.png | accepted | A1 | no text |
```

## Final Handoff

After generation, call `danho-detailpage-coding` to:

- insert full-section images
- insert support images in HTML sections
- validate image paths
- render mobile screenshots
