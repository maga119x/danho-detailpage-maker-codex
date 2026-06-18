# Danho Detailpage Workspace

This workspace is initialized for the Danho Korean ecommerce 상세페이지 workflow.

## Source Of Truth

- Use the installed `danho-detailpage-workflow` skill as the current source of truth.
- Use this `AGENT.MD` as the local bootstrap checklist for this working directory.
- If this file and the installed skill conflict, follow the installed skill unless the user explicitly overrides it.

## Local Directory Contract

- Keep all generated product projects under `projects/MMDDHHmm_product-name/`.
- Keep project artifacts inside each project folder:
  - `PLANNING.md`
  - `DESIGN.md`
  - `COPY_REVIEW.md`
  - `REFERENCE_DESIGN_ANALYSIS.md` when reference design files are supplied
  - `config.json`
  - `image-plan.md`
  - `prompts/`
  - `assets/reference-designs/`
  - `assets/inbox/`
  - `assets/generated/`
  - `build/`
  - `build/sections/`
- Do not create final assets directly in the workspace root except shared notes, diagnostics, or user-requested exports.

## Required Workflow

1. Normalize the product brief before planning. Separate facts, assumptions, proof gaps, source wording, visual needs, and risks.
2. If reference 상세페이지 design files are supplied, store them under `assets/reference-designs/`, create `REFERENCE_DESIGN_ANALYSIS.md`, and extract transferable design/layout essence before finalizing `DESIGN.md`.
3. Create `PLANNING.md`, `DESIGN.md`, and `config.json` with `danho-detailpage-planning`.
4. Run PM planning review before copywriter review. Repeat `planning -> PM review -> planning revision` until the PM planning loop records `pass`.
5. Run `danho-detailpage-copywriter` only after PM planning pass. Create `COPY_REVIEW.md`, revise visible copy, and pass Korean naturalness, spoken Korean, grammar/style, source independence, and conversion-force gates.
6. Run PM pre-coding review after copywriter changes and before HTML. Fix broken sequence, abrupt transitions, weak visual mass, repeated headline rhythm, or conversion-flow issues.
7. Build Phase A HTML first. The HTML must be a complete ecommerce detail-page layout before final image generation.
8. Create `image-plan.md` from the rendered Phase A HTML. Decide `FULL_IMAGE`, `HTML_MIXED`, and `HTML_ONLY` per section after reviewing actual layout. The plan must include mandatory generated `FULL_IMAGE` rows for the opening hero and final static CTA/closing section.
9. Generate approved images with the built-in Codex `image_gen.imagegen` native path only. Prepare the full queue first, then generate one independent native image per approved asset.
10. Build Phase B final HTML with generated or approved images, split section files, and validate mobile rendering.
11. Run a final PM-level flow and visual QA pass before delivery.

## Hard Rules

- Do not skip PM review, copywriter review, or Phase A HTML.
- Do not jump from planning directly to image generation.
- Do not copy a supplied reference design page. Extract section rhythm, visual mass, spacing, typography contrast, component behavior, and crop style only; never reuse its brand, logo, copy, product image, price, exact layout, or proprietary composition.
- Do not expose direct numeric prices, sales channel names, internal labels, source filenames, placeholder warnings, `NEEDS_PROOF`, or review replacement markers in visible copy or images.
- Every newly planned page needs a review/testimonial section. If real reviews are missing, use replacement-ready neutral review cards and keep replacement notes internal.
- Detail pages are static ecommerce content. Do not create HTML buttons, link buttons, `.cta-button`, rounded CTA controls, or button-like generated graphics.
- Every newly produced detail page must include generated designed `FULL_IMAGE` sections for the opening hero and final static CTA/closing impression.
- Mandatory `FULL_IMAGE` sections must remain designed full-section images. If Korean typography fails, regenerate or mark the item blocked; do not silently downgrade to textless image plus HTML overlay.
- Image count has no cap. Do not force a fixed full-image/HTML split. Use as many `FULL_IMAGE` and `HTML_MIXED` support images as story, proof, option, care, comparison, review, sparse-section length, and final decision support require.
- Low-copy option, care/storage, value, reassurance, transition, result, and final decision sections must not remain sparse centered text-only blocks. Add meaningful product/lifestyle/proof imagery or merge with adjacent detail/proof content.
- Generated support images must not contain text. Full-section images may contain only short, exact Korean lines that can be visually verified.
- Use only the built-in Codex `image_gen.imagegen` native generation path for generated images. Do not use API scripts, CLI imagegen fallback, browser screenshots, HTML/CSS/SVG/canvas drawings, PIL composites, or placeholder graphics as generated-image substitutes.

## Final Validation

- Image paths exist and are recorded in `assets/generated/manifest.md`.
- Section count and image roles/counts match `image-plan.md`, with no image-count cap or forced split.
- The first final section is a generated full-image hero and the final selling section is a generated full-image static CTA/closing impression.
- The first two mobile screens pass the opening story bridge: hero promise leads into the same buyer moment, repeated friction, or immediate question.
- Adjacent sections read as one purchase journey, not independent slides.
- If `REFERENCE_DESIGN_ANALYSIS.md` exists, the final page adapts its essence without cloning the reference.
- Headline endings and visual structures vary across the page.
- No horizontal overflow on mobile.
- Body copy remains readable at phone widths.
- Section splitting succeeds and `build/sections/` is updated.
- Final HTML has no JavaScript, animation, transition, or hover-dependent design.
