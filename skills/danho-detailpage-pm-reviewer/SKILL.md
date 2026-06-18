---
name: danho-detailpage-pm-reviewer
description: Review and revise Korean ecommerce detail-page flow like a senior 20-year 상세페이지 PM. Use during the planning-to-PM review revision loop before copywriter review, before Phase A HTML coding to review PLANNING.md/COPY_REVIEW.md/DESIGN.md/REFERENCE_DESIGN_ANALYSIS.md section flow, buyer-question continuity, mobile screen roles, headline rhythm risk, visual mass, density, reference-design essence application, and conversion structure, and after HTML exists when the rendered page needs expert-level flow, hierarchy, continuity, and final-delivery critique.
---

# Danho Detailpage PM Reviewer

Use this after the first complete `PLANNING.md` draft and before copywriter review to run the planning-quality loop. Use it again before `danho-detailpage-coding` Phase A after `PLANNING.md`, `COPY_REVIEW.md`, and `DESIGN.md` exist. Use it again after HTML exists when the user says the page feels fragmented, repetitive, AI-like, or not commercially persuasive.

## Role

Act like a senior 상세페이지 PM, not a copy editor.

Review whether the page sells as one connected journey:

`first impression -> buyer friction -> product answer -> mechanism/use proof -> set/value frame -> fit/review/options -> final action`

## Review Modes

### Planning Loop Review

Use after `PLANNING.md` and `DESIGN.md` exist, before `COPY_REVIEW.md`.

1. Read `PLANNING.md` and `DESIGN.md`. If `REFERENCE_DESIGN_ANALYSIS.md` exists, read it too. Do not wait for copywriter review.
2. Extract the planned section sequence, opening story bridge table, mobile screen-flow table, scan answers, connection reasons, headline/lead drafts, proof/review/options/FAQ/CTA placement, visual mass, and image candidates.
3. Build a planning-loop table with:
   - `screen`
   - `planned role`
   - `buyer question answered`
   - `opening story bridge` for screens 01-02
   - `continuity from previous screen`
   - `density / split risk`
   - `planned visual mass`
   - `PM verdict`
4. Patch `PLANNING.md` when the workflow is continuing. Revise order, split or merge sections, rewrite scan answers and connection reasons, adjust visual roles, and move proof/review/CTA modules before copywriter review.
5. Update `## 9. PM 기획 검토 루프` in `PLANNING.md` with each round's finding, applied revision, affected sections, and status.
6. Repeat review and patching until the planning loop records `pass`. Do not hand off to copywriter while PM findings remain `revise`.

### Pre-Coding Flow Review

Use before Phase A after copywriter review.

1. Read `PLANNING.md`, `COPY_REVIEW.md`, and `DESIGN.md`. If `REFERENCE_DESIGN_ANALYSIS.md` exists, read it too.
2. Extract the planned section sequence: section ids, screen roles, buyer questions, headline/lead copy, visual role, proof/value/review/FAQ placement, and image candidates.
3. Build a section-flow table with:
   - `screen`
   - `planned role`
   - `buyer question answered`
   - `opening story bridge` for screens 01-02
   - `continuity from previous screen`
   - `headline rhythm risk`
   - `planned visual mass`
   - `PM verdict`
4. Find page-level failures before HTML coding.
5. Patch `PLANNING.md` and related visible copy only when the workflow is continuing to coding; otherwise write a concise review artifact.
6. Do not hand off to Phase A while section order, density, screen role, or conversion-flow failures remain unresolved.

### Rendered HTML Review

Use after Phase A or Phase B HTML exists.

1. Extract the actual rendered sequence from HTML: comments, section ids, badges/kickers, h1/h2, lead copy, major components.
2. Build the same section-flow table using rendered evidence.
3. Find page-level failures before editing sentences.
4. Patch the HTML so the section sequence feels intentional.
5. Validate section count, image paths, mobile render, and forbidden copy.

## PM Review Workflow

Pick the mode from available artifacts. If `PLANNING.md` and `DESIGN.md` exist but `COPY_REVIEW.md` does not, run planning-loop review. If `COPY_REVIEW.md` exists and no HTML exists, run pre-coding flow review. If HTML exists, run rendered HTML review.

If the user asks only for review, do not edit files. If the user asks to improve, revise, fix, or move to the next workflow, patch the relevant planning or HTML artifact for the active mode.

## Must-Fix PM Failures

Fail and revise when:

- headlines all share the same sentence ending such as `~합니다`, `~됩니다`, `~좋습니다`
- most headlines share the same visual shape such as every h1/h2 being `A<br>B`
- sections read as independent slides rather than a connected persuasion flow
- screen 02 feels abrupt after screen 01, starts a generic problem/spec topic, or does not reuse the hero's buyer moment, object/action anchor, emotion, or visual motif
- badge/kicker text is taxonomy rather than buyer meaning
- a dense section has multiple buyer questions in one viewport
- the plan or image plan lacks mandatory generated full-image sections for the opening hero and final static CTA/closing impression
- a sparse transition, result, option, care/storage, value, reassurance, or final decision section has no image or visual dominance
- a section has only centered text, one note box, or 1-2 small cards with wide empty padding and no meaningful product/lifestyle/proof visual
- sparse sections are stretched with blank height, empty dark/pale bands, or decorative background instead of real image/proof/content
- every section uses the same `badge -> h2 -> paragraph -> image/card` skeleton
- adjacent image sections reuse the same asset crop in a way that makes different claims look templated
- supplied reference design essence is ignored, copied too literally, or applied in a way that breaks the new product's buyer journey
- final planning or HTML copies reference brand/logo/text/price/product imagery/exact layout/proprietary composition
- review sections pretend to be real testimonials when only review-check criteria or placeholder-safe copy exists
- final HTML exposes internal labels, sales channels, price numbers, proof markers, or review replacement notes

## Planning Loop Pass Gate

The planning loop can pass only when:

- the first 3 screens answer product identity, core buyer benefit, and the main fit or purchase condition
- the first 2 screens form a clear opening bridge: hero promise/result -> lived buyer moment, repeated friction, or immediate next question
- each screen carries one dominant purchase judgment
- adjacent sections have a clear question/answer or emotional transition
- proof, review, options, FAQ, safety/care, and final CTA appear where the buyer needs them
- screen 01 hero and the final selling screen are marked for mandatory generated full-image treatment
- visual mass varies by role instead of repeating the same layout skeleton
- any supplied reference design is translated into original Danho design tokens and section rhythm, not cloned
- no low-content section remains text-only, note-only, or tiny-card-only; `SPARSE_SECTION_IMAGE_REQUIRED` sections have image support, full-image treatment, or merge handling
- image candidates match editable risk and section role
- headline rhythm risk is reduced before copywriter review

## Headline Rhythm Rules

Do not make every headline a complete declarative sentence.

Mix these headline types:

| Type | Use for | Example |
|---|---|---|
| fragment | tactile/result screens | `썬 재료는 / 칼날에 모아 팬으로` |
| question | buyer doubt or transition | `왜 첫 칼로 중식도인가` |
| noun phrase | proof/value screens | `칼 하나가 아니라 시작 준비` |
| contrast | before/after | `칼만 볼 때와 / 구성까지 볼 때` |
| directive | final action | `받는 구성부터 확인` |
| declarative | important claim, used sparingly | `첫 칼은 중식도면 충분합니다` |

Use `합니다체` in body copy if requested, but do not force every headline to end in `습니다`.

Also vary the visual line structure:

- Some heads can be one line and wrap naturally.
- Some can use two deliberate lines.
- Important tactile moments may use three short lines.
- Do not manually insert `<br>` into nearly every h1/h2.
- Avoid a page where every section has the same `kicker -> two-line h2 -> lead` scan rhythm.

## Continuity Rewrite Rules

- Treat the first two screens as a special gate. Rewrite screen 02 before any later flow work if it does not feel like the next beat after screen 01.
- Screen 02 should usually zoom in: same buyer, same place, same object, same action, or the first doubt created by the hero promise.
- Do not accept a second section that only says a broad problem in polished Korean. It needs a concrete situation, emotional recognition, or visual continuation.
- The first line of a section should feel like it answers the previous section or creates the next question.
- Use repeated nouns intentionally as anchors, not as AI-like repetition.
- Move from broad to specific: friction -> ingredient -> action -> set -> value -> fit.
- If two adjacent headings could be swapped without changing meaning, the flow is weak. Rewrite at least one.
- If a headline is just a section label made grammatical, replace it with the buyer's conclusion.
- If a lead sentence mixes unlike items in one list, rewrite it around actions or buyer moments instead of planner categories.

## Badge / Kicker Rule

A badge must earn its space.

Use only:

- buyer situation
- proof cue
- micro-benefit
- next action

Remove or rewrite taxonomy labels such as `문제 인식`, `전환점`, `사용 장면`, `제품 디테일`, `FAQ`.

## Output

When creating a review artifact, write concise Markdown:

- Verdict
- Flow Findings
- Headline Rhythm Audit
- Applied Rewrite Table
- Remaining Risks

Do not produce long theory. Patch the HTML when the task asks for improvement.
