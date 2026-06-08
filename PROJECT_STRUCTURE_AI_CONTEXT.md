# Danho Detailpage Maker Codex - AI Parsing Context

> 이 문서는 AI 에이전트가 프로젝트 구조와 실행 흐름을 빠르게 파싱하도록 만든 단일 혼합 포맷 문서다.
> Markdown은 사람이 읽는 요약, YAML은 정규화된 데이터, XML은 계층 관계와 워크플로우 경계를 표현한다.

## 1. Human Summary

`danho-detailpage-maker-codex`는 한국 이커머스 상세페이지를 기획, 코딩, 이미지 제작까지 진행하는 Codex 플러그인 프로젝트다.

핵심 방식은 `v4 hybrid detail workflow`다. 먼저 `PLANNING.md`와 `DESIGN.md`로 카피와 설득 흐름을 확정하고, HTML에서는 모바일 세로형 스토리 구조를 만든다. 이후 `image-plan.md`에서 각 섹션을 `FULL_IMAGE`, `HTML_MIXED`, `HTML_ONLY`로 확정한다. legacy 용어로는 각각 `REPLACE`, `SUPPORT`, `NONE`에 대응한다. 최종 페이지는 통 이미지 섹션과 HTML+이미지 혼합 섹션을 함께 사용하며, 같은 한국어 카피가 이미지와 HTML에 중복 노출되지 않게 한다.

### Root Layout

```text
danho-detailpage-maker-codex/
├── .codex-plugin/
│   └── plugin.json
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── assets/
└── skills/
    ├── danho-detailpage-workflow/
    ├── danho-detailpage-planning/
    ├── danho-detailpage-coding/
    └── danho-imageprompt-helper/
```

### Main Skills

| Skill | Purpose | Primary Outputs |
|---|---|---|
| `danho-detailpage-workflow` | 전체 제작 흐름 오케스트레이션 | 다음 실행 단계 판단 |
| `danho-detailpage-planning` | 상세페이지 기획 및 카피 작성 | `PLANNING.md`, `DESIGN.md`, `config.json` |
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
  manifest: .codex-plugin/plugin.json
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
    path: ./
  policy:
    installation: AVAILABLE
    authentication: ON_INSTALL
  category: Productivity

directories:
  root:
    .codex-plugin/:
      role: plugin_manifest_directory
      contains:
        - plugin.json
    .agents/plugins/:
      role: local_marketplace_registration
      contains:
        - marketplace.json
    assets/:
      role: root_shared_assets
      current_state: empty
    skills/:
      role: skill_packages
      contains:
        - danho-detailpage-workflow
        - danho-detailpage-planning
        - danho-detailpage-coding
        - danho-imageprompt-helper

