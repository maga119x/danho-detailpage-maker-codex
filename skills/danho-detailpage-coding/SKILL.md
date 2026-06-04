---
name: danho-detailpage-coding
description: Convert approved planning documents into static HTML for Korean e-commerce product detail pages (상세페이지 코딩). Phase A는 텍스트-온리 HTML 빌드, Phase B는 image-plan.md에 따라 이미지를 반영. Use when user has an approved content plan and DESIGN.md, and needs HTML/CSS implementation. Triggers on "상세페이지 코딩", "HTML로 만들어줘", "기획서 코딩", "상세페이지 퍼블리싱".
---

# Korean Product Detail Page Coding (v3 Text-First, DESIGN.md 기반)

PLANNING.md(기획서) + DESIGN.md(디자인 시스템)를 입력으로 받아 한국 이커머스용 정적 HTML/CSS를 생성한다.

**v3 핵심 원칙**: 코딩은 두 페이즈로 분리한다.
- **Phase A (텍스트-온리 빌드)**: 모든 카피가 HTML에 들어간 완전한 페이지를 먼저 만든다. 이미지 슬롯은 placeholder.
- **Phase B (이미지 대체 빌드)**: image-plan.md의 결정에 따라 이미지를 반영한다. REPLACE 케이스의 HTML 텍스트는 이 시점에 제거된다.

> 🚨 **왜 이렇게 바뀌었나**: v2에서는 PLANNING.md의 같은 카피가 이미지 안 텍스트와 HTML `<h1>`에 둘 다 들어가 인접한 위치에 중복 노출됐다. v3은 HTML을 single source of truth로 두고, 이미지가 그 카피를 "대체"하거나 "보조"하는 방식으로 역할을 분리한다.
> 상세: [text-image-deduplication.md](references/text-image-deduplication.md)

**이 스킬은 입력으로 다음을 요구합니다:**

### Phase A 입력
1. **PLANNING.md** — 섹션 콘텐츠 (planning 스킬 출력, 이미지 슬롯 분리 없음)
2. **DESIGN.md** — 디자인 시스템

