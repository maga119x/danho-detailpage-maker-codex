---
name: danho-detailpage-coding
description: Build or revise static HTML/CSS for Korean ecommerce 상세페이지 projects from PLANNING.md, DESIGN.md, image-plan.md, and generated assets. Use for HTML-first detail-page layout, mobile-readable typography, final hybrid image/HTML pages, section splitting, color-system cleanup, image replacement, and visual validation.
---

# Danho Detailpage Coding

Create static, mobile-first ecommerce detail pages. Build the HTML layout first, then use image planning and generated images to replace or support selected sections.

## Inputs

- `PLANNING.md`
- `DESIGN.md`
- `config.json`
- Optional `image-plan.md`
- Optional `assets/generated/` or `assets/inbox/`

## Build Modes

### Phase A: Text-First HTML

Use when image roles are not final.

- Include all copy in HTML.
- Build a finished ecommerce detail-page layout in HTML before any final image generation.
- Use placeholders, existing product images, or visual slots only after deciding their section role.
- Keep the page persuasive and visually structured without generated images.
- Do not output a generic landing page, simple centered web page, or desktop feature grid.

### Phase B: Hybrid Final HTML

Use when image roles and assets exist.

- Use designed full-section images for high-impact visual/story sections.
- Use HTML+image mixed sections for editable factual sections.
- Avoid duplicated Korean copy between nearby HTML and full-section images.
- Preserve exact pricing, options, compatibility, and FAQ as HTML.

## Current Layout Rules

Read `references/html-first-detailpage-build.md` before starting a new page.
Read `references/mobile-hybrid-layout.md` before major layout work.
Read `references/detailpage-typography.md` before writing CSS.

Core rules:

- Do not force fixed 9:16 or 3:4 section ratios.
- Mobile-first means readable responsive typography on phone widths, not a fixed `413px` wrapper.
- Keep a vertical mobile rhythm: top copy, large image/scene, then evidence card, quote card, speech bubble, checklist, or comparison.
- HTML sections may and often should contain images.
- Full-section images are valid when the image model designed the whole section with background, typography, cards, and icons.
- Keep a typical hybrid split around 50% full-section images and 50% HTML+image sections when the user asks for hybrid.
- Use consumer-facing labels only; internal planning labels must not appear.
- Use a restrained color system. Read `references/color-system.md`.

## Image Role Rules

Read `references/image-handling.md` and `references/text-image-deduplication.md`.

- `FULL_IMAGE`: full-section image replaces the original HTML layout.
- `HTML_MIXED`: HTML section remains and uses a textless image inside or near the section.
- `HTML_ONLY`: no image needed.
- Legacy plans may call these `REPLACE`, `SUPPORT`, and `NONE`; map them before coding.
- If generated Korean typography is wrong, fall back to textless image + accurate HTML overlay or keep the section as HTML.

## CSS Rules

- Max page width: 860px.
- Set `box-sizing: border-box`.
- Set page `overflow-x: hidden`.
- Use detail-page typography: body 16-18px, lead 17-22px, h2 28-44px, hero 36-54px unless the brand requires otherwise.
- Use `clamp()` for responsive type and spacing; do not set a fixed mobile canvas width such as 413px.
- Avoid JavaScript, `:hover`, `transition`, `animation`, and `@keyframes`.
- Cards and quote blocks must look complete in default static state.
- Do not use card-in-card layouts.
- Use stable image dimensions or responsive constraints so text and media do not overlap.

## Validation

Before final response:

1. Check image paths and section counts.
2. Split sections:
   ```bash
   python skills/danho-detailpage-coding/scripts/split_sections.py <html> <output-dir>
   ```
3. Render mobile width, preferably 393px, and verify:
   - no broken images
   - no horizontal overflow
   - typography is readable and not oversized
   - the page looks like a product detail page, not a simple web page
   - full-image/HTML split matches `image-plan.md`
   - quote/speech-bubble pseudo-elements render correctly
   - HTML colors follow the role-based palette

## References

- `references/mobile-hybrid-layout.md` - current layout and hybrid rules
- `references/html-first-detailpage-build.md` - mandatory HTML-first production workflow
- `references/detailpage-typography.md` - mobile-readable type and spacing scale
- `references/color-system.md` - commercial color system rules
- `references/image-handling.md` - image role and placement rules
- `references/design-patterns.md` - text-to-design patterns
- `references/output-checklist.md` - final validation checklist
- `references/static-design.md` - static page constraints