skills:
  danho-detailpage-workflow:
    path: skills/danho-detailpage-workflow/
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
      - if: PLANNING.md_and_DESIGN.md_exist_and_approved
        run: danho-detailpage-coding.phase_a
      - if: v1_textonly_exists_and_image_plan_missing
        run: create_image_plan
      - if: image_plan_exists_and_user_wants_prompts_or_images
        run: danho-imageprompt-helper
      - if: generated_or_inbox_images_available_and_plan_approved
        run: danho-detailpage-coding.phase_b

  danho-detailpage-planning:
    path: skills/danho-detailpage-planning/
    skill_file: SKILL.md
    agent_file: agents/openai.yaml
    role: 한국 이커머스 상세페이지 기획과 설득 카피 작성
    implicit_invocation: true
    required_inputs:
      critical:
        - product_name
        - price
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
    outputs:
      - projects/MMDDHHmm_project-name/PLANNING.md
      - projects/MMDDHHmm_project-name/DESIGN.md
      - projects/MMDDHHmm_project-name/config.json
    references:
      - references/korean-headline-rules.md
      - references/product-naming-consistency.md
      - references/section-library.md
      - references/genre-composition.md
      - references/image-guidelines.md
      - references/persuasion-framework.md
      - references/output-format.md
      - references/copy-templates.md
    rule:
      planning_must_be_text_first: true
      image_slots_are_forbidden_in_planning: true
      only_mark_image_candidates: true

  danho-detailpage-coding:
    path: skills/danho-detailpage-coding/
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
        legacy_case_mapping:
          FULL_IMAGE: REPLACE
          HTML_MIXED: SUPPORT
          HTML_ONLY: NONE
        requires_user_agreement: true
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
        path: skills/danho-detailpage-coding/scripts/build.py
        role: DESIGN.md 기반 HTML 초기화 및 섹션 병합 빌드
      design_md.py:
        path: skills/danho-detailpage-coding/scripts/design_md.py
        role: DESIGN.md 파싱, 검증, CSS variables와 component class 생성
      split_sections.py:
        path: skills/danho-detailpage-coding/scripts/split_sections.py
        role: 완성 HTML을 섹션별 파일과 CSS로 분리
      replace_placeholders.py:
        path: skills/danho-detailpage-coding/scripts/replace_placeholders.py
        role: placeholder를 실제 이미지로 치환
      generate_placeholder.py:
        path: skills/danho-detailpage-coding/scripts/generate_placeholder.py
        role: 단일 placeholder 이미지 생성
      generate_placeholders_to_assets.py:
        path: skills/danho-detailpage-coding/scripts/generate_placeholders_to_assets.py
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
    path: skills/danho-imageprompt-helper/
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
    scripts:
      generate_banner.py:
        path: skills/danho-imageprompt-helper/scripts/generate_banner.py
        role: legacy API fallback only, not the default generation path
        requires_explicit_user_request: true
    native_generation:
      default: true
      engine: Codex native image generation
      output_directory: assets/generated/
      manifest: assets/generated/manifest.md
      product_reference_policy:
        default: assets/inbox images are PRODUCT_REFERENCE
        direct_use_requires: USER_IMAGE_DIRECT in image-plan.md
        generated_outputs: assets/generated/
    references:
      - references/prompt-guide.md
      - references/native-image-generation.md
      - references/product-reference-images.md

workflow:
  version: v4_hybrid_detail
  copy_source_of_truth: build/project-name-v1-textonly.html
  strict_sequence:
    - order: 1
      skill: danho-detailpage-planning
      action: 제품 정보로 PLANNING.md, DESIGN.md, config.json 생성
    - order: 2
      skill: danho-detailpage-coding
      phase: phase_a
      action: 텍스트만으로 완전한 v1 HTML 생성
    - order: 3
      artifact: image-plan.md
      action: 섹션별 FULL_IMAGE, HTML_MIXED, HTML_ONLY 결정
      stop_for_user_agreement: true
    - order: 4
      skill: danho-imageprompt-helper
      action: 이미지 프롬프트 작성 후 Codex 네이티브 이미지 생성 큐를 병렬 배치로 처리
    - order: 5
      skill: danho-detailpage-coding
      phase: phase_b
      action: image-plan.md에 따라 v2 HTML 생성

image_cases:
  FULL_IMAGE:
    legacy_name: REPLACE
    meaning: 이미지 모델이 만든 완성 통 이미지가 HTML 레이아웃을 대체
    html_text_handling: remove_original_section
    image_policy: 짧은 한글 카피와 디자인 요소를 이미지 안에 포함 가능
    duplicate_copy_allowed: false
    typical_sections:
      - hook
      - scene-problem
      - blocker
      - answer
      - no-damage
      - daily-use
      - control
      - final-cta
  HTML_MIXED:
    legacy_name: SUPPORT
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
    legacy_name: NONE
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
    - config.json
    - image-plan.md
  directories:
    prompts:
      - banners.md
      - photos.md
    assets:
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
  parser: skills/danho-detailpage-coding/scripts/design_md.py
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
    - cta-button
    - stat-value
    - badge