### Phase B 입력 (추가)
3. **image-plan.md** — 섹션별 REPLACE/SUPPORT/NONE 결정
4. **assets/generated/** + **assets/inbox/** — Codex 네이티브 생성 또는 사용자가 제공한 실제 이미지 파일

콘텐츠 기획은 `danho-detailpage-planning` 스킬을 먼저 실행하세요.

명령 예시의 `<danho-detailpage-coding-skill-dir>`는 이 `SKILL.md`가 들어 있는 실제 디렉터리로 치환하세요. 플러그인 설치 위치는 환경마다 달라질 수 있으므로 전역 고정 경로를 가정하지 않습니다.

---

## 디자인 시스템: DESIGN.md (Google Stitch alpha 스펙)

**기존 `theme` 키 방식은 폐기되었습니다.** 모든 디자인 토큰은 프로젝트 루트의 `DESIGN.md` 한 파일에 정의됩니다.

- 스펙: [design-md-spec.md](references/design-md-spec.md) - YAML frontmatter + 9개 표준 섹션
- 프리셋: [design-md-presets/](references/design-md-presets/) - 6개 기본 프리셋 (`*.design.md`)
- 빌드 시 build.py가 DESIGN.md를 파싱해 CSS variables + 컴포넌트 클래스 자동 생성

| 프리셋 | 적합 카테고리 |
|---|---|
| `clean-minimal` | 테크, 전자제품 (기본값) |
| `dark-luxury` | 주얼리, 시계, 프리미엄 |
| `warm-natural` | 유기농, 웰니스, 스킨케어 |
| `soft-modern` | 패션, 라이프스타일, 코스메틱 |
| `fresh-vibrant` | 식품, 음료, 건강기능식품 |
| `heritage` | 전통, 한복, 공예품 |

---

> **CRITICAL: 두 페이즈 코딩 (v3)**
>
> - **Phase A (텍스트-온리)** → `build/[프로젝트명]-v1-textonly.html`
>   - 모든 카피가 HTML 안에 들어감
>   - 이미지 슬롯은 빈 placeholder (`.image-placeholder` 또는 `{{PLACEHOLDER:...}}`)
>   - **이미지 자리에 한글 카피를 미리 넣지 마세요** (4단계 imageprompt에서 결정됨)
> - **Phase B (이미지 대체)** → `build/[프로젝트명]-v2.html`
>   - image-plan.md의 결정에 따라 이미지 반영
>   - REPLACE 섹션은 HTML `<section>` 삭제 후 `<div class="full-image">`만 남김
>   - SUPPORT 섹션은 `<section>` 유지하고 `<div class="full-image">` 추가
>   - NONE 섹션은 그대로

> **CRITICAL: 중복 방지 (Single Source of Truth)**
>
> 한 카피는 HTML 또는 이미지 중 **한 곳에만** 존재해야 한다.
> - 인접한 두 슬롯(텍스트 섹션 + 그 옆 이미지 섹션)에 같은 한글 카피가 두 번 들어가지 않도록 검증
> - 상세 가이드: [text-image-deduplication.md](references/text-image-deduplication.md)

---

## Workflow (반드시 순서대로, v3)

### Phase 0: 준비 (공통)

1. **입력 확인**:
   - `<project>/PLANNING.md` 존재
   - `<project>/DESIGN.md` 존재 (없으면 `--init` 시 `clean-minimal` 자동 복사)
2. **프로젝트 구조 확인/생성**:
   ```
   projects/MMDDHHmm_[프로젝트명]/
   ├── DESIGN.md             # 디자인 시스템 (필수)
   ├── config.json           # title 등 메타 (선택)
   ├── PLANNING.md           # planning 스킬 출력 (텍스트 only, 이미지 슬롯 분리 X)
   ├── image-plan.md         # Phase A 이후 작성 (REPLACE/SUPPORT/NONE 결정)
   ├── prompts/              # imageprompt 스킬 출력 (Phase A 이후)
   ├── assets/
   │   ├── inbox/            # 사용자 보유/생성 이미지
   │   └── generated/        # Codex native image generation 결과
   └── build/
       ├── [프로젝트명]-v1-textonly.html  # Phase A 산출물
       ├── [프로젝트명]-v2.html           # Phase B 산출물 (이미지 반영)
       └── sections/                      # 분리된 섹션 파일들
   ```

---

### Phase A: 텍스트-온리 빌드 (이미지 없이 완전한 페이지)

> ✅ **이 단계의 목표**: 이미지가 한 장도 없어도 페이지가 의미 전달에 완전한 상태가 되도록 모든 카피를 HTML에 작성.

3. **빈 템플릿 생성**:
   ```bash
   python <danho-detailpage-coding-skill-dir>/scripts/build.py projects/[프로젝트명] --init
   ```
   → DESIGN.md 기반 CSS variables + BASE CSS + components 클래스가 포함된 빈 HTML 생성

4. **콘텐츠 작성 (텍스트만)** - Edit 도구로 `<!-- CONTENT_START -->` ~ `<!-- CONTENT_END -->` 사이에:
   - PLANNING.md의 모든 섹션을 HTML로 옮김 (텍스트만)
   - 각 섹션에 주석 + id 필수 (예: `<!-- Hook Section --><section id="hook">`)
   - **DESIGN.md 컴포넌트 클래스 적극 활용**
   - 이미지가 들어갈 자리에는 빈 `<div class="full-image image-placeholder">` 또는 `{{PLACEHOLDER:설명:W:H:테마}}`
   - **이 단계에서 절대 하지 말 것**:
     - ❌ assets/generated/*.png 를 미리 `<img src=...>`로 참조 (아직 없거나 의미 미확정)
     - ❌ 이미지 안에 들어갈 카피를 미리 HTML에서 빼두기 (역으로 풀 텍스트로 작성)
   - 레이아웃 규칙: [layout-rules.md](references/layout-rules.md)
   - 텍스트→디자인 변환: [design-patterns.md](references/design-patterns.md)

5. **Phase A 결과물 저장**:
   - 파일명: `build/[프로젝트명]-v1-textonly.html`
   - 한 번 사용자에게 보여주고 텍스트 차원에서 만족스러운지 검토 (이미지 결정 전 의사 결정 가능)

---

### Phase A→B 사이: image-plan.md 작성

> ✅ **이 단계의 목표**: v1-textonly.html을 보면서 각 섹션을 시각적으로 어떻게 강화할지 결정.

6. **image-plan.md 작성** - 다음 양식으로 `<project>/image-plan.md` 생성:

   ```markdown
   # Image Plan — [프로젝트명]

   각 섹션을 셋 중 하나로 결정. v1-textonly.html을 위에서 아래로 훑으며 작성.

   | # | 섹션 id | 케이스 | 이미지 종류 | HTML 텍스트 처리 | 비고 |
   |:-:|---|:---:|---|---|---|
   | 01 | hook | REPLACE | banner (배너, 카피 포함) | 섹션 전체 제거 | 슬로건 임팩트 |
   | 02 | problem | NONE | - | 그대로 | 정보형, 이미지 불필요 |
   | 03 | hero | REPLACE | banner (히어로, 카피 포함) | 섹션 전체 제거 | 메인 헤드라인 |
   | 04 | features | SUPPORT | photo (텍스트 없음) | 그대로 + 이미지 추가 | 기능 비주얼 |
   | 05 | materials | SUPPORT | photo (소재 디테일) | 그대로 + 이미지 추가 | 텍스트 절대 금지 |
   | 06 | reviews | NONE | - | 그대로 | 리뷰 카드만 |
   | 07 | faq | NONE | - | 그대로 | FAQ |
   | 08 | cta | NONE | - | 그대로 | 가격/버튼 |
   ```

   결정 기준은 [text-image-deduplication.md](references/text-image-deduplication.md)의 의사결정 트리 참조.

7. **사용자 합의**: image-plan.md를 사용자에게 보여주고 확인. 생성 수량·디자인 방향과 직결되므로 반드시 합의된 상태로 4단계 진입.

---

### Phase A→B 사이: 이미지 프롬프트 + 생성

8. **imageprompt 스킬 호출** (`danho-imageprompt-helper`):
   - 입력: `v1-textonly.html` + `image-plan.md` + `DESIGN.md`
   - 출력:
     - `prompts/banners.md` — REPLACE 섹션의 카피를 HTML에서 그대로 추출해 이미지 안에 포함시키는 프롬프트
     - `prompts/photos.md` — SUPPORT 섹션의 텍스트-없는 비주얼 프롬프트
     - `assets/generated/*.png` — Codex 네이티브 이미지 생성 결과

> 자세한 워크플로우는 `danho-imageprompt-helper` 스킬을 참조.

---

### Phase B: 이미지 대체 빌드

> ✅ **이 단계의 목표**: image-plan.md 결정에 따라 v1-textonly.html을 변형해 v2.html을 생성.

9. **v2.html 생성**:
   - `v1-textonly.html`을 복사해 `[프로젝트명]-v2.html`로 저장 후 image-plan.md를 따라 수정 (또는 build.py가 image-plan.md를 인식하면 자동 변환 — 미구현 시 수동 Edit).
   - **REPLACE 섹션**:
     ```html
     <!-- BEFORE: 인접 텍스트 + 이미지 = 중복 -->
     <div id="image-hero" class="full-image">...</div>
     <section id="hero"><h1>버려도 죄책감 없는...</h1></section>

     <!-- AFTER: 이미지만 남김, alt에 카피 보존 -->
     <div id="image-hero" class="full-image">
         <img src="../assets/generated/hero.png"
              alt="버려도 죄책감 없는 항균 실리콘 수세미">
     </div>
     ```
   - **SUPPORT 섹션**:
     ```html
     <!-- 그대로 유지 + 이미지 (텍스트 없는 비주얼) 추가 -->
     <section id="materials">...</section>
     <div id="image-materials" class="full-image">
         <img src="../assets/inbox/materials-detail.png" alt="...">
     </div>
     ```
   - **NONE 섹션**: 변경 없음.

10. **섹션 분리** (유지보수용):
    ```bash
    python <danho-detailpage-coding-skill-dir>/scripts/split_sections.py build/[프로젝트명]-v2.html build/sections
    ```

11. **남아있는 placeholder 처리** (v1 placeholder가 v2에서 살아남았을 경우):
    ```bash
    python <danho-detailpage-coding-skill-dir>/scripts/generate_placeholders_to_assets.py projects/[프로젝트명]
    ```

12. **중복 검증 (필수)**:
    - 페이지를 위에서 아래로 훑으며 같은 한글 카피가 두 번 보이는지 육안 확인
    - REPLACE 섹션 처리 누락 시 v1의 HTML 섹션이 그대로 남아있음 → 즉시 제거
    - 자세한 검증 체크리스트: [text-image-deduplication.md](references/text-image-deduplication.md) §6

13. **검증 체크리스트** - [output-checklist.md](references/output-checklist.md) 참조

---

### Phase C: 이후 수정

```bash
# 섹션 파일 직접 Edit (build/sections/01_*.html)
python <danho-detailpage-coding-skill-dir>/scripts/build.py projects/[프로젝트명]
# → 새 버전 (v3, v4, ...) HTML 생성
```

> ⚠️ 텍스트 카피를 수정하려면 우선 v1-textonly.html (또는 PLANNING.md)에서 수정 후 image-plan.md 재검토. REPLACE 섹션의 카피를 바꿨다면 해당 이미지도 재생성 필요.

---

## CSS Variables / 컴포넌트 클래스 (DESIGN.md에서 자동 생성)

build.py가 DESIGN.md를 파싱해 다음을 자동 생성합니다:

### Variables 명명 규칙

| YAML 키 | 생성 CSS variable |
|---|---|
| `colors.primary` | `var(--color-primary)` |
| `colors.bg`, `colors.bg-var-1` | `var(--color-bg)`, `var(--color-bg-var-1)` |
| `colors.text`, `colors.text-secondary` | `var(--color-text)`, `var(--color-text-secondary)` |
| `typography.h2.fontSize` | `var(--font-h2-size)` |
| `typography.body-md.fontSize` | `var(--font-body-md-size)` |
| `rounded.lg` | `var(--rounded-lg)` |
| `spacing.md` | `var(--space-md)` |
| `elevation.md` | `var(--shadow-md)` |

### 자동 생성되는 컴포넌트 클래스

DESIGN.md `components:` 아래 각 항목이 동일 이름의 CSS class로 생성됩니다 (모든 프리셋 공통):

| 클래스 | 용도 |
|---|---|
| `.hero-headline` | 메인 히어로 헤드라인 |
| `.section-title` | 섹션 제목 |
| `.card` | 일반 카드 (배경 + 보더 + 그림자) |
| `.checklist-item` | 체크리스트 항목 카드 |
| `.cta-button` | CTA 버튼 |
| `.stat-value` | 통계 숫자 강조 |
| `.badge` | 작은 라벨/배지 |

추가 컴포넌트가 필요하면 DESIGN.md `components:` 에 새 항목을 추가하세요.

### 추가 유틸리티 (BASE_CSS, 도메인 공통)

| 클래스 | 용도 |
|---|---|
| `.content-section` | 본문 섹션 컨테이너 (`padding: 120px 10%`) |
| `.section-var-1/2/3`, `.section-inverted` | 배경 변화 |
| `.full-image` | 별도 이미지 섹션 (100% width) |
| `.section-desc`, `.section-intro`, `.section-subtitle` | 보조 텍스트 |
| `.title-gradient`, `.title-shadow`, `.title-glow`, `.title-neon-gradient` | 타이틀 효과 |
| `.checklist`, `.check-box`, `.check-text` | 체크리스트 구조 |
| **`.stack-cards`, `.stack-card`** ⭐ | **수직 스택 카드 (카드당 본문이 2줄 이상이거나 텍스트 길면 우선 사용)** |
| **`.stack-card.has-image` + `.card-image` + `.card-body`** ⭐ | **카드 상단 풀-블리드 이미지 + 본문 (별도 `.full-image` 슬롯과 흡수해 더 직관적)** |
| `.grid-2`, `.grid-3` | 그리드 (라벨/태그/한 줄 카드 등 짧은 카피 한정) |
| `.stats-grid`, `.stat-item`, `.stat-label` | 통계 (작은 박스, max-width 180px — **가격 강조 금지**) |
| **`.price-display`, `.price-value`, `.price-unit`, `.price-meta`** ⭐ | **CTA 가격 강조 전용** (큰 숫자 + 작은 단위 + 부가 메타. `.stat-item`의 좁은 폭 제약 없음) |
| `.gold`/`.accent`, `.highlight`, `.block` | 인라인 강조 |
| `.cta-section`, `.footer-section`, `.footer-brand`, `.footer-tagline` | 섹션/푸터 |

> 🚨 **그리드 vs 스택 선택 룰**: 카드 안 본문이 **2줄 이상이거나 30자를 넘으면 거의 항상 `.stack-cards`**가 정답입니다. 본문 폭(80% = ~688px)에서 grid-3는 카드당 ~210px라 긴 텍스트가 답답하게 깨집니다. 상세: [layout-rules.md §5](references/layout-rules.md#5-content-length-based-layout-decision-critical--콘텐츠-양-기반-배치-결정)

---

## Core Technical Specifications

### Image Interleaving (CRITICAL)

기획서의 이미지 배치를 그대로 따르지 마세요. 텍스트와 이미지가 교차되어야 합니다. 상세: [image-handling.md](references/image-handling.md)

### Layout Rules (CRITICAL)

- Max width: **860px**
- Content sections: `padding: var(--space-section, 120px) 10%` (margin 금지, width 지정 금지)
- Images: 별도 `.full-image` 섹션, 100% width
- **NO animations, NO JavaScript, NO :hover effects**

상세: [layout-rules.md](references/layout-rules.md)

### Static Design Principle (CRITICAL)

```css
/* ❌ FORBIDDEN */
:hover, :focus, transition, animation, @keyframes

