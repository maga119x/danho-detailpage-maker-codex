# Commercial Color System Reference

Use this reference when HTML elements look too colorful or when creating a new `DESIGN.md`/CSS system.

## Principle

Commercial detail pages should not use many unrelated accent colors. Use role-based color tokens:

| Role | Purpose | Example |
|---|---|---|
| Key | body text, dark sections, strong contrast | deep navy / charcoal |
| Main | brand emphasis, price, active proof, key icon | restrained blue or brand primary |
| Sub | neutral backgrounds, cards, soft surfaces | cool gray / blue tint |
| Exception | warning, limitation, unavailable condition | muted amber or red, used rarely |

## Rules

- Use Key and Sub for most of the page.
- Use Main for important selling emphasis only.
- Use Exception only for risk, warning, incompatibility, or stock/availability conditions.
- Do not use green, yellow, red, purple, and blue all as generic accents in the same page.
- Do not color-code every speech bubble differently unless the colors carry real meaning.
- Prefer hierarchy through size, weight, border, tint, spacing, and shadow before adding another hue.

## Token Pattern

```css
:root {
  --ink: #111827;
  --muted: #4b5563;
  --key: #101827;
  --main: #1559d6;
  --sub: #e8edf3;
  --main-tint: #eaf2ff;
  --exception: #8a5a00;
  --exception-tint: #fff6df;
  --paper: #fff;
  --soft: #f6f8fb;
}
```

## Component Mapping

- Headline emphasis: `--main`
- Tags and badges: `--main-tint` background, `--main` text
- Cards: white or `--soft`
- Dark sections: `--key`
- Price: `--main`
- Checklist icon background: `--main-tint`
- Comparison winner: `--main`, not a new green
- Warning or incompatible product note: `--exception-tint` + `--exception`

## Checklist

- Search CSS for raw hex colors before delivery.
- Confirm general HTML elements use only role tokens and neutral colors.
- Allow generated full-section images to contain their own palette, but keep adjacent HTML calmer.
- If a color does not mean brand, hierarchy, surface, or warning, remove it.
