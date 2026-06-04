# Output Checklist (출력 체크리스트)

HTML 코딩 완료 후, 아래 체크리스트를 모두 확인하세요.

---

## 1. Layout Checklist (레이아웃)

- [ ] Max width 860px 적용됨
- [ ] `box-sizing: border-box` 모든 요소에 적용됨
- [ ] `.detail-page`에 `overflow-x: hidden` 적용됨
- [ ] 콘텐츠 섹션: `padding: 0 10%`만 사용 (margin, width 지정 금지)
- [ ] 이미지는 별도 `.full-image` 섹션으로 분리됨

---

## 2. Section IDs Checklist (섹션 ID - 필수)

- [ ] 모든 `<section>` 요소에 고유 id 부여됨
- [ ] 모든 `.full-image` 요소에 고유 id 부여됨 (예: `id="image-hero"`)
- [ ] ID 명명 규칙 준수 (영문 소문자, 하이픈 구분)
- [ ] 중복 ID 없음

**예시:**
```html
<!-- HOOK Section -->
<section id="hook" class="hook-section">...</section>

<!-- Hero Image -->
<div id="image-hero" class="full-image">...</div>
```

---

## 3. Images Checklist (이미지)

- [ ] 모든 이미지가 `<img>` 태그 사용 (background-image 아님)
- [ ] 모든 이미지에 `max-width: 100%` 적용됨
- [ ] 플레이스홀더 이미지 생성 완료: `python scripts/generate_placeholders_to_assets.py [project_dir]`
- [ ] 생성된 이미지가 `assets/placeholders/` 디렉토리에 저장됨
- [ ] HTML의 이미지 경로가 상대 경로로 업데이트됨 (`../assets/placeholders/xxx.png`)

---

## 4. Flexible Image Placement Checklist (유연한 이미지 배치)

- [ ] 기획서의 📍위치 지정에 따라 이미지 배치됨
- [ ] 📍전 (텍스트 전): `<div.full-image>` → `<section>` 순서
- [ ] 📍후 (텍스트 후): `<section>` → `<div.full-image>` 순서
- [ ] 📍사이 (텍스트 사이): `<section>` → `<div.full-image>` → `<section>` 구조
- [ ] 📍교차: 이미지 → 텍스트 → 이미지 → 텍스트 반복
- [ ] 이미지가 `<section>` 안에 직접 포함되지 않음 (항상 별도 `.full-image` 컨테이너)

**위치별 HTML 패턴:**

| 위치 | 효과 | 권장 섹션 | HTML 순서 |
|------|------|-----------|-----------|
| 📍후 | 설명 후 증거 제시 | HERO, FAQ, OPTIONS | `<section>` → `<div.full-image>` |
| 📍전 | 시각적 임팩트 먼저 | EMPATHY, TARGET, CTA | `<div.full-image>` → `<section>` |
| 📍사이 | 단락 구분, 리듬감 | REVIEWS, STORY | `<section>` → `<div.full-image>` → `<section>` |
| 📍교차 | 각 포인트별 설득 | FEATURES, CRAFTSMANSHIP | `<div.full-image>` → `<section>` 반복 |

---

## 4-A. PLANNING ↔ HTML Sync Checklist (동기화 검증 — CRITICAL)

> PLANNING.md에서 정의된 제품명·가격·옵션·핵심 카피가 HTML 본문, alt 속성, prompts/banners.md에 **일관되게** 반영되었는지 확인.
> 한 곳만 수정되고 다른 곳이 누락되면 페이지 전체에 모순이 생긴다.

### 제품 호칭 일관성

- [ ] **PLANNING.md의 "제품 호칭 3계층"이 HTML 본문에 동일하게 사용됨**
  - 풀네임이 hero/CTA에 등장
  - 본문 paragraph·카드 텍스트·alt에 단축형 사용
  - 브랜드 단독("알파") 표기가 본문에 누락 없이 단축형으로 교정됨
- [ ] **잔존 검증 grep** (출력 0이어야 합격):
  ```bash
  # 예: 브랜드 "알파" / 단축형 "알파 실리콘 수세미" / 풀네임 "알파 식기세척기 초벌 전용 실리콘 수세미"
  grep "알파" build/*.html | grep -v "알파 실리콘 수세미\|알파 식기세척기"
  ```
  상세: [../../danho-detailpage-planning/references/product-naming-consistency.md](../../danho-detailpage-planning/references/product-naming-consistency.md)

