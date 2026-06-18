---
name: danho-imageprompt-helper
description: Create image prompts and generate images for Danho Korean ecommerce 상세페이지 projects using only the built-in Codex `image_gen.imagegen` native image tool, which is the required GPT Image 2.0 (`gpt-image-2`) production path. Use when the user asks for section images, designed full-section images, product/lifestyle support images, prompt files, or native image generation from image-plan.md. Do not use API scripts, browser-rendered screenshots, HTML/CSS drawing, SVG/canvas substitutes, legacy generation fallbacks, other image models, or CLI/API imagegen workflows.
---

# Danho Image Prompt Helper

Generate image prompts and images for a hybrid detail page. The only image generation path is the built-in Codex `image_gen.imagegen` tool. For Danho production, that tool is the required GPT Image 2.0 (`gpt-image-2`) native path.

Do not use API scripts, `OPENAI_API_KEY`, curl, browser-rendered screenshots, HTML/CSS/SVG/canvas drawing, PIL/local image compositing, or placeholder graphics as substitutes for requested generated images.

## Native Tool Contract

- Use `image_gen.imagegen` directly for generation. Do not search for another plugin, connector, API, model runner, or local script first.
- If `image_gen.imagegen` is present in the active tools, native generation is available. Do not report image generation as blocked just because the tool schema does not expose `model`, `output_path`, `reference_images`, `quality`, or batch parameters.
- Do not pass a model parameter. The Danho production rule is "Codex built-in `image_gen.imagegen`, GPT Image 2.0 (`gpt-image-2`) native path"; the model choice is implicit in the built-in tool.
- Do not claim native generation is blocked because you cannot set `model=gpt-image-2`. The built-in tool is the gpt-image-2 path for this workflow.
- If the Codex runtime explicitly reports that built-in `image_gen.imagegen` is not GPT Image 2.0 (`gpt-image-2`), stop and report `native_model_mismatch`. Do not switch to API, CLI, another model, or a local workaround.
- For local product references, first make the image visible in the conversation context with `view_image`, then describe it in the prompt as the product reference. If the runtime supports attaching the visible image to the native call, use it. If it does not, still generate with a strong product-consistency prompt instead of switching to API/CLI.
- After generation, first check whether Codex exposed a saved file path in the tool result, message context, or attachment metadata. OpenAI Codex changelog notes that saved paths can be exposed for local image attachments and standalone image generations in supported surfaces, so use that path when present.
- If no saved path is exposed, recover the selected built-in output from Codex's generated-images location before declaring any block. Search `%USERPROFILE%/.codex/generated_images/` first, especially `generated_images/<session-id>/ig_*.png`, sorted by `LastWriteTime` after the generation call. Copy the accepted `ig_*.png` into the project path required by `image-plan.md`, then record the original `ig_*.png` source in `assets/generated/manifest.md`.
- If `%USERPROFILE%/.codex/generated_images/` has no matching file but the Codex UI preview appeared, scan `%USERPROFILE%/.codex/sessions/**/*.jsonl` for the matching `image_generation_end` event and decode its `result` field with `collect_codex_generated_images.py --copy-latest-session`. Record this as `SESSION_JSONL_NATIVE_OUTPUT` in the manifest. This is still native Codex output, not an API/CLI fallback.
- If the Codex UI shows a generated preview, treat generation as successful. A missing file path is a path exposure/export/recovery issue, not an image-generation failure. Only record `generated_export_blocked` or `native_preview_path_unavailable` after checking exposed paths, `%USERPROFILE%/.codex/generated_images/`, `%USERPROFILE%/.codex/sessions/**/*.jsonl`, likely recent session subfolders, and the planned project `assets/generated/` paths. Do not relabel it as image generation unavailable.
- If the user provides the actual saved generated image file after the preview appears, copy it into `assets/generated/` and mark the source as `USER_SUPPLIED_NATIVE_OUTPUT`. If the user provides only a screenshot of the conversation or a `codex-clipboard-*.png` capture, use it as diagnostic evidence only; do not treat a conversation screenshot as the generated asset.
- Use one native image call per final asset or variant. "Batch" means preparing the queue first and then issuing independent native calls, not using CLI batch scripts.
- Do not reduce the image queue because of an assumed maximum image count, generation-call limit, or fixed full-image/HTML ratio. Generate every approved `FULL_IMAGE` and `HTML_MIXED` asset needed for story continuity, sparse-section length, proof, options, care/storage, comparison, reviews, and final decision support.
- Every newly produced detail page must generate at least two designed `FULL_IMAGE` assets: opening hero and final product/result closing. If `image-plan.md` lacks these rows, stop prompt generation and send the plan back for revision.

