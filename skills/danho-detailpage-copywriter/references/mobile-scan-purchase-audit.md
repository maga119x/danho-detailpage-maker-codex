# Mobile Scan Purchase Audit

Use this to judge whether Korean ecommerce detail-page copy works for a mobile shopper who is skimming, not reading carefully.

## Research-Informed Principles

- Mobile shoppers scan before they commit. Put the answer in the first 1-2 visible lines.
- The first two sections must feel connected before the rest of the page can persuade. A hero promise followed by an abrupt generic problem section fails even if both sections are individually clear.
- The first 3 sections must answer: what this is, what benefit I get, and what I should understand before using the store purchase area.
- Section copy should support one decision at a time. Do not mix problem, proof, option, and FAQ logic in one headline.
- Product pages need concrete facts, not broad brand claims. Use fit, component, compatibility, limits, review/testimonial, proof, factual option information, and value framing where relevant. Do not expose direct numeric prices, sales-channel names, or final-section purchase-action prompts in visible copy.
- The customer is the hero. The product is the tool or guide that helps the customer act.
- Natural language is not enough. Selling sections must create conversion force through before/after, target desire, value confidence, proof, or a clear next decision point. The store UI handles the actual purchase action.
- Korean-first expression is mandatory. Visible copy must sound like Korean speech, not translated strategy.
- Native Korean quality is mandatory. Apply the DaleSeo-inspired sequence: AI-marker detection, grammar check, then style consistency check. A page can be understandable and still fail if it reads like LLM Korean.

## Page-Level Gate

Before section scoring, check the whole page:

| Question | Pass Standard |
|---|---|
| What is this product? | A buyer can name the product category and use case within the first 3 sections. |
| Do the first two screens connect? | Section 02 continues the promise, situation, object/action, emotion, or visual motif from section 01 and explains why the hero matters. |
| What benefit do I get? | The page states a concrete daily-life improvement, not only a product feature. |
| What should I understand before buying? | Fit, option, component, limits, and value information are easy to find before the final closing. |
| Why should I want it? | The page names the buyer's before-state, desired after-state, and value reason without relying on generic hype. |
| What proves the change? | Core claims have proof facts, visual proof direction, or safe wording when proof is missing. |
| Does the page feel upload-ready? | It includes a review/testimonial section with shopping-mall review-card structure, uses a check-oriented review headline, and does not expose channel names, placeholder warnings, internal labels, or production notes. |
| Does the Korean sound human? | No S1 AI-writing marker remains, repeated S2 markers are gone, grammar is clean, and section-level tone/terminology/list rhythm is consistent. |

Each page-level question must score at least 8/10. If not, rewrite the early flow before polishing sentences.

## Section Scorecard

Score each visible section from 0-10.

