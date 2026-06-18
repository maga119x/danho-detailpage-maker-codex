# Reference Design Analysis

Use this when the user attaches a reference 상세페이지 design file, long screenshot, image, PDF render, or HTML capture and asks Danho to use it as design inspiration.

The goal is to extract design and layout essence, not to copy the reference page.

## Artifact Contract

Create this project artifact before finalizing `DESIGN.md`:

```text
REFERENCE_DESIGN_ANALYSIS.md
```

Store reference files under:

```text
assets/reference-designs/
```

If a long image needs slicing for review, store slices under:

```text
assets/reference-designs/slices/<reference-name>/
```

Do not place reference design files in `assets/inbox/` unless they are also product images. `assets/inbox/` is for product or brand assets; `assets/reference-designs/` is for style/layout references.

## Extraction Workflow

1. Identify every supplied reference file and classify it:
   - `REFERENCE_DETAILPAGE_IMAGE`: long PNG/JPG/WebP screenshot or exported design image
   - `REFERENCE_DETAILPAGE_PDF`: PDF or rendered page capture
   - `REFERENCE_DETAILPAGE_HTML`: HTML/page capture
   - `REFERENCE_STYLE_SAMPLE`: partial section, brand mood board, or component sample
2. Make visual references inspectable. Use `view_image` for local images. For long images, inspect the full file and relevant slices.
3. Extract reusable design grammar:
   - section rhythm
   - vertical pacing
   - hero composition
   - section transitions
   - typography scale and contrast
   - color roles
   - card, quote, badge, divider, comparison, and proof patterns
   - image placement and crop behavior
   - density changes across the page
4. Translate the grammar into Danho design tokens and layout rules.
5. Record what must not be copied.
6. Apply the analysis to `DESIGN.md`, mobile screen-flow planning, Phase A HTML, and image prompt style anchors.

## Do Not Copy

Do not copy or closely imitate:

- brand names, logos, marks, badges, or certification graphics
- exact product photography, models, backgrounds, or illustrations
- exact Korean copy, review text, claims, prices, or option names
- exact section order when it does not fit the new product's buyer journey
- exact pixel layout, crop, card positions, or distinctive proprietary composition
- fake proof implied by the reference page

Write the analysis as transferable rules, not as a command to reproduce the reference.

## `REFERENCE_DESIGN_ANALYSIS.md` Template

```markdown
# Reference Design Analysis

## Source Files

| file | type | inspected as | notes |
|---|---|---|---|
| assets/reference-designs/originals/reference-01.png | REFERENCE_DETAILPAGE_IMAGE | full + slices | long mobile screenshot |

## Design Essence Summary

- Overall impression:
- Page rhythm:
- Best reusable strength:
- What to avoid:

## Layout Grammar To Reuse

| pattern | observed essence | Danho adaptation |
|---|---|---|
| hero | e.g. product/result first, short typography, large image mass | adapt with new product promise |
| problem bridge | e.g. close lived moment after hero | use for opening story bridge |
| proof block | e.g. split visual proof from exact facts | keep facts in HTML |
| option section | e.g. large component visual plus concise option cards | keep option facts editable |

## Visual System To Adapt

- Color roles:
  - Key:
  - Main:
  - Sub:
  - Exception:
- Typography:
  - headline behavior:
  - body behavior:
  - label/badge behavior:
- Spacing:
  - section height rhythm:
  - image-to-copy spacing:
  - card density:
- Components:
  - cards:
  - quote/review:
  - comparison:
  - dividers:

## Image Direction Influence

- Full-section image style anchors:
- Support image style anchors:
- Cropping/framing rules:
- What must remain textless:

## Application To This Product

| Danho section/screen | reference essence used | adaptation reason | copy/image caution |
|---|---|---|---|
| 01 hero |  |  |  |
| 02 opening bridge |  |  |  |

## Non-Copy Guardrails

- Do not reuse:
- Transform by:
- Keep product-specific because:

## DESIGN.md Changes

- preset:
- color token changes:
- typography token changes:
- section/component rules:

## QA Notes

- [ ] Reference essence is visible in rhythm and layout, not copied as a clone.
- [ ] New page still follows the new product's buyer journey.
- [ ] No reference brand/copy/logo/image appears in final HTML or generated images.
- [ ] Mutable facts remain editable HTML.
```

## How To Apply To `DESIGN.md`

Use the reference analysis to adjust:

- `design_profile`: describe the adapted visual mood in original words
- color tokens: map reference colors into Danho `Key/Main/Sub/Exception`, not raw copied palette names
- typography tokens: use scale behavior and contrast, not exact font identity unless the user owns the font
- section rhythm: choose compact, medium, full-image, proof-board, and image-supported screens
- components: adapt cards, comparison rows, review blocks, option blocks, and dividers

Do not let reference design override Danho conversion gates. If the reference has weak story flow, copied marketing claims, button UI, sparse text-only bands, or channel-specific pricing, ignore those parts.

## How To Apply To Image Prompts

For prompts, use style anchors like:

```text
Adapt the reference design essence: vertical mobile ecommerce rhythm, large product-led visual mass, restrained proof cards, soft section dividers, high-contrast Korean headline area. Do not copy the reference page, brand, product, exact layout, logos, text, or images.
```

Do not attach or describe a reference design as if it were the product reference. Product consistency comes from product images; design references only guide composition and visual language.
