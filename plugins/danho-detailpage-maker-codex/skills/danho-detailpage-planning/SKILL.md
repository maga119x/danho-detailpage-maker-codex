---
name: danho-detailpage-planning
description: Plan Korean ecommerce product detail pages and draft persuasive Korean 상세페이지 copy. Use when Codex needs to create or revise PLANNING.md, analyze attached reference 상세페이지 design files into reusable design/layout essence, run the planning-to-PM review revision loop, decide page flow, define Korean customer-verbatim strategy, define section roles, draft buyer-first spoken Korean copy, mark image conversion candidates, or prepare DESIGN.md for a Danho detail-page project before copywriter review.
---

# Danho Detailpage Planning

Create a text-first plan that can later become a hybrid HTML/image detail page.

## Required Inputs

Do not write the plan until these factual blockers are clear enough:

- Product name, full product name, short product name, brand name
- Internal price, options, components, usage limits
- Pain points and selling points
- Category
- Existing product images, reference 상세페이지 design files, or desired image direction, if any

Infer non-critical planning context when it is not supplied:

- Likely target customer and main buying anxiety
- Speaker/listener relationship for copy
- Medium, honorific level, and tone temperature
- Daily use scenes and expected objections

Ask concise follow-up questions only when missing information affects factual accuracy, internal price, components, compatibility, legal claims, or user-provided brand constraints.

## Workflow

