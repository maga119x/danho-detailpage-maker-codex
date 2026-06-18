# Detail Page Typography Reference

Use this before writing or revising detail-page HTML/CSS.

## Meaning Of Mobile-First

Mobile-first does not mean "make the canvas exactly 413px wide" or render the page directly at 393px/438px as the main QA target.

It means:

- design a canonical 860px-wide ecommerce detail-page source
- preview that same source scaled down to 438px phone width
- keep text readable in the 438px scaled preview without zooming
- keep line length short enough for fast scanning
- use `clamp()` values for source-sized typography and spacing
- avoid a fixed phone wrapper and avoid direct 393px/438px viewport reflow as the primary check

The expected scale factor is `438 / 860 = 0.509`. A 32px source body reads as about 16px after scaling.

## Required Font Scale

Use this scale unless the user provides a stronger brand system.

```css
:root {
  --font-display: clamp(4rem, 8vw, 6rem);        /* source 64-96px -> 438px preview about 33-49px */
  --font-h1: clamp(3.5rem, 7vw, 5.25rem);        /* source 56-84px -> 438px preview about 29-43px */
  --font-h2: clamp(2.875rem, 5.6vw, 4.25rem);    /* source 46-68px -> 438px preview about 23-35px */
  --font-h3: clamp(2.25rem, 4.2vw, 3rem);        /* source 36-48px -> 438px preview about 18-24px */
  --font-body-lg: clamp(2rem, 3.6vw, 2.375rem);  /* source 32-38px -> 438px preview about 16-19px */
  --font-body: clamp(2rem, 3.7vw, 2.25rem);      /* source 32-36px -> 438px preview about 16-18px */
  --font-small: clamp(1.875rem, 3.4vw, 2.125rem); /* source 30-34px -> 438px preview about 15-17px */
  --font-caption: clamp(1.875rem, 3.2vw, 2rem);  /* source 30-32px -> 438px preview about 15-16px */
  --font-micro: clamp(1.625rem, 3vw, 1.875rem);  /* source 26-30px -> 438px preview about 13-15px, exceptional only */
}
```

Korean ecommerce detail pages should usually use:

- body: 32-36px at 860px source, about 16-18px at 438px preview
- lead copy and other headline-adjacent text: 32-38px at source, about 16-19px at preview
- section headline: 46-68px at source, about 23-35px at preview
- hero headline: 56-84px at source; only the shortest opening display headline may use 64-96px
- card text: 30-34px at source, about 15-17px at preview
- badges/captions inside the selling flow: source size that scales to 15-16px or larger
- micro legal/spec footnotes: source size that scales to 13-15px only when the content is intentionally secondary

Avoid:

- body text that scales above about 20px in the 438px preview for normal paragraphs
- card body text that scales above about 18px in the preview
- FAQ answers, card paragraphs, long leads, closing reassurance, or option guidance set in display, h1, or h2 sizing
- three-line Korean headlines that fill most of the section height before the visual/proof appears
- normal labels, badges, reviews, comparison text, or closing text that scales below 16px
- micro copy that scales below about 13px
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
- product/result closing copy

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

- Section padding source: `96-140px` top/bottom, which previews as about `49-71px`
- Gap between headline and lead source: `20-32px`
- Gap between copy block and image source: `36-56px`
- Gap between image and proof card source: `32-48px`

## Validation

At 860px source width and in the 438px scaled preview:

- The body copy should read naturally without zooming.
- No heading should wrap into awkward one-character lines.
- Korean headlines should wrap by phrase/word, not syllable by syllable.
- Cards should not feel like desktop cards squeezed into mobile.
- The page should feel like a product detail page, not a generic landing page.

Do not treat a direct 393px/438px viewport render as the primary QA result. That path is useful only as an additional stress check after the 860px source plus scaled preview passes.