### 가격·옵션 동기화

- [ ] **PLANNING.md의 가격이 HTML의 옵션 카드와 CTA `.price-display` 양쪽 모두에 동일 금액으로 반영됨**
  - 가격을 변경할 때는 다음 3곳을 모두 갱신:
    1. PLANNING.md 기본 정보 표
    2. HTML `options` 섹션의 카드 (옵션별 가격)
    3. HTML `cta` 섹션의 `.price-display` + `.price-meta`
- [ ] **검증 grep** (모든 가격 위치를 한 번에 확인):
  ```bash
  grep -nE "[0-9],?[0-9]{3}원|[0-9]{4,}원" build/*.html
  ```
  → 위 출력을 PLANNING.md의 가격 정의와 한 줄씩 대조

### 옵션 구성 동기화

- [ ] PLANNING.md에 정의된 옵션 개수 = HTML `options` 섹션의 카드 개수
- [ ] PLANNING.md에 정의된 옵션 라벨 = HTML 카드 라벨
- [ ] CTA `.price-meta`의 옵션 요약이 PLANNING.md 옵션 정의와 일치

### REPLACE 카피 동기화

- [ ] image-plan.md의 REPLACE 카피 원문 = banners.md 프롬프트 안 한글 카피
- [ ] 위 두 카피가 v1-textonly.html에 원래 있던 카피와 글자 그대로 일치 (변형·재작성 금지)
- [ ] v2.html에서는 REPLACE 섹션의 `<section>`이 모두 삭제되었고 `<div class="full-image">`로 대체됨

---

## 5. Text Checklist (텍스트)

- [ ] **헤드라인·슬로건·CTA·badge·섹션 제목 끝에 마침표(.) 없음** ⭐ — 한국 광고 카피 관례. `h1`/`h2`/`h3`/`.cta-button`/`.badge`/`.section-intro`/슬로건성 `.section-desc` 모두 마침표로 닫지 않음. 본문 paragraph는 정상 마침표. 상세: [../../danho-detailpage-planning/references/korean-headline-rules.md](../../danho-detailpage-planning/references/korean-headline-rules.md)
  - 빠른 검증 grep (출력 0이어야 합격):
    ```bash
    grep -E '(section-title|hero-headline|section-subtitle|cta-button|block accent|section-intro)">[^<]*\.</' build/*.html
    ```
  - 자주 발생하는 사례:
    - ❌ `<span class="block accent">단단하게.</span>` → ✅ `<span class="block accent">단단하게</span>`
    - ❌ `<h3 class="section-subtitle">사용 후기.</h3>` → ✅ `<h3 class="section-subtitle">사용 후기</h3>`
    - ❌ `<a class="cta-button">지금 구매하기.</a>` → ✅ `<a class="cta-button">지금 구매하기</a>`
  - ⚠️ 물음표(?)·느낌표(!)·쉼표(,)는 허용. "왜 초벌은 남을까요?", "지금 만나보세요!" OK.
- [ ] 의미 단위 유지를 위해 `&nbsp;` 사용됨
- [ ] 3줄 이상 연속 텍스트는 디자인 패턴으로 변환됨

---

## 5-1. Checklist Symbol Conversion (체크박스 기호 변환 - CRITICAL)

**기획서의 텍스트 체크박스 기호(☐, □, •)는 반드시 SVG 아이콘으로 변환합니다.**

- [ ] `☐`, `□`, `■`, `▢`, `◻` 등 유니코드 체크박스 기호가 HTML에 없음
- [ ] 모든 체크리스트 항목이 SVG 아이콘 + 텍스트 조합으로 변환됨
- [ ] `.checklist-bullet` 또는 SVG 체크 아이콘 스타일 사용됨

**변환 예시:**
```
❌ FORBIDDEN (텍스트 기호 그대로):
<li>☐ 잠들기 전 ASMR을 듣고 싶어요</li>

✅ REQUIRED (SVG 아이콘으로 변환):
<li>
    <span class="bullet-icon"><svg width="16" height="16">...</svg></span>
    <span class="check-text">잠들기 전 ASMR을 듣고 싶어요</span>
</li>
```

**권장 스타일:** `css-examples.md`의 "Style 5: Bullet Square" 참조

