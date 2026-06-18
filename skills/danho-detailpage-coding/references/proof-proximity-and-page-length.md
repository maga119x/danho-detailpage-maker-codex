# Proof Proximity And Page Length

Use this to decide whether a page is too dense or too shallow.

## Long Is Acceptable; Dense Is Not

Korean ecommerce detail pages can be long because each mobile screen should be easy to understand. A short page that compresses several claims into one screen is harder to read and usually looks amateur.

When in doubt, split:

- one complex benefit into 3-5 screens
- one technical claim into 4-6 screens
- one option/reward system into 5-10 screens
- one proof/review block into 2-4 screens

## Claim Splitting

Use this table when a section feels crowded.

| Crowded section contains | Split into |
|---|---|
| problem + solution | problem scene, then product answer |
| solution + mechanism | answer claim, then mechanism explainer |
| mechanism + proof | mechanism screen, then proof screen |
| proof + comparison | proof board, then comparison screen |
| feature list + use case | feature detail, then use-case grid |
| option + price + component | option overview, component cards, price rows |
| FAQ + safety + policy | FAQ screen, safety/care screen, policy zone |

## Proof Proximity Rules

- A strong claim needs proof in the same screen or next screen.
- If proof appears before the claim, the next screen must explain what the buyer should conclude.
- Do not let proof images float as decoration. Caption or frame the buying meaning.
- Do not invent proof. If unsupported, soften the visible claim and keep `NEEDS_PROOF` internal.

## Proof Types

| Claim type | Preferred proof |
|---|---|
| works better | before/after or side-by-side comparison |
| tastes/looks/feels better | result image plus review |
| safe | use scene, material fact, caution, certification if supplied |
| durable | material close-up, test result, warranty if supplied |
| easy | hands-in-use sequence, step cards |
| compatible | fit image, checklist, spec row |
| worth the price | included items, avoided extra purchase, comparison, real components |
| trusted | real review, certificate, award, manufacturing story, media proof |

## Page-Length Gates

Fail the layout if:

- the whole page has fewer than 10 screens for a normal product
- a technical/high-consideration product has fewer than 18 screens
- a reward/option-heavy product has fewer than 22 screens
- the final hybrid page starts with an HTML text hero even though a designed full-image hero exists
- the first 3 screens are mostly text
- a key feature gets only one text card and no result/proof/use screen
- a low-copy result/transition section is left as a sparse HTML block without image dominance
- a low-copy option, care/storage, value, reassurance, or final decision section is only centered text, one note box, or 1-2 small cards with no meaningful image
- a section is made taller with blank padding or empty background space instead of product/lifestyle/proof content
- FAQ/options/specs consume more visual weight than the main benefit before the midpoint

These are not rigid section counts, but they prevent over-compressed pages.

## Dense Screen Red Flags

Revise when one mobile viewport contains:

- more than one headline-level idea
- more than 5 bullets before a proof image
- more than 2 cards with paragraph-length text
- three or more independent subtopics in one card grid
- a feature list and FAQ answer together
- pricing, option, component, and warning in one card
- three or more visual hierarchy styles competing at once

## Sparse Screen Red Flags

Revise when one mobile viewport contains:

- only a label, headline, and one short lead
- a transition sentence with no proof image or product image
- a low-copy result moment represented only by two small cards
- an option, care/storage, value, or reassurance screen represented only by one note box or 1-2 cards
- a dark or pale band where most height is empty space
- a section that feels like it exists only to add length

Fix sparse screens by converting them into a full-image section, an image-story section, adding a large `HTML_MIXED` support image, or merging them with a nearby proof/detail screen. Choose image-story when the image can explain the point faster than more copy. Choose support images when option, care, or factual text must remain editable.

## Expansion Examples

### From One Dense Benefit Section

Bad:

```text
It cooks faster, tastes better, uses special material, is easy to clean, and is safe.
```

Better:

1. result screen: what the buyer gets
2. question screen: why it works
3. mechanism screen: special material/structure
4. use screen: easy daily action
5. proof screen: comparison, review, or measurement
6. care screen: cleaning/safety detail

### From One Dense Option Section

Bad:

```text
Bundle A/B, all components, discounts, color, size, compatibility, FAQ in one section.
```

Better:

1. reward overview
2. component card A
3. component card B
4. set summary
5. price/order guidance
6. compatibility note
7. FAQ

## Final QA

At mobile width, scroll screen by screen and ask:

- What is the one thing this screen wants me to understand?
- What visual proves or clarifies it?
- Is the next screen a new step, proof, or relief from density?
- Could this screen be split to make the claim easier?

If the answer is unclear, split or reorder before final delivery.
