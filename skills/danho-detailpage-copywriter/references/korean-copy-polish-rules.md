# Korean Copy Polish Rules

Use this after benefit, scan, source-independence, and persuasion passes. This pass catches Korean that is understandable but still unnatural for a real ecommerce detail page.

## Core Principle

Meaning is not enough. Visible copy must sound like a Korean product page, not a translated planning note.

Reject copy that is technically understandable but has:

- incomplete headline endings
- unnatural collocations
- repeated AI-like words
- spec-sheet or internal production terms
- strategy terms leaking into display copy
- English sentence skeletons in Korean words
- sentence endings that are grammatical but contextually wrong
- repeated sentence-ending rhythm that makes the page feel AI-written
- inconsistent table endings
- duplicated purchase-action cues
- inconsistent action vocabulary
- list/card rhythm breaks
- FAQ answers that do not answer the question directly
- direct price mentions or safety-disclaimer repetition
- sales channel names or repeated `구매 페이지` cues
- missing review/testimonial section or visible review-placeholder warnings
- production notes mixed into buyer-facing copy

## Common Failure Patterns

| Failure | Why it fails | Better direction |
|---|---|---|
| `~요리부터` | Headline feels unfinished. | End with a completed action or benefit: `~일까지 한 자루로`, `~부터 시작하세요`. |
| `도구가 체감됩니다`, `안정감이 체감됩니다`, `쓰임이 느껴집니다` | Wrong subject for `체감/느껴짐`; translationese. | `차이가 바로 느껴집니다`, `확실히 다릅니다`, `한결 편해집니다`. |
| `묵직한 실루엣` | `실루엣` describes shape, not handling weight. | `묵직한 무게감`, `손에 잡히는 무게감`. |
| `리듬 있게 손질` | Decorative and unnatural for practical cooking copy. | `쭉쭉 썰기`, `빠르게 썰기`, `한 번에 썰기`. |
| `도마 앞이 달라집니다` | Slightly translated and abstract. | `요리가 한결 편해집니다`, `도마 앞에서의 작업이 수월해집니다`. |
| `시작 구성이 완성됨` | Stiff nominal ending and unclear meaning. | `처음에 필요한 게 다 있어요`. |
| `관리 기준 확인` | Bureaucratic. | `처음 쓸 때 알아둘 관리법`. |
| `절단 가능 여부` | Manual/legal phrasing. | `자를 수 있는지는 제품 설명서를 확인해 주세요`. |
| `첫 구매의 선택을 줄였습니다` | Translated strategy sentence with abstract object subject. | `처음부터 같이 있으면 따로 찾을 일이 줄어요`. |
| `도마 위 동선을 줄입니다` | English-style object subject and abstract noun. | `썬 재료를 바로 팬으로 옮길 수 있어요`. |
| `장비를 쓰는 요리로 전환` | Strategy wording exposed as copy. | `좋은 칼 하나 있으면 요리할 맛이 달라져요`. |

## Terms To Downgrade In Visible Copy

Use simpler buyer language unless the section is a formal spec table.

| Spec/internal term | Buyer-facing term |
|---|---|
| 본품 | 칼, 중식도 |
| 관리 구성 | 관리용품, 관리에 필요한 구성 |
| 보관 구성 | 보관용품, 보호 커버/칼집 |
| 스펙 | 상품 정보 |
| 강재 | 칼날 소재, 재질 |
| 제공 이미지 | remove from visible copy; keep in planner notes |
| 추가 확인 필요 | remove from visible copy; keep in proof log |
| REPLACE_CANDIDATE / SUPPORT_CANDIDATE | internal planning only |
| 장비감 / 전환 / before-after / 메커니즘 / 가치 프레임 | internal planning only; rewrite as buyer speech |
| 동선 / 흐름을 줄이다 / 선택을 줄이다 | rewrite as a concrete action the buyer can do |

## Repetition Gate

Before passing copy, scan repeated wording across the full page:

- Do not repeat the same headline structure in hero and final product/result closing.
- Avoid repeating `처음 사는/처음 쓰는/첫` across adjacent sections. Change the angle: first purchase anxiety, set composition, long-term care, final product/result confidence.
- Avoid repeating `관리와 보관` in multiple headlines. Use one section for set composition and one section for care habits.
- Avoid overusing one verb or noun such as `손질`; rotate naturally with `썰기`, `다듬기`, `준비`, `요리`, `옮기기`.
- Avoid repeated `확인해 주세요`; vary with `챙겨보세요`, `참고해 주세요`, or `살펴보세요` when appropriate. Do not use the final closing for purchase-action prompts.
- If the same action appears in multiple sections, choose one vocabulary family and keep it consistent. Do not call the same cooking task `손질` in one section and `다듬기` in another unless the nuance is intentionally different.
- Do not duplicate a label and its description ending. Rewrite `재료 옮기기: 팬으로 옮기기` as `재료 옮기기: 넓은 칼날에 모아 팬으로 한 번에`.