1. If the user supplied reference 상세페이지 design files, read `references/reference-design-analysis.md`, prepare files under `assets/reference-designs/`, create `REFERENCE_DESIGN_ANALYSIS.md`, and extract only transferable design/layout essence before choosing the final design direction.
2. Choose a design preset and create `DESIGN.md`. If `REFERENCE_DESIGN_ANALYSIS.md` exists, adapt the preset with its design tokens, section rhythm, and component rules without copying the reference page.
3. If the user supplied a plan, prompt, memo, or draft copy, run source brief normalization before writing any visible copy.
4. Choose the planning mode: `Draft Planning` for rough product concepts, `Final Planning` when facts are fixed for design/coding.
5. Build a conversion desire architecture as internal strategy only.
6. Convert the strategy into Korean customer-verbatim strategy: buyer thoughts, seller explanations, and good/bad tone pairs written as actual Korean speech.
7. Build a Wadiz-style empathy conversion map before writing sections: vivid problem, existing friction, origin/why, solution, benefit modules, proof, and final product/result impression.
8. Build a persuasion flow before writing sections.
9. Build a 3-second mobile scan plan: what the buyer can understand from the first 1-2 lines of each section.
10. Build the opening story bridge before the mobile screen-flow plan: screen 01 states the promise/result, screen 02 continues the same buyer moment and shows why that promise matters. Mark this gate `OPENING_STORY_BRIDGE_REQUIRED`.
11. Build a mobile screen-flow plan before the section table. Read `references/screen-flow-planning.md`.
12. Apply `DESIGNED_FULL_IMAGE_REQUIRED`: every newly produced detail page must reserve generated designed full-image sections for at least screen 01 hero and the final product/result closing screen. Mark both as `REPLACE_CANDIDATE`; these are mandatory production images, not optional nice-to-have images.
13. Split major content points into multiple screen-sized sections. One benefit, mechanism, proof set, option system, or review block may require 3-6 sections.
14. Run the `SPARSE_SECTION_IMAGE_REQUIRED` gate: if a section has only a kicker/headline/short lead, one note, or 1-2 small cards, mark it for merge, `REPLACE_CANDIDATE`, or `SUPPORT_CANDIDATE` with a large product/lifestyle/proof visual. Do not leave it as `NONE`.
15. Add a copy context block to `PLANNING.md`: speaker, listener, relationship, medium, honorific, tone persona, and inferred assumptions.
16. Write `PLANNING.md` with all visible copy in text form, and keep production notes separate from buyer-facing copy.
17. Include a review/testimonial section in the plan. Use supplied reviews when available; otherwise create replacement-ready mock review cards with generic nicknames, star ratings, highlighted quotes, and detailed benefit-based review copy. Mark them only in internal notes as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`. Review-section headlines should invite the buyer to check reviews, not claim real-review status unless real reviews were supplied.
18. Run the spoken Korean gate on visible copy before copywriter review: no strategy-term leak, no English skeleton, no abstract noun subject, no long breath.
19. Run the native Korean pre-gate before copywriter review: remove obvious DaleSeo-style AI markers such as translationese, noun-heavy Korean, repeated S2 patterns, and page-wide identical endings.
20. Run the production-readiness gate: no sales channel names, no visible placeholder warnings, no `NEEDS_PROOF`/candidate labels/source filenames in buyer-facing copy.
21. Mark each section as `REPLACE_CANDIDATE`, `SUPPORT_CANDIDATE`, or `NONE`.
22. Run `danho-detailpage-pm-reviewer` in planning-loop mode before copywriter review. Revise `PLANNING.md` and repeat PM review until section order, screen roles, buyer-question continuity, proof/review placement, visual mass, density, and conversion path pass.
23. Record the PM planning loop in `PLANNING.md` with final status `pass`.
24. Run `danho-detailpage-copywriter` to create `COPY_REVIEW.md`, score every section, and patch awkward, timid, translated, feature-first, or AI-marker-heavy visible copy until it passes.
25. Create `config.json`.

## Reference Design Routine

When the user supplies a reference 상세페이지 design file:

1. Store it under `assets/reference-designs/`, not `assets/inbox/`.
2. For long PNG/JPG/WebP captures, optionally run this helper when Python is available:

```powershell
python <planning-skill-dir>/scripts/prepare_reference_designs.py --project <project-dir> <reference-files...>
```

   If Python is unavailable, copy the reference files into `assets/reference-designs/` manually and inspect the original file directly; do not block `REFERENCE_DESIGN_ANALYSIS.md`.
3. Inspect the original and useful slices visually.
4. Create `REFERENCE_DESIGN_ANALYSIS.md` using `references/reference-design-analysis.md`.
5. Apply only transferable design essence to `DESIGN.md` and the mobile screen-flow plan.

Do not copy the reference page's brand, logo, exact Korean text, prices, product images, model photos, badges, exact section order, exact pixel layout, or proprietary composition. If the reference's flow conflicts with the new product's buyer journey, follow the new product's buyer journey.

## PM Planning Loop Gate

Before copywriter review, run this loop:

`draft PLANNING.md -> PM planning review -> revise PLANNING.md -> PM re-review -> pass`

The PM planning loop must fail and revise when:

- the first 3 screens do not establish product identity, core buyer benefit, and the main fit/purchase condition
- the first 2 screens do not form a story bridge: screen 02 must zoom into the same buyer moment, repeated friction, or immediate next question created by screen 01
- two adjacent sections can be swapped without changing meaning
- a section contains three or more independent buyer questions, proof points, or use cases
- proof, review, options, FAQ, safety/care, or final product closing is missing or placed too late for the product risk
- every screen uses the same visual mass or `headline -> paragraph -> card/image` skeleton
- supplied reference design files are copied too literally, ignored entirely, or used without `REFERENCE_DESIGN_ANALYSIS.md`
- screen 01 hero or the final product/result closing screen is not marked as mandatory `REPLACE_CANDIDATE` for a generated designed full-section image
- the final product/result closing screen contains purchase-action text, option/order prompts, benefit-check prompts, or button-equivalent wording
- a low-content option, care/storage, value, reassurance, result, or transition section is planned as centered text-only, one note box, or 1-2 small cards without a real image role
- headline rhythm risk is already visible before copywriter review
- image candidates do not match section roles, such as dense specs marked as full-image candidates or emotional scenes left with no visual plan

On each loop, patch the plan rather than only writing comments. Revise section order, split/merge screens, rewrite scan answers and connection reasons, adjust visual roles, and move proof/review/final-closing modules where needed. Only proceed to copywriter when `PLANNING.md` contains a PM planning loop row with `status: pass`.

## Persuasion Flow

Prefer a connected decision journey:

`hook → real-life moment → buying anxiety → product answer → fit check → install/use confidence → damage/removal confidence → daily use → compatibility/detail → comparison → proof/review → options → FAQ → final product closing`

Rules:

- Do not list features in parallel without transition.
- Treat screen 01 and screen 02 as one opening pair, not two independent slides. Screen 01 should stop the scroll with product identity and a result promise; screen 02 should continue the same scene with a concrete everyday moment, repeated inconvenience, buyer feeling, or the first question that makes the solution necessary.
- Do not let screen 02 be a generic problem/spec section that could follow any hero. It must reuse at least one anchor from screen 01: the same buyer situation, object, action, place, visual motif, or emotional phrase.
- The opening pair often needs more volume than a headline plus one sentence. Give screen 02 a concrete scene, 2-3 narrative beats, and meaningful visual direction unless it is merged into a full designed image.
- Treat supplied product plans as strategy briefs. Preserve facts and intent, but rewrite all draft copy before it becomes visible copy. See `references/source-brief-normalization.md`.
- Do not copy source slogans, section titles, or memo sentences into headlines, body copy, badges, or CTA unless the user explicitly marks that exact phrase as approved final copy and it still passes naturalness review.
- For empathy-heavy or Wadiz-style pages, read `references/wadiz-empathy-conversion-flow.md` and plan the buyer's emotional agreement before the product explanation.
- For pages that feel natural but weak, read `references/conversion-desire-architecture.md` and define the buyer's desired after-state before writing sections.
- Before visible copy, read `../danho-detailpage-copywriter/references/korean-first-expression-gate.md` and convert internal strategy into buyer/seller speech. Strategy terms must stay internal.
- Start from a vivid buyer problem and existing workaround friction before explaining product features, unless the product is a commodity where immediate specs are more important.
- Frame the problem as a mismatch with the current tool, habit, setup, product gap, or missing information. Do not make the buyer feel incompetent.
- Make hero, problem, core solution, key benefit, value, and final product closing carry a clear before/after shift.
- Split major benefits into modules: buyer scene -> pain/emotion -> product mechanism -> buyer gain -> proof/limit -> visual cue.
- Convert every key feature into `before friction -> product mechanism -> after-state`. A clean feature list without a change in the buyer's life is not enough.
- Express the strategy in Korean buyer verbatims before drafting copy. Example: write `좋은 칼 하나 있으면 요리할 맛이 달라지겠다`, not `self-image 강화`.
- Put the strongest purchase condition early when it can block buying.
- Put product identity, core benefit, and the main purchase condition within the first 3 sections.
- Do not treat one source bullet or one content point as exactly one section. Split dense ideas into mobile screen units: scene/result, question, mechanism/detail, proof, caveat/action.
- Do not treat short copy as permission to make a short empty section. If an option, care, value, reassurance, or transition section has little text, plan a product/lifestyle/proof image that gives the section enough visual length, or merge it with a neighboring section.
- A normal ecommerce page should usually have 14-22 screen-sized sections. Technical, high-consideration, reward-heavy, or option-heavy pages may need 20-40. Do not shorten the page by compressing multiple purchase judgments into one section.
- Assign each section a screen role, visual mass, surface role, tempo, proof type, editable risk, and layout pattern before coding.
- Combine similar daily-use moments instead of scattering them.
- Include each section's persuasion role or connection reason in the section table.
- Include visual roles for sections, not generic image placeholders.
- Plan mandatory designed full-image sections as part of the conversion flow, not as decoration. At minimum, screen 01 must become a generated full-image hero and the last selling screen must become a generated full-image product/result closing impression. If legal, option, price, or compatibility facts must remain editable, split those facts into an adjacent HTML section and still keep a separate full-image closing screen with no purchase-action text.
- Plan at least one demonstration-oriented visual for the core problem and one for the core solution when the category allows it. Product flatlays alone are not enough for high-friction products.
- Build value confidence without defensive price apology. Use value stack, avoided extra purchase, reduced hassle, included components/services, or common-alternative contrast. Do not expose direct numeric prices in visible copy.
- Do not mention the sales channel in visible copy. The buyer is already on the selling page; channel names and channel-specific notes belong in internal facts only.

See `references/persuasion-framework.md`, `references/genre-composition.md`, and `references/section-library.md`.
For the current Danho flow standard, read `references/detail-flow-rules.md`.

## Copy Rules

- Use the product naming 3-level rule. See `references/product-naming-consistency.md`.
- Follow Korean headline rules. See `references/korean-headline-rules.md`.
- Design for mobile skimming. In the first 1-2 visible lines of each section, answer at least one of: what this is, what situation it solves, what benefit the buyer gets, or what the buyer should check/do next.
- For `Draft Planning`, allow fuller text to discover story, objections, benefit logic, and proof gaps. For `Final Planning`, compress into strong visible copy and visual directions before coding.
- If source planning text exists, include a source normalization table and quarantine awkward source phrases before writing display copy.
- Avoid internal labels in final-facing copy. Planning labels may exist in tables, but visible copy must sound like selling copy.
- Write section copy that can stand alone in HTML before image generation.
- Do not create separate image-only sections in `PLANNING.md`; only mark candidates.
- Treat planning structure as a draft until the PM planning loop passes. Treat planning copy as a draft until `danho-detailpage-copywriter` reviews it.
- Treat planning copy as unfinished when skill-improvement strict mode is active. It is not approved for coding until copywriter review proves the lowest section average is at least 9.2 for both fixed validation products.
- Convert product merits into consumer benefits: buyer situation -> worry -> benefit -> proof.
- Define the target desire before drafting copy. The buyer should not only understand the product; they should recognize the improved version of their routine, role, or self-image.
- Do not put internal strategy terms into visible copy. Terms such as `장비감`, `전환`, `before/after`, `메커니즘`, `가치 프레임`, `동선`, `흐름을 줄이다`, `선택을 줄이다`, `구매 저항`, and `가격 방어` are planning language.
- Draft visible copy from the buyer's point of view. The subject should usually be the buyer's situation, action, worry, home/body/routine, or desired outcome, not the seller/brand/product.
- Visible copy must pass a spoken Korean test: it should sound like a Korean shop owner or brand seller explaining it aloud to a cautious customer.
- Visible copy must pass a native Korean pre-gate before copywriter review. Remove AI-like Korean markers from the DaleSeo-inspired checklist: `~에 있어서`, `가지고 있다`, `~되어진다`, `~에 대해`, `~를 통해`, `~에 기반하여`, `~할 수 있다` overuse, `~적 N` chains, excessive commas, repeated three-part rhythm, and page-wide identical endings.
- Avoid English skeletons in Korean words. Rewrite abstract object-subject sentences into person/action sentences: `첫 구매의 선택을 줄였습니다` -> `처음부터 같이 있으면 따로 찾을 일이 줄어요`.
- Keep visible copy short enough to say aloud. Use 1-2 clauses per sentence and split long modifiers.
- Do not use generic AI-slop phrasing such as "비밀 공개", "단 하나의", "당신의 삶을 바꿉니다", or unsupported "수많은 분들이 선택".
- Use natural Korean ecommerce language for visible copy. Example: `구매 전, 이 부분만 꼭 확인해 주세요!` instead of a report-like instruction.
- Visible copy must not expose production notes, source asset filenames, image-candidate labels, pre-publication instructions, or unchecked internal lists. Put those in visual instructions, planning notes, or proof logs only.
- Avoid spec-sheet wording in visible copy unless the section is a formal spec table. Prefer buyer terms such as `칼`, `관리용품`, `상품 정보`, and `칼날 소재` over `본품`, `관리 구성`, `최종 상품 스펙`, and `강재`.
- Control repetition at the planning stage: do not repeat the same hero/final-closing headline, the same `처음/첫` angle, or the same `관리와 보관` message.
- Choose repeated action terms deliberately and keep them consistent across related sections. Do not call the same action `손질` in one module and `다듬기` in another unless the nuance is intentional.
- Keep parallel problem cards, usage labels, and comparison rows rhythmically consistent. Do not mix short fragments with one long complete sentence in the same set.
- Mid-page informational cues may clarify fit, contents, care, or usage criteria, but they must not look like purchase actions.
- Final product closing sections must not include CTA buttons, button-equivalent text, option/order-area prompts, benefit-check prompts, or action words such as `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `구성 확인`, `장바구니`, or `주문`. End with product/result confidence, use scene, brand tone, or quiet reassurance instead.
- FAQ answers must answer the actual question first. For yes/no questions, start with `네` or `아니요`, then add conditions, limits, or where to confirm.
- Do not write direct numeric prices in visible detail-page copy, generated image text, comparison tables, or final HTML sections. Promotions and channel discounts can change. Do not add final-section price, option, or benefit-check prompts; the shopping mall purchase area already handles them.
- Do not write sales channel names or phrases such as `판매 채널`, `스마트스토어`, `쿠팡`, `자사몰`, `채널별 구성`, or repeated `구매 페이지에서 확인해 주세요` in visible copy. Keep them in `config.json`, internal facts, or proof logs.
- Every page must include a review/testimonial section. If real reviews are not supplied, write replacement-ready mock review cards with generic nicknames, star ratings, highlighted quotes, and 2-4 lines of detailed benefit-based review copy. Mark the section internally as `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`. Do not expose `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `NEEDS_PROOF`, or similar warnings in visible copy.
- Review-section headlines must be check-oriented, not pseudo-testimonial. Prefer `실제 사용자 후기를 확인해 보세요` or `구매 전, 실제 사용 후기를 살펴보세요` when supplied real reviews exist. When reviews are replacement-ready mockups, do not claim `실제 사용자`; use a neutral headline such as `사용 후기를 확인해 보세요`, `사용 후기로 확인할 포인트`, or `구매 전 많이 보는 후기를 모았습니다`.
- Avoid reviewer-persona headlines such as `먼저 써본 사람이 말해요`, `먼저 써본 사람들의 이야기`, or `써본 사람은 이렇게 말합니다`. They sound staged and can imply invented testimony.
- Mock review cards may contain generic nicknames/handles and star visuals because the review section must be design-complete. They must not contain real names, ages, locations, dates, review counts, purchase counts, order numbers, `실제 구매자`, or verified-review badges unless supplied.
- Consolidate safety and liability copy into one calm safety/care section. Avoid repeating defensive phrasing in FAQ and body copy.
- Keep factual caveats in specs, safety/care, compatibility, or FAQ. Do not let selling sections become a chain of hedges such as `확인해 주세요`.
- Provide a copy context so the copywriter does not have to guess relationship, honorific, and medium from scratch.
- Keep specs, internal price facts, components, compatibility, and limits exact even when rewriting copy. Internal price facts may appear in basic info, config, planning notes, or proof logs, but not in visible copy.
- If a section cannot pass a quick scan test, rewrite the headline and first body line before continuing.
- If a section cannot pass micro-polish checks for final-section CTA removal, action-term consistency, parallel rhythm, or direct FAQ answers, rewrite before copywriter review.
- If a section is natural but does not create desire, add a before/after shift, self-identification cue, value-confidence reason, or proof visual before continuing.
- If a visible sentence fails the Kakao/read-aloud/seller tests, rewrite the sentence before continuing.
- If a visible sentence would fail humanizer, grammar, or style-guide checks, rewrite it before copywriter review and still leave it for strict copywriter scoring.
- Mark unsupported proof, certifications, awards, scarcity, or performance claims as `NEEDS_PROOF` in internal logs; do not write them as visible facts. Reviews are mandatory as a section: use supplied reviews or replacement-ready mock review cards with internal replacement flags.
- Fail the planning draft if visible copy still sounds like the source memo rather than a consumer-facing detail page.

## Image Candidate Rules

Use:

- `REPLACE_CANDIDATE` for the mandatory screen 01 hero and final product/result closing screen.
- `REPLACE_CANDIDATE` for short emotional hooks, scene-defining moments, strong typography, and final product impression.
- `REPLACE_CANDIDATE` for low-content result, value, reassurance, or transition sections when the whole screen should become a designed image section.
- `SUPPORT_CANDIDATE` for factual sections that need a product photo or lifestyle visual while keeping HTML text, especially low-copy option, care/storage, value, and fit sections that would otherwise look sparse.
- `NONE` for dense editable facts, current-price guidance, specs, and FAQ unless an image materially improves comprehension. Do not use `NONE` for a low-content section just because there are no more words to write.

Do not plan toward a fixed image count, maximum count, or full-image/HTML ratio. Mark every section that needs a `REPLACE_CANDIDATE` or `SUPPORT_CANDIDATE` visual for story, proof, options, care, review, comparison, sparse-section support, or opening continuity. The final image quantity is allowed to grow as needed.

## References

- `references/output-format.md` for `PLANNING.md` structure
- `references/reference-design-analysis.md` for extracting design/layout essence from supplied reference 상세페이지 design files before `DESIGN.md`
- `references/detail-flow-rules.md` for current section flow and internal-label rules
- `references/screen-flow-planning.md` for mobile screen-flow planning, content expansion, visual mass, tempo, and category presets
- `references/source-brief-normalization.md` for turning supplied plans/prompts into strategy without copying awkward phrases
- `references/wadiz-empathy-conversion-flow.md` for empathy-heavy Wadiz-style persuasion planning
- `references/conversion-desire-architecture.md` for target desire, before/after, value framing, caveat placement, and proof visual planning
- `../danho-detailpage-copywriter/references/korean-first-expression-gate.md` for separating strategy language from visible Korean and running spoken Korean sentence gates
- `../danho-detailpage-copywriter/references/native-korean-humanizer-gate.md` for DaleSeo-inspired AI-marker, grammar, and style consistency checks
- `../danho-detailpage-copywriter/references/channel-review-production-rules.md` for sales-channel visibility, mandatory review sections, and no visible placeholder warnings
- `references/copy-templates.md` for phrasing patterns
- `../danho-detailpage-copywriter/references/mobile-scan-purchase-audit.md` for 3-second mobile scan planning and scoring
- `../danho-detailpage-copywriter/references/consumer-benefit-copy.md` for natural Korean benefit-first copy
- `../danho-detailpage-copywriter/references/korean-pragmatic-style.md` for speaker/listener/tone/honorific inference
- `../danho-detailpage-copywriter/references/korean-commerce-expression-bank.md` for practical Korean ecommerce expression patterns
- `../danho-detailpage-copywriter/references/persuasion-storybrand-check.md` for ethical persuasion and buyer journey checks
- `references/image-guidelines.md` for candidate thinking
- `../danho-detailpage-coding/references/mobile-hybrid-layout.md` for current coding implications
