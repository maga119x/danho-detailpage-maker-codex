# HTML-First Detail Page Build

Use this whenever creating a new detail page after planning.

## Required Order

Do not generate final design images before the HTML layout exists.

1. Build a complete HTML detail page from `PLANNING.md` and `DESIGN.md`.
2. Read the mobile screen-flow plan. If missing, create a temporary viewport storyboard before coding.
3. Split dense content points into screen-sized sections before writing HTML.
4. Make the HTML look like a finished ecommerce detail page with placeholders or support-image slots.
5. Open or render the HTML at the 860px source width, then inspect the same source scaled to a 438px phone preview.
6. Create `image-plan.md` from the inspected HTML.
7. Confirm `image-plan.md` contains mandatory `FULL_IMAGE` rows for the opening hero and final product/result closing section.
8. Generate designed section images for every approved `FULL_IMAGE` section.
9. Replace those HTML sections with generated images in Phase B.
10. Keep factual sections as editable `HTML_MIXED` or `HTML_ONLY`.

## Phase A Quality Bar

The first HTML version must not be a simple web page.

It must already include:

- ecommerce detail-page section rhythm
- mobile screen roles and varied visual mass, not one repeated section skeleton
- enough screen depth for the product complexity; do not compress multiple purchase judgments into one viewport
- strong product hero or hook area
- large visual slots where imagery will persuade
- proof components such as quote cards, checklists, comparison rows, FAQ bubbles, fit/option information panels, and value-support panels
- a review/testimonial section; use supplied reviews or replacement-ready mock review cards with generic nickname/handle, star rating, highlighted quote, and detailed review copy, without visible replacement warnings
- mobile-readable typography
- role-based color system

If Phase A looks unfinished without generated images, fix the HTML before image generation.

## Forbidden Phase A Output

- Generic landing page sections
- Navigation/marketing hero plus feature cards only
- Plain centered text blocks with empty space
- Desktop 2-column layouts squeezed into mobile
- Repeated identical cards from top to bottom
- One dense section per source bullet when the content needs multiple screen units
- Core benefit, mechanism, proof, option, and FAQ all squeezed into one section
- fixed phone-width page wrappers or direct 393px/438px source canvases
- Image generation prompts before layout decisions
- visible sales channel names, proof markers, review replacement warnings, or production notes

## Section Design Pattern

Most editable sections should follow:

```html
<!-- Fit Check Section -->
<section id="fit-check" class="detail-section">
  <div class="section-copy">
    <span class="eyebrow">구매 전 꼭 확인</span>
    <h2>우리 집 문에 자석이 붙는지 먼저 확인해 주세요</h2>
    <p class="lead">자석이 붙는 철문이나 방화문이라면 간단하게 설치할 수 있어요.</p>
  </div>
  <figure class="section-visual">
    <img src="../assets/generated/fit-check.png" alt="현관문에 자석 부착 여부를 확인하는 모습">
  </figure>
  <div class="proof-card">
    <ul class="check-list">
      <li><span class="mark">✓</span><span>철문 / 방화문 권장</span></li>
      <li><span class="mark">!</span><span>목재문 / 알루미늄문 사용 불가</span></li>
    </ul>
  </div>
</section>
```

This structure is only one medium-tempo pattern. Do not use it for every screen. Use `mobile-screen-storyboarding.md` and `commercial-layout-components.md` to choose impact, question, explainer, proof, compare, catalog, info, and policy screens.

Full-image sections are allowed only after this HTML role has been planned:

```html
<!-- Hook Section -->
<section id="hook" class="full-image-section">
  <img class="full-section-image" src="../assets/generated/ai-section-designs/01_hook.png" alt="...">
</section>
```

## Image Replacement Rule

- `FULL_IMAGE`: image replaces the whole HTML section after generation.
- `HTML_MIXED`: keep the HTML section and add a textless support image.
- `HTML_ONLY`: keep HTML only.

Never skip the HTML layout stage just because the final section may become an image.

## Low-Dependency Preview Rule

Phase A and Phase B HTML must remain plain static HTML/CSS.

- Use relative asset paths so the file opens directly through `file://`.
- Do not require Node, npm, a temporary dev server, Playwright, Python, a bundler, or a local HTTP server for ordinary viewing.
- If browser automation exists, it may produce screenshots, but the screenshot workflow must use 860px source width plus a 438px scaled preview.
- If automation is unavailable, perform manual browser inspection or static HTML checks and note any visual QA that could not be executed.
