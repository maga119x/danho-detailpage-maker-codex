# Screen Flow Planning

Use this before writing the section table. A strong mobile detail page is not a short list of sections. It is a sequence of screen-sized purchase decisions.

## Core Principle

One content point is often too much for one section and too dense for one mobile screen.

Do not compress a major benefit into one section like:

`problem + product answer + mechanism + proof + caveat + final product impression`

Split it into multiple screen units:

1. buyer scene or result
2. short claim or question
3. product mechanism or detail
4. proof, comparison, review, or measurement
5. caveat, fit check, or closing impression when needed

This intentionally makes the page longer. Long is not a problem when each screen answers one purchase question clearly. A short dense page is harder to understand and usually looks less commercial.

## Opening Story Bridge Gate

Before writing the screen-flow table, define the first two screens as a connected opening pair.

| Screen | Required job | Failure mode |
|---|---|---|
| 01 | name the product/use case and promise the buyer's desired result | vague slogan, tiny product, no category cue |
| 02 | continue the same buyer moment and show the repeated friction, feeling, or next question behind the promise | abrupt generic problem, unrelated benefit, feature/spec jump |

Use `OPENING_STORY_BRIDGE_REQUIRED` when the first two screens do not yet connect. Do not proceed to the section table until the bridge is fixed.

Required fixes:

- Give screen 02 a concrete moment that naturally follows screen 01: after purchase, while using, while failing with the current workaround, or while deciding whether the product fits.
- Reuse one anchor across both screens: buyer situation, product noun, repeated action, location, color/visual motif, or emotional phrase.
- Expand screen 02 beyond a short centered statement when needed. Use a large story image, 2-3 short narrative beats, a quote/checklist, or a before/current workaround visual.
- Keep screen 02 distinct from screen 01. It should deepen the story, not repeat the hero promise with different wording.

## Required Visual Strategy Pass

Before the visible section table, create a screen-flow table.

Use these fields:

| Field | Meaning |
|---|---|
| `screen_role` | `impact`, `question`, `explainer`, `result`, `proof`, `compare`, `catalog`, `info`, `policy` |
| `visual_mass` | `image-dominant`, `type-dominant`, `proof-dominant`, `card-dominant` |
| `surface_role` | `paper`, `warm-lifestyle`, `dark-proof`, `accent-declaration`, `policy-quiet` |
| `tempo` | `low`, `medium`, `high` |
| `proof_type` | `none`, `photo`, `measurement`, `certificate`, `review`, `comparison`, `spec`, `policy` |
| `editable_risk` | `low`, `medium`, `high`; use high for price, options, specs, compatibility, FAQ, policy |
| `layout_pattern` | e.g. `comparison-hook`, `result-first-hero`, `question-transition`, `mechanism-explainer`, `proof-board`, `measurement-proof`, `use-case-grid`, `feature-callout-map`, `review-highlight-stack`, `reward-option-card`, `faq-policy-zone` |
| `sparse_image_gate` | `pass`, `SPARSE_SECTION_IMAGE_REQUIRED`, or `merge_required`; use this when a section has little copy, one note, or 1-2 small cards |

When planning badges/kickers, do not use the internal `screen_role` or section category as visible copy. A badge must become a buyer-facing micro message, proof cue, or action cue. If it adds no meaning beyond the headline, omit it.

## Mandatory Full-Image Gate

Every newly produced Danho detail page must plan generated designed full-image sections. This is a production requirement, not a stylistic option.

Minimum contract:

- Screen 01 hero: `REPLACE_CANDIDATE` / future `FULL_IMAGE`
- Final product/result closing impression: `REPLACE_CANDIDATE` / future `FULL_IMAGE`

If the final area also needs mutable legal, price, option, or compatibility facts, split those facts into an adjacent editable HTML section. Do not use mutable facts as a reason to omit the generated full-image closing screen, and do not put purchase-action text in that final image.

Fail the plan when the screen-flow table or section table has no mandatory full-image hero and no mandatory full-image final closing screen.

## Screen Flow Table Template

```markdown
## 1-8. 모바일 화면 흐름 설계

| screen | section id | screen_role | visual_mass | surface_role | tempo | main claim / scan answer | evidence or visual | layout_pattern | sparse_image_gate | editable_risk |
|---:|---|---|---|---|---|---|---|---|---|---|
| 01 | hook | impact | image-dominant | dark-proof | low | 무엇이 다른지 첫 화면에서 판단 | 결과/비교 이미지 | comparison-hook | pass | low |
| 02 | result | result | image-dominant | paper | low | 구매자가 원하는 결과 | 사용 후 장면 | result-first-hero | pass | low |
| 03 | why-possible | question | type-dominant | paper | low | 어떻게 가능할까요? | 다음 화면으로 연결 | question-transition | SPARSE_SECTION_IMAGE_REQUIRED | low |
| 04 | mechanism | explainer | proof-dominant | paper | medium | 구조가 다릅니다 | 단면/부품/화살표 | mechanism-explainer | pass | medium |
```

## Content Expansion Rules

### Major Benefit

Split one major benefit into at least 3 screens when it is central to purchase.

Recommended split:

1. `result` screen: desired after-state or use result
2. `question` screen: why this result happens
3. `explainer` screen: mechanism, material, structure, or method
4. `proof` screen: review, comparison, measurement, certification, or real-use photo

### Complex Feature

Do not put every detail into one feature card.

Split:

