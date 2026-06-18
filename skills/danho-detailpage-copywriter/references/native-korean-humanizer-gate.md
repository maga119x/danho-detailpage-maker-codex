# Native Korean Humanizer Gate

Use this after the Korean-first, benefit, sentence-ending, and expression-polish passes. This gate adapts the full `DaleSeo/korean-skills` skill set for Korean ecommerce detail-page copy.

## Source And License

- Source reference: `DaleSeo/korean-skills`
- Skills analyzed: `humanizer`, `grammar-checker`, `style-guide`, including their `SKILL.md`, `references/`, and `examples/`
- License: MIT in the source repository
- Do not vendor the source skill text into Danho skills. Apply the operating rules below to visible detail-page copy.

## Required Pipeline

Run these three checks in order:

1. `humanizer`: detect AI-like Korean writing patterns and rewrite while preserving meaning.
2. `grammar-checker`: catch spelling, spacing, grammar, and punctuation errors after the humanizer rewrite.
3. `style-guide`: check tone, terminology, list rhythm, informational cues, number/unit style, and section-level consistency.

Do not run `style-guide` before `humanizer`. The source style-guide notes that humanizer may add intentional variation across a whole text, while style-guide should keep each paragraph/list/section internally consistent.

## Humanizer Severity Mapping

Treat source `humanizer` severities as ecommerce copy blockers:

| Severity | Detail-page action |
|---|---|
| S1 | Hard fail. Rewrite before scoring. |
| S2 | Revise if repeated in a section, adjacent sections, or a full page. |
| S3 | Track as weak signal; revise when combined with S1/S2 or when it makes copy feel machine-written. |

Strict skill-improvement tests pass only when the final page has:

- S1 marker count: `0`
- Repeated S2 marker count: `0`
- Naturalness grade: `A`
- Meaning preservation: pass
- Over-rewrite risk: pass

## Detail-Page AI Marker Checklist

Use the full source humanizer categories, mapped to ecommerce visible copy:

| Source category | Detail-page fail patterns | Rewrite direction |
|---|---|---|
| Punctuation | Too many commas, English-style comma after `-고/-지만/-어서`, colon labels like `특징:` in visible copy | Remove commas, split sentences, convert labels into buyer-facing lines |
| Spacing rigidity | Robotic spacing in repeated `것/수/만큼`, unnatural unit spacing for ecommerce context | Keep standard Korean readable; avoid both error and machine-stiff repetition |
| POS diversity | Noun-heavy copy, `설치 방식`, `사용성 향상`, `구매 판단`, `경험 제공` | Use verbs and buyer actions: `붙이고 바로 쓸 수 있어요` |
| Vocabulary | `혁신적`, `핵심적`, `효과적`, `다양한`, `프리미엄 경험`, `완벽한` without proof | Replace hype with concrete scene, mechanism, or proof |
| Korean pro-drop | Repeating product/seller as subject: `이 제품은`, `저희는`, `브랜드는` | Omit obvious subjects or make buyer situation/action the subject |
| Structure | Same sentence length, repeated three-item rhythm, excessive `또한/따라서/그리고`, page-wide `합니다` endings | Vary headline shape, sentence length, and section tempo while keeping each block coherent |
| Translationese | `~에 대해`, `~를 통해`, `~에 있어서`, `~와 관련하여`, `~에 기반하여`, `가지고 있다`, `~에 의해`, `~할 수 있다` overuse, `~것이다`, `~라는 점에서` | Rewrite into direct Korean verbs, concrete subjects, and seller speech |

## Ecommerce-Specific Rewrites