| Criterion | 10 | 7 | 4 or lower |
|---|---|---|---|
| identity_clarity | Section makes the product, situation, or decision role immediately clear. | Understandable after reading body copy. | Vague slogan or internal label. |
| benefit_concreteness | Buyer can picture the daily outcome. | Benefit is present but abstract. | Only lists a feature or product merit. |
| korean_naturalness | Sounds like a Korean seller speaking naturally to a customer. | Slightly stiff but acceptable. | Translationese, report tone, awkward honorific. |
| sentence_ending_fit | Endings match sentence function, section role, speaker/listener relationship, and page rhythm. `none fits` cases are rewritten. | Mostly natural but one or two endings feel slightly too formal, casual, or repetitive. | Wrong force/formality, forced ending, repeated ending rhythm, or awkward command/request remains. |
| spoken_korean_gate | Every visible sentence passes Kakao, read-aloud, seller, strategy-leak, and sentence-skeleton tests. | A few sentences are slightly written but still speakable. | Strategy terms, English skeletons, abstract object subjects, noun chains, or long-breath sentences remain. |
| expression_polish | Headlines are complete, collocations are natural, direct prices are absent from visible copy, final closing has no purchase-action text, repeated action terms are consistent, FAQ answers are direct, repeated words are controlled, and buyer-facing terms replace spec/internal terms. | Meaning is clear but one or two phrases are stiff, repetitive, or slightly uneven in rhythm. | Incomplete headlines, direct numeric prices, wrong `체감/느껴짐` subjects, duplicated purchase-action cues, inconsistent action terms, FAQ non-answers, final-section purchase prompt, spec-sheet terms, production notes, or repeated phrases remain. |
| native_korean_human_score | Source-inspired AI markers are absent: no S1, no repeated S2, no translationese, no noun-heavy machine rhythm, and meaning is preserved after rewrite. | Minor S3-style stiffness remains but does not affect seller-like readability. | S1 marker, repeated S2 marker, AI hype, translationese, over-rewrite, or meaning drift remains. |
| grammar_confidence | Spelling, spacing, particles, endings, and punctuation are clean, with only intentional ecommerce style choices left. | One or two low-risk recommendations remain by brand choice. | Certain spelling/spacing/particle/ending/punctuation error remains. |
| style_consistency | Tone is coherent within each section, repeated action terms are deliberate, lists/cards have matching rhythm, and informational cues do not become purchase-action prompts. | Page-level variation is acceptable but one minor list/term inconsistency remains. | Random `해요/합니다` mixing, terminology drift, broken card/list rhythm, duplicated purchase-action verbs, or inconsistent emphasis remains. |
| buyer_centered_subject | Buyer situation, action, worry, or outcome leads the sentence. | Mixed buyer/product perspective. | Seller, brand, or product is the hero. |
| purchase_decision_help | Helps the buyer check fit, reduce anxiety, compare, or choose. | Nice to know but not decisive. | Decorative copy with no decision value. |
| scanability | First 1-2 lines carry the message. | Requires reading most of the section. | Message is buried or scattered. |
| empathy_depth | Buyer feels the page understands a real situation, emotion, or repeated frustration. | Mentions a problem but not vividly. | Generic pain point anyone could say. |
| purchase_desire | Section increases desire, confidence, urgency to decide, or self-identification. | Informative but not motivating. | Fact list with no reason to want it. |
| conversion_force | Section moves a buyer from interest to action through a before/after shift, self-identification, value confidence, proof visual, or next decision. | Section is useful but mostly informative. | Natural wording with no desire, value, proof, or action pressure. |
| source_independence | Supplied plan/memo wording is transformed into buyer-facing Korean without copying source slogans or sentence structure. | Source intent is preserved but a few phrases still feel memo-like. | Source draft copy, strategy labels, or awkward memo sentences appear as visible copy. |

## Pass And Revision Rules

- Pass: section average >= 8.0 and no criterion < 7.0.
- Revise: section average < 8.0, any criterion < 7.0, or the first 1-2 lines fail the scan test.
- Revise: the opening bridge fails. If section 02 feels abrupt, expand it with a concrete buyer scene, repeated friction, emotion, or next question before polishing later sections.
- Hard fail: unsupported proof, fake verified-review claim, fake scarcity, staged review headline, wrong real-review claim, internal planning label, sales-channel name, visible placeholder warning, missing review/testimonial section, mock review section without nickname/star/detail structure, or product/seller-centered selling copy.
- Hard fail: visible strategy terms, English-style sentence skeletons, or copy that cannot be read aloud naturally.
- For empathy-heavy pages, `empathy_depth` and `purchase_desire` must each be at least 8.0 in the problem, solution, benefit, and closing sections.
- `spoken_korean_gate` must be at least 8.0 in every visible section.
- `sentence_ending_fit` must be at least 8.0 in every visible section. If no ending is natural, rewrite rather than forcing a grammatical ending.
- Selling sections must score at least 8.0 for `conversion_force`. If a section is natural but only informative, revise it.
- When source planning text exists, `source_independence` must be at least 8.0 in every visible section. Exact source slogans, memo sentences, quoted concepts, and section titles are revise items even if the user supplied them.
- `expression_polish` must be at least 8.0 in every visible section. Any direct numeric price in visible detail-page copy, generated image text, or final HTML text is a revise item. Duplicated purchase-action cues, inconsistent action terms, broken parallel list rhythm, FAQ non-answers, final-section purchase-action text, repeated safety disclaimers, visible production notes, or repeated unnatural word choices are also revise items.
- `native_korean_human_score`, `grammar_confidence`, and `style_consistency` must each be at least 8.0 in every visible section for ordinary copy review.
- Hard fail: any S1 AI-writing marker remains after rewrite, including `~에 있어서`, `가지고 있다`, `~되어진다`, abstract subject + generic verb, unsupported hype, AI conclusion formulas, or visible strategy terms.
- Hard fail: repeated S2 AI-writing markers remain across a section or page, including `~에 대해`, `~를 통해`, `~에 기반하여`, `~할 수 있다`, excessive commas, repeated three-item rhythm, `~적 N` chains, or page-wide identical endings.