## Micro-Polish Gate

- Run the sentence-ending fit gate from `korean-sentence-ending-gate.md` before approving copy. Do not treat endings as a final surface decoration.
- For each fragile line, compare plausible endings and include `none fits` as a valid outcome. If no ending fits, rewrite the sentence or convert it to a phrase.
- Check that request endings, FAQ endings, safety endings, informational cue endings, and headline endings use the right degree of force and formality for the section.
- Do not let adjacent headlines/leads all end with the same pattern such as `~합니다`, `~됩니다`, `~좋습니다`, `~확인합니다`, or `~해 주세요`.
- Informational cues must stay factual and non-purchase-oriented. Avoid adjacent cues that both end with the same generic verb such as `보기`, and never use the final closing for option/order, benefit-check, or purchase-action wording.
- Card lists should keep the same rhythm and ending when they are parallel. If three cards end with `~고`, the fourth should not suddenly become a long complete sentence.
- Short usage labels should have similar length and structure. Replace an outlier such as `캠핑 요리 재료 준비` with `캠핑 요리 준비` when neighboring labels are compact.
- Use consumer-facing spec labels such as `상세 사양` or `상품 상세 정보`, not vague labels like `확인할 정보`.
- Final product/result closing sections must not include button copy, option/order prompts, benefit-check prompts, or purchase-action wording such as `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `구성 확인`, `장바구니`, or `주문`. Close with product/result confidence, a use scene, brand tone, or quiet reassurance.

## Price And Safety Gate

- Do not show direct numeric prices in detail-page visible copy, generated images, or designed HTML sections. Promotions and channel discounts change often, and embedded prices make maintenance harder.
- Keep price facts in internal inputs, config, planning notes, or proof logs only.
- Use price-safe wording only when needed, and keep it in editable factual/options sections, never in the final closing. Avoid repeated purchase-area prompts.
- Do not name sales channels or write `판매 채널`, `스마트스토어`, `쿠팡`, `자사몰`, `채널별 구성`, or repeated `구매 페이지에서 확인해 주세요` in visible copy.
- Put safety disclaimers in one consolidated safety/care section. Repeating defensive phrases such as `단정하지 않습니다` in FAQ and body copy increases anxiety.
- Keep safety copy calm and practical: `낯설다면 천천히 사용해 주세요`, `뼈나 냉동식품을 자를 수 있는지는 제품 설명서를 확인해 주세요`.

## Review Section Gate

- A review/testimonial section must exist in the final page.
- If real reviews are supplied, keep their meaning and rewrite only for clarity.
- If no real reviews are supplied, use neutral replacement-ready dummy review cards and flag them only in internal logs as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- Review-section headlines must invite review checking, not imitate a testimonial voice. Prefer `실제 사용자 후기를 확인해 보세요` when real reviews exist; use `사용 후기를 확인해 보세요` or `사용 후기로 확인할 포인트` for replacement-ready cards.
- Reject `먼저 써본 사람이 말해요`, `먼저 써본 사람들의 이야기`, and similar staged reviewer headlines.
- Dummy reviews must not include names, ages, dates, locations, stars, review counts, purchase counts, or `실제 구매자`.
- Visible copy must not expose `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, `NEEDS_PROOF`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.

## Table And FAQ Polish

- Keep comparison table endings consistent: all conversational (`~예요`, `~해요`) or all concise noun phrases, not mixed.
- FAQ answers should answer the buyer, not expose production instructions. Move statements like `상세페이지 공개 전 확인` to proof logs.
- FAQ answers to yes/no questions must answer yes/no first, then add conditions or where to confirm. Do not answer `포함되나요?` with only `확인해 주세요`.
- Use consumer vocabulary: `식칼` is more natural than `식도` in buyer-facing copy unless the product/category specifically requires a technical term.

## Pass Requirement

Visible copy passes only when:

- no incomplete headline remains
- no unnatural `체감/느껴짐` collocation remains
- no spec-sheet/internal term appears outside formal specs
- no strategy term appears in visible copy
- no English sentence skeleton remains
- no contextually wrong sentence ending remains
- no sentence was forced to keep an ending when no natural ending fits
- no production note appears in buyer-facing copy
- no direct numeric price appears in visible copy
- no sales channel name or repeated `구매 페이지` cue appears in visible copy
- a review/testimonial section exists, with placeholder status kept internal when real reviews are missing
- safety disclaimers are controlled
- final product/result closing contains no CTA button, button-equivalent text, option/order prompt, benefit-check prompt, or purchase-action wording
- repeated action terms are intentionally consistent
- parallel card/list copy keeps the same rhythm
- FAQ answers respond directly before adding explanation
- the copy can be read aloud naturally by a Korean seller
