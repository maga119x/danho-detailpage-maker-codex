---
name: danho-imageprompt-helper
description: Create image prompts and generate images for Danho Korean ecommerce 상세페이지 projects using Codex native image generation. Use when the user asks for section images, designed full-section images, product/lifestyle support images, prompt files, or native image generation from image-plan.md.
---

# Danho Image Prompt Helper

Generate image prompts and images for a hybrid detail page. Default to Codex native image generation, not API scripts.

## Inputs

- `DESIGN.md`
- HTML source, usually `build/*-v1-textonly.html` or the current final HTML
- `image-plan.md` or a user-approved section list
- Existing assets in `assets/inbox/`, if any

## Image Types

### Designed Full-Section Image

Use for `FULL_IMAGE` or hybrid full-image sections.

- The image model creates the whole ecommerce section: background, product scene, Korean typography, cards, icons, and layout.
- Use for hook, emotional scene, problem, answer, no-damage proof, daily-use scene, control moment, and final CTA.
- Keep text short. Long Korean copy, price, FAQ, and conditions should stay in HTML.
- Save under `assets/generated/ai-section-designs/` when generating multiple section images.

### Support Image

Use when HTML text remains.

- No text, no Korean caption, no overlay text, no signage.
- Use for product detail, installation, compatibility, material, comparison visual, review/lifestyle proof, and FAQ support.

## Prompt Rules

Read `references/prompt-guide.md`, `references/native-image-generation.md`, and `references/product-reference-images.md`.

- If the user provides product images, treat them as product references by default. Generate new images from those references instead of simply inserting the original files.
- For full-section images, include: `complete Korean ecommerce product detail page section image`, `include content and design`, `not a plain photo`.
- For support images, end with: `no text, no Korean caption, no overlay text, no signage with letters, pure visual`.
- Use the page color system: Key/Main/Sub/Exception. Do not request many unrelated accent colors.
- For Korean typography, specify exact short lines and verify the output visually.
- If text generation fails repeatedly, shorten the line or move that copy back to HTML.

## Workflow

1. Read image roles and section ids.
2. Classify user-provided images as `PRODUCT_REFERENCE`, `DIRECT_USE`, or `STYLE_REFERENCE`.
3. Write `prompts/banners.md` for full-section or typography images.
4. Write `prompts/photos.md` for textless support images.
5. Generate the approved image queue with Codex native image generation, attaching product references when available.
6. Save files in `assets/generated/` and record `assets/generated/manifest.md`.
7. Hand off to `danho-detailpage-coding` for final HTML.

## Parallel Generation

After `image-plan.md`, filenames, and prompts are fixed, image generation can run in parallel batches because section images are independent.

- Prepare every prompt before generating the first image.
- Use stable filenames before generation starts.
- Run textless support images in larger parallel batches.
- Run full-section images with Korean typography in smaller parallel batches, then visually verify Korean text before final handoff.
- Do not change shared style tokens mid-batch.
- Keep the same product reference set for all product/lifestyle images in the batch unless `image-plan.md` says otherwise.
- Retry only failed or unusable items and update `assets/generated/manifest.md`.

## Legacy Fallback

Use `scripts/generate_banner.py` only when the user explicitly requests API-based generation and `OPENAI_API_KEY` is available. The normal path is native image generation.

The legacy script supports `--reference-image` and item-level `reference` metadata, but the native path should still follow the same product-reference rules.
