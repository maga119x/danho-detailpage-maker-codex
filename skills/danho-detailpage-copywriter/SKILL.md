---
name: danho-detailpage-copywriter
description: Review, score, and rewrite Korean ecommerce 상세페이지 copy after planning and before HTML coding. Use when Codex needs to remove AI-slop wording, apply DaleSeo-inspired native Korean humanizer/grammar/style gates, audit Korean sentence-ending naturalness, separate strategy language from visible Korean copy, infer missing buyer/tone context, convert product merits into consumer benefits, apply spoken Korean buyer language, strengthen weak-but-natural copy with conversion force, run a section-by-section mobile scan purchase audit, and check copy with ethical persuasion psychology and StoryBrand-style customer journey principles.
---

# Danho Detailpage Copywriter

Run this after `danho-detailpage-planning` and before `danho-detailpage-coding` Phase A whenever visible Korean copy is being created or revised.

## Inputs

- `PLANNING.md`
- Product facts, internal price, components, limits, claims, and proof
- Target customer, buying anxiety, pain points, and desired after-state
- Optional current HTML or user feedback about awkward copy
- Optional source product plan, prompt, memo, or draft copy that may contain non-final wording

If non-critical copy context is missing, infer it from the product category, internal price, risk, usage scene, and target. Ask only when the missing fact affects legal accuracy, compatibility, internal price, components, or a factual claim.

## Output

Create or update `COPY_REVIEW.md`, score every visible section, then patch the visible copy in `PLANNING.md` when the workflow is continuing to coding.

## Workflow

1. Build a copy context: speaker persona, listener, relationship, medium, honorific level, buyer stage, tone coordinates, and inferred assumptions.
2. Extract all visible copy from `PLANNING.md`: headlines, subcopy, bullets, badges, CTA, FAQ, reviews, and option text.
3. If source planning text exists, compare visible copy against it. Treat copied slogans, memo sentences, and section titles as suspect even if supplied by the user.
4. Separate `strategy_note`, `customer_verbatim_strategy`, and `display_copy`. Internal labels, English marketing concepts, and section-role explanations must not become visible copy.
5. Diagnose AI-slop: translated phrasing, strategy-term leak, English sentence skeleton, abstract object subject, noun-chain Korean, generic hype, feature-first wording, polite-but-powerless copy, timid value framing, defensive price apology, sales-channel leakage, missing review section, staged review headlines, visible placeholder warnings, scattered caveats, decorative-only visual planning, stiff report tone, fake urgency, unsupported proof, honorific mismatch, sentence-ending mismatch, repeated ending rhythm, noun-heavy Korean, incomplete headlines, unnatural collocations, repeated phrases, CTA-action duplication, inconsistent action vocabulary, list rhythm breaks, FAQ non-answers, missing final static CTA cue, spec-sheet/internal terms, production notes in buyer-facing copy, source-brief smell, and source-copy overpreservation.
6. Rewrite in passes:
   - Source normalization pass: preserve facts and strategy, but rewrite source phrases into buyer-facing Korean. Do not keep the source sentence structure unless it is explicitly approved and natural.
   - Korean-first strategy pass: convert strategy notes into customer/seller verbatims before touching display copy. Do not translate strategy terms directly.
   - Opening bridge pass: rewrite the first two sections so section 02 feels like the next beat after section 01, not a sudden generic problem/spec slide.
   - Scan pass: make the first 1-2 visible lines answer what this is, why it matters to the buyer, or what to check/do next.
   - Perspective pass: make the buyer's situation, action, worry, or desired outcome the subject of the copy. Keep the product/brand as guide, tool, or proof.
   - Benefit pass: buyer situation -> worry -> benefit -> proof -> next action.
   - Conversion force pass: add target desire, before/after shift, self-identification, confident value framing, and proof visual direction where the copy is natural but weak.
   - Korean sentence skeleton pass: rewrite object-subject, abstract noun, nominal-ending, and long modifier structures into short spoken Korean.
   - Sentence-ending fit pass: read `references/korean-sentence-ending-gate.md`; classify each visible sentence by function, compare plausible endings, allow `none fits`, and rewrite when the current ending does not fit the context.
   - Korean polish pass: remove incomplete headline endings, wrong `체감/느껴짐` collocations, spec-sheet terms, repeated words, duplicated CTA actions, inconsistent action vocabulary, broken list rhythm, FAQ non-answers, missing final static CTA cue, direct price mentions in visible copy, safety-disclaimer overexposure, and production notes.
   - Native Korean quality pass: read `references/native-korean-humanizer-gate.md`; apply the full DaleSeo-inspired pipeline of AI-marker detection, grammar check, and style consistency. Remove all S1 markers and repeated S2 markers before scoring.
   - Production page pass: remove sales channel names, remove buyer-facing placeholder/warning copy, require a review/testimonial section, and move replacement notes to internal logs only.
   - Spoken Korean gate: run Kakao, read-aloud, seller, strategy leak, and skeleton tests on every visible sentence.
   - Persuasion pass: ethical proof, clear plan, customer-as-hero, concrete after-state.