## Recovering Generated Files

Codex native image previews are normally persisted outside the project before being copied into `assets/generated/`.

Expected source root on Windows:

```text
C:/Users/<user>/.codex/generated_images/<session-id>/ig_*.png
```

Recovery sequence after every `image_gen.imagegen` call:

1. Note the generation start time and planned destination filename from `image-plan.md`.
2. Check the native tool result and current message/attachment context for an exposed saved path. If present, verify it exists and copy it.
3. Search `%USERPROFILE%/.codex/generated_images/` recursively for recent `ig_*.png` files, newest first. Prefer files modified after the generation start time.
4. If no `generated_images` file exists, scan `%USERPROFILE%/.codex/sessions/**/*.jsonl` for a recent `image_generation_end` event and decode the newest matching native result.
5. If several candidates exist, inspect thumbnails or dimensions and choose the preview that matches the accepted Codex UI image.
6. Copy the chosen source file to the planned project destination, for example `assets/generated/ai-section-designs/01_hero.png`.
7. Update `assets/generated/manifest.md` with:
   - `generated_images_root`
   - `sessions_root` when recovered from session JSONL
   - planned destination path
   - source `ig_*.png` or session `image_generation_end` call id
   - status `accepted` or `retry`
   - visual QA note
8. Run `--diagnose` when the UI shows a preview but no file is found; it lists generated image files, session image events, and `codex-clipboard-*.png` captures so they are not confused with each other.
9. Only after this recovery search fails should the manifest use `generated_export_blocked` or `native_preview_path_unavailable`.

Use `scripts/collect_codex_generated_images.py` to avoid manual path mistakes when Python is available:

```powershell
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --list --minutes 240 --limit 30
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --diagnose --minutes 240 --limit 30
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --copy-latest --minutes 30 --to projects/<project>/assets/generated/<file>.png
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --copy-latest-session --minutes 30 --to projects/<project>/assets/generated/<file>.png
python skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --copy C:\Users\<user>\.codex\generated_images\<session-id>\ig_xxx.png --to projects/<project>/assets/generated/<file>.png
```

If Python is unavailable, perform the same recovery manually:

- Inspect or search `%USERPROFILE%/.codex/generated_images/` for recent `ig_*.png` files and copy the accepted file into the planned `assets/generated/` path.
- If no file is materialized but a Codex preview appeared, inspect `%USERPROFILE%/.codex/sessions/**/*.jsonl` for recent `image_generation_end` events when the local tools allow it, or ask the user to attach the actual generated file from the Codex UI.
- Do not mark generation as failed merely because the helper script cannot run.

## Inputs

- `DESIGN.md`
- Optional `REFERENCE_DESIGN_ANALYSIS.md`
- HTML source, usually `build/*-v1-textonly.html` or the current final HTML
- `image-plan.md` or a user-approved section list
- Existing assets in `assets/inbox/`, if any

## Image Types

### Designed Full-Section Image

Use for `FULL_IMAGE` or hybrid full-image sections.

