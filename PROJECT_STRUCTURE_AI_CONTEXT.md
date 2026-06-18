# Danho Detailpage Maker Codex - AI Parsing Context

> 이 문서는 AI 에이전트가 프로젝트 구조와 실행 흐름을 빠르게 파싱하도록 만든 단일 혼합 포맷 문서다.
> Markdown은 사람이 읽는 요약, YAML은 정규화된 데이터, XML은 계층 관계와 워크플로우 경계를 표현한다.

## 1. Human Summary

`danho-detailpage-maker-codex`는 한국 이커머스 상세페이지를 기획, 코딩, 이미지 제작까지 진행하는 Codex 플러그인 프로젝트다.

플러그인을 설치한 뒤 새 작업 디렉토리에서 상세페이지를 만들 때는 먼저 해당 작업 루트에 `AGENT.MD`를 초기화한다. `AGENT.MD`는 로컬 작업 폴더용 부트스트랩 체크리스트이며, 프로젝트 산출물은 그 아래 `projects/MMDDHHmm_product-name/`에 만든다.

핵심 방식은 `v12_review_mockup_social_proof_required_workflow`다. 사용자가 제품 기획, 프롬프트, 메모, 초안 카피를 제공하면 먼저 소스 브리프 정규화를 진행해 사실/전략/증거/초안문구/비주얼/리스크를 분리하고, 소스 문장은 visible copy로 그대로 보존하지 않는다. 그 다음 전략어를 바로 노출 카피로 옮기지 않고, 고객 입말 전략으로 한 번 바꾼다. 공감 설득, 전환 욕망, 가치 프레임, 증거 비주얼 같은 내부 개념은 `PLANNING.md` 안에서만 사고 도구로 쓰고, visible copy에는 실제 한국 소비자 속마음이나 판매자 설명처럼 말할 수 있는 문장만 남긴다. 첫 `PLANNING.md` 초안이 완성되면 copywriter로 넘어가기 전에 `danho-detailpage-pm-reviewer`로 `계획 -> PM 검토 -> 계획 수정 -> 재검토` 루프를 실행해 섹션 순서, 모바일 화면 흐름, 구매 질문 연결, 헤드라인 리듬 위험, 비주얼 무게 중심, 증거/리뷰/마감 배치를 고친다. 이 루프가 `pass`를 기록한 뒤에만 `COPY_REVIEW.md`에서 자연스러운 한국어, 소비자 베네핏, 번역투 제거, 높임말 일관성, 윤리적 설득 원칙, 소스 독립성, 한국어 표현 폴리싱, 전환력뿐 아니라 `spoken_korean_gate`와 production readiness를 검수한다. 문장별로 Kakao 테스트, 소리 내 읽기 테스트, 실제 판매자 발화 테스트, 전략어 누출 테스트, 영어식 문장 골격 테스트를 통과해야 한다. 가격은 프로모션과 채널 할인으로 변동될 수 있으므로 내부 정보/config에만 보관하고, 상세페이지 visible copy/HTML/이미지에는 숫자 가격을 넣지 않는다. 판매채널명은 이미 해당 채널 안에 있는 상세페이지에서 다시 노출하지 않고, 혜택/프로모션처럼 변동되는 정보는 필요한 경우 editable factual/options 섹션에만 둔다. 모든 신규 상세페이지에는 리뷰/후기 섹션을 포함하며, 실제 리뷰가 없으면 닉네임/핸들, 별점, 하이라이트 문장, 상세 후기 copy를 갖춘 교체용 목업 리뷰 카드를 만들고 교체 표시는 내부 로그에만 남긴다. 이후 Phase A HTML을 만들기 전에 `danho-detailpage-pm-reviewer`로 copywriter 수정 후에도 흐름이 유지되는지 다시 확인한다. 그 다음 HTML에서는 모바일 세로형 스토리 구조를 만들고, `image-plan.md`에서 각 섹션을 `FULL_IMAGE`, `HTML_MIXED`, `HTML_ONLY`로 확정한다. 내용이 적은 옵션/보관/가치/전환/마무리 섹션은 `SPARSE_SECTION_IMAGE_REQUIRED`로 분류해 통 이미지, 이미지 스토리, 큰 지원 이미지, 또는 병합으로 처리하며 빈 여백만으로 길이를 늘리지 않는다. 특히 첫 2개 화면은 `OPENING_STORY_BRIDGE_REQUIRED` 게이트로 관리해, 1번 화면의 약속/결과가 2번 화면의 같은 생활 장면, 반복 불편, 감정, 다음 질문으로 이어지지 않으면 기획과 코딩 모두 실패로 본다.

이미지 장수에는 상한이나 고정 비율을 두지 않는다. 모든 신규 상세페이지는 최소한 1번 히어로와 마지막 상품/결과 클로징 화면을 Codex 네이티브 생성 기반 `FULL_IMAGE`로 구성해야 한다. `FULL_IMAGE`와 `HTML_MIXED` 지원 이미지는 스토리 연결, 증거 밀도, 옵션/보관/비교/리뷰/FAQ 보강, sparse 섹션 길이, 최종 결정 지원에 필요한 만큼 사용하며, 고정 split이나 생성 호출 절약을 위해 이미지를 줄이지 않는다.

디자인된 `FULL_IMAGE` 프롬프트는 텍스트를 문장이 아니라 locked layout asset으로 다룬다. `IMAGE JOB`, `EXACT TEXT ASSETS`, `LAYOUT GRAMMAR`, `TYPOGRAPHY SYSTEM`, `CONSTRAINTS` 슬롯을 사용하고, headline/subhead/badge/label/stat card/callout/comparison header/caption 같은 역할, title block/stat cards/comparison strip/step flow/icon row/radial callouts 같은 인포그래픽 primitive, 읽는 순서, safe margin, negative space를 명시한다.

사용자가 레퍼런스용 상세페이지 디자인 파일을 첨부하면 `assets/reference-designs/`에 보관하고 `REFERENCE_DESIGN_ANALYSIS.md`를 만든다. 여기서는 섹션 리듬, 시각 무게, 여백, 타이포 대비, 카드/구분선/비교/후기 패턴, 이미지 크롭 같은 디자인 에센스만 추출하며, 레퍼런스의 브랜드, 문구, 로고, 제품 이미지, 가격, 정확한 레이아웃, 고유 구성을 복제하지 않는다.

### Root Layout

```text
danho-detailpage-maker-codex/
├── .agents/
│   └── plugins/
│       └── marketplace.json
└── plugins/
    └── danho-detailpage-maker-codex/
        ├── .codex-plugin/
        │   └── plugin.json
        └── skills/
            ├── danho/
            ├── danho-detailpage-workflow/
            ├── danho-detailpage-planning/
            ├── danho-detailpage-copywriter/
            ├── danho-detailpage-pm-reviewer/
            ├── danho-detailpage-coding/
            └── danho-imageprompt-helper/
```

### Main Skills

| Skill | Purpose | Primary Outputs |
|---|---|---|
| `danho` | `/단호한상세페이지` 한글 슬래시 명령어/시작 alias | `danho-detailpage-workflow` 실행 |
| `danho-detailpage-workflow` | 전체 제작 흐름 오케스트레이션 | 다음 실행 단계 판단 |
| `danho-detailpage-planning` | 상세페이지 기획 및 카피 작성 | `PLANNING.md`, `DESIGN.md`, `config.json` |
| `danho-detailpage-copywriter` | 모바일 스캔 이해도 점수화, 자연스러운 한국어와 소비자 베네핏 중심 카피 검수/재작성 | `COPY_REVIEW.md`, 갱신된 `PLANNING.md` |
| `danho-detailpage-pm-reviewer` | copywriter 전 planning 루프와 Phase A 전/후 상세페이지 흐름, 섹션 연속성, 헤드라인 리듬, 시각 무게 중심, 전환 구조 검토 | 갱신된 `PLANNING.md` 또는 HTML 패치 |
| `danho-detailpage-coding` | 세로형 하이브리드 HTML 빌드 및 이미지 반영 | `v1-textonly.html`, `vN-hybrid.html`, `sections/` |
| `danho-imageprompt-helper` | 통 이미지/지원 이미지 프롬프트 및 Codex 네이티브 이미지 생성 | `banners.md`, `photos.md`, `assets/generated/*.png` |

