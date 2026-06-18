# Detail Page Flow Rules

Use this when planning or replanning a product 상세페이지.

## Flow Before Sections

Do not start by listing features. Start with the buyer's decision path.
After the decision path, convert it into a mobile screen flow. One item in the path is not automatically one section.

Strong default flow:

1. Hook: product identity or sharp promise
2. Real-life moment: when the problem happens
3. Blocker: why current solutions feel risky or inconvenient
4. Answer: why this product's method is different
5. Fit check: early purchase-blocking condition
6. Install/use flow: how easy it is to start
7. Removal/damage proof: risk reduction
8. Daily-use effect: what changes in life
9. Control/detail: tactile or functional confidence
10. Compatibility/material: precise confidence
11. Comparison: why this method over alternatives
12. Review proof: lived experience
13. Options/current-price guidance: buyable facts without fixed numeric prices
14. FAQ: remaining objections
15. Final closing: memorable product/result close without purchase-action text

## Opening Two-Screen Story Bridge

The first two screens must read as one opening sequence.

Screen 01 is the promise: product identity, desired result, or sharp contrast.
Screen 02 is the lived moment: the same buyer, place, object, or action shows why that promise matters.

Fail the plan when screen 02 feels like a new slide that could follow any hero. Fix it by adding one or more of:

- same buyer situation or location from screen 01
- repeated object/action noun from the hero copy
- concrete before moment or existing workaround
- emotional beat the buyer would recognize
- visual continuation: same product angle, same setting, or a closer crop of the first scene

Do not make screen 02 only `problem`, `benefit`, `feature`, or `why` as a label. It needs enough story mass: a scene headline, a short lead, and 2-3 narrative beats or a designed image that carries those beats visually.

## Wadiz-Style Empathy Flow

Use this flow when the product needs strong empathy, story, novelty explanation, or buyer desire-building.

1. Catchphrase: a sharp promise or a familiar frustration.
2. Vivid problem: make the buyer recognize their own scene, emotion, wasted time, wasted money, or repeated annoyance.
3. Existing workaround friction: show why current habits, cheap alternatives, or common tools still leave the buyer dissatisfied.
4. Origin/why: briefly explain why this product was made, only with credible facts or safe inferred motivation.
5. Core solution: state the new method in buyer language.
6. Benefit module 1: buyer scene -> product mechanism -> buyer gain.
7. Benefit module 2: buyer scene -> product mechanism -> buyer gain.
8. Benefit module 3: buyer scene -> product mechanism -> buyer gain.
9. Detail/differentiator: material, design, usability, option, service, or care detail that supports the benefits.
10. Trust builder: review/testimonial section plus real test, certification, manufacturing detail, warranty, or supplied proof when available.
11. Specs/components/options: buyable facts.
12. Use guide/care/safety: how to use well and what not to do.
13. Recommended for: concrete buyer types and situations.
14. FAQ: direct objection handling.
15. Final closing: future moment + product/result confidence, without option/order prompts or purchase-action text.

Rules:

- Do not expose labels like "vivid problem" or "origin" as final copy.
- Do not compress a major benefit, technical claim, option system, or proof block into one section. Split it into screen-sized steps: result/scene, question, mechanism/detail, proof, caveat/action.
- A long page is acceptable when each screen is easy to understand. A normal product usually needs 14-22 screens; technical or option-heavy products often need 20-40.
- Use `references/screen-flow-planning.md` to assign screen role, visual mass, surface role, tempo, proof type, editable risk, and layout pattern before coding.
- If no real origin story exists, use a short problem-aware bridge instead of inventing a founder story.
- A review/testimonial section is mandatory. If no real reviews exist, use replacement-ready mock review cards with generic nickname/handle, star rating, highlighted quote, and detailed benefit-based copy. Mark them internally as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`; do not expose this note in visible copy.
- If no other trust proof exists, use precise specs, limits, care guidance, or internal `NEEDS_PROOF` notes instead of fake authority.
- Keep the strongest safety, fit, or compatibility condition early even in emotional pages.
- A long draft is allowed for planning, but final visible copy must be compressed before coding.

## Section Role Table

In `PLANNING.md`, include each section's:

- id
- purpose
- scan answer
- persuasion role
- reason it follows the previous section
- opening bridge role for sections 01-02
- screen role
- visual mass
- tempo
- proof type
- visual role
- image conversion candidate

## Screen Expansion

Use this when a section feels dense:

- `problem + solution` -> split into problem scene and product answer
- `solution + mechanism` -> split into answer claim and mechanism explainer
- `mechanism + proof` -> split into mechanism screen and proof screen
- `feature list + use cases` -> split into feature detail and use-case grid
- `option + component + price + warning` -> split into option overview, component cards, price/order guidance, and compatibility note
- `FAQ + policy` -> split into FAQ screen and quiet policy zone

The reference pages are long because they do not ask the buyer to understand too much in one viewport. Follow that principle for other products too.

## Internal Labels

Planning labels can help the agent, but final page copy must not expose them.

Avoid final visible labels like:

- 모바일 구매 판단 요약
- 불편의 순간
- 설치 방식
- 소재감
- FAQ

Convert them into buyer-facing labels:

- 우리 집 문부터 체크
- 구멍과 자국이 걱정될 때
- 공구 없이 3단계
- 현관에 어울리는 실버
- 마지막 궁금증

## Candidate Marking

Mark image candidates only. Do not create separate image-only sections in planning.

- `REPLACE_CANDIDATE`: short emotional or visual-impact section
- `SUPPORT_CANDIDATE`: factual section that benefits from a support image
- `NONE`: dense editable information
