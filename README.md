# Danho Detailpage Maker Codex

Korean ecommerce detail-page workflow plugin for OpenAI Codex.

This plugin helps Codex plan, review, write, design, and build mobile-first Korean product detail pages with a hybrid HTML and generated-image workflow.

## Features

- Korean ecommerce detail-page planning from rough product briefs
- PM-style planning review loop before copy review
- Korean buyer-first copy review with naturalness, grammar/style, source-independence, and conversion-force gates
- Static mobile-first HTML detail-page builds
- `image-plan.md` driven `FULL_IMAGE`, `HTML_MIXED`, and `HTML_ONLY` decisions
- Mandatory designed `FULL_IMAGE` hero and final product/result closing section generation
- Locked text-asset, layout-grammar, and infographic-primitive prompting for designed images
- Built-in Codex `image_gen.imagegen` native image generation workflow
- No arbitrary image-count cap for detail-page images
- Reference detail-page design analysis through `REFERENCE_DESIGN_ANALYSIS.md`
- Workspace initialization with `AGENT.MD`

## Requirements

- OpenAI Codex with plugin support
- Built-in Codex image generation available when generating final images
- Git, if installing from this repository

No OpenAI API key is required for the Danho native image path. The workflow intentionally uses Codex's built-in `image_gen.imagegen` tool instead of API scripts or local image generation fallbacks.

Python, Playwright, Node/npm, bundlers, and local HTTP/dev servers are not required for ordinary detail-page production or preview. The generated output is plain static HTML/CSS with relative asset paths and should open directly from the filesystem. Helper scripts and browser automation may be used when available, but they are optional.

## Install From GitHub

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add maga119x/danho-detailpage-maker-codex --ref main
```

Then open Codex, install `danho-detailpage-maker-codex` from the added marketplace, and start a new thread so the plugin skills are loaded.

If your Codex version expects a Git URL instead of `owner/repo`, use:

```bash
codex plugin marketplace add git@github.com:maga119x/danho-detailpage-maker-codex.git --ref main
```

## Manual Local Install

Clone the repository:

```bash
git clone git@github.com:maga119x/danho-detailpage-maker-codex.git
```

Add or update your personal marketplace file at `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "danho-detailpage-maker-codex-local",
  "interface": {
    "displayName": "Danho Detailpage Maker Codex Local"
  },
  "plugins": [
    {
      "name": "danho-detailpage-maker-codex",
      "source": {
        "source": "local",
        "path": "./"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

For local marketplace installs, keep the marketplace file relative to the cloned repository or adjust `source.path` to point at the plugin root.

## Usage

In a clean work directory, start the workflow:

```text
/danho
```

or ask:

```text
상세페이지 전체 제작 워크플로우를 시작해줘
```

The plugin initializes `AGENT.MD` in the current work directory when needed. Product projects are created under:

```text
projects/MMDDHHmm_product-name/
```

Typical project artifacts:

```text
PLANNING.md
DESIGN.md
COPY_REVIEW.md
REFERENCE_DESIGN_ANALYSIS.md
config.json
image-plan.md
prompts/
assets/reference-designs/
assets/inbox/
assets/generated/
build/
build/sections/
```

## Workflow Summary

1. Normalize the product brief into facts, assumptions, proof gaps, visual needs, and risks.
2. If reference detail-page design files are supplied, extract transferable design/layout essence into `REFERENCE_DESIGN_ANALYSIS.md`.
3. Create `PLANNING.md`, `DESIGN.md`, and `config.json`.
4. Run a PM planning review loop until the plan passes.
5. Run copy review and patch visible Korean copy.
6. Run PM pre-coding review.
7. Build Phase A HTML before image generation.
8. Create `image-plan.md` with mandatory generated `FULL_IMAGE` rows for the opening hero and final product/result closing.
9. Generate approved images through Codex native `image_gen.imagegen`.
10. Build Phase B final HTML and verify section ids/comments.
11. Run final PM-level validation at 860px source width and inspect the same source scaled to a 438px phone preview.

## Important Production Rules

- Do not expose direct numeric prices in visible copy or generated images.
- Do not expose sales channel names inside the detail page.
- Do not create button UI, link buttons, or button-like CTA graphics.
- Do not skip PM review, copy review, or Phase A HTML.
- Do not jump from planning directly to image generation.
- Do not omit the mandatory designed full-image hero and final product/result closing section.
- Do not put CTA buttons, button-equivalent text, option/order prompts, benefit-check prompts, or purchase-action wording in the final closing; the shopping mall purchase UI handles that.
- Do not copy a supplied reference design page; extract layout rhythm and design essence only.
- Do not cap image count or force a fixed full-image/HTML split.
- Do not use browser screenshots, SVG/canvas, PIL composites, API scripts, or CLI imagegen fallbacks as generated-image substitutes.
- Do not treat a direct 393px/438px viewport as the primary mobile QA canvas; build an 860px source detail page and judge readability after scaling it to a 438px phone preview.
- Do not start a Node/dev server for plain HTML unless the user explicitly asks or a real browser security limitation blocks local assets.

## Repository Layout

```text
.codex-plugin/plugin.json
.agents/plugins/marketplace.json
skills/
  danho/
  danho-detailpage-workflow/
  danho-detailpage-planning/
  danho-detailpage-copywriter/
  danho-detailpage-pm-reviewer/
  danho-detailpage-coding/
  danho-imageprompt-helper/
```

## License

MIT