/* ✅ REQUIRED - 기본 상태에서 완성 */
.card { border: 1px solid; box-shadow: var(--shadow-md); }
```

상세: [static-design.md](references/static-design.md)

### Checklist Symbol Conversion (CRITICAL)

기획서의 텍스트 체크박스 기호(`☐`, `□`, `•`)는 반드시 HTML 요소로 변환:

```html
✅ REQUIRED:
<li>
    <span class="check-box"></span>
    <span class="check-text">잠들기 전 ASMR을 듣고 싶어요</span>
</li>
```

### Section ID Rules (REQUIRED)

```html
<!-- Hook Section -->
<section id="hook" class="content-section">...</section>

<!-- Hero Image -->
<div id="image-hero" class="full-image">...</div>
```

---

## Reference Documents

| Reference | Content |
|-----------|---------|
| [text-image-deduplication.md](references/text-image-deduplication.md) | **v3 핵심**: 텍스트-이미지 중복 방지, 케이스 의사결정 ⭐ |
| [image-plan-template.md](references/image-plan-template.md) | **v3 핵심**: image-plan.md 작성 양식 + 가이드 ⭐ |
| [design-md-spec.md](references/design-md-spec.md) | DESIGN.md 작성 규격 ⭐ |
| [design-md-presets/](references/design-md-presets/) | 6개 기본 프리셋 ⭐ |
| [layout-rules.md](references/layout-rules.md) | 레이아웃, 그리드, 섹션 ID, 정렬 규칙 |
| [static-design.md](references/static-design.md) | 정적 디자인 원칙, 금지/필수 CSS |
| [depth-design.md](references/depth-design.md) | 3D 입체감, Shadow 시스템 |
| [image-handling.md](references/image-handling.md) | 이미지 배치, 플레이스홀더 |
| [title-effects.md](references/title-effects.md) | h1/h2 효과, 그라데이션, 네온 |
| [css-examples.md](references/css-examples.md) | 버튼, 체크리스트, 통계, 리뷰 |
| [design-patterns.md](references/design-patterns.md) | 텍스트→디자인 변환 패턴 |
| [output-checklist.md](references/output-checklist.md) | 최종 검증 체크리스트 |

---

## Section Templates

### Content Section Template

```html
<!-- Section Name -->
<section id="section-id" class="content-section section-var-1">
    <h2 class="section-title title-glow">
        <span class="block">첫 번째 줄</span>
        <span class="block gold">두 번째 줄 (강조)</span>
    </h2>
    <p class="section-desc">설명 텍스트.</p>
    <!-- 콘텐츠 -->
