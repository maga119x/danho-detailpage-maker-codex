# COPY_REVIEW.md Format

```markdown
# COPY_REVIEW.md

## Verdict

- status: pass | revise
- main_issue:
- copy_direction:

## Copy Context

| field | value | source |
|---|---|---|
| speaker |  | supplied | inferred |
| listener |  | supplied | inferred |
| relationship |  | supplied | inferred |
| medium | 모바일 이커머스 상세페이지 | inferred |
| honorific |  | supplied | inferred |
| tone |  | supplied | inferred |

## Assumption Log

| assumption | reason | risk | copy_safety_rule |
|---|---|---|---|

## Benefit Map

| feature_or_fact | buyer_worry | benefit_copy | proof_or_limit |
|---|---|---|---|

## Opening Story Bridge Audit

Use this before section scoring. Section 02 must continue section 01, not merely start a generic problem section.

| check | section 01 | section 02 | fix | status |
|---|---|---|---|---|
| product/result promise is clear |  |  |  | pass/revise |
| shared buyer situation/object/action/emotion exists |  |  |  | pass/revise |
| section 02 explains why section 01 matters |  |  |  | pass/revise |
| section 02 has enough scene/story/image substance |  |  |  | pass/revise |

## Korean-First Expression Audit

| check | found | fix | status |
|---|---|---|---|
| strategy terms leaked into visible copy |  |  | pass/revise |
| English sentence skeleton |  |  | pass/revise |
| abstract object subject |  |  | pass/revise |
| noun-chain or nominal ending |  |  | pass/revise |
| sentence too long to say aloud |  |  | pass/revise |
| abstract tone without persona/good-bad pair |  |  | pass/revise |

## Native Korean Humanizer Audit

Use this after Korean-first rewriting and before final scoring. It adapts `DaleSeo/korean-skills` humanizer rules to ecommerce visible copy.

| source_gate | marker_or_risk | found_examples | fix | status |
|---|---|---|---|---|
| S1 AI marker | `~에 있어서` / `가지고 있다` / `~되어진다` / abstract subject + generic verb / AI conclusion formula / unsupported hype |  |  | pass/revise |
| repeated S2 marker | `~에 대해` / `~를 통해` / `~에 기반하여` / `~할 수 있다` / excessive commas / `~적 N` chain / repeated 3-part rhythm / identical endings |  |  | pass/revise |
| punctuation rhythm | English-style commas, visible colon labels, exclamation overuse |  |  | pass/revise |
| POS and noun density | noun-heavy or nominalized copy that should be buyer action |  |  | pass/revise |
| translationese | English/Japanese-style syntax or direct idiom translation |  |  | pass/revise |
| meaning preservation | facts, polarity, components, compatibility, limits, and proof status preserved |  |  | pass/revise |
| over-rewrite guard | rewrite changed strategy/facts too much or invented proof |  |  | pass/revise |
| naturalness grade | A / B / C / D after rewrite |  |  | pass/revise |

## Grammar And Style Audit

Apply the DaleSeo-inspired order: grammar after humanizer, style after grammar.

| check | found | fix | confidence_or_rule | status |
|---|---|---|---|---|
| spelling |  |  | certain_error / recommendation / style_suggestion | pass/revise |
| spacing |  |  | certain_error / recommendation / style_suggestion | pass/revise |
| particles and endings |  |  | certain_error / recommendation / style_suggestion | pass/revise |
| punctuation |  |  | certain_error / recommendation / style_suggestion | pass/revise |
| paragraph tone consistency |  |  | ecommerce: section-internal consistency, page-level variation allowed | pass/revise |
| terminology consistency |  |  | same buyer action uses same term family | pass/revise |
| list/card/CTA consistency |  |  | parallel rhythm and distinct CTA actions | pass/revise |

## Sentence Gate Log

| visible_sentence | failed_test | rewrite | status |
|---|---|---|---|
|  | Kakao / read_aloud / seller / strategy_leak / skeleton |  | pass/revise |

## Sentence Ending Audit

Use this for Korean sentence endings after the Korean-first expression audit.

| visible_sentence | function | current_ending | candidate_endings | decision | rewrite | status |
|---|---|---|---|---|---|---|
|  | statement / suggestion / warning / FAQ / CTA / review-check |  |  | keep / replace / none_fits |  | pass/revise |

## Conversion Architecture Audit

| check | current_state | fix | status |
|---|---|---|---|
| target desire is specific |  |  | pass/revise |
| before/after shift is clear |  |  | pass/revise |
| buyer self-image is present without stereotyping |  |  | pass/revise |
| problem is framed as current setup/tool/process, not buyer incompetence |  |  | pass/revise |
| value framing is confident without direct numeric price |  |  | pass/revise |
| caveats are concentrated in factual sections |  |  | pass/revise |
| core claims have proof-oriented visual direction |  |  | pass/revise |

## Source Phrase Audit

Use this when the user supplied an existing plan, prompt, memo, or draft copy.

| source_phrase | source_role | visible_copy_risk | rewrite | status |
|---|---|---|---|---|
|  | fact / strategy / draft copy / visual direction | copied / stiff / memo-like / ok |  | removed / rewritten / fact_preserved |

## Expression Polish Audit

| issue_type | found | fix | status |
|---|---|---|---|
| incomplete headline |  |  | pass/revise |
| wrong collocation / `체감` misuse |  |  | pass/revise |
| spec-sheet or internal term |  |  | pass/revise |
| repeated phrase or word |  |  | pass/revise |
| CTA action duplication |  |  | pass/revise |
| action vocabulary inconsistency |  |  | pass/revise |
| parallel list/card rhythm break |  |  | pass/revise |
| FAQ non-answer |  |  | pass/revise |
| missing final static CTA cue |  |  | pass/revise |
| direct price in visible copy |  |  | pass/revise |
| safety-disclaimer overexposure |  |  | pass/revise |
| production note in visible copy |  |  | pass/revise |

## Production Readiness Audit

| issue_type | found | fix | status |
|---|---|---|---|
| sales channel name in visible copy |  |  | pass/revise |
| repeated purchase-page cue |  |  | pass/revise |
| missing review/testimonial section |  |  | pass/revise |
| staged review headline or wrong real-review claim |  |  | pass/revise |
| dummy review with fabricated specifics |  |  | pass/revise |
| placeholder or replacement warning visible to buyer |  |  | pass/revise |

## Review Replacement Log

Use this when no real reviews were supplied. Keep this log internal; do not expose these markers in visible copy.

| review_card | source_status | visible_copy_type | replacement_required | notes |
|---|---|---|---|---|
|  | supplied / placeholder | real_review / replacement_ready_dummy | yes/no |  |

## Section Scorecard

Use 0-10 scores. Mark ordinary copy review `pass` only when each section average is at least 8.0 and no core criterion is below 7.0.

For skill-improvement validation, mark `pass` only when each section average is at least 9.2, Korean core scores (`korean_naturalness`, `sentence_ending_fit`, `spoken_korean_gate`, `expression_polish`, `native_korean_human_score`, `grammar_confidence`, `style_consistency`) are at least 9.2, and all other scores are at least 8.8.

| section | identity_clarity | benefit_concreteness | korean_naturalness | sentence_ending_fit | spoken_korean_gate | expression_polish | native_korean_human_score | grammar_confidence | style_consistency | buyer_centered_subject | purchase_decision_help | scanability | empathy_depth | purchase_desire | conversion_force | source_independence | average | status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | pass/revise |

## Page-Level Purchase Understanding

| question | score | where_answered | fix_if_under_8 |
|---|---:|---|---|
| What is this product? |  |  |  |
| Do the first two sections connect as one opening story? |  |  |  |
| What benefit does the buyer get? |  |  |  |
| What should the buyer check or do to buy? |  |  |  |
| Why would the buyer want it now? |  |  |  |
| What before/after change makes the page persuasive? |  |  |  |
| Why does the value feel worth checking without fixed visible price? |  |  |  |
| What proof or visual demonstration supports the core claim? |  |  |  |
| Does the Korean sound human and native? |  |  |  |

## Revision Loop

| round | section | failing_scores | rewrite_action | new_average | result |
|---:|---|---|---|---:|---|
| 1 |  |  |  |  | pass/revise |

## Rewrite Table

| section | original | issue | rewrite | benefit | principle |
|---|---|---|---|---|---|

## Korean Naturalness Audit

| check | result | fixed_examples |
|---|---|---|
| buyer-centered subject | pass |  |
| honorific consistency | pass |  |
| translationese removed | pass |  |
| noun-heavy phrases rewritten | pass |  |
| spoken rhythm acceptable | pass |  |
| spec-sheet/internal terms removed from visible copy | pass |  |
| repeated phrases controlled | pass |  |
| production notes separated | pass |  |

## Final Checks

- [ ] Visible copy uses buyer benefits, not only product merits.
- [ ] Each section average is at least 8.0.
- [ ] No core criterion score is below 7.0.
- [ ] Every section has expression polish score at least 8.0.
- [ ] Every section has native Korean human score at least 8.0.
- [ ] Every section has grammar confidence pass.
- [ ] Every section has style consistency score at least 8.0.
- [ ] Every section has sentence ending fit score at least 8.0.
- [ ] Every section has spoken Korean gate score at least 8.0.
- [ ] If source planning text exists, every section has source independence score at least 8.0.
- [ ] Source slogans, memo sentences, and section titles are not copied as visible copy unless explicitly approved and natural.
- [ ] Page-level product identity, buyer benefit, and purchase/check action each score at least 8.0.
- [ ] The first two sections pass the opening story bridge audit.
- [ ] Empathy-heavy pages score at least 8.0 for empathy depth and purchase desire in problem, solution, benefit, and CTA sections.
- [ ] Selling sections score at least 8.0 for conversion force.
- [ ] The first 1-2 visible lines of each section can be understood by a skimming mobile shopper.
- [ ] The buyer's situation, action, worry, or desired outcome is the main subject of selling copy.
- [ ] The buyer's desired after-state or self-image is explicit without relying on demographic stereotypes.
- [ ] Hero, problem, core solution, key benefit, value, and final CTA show a clear before/after shift.
- [ ] Value framing is confident and explains why the offer is worth checking without direct numeric prices.
- [ ] Core claims have proof-oriented visual directions or are softened/marked when proof is missing.
- [ ] Seller/brand/product-centered wording is used only for factual proof, specs, or limits.
- [ ] Internal planning labels are not visible.
- [ ] No unsupported proof, scarcity, authority, or review claim.
- [ ] Korean tone is natural for ecommerce detail pages.
- [ ] Speaker, listener, medium, honorific, and tone are explicit or reasonably inferred.
- [ ] Tone is defined by persona and good/bad examples, not abstract adjectives only.
- [ ] Translationese, excessive passive voice, and noun-heavy phrases are removed.
- [ ] Visible copy contains no strategy terms such as `장비감`, `전환`, `before/after`, `메커니즘`, `가치 프레임`, `동선`, `흐름을 줄이다`, `선택을 줄이다`, `구매 저항`, or `가격 방어`.
- [ ] Visible copy passes Kakao, read-aloud, seller, strategy-leak, and sentence-skeleton tests.
- [ ] Visible copy passes the sentence-ending fit gate, including `none_fits` rewrites when no natural ending exists.
- [ ] Native Korean humanizer audit passes: S1 marker count is 0, repeated S2 marker count is 0, naturalness grade is A for final copy, meaning preservation passes, and over-rewrite guard passes.
- [ ] Grammar audit passes after humanizer rewrite, with no certain spelling, spacing, particle, ending, or punctuation error.
- [ ] Style audit passes after grammar check: section-internal tone is consistent, repeated terms are deliberate, lists/cards are parallel, and CTA actions are distinct.
- [ ] Incomplete headlines, wrong `체감/느껴짐` collocations, and spec-sheet terms are removed.
- [ ] CTA cues have distinct actions and the final CTA includes a visible non-button closing/option cue.
- [ ] Repeated buyer actions use consistent terms across sections unless the nuance intentionally changes.
- [ ] Parallel cards, bullets, and short usage labels keep a consistent rhythm.
- [ ] FAQ answers respond directly to the question before adding explanation or confirmation steps.
- [ ] No direct numeric price appears in visible detail-page copy, generated-image text, or final HTML text.
- [ ] Visible copy does not mention sales channel names such as `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, or `채널별 구성`.
- [ ] Current mutable benefits are directed to the option/order area only when needed, without repeated `구매 페이지에서 확인` phrasing.
- [ ] A review/testimonial section exists.
- [ ] If review cards are placeholders, they have no fabricated names, ages, dates, locations, stars, review counts, purchase counts, or `실제 구매자` claims.
- [ ] Placeholder or replacement warnings are internal only; visible copy does not contain `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, `NEEDS_PROOF`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- [ ] Safety disclaimers are consolidated.
- [ ] Caveats, compatibility, and safety limits are concentrated in factual sections unless they are purchase blockers.
- [ ] Production notes, image filenames, candidate labels, and pre-publication instructions are not visible copy.
- [ ] Specs, internal price facts, components, and limits remain exact; numeric prices are not exposed in visible copy.

## Strict Skill-Improvement Checks

Use only when validating changes to the planning/copywriter skills.

- [ ] Test product 1 `무타공 자석 도어스토퍼` exists with `PLANNING.md`, `COPY_REVIEW.md`, and `SKILL_TEST_REPORT.md`.
- [ ] Test product 2 `남자의 첫 중식도 스타터 세트` exists with `PLANNING.md`, `COPY_REVIEW.md`, and `SKILL_TEST_REPORT.md`.
- [ ] Lowest section average across both tests is at least 9.2.
- [ ] Lowest Korean core score across both tests is at least 9.2.
- [ ] Lowest non-core score across both tests is at least 8.8.
- [ ] S1 AI marker count is 0 in both tests.
- [ ] Repeated S2 AI marker count is 0 in both tests.
- [ ] Both tests record DaleSeo-pattern pre-risk, failed sentences, rewrite loop, final strict score, and pass reason.

## Final Pass Reason

Summarize why the copy can move to coding in 2-4 concise bullets. Mention the final average score and any remaining factual assumptions.
```
