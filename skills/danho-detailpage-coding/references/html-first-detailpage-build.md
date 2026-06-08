# HTML-First Detail Page Build

Use this whenever creating a new detail page after planning.

## Required Order

Do not generate final design images before the HTML layout exists.

1. Build a complete HTML detail page from `PLANNING.md` and `DESIGN.md`.
2. Make the HTML look like a finished ecommerce detail page with placeholders or support-image slots.
3. Render and inspect the HTML at mobile widths.
4. Create `image-plan.md` from the inspected HTML.
5. Generate designed section images only for approved `FULL_IMAGE` sections.
6. Replace those HTML sections with generated images in Phase B.
7. Keep factual sections as editable `HTML_MIXED` or `HTML_ONLY`.

## Phase A Quality Bar

The first HTML version must not be a simple web page.

It must already include:

- ecommerce detail-page section rhythm
- strong product hero or hook area
- large visual slots where imagery will persuade
- proof components such as quote cards, checklists, comparison rows, FAQ bubbles, price panels
- mobile-readable typography
- role-based color system

If Phase A looks unfinished without generated images, fix the HTML before image generation.

## Forbidden Phase A Output

- Generic landing page sections
- Navigation/marketing hero plus feature cards only
- Plain centered text blocks with empty space
- Desktop 2-column layouts squeezed into mobile
- Repeated identical cards from top to bottom
- `413px` fixed-width page wrappers
- Image generation prompts before layout decisions

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
