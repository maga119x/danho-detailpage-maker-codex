---
name: danho-detailpage-workflow
description: Orchestrate the full v3 text-first workflow for Korean e-commerce product detail pages in Codex. Use when the user asks to make a complete 상세페이지, convert product information into a detail-page project, continue an existing project through planning/coding/image steps, or decide which Danho skill should run next. Triggers include "상세페이지 만들어줘", "전체 워크플로우", "단호한 상세페이지", "제품 상세페이지 제작", and "Danho detail page".
---

# Danho Detailpage Workflow

## Overview

Run the Danho v3 workflow as a strict sequence: planning, text-only HTML, image plan, image prompts/native generation, then image replacement. Keep HTML as the single source of truth until `image-plan.md` explicitly decides whether each section is `REPLACE`, `SUPPORT`, or `NONE`.

## Decision Tree

1. If the user only provided rough product information, run `danho-detailpage-planning`.
2. If `PLANNING.md` and `DESIGN.md` exist and the user approved them, run `danho-detailpage-coding` Phase A.
3. If `build/*-v1-textonly.html` exists but `image-plan.md` does not, create `image-plan.md` and ask for user agreement before image generation.
4. If `image-plan.md` exists and the user wants prompts or generated banners, run `danho-imageprompt-helper`.
5. If generated or inbox images are available and the user approved the image plan, run `danho-detailpage-coding` Phase B.

## Required Order

Do not skip phases or run them in parallel.

1. `danho-detailpage-planning`
   - Input: user interview, product facts, target customer, selling points, brand tone.
   - Output: `projects/MMDDHHmm_project-name/PLANNING.md`, `DESIGN.md`, `config.json`.
2. `danho-detailpage-coding` Phase A
   - Input: approved `PLANNING.md` and `DESIGN.md`.
   - Output: `build/project-name-v1-textonly.html`.
3. `image-plan.md`
   - Input: visual review of `v1-textonly.html`.
   - Output: a section table choosing `REPLACE`, `SUPPORT`, or `NONE`.
   - Stop for user agreement before generating images.
4. `danho-imageprompt-helper`
   - Input: `v1-textonly.html`, `image-plan.md`, and `DESIGN.md`.
   - Output: `prompts/banners.md`, `prompts/photos.md`, and Codex-native generated images in `assets/generated/*.png`.
5. `danho-detailpage-coding` Phase B
   - Input: `v1-textonly.html`, `image-plan.md`, and actual image assets.
   - Output: `build/project-name-v2.html` with duplicate copy removed.

## Project Rules

- Create new projects under `projects/MMDDHHmm_project-name`.
- Keep `PLANNING.md` text-first. Do not create separate image sections during planning.
- Treat `DESIGN.md` as the design-token source. Do not revive legacy hardcoded theme keys.
- Use existing scripts from the relevant skill directory. Resolve script paths relative to the loaded `SKILL.md`, not from a hardcoded global path.
- For image generation, prefer Codex native image generation. Do not require `OPENAI_API_KEY` or run legacy API scripts unless the user explicitly requests fallback API generation.
- Before final delivery, run the validators/checks named by the phase skill.

## Copy Deduplication

Apply these rules throughout:

- `REPLACE`: remove HTML text section in Phase B; image may include the exact Korean copy.
- `SUPPORT`: keep HTML text; image must have no text or captions.
- `NONE`: keep HTML text; no image.

When a request conflicts with this order, explain that v3 prevents duplicated HTML/image copy by making `v1-textonly.html` the source of truth, then continue from the earliest missing phase.
