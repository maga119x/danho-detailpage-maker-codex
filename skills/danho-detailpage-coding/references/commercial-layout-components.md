# Commercial Layout Components

Use this when converting a screen storyboard into HTML/CSS. These are not decorative components; each one handles a specific purchase judgment.

## Global Component Rules

### Badges / Kickers

Badges and kickers must not be internal section taxonomy. Use them only when they add buyer-facing meaning.

Use badges for:

- buyer situation: `칼 때문에 시작이 막힌다면`
- micro-benefit: `무뎌질 때 바로 관리합니다`
- proof cue: `고기와 대파부터 달라집니다`
- action cue: `받는 구성을 먼저 봅니다`

Avoid badges such as:

- `문제 인식`
- `전환점`
- `사용 장면`
- `제품 디테일`
- `구매 전 FAQ`

If the badge only names the section type, remove it and let the headline do the work.

### Text Alignment

Default section-level selling copy should be centered. Left-align text inside structured components where scanning exact information matters: cards, comparison rows, option rows, FAQ items, review cards, notices, and checklists.

## 1. Comparison Hook

Purpose: define why this product deserves attention before detailed explanation.

Use when:

- the buyer knows a common alternative
- the product has a clear method, result, material, or convenience difference

Layout:

- bold headline at top
- 2 visual columns or cards
- winner uses brand/main/accent color
- alternative uses gray/desaturated treatment
- one short conclusion below

Avoid:

- equal visual weight for winner and alternative
- long table copy
- more than 3 comparison points in the opening hook

## 2. Result-First Hero

Purpose: show the desired after-state before explaining features.

Use when:

- the outcome is visually understandable
- the buyer cares about the final result more than specs

Layout:

- large result image, usually 60-80% of the screen
- product appears in or near the result when possible
- 1-2 line headline
- minimal body copy

Avoid:

- product-only photo with no outcome
- vague lifestyle background where the product/result is hard to inspect

## 3. Question Transition

Purpose: make a long page feel intentional and easier to follow.

Use before:

- mechanism explanation
- comparison
- proof
- FAQ-like objection handling

Layout:

- wide vertical spacing
- short question or declaration
- optional vertical line, dot, arrow, or tiny label
- no dense paragraph

Avoid:

- internal labels such as "기술 설명" or "구매 판단"
- a question that is not answered in the next screen

## 4. Mechanism Explainer

Purpose: turn a technical or structural advantage into a visual explanation.

Use when:

- the product works differently from alternatives
- material, structure, process, or method matters

Layout:

- one principle sentence
- diagram, product cross-section, close-up, or simple arrows
- 1-3 callouts
- final buyer-gain sentence

Implementation:

- Prefer HTML/CSS/SVG labels for editable text.
- Do not generate long Korean or numeric proof into an image.

## 5. Spec Proof Pair

Purpose: make a technical detail tangible.

Use when:

- two parts/specs support one claim

Layout:

- two matched images or close-ups
- short label under each
- one conclusion statement

Avoid:

- placing many unrelated specs in one row
- using tiny captions below 16px for important selling copy

## 6. Proof Board

Purpose: build authority quickly.

Use for:

- awards
- sales records
- certifications
- media proof
- real measured claims

Layout:

- dark or high-contrast background
- one large proof number or title
- evidence images or badges
- concise basis/source line

Avoid:

- fake authority
- unsupported numbers
- more than 3 equal-priority proof items

## 7. Measurement Proof

Purpose: make quantitative claims believable.

Use for:

- temperature, time, weight, noise, brightness, durability, absorption, strength, cost/time reduction

Layout:

- real measurement/use scene
- numeric badge
- simplified graph or comparison
- final conclusion in plain buyer language

Keep numeric claims editable when they are factual or may change.

## 8. Use-Case Grid

Purpose: expand perceived utility without long explanation.

Use for:

- food categories
- styling examples
- storage uses
- app/service features
- routines or scenarios

Layout:

- 2-column grid on mobile
- consistent image ratio
- labels of 1-3 words
- intro headline before the grid

Avoid:

- icon-only grids for visual products
- long sentences inside tiles

## 9. Feature Callout Map

Purpose: show product details as a designed infographic.

Use for:

- physical products with visible details
- material/structure/function differentiation

Layout:

- product image or multiple angle crops
- connecting lines
- short title + 1-line explanation per callout
- emphasized callouts for the top 1-2 purchase drivers

Implementation:

- Keep text in HTML where possible.
- Verify callout labels do not overlap at 393px width.

## 10. Review Highlight Stack

Purpose: turn reviews into readable proof, not a wall of text.

Use for:

- every page, with supplied reviews or neutral replacement-ready dummy cards

Layout:

- review proof intro
- review card or capture
- one highlighted sentence per review
- optional user image/product result image

Avoid:

- fabricated names, stars, dates, counts, or "actual buyer" claims when reviews are placeholders
- long unhighlighted review blocks

## 11. Recommended-For Cards

Purpose: let buyers self-identify.

Use when:

- product applies to multiple situations or user types

Layout:

- alternating image/text cards or 2-column cards
- buyer type
- one specific situation
- check icon or small badge

Avoid:

- generic target labels such as "everyone"
- six text-only cards with no scene difference

## 12. Reward / Option Card

Purpose: show what the buyer receives and how choices differ.

Use for:

- sets, rewards, bundles, variants, options, subscriptions

Layout:

- option or item badge
- product image
- included items
- color/size/capacity/spec rows
- price/order guidance as editable HTML

Split into multiple screens:

1. overview
2. item cards
3. set summary
4. price/order guidance
5. compatibility or FAQ

Avoid:

- one giant pricing table with every item
- price embedded in generated images

## 13. Compatibility Note

Purpose: prevent wrong purchase.

Use for:

- fit, size, device, material, installation, safety limits

Layout:

- clear buyer-facing heading
- allowed conditions
- not recommended / check first conditions
- calm warning color for exception
- support image if it clarifies the condition

Place important blockers early, not only in FAQ.

## 14. FAQ / Policy Zone

Purpose: remove final objections and present operational information.

Layout:

- FAQ question as pill or bold row
- answer with line-height 1.6+
- policy in a quieter section after selling flow
- no decorative complexity

Avoid:

- FAQ that repeats earlier selling copy
- defensive caveats scattered through the page
