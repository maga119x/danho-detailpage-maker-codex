---
name: danho
description: Start or initialize the Danho Korean ecommerce 상세페이지 maker workflow with a Korean slash-command-friendly alias. Use when the user invokes /단호한상세페이지, /danho, asks to start the Danho detail-page maker, wants to initialize a new working directory with AGENT.MD, supplies reference 상세페이지 design files to guide layout/style, or wants the full product 상세페이지 workflow from planning through PM review, copy review, HTML coding, image planning, GPT Image 2.0 native generation, and final validation.
---

# 단호한상세페이지 Slash Alias

Start the full Danho detail-page workflow.

Use `danho-detailpage-workflow` as the source of truth. Read its `SKILL.md` and follow the current production sequence there.

## Workspace Initialization

When the user asks to initialize a new 작업 디렉토리, or when the user starts Danho in a clean directory before creating product artifacts, create `AGENT.MD` in the current working directory before starting the detail-page project.

Use the bundled script from this skill folder:

```powershell
python <danho-skill-dir>/scripts/init_workspace.py --target <current-working-directory>
```

Rules:

- Create `AGENT.MD` at the workspace root, not inside `projects/MMDDHHmm_product-name/`.
- Do not overwrite an existing `AGENT.MD` unless the user explicitly asks. If it exists, read it and continue.
- If the script is unavailable, create `AGENT.MD` from `assets/AGENT.MD.template.md`.
- After initialization, continue with `danho-detailpage-workflow`.

Default behavior:

1. If the current working directory lacks `AGENT.MD`, initialize it first when this is a new Danho workspace.
2. If the user provides product information, start the full workflow from planning.
3. If a project already has artifacts, diagnose the current stage and continue from the next required step.
4. If the user supplies reference 상세페이지 design files, route them through `REFERENCE_DESIGN_ANALYSIS.md` before `DESIGN.md`; do not copy the reference page directly.
5. Preserve all current Danho workflow gates: PM planning loop before copywriter review, copywriter review before Phase A, PM pre-coding review before HTML, HTML before image generation, and built-in Codex `image_gen.imagegen` GPT Image 2.0 native generation only.
6. Ask only for factual blockers. Infer non-critical ecommerce context from the supplied product details.

Do not duplicate or override the workflow rules here. This skill is a short entry point for the full workflow.
