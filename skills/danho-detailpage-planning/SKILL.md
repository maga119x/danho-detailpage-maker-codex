---
name: danho-detailpage-planning
description: Plan Korean ecommerce product detail pages and write persuasive Korean 상세페이지 copy. Use when Codex needs to create or revise PLANNING.md, decide page flow, define section roles, write product copy, mark image conversion candidates, or prepare DESIGN.md for a Danho detail-page project.
---

# Danho Detailpage Planning

Create a text-first plan that can later become a hybrid HTML/image detail page.

## Required Inputs

Do not write the plan until these are clear enough:

- Product name, full product name, short product name, brand name
- Price, options, components, usage limits
- Target customer and main buying anxiety
- Pain points and selling points
- Brand tone and category
- Existing images or desired image direction, if any

Ask concise follow-up questions only when critical facts are missing.

## Workflow

1. Choose a design preset and create `DESIGN.md`.
2. Build a persuasion flow before writing sections.
3. Write `PLANNING.md` with all copy in text form.
4. Mark each section as `REPLACE_CANDIDATE`, `SUPPORT_CANDIDATE`, or `NONE`.
5. Create `config.json`.

## Persuasion Flow

Prefer a connected decision journey:

`hook → real-life moment → buying anxiety → product answer → fit check → install/use confidence → damage/removal confidence → daily use → compatibility/detail → comparison → proof/review → options → FAQ → final CTA`

Rules:

- Do not list features in parallel without transition.
- Put the strongest purchase condition early when it can block buying.
- Combine similar daily-use moments instead of scattering them.
- Include each section's persuasion role or connection reason in the section table.

See `references/persuasion-framework.md`, `references/genre-composition.md`, and `references/section-library.md`.
For the current Danho flow standard, read `references/detail-flow-rules.md`.

## Copy Rules

- Use the product naming 3-level rule. See `references/product-naming-consistency.md`.
- Follow Korean headline rules. See `references/korean-headline-rules.md`.
- Avoid internal labels in final-facing copy. Planning labels may exist in tables, but visible copy must sound like selling copy.
- Write section copy that can stand alone in HTML before image generation.
- Do not create separate image-only sections in `PLANNING.md`; only mark candidates.

## Image Candidate Rules

Use:

- `REPLACE_CANDIDATE` for short emotional hooks, scene-defining moments, strong typography, and final CTA.
- `SUPPORT_CANDIDATE` for factual sections that need a product photo or lifestyle visual while keeping HTML text.
- `NONE` for dense editable facts, prices, options, specs, and FAQ unless an image materially improves comprehension.

The final ratio may become hybrid, often around half designed full-image sections and half HTML+image mixed sections, but planning only marks candidates.

## References

- `references/output-format.md` for `PLANNING.md` structure
- `references/detail-flow-rules.md` for current section flow and internal-label rules
- `references/copy-templates.md` for phrasing patterns
- `references/image-guidelines.md` for candidate thinking
- `../danho-detailpage-coding/references/mobile-hybrid-layout.md` for current coding implications
