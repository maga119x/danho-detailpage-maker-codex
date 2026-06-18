# Layout Rules Reference

Use this for static HTML/CSS detail pages.

## Container

```css
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; }
.detail-page {
  width: min(860px, 100%);
  margin: 0 auto;
  overflow-x: hidden;
}
img {
  display: block;
  max-width: 100%;
}
```

## Section Rhythm

Do not use a single fixed ratio for all sections. Build a vertical mobile rhythm instead.
Do not fix the whole page to a phone wrapper. Author the page as an 860px source detail page and verify the same source scaled down to a 438px phone preview. Direct 393px/438px viewport rendering is only a secondary stress check, not the primary QA path.
Design screen-sized purchase judgments. A major content point can and should become multiple sections when it contains several claims, proof types, or buying decisions.

Recommended HTML section order:

1. short consumer-facing tag or badge
2. headline and optional lead
3. large product/lifestyle image
4. proof component: quote, checklist, bubble, comparison, option card, FAQ

Use `min-height` only as a minimum vertical feel, not as the design itself.

Screen rhythm rules:

- Assign each screen one dominant mass: image, type, proof, or cards.
- Split crowded sections before styling. Do not solve density with smaller fonts.
- Insert question, result, or proof screens between dense info/card screens.
- Keep claim and evidence within one screen of each other.
- Normal products usually need 14-22 screen-sized sections; technical or option-heavy products often need more.

## HTML-First Requirement

Before generating or replacing section images, the HTML must already feel like an ecommerce detail page.

Required:

- hero/hook section
- problem or use-scene section
- product answer section
- fit/condition section
- install or use-confidence section
- proof/review section
- options/value information section when product data exists
- FAQ or objection handling
- final product/result closing

If the output looks like a generic website with centered text and cards, revise the HTML before image generation.

## Typography

Use `references/detailpage-typography.md` for exact scale.

Minimum rules:

- body: 32-36px at 860px source, about 16-18px in the 438px scaled preview
- lead/body-lg: 32-38px at source, about 16-19px in the preview
- h2: 46-68px at source, about 23-35px in the preview
- h1/hero: 56-84px at source; largest display hero only 64-96px
- card body: 30-34px at source, about 15-17px in the preview
- line-height: 1.55-1.75 for body
- use `clamp()` for responsive type
- do not use display/h1/h2 sizing for FAQ answers, card paragraphs, long leads, or closing reassurance copy

## Full-Image Sections

Use when a generated image is the whole designed section.

```html
<!-- Hook Section -->
<section id="hook" class="full-image-section">
  <img class="full-section-image" src="../assets/generated/ai-section-designs/01_hook.png" alt="...">
</section>
```

```css
.full-image-section { line-height: 0; background: #fff; }
.full-section-image { display: block; width: 100%; height: auto; }
```

## HTML+Image Sections

Use when text must stay editable.

```html
<!-- Fit Check Section -->
<section id="fit-check" class="detail-section">
  <div class="copy">...</div>
  <div class="visual"><img src="../assets/generated/fit-check.png" alt="..."></div>
  <div class="card">...</div>
</section>
```

Support images can live inside the section when they tighten the argument.

## Layout Selection

- Use vertical stack for mobile-first sections.
- Avoid 2-column layouts unless desktop-only or content is very short.
- Use comparison rows instead of dense tables.
- Use quote cards for reviews.
- Use review/testimonial cards even when real reviews are not supplied. Replacement-ready mock cards must look complete with generic nickname/handle, star rating, highlighted quote, and detailed benefit-based review copy; replacement status stays internal.
- Mock review cards must not contain verified-buyer or sourced-specific claims such as `실제 구매자`, exact dates, locations, review counts, purchase counts, or order numbers unless supplied.
- Use option/benefit guidance panels for options. Do not hard-code numeric prices or sales channel names in the detail page.
- Use grids only for short labels or 1-word/2-word items.

## Section IDs

Every section must have:

- an HTML comment
- a unique lowercase hyphenated id

```html
<!-- Review Proof Section -->
<section id="review-proof" class="detail-section dark">...</section>
```

## Overflow Prevention

Check at 860px source width and in the 438px scaled preview:

- no element exceeds viewport width
- no text overlaps images
- pseudo-elements do not escape awkwardly
- images are fully loaded

The static HTML must also open directly from the filesystem with relative asset paths. Do not require a Node/dev server, bundler, Playwright, Python runtime, or local HTTP server for ordinary viewing and manual QA.

## Forbidden

- JavaScript
- `:hover`-dependent design
- `transition`
- `animation`
- `@keyframes`
- card inside card
- over-compressed sections that combine problem, solution, mechanism, proof, caveat, and action
- fixed global aspect-ratio for all sections
- fixed phone-width page wrappers or direct 393px/438px source canvases
- image generation before HTML layout and image-plan
- visible `NEEDS_PROOF`, `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`, sales channel names, or channel-specific instructions