| AI-like / translated | Buyer-facing Korean |
|---|---|
| 제품의 사용성을 향상시킵니다 | 손이 부족할 때도 발로 간단히 고정할 수 있어요 |
| 설치 방식에 대해 안내합니다 | 자석이 붙는 문인지 먼저 확인해 주세요 |
| 강력한 기능을 가지고 있습니다 | 필요한 순간에 문을 잡아둘 수 있어요 |
| 관리와 관련된 구성을 제공합니다 | 처음 관리할 때 필요한 것까지 함께 들어 있어요 |
| 이 제품을 통해 편의성을 경험할 수 있습니다 | 붙이고 내리면 바로 편해집니다 |
| 구매 판단에 있어서 중요한 조건입니다 | 구매 전, 이 부분만 먼저 확인해 주세요 |
| 다양한 문제를 효과적으로 해결합니다 | 짐 들고 들어올 때 문이 다시 닫히는 불편을 줄여요 |
| 도마 위 동선을 줄입니다 | 썬 재료를 칼날 위에 모아 바로 팬으로 옮길 수 있어요 |

## Grammar Checker Adaptation

After rewriting for naturalness, check:

- Spelling: `되요 -> 돼요`, `됬어요 -> 됐어요`, `왠만하면 -> 웬만하면`, `어떻게/어떡해`
- Spacing: `할수있다 -> 할 수 있다`, `궁금한점 -> 궁금한 점`, `연락주세요 -> 연락 주세요`
- Particles: `사과을`, `책를`, wrong `이/가`, `은/는`, `와/과`
- Endings: malformed `-습니다`, wrong `-아요/-어요`, awkward request or action-prompt endings
- Punctuation: excessive exclamation marks, unnecessary commas, mixed quotes

Mark grammar issues by confidence:

- `certain_error`: must fix
- `recommendation`: fix unless brand voice intentionally uses it
- `style_suggestion`: fix only if it improves ecommerce readability

## Style Guide Adaptation

For Korean ecommerce detail pages, classify the document type as `marketing/ecommerce`.

Use these style defaults:

- Tone: friendly polite `해요체` for selling copy; `합니다체` for specs, limits, warranty, and factual FAQ.
- Paragraph consistency: do not randomly mix `해요` and `합니다` inside one paragraph/card/list.
- Page rhythm: deliberate variation across sections is good; robotic uniformity is bad.
- Terminology: choose one term for the same buyer action. Do not drift between `손질`, `다듬기`, `썰기`, and `준비` unless the action differs.
- Lists/cards: keep item length, ending, and structure consistent within one card group.
- Informational cues: keep them factual and non-purchase-oriented. Avoid repeated `보기/보기`, and do not use final closing copy for option/order prompts, benefit-check prompts, or purchase-action wording.
- Numbers/prices: do not expose direct numeric prices in visible detail-page copy.
- Emphasis: avoid visible production labels, markdown-ish labels, and excessive punctuation.

## Meaning Preservation And Over-Rewrite Guard

Before final scoring, record:

- Fixed facts preserved: product name, components, compatibility, limits, internal price facts, claim conditions.
- No polarity reversal: possible/impossible, included/not included, safe/unsafe, compatible/incompatible.
- No invented proof: no fake reviews, numbers, awards, scarcity, certifications, or expert authority.
- Rewrite scope: large enough to remove AI markers, but not so large that supplied facts or strategy are lost.

If a rewrite would change more than half of the factual content, stop and convert the risky part into an internal assumption/proof log instead of presenting it as visible copy.

## Strict 9.2 Gate

Use strict mode when improving or validating Danho planning/copywriter skills.

Pass only when both fixed test products meet all of these:

- Lowest visible section average: at least `9.2`
- `native_korean_human_score`: at least `9.2` in every section
- `korean_naturalness`, `sentence_ending_fit`, `spoken_korean_gate`, `expression_polish`, `grammar_confidence`, and `style_consistency`: each at least `9.2` in every section
- Other criteria: at least `8.8` in every section
- Page-level identity, benefit, action, desire, proof/readiness: each at least `9.2`
- S1 AI markers: `0`
- Repeated S2 AI markers: `0`
- Grammar confidence: score gate passed and no certain grammar error remains
- Meaning preservation: `pass`

If any section is under `9.2`, rewrite and rescore. Do not mark the test passed because the page is merely better than the old 8.0 gate.