---

## 2. YAML Canonical Data

```yaml
project:
  name: danho-detailpage-maker-codex
  type: codex_plugin
  version: "0.2.0"
  language: ko
  domain: korean_ecommerce_detail_page
  purpose:
    - 상세페이지 기획
    - 정적 HTML 코딩
    - 이미지 프롬프트 생성
    - Codex 네이티브 이미지 생성
    - 이미지 반영 후 최종 상세페이지 제작

plugin:
  manifest: plugins/danho-detailpage-maker-codex/.codex-plugin/plugin.json
  display_name: 단호한 상세페이지 메이커
  description: Korean e-commerce detail-page planning, text-first HTML publishing, and image prompt generation.
  skills_path: ./skills/
  capabilities:
    - Write
    - Design
    - Generate
  default_prompts:
    - 상세페이지 전체 제작 워크플로우를 시작해줘
    - PLANNING.md와 DESIGN.md로 텍스트 HTML을 만들어줘
    - v1 HTML 기준 image-plan과 이미지 프롬프트를 만들어줘

marketplace:
  file: .agents/plugins/marketplace.json
  source:
    type: local
    path: ./plugins/danho-detailpage-maker-codex
  policy:
    installation: AVAILABLE
    authentication: ON_INSTALL
  category: Productivity

directories:
  root:
    .agents/plugins/:
      role: local_marketplace_registration
      contains:
        - marketplace.json
    plugins/danho-detailpage-maker-codex/.codex-plugin/:
      role: plugin_manifest_directory
      contains:
        - plugin.json
    plugins/danho-detailpage-maker-codex/skills/:
      role: skill_packages
      contains:
        - danho-detailpage-workflow
        - danho
        - danho-detailpage-planning
        - danho-detailpage-copywriter
        - danho-detailpage-pm-reviewer
        - danho-detailpage-coding
        - danho-imageprompt-helper

skills:
  danho:
    path: plugins/danho-detailpage-maker-codex/skills/danho/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: /단호한상세페이지 Korean slash-command-friendly workflow alias and workspace initializer
    implicit_invocation: true
    triggers:
      - /단호한상세페이지
      - /danho
      - Danho 시작
      - 단호한 상세페이지 메이커 시작
      - 상세페이지 전체 제작 시작
      - 새 작업 디렉토리 초기화
      - AGENT.MD 생성
    routes_to: danho-detailpage-workflow
    workspace_init:
      output: AGENT.MD
      script: plugins/danho-detailpage-maker-codex/skills/danho/scripts/init_workspace.py
      template: plugins/danho-detailpage-maker-codex/skills/danho/assets/AGENT.MD.template.md
      overwrite_policy: do not overwrite unless explicitly requested

  danho-detailpage-workflow:
    path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-workflow/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: 전체 상세페이지 제작 워크플로우 오케스트레이션
    implicit_invocation: true
    triggers:
      - 상세페이지 만들어줘
      - 전체 워크플로우
      - 단호한 상세페이지
      - 제품 상세페이지 제작
    decision_tree:
      - if: rough_product_information_only
        run: danho-detailpage-planning
      - if: PLANNING.md_and_DESIGN.md_exist_and_pm_planning_loop_missing_or_revise
        run: danho-detailpage-pm-reviewer.planning_loop_review
      - if: PLANNING.md_DESIGN.md_and_pm_planning_loop_pass
        run: danho-detailpage-copywriter
      - if: PLANNING.md_COPY_REVIEW.md_and_DESIGN.md_exist_and_approved
        run: danho-detailpage-pm-reviewer.pre_coding_flow_review
      - if: PLANNING.md_COPY_REVIEW.md_DESIGN.md_and_pm_flow_review_pass
        run: danho-detailpage-coding.phase_a
      - if: v1_textonly_exists_and_image_plan_missing
        run: create_image_plan
      - if: image_plan_exists_and_user_wants_prompts_or_images
        run: danho-imageprompt-helper
      - if: generated_or_inbox_images_available_and_plan_approved
        run: danho-detailpage-coding.phase_b

  danho-detailpage-planning:
    path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-planning/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: 한국 이커머스 상세페이지 기획과 설득 카피 작성
    implicit_invocation: true
    required_inputs:
      critical:
        - product_name
        - internal price
        - product_naming_3_levels
        - brand_name
        - brand_tone
        - target_customer
        - pain_points
        - selling_points
      optional:
        - category
        - material_or_ingredients
        - product_story
        - existing_images
        - reference_detailpage_design_files
    outputs:
      - projects/MMDDHHmm_project-name/PLANNING.md
      - projects/MMDDHHmm_project-name/DESIGN.md
      - projects/MMDDHHmm_project-name/REFERENCE_DESIGN_ANALYSIS.md
      - projects/MMDDHHmm_project-name/config.json
    references:
      - references/korean-headline-rules.md
      - references/product-naming-consistency.md
      - references/section-library.md
      - references/genre-composition.md
      - references/image-guidelines.md
      - references/persuasion-framework.md
      - references/output-format.md
      - references/source-brief-normalization.md
      - references/reference-design-analysis.md
      - references/wadiz-empathy-conversion-flow.md
      - references/conversion-desire-architecture.md
      - references/copy-templates.md
      - ../danho-detailpage-copywriter/references/mobile-scan-purchase-audit.md
      - ../danho-detailpage-copywriter/references/korean-commerce-expression-bank.md
      - ../danho-detailpage-copywriter/references/channel-review-production-rules.md
    rule:
      planning_must_be_text_first: true
      copy_is_draft_until_review: true
      infer_noncritical_copy_context: true
      first_3_sections_must_answer_identity_benefit_purchase_check: true
      opening_story_bridge_required: true
      source_brief_normalization_required_when_source_plan_exists: true
      empathy_conversion_map_required_for_persuasion_pages: true
      conversion_desire_architecture_required: true
      reference_design_analysis_required_when_reference_design_files_exist: true
      benefit_modules_required_for_feature_rich_products: true
      ask_only_for_factual_blockers: true
      image_slots_are_forbidden_in_planning: true
      only_mark_image_candidates: true
      sparse_section_image_required: true
      image_count_has_no_cap: true
    scripts:
      prepare_reference_designs.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-planning/scripts/prepare_reference_designs.py
        role: copy reference design files into assets/reference-designs and slice tall images for visual analysis

  danho-detailpage-copywriter:
    path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-copywriter/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: 모바일 스캔 이해도 점수화와 자연스러운 한국어 상세페이지 카피 검수/재작성
    implicit_invocation: true
    required_inputs:
      - PLANNING.md
      - product_facts
      - target_customer
      - pain_points
      - selling_points
    outputs:
      - projects/MMDDHHmm_project-name/COPY_REVIEW.md
      - updated projects/MMDDHHmm_project-name/PLANNING.md
    principles:
      - customer_language_first
      - benefits_over_product_merits
      - infer_speaker_listener_medium_honorific_tone
      - buyer_as_subject_brand_as_guide
      - mobile_scan_purchase_audit
      - empathy_depth_and_purchase_desire_scoring
      - source_independence_scoring
      - korean_expression_polish_scoring
      - spoken_korean_gate_scoring
      - conversion_force_scoring
      - score_gate_before_coding
      - remove_translationese_and_noun_heavy_korean
      - ethical_cialdini_principles_only
      - storybrand_style_customer_as_hero
      - no_fake_verified_social_proof_or_scarcity
      - review_section_required
      - sales_channel_hidden_from_visible_copy
    references:
      - references/consumer-benefit-copy.md
      - references/mobile-scan-purchase-audit.md
      - references/korean-copy-polish-rules.md
      - references/korean-commerce-expression-bank.md
      - references/korean-pragmatic-style.md
      - references/korean-first-expression-gate.md
      - references/channel-review-production-rules.md
      - references/persuasion-storybrand-check.md
      - references/copy-review-format.md
      - ../danho-detailpage-planning/references/conversion-desire-architecture.md

  danho-detailpage-pm-reviewer:
    path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-pm-reviewer/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: copywriter 전 planning 루프와 Phase A 전/후 상세페이지 PM 플로우 검토와 흐름 패치
    implicit_invocation: true
    modes:
      planning_loop_review:
        inputs:
          - PLANNING.md
          - DESIGN.md
        output:
          - updated PLANNING.md
        checks:
          - mobile_screen_flow
          - opening_story_bridge
          - buyer_question_continuity
          - section_density
          - proof_review_options_closing_placement
          - headline_rhythm_risk
          - planned_visual_mass
          - image_candidate_fit
      pre_coding_flow_review:
        inputs:
          - PLANNING.md
          - COPY_REVIEW.md
          - DESIGN.md
        output:
          - updated PLANNING.md
        checks:
          - planned_section_sequence
          - mobile_screen_flow
          - opening_story_bridge
          - buyer_question_continuity
          - headline_rhythm_risk
          - planned_visual_mass
          - conversion_structure
      rendered_html_review:
        inputs:
          - build/project-name-v1-textonly.html
          - build/project-name-v2.html
        output:
          - patched HTML
        checks:
          - actual_rendered_sequence
          - section_continuity
          - headline_rhythm
          - visual_hierarchy
          - density
          - forbidden_copy

  danho-detailpage-coding:
    path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: DESIGN.md 기반 세로형 정적 HTML 생성 및 image-plan.md 기반 하이브리드 이미지 반영
    implicit_invocation: true
    phases:
      phase_a:
        name: text_only_build
        inputs:
          - PLANNING.md
          - DESIGN.md
        output:
          - build/project-name-v1-textonly.html
        invariant:
          - 신규 기획은 PM planning loop pass 이후에만 Phase A로 진입한다
          - 모든 카피는 HTML 안에 존재해야 한다
          - 이미지는 placeholder만 사용한다
          - 이미지 안에 들어갈 카피를 미리 HTML에서 제거하지 않는다
      image_plan:
        name: section_image_decision
        input:
          - build/project-name-v1-textonly.html
        output:
          - image-plan.md
        cases:
          - FULL_IMAGE
          - HTML_MIXED
          - HTML_ONLY
        requires_user_agreement: true
        invariant:
          - 이미지 장수 상한이나 고정 full-image/HTML 비율을 적용하지 않는다
          - 스토리, 증거, 옵션, 보관, 비교, 리뷰, sparse 섹션 보강에 필요한 모든 이미지를 계획한다
      phase_b:
        name: image_replacement_build
        inputs:
          - build/project-name-v1-textonly.html
          - image-plan.md
          - assets/inbox/
          - assets/generated/
        outputs:
          - build/project-name-v2.html
          - build/sections/
    scripts:
      build.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/scripts/build.py
        role: DESIGN.md 기반 HTML 초기화 및 섹션 병합 빌드
      design_md.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/scripts/design_md.py
        role: DESIGN.md 파싱, 검증, CSS variables와 component class 생성
      split_sections.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/scripts/split_sections.py
        role: Python이 있을 때 완성 HTML을 섹션별 파일과 CSS로 분리하는 선택 helper
      replace_placeholders.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/scripts/replace_placeholders.py
        role: placeholder를 실제 이미지로 치환
      generate_placeholder.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/scripts/generate_placeholder.py
        role: 단일 placeholder 이미지 생성
      generate_placeholders_to_assets.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/scripts/generate_placeholders_to_assets.py
        role: 프로젝트 placeholder 이미지를 assets로 일괄 생성
    references:
      - references/design-md-spec.md
      - references/design-md-presets/
      - references/text-image-deduplication.md
      - references/image-plan-template.md
      - references/mobile-hybrid-layout.md
      - references/html-first-detailpage-build.md
      - references/detailpage-typography.md
      - references/color-system.md
      - references/layout-rules.md
      - references/static-design.md
      - references/output-checklist.md

  danho-imageprompt-helper:
    path: plugins/danho-detailpage-maker-codex/skills/danho-imageprompt-helper/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: HTML과 image-plan.md 기반 통 이미지/지원 이미지 프롬프트 작성 및 Codex 네이티브 이미지 생성
    implicit_invocation: true
    required_inputs:
      - DESIGN.md
      - build/project-name-v1-textonly.html
      - image-plan.md
    outputs:
      - prompts/banners.md
      - prompts/photos.md
      - assets/generated/*.png
      - assets/generated/manifest.md
    native_generation:
      default: true
      engine: built-in Codex image_gen.imagegen only
      model_family: GPT Image 2.0 / gpt-image-2 native path via built-in Codex capability
      model_rule: use only built-in Codex image_gen.imagegen as GPT Image 2.0; do not switch to API, CLI, older GPT Image models, or other image generators
      availability_rule: if image_gen.imagegen is in the active tool list, native generation is available
      mismatch_rule: if the runtime explicitly reports built-in image_gen.imagegen is not GPT Image 2.0 / gpt-image-2, stop with native_model_mismatch
      no_block_on_missing_tool_fields:
        - model
        - output_path
        - reference_images
        - quality
        - batch
      forbidden:
        - direct OpenAI API calls
        - OPENAI_API_KEY
        - curl image generation
        - CLI imagegen fallback workflows
        - browser-rendered section screenshots
        - HTML/CSS/SVG/canvas/PIL drawings as generated-image substitutes
        - local API generation scripts
      output_directory: assets/generated/
      manifest: assets/generated/manifest.md
      product_reference_policy:
        default: assets/inbox images are PRODUCT_REFERENCE
        direct_use_requires: USER_IMAGE_DIRECT in image-plan.md
        generated_outputs: assets/generated/
      full_image_prompting_policy:
        required_slots:
          - IMAGE JOB
          - EXACT TEXT ASSETS
          - LAYOUT GRAMMAR
          - TYPOGRAPHY SYSTEM
          - CONSTRAINTS
        text_asset_roles:
          - kicker
          - headline
          - subhead
          - badge
          - feature_label
          - stat_card
          - callout_label
          - comparison_header
          - caption
          - proof_label
          - closing_phrase
        infographic_primitives:
          - title_block
          - stat_cards
          - comparison_strip
          - step_flow
          - icon_row
          - radial_callouts
          - ingredient_cards
          - before_after_split
          - leader_lines
        layout_rules:
          - specify_reading_flow
          - specify_safe_margins
          - use_generous_negative_space_for_typography
          - no_extra_words_or_duplicate_text
      generated_output_recovery:
        source_root: "%USERPROFILE%/.codex/generated_images/<session-id>/ig_*.png"
        session_jsonl_root: "%USERPROFILE%/.codex/sessions/**/*.jsonl"
        rule: if Codex UI shows a preview, generation succeeded; first use any exposed saved path, then search generated_images, then decode session JSONL image_generation_end result before marking export blocked
        helper_script: plugins/danho-detailpage-maker-codex/skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py
        diagnostic_command: "python plugins/danho-detailpage-maker-codex/skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py --diagnose --minutes 240 --limit 30"
        copy_rule: copy accepted ig_*.png or decoded SESSION_JSONL_NATIVE_OUTPUT into the planned assets/generated path and record source id in manifest
        clipboard_rule: codex-clipboard screenshots prove a UI preview existed but are not valid generated asset provenance unless the user supplies the actual generated image file
    references:
      - references/prompt-guide.md
      - references/native-image-generation.md
      - references/product-reference-images.md
    scripts:
      collect_codex_generated_images.py:
        path: plugins/danho-detailpage-maker-codex/skills/danho-imageprompt-helper/scripts/collect_codex_generated_images.py
        role: list/copy Codex native ig_*.png outputs from .codex/generated_images into project assets/generated

workflow:
  version: v12_review_mockup_social_proof_required
  copy_source_of_truth: build/project-name-v1-textonly.html
  strict_sequence:
    - order: 0
      skill: danho
      mode: workspace_init
      action: 새 작업 디렉토리 루트에 AGENT.MD가 없으면 먼저 생성하고, 기존 파일은 덮어쓰지 않는다
    - order: 0.5
      skill: danho-detailpage-planning
      mode: reference_design_analysis
      action: 레퍼런스 상세페이지 디자인 파일이 있으면 assets/reference-designs/에 정리하고 REFERENCE_DESIGN_ANALYSIS.md로 디자인/레이아웃 에센스를 추출한다
    - order: 1
      skill: danho-detailpage-planning
      action: 제품 정보로 PLANNING.md, DESIGN.md 생성
    - order: 2
      skill: danho-detailpage-pm-reviewer
      mode: planning_loop_review
      action: copywriter 전 PLANNING.md와 DESIGN.md 기준으로 계획 -> PM 검토 -> 계획 수정 루프를 실행하고 PM planning loop pass를 기록
    - order: 3
      skill: danho-detailpage-copywriter
      action: COPY_REVIEW.md 생성, 섹션별 점수 평가, 재작성 루프 후 PLANNING.md의 노출 카피를 자연스러운 한국어와 소비자 베네핏 중심으로 갱신
    - order: 4
      skill: danho-detailpage-pm-reviewer
      mode: pre_coding_flow_review
      action: PLANNING.md, COPY_REVIEW.md, DESIGN.md 기준으로 섹션 순서, 모바일 화면 흐름, 구매 질문 연결, 헤드라인 리듬 위험, 비주얼 무게 중심을 검토하고 문제를 패치
    - order: 5
      skill: danho-detailpage-coding
      phase: phase_a
      action: PM 검토를 통과한 화면 흐름으로 텍스트만으로 완전한 v1 HTML 생성
    - order: 6
      artifact: image-plan.md
      action: 섹션별 FULL_IMAGE, HTML_MIXED, HTML_ONLY 결정. 1번 히어로와 마지막 상품/결과 클로징은 mandatory FULL_IMAGE로 포함
      stop_for_user_agreement: true
    - order: 7
      skill: danho-imageprompt-helper
      action: locked text assets, layout grammar, infographic primitives, reading flow, whitespace를 포함한 이미지 프롬프트 작성 후 Codex 네이티브 이미지 생성 큐를 병렬 배치로 처리
    - order: 8
      skill: danho-detailpage-coding
      phase: phase_b
      action: image-plan.md에 따라 v2 HTML 생성

image_cases:
  FULL_IMAGE:
    meaning: 이미지 모델이 만든 완성 통 이미지가 HTML 레이아웃을 대체
    mandatory_minimum:
      - opening_hero
      - final_product_result_closing
    html_text_handling: remove_original_section
    image_policy: 짧은 한글 카피는 역할별 locked text asset으로 지정하고, 인포그래픽 primitive와 읽는 순서를 함께 프롬프트에 포함
    duplicate_copy_allowed: false
    typical_sections:
      - hook
      - scene-problem
      - blocker
      - answer
      - no-damage
      - daily-use
      - control
      - final-closing
  HTML_MIXED:
    meaning: HTML 텍스트는 유지하고 섹션 안 또는 인접 위치에 지원 이미지를 결합
    html_text_handling: keep_original_section_and_add_visual_or_component
    image_policy: no text, no Korean caption, no overlay text
    duplicate_copy_allowed: false
    typical_sections:
      - fit-check
      - install-flow
      - fit-adjust
      - material
      - compare
      - review-proof
      - options
      - faq
  HTML_ONLY:
    meaning: 이미지 없이 HTML 텍스트만 유지
    html_text_handling: keep_original_section
    image_policy: no image
    typical_sections:
      - faq
      - specs
      - options
      - footer

expected_project_output:
  root: projects/MMDDHHmm_project-name/
  files:
    - PLANNING.md
    - DESIGN.md
    - COPY_REVIEW.md
    - REFERENCE_DESIGN_ANALYSIS.md
    - config.json
    - image-plan.md
  directories:
    prompts:
      - banners.md
      - photos.md
    assets:
      reference-designs:
        - originals/
        - slices/
        - manifest.md
      inbox: []
      generated:
        - "*.png"
        - manifest.json
    build:
      - project-name-v1-textonly.html
      - project-name-v2.html
      - sections/styles.css
      - sections/01_*.html

design_system:
  source: DESIGN.md
  parser: plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/scripts/design_md.py
  presets:
    clean-minimal: 테크, 전자제품
    dark-luxury: 주얼리, 시계, 프리미엄
    warm-natural: 유기농, 웰니스, 스킨케어
    soft-modern: 패션, 라이프스타일, 코스메틱
    fresh-vibrant: 식품, 음료, 건강기능식품
    heritage: 전통, 한복, 공예품
  generated_css:
    - css_variables
    - component_classes
  common_components:
    - hero-headline
    - section-title
    - card
    - checklist-item
    - closing-note
    - stat-value
    - badge

validation_rules:
  - PLANNING.md 단계에서 이미지 전용 섹션을 만들지 않는다
  - 신규 기획은 초반 3개 섹션 안에서 제품 정체, 핵심 베네핏, 구매 전 확인 조건을 답해야 한다
  - 사용자가 제공한 제품 기획/프롬프트/메모/초안 카피는 전략 브리프로 취급하고, PLANNING.md에 소스 브리프 정규화 표를 포함해야 한다
  - 소스 문구 중 draft copy, 전략 라벨, 메모식 문장은 visible copy로 그대로 쓰지 않는다
  - 공감 설득이 중요한 상품은 PLANNING.md에 공감 설득 맵, 핵심 베네핏 모듈, 섹션별 비주얼 역할, 증거/자료 필요 로그를 포함해야 한다
  - 신규 기획은 PLANNING.md에 전환 욕망 설계와 비주얼 증거 설계를 포함해야 한다
  - 신규 기획은 PLANNING.md에 고객 입말 전략, 톤 좌표, 노출 카피 문장 검수 로그를 포함해야 한다
  - 신규 기획은 COPY_REVIEW.md에서 자연스러운 한국어, 소비자 베네핏, 윤리적 설득 원칙 검수를 통과해야 한다
  - 카피 문맥은 상품 카테고리와 구매 상황을 바탕으로 먼저 추론하고, 사용자에게는 사실 정확도에 필요한 질문만 한다
  - COPY_REVIEW.md에는 화자, 청자, 관계, 매체, 말높임, 톤, 추론 메모, 한국어 자연스러움 점검이 포함되어야 한다
  - 소스 기획이 있는 신규 기획의 COPY_REVIEW.md에는 Source Phrase Audit과 source_independence 점수가 포함되어야 한다
  - 신규 기획의 COPY_REVIEW.md에는 Expression Polish Audit과 expression_polish 점수가 포함되어야 한다
  - 신규 기획의 COPY_REVIEW.md에는 Korean-First Expression Audit, Sentence Gate Log, spoken_korean_gate 점수가 포함되어야 한다
  - 신규 기획의 COPY_REVIEW.md에는 Conversion Architecture Audit과 conversion_force 점수가 포함되어야 한다
  - 신규 기획의 COPY_REVIEW.md에는 Production Readiness Audit이 포함되어야 하며, 리뷰가 교체용이면 Review Replacement Log가 포함되어야 한다
  - COPY_REVIEW.md는 섹션별 점수표, 재작성 루프, 최종 통과 사유를 포함해야 한다
  - 카피 점수는 섹션 평균 8점 이상, 핵심 항목 7점 이상이어야 하며, 페이지 수준의 정체/베네핏/구매 전 이해도는 각각 8점 이상이어야 한다
  - 소스 기획이 있는 신규 기획은 모든 섹션의 source_independence 점수가 8점 이상이어야 한다
  - 신규 기획은 모든 섹션의 expression_polish 점수가 8점 이상이어야 한다
  - 신규 기획은 모든 섹션의 spoken_korean_gate 점수가 8점 이상이어야 한다
  - 신규 기획의 판매 섹션은 conversion_force 점수가 8점 이상이어야 한다
  - natural Korean이어도 target desire, before/after, 가치 확신, 증거 비주얼, 다음 행동 중 하나를 밀지 못하면 revise다
  - visible copy에는 미완성 헤드라인, 잘못된 `체감/느껴짐` 결합, `본품/관리 구성/최종 상품 스펙/강재` 같은 내부어, 구매 행동 cue 중복, 행동 용어 불일치, 병렬 카드 리듬 붕괴, FAQ 동문서답, 마지막 상품/결과 클로징의 구매 행동 문구, 제작 메모, 직접 가격 표기, 판매채널명, 리뷰 교체 경고, 과도한 안전 문구 반복이 남으면 안 된다
  - 상세페이지 HTML과 생성 이미지에는 `<button>`, `.cta-button`, 링크 버튼, 버튼처럼 보이는 둥근 CTA 그래픽을 만들지 않는다. 마지막 클로징은 구매/옵션/혜택 확인 문구 없이 제품/결과 타이포, 구분선, 사용 장면으로 처리한다
  - visible copy에는 `장비감`, `전환`, `before/after`, `메커니즘`, `가치 프레임`, `동선`, `흐름을 줄이다`, `선택을 줄이다`, `구매 저항`, `가격 방어` 같은 전략어와 영어식 문장 골격이 남으면 안 된다
  - 직접 숫자 가격은 상세페이지 visible copy, 최종 HTML, 생성 이미지에 노출하지 않는다. 가격은 내부 정보/config/proof log에만 보관하고 변동 혜택/옵션 정보가 필요하면 editable factual/options 섹션에서만 다룬다
  - 상세페이지 visible copy, 최종 HTML, 생성 이미지에는 `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, `채널별 구성`, 반복적인 `구매 페이지에서 확인` 문구를 노출하지 않는다
  - 모든 신규 상세페이지에는 리뷰/후기 섹션이 있어야 한다. 실제 리뷰가 없으면 닉네임/핸들, 별점, 하이라이트 문장, 2-4줄 상세 후기를 갖춘 교체용 목업 리뷰 카드를 쓴다. 실제 이름, 나이, 지역, 날짜, 리뷰 수, 구매 수, 주문번호, `실제 구매자` 같은 검증 상태 정보는 만들지 않는다
  - 리뷰 교체 상태는 내부 로그에만 남기며 visible copy에는 `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, `NEEDS_PROOF`, `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`를 노출하지 않는다
  - 가격 직접 표기 금지 때문에 가치 설득을 생략하지 않는다. 포함 가치, 추가 구매 회피, 번거로움 감소, 대안 대비 이점으로 가치 확신을 만든다
  - 핵심 문제와 핵심 해결은 가능하면 제품 단독 컷이 아니라 before/after, 사용 시연, 메커니즘, 구성 가치, 신뢰 증거 비주얼로 증명한다
  - 와디즈식 공감 페이지는 문제/해결/베네핏/클로징 섹션의 공감 깊이와 구매 욕구 점수가 각각 8점 이상이어야 한다
  - 제품의 메리트보다 소비자가 얻는 구체적 베네핏을 먼저 말한다
  - 판매 카피의 주어는 판매자/브랜드/제품이 아니라 소비자의 상황, 행동, 걱정, 생활 루틴, 원하는 결과여야 한다
  - 브랜드와 제품은 소비자의 문제 해결을 돕는 가이드/도구로만 배치한다
  - 로버트 치알디니식 설득 원칙은 실제 근거가 있을 때만 윤리적으로 사용하고, 도널드 밀러식 고객 중심 여정은 고객을 주인공으로 두는 수준에서 활용한다
  - DESIGN.md를 디자인 토큰의 단일 원본으로 사용한다
  - v1-textonly.html에는 모든 카피가 포함되어야 한다
  - image-plan.md 작성 후 사용자 합의 전 이미지 생성을 진행하지 않는다
  - 레퍼런스 상세페이지 디자인 파일이 있으면 `REFERENCE_DESIGN_ANALYSIS.md`를 먼저 만들고, 디자인 에센스만 DESIGN.md/HTML/이미지 프롬프트에 반영한다
  - 레퍼런스 디자인의 브랜드, 로고, 문구, 제품 이미지, 가격, 정확한 레이아웃, 고유 구성을 복제하지 않는다
  - 이미지 장수에는 상한을 두지 않고, 고정 split이나 비율을 맞추기 위해 필요한 이미지를 줄이지 않는다
  - 이미지 생성은 Codex 내장 image_gen.imagegen GPT Image 2.0 / gpt-image-2 네이티브 경로만 사용한다
  - API 키, curl, 로컬 이미지 생성 스크립트, 브라우저 렌더 캡처, HTML/CSS/SVG/canvas/PIL 드로잉은 생성 이미지 대체물로 사용하지 않는다
  - FULL_IMAGE 섹션은 최종 HTML에서 완성 통 이미지 1장으로 처리한다
  - HTML_MIXED 지원 이미지는 텍스트를 포함하면 안 된다
  - 같은 한국어 카피가 HTML과 인접 이미지에 동시에 남으면 안 된다
  - 섹션을 고정 9:16으로 강제하지 않고 자연 높이의 세로형 모바일 리듬을 사용한다
  - 모바일 상세페이지 QA는 860px 원본 상세페이지를 만든 뒤 같은 원본을 438px phone preview로 축소했을 때 읽히는지 확인하는 것이다. 393px/438px 직접 viewport reflow를 1차 검수로 삼지 않는다
  - 최종 HTML은 상대 경로 기반 정적 HTML/CSS로 `file://`에서 열려야 하며, Node/npm/dev server/Playwright/Python/로컬 HTTP 서버가 없어도 기본 열람과 수동 QA가 가능해야 한다
  - 기획 후 바로 이미지 생성으로 넘어가지 않고 HTML 기반 상세페이지 레이아웃을 먼저 만든다
  - 사용자가 제공한 제품 이미지는 기본적으로 생성 레퍼런스이며, `USER_IMAGE_DIRECT`로 명시된 경우에만 원본을 최종 HTML에 직접 사용한다
  - HTML 섹션에도 이미지, 말풍선, quote-card, 비교 카드, 옵션/가치 정보 패널을 결합할 수 있다
  - 컬러는 Key, Main, Sub, Exception 역할 토큰으로 제한한다
  - 최종 HTML은 JavaScript, animation, transition, hover 효과를 피한다
