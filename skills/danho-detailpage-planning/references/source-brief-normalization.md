# Source Brief Normalization

Use this whenever the user supplies an existing product plan, prompt, sales memo, strategy document, or draft copy.

## Core Rule

Treat supplied planning text as a strategy brief, not as final visible copy.

Do not copy source phrases into `display_copy` just because the user provided them. First extract the role of each phrase, then rewrite it in natural Korean for the target buyer and channel.

## Extraction Pass

Before writing sections, split the source into:

| Type | Meaning | How to Use |
|---|---|---|
| fixed fact | price, component, sales channel, size, material, limit | Preserve exactly in internal facts. Price and sales-channel data must not become visible copy. |
| strategy | positioning, target, price defense, emotional trigger | Preserve intent, rewrite language. |
| evidence | real review, certification, test, award, warranty | Use only if supplied and verifiable. |
| draft copy | slogans, section titles, emotional phrases | Quarantine and rewrite. |
| visual direction | image/GIF/layout notes | Convert into visual role or image-plan direction. |
| risk | safety, legal, 구성 불일치, unsupported claim | Move to assumption/proof log. |

## Quarantine Draft Copy

Put source slogans and section titles through a rewrite pass. They must not become visible copy until they pass:

- natural Korean spoken rhythm
- buyer-centered subject
- concrete benefit
- scanability
- no awkward metaphor
- no source-brief smell

Source-brief smell includes:

- abstract labels posing as copy: `장비감`, `가격 합리화`, `세트 완성도`
- stiff assertions: `첫 칼은 중식도면 충분합니다`
- vague emotion: `의외로 칼부터 답답합니다`
- quoted concepts: `"요리 장비"처럼 느껴지지 않았던`
- unnatural contrast: `일반 식도는 익숙합니다`
- direct memo sentences: `칼 하나가 아닙니다`

## Rewrite Method

For every source phrase:

1. Identify the intended persuasion job.
2. Identify the buyer scene.
3. Rewrite without preserving the original syntax.
4. Check whether a Korean shopper would actually say or accept the sentence.
5. If still stiff, reduce it to a factual label or move it into planner notes.

Example:

| Source phrase | Persuasion job | Better visible direction |
|---|---|---|
| 요리 좀 해보고 싶은 남자에게, 첫 칼은 중식도면 충분합니다 | starter identity | 고기 썰고, 파 다지고, 마늘 으깨는 일까지 한 자루로 |
| 의외로 칼부터 답답합니다 | problem recognition | 고기 손질할 때 칼이 밀리면 요리할 맛이 줄어들죠 |
| "요리 장비"처럼 느껴지지 않았던 걸지도 모릅니다 | tool-confidence desire | 손에 맞는 칼 하나면 요리가 한결 편해집니다 |
| 일반 식도는 익숙합니다 | existing workaround | 늘 쓰던 식칼로도 되지만, 많이 썰고 옮길 때는 아쉬움이 남아요 |
| 칼 하나가 아닙니다 | set-value defense | 중식도에 칼갈이와 보관용품까지 함께 챙겼어요 |

## Output Requirements

In `PLANNING.md`, include a source normalization table when source planning text exists:

| source_item | type | keep_as_fact | rewrite_direction | visible_copy_allowed |
|---|---|---|---|---|

If `visible_copy_allowed` is `no`, the exact source phrase must not appear in visible section copy.

## Fail Conditions

Fail the planning step if:

- source draft copy appears unchanged in a headline, CTA, or body line
- the page repeats the user's memo wording instead of rewriting it for buyers
- strategy labels appear as consumer-facing copy
- the copy sounds like a planning document, not an ecommerce detail page
