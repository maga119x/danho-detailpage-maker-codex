# Text-Image Deduplication

Prevent the same Korean copy from appearing twice in adjacent HTML and image areas.

## Rule

One message should be carried by one primary surface:

- Full-section image: image carries the designed copy.
- HTML mixed section: HTML carries the copy and image supports it without text.

## Roles

| Current role | Legacy name | Text policy |
|---|---|---|
| `FULL_IMAGE` | `REPLACE` | Image may contain short Korean copy; remove duplicate HTML layout |
| `HTML_MIXED` | `SUPPORT` | HTML keeps copy; support image has no text |
| `HTML_ONLY` | `NONE` | HTML only |

## Full-Image Handling

```html
<section id="hook" class="full-image-section">
  <img class="full-section-image" src="../assets/generated/ai-section-designs/01_hook.png" alt="방화문에도 붙는 무타공 자석도어스토퍼">
</section>
```

Do not leave a nearby HTML `<h1>` with the same text.

## HTML-Mixed Handling

```html
<section id="fit-check" class="detail-section">
  <h2>구매 전에는 이 조건만 먼저 확인하세요</h2>
  <img src="../assets/generated/fit-check-magnet-test.png" alt="자석 부착 가능 여부 확인">
  <ul>...</ul>
</section>
```

The support image must not include the same Korean copy as the HTML.

## Fallback

If a generated full-section image has incorrect Korean text:

1. Regenerate with shorter text, or
2. Use a textless support image plus accurate HTML text, or
3. Keep the section as HTML mixed.

## Validation

- Search the final page visually for repeated headlines.
- Check `alt` text does not create adjacent visible duplication; descriptive alt is fine.
- Verify `FULL_IMAGE` sections do not leave duplicate HTML siblings.
- Verify support images have no visible text, labels, captions, or signage.
