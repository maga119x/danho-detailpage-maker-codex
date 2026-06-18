# Codex Native Image Generation

Use Codex native image generation for Danho detail pages. This is the only supported generation path.

## Native Tool Definition

For this project, "Codex native image generation" means the built-in `image_gen.imagegen` tool. For Danho production, this is the required GPT Image 2.0 (`gpt-image-2`) native path. Do not look for direct API access, an `OPENAI_API_KEY`, a local generator script, a browser capture workflow, or a separate plugin before using it.

## Official OpenAI Notes To Preserve

- OpenAI Codex app and CLI documentation says built-in Codex image generation uses `gpt-image-2` and can be invoked naturally or with `$imagegen`.
- OpenAI API documentation shows GPT Image API outputs are returned as image data that must be explicitly saved to a file by the caller. A visible preview is therefore not the same operational event as a copied project asset.
- OpenAI Codex changelog notes that local image attachments and standalone image generations expose saved file paths to the model in supported Codex versions/surfaces. Treat path exposure as a runtime feature to verify, not as something guaranteed by the prompt alone.
- OpenAI docs also suggest using the API for larger batches so API pricing applies. Danho production intentionally does not use that route unless the user changes this plugin policy, because Danho provenance requires the built-in Codex native path.

Required model path:

- Use only built-in Codex `image_gen.imagegen` as GPT Image 2.0 (`gpt-image-2`).
- Do not use GPT Image 1, GPT Image 1.5, `gpt-image-1`, `gpt-image-1-mini`, legacy image models, or any other image generator.
- Do not switch to an API or CLI workflow to force a model name. The native Codex tool is the required model path.
- If the runtime explicitly says built-in `image_gen.imagegen` is not GPT Image 2.0 (`gpt-image-2`), stop and report `native_model_mismatch`.

Availability rule:

- If `image_gen.imagegen` appears in the active tool list, native image generation is available.
- Do not block just because the native tool schema does not expose `model`, `output_path`, `reference_images`, `quality`, `size`, or batch parameters.
- Do not pass a model argument. The native tool controls the model internally and is the GPT Image 2.0 (`gpt-image-2`) path for this workflow.
- Do not report a blocker because `model=gpt-image-2` cannot be set. That parameter is intentionally unavailable in the built-in path.
- Use one native call per final asset. Prepare a batch queue in prompts/manifest first, then call the native tool for each item.
- If the native tool returns a preview but no filesystem path is directly exposed, the problem is path exposure/export/recovery, not generation. Search `%USERPROFILE%/.codex/generated_images/` for the recent `ig_*.png` output first. If no file exists there, search `%USERPROFILE%/.codex/sessions/**/*.jsonl` for the matching `image_generation_end` result and decode it before considering `generated_export_blocked`.
- Only report image generation as blocked when `image_gen.imagegen` is absent, the native call itself fails, or an explicit `native_model_mismatch` is reported.

## Never Use For Generation

- `OPENAI_API_KEY`
- `.env`
- curl API calls
- local API generation scripts
- browser screenshots
- HTML/CSS/SVG/canvas drawings
- PIL drawings, local product-photo compositing, or local placeholder drawings
- stock image downloads

If `image_gen.imagegen` is absent or fails, do not switch to API or drawn substitutes. Prepare prompts and report the block. A product photo arranged with local typography, shapes, or effects is still a local composite and must not be recorded as a generated image.

## Output Folders

- User-provided reference images: `assets/inbox/`
- Full-section designed images: `assets/generated/ai-section-designs/`
- Support photos/visuals: `assets/generated/`
- Manifest: `assets/generated/manifest.md`

## Built-In Output Recovery

When `image_gen.imagegen` succeeds, Codex may show the image preview before the project file exists. That is not a generation failure.

The recovery order is:

1. Inspect the tool result and the immediate assistant context for any exposed saved file path. If a path is present, verify it exists and copy that file.
2. If no path is exposed, search Codex's generated-images root for recent `ig_*.png` files.
3. If no `ig_*.png` exists, search Codex session JSONL files for a recent `image_generation_end` event with a `result` field. Decode it and mark the source as `SESSION_JSONL_NATIVE_OUTPUT`.
4. If the user supplies or attaches the actual generated image file, copy that file and mark the source as `USER_SUPPLIED_NATIVE_OUTPUT` with a note that it was recovered from a Codex-generated preview.
5. If the user supplies only a screenshot of the conversation or a `codex-clipboard-*.png` capture, use it only as diagnostic evidence that a preview existed. Do not use that screenshot as the generated asset.
6. Only after these checks fail should the item be `generated_export_blocked` or `native_preview_path_unavailable`.

On Windows, successful Codex native outputs have been persisted here:

```text
C:/Users/<user>/.codex/generated_images/<session-id>/ig_*.png
```

Before marking any item `generated_export_blocked`, search this root first. The helper script is optional and requires Python:

```powershell
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --list --minutes 240 --limit 30
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --diagnose --minutes 240 --limit 30
```

If Python is unavailable, use file search or the OS file explorer to inspect `%USERPROFILE%/.codex/generated_images/` manually and copy the accepted `ig_*.png` into the project. Do not fail generation recovery just because the helper cannot run.

Then copy the selected accepted source to the planned project path. With Python:

```powershell
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --copy C:\Users\<user>\.codex\generated_images\<session-id>\ig_xxx.png --to projects\<project>\assets\generated\<file>.png
```

For the newest output immediately after a generation call:

```powershell
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --copy-latest --minutes 30 --to projects\<project>\assets\generated\<file>.png
```

For a native preview that is not materialized under `generated_images`, decode the newest matching session event:

```powershell
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --diagnose --minutes 30 --limit 10
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --copy-latest-session --minutes 30 --to projects\<project>\assets\generated\<file>.png
```

Without Python, inspect `%USERPROFILE%/.codex/sessions/**/*.jsonl` only if local tools can safely read it, or ask the user to attach the actual saved generated image file. A user-supplied actual generated output should be recorded as `USER_SUPPLIED_NATIVE_OUTPUT`; a screenshot of the conversation remains diagnostic only.

Recovery rules:

- Record the generation start time before each native call.
- First use any explicit saved path exposed to the model by Codex. Do not ignore a path returned in the tool result or message metadata.
- Search `%USERPROFILE%/.codex/generated_images/` recursively and sort by modification time.
- Prefer files modified after the generation start time.
- If `generated_images` has no matching file, search `%USERPROFILE%/.codex/sessions/**/*.jsonl` for `image_generation_end` with `result`; this is the native session result and can be decoded as the generated PNG.
- If multiple recent `ig_*.png` files exist, visually inspect candidates and choose the one matching the accepted preview.
- Copy, never move, the Codex original into the project.
- Record `generated_images_root` or `sessions_root`, source `ig_*.png` or session call id, destination file, prompt file, references, and QA status in `assets/generated/manifest.md`.
- `codex-clipboard-*.png` files are usually clipboard/UI captures. They can prove the preview was visible, but they are not enough for generated-asset provenance when they are screenshots of the conversation.
- Do not use `generated_export_blocked` until the exposed-path check, generated-images recovery, session JSONL recovery, and any user-supplied actual generated file check have been tried.

## User-Provided Product Images

Treat images in `assets/inbox/` as product identity references unless `image-plan.md` explicitly marks them as `USER_IMAGE_DIRECT`.

When product references exist:

- make the reference image(s) visible with `view_image` before generation
- attach the visible reference image(s) to native generation when the runtime supports it
- if explicit attachment is not exposed, include a strong product consistency lock in the prompt and still use `image_gen.imagegen`
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
- structured section brief: output purpose, buyer screen role, one purchase judgment, product/scene, layout, style, color, exact text contract, and constraints
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
- If the section is marked `FULL_IMAGE`, these checks are mandatory. A failed Korean text check requires native regeneration/revision, not a role downgrade.

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
2. Reduce to one headline fragment and retry.
3. Increase text size, simplify background, and retry.
4. If a mandatory `FULL_IMAGE` still fails, mark `FULL_IMAGE_TEXT_QA_BLOCKED` and do not ship that section as textless HTML overlay unless the user explicitly changes the role.

For non-mandatory image-story/support visuals, textless imagery plus HTML copy can be acceptable. For mandatory `FULL_IMAGE`, avoiding Korean typography by removing it from the image is a failure, not a fallback.

Direct prices must not be generated into section images. Promotions and channel discounts can change, so mutable price/promotion facts belong in editable factual/options sections, not fixed artwork or the final closing image. Compatibility limits, FAQ, and long instructions should normally stay HTML.

Do not solve failed Korean typography by rendering HTML as an image. Do not solve mandatory `FULL_IMAGE` typography failure by converting the section to HTML overlay. Use native image regeneration/revision for the designed full-section image.

## Parallel Batch Workflow

Use parallel generation after the planning and prompt stages are complete.

Required preconditions:

- `image-plan.md` is approved.
- `image-plan.md` includes mandatory `FULL_IMAGE` rows for opening hero and final product/result closing.
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
- For accepted native outputs, record the source `ig_*.png` from `%USERPROFILE%/.codex/generated_images/` or the `image_generation_end` call id from `%USERPROFILE%/.codex/sessions/**/*.jsonl`, plus the copied project destination.
- Mandatory `FULL_IMAGE` items must remain `FULL_IMAGE` in the manifest. If Korean text fails, record `retry` or `FULL_IMAGE_TEXT_QA_BLOCKED`; do not mark an unapproved downgraded textless/HTML-overlay version as accepted.
- Retry only failed items. Do not regenerate accepted images just because another section failed.
- After every typography batch, verify Korean spelling, cropped text, and random extra letters before continuing to final HTML.

## Manifest

```markdown
# Generated Image Manifest

## Status

- native_generation_status: completed
- generator: Codex built-in `image_gen` using gpt-image-2
- generated_images_root: `C:/Users/<user>/.codex/generated_images/<session-id>/`
- sessions_root: `C:/Users/<user>/.codex/sessions/` when source is `SESSION_JSONL_NATIVE_OUTPUT`

| file | type | source | prompt_file | references | status | batch | notes |
|---|---|---|---|---|---|---|---|
| ai-section-designs/01_hook.png | FULL_IMAGE | Codex built-in image_gen / gpt-image-2 | prompts/banners.md#hook | assets/inbox/product-front.png | accepted | C1 | source `ig_xxx.png` or session call id `ig_xxx`; Korean text checked; product consistent |
| ai-section-designs/99_final-closing.png | FULL_IMAGE | Codex built-in image_gen / gpt-image-2 | prompts/banners.md#final-closing | assets/inbox/product-front.png | accepted | C2 | mandatory final product/result closing; no button UI, option/order prompt, benefit-check prompt, or purchase-action text; Korean text checked |
| magnetic-install.png | HTML_MIXED | Codex built-in image_gen / gpt-image-2 | prompts/photos.md#install-flow | assets/inbox/product-front.png | accepted | A1 | source `ig_yyy.png`; no text |
```

## Final Handoff

After generation, call `danho-detailpage-coding` to:

- insert full-section images
- insert support images in HTML sections
- validate image paths
- visually validate the final HTML layout