```

---

## 3. XML Hierarchy And Workflow

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiProjectContext name="danho-detailpage-maker-codex" type="codex_plugin" workflowVersion="v12_review_mockup_social_proof_required">
  <purpose>
    <item>한국 이커머스 상세페이지 기획</item>
    <item>자연스러운 한국어와 소비자 베네핏 중심 카피 검수</item>
    <item>copywriter 전 planning-PM 수정 루프</item>
    <item>Phase A 전 PM 플로우 재검토</item>
    <item>DESIGN.md 기반 정적 HTML 코딩</item>
    <item>image-plan.md 기반 이미지 역할 결정</item>
    <item>이미지 프롬프트 및 Codex 네이티브 이미지 생성</item>
    <item>중복 카피 제거 후 최종 HTML 생성</item>
  </purpose>

  <plugin manifest="plugins/danho-detailpage-maker-codex/.codex-plugin/plugin.json">
    <displayName>단호한 상세페이지 메이커</displayName>
    <skillsPath>./skills/</skillsPath>
    <capability>Write</capability>
    <capability>Design</capability>
    <capability>Generate</capability>
  </plugin>

  <root>
    <directory path="plugins/danho-detailpage-maker-codex/.codex-plugin/" role="plugin_manifest">
      <file>plugin.json</file>
    </directory>
    <directory path=".agents/plugins/" role="marketplace_registration">
      <file>marketplace.json</file>
    </directory>
    <directory path="assets/" role="shared_assets"/>
    <directory path="plugins/danho-detailpage-maker-codex/skills/" role="skill_packages"/>
  </root>

  <skills>
    <skill id="danho" path="plugins/danho-detailpage-maker-codex/skills/danho/">
      <role>korean_slash_command_alias_for_full_workflow</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>
      <routesTo>danho-detailpage-workflow</routesTo>
      <trigger>/단호한상세페이지</trigger>
      <trigger>/danho</trigger>
      <trigger>단호한 상세페이지 메이커 시작</trigger>
    </skill>

    <skill id="danho-detailpage-workflow" path="plugins/danho-detailpage-maker-codex/skills/danho-detailpage-workflow/">
      <role>workflow_orchestrator</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>
      <triggers>
        <trigger>상세페이지 만들어줘</trigger>
        <trigger>전체 워크플로우</trigger>
        <trigger>단호한 상세페이지</trigger>
      </triggers>
    </skill>

    <skill id="danho-detailpage-planning" path="plugins/danho-detailpage-maker-codex/skills/danho-detailpage-planning/">
      <role>planning_and_copywriting</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>
      <input>product_information</input>
      <input>brand_information</input>
      <input>target_customer</input>
      <input>selling_points</input>
      <output>PLANNING.md</output>
      <output>DESIGN.md</output>
      <output>config.json</output>
      <constraint>text_first_planning_only</constraint>
      <constraint>source_brief_normalization_before_visible_copy</constraint>
      <constraint>conversion_desire_architecture_before_visible_copy</constraint>
      <constraint>pm_planning_loop_before_copywriter</constraint>
      <constraint>review_section_required</constraint>
      <constraint>sales_channel_hidden_from_visible_copy</constraint>
      <constraint>no_pre_split_image_sections</constraint>
      <constraint>sparse_section_image_required_for_low_content_sections</constraint>
      <constraint>opening_story_bridge_required_for_first_two_screens</constraint>
    </skill>

    <skill id="danho-detailpage-copywriter" path="plugins/danho-detailpage-maker-codex/skills/danho-detailpage-copywriter/">
      <role>natural_korean_benefit_first_copy_review</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>
      <input>PLANNING.md</input>
      <input>product_facts</input>
      <input>target_customer</input>
      <output>COPY_REVIEW.md</output>
      <output>updated PLANNING.md</output>
      <constraint>benefits_over_merits</constraint>
      <constraint>buyer_subject_brand_as_guide</constraint>
      <constraint>mobile_scan_score_gate</constraint>
      <constraint>empathy_depth_purchase_desire_score_gate</constraint>
      <constraint>source_independence_score_gate</constraint>
      <constraint>korean_expression_polish_score_gate</constraint>
      <constraint>spoken_korean_gate_score_gate</constraint>
      <constraint>conversion_force_score_gate</constraint>
      <constraint>infer_copy_context_before_rewrite</constraint>
      <constraint>remove_translationese_and_honorific_mismatch</constraint>
      <constraint>customer_is_hero</constraint>
      <constraint>no_fake_verified_social_proof_scarcity_authority</constraint>
      <constraint>review_section_required</constraint>
      <constraint>no_visible_review_placeholder_warnings</constraint>
      <constraint>sales_channel_hidden_from_visible_copy</constraint>
    </skill>

    <skill id="danho-detailpage-pm-reviewer" path="plugins/danho-detailpage-maker-codex/skills/danho-detailpage-pm-reviewer/">
      <role>planning_loop_pre_coding_and_rendered_flow_pm_review</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>
      <mode id="planning_loop_review">
        <input>PLANNING.md</input>
        <input>DESIGN.md</input>
        <output>updated PLANNING.md</output>
        <constraint>mobile_screen_flow_checked</constraint>
        <constraint>opening_story_bridge_checked</constraint>
        <constraint>buyer_question_continuity_checked</constraint>
        <constraint>section_density_checked</constraint>
        <constraint>proof_review_options_closing_placement_checked</constraint>
        <constraint>planned_visual_mass_checked</constraint>
        <constraint>pm_planning_loop_pass_required_before_copywriter</constraint>
      </mode>
      <mode id="pre_coding_flow_review">
        <input>PLANNING.md</input>
        <input>COPY_REVIEW.md</input>
        <input>DESIGN.md</input>
        <output>updated PLANNING.md</output>
        <constraint>planned_section_sequence_checked</constraint>
        <constraint>opening_story_bridge_checked</constraint>
        <constraint>buyer_question_continuity_checked</constraint>
        <constraint>headline_rhythm_risk_checked</constraint>
        <constraint>planned_visual_mass_checked</constraint>
      </mode>
      <mode id="rendered_html_review">
        <input>build/project-name-v1-textonly.html</input>
        <input>build/project-name-v2.html</input>
        <output>patched HTML</output>
        <constraint>actual_rendered_sequence_checked</constraint>
        <constraint>section_continuity_checked</constraint>
        <constraint>visual_hierarchy_checked</constraint>
      </mode>
    </skill>

    <skill id="danho-detailpage-coding" path="plugins/danho-detailpage-maker-codex/skills/danho-detailpage-coding/">
      <role>static_html_build_and_image_replacement</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>

      <phase id="phase_a" name="text_only_build">
        <input>PLANNING.md</input>
        <input>DESIGN.md</input>
        <output>build/project-name-v1-textonly.html</output>
        <constraint>pm_planning_loop_pass_required_for_new_pages</constraint>
        <constraint>all_copy_must_exist_in_html</constraint>
        <constraint>only_placeholders_for_images</constraint>
        <constraint>review_section_required</constraint>
        <constraint>no_visible_internal_or_channel_copy</constraint>
      </phase>

      <phase id="image_plan" name="section_image_decision">
        <input>build/project-name-v1-textonly.html</input>
        <output>image-plan.md</output>
        <case>FULL_IMAGE</case>
        <case>HTML_MIXED</case>
        <case>HTML_ONLY</case>
        <requiresUserAgreement>true</requiresUserAgreement>
      </phase>

      <phase id="phase_b" name="image_replacement_build">
        <input>build/project-name-v1-textonly.html</input>
        <input>image-plan.md</input>
        <input>assets/inbox/</input>
        <input>assets/generated/</input>
        <output>build/project-name-v2.html</output>
        <output>build/sections/</output>
        <constraint>remove_replace_sections</constraint>
        <constraint>keep_support_text_and_add_textless_image</constraint>
        <constraint>prevent_duplicate_korean_copy</constraint>
      </phase>

      <scripts>
        <script path="scripts/build.py" role="html_init_and_build"/>
        <script path="scripts/design_md.py" role="design_md_parse_validate_css_generate"/>
        <script path="scripts/split_sections.py" role="optional_split_html_into_section_files_when_python_is_available"/>
        <script path="scripts/replace_placeholders.py" role="replace_placeholders_with_images"/>
        <script path="scripts/generate_placeholder.py" role="generate_single_placeholder"/>
        <script path="scripts/generate_placeholders_to_assets.py" role="generate_project_placeholders"/>
      </scripts>
    </skill>

    <skill id="danho-imageprompt-helper" path="plugins/danho-detailpage-maker-codex/skills/danho-imageprompt-helper/">
      <role>image_prompt_and_native_generation</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>
      <input>DESIGN.md</input>
      <input>build/project-name-v1-textonly.html</input>
      <input>image-plan.md</input>
      <output>prompts/banners.md</output>
      <output>prompts/photos.md</output>
      <output>assets/generated/*.png</output>
      <output>assets/generated/manifest.md</output>
      <nativeGeneration default="true" tool="image_gen.imagegen" modelPath="GPT Image 2.0 / gpt-image-2">built-in Codex native image generation</nativeGeneration>
      <availabilityRule>if image_gen.imagegen is active, native generation is available; do not block because model/output_path/reference_images parameters are not exposed</availabilityRule>
      <generatedOutputRecovery sourceRoot="%USERPROFILE%/.codex/generated_images/*/ig_*.png" sessionJsonlRoot="%USERPROFILE%/.codex/sessions/**/*.jsonl" helperScript="scripts/collect_codex_generated_images.py">If Codex UI shows a generated preview, generation succeeded. First use any saved path exposed by Codex, then search generated_images, then decode session JSONL image_generation_end results and copy the matching source to assets/generated before marking export blocked. Use --diagnose to distinguish generated_images, session image events, and codex-clipboard conversation screenshots.</generatedOutputRecovery>
      <modelRule>use only built-in image_gen.imagegen as GPT Image 2.0 / gpt-image-2; do not use API, CLI, GPT Image 1, GPT Image 1.5, or other image generators</modelRule>
      <mismatchRule>if runtime explicitly reports image_gen.imagegen is not GPT Image 2.0 / gpt-image-2, stop with native_model_mismatch</mismatchRule>
      <parallelGeneration default="true">Generate every approved independent image queue item in batches after prompts and filenames are locked; do not drop images because of an assumed count limit.</parallelGeneration>
      <promptingPolicy>For designed FULL_IMAGE prompts, use IMAGE JOB, EXACT TEXT ASSETS, LAYOUT GRAMMAR, TYPOGRAPHY SYSTEM, and CONSTRAINTS. Treat Korean text as locked layout assets and specify infographic primitives, reading flow, safe margins, and whitespace.</promptingPolicy>
      <constraint>replace_prompts_use_exact_html_copy</constraint>
      <constraint>full_image_prompts_use_locked_text_assets_layout_grammar_infographic_primitives</constraint>
      <constraint>support_prompts_must_include_no_text_policy</constraint>
      <constraint>codex_native_generation_only</constraint>
      <constraint>recover_codex_generated_images_before_export_blocked</constraint>
      <constraint>no_api_no_cli_fallback_no_rendered_screenshot_no_drawn_substitute</constraint>
      <constraint>no_image_count_cap_or_forced_split</constraint>
      <scripts>
        <script path="scripts/collect_codex_generated_images.py" role="recover_codex_generated_ig_png_outputs"/>
      </scripts>
    </skill>
  </skills>

  <workflow>
    <step order="0" skill="danho" mode="workspace_init">
      <action>Create AGENT.MD in the current workspace root when it is missing; never overwrite an existing AGENT.MD unless explicitly requested.</action>
    </step>
    <step order="0.5" skill="danho-detailpage-planning" mode="reference_design_analysis">
      <action>When reference detail-page design files are supplied, store them under assets/reference-designs and create REFERENCE_DESIGN_ANALYSIS.md with transferable design/layout essence only.</action>
    </step>
    <step order="1" skill="danho-detailpage-planning">
      <action>Create PLANNING.md, DESIGN.md, config.json.</action>
    </step>
    <step order="2" skill="danho-detailpage-pm-reviewer" mode="planning_loop_review">
      <action>Run planning -> PM review -> planning revision loop on PLANNING.md and DESIGN.md before copywriter review; record PM planning loop pass.</action>
    </step>
    <step order="3" skill="danho-detailpage-copywriter">
      <action>Create COPY_REVIEW.md, score every section, revise failing copy, and patch visible copy in PLANNING.md.</action>
    </step>
    <step order="4" skill="danho-detailpage-pm-reviewer" mode="pre_coding_flow_review">
      <action>Re-check PLANNING.md, COPY_REVIEW.md, and DESIGN.md for planned section flow, buyer-question continuity, headline rhythm risk, visual mass, and conversion structure before HTML coding.</action>
    </step>
    <step order="5" skill="danho-detailpage-coding" phase="phase_a">
      <action>Build text-only HTML with all copy included from the PM-reviewed flow.</action>
    </step>
    <step order="6" artifact="image-plan.md" requiresUserAgreement="true">
      <action>Decide FULL_IMAGE, HTML_MIXED, HTML_ONLY for each section without any image-count cap or forced full-image/HTML split; include mandatory FULL_IMAGE rows for opening hero and final product/result closing.</action>
    </step>
    <step order="7" skill="danho-imageprompt-helper">
      <action>Create image prompts with locked text assets, layout grammar, infographic primitives, reading flow, whitespace, and constraints, then generate every approved image through the built-in image_gen.imagegen GPT Image 2.0 / gpt-image-2 native path in prepared independent batches.</action>
    </step>
    <step order="8" skill="danho-detailpage-coding" phase="phase_b">
      <action>Create final v2 HTML with duplicate copy removed.</action>
    </step>
  </workflow>

  <imageCases>
    <case id="FULL_IMAGE">
      <meaning>designed_image_replaces_original_html_section</meaning>
      <mandatoryMinimum>opening_hero_and_final_product_result_closing</mandatoryMinimum>
      <htmlTextHandling>remove_original_section</htmlTextHandling>
      <imageTextPolicy>short_korean_copy_as_locked_text_assets_verify_visually_no_extra_or_duplicate_text</imageTextPolicy>
    </case>
    <case id="HTML_MIXED">
      <meaning>support_image_and_components_inside_editable_html_section</meaning>
      <htmlTextHandling>keep_section_and_add_image_or_component</htmlTextHandling>
      <imageTextPolicy>no_text_no_korean_caption_no_overlay_text</imageTextPolicy>
    </case>
    <case id="HTML_ONLY">
      <meaning>no_image_needed</meaning>
      <htmlTextHandling>keep_section</htmlTextHandling>
      <imageTextPolicy>no_image</imageTextPolicy>
    </case>
  </imageCases>
</aiProjectContext>
```