validation_rules:
  - PLANNING.md 단계에서 이미지 전용 섹션을 만들지 않는다
  - DESIGN.md를 디자인 토큰의 단일 원본으로 사용한다
  - v1-textonly.html에는 모든 카피가 포함되어야 한다
  - image-plan.md 작성 후 사용자 합의 전 이미지 생성을 진행하지 않는다
  - FULL_IMAGE 섹션은 최종 HTML에서 완성 통 이미지 1장으로 처리한다
  - HTML_MIXED 지원 이미지는 텍스트를 포함하면 안 된다
  - 같은 한국어 카피가 HTML과 인접 이미지에 동시에 남으면 안 된다
  - 섹션을 고정 9:16으로 강제하지 않고 자연 높이의 세로형 모바일 리듬을 사용한다
  - 모바일 우선은 413px 고정 폭이 아니라 360-430px phone width에서 읽히는 반응형 타이포그래피를 의미한다
  - 기획 후 바로 이미지 생성으로 넘어가지 않고 HTML 기반 상세페이지 레이아웃을 먼저 만든다
  - 사용자가 제공한 제품 이미지는 기본적으로 생성 레퍼런스이며, `USER_IMAGE_DIRECT`로 명시된 경우에만 원본을 최종 HTML에 직접 사용한다
  - HTML 섹션에도 이미지, 말풍선, quote-card, 비교 카드, 가격 패널을 결합할 수 있다
  - 컬러는 Key, Main, Sub, Exception 역할 토큰으로 제한한다
  - 최종 HTML은 JavaScript, animation, transition, hover 효과를 피한다
```

---

## 3. XML Hierarchy And Workflow

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiProjectContext name="danho-detailpage-maker-codex" type="codex_plugin" workflowVersion="v4_hybrid_detail">
  <purpose>
    <item>한국 이커머스 상세페이지 기획</item>
    <item>DESIGN.md 기반 정적 HTML 코딩</item>
    <item>image-plan.md 기반 이미지 역할 결정</item>
    <item>이미지 프롬프트 및 Codex 네이티브 이미지 생성</item>
    <item>중복 카피 제거 후 최종 HTML 생성</item>
  </purpose>

  <plugin manifest=".codex-plugin/plugin.json">
    <displayName>단호한 상세페이지 메이커</displayName>
    <skillsPath>./skills/</skillsPath>
    <capability>Write</capability>
    <capability>Design</capability>
    <capability>Generate</capability>
  </plugin>

  <root>
    <directory path=".codex-plugin/" role="plugin_manifest">
      <file>plugin.json</file>
    </directory>
    <directory path=".agents/plugins/" role="marketplace_registration">
      <file>marketplace.json</file>
    </directory>
    <directory path="assets/" role="shared_assets"/>
    <directory path="skills/" role="skill_packages"/>
  </root>

  <skills>
    <skill id="danho-detailpage-workflow" path="skills/danho-detailpage-workflow/">
      <role>workflow_orchestrator</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>
      <triggers>
        <trigger>상세페이지 만들어줘</trigger>
        <trigger>전체 워크플로우</trigger>
        <trigger>단호한 상세페이지</trigger>
      </triggers>
    </skill>

    <skill id="danho-detailpage-planning" path="skills/danho-detailpage-planning/">
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
      <constraint>no_pre_split_image_sections</constraint>
    </skill>

    <skill id="danho-detailpage-coding" path="skills/danho-detailpage-coding/">
      <role>static_html_build_and_image_replacement</role>
      <file type="skill">SKILL.md</file>
      <file type="agent">agents/openai.yaml</file>

      <phase id="phase_a" name="text_only_build">
        <input>PLANNING.md</input>
        <input>DESIGN.md</input>
        <output>build/project-name-v1-textonly.html</output>
        <constraint>all_copy_must_exist_in_html</constraint>
        <constraint>only_placeholders_for_images</constraint>
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
        <script path="scripts/split_sections.py" role="split_html_into_section_files"/>
        <script path="scripts/replace_placeholders.py" role="replace_placeholders_with_images"/>
        <script path="scripts/generate_placeholder.py" role="generate_single_placeholder"/>
        <script path="scripts/generate_placeholders_to_assets.py" role="generate_project_placeholders"/>
      </scripts>
    </skill>

    <skill id="danho-imageprompt-helper" path="skills/danho-imageprompt-helper/">
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
      <nativeGeneration default="true">Codex native image generation</nativeGeneration>
      <parallelGeneration default="true">Generate approved independent image queue in batches after prompts and filenames are locked.</parallelGeneration>
      <script path="scripts/generate_banner.py" mode="legacy_fallback" requiresExplicitUserRequest="true"/>
      <constraint>replace_prompts_use_exact_html_copy</constraint>
      <constraint>support_prompts_must_include_no_text_policy</constraint>
    </skill>
  </skills>

  <workflow>
    <step order="1" skill="danho-detailpage-planning">
      <action>Create PLANNING.md, DESIGN.md, config.json.</action>
    </step>
    <step order="2" skill="danho-detailpage-coding" phase="phase_a">
      <action>Build text-only HTML with all copy included.</action>
    </step>
    <step order="3" artifact="image-plan.md" requiresUserAgreement="true">
      <action>Decide FULL_IMAGE, HTML_MIXED, HTML_ONLY for each section.</action>
    </step>
    <step order="4" skill="danho-imageprompt-helper">
      <action>Create image prompts and generate approved images through Codex native image generation in parallel batches.</action>
    </step>
    <step order="5" skill="danho-detailpage-coding" phase="phase_b">
      <action>Create final v2 HTML with duplicate copy removed.</action>
    </step>
  </workflow>

  <imageCases>
    <case id="FULL_IMAGE" legacy="REPLACE">
      <meaning>designed_image_replaces_original_html_section</meaning>
      <htmlTextHandling>remove_original_section</htmlTextHandling>
      <imageTextPolicy>short_korean_copy_allowed_verify_visually</imageTextPolicy>
    </case>
    <case id="HTML_MIXED" legacy="SUPPORT">
      <meaning>support_image_and_components_inside_editable_html_section</meaning>
      <htmlTextHandling>keep_section_and_add_image_or_component</htmlTextHandling>
      <imageTextPolicy>no_text_no_korean_caption_no_overlay_text</imageTextPolicy>
    </case>
    <case id="HTML_ONLY" legacy="NONE">
      <meaning>no_image_needed</meaning>
      <htmlTextHandling>keep_section</htmlTextHandling>
      <imageTextPolicy>no_image</imageTextPolicy>
    </case>
  </imageCases>
</aiProjectContext>
```