7. Score each section from 0-10 for identity clarity, benefit concreteness, Korean naturalness, sentence-ending fit, spoken Korean gate, expression polish, native Korean human score, grammar confidence, style consistency, buyer-centered subject, purchase-decision help, scanability, empathy depth, purchase desire, conversion force, and source-independence.
8. Revise any section with an average below 8.0, any core score below 7.0, sentence-ending-fit below 8.0, spoken-Korean-gate below 8.0, expression-polish below 8.0, native-Korean-human-score below 8.0, style-consistency below 8.0, conversion-force below 8.0 in selling sections, source-independence below 8.0, or any failed identity/benefit/purchase-action check. Repeat scoring until all sections pass or record the blocker.
9. In skill-improvement validation, use strict mode: every section average must be at least 9.2, Korean core criteria must be at least 9.2, other criteria must be at least 8.8, S1 AI markers must be 0, repeated S2 AI markers must be 0, and both fixed test products must pass before the improvement is accepted.
10. Produce `COPY_REVIEW.md` with copy context, inference log, benefit map, Korean-first expression audit, native Korean humanizer audit, grammar/style audit, sentence gate log, sentence-ending audit, conversion architecture audit, source phrase audit, expression polish audit, scorecard, revision loop, original, issue, rewrite, benefit, persuasion principle, and final pass reason.
11. Patch `PLANNING.md` so the approved copy is the source for coding. Do not leave rejected draft copy in visible copy fields.

## Autonomous Context Inference

Infer sensible defaults instead of stopping for broad preference questions:

- Speaker: usually `brand/product seller`.
- Listener: category-specific likely buyer, not a vague "consumer".
- Relationship: helpful seller to cautious buyer.
- Medium: Korean ecommerce 상세페이지.
- Default honorific: friendly polite `해요체`; switch to formal `합니다체` for specs, limits, warranty, and FAQ facts.
- Tone: specific, warm, practical, not cute unless the brand/product clearly supports it.
- Tone coordinates: define a seller persona and good/bad examples, not only adjectives.
- Buyer psychology: identify the purchase blocker early, then reduce anxiety with a simple plan and proof.

Record important assumptions in `COPY_REVIEW.md`. If an assumption is risky, write copy that is safe without pretending certainty.

## Native Korean Quality Pass

Use `references/native-korean-humanizer-gate.md` as the full operating reference whenever copy feels even slightly AI-written, translated, overly formal, or mechanically polished.

This pass adapts all three DaleSeo Korean skills:

- `humanizer`: detect S1/S2/S3 AI-writing markers, then rewrite while preserving meaning.
- `grammar-checker`: verify spelling, spacing, particles, endings, and punctuation after rewriting.
- `style-guide`: verify paragraph-level tone, terminology, list rhythm, CTA labels, number/unit style, and section consistency.

For ecommerce visible copy, hard-fail these source-inspired markers:

- S1-like markers: `~에 있어서`, `가지고 있다`, `~되어진다`, abstract subject + generic verb, English idiom literal translation, AI conclusion formulas, unsupported hype, and visible strategy terms.
- Repeated S2-like markers: `~에 대해`, `~를 통해`, `~와 관련하여`, `~에 기반하여`, `~할 수 있다`, `~을 위해`, `~것이다`, `~라는 점에서`, excessive commas, repeated `해당/본`, `~적 N` chains, same-length sentence rhythm, repeated three-item structure, and page-wide identical endings.
- Grammar markers: `되요`, `됬어요`, wrong particles, malformed endings, excessive exclamation marks, and visible punctuation copied from English templates.
- Style markers: random `해요/합니다` mixing inside one paragraph, drifting action terms, mismatched card/list endings, duplicated CTA actions, inconsistent quote/emphasis use, and visible production labels.

The goal is not generic polished Korean. The final copy should sound like a Korean ecommerce seller speaking naturally to a cautious buyer, with enough human rhythm that it does not read like an LLM output.

## Copy Standards

- The customer is the hero. The product is the guide or tool that helps the customer avoid a problem and get a better daily outcome.
- The grammatical or semantic subject should usually be the buyer, the buyer's home/body/routine/problem, or the outcome they want. Avoid seller-centered subjects such as `저희는`, `브랜드는`, `제품은` unless the line is factual proof.
- Do not write from the seller's achievement perspective: `개발했습니다`, `담았습니다`, `제공합니다`, `설계했습니다`, `선택했습니다`. Rewrite to buyer experience: `쓸 수 있어요`, `줄일 수 있어요`, `확인해 주세요`, `편해져요`.
- Write benefits the buyer can feel in a real situation, not abstract product merits.
- Strategy terms are allowed only in planning notes. Visible copy must not expose terms such as `장비감`, `전환`, `before/after`, `메커니즘`, `가치 프레임`, `동선`, `흐름을 줄이다`, `선택을 줄이다`, `구매 저항`, or `가격 방어`.
- Turn every abstract strategy into Korean speech before writing visible copy. Example: `value stack` -> `칼만이 아니라 같이 필요한 것까지 들어 있어요`.
- Make the buyer's before/after transformation explicit in the sections that sell: hero, problem, core solution, benefit, value, and final CTA.
- Make the first two sections carry a connected story. The hero names the promise/result; the second section should continue with the buyer's actual moment, repeated friction, emotion, or next question. Do not solve this with sentence polish alone.
- Identify the buyer's desired after-state or self-image by category. Do not use shallow demographic stereotypes as desire.
- Protect the buyer's self-esteem: frame the problem as current setup, tool, process, product gap, or missing information, not buyer incompetence.
- Build value confidence before sending the buyer to the purchase channel. Because direct numeric prices are not allowed, use value stack, avoided extra purchase, reduced hassle, bundled service/component value, or common-alternative contrast.
- Do not send the buyer to a named sales channel from inside the detail page. The buyer is already in the selling context. Channel names and channel-specific notes belong in internal data, not visible copy.
- Prefer natural Korean ecommerce phrasing: `확인해 주세요`, `사용할 수 있어요`, `걱정을 줄였어요`, `간단하게 설치할 수 있어요`.
- Use `~합니다` mainly for specs, policy, warranty, FAQ facts, and legal-safe claims.
- Prefer Korean speech rhythm over literal completeness. Omit obvious subjects when natural.
- Prefer Korean sentence skeletons: people/actions as subjects, verb-centered endings, 1-2 clauses per sentence, and no long abstract noun chains.
- Treat Korean sentence endings as meaning-bearing choices, not just politeness. Before accepting a line, check whether the ending matches the speaker, listener, section role, and sentence function.
- Always allow the possibility that no ending choice is natural. If no ending fits, rewrite the sentence, split it, or make the headline a phrase instead of forcing a grammatical ending.
- Compare plausible ending candidates for fragile lines such as CTA, FAQ, safety, review-check, and headline copy. Do not accept the first ending that merely sounds grammatical.
- Control ending repetition across the page. A page where most headlines or leads end the same way feels machine-written even when every sentence is individually correct.
- Prefer verbs over noun stacks: `설치가 가능합니다` -> `설치할 수 있어요`.
- Avoid English skeletons in Korean words: `넓은 칼날이 도마 위 동선을 줄입니다`, `첫 구매의 선택을 줄였습니다`, `재료 준비의 흐름을 줄여주는 도구`.
- Use spoken rewrites: `썬 재료를 바로 팬으로 옮길 수 있어요`, `처음부터 같이 있으면 따로 찾을 일이 줄어요`.
- Avoid overusing `~에 대한`, `~를 기반으로`, `~의 진행`, `~의 제공`, `사용자의 경험을 향상`.
- Avoid incomplete headline endings such as `~요리부터` unless the phrase naturally completes the thought.
- Avoid wrong collocations such as `도구가 체감됩니다`, `안정감이 체감됩니다`, or `쓰임이 느껴집니다`. The buyer feels a difference, convenience, or stability; the tool itself is not "felt" in that way.
- Avoid spec-sheet and production terms in visible copy: `본품`, `관리 구성`, `최종 상품 스펙`, `강재`, `제공 이미지`, `추가 확인 필요`, and image-candidate labels. Use buyer language or move them to proof logs.
- Control repetition across the full page. If the same phrase appears in multiple sections, change the angle instead of repeating the wording.
- Keep repeated action vocabulary intentional. If one task is called `손질` in the benefit module, do not call the same task `다듬기` in a usage module unless the meaning changes.
- Keep parallel cards and short usage labels rhythmically consistent. A four-card list should not mix three short `~고` fragments with one long complete sentence.
- CTA cues must do different jobs. Avoid adjacent static cues with the same generic ending such as `보기/보기`; use distinct meanings such as `구성 확인`, `옵션 기준`, or `관리 기준`.
- Final CTA sections must include a clear static closing cue or option/order-area cue, not a button label. Do not request, write, or preserve button UI for 상세페이지 copy.
- FAQ answers must answer the exact question first. For yes/no questions, answer `네` or `아니요` before adding conditions or where to confirm.
- Do not put direct prices in visible detail-page copy, generated images, or designed HTML sections. Prices change through promotions; keep numeric prices in internal facts/config only, and use generic option/order-area cues only when needed.
- Do not use the no-direct-price rule as a substitute for value persuasion. Repeating `구매 페이지에서 확인해 주세요` or naming a channel is not a value section; explain included value, saved hassle, or option choice instead.
- Do not write sales channel names or phrases such as `판매 채널`, `스마트스토어`, `쿠팡`, `자사몰`, `채널별 구성`, or repeated `구매 페이지에서 확인해 주세요` in visible copy.
- Every detail page must have a visible review/testimonial section. If real reviews are supplied, rewrite them naturally without adding facts. If none are supplied, create neutral replacement-ready dummy review cards and mark them internally as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- Review-section headlines should sound like a seller inviting the buyer to verify social proof, not like a staged testimonial voice. Use `실제 사용자 후기를 확인해 보세요`, `구매 전, 실제 사용 후기를 살펴보세요`, or similar only when real reviews are supplied. For replacement-ready placeholder cards, remove `실제 사용자` and use neutral check-oriented wording such as `사용 후기를 확인해 보세요` or `사용 후기로 확인할 포인트`.
- Reject headlines like `먼저 써본 사람이 말해요`, `먼저 써본 사람들의 이야기`, `써본 사람은 이렇게 말합니다`, or any line that makes a nonexistent reviewer seem to speak before the actual review cards.
- Dummy review cards must not invent names, ages, locations, dates, star ratings, review counts, purchase counts, or claims such as `실제 구매자`. Keep them generic and benefit-based, and keep replacement warnings out of visible copy.
- Visible copy must not expose `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, `NEEDS_PROOF`, `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`, or similar production warnings.
- Keep safety disclaimers consolidated. Do not repeat defensive phrases that make the product feel dangerous.
- Keep caveats in factual sections. Selling sections should sound confident within verified facts, not hedged at every line.
- Treat visual directions as part of persuasion. For important claims, require a problem scene, before/after, mechanism demo, value-stack, or trust-proof visual instead of only decorative product shots.
- Apply the native Korean humanizer gate before final scoring. Meaning-preserving rewrite is mandatory: fixed facts, component inclusion, compatibility, limits, and proof status must not change while removing AI markers.
- Do not over-correct into stiff standard Korean. The grammar pass fixes clear errors; the style pass keeps ecommerce tone consistent and human, not bureaucratic.
- Use exclamation marks sparingly for hooks and reassurance, not every sentence.
- Never invent specific reviews, numbers, scarcity, certifications, awards, or expert authority. Replacement-ready dummy review cards are allowed only as generic placeholders without fabricated specifics and must be flagged in internal logs.
- Social proof, scarcity, and authority are allowed only when product facts provide real evidence.
- Preserve exact specs, internal price facts, components, dimensions, compatibility, and usage limits. Internal price facts must not become visible copy unless the user explicitly overrides the no-direct-price rule.
- Preserve source strategy, not source wording. A supplied phrase is still rejected if it sounds awkward, memo-like, or unnatural.
- When user feedback identifies awkward lines, add those patterns to the rewrite table and remove similar phrasing across the page, not only the quoted lines.

## Scoring Gate

Use the scoring rubric in `references/mobile-scan-purchase-audit.md`.

Pass only when:

- Overall section average is at least 8.0.
- No individual section average is below 8.0.
- No core criterion score is below 7.0.
- The page-level checks for `what is it`, `what benefit do I get`, and `how do I buy/check fit` are each at least 8.0.
- For empathy-heavy or Wadiz-style pages, problem, solution, benefit, and CTA sections score at least 8.0 for empathy depth and purchase desire.
- Selling sections score at least 8.0 for conversion force: target desire, before/after shift, value confidence, or proof visual direction.
- Source-independence score is at least 8.0 when a source plan or draft copy exists.
- Expression-polish score is at least 8.0 in every visible section.
- Internal labels, seller-centered selling copy, unsupported proof, and awkward Korean are resolved.
- Direct price mentions, repeated safety disclaimers, and production notes are removed from visible copy or moved to planner/proof logs.
- Sales channel names, repeated `구매 페이지` cues, and buyer-facing placeholder warnings are removed from visible copy.
- A review/testimonial section exists. If reviews are placeholders, internal replacement status is recorded and no fabricated specifics are visible.
- CTA-action duplication, action-term inconsistency, broken parallel list rhythm, FAQ non-answers, and missing final static CTA cues are resolved.
- Value sections explain why the offer is worth checking without exposing a direct numeric price.
- Core problem and solution claims have proof-oriented visual directions when the category can be demonstrated.
- Every visible sentence passes the Kakao/read-aloud/seller/strategy-leak/skeleton tests.
- Every visible sentence passes the sentence-ending fit gate: the ending fits context, no natural-ending absence was forced, and adjacent copy does not repeat the same ending pattern mechanically.
- Native Korean humanizer gate passes: S1 AI markers are 0, repeated S2 markers are 0, grammar confidence is pass, style consistency is pass, and meaning preservation is pass.

Use strict mode when improving or validating the planning/copywriter skills:

- Every visible section average is at least 9.2.
- Every section scores at least 9.2 for `korean_naturalness`, `sentence_ending_fit`, `spoken_korean_gate`, `expression_polish`, `native_korean_human_score`, and `style_consistency`.
- Every other section criterion is at least 8.8.
- Page-level identity, benefit, buying/check action, desire, proof/readiness, and native Korean quality are each at least 9.2.
- Opening bridge quality is at least 9.2: section 02 naturally follows section 01 and gives enough scene/emotion/detail for empathy.
- Both fixed test products, `무타공 자석 도어스토퍼` and `남자의 첫 중식도 스타터 세트`, must pass. If either fails, revise the skill or references and rerun the test.

If a score fails, rewrite the visible copy and rescore. Do not mark `status: pass` just because a rewrite was attempted.

## Fail If

- The copy still says what the product is instead of what the buyer gains.
- The first 1-2 visible lines of a section cannot be understood by a skimming mobile shopper.
- The second section could be moved under another hero without losing meaning, or it starts a new topic instead of continuing the opening story.
- A problem section is generic and does not make the buyer feel "this is my situation."
- A benefit section explains a feature but does not increase purchase desire.
- A section is natural and accurate but does not create a reason to want, trust, compare, or act.
- The page repeats functional uses without identifying the buyer's desired after-state.
- The value section feels apologetic, defensive, or only tells the buyer where to check price.
- The main subject is the seller, brand, or product when it should be the buyer's situation or outcome.
- A headline sounds like a report title or internal planning label.
- The copy uses generic hype such as "비밀 공개", "단 하나의", "당신의 삶을 바꿉니다", "수많은 분들이 선택", or "프리미엄 경험".
- The page asks the buyer to trust an unsupported claim.
- The final copy cannot be spoken naturally by a Korean seller to a customer.
- The copy still has DaleSeo-style AI Korean markers: S1 marker, repeated S2 marker, grammar error, style inconsistency, or meaning drift after rewrite.
- Visible copy contains strategy language instead of customer/seller speech.
- A sentence only works as written marketing text and would sound strange in KakaoTalk or spoken explanation.
- A sentence uses an English-style abstract object as the subject when a person/action sentence would be natural.
- A sentence ending changes the force of the sentence in the wrong direction: command instead of suggestion, seller promise instead of buyer action, casual tone in policy/safety, or formal report tone in a warm selling section.
- A sentence is kept only because one ending is grammatically possible, even though no ending feels natural in context.
- A headline is grammatically incomplete or sounds like a clipped planning note.
- Visible copy uses unnatural collocations, especially wrong `체감/느껴짐` subjects.
- Visible copy exposes spec-sheet or production terms where buyer language should be used.
- A direct numeric price appears in visible detail-page copy, generated image text, or final HTML text.
- A sales channel name or channel-specific instruction appears in visible detail-page copy.
- The page has no review/testimonial section.
- A review/testimonial headline uses a staged reviewer voice such as `먼저 써본 사람이 말해요` instead of inviting the buyer to check reviews.
- A placeholder review section claims `실제 사용자`, `실제 구매자`, or any other real-review status that was not supplied.
- A dummy review uses fabricated specifics such as names, ages, dates, stars, review counts, or `실제 구매자`.
- Visible copy exposes placeholder or production warnings such as `실제 리뷰 없음`, `더미 리뷰`, `교체 예정`, `NEEDS_PROOF`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- The same safety disclaimer or key phrase is repeated enough to create anxiety or AI-written texture.
- Caveats or `확인해 주세요` language are scattered through selling sections instead of concentrated in factual sections.
- Core visual directions are mostly decorative product shots when the claim needs a problem, mechanism, before/after, value-stack, or trust-proof visual.
- Adjacent CTA cues have indistinct actions or repeat the same generic verb.
- The same buyer action is named inconsistently across sections without a clear reason.
- Parallel cards, bullets, or short usage labels break rhythm in a way that feels AI-written.
- A FAQ answer dodges the question instead of answering directly first.
- The final CTA section lacks a clear non-button closing or option-area cue.
- Production notes such as supplied image filenames, candidate labels, or pre-publication instructions appear as buyer-facing copy.
- Visible copy copies source brief phrases that were not explicitly approved final copy.
- Visible copy contains source-brief smell such as quoted concepts, memo-like assertions, or strategy labels dressed as headlines.
- `COPY_REVIEW.md` lacks a section scorecard, revision loop, or final pass reason for newly planned pages.
- A skill-improvement test reports pass while any section is below 9.2, any Korean core score is below 9.2, or either fixed test product is missing.

## References

- `references/mobile-scan-purchase-audit.md`
- `references/consumer-benefit-copy.md`
- `references/korean-copy-polish-rules.md`
- `references/korean-commerce-expression-bank.md`
- `references/channel-review-production-rules.md`
- `references/korean-pragmatic-style.md`
- `references/korean-first-expression-gate.md`
- `references/korean-sentence-ending-gate.md`
- `references/native-korean-humanizer-gate.md`
- `references/persuasion-storybrand-check.md`
- `references/copy-review-format.md`
- `../danho-detailpage-planning/references/conversion-desire-architecture.md`
