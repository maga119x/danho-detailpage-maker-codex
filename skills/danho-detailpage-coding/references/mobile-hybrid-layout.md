# Mobile Hybrid Layout Reference

Use this reference when building or revising the final ecommerce detail page.

## Current Direction

The final page should feel like a mobile-first vertical story, not a collection of fixed-ratio cards.

Build the HTML detail-page layout before image generation. Generated section images should replace or support an already planned HTML section role.

Do:

- Use natural-height sections with enough top/bottom breathing room.
- Keep sections vertically oriented: headline, large image, then proof or action element.
- Mix full-section generated images with HTML+image sections.
- Use images inside HTML sections when they help persuasion.
- Use speech bubbles, badges, checklists, quote cards, comparison rows, and product cards as designed HTML components.
- Use readable mobile typography. Mobile-first is not a fixed 413px canvas.

Do not:

- Force every section to 9:16 or 3:4.
- Set the page wrapper to a fixed phone width.
- Stretch a weak layout by only changing height.
- Use the same section layout repeatedly.
- Separate text and image so far apart that the section feels unfinished.
- Show internal planning labels in the page.
- Generate final section images before the HTML structure and image-plan exist.

## Hybrid Split

When the user asks for hybrid, a strong default is:

- 50% designed full-section images
- 50% editable HTML+image sections

Use full-section images for:

- hook or opening hero
- lifestyle problem scene
- emotional blocker
- product answer or concept turn
- no-damage / rental reassurance
- daily-use lifestyle moment
- foot-control or tactile use moment
- final CTA

Use HTML+image sections for:

- fit check and compatibility
- install steps
- height or size guidance
- material details
- comparison
- reviews that must stay editable
- price and options
- FAQ

## Section Structure

Use this vertical sequence for HTML sections:

```html
<section id="fit-check" class="detail-section">
  <div class="copy">
    <span class="tag">consumer-facing label</span>
    <h2>headline</h2>
    <p class="lead">short setup</p>
  </div>
  <div class="visual">
    <img src="../assets/generated/fit-check.png" alt="...">
    <div class="image-note">short visual proof</div>
  </div>
  <div class="card">checklist / quote / comparison / price</div>
</section>
```

For designed full-section images:

```html
<section id="hook" class="full-image-section">
  <img class="full-section-image" src="../assets/generated/ai-section-designs/01_hook.png" alt="...">
</section>
```

## Component Guidance

- Use speech bubbles for customer thoughts, short questions, or quick FAQ.
- Use quote cards for reviews. Do not put generic speech-bubble tails between stacked cards; they can render like broken diamonds.
- Use a left accent rule and a subtle quote watermark for dark review cards.
- Use comparison rows instead of dense tables on mobile.
- Use product images in price/options sections when the buyer is close to purchase.

## Visual Checks

Render at 393px and optionally 413px mobile width and verify:

- no horizontal overflow
- body copy is 16-18px or equivalent readable size
- headings are large enough to sell but not so large that they wrap awkwardly
- all images loaded
- full-image section count matches plan
- HTML section count matches plan
- pseudo-elements such as speech-bubble tails and quote marks render intentionally
- section rhythm alternates between image impact and editable information
