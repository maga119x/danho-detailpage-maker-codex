# PLANNING.md Output Format

Use this format for current Danho projects.

## Template

```markdown
# {제품명} 상세페이지 기획서

## 1. 기본 정보

| 항목 | 내용 |
|---|---|
| 제품명 |  |
| 제품 호칭 풀네임 |  |
| 제품 호칭 단축형 |  |
| 브랜드 단독 표기 |  |
| 내부 가격 정보 |  |
| 카테고리 |  |
| 타겟 |  |
| 핵심 페인포인트 |  |
| 핵심 셀링포인트 |  |
| 핵심 메시지 |  |
| 톤앤매너 |  |
| 디자인 프리셋 |  |
| 기획 모드 | Draft Planning / Final Planning |

## 1-1. 카피 문맥

| 항목 | 내용 | 출처 |
|---|---|---|
| 화자 | 브랜드 담당자/판매자 | supplied/inferred |
| 청자 |  | supplied/inferred |
| 관계 | 구매 전 망설이는 고객에게 친절히 안내 | supplied/inferred |
| 매체 | 모바일 이커머스 상세페이지 | inferred |
| 말높임 | 친근한 존댓말, 정책/스펙은 안내형 | supplied/inferred |
| 톤 온도 | 실용적이고 구체적, 과장 없이 따뜻함 | supplied/inferred |

## 1-2. 추론 메모

| 추론한 항목 | 이유 | 리스크 | 카피 안전장치 |
|---|---|---|---|
|  |  |  |  |

## 1-2-1. 소스 브리프 정규화

Use this when the user supplied an existing plan, prompt, memo, or draft copy.

| source_item | type | keep_as_fact | rewrite_direction | visible_copy_allowed |
|---|---|---|---|---|
|  | fixed fact / strategy / evidence / draft copy / visual direction / risk | yes/no |  | yes/no |

## 1-2-1A. 레퍼런스 디자인 에센스

Use this when the user supplied reference 상세페이지 design files. The full analysis belongs in `REFERENCE_DESIGN_ANALYSIS.md`.

| 항목 | 적용 방향 | 복제 금지 |
|---|---|---|
| 섹션 리듬 |  | 브랜드/문구/정확한 섹션 복제 금지 |
| 시각 무게 |  | 제품 이미지/모델 사진 복제 금지 |
| 타이포 대비 |  | 폰트/카피 그대로 복제 금지 |
| 컴포넌트/카드 |  | 고유 카드 구성 그대로 복제 금지 |
| 이미지 크롭 |  | 정확한 배경/구도 복제 금지 |

## 1-2-2. 고객 마음 정리

| 항목 | 내용 | visible copy 반영 위치 |
|---|---|---|
| 핵심 구매자 상황 |  |  |
| 구매 전 불편 |  |  |
| 구매 후 기대 |  |  |
| 구매자가 하고 싶은 말 |  |  |
| 기존 방식/대안의 한계 |  |  |
| 제품이 도와주는 방식 |  |  |
| 가격을 직접 쓰지 않고 설명할 가치 |  |  |
| 핵심 증거/비주얼로 보여줄 장면 |  |  |

## 1-2-3. 고객 입말 전략

Write strategy as actual Korean buyer thoughts or seller speech before drafting display copy. Do not use abstract English marketing concepts here.

| 전략 역할 | 고객/판매자 입말 | visible copy 방향 |
|---|---|---|
| 고객 속마음 |  |  |
| 문제 인식 |  |  |
| 구매 명분 |  |  |
| 가치 납득 |  |  |
| 마지막 인상 |  |  |

## 1-2-4. 톤 좌표

| 항목 | 내용 |
|---|---|
| 말하는 사람 | 예: 주방용품을 오래 판 사장님이 첫 구매자에게 설명하듯 |
| 듣는 사람 | 예: 처음 사는 고객, 가격과 관리가 걱정되는 고객 |
| 말투 기준 | 예: 짧게, 말하듯, 과장 없이 |
| 좋은 예 |  |
| 피할 예 |  |

## 1-3. 3초 스캔 설계

| 확인 항목 | 상세페이지 안에서 답하는 위치 | 소비자가 바로 이해해야 할 답 |
|---|---|---|
| 이것이 무엇인가 | 1-3번 섹션 안 |  |
| 나에게 어떤 베네핏이 있는가 | 1-3번 섹션 안 |  |
| 구매 전 무엇을 확인해야 하는가 | 1-3번 섹션 안 |  |
| 구매 전 막히는 조건은 무엇인가 | 초반 조건/옵션/FAQ 전후 |  |

## 1-3-1. 오프닝 스토리 브릿지

The first two screens must feel like one connected opening story, not a hero followed by a sudden new slide.

| 항목 | 01번 화면 | 02번 화면 |
|---|---|---|
| 화면 역할 | 약속/결과/상품 정체성 | 같은 장면의 불편/반복/질문 |
| 공유 앵커 |  |  |
| 이어지는 감정 |  |  |
| 다음 구매 질문 |  |  |
| 필요한 분량/비주얼 |  |  |
| 게이트 | pass / OPENING_STORY_BRIDGE_REQUIRED | pass / revise |

## 1-4. 공감 설득 맵

| 설득 단계 | 소비자가 느껴야 할 생각 | 사용할 내용 | 증거/주의 |
|---|---|---|---|
| 생생한 문제 | "이거 내 얘기다" |  |  |
| 기존 방식의 한계 | "그래서 지금까지 불편했구나" |  |  |
| 탄생/진정성 | "이 문제를 알고 만든 제품이구나" |  | NEEDS_PROOF if unsupported |
| 핵심 해결 | "이렇게 바뀌는구나" |  |  |
| 신뢰/안심 | "믿고 사도 되겠다" |  | real proof only |
| 마지막 인상 | "이 제품을 쓰는 장면이 선명해졌다" |  |  |

## 1-5. 핵심 베네핏 모듈

| 모듈 | 고객 장면 | 불편/감정 | 제품이 도와주는 방식 | 고객이 얻는 변화 | 증거/제한 | 비주얼 역할 |
|---|---|---|---|---|---|---|
| benefit-1 |  |  |  |  |  | problem scene / solution demo |
| benefit-2 |  |  |  |  |  | solution demo / detail proof |
| benefit-3 |  |  |  |  |  | final aspiration |

## 1-6. 비주얼 증거 설계

| 보여줄 내용 | 필요한 비주얼 증거 | 적용 섹션 | 자료 상태 | 없을 때 처리 |
|---|---|---|---|---|
| before 문제 |  |  | available / NEEDS_ASSET | safe wording / text only |
| 핵심 메커니즘 |  |  | available / NEEDS_ASSET | safe wording / text only |
| after 변화 |  |  | available / NEEDS_ASSET | safe wording / text only |
| 가치 구성 |  |  | available / NEEDS_ASSET | safe wording / text only |

## 1-7. 리뷰 섹션 준비

Every detail page must include a review/testimonial section. If real reviews are missing, create replacement-ready mock review cards and flag them only here. Use a check-oriented headline: `실제 사용자 후기를 확인해 보세요` for supplied real reviews, or `사용 후기를 확인해 보세요` / `구매 전 많이 보는 후기를 모았습니다` for replacement-ready mock cards. Do not use staged reviewer-voice headlines such as `먼저 써본 사람이 말해요`.

| review_item | source_status | visible_copy_type | nickname_or_handle | rating_visual | highlighted_quote | detailed_review_copy | internal_replacement_note |
|---|---|---|---|---|---|---|---|
| review-1 | supplied / mock | real_review / replacement_ready_mock |  | ★★★★★ |  | 2-4 lines | REVIEW_PLACEHOLDER_REPLACE_REQUIRED if mock |
| review-2 | supplied / mock | real_review / replacement_ready_mock |  | ★★★★★ |  | 2-4 lines | REVIEW_PLACEHOLDER_REPLACE_REQUIRED if mock |
| review-3 | supplied / mock | real_review / replacement_ready_mock |  | ★★★★★ |  | 2-4 lines | REVIEW_PLACEHOLDER_REPLACE_REQUIRED if mock |

## 1-8. 모바일 화면 흐름 설계

Plan screen-sized sections before writing the final section table. One content point may become several screens when it contains scene, claim, mechanism, proof, caveat, option, or action.

Every new page must include mandatory designed full-image candidates:

- `01 hook`: mandatory `REPLACE_CANDIDATE` for generated full-image hero
- final product/result closing section: mandatory `REPLACE_CANDIDATE` for generated full-image closing image with no purchase-action text

| screen | section id | screen_role | visual_mass | surface_role | tempo | main claim / scan answer | evidence or visual | layout_pattern | sparse_image_gate | editable_risk |
|---:|---|---|---|---|---|---|---|---|---|---|
| 01 | hook | impact | image-dominant | dark-proof | low |  |  | comparison-hook / result-first-hero | pass | low |
| 02 | vivid-moment | result/question | image-dominant | paper | low | 01번 약속이 필요한 생활 장면 | 01번과 이어지는 사용/불편 장면 | story-bridge / vivid-problem | pass / OPENING_STORY_BRIDGE_REQUIRED | low |
| 03 | why | question | type-dominant | paper | low |  |  | question-transition | SPARSE_SECTION_IMAGE_REQUIRED / pass | low |
| 04 | proof | proof | proof-dominant | paper | medium |  |  | proof-board / measurement-proof | pass | medium |

## 2. 섹션 구성표

| # | 섹션 id | 목적 | 스캔 답변 | 설득 역할 | 이전 섹션과 연결 이유 | screen_role | visual_mass | tempo | proof_type | 비주얼 역할 | sparse_image_gate | 이미지 변환 후보 |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | hook | 첫인상 | 어떤 상황/베네핏인지 즉시 이해 | 감각 | 시작 | impact | image-dominant | low | photo/comparison | final aspiration | pass | REPLACE_CANDIDATE |
| 02 | vivid-problem | 실제 장면 | 어떤 불편을 줄이는지 이해 | 공감 | hook의 약속을 생활 상황으로 구체화 | result | image-dominant | low | photo | problem scene | pass | SUPPORT_CANDIDATE |
| 99 | final-closing | 마무리 | 제품을 쓰는 마지막 장면이 남음 | 인상 | 옵션/FAQ 이후 제품 결과를 조용히 정리 | final closing | image-dominant | low | none | product/result closing image, no CTA text | pass | REPLACE_CANDIDATE |

## 3. 단계 분할

| 단계 | 비중 | 적용 섹션 | 설계 의도 |
|---|---:|---|---|
| 문제 인식 | 20% | hook, scene-problem, blocker | 고객 불편을 생활 장면으로 묶음 |

## 4. 섹션별 콘텐츠

### 01. hook

**헤드라인**  
...

**본문**  
...

**핵심 속성**
- ...

**내부 이미지 후보(비노출)**: REPLACE_CANDIDATE

### 02. fit-check

**헤드라인**  
...

**체크 포인트**
- ...

**내부 이미지 후보(비노출)**: SUPPORT_CANDIDATE

## 5. 이미지 변환 후보 요약

| 후보 | 개수 | 의미 |
|---|---:|---|
| REPLACE_CANDIDATE | at least 2 | 통 이미지 후보; mandatory hero + final closing 포함 |
| SUPPORT_CANDIDATE |  | HTML+이미지 혼합 후보 |
| NONE |  | HTML 중심 후보 |

## 6. 기획 메모

- 주요 구매 불안:
- 초반에 해결해야 할 조건:
- 통 이미지로 강하게 보여줄 장면:
- HTML로 정확히 유지할 정보:
- visible copy에서 제외할 제작 메모:
- visible copy에서 제외할 판매채널/운영 메모:

## 7. 증거/자료 필요 로그

| claim_or_section | 필요한 자료 | 없을 때 처리 |
|---|---|---|
|  |  | NEEDS_PROOF / safe wording / remove |

## 8. 노출 카피 문장 검수 로그

| visible_sentence | issue | rewrite | status |
|---|---|---|---|
|  | strategy leak / English skeleton / abstract subject / noun ending / too long / tone mismatch |  | pass/revise |

## 9. PM 기획 검토 루프

Run this after the first complete `PLANNING.md` draft and before copywriter review. The PM reviewer fills or updates this section while patching the plan.

| round | PM finding | planning revision applied | affected sections | status |
|---:|---|---|---|---|
| 1 |  |  |  | revise/pass |

### PM 최종 통과 사유

- 첫 3개 화면이 상품 정체성, 핵심 베네핏, 주요 구매 조건을 답한다:
- 01-02번 화면이 약속 -> 생활 장면/불편/질문으로 자연스럽게 이어진다:
- 섹션 순서가 구매 질문 흐름으로 이어진다:
- 한 화면에 여러 구매 판단이 압축되지 않았다:
- 증거/리뷰/옵션/FAQ/마감 위치가 자연스럽다:
- 비주얼 무게 중심과 이미지 후보가 섹션 역할에 맞다:
- 헤드라인 리듬 위험이 구조 단계에서 줄었다:
```