1. `use scene`: when the buyer notices the feature
2. `detail close-up`: product part or material
3. `proof/caveat`: what it solves and what to check

### Technical Claim

Split:

1. result or problem
2. simple principle
3. part/spec proof
4. measured or comparative proof
5. buyer gain

### Options / Components / Price

Split:

1. option overview
2. individual component cards
3. set summary
4. mutable price or order-area guidance
5. compatibility, FAQ, or policy

Do not put component explanation, prices, specs, warnings, and FAQ into one section.

### Review / Social Proof

Split:

1. review intro or proof context
2. review highlight stack
3. buyer type or use-case recommendation

If real reviews are missing, keep replacement notes internal and write neutral replacement-ready cards only.

## Screen Count Guidance

Use section count based on complexity, not on the number of source bullets.

| Product complexity | Typical screen count | Notes |
|---|---:|---|
| simple low-friction product | 10-14 | still include hook, result/use, proof/review, options, FAQ |
| normal ecommerce product | 14-22 | most Danho pages should land here |
| technical or high-consideration product | 20-32 | split mechanism, proof, comparison, options, FAQ |
| funding/reward/option-heavy product | 24-40 | split reward cards, set summaries, compatibility, policy |

The page may be long. The failure mode to avoid is not length; it is putting too many claims on one screen.

## Rhythm Rules

- For final hybrid output, plan screen 01 as a mandatory generated full-image hero. The final page must not begin with an ordinary HTML text hero.
- Plan the final selling screen as a mandatory generated full-image product/result closing impression. It must not be a button UI and must not include option/order prompts, benefit-check prompts, or action words such as `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `장바구니`, or `주문`.
- Screen 02 must answer why screen 01 matters in the buyer's real life. If it starts a new topic, revise the opening pair before planning later screens.
- The first 3 screens must answer product identity, core buyer benefit, and the first purchase condition or difference.
- Do not place two `high` tempo screens back to back unless the second is FAQ/policy at the end.
- Do not place three similar card sections back to back. Insert a result image, question transition, proof board, or type-dominant declaration.
- A strong claim must be close to proof. If proof is more than one screen away, split or reorder.
- Use dark sections for authority, result reversal, proof, or final impression. Do not use dark only for decoration.
- Use `policy-quiet` for long factual/legal text so it does not compete with selling screens.

## Density And Image Role Gate

Before marking image candidates, reject a section plan when:

- one section contains three or more independent buyer questions or use cases
- a card grid contains more than two paragraph cards about different topics
- a low-copy action/result/transition screen is planned as HTML-only
- a low-copy option, care/storage, value, reassurance, or final decision screen is planned as centered text-only, one note box, or 1-2 small cards with no product/lifestyle/proof image
- the planned vertical length comes from blank padding, empty dark space, or a decorative background rather than meaningful image/proof/content
- the first screen is not a mandatory generated full-image hero
- the final selling screen is not a mandatory generated full-image product/result closing impression
- the final selling screen contains purchase-action text or option/order prompts

Fixes:

- Split a crowded catalog into a summary screen plus 1-2 focused follow-up screens.
- Convert sparse action/result/value/reassurance moments into `REPLACE_CANDIDATE` or an image-story equivalent.
- Convert sparse option/care/fit sections into `SUPPORT_CANDIDATE` with a large textless product, lifestyle, option, storage, or care visual while keeping editable facts in HTML.
- Merge a sparse text-only section into an adjacent proof/detail section when it cannot justify its own visual.
- Keep mutable facts, options, FAQ, and safety as HTML, but make short emotional/result turns visual.

## Category Flow Presets

### Technical Product

`result -> difference -> question -> mechanism -> part/spec proof -> measurement/certificate -> comparison -> use-case -> review -> options -> FAQ`

Use for appliances, tools, functional materials, health devices, and structure-driven products.

### Lifestyle / Emotional Product

`life scene -> emotional promise -> buyer friction -> product answer -> detail touchpoint -> use scenes -> review -> recommended for -> options -> FAQ`

Use for gift, home, decor, premium daily goods, and brand-led products.

### Food / Cooking Product

`appetizing result -> cooking friction -> method difference -> result stack -> safety/storage/care -> review -> components/shipping -> FAQ`

Use for food, cookware, kitchen tools, and meal products.

### Beauty Product

`desired skin result -> problem empathy -> texture/ingredient principle -> routine -> clinical/review proof -> skin type fit -> options -> FAQ`

Use only real clinical proof when supplied. Otherwise keep wording safe.

### Fashion / Goods

`fit or styling result -> daily scene -> material/detail -> size/fit guide -> care -> review -> color/options -> exchange/FAQ`

### Storage / Living Product

`organized after-state -> current friction -> install/use process -> size/fit condition -> before/after comparison -> review -> options -> FAQ`

## Planning Gate

Before coding, reject the plan if:

- screen 02 is abrupt, generic, or unrelated to the promise/scene created by screen 01
- one key benefit is compressed into one dense section
- most sections share the same `visual_mass`
- the first 3 screens do not show product identity, result/benefit, and difference/fit condition
- claims are not paired with a visual or proof type
- low-content sections are left as centered text-only, note-only, or tiny card-only screens instead of `SPARSE_SECTION_IMAGE_REQUIRED` image support or merge
- there is no review/testimonial screen
- there is no mandatory generated full-image hero and final generated full-image closing screen
- options, compatibility, FAQ, or policy are missing for products that need them
- the expected screen count is too short for the product complexity
