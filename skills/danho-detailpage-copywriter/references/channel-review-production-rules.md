# Channel And Review Production Rules

Use this when planning, reviewing, or coding a Korean ecommerce detail page.

## Sales Channel Visibility

The buyer is already reading the detail page inside a sales channel. Do not waste visible copy on naming that channel.

- Do not write visible copy such as `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, or `채널별 구성`.
- Do not write repeated prompts such as `구매 페이지에서 확인해 주세요`; this sounds like the detail page is somewhere else.
- When a mutable price, option, coupon, shipping benefit, or promotion must be referenced, use generic in-page language:
  - `현재 혜택은 옵션 영역에서 확인해 주세요`
  - `구성은 옵션에서 한 번 더 확인해 주세요`
  - `옵션을 선택하고 혜택을 확인해 주세요`
- Prefer static CTA/option cues over price-location disclaimers:
  - `옵션은 구매 영역에서 확인`
  - `구성은 옵션에서 한 번 더 확인`
  - `내게 맞는 용량부터 선택`
  - `혜택은 옵션 영역 기준`
- Do not turn these cues into buttons, link buttons, or button-like rounded rectangles in 상세페이지 copy or design.

Keep sales-channel names, internal price, promotion assumptions, and channel-specific notes in `config.json`, planning notes, or proof logs only.

## Mandatory Review Section

Every real detail page should include a review section. Reviews are part of the expected buying rhythm and must not be omitted just because source reviews were not supplied.

Review section rules:

- Include a visible review/testimonial section in `PLANNING.md` and final HTML.
- If real reviews are supplied, rewrite them naturally without changing the meaning.
- If real reviews are not supplied, create replacement-ready dummy review cards and mark them internally as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- Review-section headlines should invite checking the reviews. Use `실제 사용자 후기를 확인해 보세요` or `구매 전, 실제 사용 후기를 살펴보세요` only when supplied real reviews exist.
- For replacement-ready dummy review cards, do not claim real-review status. Use neutral headlines such as `사용 후기를 확인해 보세요` or `사용 후기로 확인할 포인트`.
- Avoid staged reviewer-voice headlines such as `먼저 써본 사람이 말해요`, `먼저 써본 사람들의 이야기`, or `써본 사람은 이렇게 말합니다`.
- Do not expose placeholder warnings in visible copy. Avoid buyer-facing text such as `실제 리뷰 없음`, `더미 리뷰`, `교체 예정`, `NEEDS_PROOF`, or `업로드 전 교체`.
- Do not use fabricated specifics in dummy reviews: no names, ages, locations, dates, star ratings, review counts, purchase counts, awards, or claims such as `실제 구매자`.
- Dummy review cards should stay neutral and benefit-based, so they can be replaced cleanly later:
  - `처음 써도 어렵지 않다는 점이 좋았어요.`
  - `같이 들어 있는 구성이라 따로 찾을 일이 줄었어요.`
  - `자주 쓰는 상황에서 손이 덜 가서 편했어요.`
- In internal notes, add a replacement log with source status and replacement requirement.

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
