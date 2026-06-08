---
name: danho-detailpage-workflow
description: Orchestrate the Danho Korean ecommerce detail-page workflow in Codex. Use when the user asks to create, continue, revise, or diagnose a product 상세페이지 project across planning, HTML coding, image planning, native image generation, hybrid image/HTML layout, and final validation.
---

# Danho Detailpage Workflow

Run the workflow in order unless the user is explicitly revising an existing artifact.

## Sequence

1. Run `danho-detailpage-planning` when product facts, target, pain points, or page structure are missing.
2. Run `danho-detailpage-coding` Phase A when `PLANNING.md` and `DESIGN.md` exist. Phase A must create the HTML-based detail-page layout before final image generation.
3. Create or update `image-plan.md` after visually reviewing the HTML.
4. Run `danho-imageprompt-helper` when the user wants prompts or generated section images. After prompts and filenames are fixed, generate images in parallel batches when the environment supports it.
5. Run `danho-detailpage-coding` Phase B or revision mode when actual images exist and the page needs final HTML.

## Current Production Rules

- Prefer a hybrid final page: use designed full-section images for high-impact story moments, and HTML+image mixed sections for editable factual content.
- Always establish the HTML detail-page layout first. Do not jump from planning directly to image generation.
- Do not force every section to a fixed 9:16 or 3:4 ratio. Use vertical mobile rhythm with sufficient section height, large images, and natural content flow.
- Mobile-first means responsive readable typography for phone widths, not coding the page as a fixed 413px canvas.
- Treat HTML sections as designed sections, not text-only blocks. Add product photos, lifestyle images, badges, quote cards, speech bubbles, or comparison cards when they improve persuasion.
- Reject simple generic web pages. The result must read as an ecommerce product detail page with hero, problem, proof, comparison, price, FAQ, and CTA modules.
- Do not expose internal planning labels such as "설치 방식" or "모바일 구매 판단 요약" in the final page. Convert them into consumer-facing selling copy.
- Keep colors role-based and restrained: Key, Main, Sub, and Exception only.
- Prefer Codex native image generation. Use legacy API scripts only when the user explicitly asks for API fallback.
- Do not generate images one by one by default. Prepare the full image queue first, then batch independent image generations.

## Outputs

Create projects under `projects/MMDDHHmm_project-name/` with:

- `PLANNING.md`
- `DESIGN.md`
- `config.json`
- `image-plan.md`
- `prompts/`
- `assets/generated/`
- `build/project-name-vN.html`
- `build/sections/`

## Before Delivery

Always validate:

- Image paths exist.
- Section count and full-image/HTML section counts match the plan.
- No horizontal overflow on mobile.
- Font sizes and spacing are readable at phone widths.
- Phase A HTML has a finished detail-page layout before image replacement.
- No JavaScript, animation, transition, or hover-dependent design.
- Section splitting succeeds with `scripts/split_sections.py`.
