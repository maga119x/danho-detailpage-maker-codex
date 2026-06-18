# Wadiz-Style Empathy Conversion Flow

Use this when a detail page needs stronger empathy, story, and purchase desire. This is not a rule to imitate Wadiz wording literally. It is a planning framework for building emotional agreement before product explanation.

## Core Principle

Do not start from `what the product has`. Start from `what the buyer is tired of`, then make the buyer feel:

1. "This is exactly my problem."
2. "Existing options are why I still have this problem."
3. "This product was made for this situation."
4. "I can picture the better moment after buying."
5. "The facts are clear enough to decide now."

Natural copy is not enough. The page must create a reason to want the product, not only explain it.

## Two Planning Modes

### Draft Planning

Use when product facts are rough or the page concept is still forming.

- Write enough text to discover the story, objections, benefits, and section logic.
- Explore multiple headline angles.
- Include detailed problem scenes, customer emotions, existing workaround failures, and feature-to-benefit reasoning.
- Keep factual claims conservative. Mark missing proof as `NEEDS_PROOF`.

### Final Planning

Use when product facts are mostly fixed and the page is ready for design/coding.

- Compress the draft into strong headlines, short copy, and visual directions.
- Preserve only the copy that a mobile shopper should actually see.
- Replace long explanations with image/GIF directions when visuals can explain faster.
- Keep internal price facts, specs, options, restrictions, FAQ, and proof editable as text. Do not expose numeric prices in visible detail-page copy or images.

Default: start with `Draft Planning` when the user provides only rough product information. Convert to `Final Planning` before HTML coding.

## Required Persuasion Spine

Use this spine unless the product category clearly requires a different order:

1. **Hook / Catchphrase**: one sharp promise or problem moment.
2. **Vivid Problem**: concrete buyer situation, emotion, wasted time/money/effort.
3. **Existing Friction**: why current tools, habits, or alternatives still feel inconvenient.
4. **Origin / Why We Made It**: short sincerity bridge, only if credible.
5. **Core Solution**: what the product changes in the buyer's routine.
6. **Benefit Modules**: at least 3 modules, each `buyer problem -> product mechanism -> buyer gain -> proof/limit`.
7. **Detail / Differentiator**: material, design, usability, options, or service that makes the solution believable.
8. **Trust Builder**: mandatory review/testimonial section plus real proof when available: tests, certifications, manufacturing transparency, warranty, or supplied facts.
9. **Specs / Components / Options**: buyable facts.
10. **Use Guide / Care / Safety**: steps, tips, and warnings when relevant.
11. **Recommended For**: concrete buyer types that make the buyer self-identify.
12. **FAQ / Objection Handling**: answer likely blockers directly.
13. **CTA**: summarize the buyer's future moment, fit condition, and next action.

## Conversion Desire Layer

Before writing sections, define:

| Layer | Question |
|---|---|
| target desire | What does the buyer want to feel or become after purchase? |
| before state | What repeated friction makes the buyer open to change? |
| external cause | What tool, habit, setup, missing part, or current alternative causes the friction? |
| after state | What concrete daily moment improves? |
| value confidence | Why does the offer feel worth checking without showing a fixed numeric price? |
| proof visual | What image, comparison, sequence, or demo makes the claim believable? |

Use this layer for any category. Do not convert a sample product's specific desire into a universal rule.

## Benefit Module Rule

Every major feature must be planned as:

`buyer scene -> pain/emotion -> product mechanism -> buyer benefit -> proof or limit -> visual cue`

Example:

| Weak feature section | Strong benefit module |
|---|---|
| 넓은 칼날 | 양배추를 썰고 나면 도마 위에 재료가 흩어지죠. 넓은 칼날로 모아 팬으로 옮기면 준비 동선이 줄어들어요. |
| 스테인리스 소재 | 사용 후 물기를 닦아 말리면 매일 쓰는 주방칼처럼 관리할 수 있어요. 단, 젖은 채 보관하지 마세요. |

## Desire-Building Checks

Before writing final copy, answer:

- What exact moment makes the buyer annoyed enough to care?
- What current workaround does the buyer already try, and why is it still unsatisfying?
- What does the buyer want to feel after purchase: relief, control, confidence, speed, pride, safety?
- What identity or self-image does the buyer want in this category, and is it expressed without stereotyping?
- Where does the page protect the buyer's self-esteem by blaming the current setup or missing tool instead of the buyer's ability?
- Which 3 benefits are strong enough to deserve separate visual sections?
- Which facts must be shown so desire does not feel like hype?
- Does the value section build confidence through value stack, avoided extra purchase, reduced hassle, or common-alternative contrast without exposing direct numeric prices?
- What should the buyer do next: check fit, choose option, compare, or buy?

## Visual Planning Rule

Each section should include a visual role, not just an image placeholder.

Use:

- `problem scene`: buyer frustration or inconvenient moment.
- `solution demo`: product action or before/after behavior.
- `detail proof`: material, size, component, texture, mechanism.
- `trust proof`: review/testimonial section, supplied review, certificate, test, manufacturing proof.
- `buying info`: options, package, option-area benefit cue, size, compatibility.
- `final aspiration`: buyer's improved moment after purchase.

Do not use decorative images that do not carry persuasion.
Do not rely only on product flatlays for high-friction products. Plan demonstration visuals for the core problem and core solution whenever the category allows it.

## Confidence And Caveats

- Selling sections should be confident within supplied facts.
- Concentrate limits, usage cautions, compatibility, and safety caveats in factual sections.
- Repeating `확인해 주세요` across benefit sections makes the page feel uncertain. Keep it for purchase blockers and factual tables.
- Do not defend the price before the buyer asks. Build value first, then direct the buyer to the purchase channel for current price and promotion details.

## Ethical Limits

- Do not invent specific reviews, certifications, expert endorsements, sales numbers, awards, patents, scarcity, discounts, or deadlines.
- If real reviews are missing, create neutral replacement-ready dummy review cards and mark them internally as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`; do not expose that marker in visible copy.
- Do not say "완벽 해결", "삶을 바꿉니다", or "수많은 분들이 선택" without real proof.
- Do not over-amplify fear. Acknowledge the inconvenience, then give a useful path.
- If a claim needs evidence, write `NEEDS_PROOF` or phrase it as a safe use-case.

## Output Requirements

In `PLANNING.md`, include:

- Planning mode: `Draft Planning` or `Final Planning`.
- Conversion desire architecture.
- Empathy conversion map.
- At least 3 benefit modules for products with enough features.
- Visual proof plan for core problem, mechanism, after-state, and value frame.
- Visual role for every section.
- Missing proof log for claims that should not be written as facts yet.