---

## 6. Contrast Checklist (대비)

- [ ] 모든 텍스트가 배경과 충분한 대비로 가독성 확보됨
- [ ] 같은 색조(hue) 조합 사용되지 않음

---

## 7. Card Text Contrast Checklist (카드 텍스트 대비 - CRITICAL)

- [ ] 밝은 배경 카드 (`#f0f0f0` 이상) → 어두운 텍스트 (`#1a1a1a` ~ `#4a4a4a`) 사용
- [ ] 어두운 배경 카드 (`#2a2a2a` 이하) → 밝은 텍스트 (`#ffffff` ~ `#e0e0e0`) 사용
- [ ] 비교 카드 (X vs ✓) 본문 텍스트가 배경과 대비됨
- [ ] 아이콘/강조색만 테마색 사용, 본문은 기본 대비색 사용

**테마별 카드 텍스트 색상 매핑:**

| 테마 | 카드 배경 | 제목 색상 | 본문 색상 |
|------|----------|----------|----------|
| Clean Minimal (밝은 카드) | `#f8f9fa` | `#1a1a1a` | `#1a1a1a` |
| Clean Minimal (다크 반전) | `#1a1a1a` | `#ffffff` | `#ffffff` |
| Dark Luxury (다크 카드) | `#141414` | `#c9a962` | `#ffffff` |
| Dark Luxury (라이트 반전) | `#faf7f2` | `#1a1a1a` | `#1a1a1a` |
| Warm Natural (밝은 카드) | `#f5efe6` | `#3d3028` | `#3d3028` |
| Warm Natural (다크 반전) | `#3d3028` | `#faf7f2` | `#faf7f2` |

---

## 8. Title Effects Checklist (타이틀 효과 - CRITICAL)

- [ ] h1, h2 타이틀에 테마별 효과 **필수** 적용됨
- [ ] Clean Minimal: h1에 `title-gradient title-shadow`, h2에 `title-shadow`
- [ ] Dark Luxury (그라데이션): h1에 `title-gradient-shadow`, h2에 `title-glow`
- [ ] Dark Luxury (단색+네온): h1에 `title-neon`, h2에 `title-glow`
- [ ] Warm Natural: h1에 `title-gradient title-shadow`, h2에 `title-shadow`
- [ ] **그라데이션 + 네온 동시 적용 금지** (가독성 저하)
- [ ] 본문 텍스트(p, li)에는 효과 미적용

**테마별 필수 클래스 매핑:**

| 테마 | h1 클래스 | h2 클래스 |
|------|-----------|-----------|
| Clean Minimal | `title-gradient title-shadow` | `title-shadow` |
| Dark Luxury (그라데이션) | `title-gradient-shadow` | `title-glow` |
| Dark Luxury (단색+네온) | `title-neon` 또는 `title-neon-intense` | `title-glow` |
| Warm Natural | `title-gradient title-shadow` | `title-shadow` |

---

## 9. Static Design Checklist (정적 디자인 - CRITICAL)

- [ ] JavaScript 사용 없음
- [ ] CSS animations 사용 없음 (`@keyframes`, `animation`)
- [ ] CSS transitions 사용 없음 (`transition`)
- [ ] :hover effects 사용 없음 (`:hover`, `:focus` 스타일 변경 금지)
- [ ] 모든 디자인 요소가 기본 상태에서 완성되어 보임
- [ ] 카드/버튼에 기본 상태 box-shadow, border 적용됨

**정적 디자인 원칙:**
- 호버 시에만 보이는 효과는 정적 상태에서 디자인이 허전해 보임
- 이커머스 상세페이지는 스크롤하며 읽는 콘텐츠 → 인터랙션 불필요
- 모바일 사용자는 호버 불가능 → 호버 효과는 무의미

---

## 10. Grid Layout Checklist (그리드 레이아웃)

- [ ] 4개 카드 → 2x2 배치 (3-1 밀림 방지)
- [ ] 5개 카드 → 3+2 교차 중앙 정렬
- [ ] 카드 그리드는 `.full-width-grid` 또는 `.grid-2col` 사용
- [ ] 모든 카드가 균등한 크기로 정렬됨

**개수별 권장 레이아웃:**