---

## 4. AI Execution Notes

1. 새 상세페이지 제작 요청은 반드시 `danho-detailpage-workflow` 기준으로 시작한다.
2. 제품 정보가 부족하면 `danho-detailpage-planning` 단계에서 정보 요청을 먼저 한다.
3. `PLANNING.md` 단계에서는 이미지 전용 섹션을 만들지 않고 `REPLACE_CANDIDATE`, `SUPPORT_CANDIDATE`, `NONE` 후보만 표시한다.
4. `danho-detailpage-coding` Phase A는 이미지 없이도 의미 전달이 완전한 `v1-textonly.html`을 만든다.
5. `image-plan.md`는 HTML을 본 뒤 작성하며, 사용자 합의 없이 이미지 생성 단계로 넘어가지 않는다.
6. `danho-imageprompt-helper`는 `PLANNING.md`가 아니라 HTML과 image-plan을 기준으로 FULL_IMAGE/HTML_MIXED 프롬프트를 만든다.
7. 이미지 생성은 기본적으로 Codex 네이티브 이미지 생성 기능을 사용한다. `generate_banner.py`는 사용자가 명시적으로 API fallback을 요청한 경우에만 사용한다.
8. 이미지 프롬프트와 파일명이 확정되면 독립 이미지는 한 장씩 순차 생성하지 말고 병렬 배치로 생성한다.
9. Phase B에서는 `FULL_IMAGE` 원본 HTML 섹션을 제거하고, `HTML_MIXED` 이미지는 텍스트 없는 비주얼로 HTML 안/주변에 결합한다.
10. 고정 비율로 섹션을 해결하지 말고 세로형 스토리보드 구조 자체를 설계한다.
11. 모바일 우선은 413px 고정이 아니라 360-430px 폭에서 읽히는 폰트 크기, 줄간격, 여백을 적용하는 것이다.
12. `assets/inbox/` 사용자 제품 이미지는 기본적으로 `PRODUCT_REFERENCE`로 취급하고, 생성 이미지의 제품 일관성을 유지하는 입력으로 사용한다.
13. 원본 사용자 이미지를 최종 HTML에 직접 쓰려면 `image-plan.md`에 `USER_IMAGE_DIRECT`가 명시되어야 한다.
14. HTML 요소 컬러는 Key/Main/Sub/Exception 시스템으로 제한한다.
15. 최종 검증에서 같은 한국어 카피가 HTML과 이미지에 동시에 남아 있으면 실패로 본다.
