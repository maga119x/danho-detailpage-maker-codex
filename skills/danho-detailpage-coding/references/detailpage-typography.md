# Detail Page Typography Reference

Use this before writing or revising detail-page HTML/CSS.

## Meaning Of Mobile-First

Mobile-first does not mean "make the canvas exactly 413px wide".

It means:

- design for 360-430px phone widths first
- keep text readable without zooming
- keep line length short enough for fast scanning
- use responsive `clamp()` values instead of fixed device-only sizes
- verify at one or more real mobile widths such as 393px or 413px

## Required Font Scale

Use this scale unless the user provides a stronger brand system.

```css
:root {
  --font-display: clamp(2.5rem, 10vw, 4rem);     /* 40-64px */
  --font-h1: clamp(2.25rem, 9vw, 3.4rem);        /* 36-54px */
  --font-h2: clamp(1.75rem, 7vw, 2.75rem);       /* 28-44px */
  --font-h3: clamp(1.25rem, 5vw, 1.875rem);      /* 20-30px */
  --font-body-lg: clamp(1.0625rem, 4vw, 1.375rem); /* 17-22px */
  --font-body: clamp(1rem, 3.7vw, 1.125rem);     /* 16-18px */
  --font-small: clamp(1rem, 3.4vw, 1.0625rem);   /* 16-17px */
  --font-caption: clamp(1rem, 3.2vw, 1rem);      /* 16px */
  --font-micro: clamp(.875rem, 3vw, .9375rem);   /* 14-15px, exceptional only */
}
```

Korean ecommerce detail pages should usually use:

- body: 16-18px
- lead copy: 17-22px
- section headline: 28-44px
- hero headline: 36-54px, occasionally larger only for very short words
- card text: 16-17px
- badges/captions inside the selling flow: 16px or larger
- micro legal/spec footnotes: 14-15px only when the content is intentionally secondary

Avoid:

- body text above 20px for normal paragraphs
- card body text above 18px
- normal labels, badges, reviews, comparison text, or CTA text below 16px
- micro copy below 14px
- negative letter spacing
- viewport-only font sizing such as `font-size: 8vw` without a min/max clamp

## Line Height

- Headlines: `1.12-1.25`
- Section titles: `1.18-1.32`
- Body: `1.55-1.75`
- Card text: `1.45-1.65`

## Korean Headline Wrapping

Korean headlines must wrap by phrase/word, not by individual syllable.

Use this for h1/h2/h3 headline selectors:

```css
h1,
h2,
h3 {
  word-break: keep-all;
  overflow-wrap: normal;
  word-wrap: normal;
  line-break: strict;
  text-wrap: balance;
}
```

If a headline still breaks awkwardly, shorten the copy or add deliberate `<br>` at phrase boundaries. Do not allow syllable-by-syllable wrapping just to fit an oversized heading.

## Text Alignment

Default detail-page selling copy should usually be centered:

- hero headline and lead
- section kicker/badge
- section headline
- section lead
- image-story overlay copy
- CTA copy

Use left alignment for structured reading surfaces:

- cards with paragraph copy
- comparison rows
- option rows
- FAQ answers
- review cards
- notices, safety notes, and checklists

Do not set the whole page to left alignment by default unless the page is intentionally a spec sheet or admin-like comparison surface.

## Badge / Kicker Text

Badges are not section labels. They must add meaning.

Good badge examples:

- `칼 때문에 시작이 막힌다면`
- `무뎌질 때 바로 관리합니다`
- `받는 구성을 먼저 봅니다`

Avoid:

- `문제 인식`
- `전환점`
- `사용 장면`
- `구매 전 FAQ`
- `제품 디테일`

## Spacing

Use vertical rhythm, not fixed aspect ratios.

- Section padding mobile: `56-96px` top/bottom
- Section padding desktop/wide detail page: up to `112-140px`
- Gap between headline and lead: `12-18px`
- Gap between copy block and image: `24-36px`
- Gap between image and proof card: `20-32px`

## Validation

At 393px and 413px widths:

- The body copy should read naturally without zooming.
- No heading should wrap into awkward one-character lines.
- Korean headlines should wrap by phrase/word, not syllable by syllable.
- Cards should not feel like desktop cards squeezed into mobile.
- The page should feel like a product detail page, not a generic landing page.