| 개수 | 레이아웃 | 방법 |
|------|----------|------|
| 2개 | 1x2 (한 줄) | `.grid-2` - flex 한 줄 |
| 3개 | 1x3 (한 줄) | `.grid-3` - flex 한 줄 또는 full-width |
| 4개 | **2x2** | `.grid-4` - 반드시 2열 배치 |
| 5개 | **3+2 교차** | `.grid-5` - 3열 기준, 중앙 정렬 |
| 6개 | 2x3 또는 3x2 | `.grid-6` - 상황에 따라 선택 |

---

## 11. Card Text Readability Checklist (카드 가독성 - CRITICAL)

- [ ] Stats 카드(숫자+라벨)는 수평 레이아웃 사용 (세로 중앙 정렬 금지)
- [ ] 숫자/가격에 `white-space: nowrap` 적용 (줄바꿈 방지)
- [ ] 좁은 카드에 여러 줄 텍스트 금지 → 2열 와이드 카드 사용
- [ ] 긴 설명이 있는 카드는 `text-align: left` + `min-width: 160px`
- [ ] 한 글자씩 줄바꿈되는 텍스트 없음

**문제 상황 예시:**
```
┌─────────┐
│   ⭐    │
│   4.    │  ← 숫자가 쪼개짐
│   6     │
│ 평 균   │  ← 한글이 한 글자씩 줄바꿈
│ 평 점   │
└─────────┘
```

**해결책:** 수평 레이아웃 카드로 변환

---

## 12. Section Label Alignment Checklist (섹션 레이블 정렬 - CRITICAL)

- [ ] `.section-label`에 `display: block` + `width: fit-content` + `margin: 0 auto 20px auto` 적용
- [ ] `.section-title`에 `text-align: center` 적용
- [ ] 섹션 레이블과 타이틀 정렬 일치 (둘 다 중앙)
- [ ] 부모 섹션에 `text-center` 적용 금지 (본문까지 중앙 정렬됨)

**필수 CSS 패턴:**
```css
.section-label {
    display: block;
    width: fit-content;
    margin: 0 auto 20px auto;
    text-align: center;
}

.section-title {
    text-align: center;
    margin-bottom: 32px;
}
```

---

## 13. 3D Depth Checklist (입체감)

- [ ] 카드에 `box-shadow` + `border` + `background gradient` 적용됨
- [ ] 버튼에 `box-shadow` + `inset highlight` 적용됨
- [ ] CTA 영역에 `--shadow-lg` 이상 적용됨
- [ ] 섹션 구분에 subtle shadow 또는 inset shadow 사용됨
- [ ] 테마별 shadow 강도 조정됨 (Dark: 강함, Minimal: 약함)

**레이어별 Shadow 시스템:**

| 레벨 | 변수 | 용도 |
|------|------|------|
| Level 1 | `--shadow-sm` | 살짝 떠있음 (기본 카드, 뱃지) |
| Level 2 | `--shadow-md` | 중간 높이 (강조 카드, 버튼) |
| Level 3 | `--shadow-lg` | 높이 떠있음 (CTA, 중요 요소) |
| Level 4 | `--shadow-xl` | 최상위 (모달, 팝업) |

---

## 14. Background Variation Checklist (배경 변화 - 필수)

- [ ] 전체 페이지에서 최소 2~3회 배경 변화 적용됨
- [ ] 반전 섹션에서 텍스트 색상이 적절히 변경됨
- [ ] CTA 섹션에 강조 배경 또는 반전 배경 적용됨

**섹션별 배경 권장:**

| 섹션 위치 | 배경 권장 |
|----------|----------|
| 1-3 (HOOK~HERO) | 기본 배경 |
| 4-6 (EMPATHY~FEATURES) | 변화1 또는 기본 |
| 7-9 (중간) | **반전 배경** (강조) |
| 10-12 (REVIEWS~CTA) | 기본으로 복귀 |
| CTA (마지막) | 반전 또는 강조 배경 |

**테마별 배경 변화 팔레트:**

| 테마 | 기본 | 변화1 | 반전 |
|------|------|-------|------|
| Clean Minimal | #ffffff | #f8f9fa | #1a1a1a + 흰색 텍스트 |
| Dark Luxury | #0a0a0a | #141414 | #faf7f2 + 다크 텍스트 |
| Warm Natural | #faf7f2 | #f5efe6 | #3d3028 + 밝은 텍스트 |