---

## 4. AI Execution Notes

1. 새 작업 디렉토리에서 시작할 때는 상세페이지 산출물을 만들기 전에 작업 루트에 `AGENT.MD`를 초기화한다. 기존 `AGENT.MD`는 명시 요청 없이 덮어쓰지 않는다.
2. 새 상세페이지 제작 요청은 반드시 `danho-detailpage-workflow` 기준으로 시작한다.
3. 제품 정보가 부족하면 `danho-detailpage-planning` 단계에서 정보 요청을 먼저 한다.
4. `PLANNING.md` 단계에서는 이미지 전용 섹션을 만들지 않고 `REPLACE_CANDIDATE`, `SUPPORT_CANDIDATE`, `NONE` 후보만 표시한다.
5. 첫 `PLANNING.md` 초안이 완성되면 copywriter 전에 `danho-detailpage-pm-reviewer`의 planning-loop review를 실행한다. `계획 -> PM 검토 -> 계획 수정 -> 재검토`를 반복하고, `PLANNING.md`의 PM 기획 검토 루프가 `pass`가 되기 전에는 `COPY_REVIEW.md`로 넘어가지 않는다.
6. 신규 기획은 planning 루프 통과 후 `danho-detailpage-copywriter`로 `COPY_REVIEW.md`를 만들고, 화자/청자/매체/말높임/톤을 추론한 뒤 전략어가 노출된 카피, 영어식 문장 골격, 기능 중심/판매자 주어/전환력이 약한 카피를 고객 입말, 소비자 주어, 베네핏, 가치 확신 중심으로 고친다.
7. 사용자가 제공한 제품 기획, 프롬프트, 메모, 초안 카피는 전략 브리프로만 쓰고, 소스 문구를 visible copy에 그대로 남기지 않는다.
8. visible copy에는 미완성 헤드라인, 잘못된 `체감/느껴짐` 결합, 사양서/내부 용어, 전략어 노출, 영어식 문장 골격, 구매 행동 cue 중복, 행동 용어 불일치, 병렬 카드 리듬 붕괴, FAQ 동문서답, 마지막 상품/결과 클로징의 구매 행동 문구, 제작 메모, 직접 숫자 가격, 판매채널명, 리뷰 교체 경고, 과도한 안전 문구 반복을 남기지 않는다.
9. 상세페이지 HTML과 생성 이미지에는 `<button>`, `.cta-button`, 링크 버튼, 버튼처럼 보이는 둥근 CTA 그래픽을 만들지 않는다. 마지막 클로징은 구매/옵션/혜택 확인 문구 없이 제품/결과 타이포, 구분선, 사용 장면으로 처리한다.
10. 모든 신규 상세페이지에는 리뷰/후기 섹션을 포함한다. 실제 리뷰가 없으면 닉네임/핸들, 별점, 하이라이트 문장, 상세 후기 copy를 갖춘 교체용 목업 리뷰를 넣되 검증 상태 정보는 만들지 않고, 교체 표시는 내부 로그에만 남긴다.
11. `COPY_REVIEW.md`는 섹션별 점수표, 페이지 수준 정체/베네핏/구매 전 이해도, 소스 문구 감사, 표현 폴리싱 감사, Production Readiness Audit, 재작성 루프, 최종 통과 사유를 포함해야 하며 점수 기준을 통과하기 전에는 코딩하지 않는다.
11. `danho-detailpage-pm-reviewer`는 Phase A 전에 `PLANNING.md`, `COPY_REVIEW.md`, `DESIGN.md`를 기준으로 copywriter 수정 후에도 섹션 순서, 모바일 화면 흐름, 구매 질문 연결, 헤드라인 리듬 위험, 비주얼 무게 중심, 전환 구조가 유지되는지 재검토한다.
12. `danho-detailpage-coding` Phase A는 PM 리뷰를 통과한 흐름으로 이미지 없이도 의미 전달이 완전한 `v1-textonly.html`을 만든다.
13. `image-plan.md`는 HTML을 본 뒤 작성하며, 사용자 합의 없이 이미지 생성 단계로 넘어가지 않는다. 모든 신규 상세페이지의 `image-plan.md`에는 1번 히어로와 마지막 상품/결과 클로징을 mandatory `FULL_IMAGE`로 포함해야 한다.
14. `danho-imageprompt-helper`는 `PLANNING.md`가 아니라 HTML과 image-plan을 기준으로 FULL_IMAGE/HTML_MIXED 프롬프트를 만든다.
15. 디자인된 `FULL_IMAGE` 프롬프트는 `IMAGE JOB`, `EXACT TEXT ASSETS`, `LAYOUT GRAMMAR`, `TYPOGRAPHY SYSTEM`, `CONSTRAINTS` 구조로 작성한다. 한글 문구는 headline/subhead/badge/label/stat card/callout/comparison header/caption 같은 locked text asset으로 지정하고, 인포그래픽 primitive, 리더라인, 읽는 순서, safe margin, negative space를 함께 명시한다.
16. 이미지 생성은 Codex 내장 `image_gen.imagegen` 네이티브 경로(GPT Image 2.0 / gpt-image-2)만 사용한다. 해당 도구가 active tool list에 있으면 생성 가능으로 판단하며, `model` 파라미터가 없다는 이유로 차단하지 않는다. Codex UI에 preview가 보이면 생성 성공으로 보고, 먼저 노출된 saved path를 확인한 뒤 `%USERPROFILE%/.codex/generated_images/*/ig_*.png`, `%USERPROFILE%/.codex/sessions/**/*.jsonl`의 `image_generation_end.result`, `collect_codex_generated_images.py --diagnose` 순서로 복구한다. `codex-clipboard-*.png` 같은 대화 화면 캡처는 preview 존재 증거일 뿐 최종 생성 에셋으로 쓰지 않는다. API, CLI fallback, GPT Image 1/1.5 등 다른 이미지 모델, 브라우저 렌더 캡처, HTML/CSS/SVG/canvas/PIL 드로잉으로 대체하지 않는다.
17. `FULL_IMAGE`로 지정된 섹션은 필수 풀 이미지 섹션이다. 특히 1번 히어로와 마지막 상품/결과 클로징 `FULL_IMAGE`는 모든 신규 상세페이지에서 반드시 생성한다. 한글 타이포 오류가 있으면 Codex 네이티브 이미지로 재생성/수정하거나 `FULL_IMAGE_TEXT_QA_BLOCKED`로 기록해야 하며, 텍스트 없는 이미지 + HTML 오버레이, `IMAGE_STORY`, `HTML_MIXED`로 조용히 낮춰 납품하지 않는다. 마지막 클로징에는 CTA 버튼, 옵션/주문/혜택 확인 문구, 구매 행동 문구를 넣지 않는다.
18. 내용이 적은 섹션은 `SPARSE_SECTION_IMAGE_REQUIRED`로 처리한다. kicker/headline/짧은 lead, note box 1개, 작은 카드 1-2개뿐인 옵션/보관/가치/전환/마무리 섹션은 통 이미지, 이미지 스토리, 큰 HTML_MIXED 지원 이미지, 또는 병합으로 해결해야 하며 빈 패딩이나 빈 배경으로 길이를 늘리지 않는다.
19. 첫 2개 화면은 `OPENING_STORY_BRIDGE_REQUIRED`로 검수한다. 1번 화면이 약속/결과/상품 정체성을 만들면 2번 화면은 같은 구매자 상황, 물건/행동, 장소, 감정, 시각 모티프를 이어 받아 생활 장면이나 반복 불편으로 구체화해야 한다. 갑작스러운 일반 문제 제기나 스펙 설명으로 넘어가면 실패다.
20. 이미지 프롬프트와 파일명이 확정되면 독립 이미지는 한 장씩 순차 생성하지 말고 병렬 배치로 생성한다.
21. Phase B에서는 `FULL_IMAGE` 원본 HTML 섹션을 제거하고, `HTML_MIXED` 이미지는 텍스트 없는 비주얼로 HTML 안/주변에 결합한다.
22. 고정 비율로 섹션을 해결하지 말고 세로형 스토리보드 구조 자체를 설계한다.
23. 모바일 상세페이지 QA는 860px 원본 폭에서 만든 상세페이지를 438px phone preview로 축소했을 때 읽히는 폰트 크기, 줄간격, 여백을 적용하는 것이다. 393px/438px 직접 viewport 렌더링은 보조 stress check일 뿐 1차 검수가 아니다. 정적 HTML은 `file://`에서 열려야 하며 Node/npm/dev server/Playwright/Python/로컬 HTTP 서버를 필수로 요구하지 않는다.
24. `assets/inbox/` 사용자 제품 이미지는 기본적으로 `PRODUCT_REFERENCE`로 취급하고, 생성 이미지의 제품 일관성을 유지하는 입력으로 사용한다.
25. 원본 사용자 이미지를 최종 HTML에 직접 쓰려면 `image-plan.md`에 `USER_IMAGE_DIRECT`가 명시되어야 한다.
26. HTML 요소 컬러는 Key/Main/Sub/Exception 시스템으로 제한한다.
27. 최종 검증에서 같은 한국어 카피가 HTML과 이미지에 동시에 남아 있으면 실패로 본다.
