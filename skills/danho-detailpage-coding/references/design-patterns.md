# Text-to-Design Patterns

Use these patterns to convert raw Korean copy into designed static HTML.

## Principles

- Design must be complete in the default state.
- Use image + copy + proof together; do not leave text floating far from media.
- Choose the screen's dominant mass before choosing a component: image, type, proof, or card.
- Split dense content into multiple screen-sized sections instead of adding more cards to one section.
- Use a restrained color system. See `color-system.md`.
- Avoid one repeated section layout across the whole page.
- Keep internal planning labels out of the final UI.

## Pattern Selection

| Content type | Pattern |
|---|---|
| Opening differentiation | comparison hook |
| Desired result | result-first hero |
| Transition to why/how | question transition |
| Mechanism / principle | mechanism explainer |
| Measurement / quantified proof | measurement proof |
| Awards / certification / sales proof | proof board |
| Use cases | use-case grid |
| Product details | feature callout map |
| Customer thoughts | speech bubbles |
| Reviews | quote cards |
| Conditions / fit check | checklist card + support image |
| Installation | large process image + numbered steps |
| Comparison | mobile comparison rows |
| Current-price guidance / options | product image + current-price guidance panel |
| FAQ | support image + question bubbles |
| Emotional hook / CTA | designed full-section image |

## Speech Bubble

Use for short customer thoughts or FAQ. Do not use tails for every stacked dark card.

```html
<div class="bubble blue-bg">Q. 모든 문에 붙나요?<br><span class="small">자석이 붙는 철문과 방화문에 적합합니다.</span></div>
```

## Quote Card

Use for stacked reviews, especially on dark backgrounds.

```html
<div class="quote-stack">
  <div class="quote-card">전세집이라 걱정했는데 구멍을 내지 않아도 돼서 바로 썼어요.</div>
  <div class="quote-card">유모차를 들여올 때 문이 다시 닫히지 않아 편해졌습니다.</div>
</div>
```

```css
.quote-card {
  position: relative;
  overflow: hidden;
  padding: 22px 28px 22px 44px;
  border-radius: 8px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.18);
}
.quote-card::before {
  content: "";
  position: absolute;
  left: 18px;
  top: 18px;
  bottom: 18px;
  width: 5px;
  border-radius: 8px;
  background: var(--main);
}
.quote-card::after {
  content: "”";
  position: absolute;
  right: 18px;
  top: -8px;
  color: rgba(255,255,255,.12);
  font-size: 90px;
  line-height: 1;
}
```

## Checklist Card

Use for compatibility and buying conditions. Convert raw checkbox symbols to styled elements.

```html
<ul class="check-list">
  <li><span class="mark">🧲</span><span>현관문에 자석이 붙는 철문 또는 방화문인가요?</span></li>
</ul>
```

## Comparison Rows

Use instead of dense tables on mobile.

```html
<div class="compare-row featured">
  <strong>자석식</strong>
  <p>자석 부착 후 떼어 이동할 수 있습니다</p>
</div>
```

## Full-Section Image

Use for a complete generated section. The HTML around it should be minimal.

```html
<section id="final-closing" class="full-image-section">
  <img class="full-section-image" src="../assets/generated/ai-section-designs/16_final-closing.png" alt="...">
</section>
```

## Static Constraints

Forbidden:

- `:hover`
- `transition`
- `animation`
- `@keyframes`
- JavaScript

Use `border`, `box-shadow`, contrast, spacing, and role-based color tokens for static polish.