</section>
```

### Image Section Template

```html
<!-- Image Description -->
<div id="image-name" class="full-image">
    <img src="../../assets/generated/banner-hero.png" alt="설명" data-placeholder="keyword">
</div>
```

**이미지 경로**: `build/<프로젝트명>-vN.html` 위치에서 `../../assets/<폴더>/이미지.png` (assets는 프로젝트 루트 기준 한 단계 위, build는 추가 한 단계).

⚠️ 정확히는 `build/<프로젝트명>-vN.html` 에서 `../assets/...` 입니다. (build가 한 단계, assets가 sibling)

```
projects/01241530_foo/
├── build/foo-v1.html        ← 여기서
└── assets/...               ← ../assets/... 로 접근
```

---

## Before Delivering: Quick Checklist

### Phase A (v1-textonly) 체크리스트

**파일 구조:**
- [ ] `DESIGN.md` 프로젝트 루트에 존재 (검증 통과)
- [ ] `config.json` 생성 (`title`)
- [ ] `sections/styles.css` 작성 (필요 시)
- [ ] 텍스트-온리 HTML 완성 (`build/[프로젝트명]-v1-textonly.html`)

**카피 완전성 (v3 핵심):**
- [ ] PLANNING.md의 모든 텍스트 카피가 HTML 안에 들어있음
- [ ] 이미지 없이도 페이지가 의미 전달에 완전함
- [ ] 이미지 슬롯에 `<img src>`로 외부 이미지 미참조 (placeholder만)
- [ ] 이미지 안에 들어갈 카피를 HTML에서 미리 빼두지 않음

### Phase B (v2, 이미지 반영) 체크리스트

**image-plan 정합성:**
- [ ] `image-plan.md` 작성 + 사용자 합의 완료
- [ ] REPLACE 섹션의 원본 `<section>` 전부 제거됨 (HTML 텍스트 잔존 금지)
- [ ] SUPPORT 섹션의 텍스트는 그대로, 이미지가 별도 `.full-image`로 추가됨
- [ ] NONE 섹션은 v1과 동일

**중복 검증 (v3 핵심):**
- [ ] 페이지를 위에서 아래로 훑었을 때 같은 한글 카피가 두 번 보이지 않음
- [ ] REPLACE 이미지의 alt에 원본 카피 보존
- [ ] SUPPORT 이미지에 한글 텍스트가 들어가 있지 않음

**PLANNING ↔ HTML 동기화 (v3 신규):**
- [ ] **제품 호칭 일관성**: PLANNING.md의 단축형이 HTML 본문에 일관 적용. 단독 브랜드명("알파" 단독) 본문 잔존 0 — `grep "{브랜드}" build/*.html | grep -v "{단축형}"` 출력 0 ([product-naming-consistency.md](../danho-detailpage-planning/references/product-naming-consistency.md))
- [ ] **가격 동기화**: PLANNING.md ↔ options 카드 ↔ CTA `.price-display`/`.price-meta` 세 곳 모두 동일 금액
- [ ] **옵션 동기화**: PLANNING의 옵션 개수·라벨 = options 섹션 카드와 일치
- [ ] **REPLACE 카피 동기화**: image-plan.md의 카피 = banners.md 프롬프트 안 한글 = v1-textonly.html의 원본 글자 그대로
- [ ] 상세 검증 항목: [output-checklist.md §4-A](references/output-checklist.md)

### 공통 (Phase A & B)

**레이아웃:**
- [ ] Content: `padding: var(--space-section) 10%` only
- [ ] 이미지: 별도 `.full-image` 섹션
- [ ] **카드 콘텐츠 길이 검증**: `.grid-2`/`.grid-3`로 묶인 카드 중 본문이 2줄 이상이거나 30자를 넘는 카드가 있다면 `.stack-cards`로 변환 ([layout-rules.md §5](references/layout-rules.md#5-content-length-based-layout-decision-critical--콘텐츠-양-기반-배치-결정))

**필수 요소:**
- [ ] 모든 섹션에 주석 + 고유 id
- [ ] h1, h2에 타이틀 효과 적용 (테마에 맞는 것)
- [ ] DESIGN.md 컴포넌트 클래스 사용 (`.card`, `.cta-button` 등)
- [ ] 배경 변화 2~3회 이상 (`.section-var-1/2/3` 또는 `.section-inverted`)

**금지 사항:**
- [ ] NO `:hover`, `transition`, `animation`
- [ ] NO JavaScript
- [ ] 이미지가 콘텐츠 섹션 안에 포함되지 않음
- [ ] 텍스트 체크박스 기호 (`☐`, `□`) → `.check-box` 클래스로
- [ ] **헤드라인 끝 마침표(.) 없음** — `h1`/`h2`/`h3`/`.cta-button`/`.badge`/슬로건성 `.section-desc` 모두. 본문 paragraph만 정상 마침표. ([korean-headline-rules.md](../danho-detailpage-planning/references/korean-headline-rules.md))
  - 빠른 검증 grep:
    ```bash
    grep -E '(section-title|hero-headline|section-subtitle|cta-button|block accent)">[^<]*\.</' build/*.html
    ```
    출력이 비어 있어야 합격

**최종 작업:**
- [ ] 섹션 분리: `python <danho-detailpage-coding-skill-dir>/scripts/split_sections.py build/[프로젝트명]-v2.html build/sections`
- [ ] DESIGN.md 검증: `python <danho-detailpage-coding-skill-dir>/scripts/design_md.py <project>/DESIGN.md --validate`

상세: [output-checklist.md](references/output-checklist.md), [text-image-deduplication.md](references/text-image-deduplication.md)
