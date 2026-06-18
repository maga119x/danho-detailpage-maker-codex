# Channel And Review Production Rules

Use this when planning, reviewing, or coding a Korean ecommerce detail page.

## Sales Channel Visibility

The buyer is already reading the detail page inside a sales channel. Do not waste visible copy on naming that channel.

- Do not write visible copy such as `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, or `채널별 구성`.
- Do not write repeated prompts such as `구매 페이지에서 확인해 주세요`; this sounds like the detail page is somewhere else.
- When a mutable price, option, coupon, shipping benefit, or promotion must be referenced, keep it in editable factual/options sections. Do not put it in the final closing.
- Do not write option/order prompts, benefit-check prompts, or purchase-action wording such as `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `구성 확인`, `장바구니`, or `주문` in the final closing.
- Do not turn informational cues into buttons, link buttons, or button-like rounded rectangles in 상세페이지 copy or design.

Keep sales-channel names, internal price, promotion assumptions, and channel-specific notes in `config.json`, planning notes, or proof logs only.

## Mandatory Review Section

Every real detail page should include a review section. Reviews are part of the expected buying rhythm and must not be omitted just because source reviews were not supplied.

Review section rules:

- Include a visible review/testimonial section in `PLANNING.md` and final HTML.
- If real reviews are supplied, rewrite them naturally without changing the meaning.
- If real reviews are not supplied, create replacement-ready mock review cards and mark them internally as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- The review section must look like a real ecommerce review module, not a proof checklist. Use 3-5 cards or speech bubbles with nickname/handle, star rating, highlighted quote, and 2-4 lines of detailed review copy.
- Review-section headlines should invite checking the reviews. Use `실제 사용자 후기를 확인해 보세요` or `구매 전, 실제 사용 후기를 살펴보세요` only when supplied real reviews exist.
- For replacement-ready mock review cards, do not claim real-review status. Use neutral headlines such as `사용 후기를 확인해 보세요`, `사용 후기로 확인할 포인트`, or `구매 전 많이 보는 후기를 모았습니다`.
- Avoid staged reviewer-voice headlines such as `먼저 써본 사람이 말해요`, `먼저 써본 사람들의 이야기`, or `써본 사람은 이렇게 말합니다`.
- Do not expose placeholder warnings in visible copy. Avoid buyer-facing text such as `실제 리뷰 없음`, `더미 리뷰`, `교체 예정`, `NEEDS_PROOF`, or `업로드 전 교체`.
- Mock review cards may include realistic ecommerce handles and star visuals because the section must be design-complete and easy to replace later. Use generic handles such as `요리입문자`, `문앞정리러`, `살림초보`, or `출근길사용자`, and star text such as `★★★★★` or `별점 5.0`.
- Mock review cards must not claim verification status or hard facts that were not supplied: no real names, ages, locations, exact dates, review counts, purchase counts, order numbers, "actual buyer" badges, `실제 구매자`, awards, certifications, or unsupported performance claims.
- Mock review copy should be detailed but derived from the product's planned benefits and safe assumptions, so it can be replaced cleanly later:
  - `처음 써도 순서가 어렵지 않았어요. 필요한 구성이 같이 있어 따로 찾는 시간이 줄었습니다.`
  - `자주 쓰는 상황에서 손이 덜 가서 편했어요. 설명을 보고 바로 어디에 쓰는지 이해됐습니다.`
  - `구매 전 걱정했던 부분을 후기 카드에서 먼저 확인할 수 있어 선택이 쉬웠어요.`
- In internal notes, add a replacement log with source status and replacement requirement.

Suggested mock card fields:

| field | visible example | rule |
|---|---|---|
| nickname | `요리입문자` | generic handle only; no real person identity |
| rating | `★★★★★` / `별점 5.0` | visual social-proof scaffold; no review count |
| quote | `처음 써도 어렵지 않았어요` | one concise highlight |
| body | 2-4 lines | product-benefit-based, no unsupported facts |

## No Weird Warning Copy

The final visible page must look upload-ready. Internal uncertainty belongs in planning/review logs, not in customer-facing sections.

Move these out of visible copy:

- `추가 확인 필요`
- `실제 리뷰 없음`
- `상세페이지 공개 전 확인`
- `제공 이미지`
- `NEEDS_PROOF`
- `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`
- source filenames
- candidate labels
- channel names
- internal price notes

Visible copy should either be a confident verified claim, a calm factual instruction, or a neutral replacement-ready module.
