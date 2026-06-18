# Korean Sentence Ending Gate

Use this when Korean copy is grammatically understandable but the sentence ending makes it feel stiff, mismatched, too commanding, too casual, or AI-written.

This reference is based on:

- Seunguk Yu, Kyeonghyun Kim, Jungmin Yun, Youngbin Kim. 2025. `Making Sense of Korean Sentences: A Comprehensive Evaluation of LLMs through KoSEnd Dataset`. ACL SRW 2025.

## Paper Takeaways For Copy Editing

- Korean sentence endings are not decorative. They carry grammatical, semantic, emotional, and cultural nuance.
- A small ending change can alter whether a sentence reads as a statement, perception, self-talk, intention, concern, command, request, confirmation, or gentle suggestion.
- LLMs often struggle with Korean endings even when the sentence meaning is otherwise clear.
- Models perform better when explicitly told that no candidate ending may be natural. In copy editing, this means: do not force a sentence to keep its current ending. Rewrite, split, or convert to a phrase when no ending fits.
- Option order can bias model judgment. In copy editing, compare several ending candidates and check consistency instead of accepting the first natural-looking rewrite.
- Imperative endings are especially fragile because command/request/permission/soft suggestion can overlap. Use them only when the speaker, buyer relationship, and section role support that force.
- Native-speaker judgments can vary by context. When ambiguous, choose the ending that best fits the page's speaker/listener relationship and the buyer's current decision stage.

## Ecommerce Sentence Context

Before judging an ending, define:

| Field | Question |
|---|---|
| speaker | Who is speaking: brand, seller, reviewer, guide, buyer thought? |
| listener | Who is addressed: cautious buyer, current user, gift buyer, expert, beginner? |
| relationship | Helpful seller, factual guide, direct CTA, FAQ answer, review check? |
| medium | Mobile ecommerce detail page, image section, FAQ, option row, policy? |
| section role | Hook, problem, answer, proof, option, review, FAQ, CTA? |
| sentence function | Statement, promise/intention, suggestion/request, confirmation, warning, perception, self-identification? |

Do not judge endings without this context.

## Ending-Fit Procedure

For every visible sentence:

1. Identify the sentence function.
2. List 2-3 plausible ending styles.
3. Include `none fits` as an allowed option.
4. Select the ending that fits speaker/listener/section role.
5. If `none fits`, rewrite the sentence, split it, or change it to a headline phrase.
6. Re-check adjacent sentences so the section does not repeat the same ending pattern.

## Common Ending Families

Use these as editing categories, not as a rigid grammar table.

| Ending family | Use when | Watch for |
|---|---|---|
| `합니다/습니다/입니다` | specs, policy, FAQ facts, calm product explanation, formal brand tone | Repetition across every headline/body line creates report tone. |
| `해요/돼요/있어요` | friendly seller explanation, soft benefit, casual product guidance | Too casual for legal/safety/spec facts or if the user requested strict `합니다체`. |
| `해 주세요/확인해 주세요` | buyer action, fit check, option confirmation | Overuse feels scolding or mechanical; do not use as a substitute for value persuasion. |
| `보세요/챙겨보세요/살펴보세요` | soft recommendation or scan-friendly next information check | Can sound too promotional if repeated. |
| `해야 합니다/필요합니다` | requirement, safety, compatibility, real limitation | Use sparingly; too much increases anxiety. |
| `~죠/~지요` | gentle confirmation, shared assumption, conversational bridge | Avoid in formal brand/spec copy. |
| `~네요/~군요/~구나` | perception, surprise, self-talk, customer thought | Usually not suitable for seller claims unless framed as buyer voice. |
| `~할게요/~하겠습니다` | seller commitment or guide promise | Do not use for buyer action or product property. |
| bare noun/fragment | headlines, badges, image text, rhythm breaks | Must still land as a complete idea; avoid clipped strategy labels. |
| imperative/command forms | direct command or instruction | Usually too strong for Korean ecommerce unless safety/use instructions require it. |

## Hard Fail Patterns

Revise when:

- The ending implies a command but the section should be a suggestion.
- A buyer action is written like a seller promise.
- A product fact is written like a buyer request.
- A safety/limitation sentence is written too casually.
- A review/check sentence pretends to be a real testimonial.
- Adjacent sentences all end in the same pattern, creating AI-slop rhythm.
- A headline is only a strategy label with a grammatical ending attached.
- No ending actually feels natural, but the sentence is kept anyway.

## Repair Moves

| Problem | Repair |
|---|---|
| Forced ending | Split the sentence or convert the headline to a noun phrase. |
| Too many `합니다` endings | Keep `합니다체` in factual body copy, but make headlines phrase-based or question-based. |
| Too many `확인합니다/확인해 주세요` endings | Use value/action wording before the confirmation cue. |
| Over-strong command | Change to a soft information check or factual requirement. |
| Casual ending in policy/safety | Change to formal factual ending. |
| Awkward imperative | Reframe as what the buyer can check/do. |
| Sentence still unnatural after ending swap | Rewrite the sentence skeleton, not just the final ending. |

## Audit Table

When producing `COPY_REVIEW.md`, include a concise audit:

| sentence | function | current_ending | candidate_endings | decision | rewrite |
|---|---|---|---|---|---|
|  | statement / suggestion / warning / FAQ / CTA / review-check |  | keep / replace / none fits |  |  |

## Pass Standard

Pass only when:

- every visible sentence has an ending that fits its function and context
- `none fits` cases were rewritten instead of forced
- headline endings and visual section copy do not repeat the same pattern across the page
- CTA/request endings are not overused
- safety, FAQ, option, and policy copy use endings with the right degree of formality
- the page can be read aloud by a Korean seller without the endings sounding mismatched