- The image model creates the whole ecommerce section: background, product scene, Korean typography, cards, icons, and layout.
- Treat text as designed layout objects, not prose. Break text into locked assets such as kicker, headline, subhead, badge, feature label, stat card, callout label, comparison header, caption, proof label, or closing phrase.
- The mandatory minimum is opening hero plus final product/result closing. These are generated full-section images, not optional support photos.
- When `image-plan.md`, the user, or the workflow marks a section as `FULL_IMAGE`, the designed full-section image is mandatory. Do not downgrade it to `IMAGE_STORY`, textless support imagery, or HTML overlay merely to avoid Korean typography risk.
- Use for hook, emotional scene, problem, answer, no-damage proof, daily-use scene, control moment, and final product closing.
- Keep text short. Long Korean copy, direct prices, FAQ, and conditions should not be generated into images. Mutable price/promotion facts belong in editable factual/options sections, not fixed section artwork or the final closing image.
- Do not generate buttons, link-button shapes, purchase buttons, rounded CTA controls, button-like labels, or final-section purchase-action text in any 상세페이지 image. Final closing artwork should use product/result composition, use scene, brand tone, dividers, quiet reassurance, or simple non-clickable labels. Do not include `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `구성 확인`, `장바구니`, `주문`, `옵션은 구매 영역에서 확인`, or `사이즈와 구성은 주문 전 한 번 더 확인`.
- Save under `assets/generated/ai-section-designs/` when generating multiple section images.

### Support Image

Use when HTML text remains.

- No text, no Korean caption, no overlay text, no signage.
- Use for product detail, installation, compatibility, material, comparison visual, review/lifestyle proof, and FAQ support.
- For review sections, prefer textless product-in-use or review-mood support images while keeping nickname, stars, and detailed review cards editable in HTML. Do not generate verified-buyer badges, review counts, exact dates, or "real buyer" claims into images unless supplied.
- Use for `SPARSE_SECTION_IMAGE_REQUIRED` option, care/storage, value, reassurance, or fit sections when editable copy remains but the section needs real visual length.
- The support image must be large enough to carry the section visually; a tiny decorative thumbnail does not satisfy the sparse-section gate.

## Prompt Rules

Read `references/prompt-guide.md`, `references/native-image-generation.md`, and `references/product-reference-images.md`.

- If the user provides product images, treat them as product references by default. Generate new images from those references instead of simply inserting the original files.
- For full-section images, include: `complete Korean ecommerce product detail page section image`, `include content and design`, `not a plain photo`.
- For complex full-section images, use the structured section-brief order from `references/prompt-guide.md`: output purpose, screen role, buyer judgment, product/scene, layout, style, color, text contract, and constraints.
- For typography or infographic full-section images, use the five locked prompt slots from `references/prompt-guide.md`: `IMAGE JOB`, `EXACT TEXT ASSETS`, `LAYOUT GRAMMAR`, `TYPOGRAPHY SYSTEM`, and `CONSTRAINTS`.
- Do not ask the model to "add the following copy prettily" or "make an infographic." Decompose the design into exact text assets, title blocks, stat cards, icon rows, comparison strips, step flows, callout labels, leader lines, reading flow, and whitespace.
- For support images, end with: `no text, no Korean caption, no overlay text, no signage with letters, pure visual`.
- Match the screen role from `image-plan.md`. Full-section images should usually be image-dominant or type-dominant impact/result/closing screens; dense facts, prices, options, specs, compatibility, FAQ, and policy stay in HTML.
- Before writing prompts, confirm `image-plan.md` includes mandatory `FULL_IMAGE` rows for the opening hero and final product/result closing. If either is missing, do not compensate with support photos or HTML; revise `image-plan.md`.
- If `REFERENCE_DESIGN_ANALYSIS.md` exists, use its visual system and layout grammar as style anchors only. Do not ask the image model to copy the reference page, brand, exact section layout, logos, text, product image, badges, prices, models, or proprietary composition.
- For section 01 and section 02 assets, preserve opening story continuity. Section 01 may show the promise/result; section 02 should use the same product, setting, action, color motif, or buyer emotion to deepen the scene, not restart the page with an unrelated image.
- Cover every `SPARSE_SECTION_IMAGE_REQUIRED` row in `image-plan.md`. Generate either a complete full-section image or a large textless support image; do not leave the section as sparse HTML because the copy is short.
- If the page needs many images, keep them in the queue. Image count has no upper cap; only remove or merge an image when the section role is genuinely redundant or the approved plan changes.
- Do not use generated images to cram several purchase judgments into one artwork. If the prompt needs many claims, split the section before generation.
- Use the page color system: Key/Main/Sub/Exception. Do not request many unrelated accent colors.
- For Korean typography, specify exact short text assets, their typographic role, placement, visual weight, and safe margins, then verify the output visually.
- For Korean typography size, use controlled detail-page scale rather than poster scale: the largest opening/final headline should feel about 1.5 steps smaller than oversized hero type, and subheads, labels, proof cards, FAQ-like copy, or closing reassurance should be about one step smaller than headline-adjacent type. Avoid huge three-line headlines that dominate the section before the product/proof appears.
- For infographic-heavy images, specify the reading flow and at least one concrete primitive: title block, stat cards, comparison strip, step flow, icon row, radial callouts, ingredient cards, before/after split, or leader-line callouts.
- For typography-heavy images, ask for generous whitespace, usually around 40% negative space when possible, to prevent cramped or cropped text.
- For mandatory `FULL_IMAGE` sections, Korean typography QA is a generation/revision gate. If Korean text is wrong, cropped, random, or omitted, regenerate or revise through native `image_gen.imagegen` with shorter exact text. Do not solve it by removing the image text and moving the copy to HTML unless the user explicitly changes the section role.
- For product references, lock product silhouette, proportions, material, finish, color, and visible marks before describing the new scene.
- If text generation fails repeatedly on a mandatory `FULL_IMAGE`, mark the item `FULL_IMAGE_TEXT_QA_BLOCKED` or ask for role approval instead of silently shipping a downgraded section.

## Workflow

1. Read image roles, section ids, and any `SPARSE_SECTION_IMAGE_REQUIRED` gates.
2. Verify the mandatory full-image contract: opening hero `FULL_IMAGE` and final product/result closing `FULL_IMAGE` exist with stable output filenames. If missing, return to `danho-detailpage-coding` / `image-plan.md` revision before generating.
3. Check whether section 01 and section 02 need opening story continuity. If both are generated, write prompts as a pair with shared product/scene anchors and distinct buyer judgments.
4. Classify user-provided images as `PRODUCT_REFERENCE`, `DIRECT_USE`, or `STYLE_REFERENCE`. Reference 상세페이지 design files belong to `STYLE_REFERENCE` and should already have `REFERENCE_DESIGN_ANALYSIS.md`.
5. If `REFERENCE_DESIGN_ANALYSIS.md` exists, add a short `Reference Design Style Anchors` block to `prompts/banners.md` and `prompts/photos.md`.
6. Write `prompts/banners.md` for full-section or typography images, using locked text assets, layout grammar, infographic primitives, reading flow, typography system, whitespace, and constraints.
7. Write `prompts/photos.md` for textless support images.
8. Generate the approved image queue with `image_gen.imagegen`, using product references when available through the built-in context.
9. Recover the generated output from an exposed saved path, `%USERPROFILE%/.codex/generated_images/`, or `%USERPROFILE%/.codex/sessions/**/*.jsonl`; copy it to `assets/generated/`, and record `assets/generated/manifest.md`.
10. Hand off to `danho-detailpage-coding` for final HTML, noting which sparse sections were resolved by full-section image, support image, or merge.

## Parallel Generation

After `image-plan.md`, filenames, and prompts are fixed, image generation can run in parallel batches because section images are independent.

- Prepare every prompt before generating the first image.
- Use stable filenames before generation starts.
- Run textless support images in larger parallel batches.
- Run full-section images with Korean typography in smaller parallel batches, then visually verify Korean text before final handoff.
- Do not change shared style tokens mid-batch.
- Keep the same product reference set for all product/lifestyle images in the batch unless `image-plan.md` says otherwise.
- Retry only failed or unusable items and update `assets/generated/manifest.md`.
- Mandatory `FULL_IMAGE` retries stay `FULL_IMAGE`. Do not reclassify them as `IMAGE_STORY`, `HTML_MIXED`, or textless assets because the first typography attempt failed.

## Hard Prohibitions

- Do not call OpenAI image APIs directly.
- Do not use GPT Image 1, GPT Image 1.5, `gpt-image-1`, `gpt-image-1-mini`, or any image model other than the built-in GPT Image 2.0 (`gpt-image-2`) native path.
- Do not ask for or read `OPENAI_API_KEY`.
- Do not run local API generation scripts.
- Do not use fallback CLI imagegen workflows, even if another installed `imagegen` skill describes them.
- Do not mark native generation blocked before attempting `image_gen.imagegen` when that tool is present.
- Do not create generated-image substitutes by drawing with HTML, CSS, SVG, canvas, PIL, browser screenshots, or local product-photo compositing.
- Do not render the HTML page and crop it as a generated section image.
- Do not use stock/image search results as generated assets unless the user explicitly asks for external images.
- Do not mark a generated preview as unusable or export-blocked before searching Codex's generated-images root and attempting to copy the matching `ig_*.png`.
- Do not replace a mandatory `FULL_IMAGE` with textless imagery plus HTML copy just to avoid Korean typography errors. Regenerate/revise the native full-section image or report `FULL_IMAGE_TEXT_QA_BLOCKED`.
- If `image_gen.imagegen` itself is absent or fails, stop and report that native image generation is blocked. Continue only with prompt preparation or HTML placeholders.
