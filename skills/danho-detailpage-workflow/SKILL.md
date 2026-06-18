---
name: danho-detailpage-workflow
description: Orchestrate the Danho Korean ecommerce detail-page workflow in Codex. Use when the user asks to initialize a new Danho work directory with AGENT.MD, create, continue, revise, or diagnose a product 상세페이지 project across reference design essence extraction, planning, PM planning-review revision loops, copywriter review, HTML coding, image planning, native image generation, hybrid image/HTML layout, and final validation.
---

# Danho Detailpage Workflow

Run the workflow in order unless the user is explicitly revising an existing artifact.

## Workspace Initialization

Before creating a new product project in a newly opened work directory, ensure the workspace root has `AGENT.MD`.

- If `AGENT.MD` is missing and the user is starting a new Danho workspace, initialize it with the `danho` skill. Use its bundled `scripts/init_workspace.py` only when Python is available; otherwise copy `assets/AGENT.MD.template.md` to `AGENT.MD`.
- Create `AGENT.MD` in the current working directory, not inside the generated `projects/MMDDHHmm_product-name/` folder.
- Do not overwrite an existing `AGENT.MD` unless the user explicitly asks. If it exists, read it and follow it as the local bootstrap rules.
- `AGENT.MD` is a local checklist. The installed `danho-detailpage-workflow` skill remains the source of truth when rules differ.

## Sequence

0. Initialize `AGENT.MD` first when this is a clean Danho work directory.
1. If the user supplied reference 상세페이지 design files, prepare them under `assets/reference-designs/` and create `REFERENCE_DESIGN_ANALYSIS.md` before finalizing `DESIGN.md`. Extract transferable layout/design essence only; do not copy the reference page.
2. Run `danho-detailpage-planning` when product facts, target, pain points, or page structure are missing. This creates the first `PLANNING.md` / `DESIGN.md` draft and uses `REFERENCE_DESIGN_ANALYSIS.md` when present.
3. Run `danho-detailpage-pm-reviewer` in planning-loop mode before copywriter review. Review `PLANNING.md` and `DESIGN.md`, patch the plan, and repeat `planning -> PM review -> planning revision` until the PM planning loop records `pass`.
4. Run `danho-detailpage-copywriter` only after the PM planning loop passes. Create `COPY_REVIEW.md`, score every section, run the native Korean humanizer/grammar/style gates, and patch visible copy into natural Korean buyer-first language until the score gate passes.
5. Run `danho-detailpage-pm-reviewer` again before Phase A when `PLANNING.md`, `COPY_REVIEW.md`, and `DESIGN.md` exist. Confirm the copywriter revision did not break section sequence, buyer-question continuity, headline rhythm, visual mass, or conversion structure.
6. Run `danho-detailpage-coding` Phase A after PM flow issues are resolved. Phase A must create the HTML-based detail-page layout from the PM-reviewed mobile screen-flow plan before final image generation.
7. Create or update `image-plan.md` after visually reviewing the Phase A HTML. The plan must include generated designed `FULL_IMAGE` rows for at least the opening hero and final product/result closing section.
8. Run `danho-imageprompt-helper` when the user wants prompts or generated section images. After prompts and filenames are fixed, generate images through the built-in `image_gen.imagegen` native tool, one independent call per asset.
9. Run `danho-detailpage-coding` Phase B or revision mode when actual images exist and the page needs final HTML.
10. Run `danho-detailpage-pm-reviewer` again before final delivery if the rendered hybrid page has repetitive headline endings, standalone-looking sections, weak transitions, or identical section skeletons.

## Current Production Rules