## Rules

- Do not create separate image-only planning sections.
- Do not create image count tables in planning.
- Mark only image conversion candidates; final image roles are decided in `image-plan.md`.
- Include connection reasons so the page does not become a feature list.
- Include the 3-second scan plan and section-level scan answers so the page can be skimmed on mobile.
- Include the opening story bridge table. Section 02 must continue section 01 with the same buyer moment, object/action anchor, emotion, or visual motif. If section 02 feels abrupt, mark `OPENING_STORY_BRIDGE_REQUIRED` and revise before writing the final section table.
- Include the empathy conversion map before the section table when the page needs strong persuasion or Wadiz-style storytelling.
- Include the customer-mind summary so buyer situation, pre-purchase discomfort, post-purchase expectation, buyer speech, value explanation, and proof visuals are explicit.
- Include customer-verbatim strategy so abstract strategy is converted into actual Korean buyer thoughts or seller speech before display copy.
- Include tone coordinates with persona and good/bad sentence pairs. Do not rely only on abstract adjectives such as `단정한`, `실용적인`, or `자신감 있는`.
- Include at least 3 benefit modules for products with enough features or use cases.
- Include a visual proof plan for the core problem, core mechanism, after-state, and value frame when the category can be demonstrated visually.
- Include review section preparation. Reviews are mandatory; if real reviews are unavailable, use replacement-ready mock review cards with generic nicknames, star visuals, highlighted quotes, and detailed benefit-based copy. Record replacement status only in internal notes.
- Include mobile screen-flow planning before the section table. Use `screen_role`, `visual_mass`, `surface_role`, `tempo`, `proof_type`, `editable_risk`, and `layout_pattern`.
- Include `sparse_image_gate` in the mobile screen-flow and section table. Use `SPARSE_SECTION_IMAGE_REQUIRED` when a section has only a short headline/lead, one note, or 1-2 small cards; then assign `REPLACE_CANDIDATE`, `SUPPORT_CANDIDATE`, or `merge_required`, not `NONE`.
- Do not compress one major content point into one dense section. Split core benefits, technical claims, option systems, reviews, and FAQ/policy into multiple screen-sized sections when needed.
- Plan enough sections for the product complexity: normal products usually need 14-22 screens; technical or high-consideration products often need 20-32; reward/option-heavy pages may need 24-40.
- A longer page is acceptable when each screen has one purchase judgment. Reject short plans that force several claims into one viewport.
- Include each section's visual role. Do not use vague placeholders such as "nice product image"; state the persuasive job of the visual.
- For low-content option, care/storage, value, reassurance, result, or transition sections, use images to create real vertical substance. Do not rely on blank padding, empty dark bands, or decorative backgrounds to make the section taller.
- In the first 3 sections, answer product identity, core buyer benefit, and the main purchase condition or next check.
- In the first 2 sections, create a story bridge. Do not jump from a hero promise into a generic problem/spec section without a concrete transition.
- Include copy context and assumption notes so the copywriter can revise without asking broad preference questions.
- If the user supplied a plan or draft copy, include the source brief normalization table before section writing.
- Exact source phrases marked `visible_copy_allowed: no` must not appear in visible copy.
- Visible copy must be buyer-centered. Use seller/brand/product as the subject only for factual proof, specs, compatibility, or limits.
- Visible copy must create a before/after shift. If a section only explains a feature and does not show the buyer's improved state, revise it.
- Visible copy must not expose strategy terms such as `장비감`, `전환`, `before/after`, `메커니즘`, `가치 프레임`, `동선`, `흐름을 줄이다`, `선택을 줄이다`, `구매 저항`, or `가격 방어`.
- Visible copy must use Korean sentence skeletons: person/action subject, verb-centered endings, 1-2 clauses per sentence, and no long abstract noun chains.
- Include a sentence review log for visible copy that failed the Kakao/read-aloud/seller tests and was rewritten.
- Include the PM planning review loop after the first complete draft. Copywriter review must not start until the loop records final `pass`.
- Keep internal labels in tables only. Visible copy must be consumer-facing.
- Keep production notes separate from visible copy. Source filenames, image-candidate labels, `제공 이미지`, `추가 확인 필요`, and pre-publication instructions belong in visual instructions, planning notes, or proof logs only.
- Avoid spec-sheet terms in visible copy unless they are inside a formal spec table. Prefer `칼`, `관리용품`, `상품 정보`, and `칼날 소재` over `본품`, `관리 구성`, `최종 상품 스펙`, and `강재`.
- Control repeated phrases across the page. Hero and final closing must not use the same headline, and repeated `처음/첫`, `관리와 보관`, or `확인해 주세요` wording should be varied by section role.
- Keep repeated action vocabulary consistent across related sections. Decide whether the page uses `손질`, `다듬기`, `썰기`, `준비`, or another term for each repeated action and do not drift between them.
- Keep parallel problem cards, usage labels, and comparison rows in the same rhythm and approximate length.
- Mid-page informational cues may clarify fit, contents, care, or usage criteria, but they must not look like purchase actions.
- The final product/result closing section must not include CTA buttons, button labels, option/order-area prompts, benefit-check prompts, or button-equivalent text such as `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `구성 확인`, `장바구니`, or `주문`.
- FAQ answers must answer directly before giving confirmation instructions. A yes/no question should begin with `네` or `아니요` unless the fact is truly unknown.
- Use consumer-facing spec labels such as `상세 사양` or `상품 상세 정보`, not vague labels such as `확인할 정보`.
- Do not put direct numeric prices in visible copy, image text, comparison tables, or final HTML sections. Keep price as internal data only because promotions and channel discounts can change.
- Do not mention sales channels in visible copy. Avoid `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, `채널별 구성`, and repeated `구매 페이지에서 확인해 주세요`; the buyer is already on the selling page.
- Do not add final-section mutable-price, promotion, option, or order prompts. The shopping mall purchase UI already handles price, option, benefit, cart, and order actions.
- Price-safe value sections must still build value confidence through included value, avoided extra purchases, reduced hassle, or common-alternative comparison. Do not use the no-direct-price rule as a reason to leave value vague.
- Include a visible review/testimonial section even when no reviews are supplied. For missing reviews, create replacement-ready mock reviews with generic nicknames/handles, star visuals, highlighted quotes, and 2-4 lines of detailed benefit-based copy.
- Mock reviews must not claim unsupported specifics: no real names, ages, locations, dates, review counts, purchase counts, order numbers, `실제 구매자`, verified-buyer badges, or sourced proof unless supplied.
- Keep review replacement markers internal only. Visible copy must not say `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, `NEEDS_PROOF`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- Keep safety disclaimers in one calm safety/care section. FAQ should reassure with practical use guidance, not repeat defensive legal language.
- Concentrate caveats in specs, safety/care, compatibility, or FAQ. Do not scatter uncertainty through the selling sections.
- Use product naming consistently.
- Keep internal price facts, options, compatibility, limits, and FAQ explicit and editable. Do not expose numeric prices in visible detail-page copy.
- Mark unsupported proof as `NEEDS_PROOF` internally instead of inventing certifications, awards, expert authority, scarcity, or performance data. Reviews remain mandatory as a section; use supplied reviews or replacement-ready mock review cards with internal replacement flags.