## Strict Skill-Improvement Gate

Use this gate only when improving or validating the planning/copywriter skills themselves.

- Every section average must be at least 9.2.
- Every section must score at least 9.2 for `korean_naturalness`, `sentence_ending_fit`, `spoken_korean_gate`, `expression_polish`, `native_korean_human_score`, `grammar_confidence`, and `style_consistency`.
- Every other criterion must be at least 8.8.
- Page-level product identity, buyer benefit, purchase-readiness information, desire, proof/readiness, and native Korean quality must each score at least 9.2.
- Page-level opening bridge must score at least 9.2.
- S1 AI marker count must be 0, repeated S2 marker count must be 0, `grammar_confidence` must pass, and meaning preservation must pass.
- Both validation products must pass: `무타공 자석 도어스토퍼` and `남자의 첫 중식도 스타터 세트`.

## Fast Rewrite Moves

- If identity is unclear: add product category or use scene in the headline.
- If benefit is abstract: name the annoying moment removed.
- If Korean is stiff: change noun stacks into verbs.
- If spoken Korean gate is weak: remove strategy terms, change abstract object subjects into person/action sentences, split long sentences, and rewrite as a seller would say it aloud.
- If sentence-ending fit is weak: classify the sentence function, compare possible endings, allow `none fits`, and rewrite or split the sentence if the ending changes the intended force.
- If expression polish is weak: complete the headline, fix wrong collocations, remove purchase-action cues from the final closing, unify repeated action terms, fix parallel list rhythm, answer FAQs directly, replace spec/internal terms, vary repeated wording, and move production notes to proof logs.
- If native Korean human score is weak: remove S1/S2 AI markers, reduce noun-heavy phrasing, replace translationese with buyer actions, vary sentence rhythm, and verify meaning preservation.
- If grammar confidence is weak: fix certain spelling, spacing, particle, ending, or punctuation errors without flattening ecommerce tone.
- If style consistency is weak: choose one vocabulary family per repeated action, align list/card endings, separate `해요체` selling copy from `합니다체` factual copy, and keep informational cues distinct from purchase-action prompts.
- If product is the hero: start with the buyer's home, body, routine, worry, or action.
- If purchase readiness is unclear: add a fit check, option information, component summary, proof cue, or compatibility note in a factual section, not in the final closing.
- If empathy is shallow: replace generic pain with a concrete moment, emotion, or failed workaround.
- If desire is weak: show the buyer's improved after-state or make the next decision easier.
- If conversion force is weak: add a target desire, before/after contrast, current-alternative friction, value-stack reason, proof visual, or clearer next decision point.
- If value framing is defensive: remove apology, show included value or avoided extra hassle, and use option/order-area language without numeric price or sales-channel names.
- If the review section is missing: add supplied review cards or replacement-ready mock review cards with generic nickname/handle, star rating, highlighted quote, and 2-4 lines of detailed benefit-based copy. Keep replacement status internal.
- If the review headline sounds staged: replace `먼저 써본 사람이 말해요`-style wording with `실제 사용자 후기를 확인해 보세요` when real reviews are supplied, or `사용 후기로 확인할 포인트` / `구매 전 많이 보는 후기를 모았습니다` when cards are replacement-ready mockups.
- If placeholder warnings are visible: remove `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `NEEDS_PROOF`, and similar wording from visible copy; move replacement notes to internal logs.
- If caveats are scattered: move non-blocking limits to specs, safety/care, compatibility, or FAQ.
- If visual proof is weak: specify a problem scene, mechanism demo, before/after, value-stack, or trust-proof visual.
- If source independence is weak: extract the source phrase's job, discard the wording, and rewrite from the buyer's real scene or decision.

## Early Flow Checklist

The first 2 sections should form a bridge:

- Screen 01: product/category cue + result promise.
- Screen 02: same buyer moment + repeated friction or first doubt.
- Shared anchor: one repeated noun, action, place, visual motif, or emotion.
- Enough story mass: not only one headline and one generic sentence.

The first 3 sections should include:

- Product/category cue: `무타공 자석 도어스토퍼`, `철문에 붙여 쓰는 도어스토퍼`.
- Core benefit: `짐 들고 들어올 때 문이 다시 닫히지 않게`.
- Purchase blocker: `자석이 붙는 철문/방화문인지 먼저 확인`.
- One clear next information check: `우리 집 문에 자석이 붙는지 확인해 주세요`.