- A hybrid final page must include generated designed full-section images. Minimum contract: opening hero `FULL_IMAGE` and final product/result closing `FULL_IMAGE`.
- Use additional designed full-section images for high-impact story moments, and HTML+image mixed sections for editable factual content.
- Planning copy is not final until the copywriter review passes. Do not code awkward draft copy just because `PLANNING.md` exists.
- Planning structure is not final until the PM planning loop passes. Do not run copywriter review on a newly planned page while section order, screen roles, buyer-question continuity, proof/review placement, visual mass, or density failures remain unresolved.
- Supplied product plans are strategy briefs, not final copy. Do not code pages that still preserve awkward source slogans or memo sentences as visible copy.
- Copywriter review must include a mobile scan purchase audit. Do not code a newly planned page when section averages are below 8.0, any core score is below 7.0, or page-level identity/benefit/purchase-action checks are below 8.0.
- Copywriter review must include the native Korean humanizer gate. Do not code when S1 AI markers, repeated S2 AI markers, grammar errors, style inconsistency, or meaning drift after rewrite remain in visible copy.
- When the task is skill improvement or validation, ordinary 8.0 copy review is not enough. Do not accept the skill change unless both fixed test products pass strict mode with every section average at least 9.2.
- If source planning text exists, `COPY_REVIEW.md` must include a source phrase audit and every section must score at least 8.0 for source independence.
- `COPY_REVIEW.md` must include expression polish checks for newly planned pages. Do not code when incomplete headlines, wrong `체감/느껴짐` collocations, spec-sheet terms, direct numeric prices, repeated safety phrasing, or production notes remain in visible copy.
- Do not code when the final closing contains purchase-action text, repeated action terms drift across sections, parallel cards/lists break rhythm, or FAQ answers do not answer the question directly.
- Empathy-heavy or Wadiz-style pages must include an empathy conversion map, benefit modules, section visual roles, and proof-gap log in `PLANNING.md`.
- `PLANNING.md` must include conversion desire architecture for newly planned pages: target desire, before/after shift, value frame, and proof visual plan.
- `PLANNING.md` must include Korean customer-verbatim strategy and tone coordinates for newly planned pages. Do not code pages whose visible copy still exposes strategy terms or English marketing skeletons.
- For empathy-heavy or Wadiz-style pages, do not code when problem, solution, benefit, or final closing sections score below 8.0 for empathy depth or purchase desire.
- Do not code when selling sections are natural but lack conversion force: no target desire, no before/after shift, timid value framing, scattered caveats, or only decorative product visuals for claims that need proof.
- Do not code when visible copy contains strategy terms such as `장비감`, `전환`, `메커니즘`, `동선`, `흐름을 줄이다`, `선택을 줄이다`, `구매 저항`, or `가격 방어`.
- Do not code when visible copy fails spoken Korean tests: Kakao, read-aloud, seller, strategy-leak, and sentence-skeleton.
- Do not code when visible copy would fail DaleSeo-style humanizer, grammar-checker, or style-guide checks adapted in `native-korean-humanizer-gate.md`.
- Do not code when visible copy names sales channels (`스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, `채널별 구성`) or repeatedly sends the buyer to `구매 페이지`; the buyer is already on the selling page.
- Do not code when a newly planned page lacks a review/testimonial section. If real reviews are missing, include replacement-ready mock review cards with generic nicknames, star ratings, highlighted quotes, and detailed benefit-based review copy. Keep `REVIEW_PLACEHOLDER_REPLACE_REQUIRED` only in internal logs.
- Do not code when visible copy exposes placeholder warnings such as `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, `NEEDS_PROOF`, or `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`.
- Visible copy must prioritize consumer benefits and daily outcomes over product merits. The product should act as the guide/tool, not the hero.
- Selling copy must be buyer-centered. The subject should usually be the buyer's situation, action, worry, home/body/routine, or desired outcome, not the seller/brand/product.
- Final HTML is not finished just because sentence-level copy is natural. Run a PM-level flow check on the rendered structure: the page must read as one connected persuasion journey, not independent sections with similar endings.
- Run PM-level planning review before copywriter so the page flow is fixed while the plan is still cheap to change. Then run PM-level flow review again before Phase A so copywriter changes do not harden a broken structure into HTML. Do not start Phase A when PM review leaves unresolved order, density, or conversion-flow failures.
- `OPENING_STORY_BRIDGE_REQUIRED`: do not code a page whose second section feels sudden after the hero. The first two screens must read as one opening story: product/result promise -> same buyer moment, repeated friction, or immediate question that makes the answer necessary.
- Screen 02 must share at least one anchor with screen 01: situation, object/action noun, location, visual motif, or emotional phrase. A generic problem/spec section after a hero is not enough.
- Headline rhythm must vary across the full page. Do not let most section heads end with the same declarative grammar such as `~합니다`, `~됩니다`, `~좋습니다`, or the page will feel machine-written even if each sentence is correct.
- Headline shape must vary as well. A page where nearly every h1/h2 is manually split as `A<br>B` still feels templated even after the sentence endings are fixed.
- Adjacent sections must answer or raise the next buyer question. If two neighboring sections can be swapped without changing meaning, revise the headline, lead, or order.
- Do not stop to ask broad tone/persona questions when reasonable ecommerce defaults can be inferred. Ask only for factual blockers.
- When reference 상세페이지 design files are supplied, create `REFERENCE_DESIGN_ANALYSIS.md` and use it as design guidance. Do not clone the reference page, copy its brand/copy/logo/product images, or let it override the new product's buyer journey.
- Use ethical persuasion only: no fake verified reviews, fake scarcity, fake authority, or unsupported numbers. Replacement-ready mock review cards are allowed as review-section scaffolds with generic handles, star visuals, detailed benefit-based copy, and internal replacement logs; they must not claim `실제 구매자`, verified status, counts, dates, or sourced proof.
- Always establish the HTML detail-page layout first. Do not jump from planning directly to image generation.
- `PLANNING.md` must include a mobile screen-flow plan for newly planned pages. Do not code a plan that treats every content point as one dense section.
- In final hybrid HTML, the first visible section must be a generated designed full-image hero. Do not leave the opening screen as a normal HTML text hero.
- In final hybrid HTML, the bottom/final selling section must be a generated designed full-image product/result closing impression. Do not leave the last selling screen as a plain HTML action block. If legal, pricing, option, or compatibility content must remain editable, split that content into an adjacent HTML section and still keep the full-image closing screen without purchase-action text.
- Detail pages are static ecommerce content, not app screens. Do not create `<button>` controls, `.cta-button` components, link buttons, button-like rounded rectangles, or final-section button-equivalent text anywhere in HTML or generated section images. Use product/result typography, dividers, labels, composition, or quiet reassurance instead.
- When a section is marked `FULL_IMAGE`, it is mandatory. Korean typography errors must trigger native regeneration/revision or `FULL_IMAGE_TEXT_QA_BLOCKED`; do not downgrade to `IMAGE_STORY`, `HTML_MIXED`, textless imagery, or HTML overlay without explicit user approval.
- `SPARSE_SECTION_IMAGE_REQUIRED`: do not deliver low-content sections as centered text-only blocks, single note boxes, or tiny 1-2 card grids surrounded by empty padding. If a section has only a kicker/headline/short lead, one note, or 1-2 small cards, either merge it with adjacent proof/detail content or make it image-dominant with `FULL_IMAGE`, `IMAGE_STORY`, or a large `HTML_MIXED` product/lifestyle/proof support image.
- Option, care/storage, value, reassurance, and final decision sections are not exempt from the sparse-section rule. When their copy is short, use product scale photos, lifestyle scenes, component/option visuals, care-use photos, or proof imagery to create real vertical length.
- Do not solve sparse sections by adding blank height, oversized padding, or decorative empty backgrounds. The extra length must come from meaningful image, product, proof, comparison, review, or option content.
- Split dense content into multiple screen-sized sections. Long pages are acceptable when each screen answers one purchase judgment clearly.
- Split any section that carries three or more independent buyer questions, use cases, or proof points before finalizing the HTML.
- Convert low-copy action, result, transition, option overview, care, or value screens into full-image, image-story, or image-supported sections instead of leaving sparse HTML cards.
- Do not code when a normal product is artificially short or when a technical/high-consideration/option-heavy product lacks enough screen depth for result, mechanism, proof, comparison, options, and FAQ.
- Each screen should have one dominant visual mass: image, type, proof, or cards. Avoid repeating the same `headline -> paragraph -> image -> card` skeleton from top to bottom.
- Do not force every section to a fixed 9:16 or 3:4 ratio. Use vertical mobile rhythm with sufficient section height, large images, and natural content flow.
- Mobile detail-page QA means building an 860px-wide source page and judging readability after scaling that source to a 438px phone preview. Do not code the page as a fixed 413px canvas, and do not use direct 393px/438px viewport reflow as the primary QA result.
- Keep the workflow low-dependency. Static HTML/CSS outputs must open directly from the filesystem with relative asset paths; do not require Node/npm, a temporary dev server, Playwright, Python, a bundler, or a local HTTP server for ordinary viewing and manual QA.
- Treat HTML sections as designed sections, not text-only blocks. Add product photos, lifestyle images, badges, quote cards, speech bubbles, or comparison cards when they improve persuasion.
- Reject simple generic web pages. The result must read as an ecommerce product detail page with hero, problem, review/testimonial, proof, comparison, options, FAQ, and a product/result closing module.
- Do not expose direct numeric prices in final detail-page HTML or generated section images. Do not add final-section option/order-area cues because the shopping mall purchase UI already handles the action.
- Final product/result closing must not use utility purchase-area guidance such as `옵션은 구매 영역에서 확인`, `사이즈와 구성은 주문 전 한 번 더 확인`, `옵션 확인`, or `구성 확인`. Keep those mutable checks in editable option/spec/FAQ sections only when genuinely needed.
- Do not expose sales channel names in final detail-page HTML or generated section images.
- Do not expose internal planning labels such as "설치 방식" or "모바일 구매 판단 요약" in the final page. Convert them into consumer-facing selling copy.
- Do not expose production notes such as source image filenames, `제공 이미지`, `추가 확인 필요`, `상세페이지 공개 전`, or candidate labels. Keep these in planning/proof logs only.
- Keep colors role-based and restrained: Key, Main, Sub, and Exception only.
- Image generation must use the built-in Codex `image_gen.imagegen` native tool only as the required GPT Image 2.0 (`gpt-image-2`) path. Do not use API scripts, CLI imagegen fallback, browser-rendered images, HTML/CSS/SVG/canvas drawings, other image models, or placeholder graphics as generated-image substitutes.
- Do not search for API keys, model runners, plugins, or local generation scripts before using `image_gen.imagegen`. If that tool is present, native image generation is available.
- Do not generate images ad hoc. Prepare the full image queue first, then issue one independent native `image_gen.imagegen` call per approved asset.
- Do not generate a page when the image queue lacks the mandatory opening hero and final product/result closing `FULL_IMAGE` assets. Revise `image-plan.md` first.
- Do not cap image quantity or force a fixed full-image/HTML split. Generate as many `FULL_IMAGE` and `HTML_MIXED` support images as the approved image plan needs for story continuity, proof, options, care/storage, comparison, reviews, sparse-section length, and final decision support.

## Outputs

Create projects under `projects/MMDDHHmm_project-name/` with:

- workspace root `AGENT.MD` for new initialized work directories
- optional `REFERENCE_DESIGN_ANALYSIS.md` and `assets/reference-designs/` when reference design files are supplied
- `PLANNING.md`
- `DESIGN.md`
- `config.json`
- `image-plan.md`
- `prompts/`
- `assets/generated/`
- `build/project-name-vN.html`
- `build/sections/`

## Before Delivery

Always validate:

- If reference design files were supplied, `REFERENCE_DESIGN_ANALYSIS.md` exists and final output adapts its essence without cloning.
- Reference design brand, logo, text, product images, prices, exact layout, or proprietary composition do not appear in final HTML or generated images.
- Image paths exist.
- Section count and image roles/counts match the plan, with no arbitrary image-count cap, fixed percentage, or forced full-image/HTML split.
- `image-plan.md` contains mandatory `FULL_IMAGE` rows for the opening hero and final product/result closing section.
- The first final section is a generated full-image hero.
- The bottom/final selling section is a generated full-image product/result closing section, and it contains no CTA button, button-like CTA graphics, option/order prompt, benefit-check prompt, utility option/size guidance, or button-equivalent text.
- No HTML or generated image contains visual buttons, link buttons, button-shaped labels, or final-section purchase-action text.
- No mandatory `FULL_IMAGE` section was accepted as a textless/HTML-overlay fallback due to Korean typography risk.
- The first 3 mobile screens show product identity, core benefit/result, and difference or fit condition.
- The first 2 mobile screens pass the opening story bridge: screen 02 follows screen 01 with a concrete lived moment, not an abrupt new topic.
- Headline endings, section kickers, and lead sentences pass the PM flow check: varied rhythm, no taxonomy labels, and no repeated formal sentence pattern across most heads.
- Headline visual structure passes the PM flow check: no page-wide repetition of the same manual two-line h1/h2 pattern.
- Adjacent sections connect as a purchase journey. They should move from friction to answer to use proof to value to fit/action, not read like separate slides.
- Key benefits, mechanisms, proof blocks, option systems, and FAQ/policy are split into readable screen-sized sections when needed.
- No single card grid carries three or more independent buying ideas that should be separate screens.
- Low-copy action/result/transition/option/care/value sections are image-dominant or merged with a proof/detail section.
- No low-content section remains as centered text-only, tiny card-only, or note-only; `SPARSE_SECTION_IMAGE_REQUIRED` sections use meaningful generated/user imagery or are merged.
- Empty padding, dark backgrounds, or large blank bands are not used as a substitute for product/lifestyle/proof imagery.
- No horizontal overflow in the 860px source or the 438px scaled phone preview.
- Font sizes and spacing are readable after the 860px source is scaled to the 438px phone preview.
- Phase A HTML has a finished detail-page layout before image replacement.
- No JavaScript, animation, transition, or hover-dependent design.
- Section ids/comments are sufficient for section splitting. `scripts/split_sections.py` is an optional Python helper; if Python is unavailable, manually inspect or update section files instead of blocking final delivery.
- `COPY_REVIEW.md` exists for newly planned pages and all visible copy issues marked revise are resolved.
- `COPY_REVIEW.md` includes copy context and Korean naturalness audit for newly planned pages.
- `COPY_REVIEW.md` includes a section scorecard, revision loop, and final pass reason for newly planned pages.
- `COPY_REVIEW.md` includes source phrase audit when the project was created from supplied planning text.
- `COPY_REVIEW.md` includes expression polish audit and every visible section scores at least 8.0 for expression polish.
- `COPY_REVIEW.md` includes conversion architecture audit and selling sections score at least 8.0 for conversion force.
- `COPY_REVIEW.md` includes Korean-first expression audit, sentence gate log, and every visible section scores at least 8.0 for spoken Korean gate.
- `COPY_REVIEW.md` includes native Korean humanizer audit, grammar/style audit, and every visible section passes native Korean quality gates.
- `COPY_REVIEW.md` includes production readiness audit and review replacement log when reviews are placeholders.
- `PLANNING.md` includes a PM planning review loop with final status `pass` before copywriter review for newly planned pages.
- Visible copy does not include direct numeric prices and does not over-repeat the same safety disclaimer, hero phrase, or key noun.
- Visible copy does not include sales channel names, repeated `구매 페이지` cues, visible placeholder warnings, `NEEDS_PROOF`, or review replacement markers.
- A review/testimonial section exists in planning and final HTML.
- Value framing explains why the offer is worth checking without exposing direct numeric prices.
- Core problem and solution claims have proof-oriented visual directions when the category can be demonstrated visually.
- Mid-page informational cues are clear, repeated action terms are consistent, parallel cards/lists keep rhythm, FAQ answers are direct, and the final closing contains no purchase-action text.
- A `SKILL_TEST_REPORT.md` is created when improving or validating the planning/copywriter skills with a test detail page.

## Skill Improvement Validation

When the task is to improve the planning or copywriter skills themselves:

- Use `무타공 자석 도어스토퍼` as the default test product unless the user provides another product.
- Use both fixed validation products unless the user provides a different pair: `무타공 자석 도어스토퍼` and `남자의 첫 중식도 스타터 세트`.
- Create one test project per product with `PLANNING.md`, `COPY_REVIEW.md`, and `SKILL_TEST_REPORT.md`.
- Record a before/after score comparison if there is a previous baseline. If no reliable baseline exists, record the pre-change risk and the post-change score.
- Keep iterating the skill instructions or references until both test pages pass strict mode: every visible section average at least 9.2, Korean core scores at least 9.2, other scores at least 8.8, S1 AI markers 0, repeated S2 markers 0, grammar/style gates pass, and meaning preservation passes.
- Each `SKILL_TEST_REPORT.md` must record DaleSeo-pattern pre-risk, failed sentences, rewrite loop, lowest section average, lowest Korean core score, and final strict pass reason.
- Do not create or update distribution zip files unless the user explicitly asks for a package.
