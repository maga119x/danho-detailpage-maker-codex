# Layout Rules Reference (레이아웃 규칙)

상세페이지 HTML/CSS 코딩 시 반드시 준수해야 하는 레이아웃 규칙입니다.

---

## 1. Layout Rules (CRITICAL - 기본 레이아웃)

### 860px 컨테이너 구조

```
┌─────────────────────────────────────┐
│            860px container           │
├─────────────────────────────────────┤
│ IMAGE ████████████████████████ 100% │ ← 별도 섹션, Full width, no padding
├─────────────────────────────────────┤
│ 10% │    CONTENT 80%    │ 10% │     │ ← padding: 0 10% 만 사용
├─────────────────────────────────────┤
│ IMAGE ████████████████████████ 100% │ ← 별도 섹션, 콘텐츠 안에 넣지 않음
└─────────────────────────────────────┘
```

### 핵심 규칙

| 항목 | 규칙 |
|------|------|
| Max width | **860px** |
| Content sections | `padding: var(--space-section) 5%` (좌우 5% — 콘텐츠 영역 90%) |
| Images | 별도 `.full-image` 섹션, 100% width |
| 인터랙션 | **NO animations, NO JavaScript, NO :hover effects** |

> ⚠️ **좌우 padding 정책**: 본 스킬의 표준은 **좌우 5%** (이전 10%에서 축소). 모바일·태블릿에서 콘텐츠 영역을 더 넓게 활용하며, max-width 860px 컨테이너 안에서 효과가 큼. CTA·footer 섹션도 동일.

---

## 2. Width Control Rules (너비 제어)

### Padding만 사용 (margin 금지)

```css
/* ❌ BAD - margin + padding 중복 → 좁은 콘텐츠 영역 */
.section { margin: 0 86px; padding: 0 86px; }

/* ✅ GOOD - padding만 사용 → 정확히 90% 너비 (좌우 5%) */
.content-section { padding: 120px 5%; }
```

**왜 중요한가:**
- margin과 padding을 함께 사용하면 예상보다 좁은 콘텐츠 영역이 됨
- width 직접 지정 시 반응형 깨짐 발생
- padding만 사용하면 컨테이너 기준 정확한 비율 유지

---

## 3. Overflow Prevention (오버플로우 방지 - REQUIRED)

모든 프로젝트에 필수 적용:

```css
/* 모든 요소에 box-sizing 적용 */
*, *::before, *::after {
    box-sizing: border-box;
}

/* 메인 컨테이너 설정 */
.detail-page {
    max-width: 860px;
    margin: 0 auto;
    overflow-x: hidden;  /* 가로 스크롤 방지 */
}

/* 모든 자식 요소 max-width 제한 */
.detail-page * {
    max-width: 100%;
}

/* 이미지 설정 */
img {
    max-width: 100%;
    height: auto;
    display: block;
}
```

---

## 4. Section ID Rules (섹션 ID 규칙 - REQUIRED)

### 필수 형식

**모든 섹션에는 반드시 고유한 id 속성을 부여해야 합니다.**

```html
<!-- ✅ GOOD - 주석 + id 형식 (수정 스킬 자동 인식) -->
<!-- HOOK Section -->
<section id="hook" class="hook-section">...</section>

<!-- Hero Section -->
<section id="hero" class="hero-section">...</section>

<!-- Hero Image -->
<div id="image-hero" class="full-image">...</div>

<!-- ❌ BAD - 주석 없음 (수정 스킬 인식 불가) -->
<section id="hero" class="hero-section">...</section>

<!-- ❌ BAD - id 없음 -->
<section class="content-section">...</section>
```

### ID 명명 규칙

| 섹션 유형 | 권장 ID | 예시 |
|----------|---------|------|
| 훅/오프닝 | `hook` | `id="hook"` |
| 히어로/메인 | `hero`, `main` | `id="hero"` |
| 문제 제기 | `problem`, `pain-point` | `id="problem"` |
| 해결책/솔루션 | `solution`, `answer` | `id="solution"` |
| 제품 특징 | `features`, `feature-{n}` | `id="features"` |
| 혜택/베네핏 | `benefits`, `benefit-{n}` | `id="benefits"` |
| 사용법/방법 | `how-to`, `usage` | `id="how-to"` |
| 리뷰/후기 | `reviews`, `testimonials` | `id="reviews"` |
| 스펙/상세정보 | `specs`, `details` | `id="specs"` |
| 구성품 | `components`, `includes` | `id="components"` |
| CTA/구매유도 | `cta`, `cta-1`, `cta-final` | `id="cta"` |
| 이미지 섹션 | `image-{설명}` | `id="image-hero"`, `id="image-lifestyle"` |

### 중요: danho-detailpage-editing 스킬 호환성

수정 스킬에서 자동 인식을 위해 반드시 아래 패턴을 따라야 합니다:

```
<!-- {섹션 설명} -->
<section id="{고유ID}" class="{클래스}">...</section>
```

---

## 4-A. Alignment Consistency Policy (CRITICAL — 정렬 일관성 정책)

> 🚨 **페이지 전체의 정렬 톤을 한 가지로 통일하지 않으면, 어느 한 컴포넌트만 좌측 정렬되어 있을 때 페이지 흐름이 어색해진다.** 본 디자인 프리셋(clean-minimal 등)들은 **가운데 정렬 톤**을 기본으로 한다.

### 기본 정렬 (가운데 톤 페이지 — clean-minimal 등 표준 프리셋)

| 요소 | 정렬 |
|---|---|
| `.section-title`, `.hero-headline` | 가운데 |
| `.section-desc`, `.section-intro` | 가운데 |
| `.stat-item`, `.stats-grid` | 가운데 |
| `.cta-section` 내부 | 가운데 |
| `.footer-section` 내부 | 가운데 |
| **`.stack-card` 내부 (badge·h3·p)** | **가운데** ⭐ 본문 p는 `max-width: 60ch`로 가독성 보호 |
| **`.stack-card.has-image .card-body`** | **가운데** ⭐ |
| `.card`(일반 단일 카드) 내부 | 가운데 |

### 좌측 정렬이 자연스러운 예외 (의도적으로 유지)

| 요소 | 이유 |
|---|---|
| `.checklist`, `.checklist-item` | 체크박스 + 텍스트는 좌측에서 시작하는 수평 흐름이 자연스러움 |
| 본문 paragraph 중 정보·표·코드 인용 | 줄 시작이 가지런해야 가독성 |
| FAQ 답변 4줄 이상 paragraph | 긴 본문 좌측 정렬이 일반 |

### 안티패턴 (자주 발생하는 어색함)

```html
<!-- ❌ BAD: 페이지 톤은 가운데인데, stack-card 안 badge·h3·p가 좌측에 박혀 어색 -->
<section class="content-section"><!-- 섹션 자체는 가운데 톤 -->
    <h2 class="section-title">알파 실리콘 수세미를 고른 3가지 이유</h2>
    <ul class="stack-cards">
        <li class="card stack-card">
            <span class="badge">01</span>            <!-- ← 좌측에 떠있어 어색 -->
            <h3>양면 디자인</h3>                       <!-- ← 좌측 -->
            <p>한 장으로 두 단계, 손목 한 번 뒤집어...</p>  <!-- ← 좌측 -->
        </li>
    </ul>
</section>

<!-- ✅ GOOD: .stack-card { text-align: center; }로 통일됨 -->
```

### CSS 강제 (BASE_CSS에 포함되는 표준)

```css
.stack-card {
    padding: 36px 40px;
    text-align: center;        /* 페이지 톤과 일치 */
}
.stack-card p {
    line-height: 1.7;
    margin: 0 auto;
    max-width: 60ch;           /* 본문 가독성 보호 */
}
.stack-card.has-image .card-body {
    padding: 36px 40px;
    text-align: center;
}
```

### 다른 페이지 톤(좌측 정렬) 프리셋 적용 시

dark-luxury 같은 좌측 정렬 톤의 프리셋을 사용한다면, 반대로 `.stack-card { text-align: left; }`로 통일. 핵심은 **페이지 톤과 카드 내부 톤을 일치시키는 것**.

### 자가 검증

빌드 후 페이지를 위에서 아래로 스크롤하며:
- [ ] 헤더(`section-title`)와 그 아래 카드(`stack-card`) 안 텍스트 정렬이 같은 방향인가?
- [ ] 카드 안 `badge`가 카드 가장자리에 떠 있어 어색하지 않은가?
- [ ] 본문 paragraph가 너무 넓게 펼쳐져 가독성이 떨어지지 않는가? (max-width 적용 확인)

---

## 4-B. Card Inner Typography Scale (CRITICAL — 카드 내부 폰트 위계)

> 🚨 **카드(`.card`, `.stack-card`) 안 텍스트는 본문 기준 한 단계(0.5rem) 작게.** 같은 사이즈일 경우 카드와 본문이 시각적으로 구분되지 않아 위계가 무너진다.

### 본문 기본 ↔ 카드 내부 매핑

| 요소 | 본문 기본 (DESIGN.md typography) | 카드 내부 (BASE_CSS override) | 차이 |
|---|---|---|---|
| `.badge` | caption 1.5rem | **1rem** | -0.5rem |
| `.section-subtitle` (카드 안 `<h3>`) | h3 2.625rem | **2.125rem** | -0.5rem |
| `<p>` 본문 (카드 안) | body-md 2rem | **1.5rem** | -0.5rem |

### 적용 위치 (BASE_CSS 표준 — 자동 적용)

```css
.stack-card .badge,
.card .badge          { font-size: 1rem; }
.stack-card .section-subtitle,
.card .section-subtitle { font-size: 2.125rem; }
.stack-card p,
.card p               { font-size: 1.5rem; line-height: 1.7; }
```

### 왜 0.5rem ↓ 인가

- 페이지 본문(`.section-desc`, `.section-intro`)이 2rem(body-md)이고 헤더가 3.25rem(h2). 카드는 이 사이의 보조 위계
- 카드 안에서도 본문과 동일 사이즈면 카드 컴포넌트가 "그냥 페이지의 연장"으로 보임 → 카드의 시각적 구분 효과 사라짐
- 한 단계 작게 두면 카드 = 보조 정보 그룹이라는 신호가 명확

### 모바일 가독성

카드 내부 1.5rem(24px) 본문은 모바일에서도 충분한 가독성을 확보. 더 줄이지 말 것 (1.5rem이 하한).

### 안티패턴

```css
/* ❌ BAD: 카드 안 본문이 페이지 본문과 동일 사이즈 → 위계 사라짐 */
.stack-card p { font-size: 2rem; }

/* ❌ BAD: 카드 안 본문이 너무 작아 모바일 가독성 떨어짐 */
.stack-card p { font-size: 1rem; }

/* ✅ GOOD: 본문 -0.5rem 위계 유지 */
.stack-card p { font-size: 1.5rem; }
```

---

## 5. Content-Length Based Layout Decision (CRITICAL — 콘텐츠 양 기반 배치 결정)

> 🚨 **이 섹션은 그리드 사용 전 반드시 확인.**
> 상세페이지는 모바일·데스크톱 모두 **본문 폭 860px 기준 80%**(약 688px)로 좁다. 좁은 폭에서 카드 3개를 가로로 늘어놓으면 카드당 폭 ~200px 남짓. 카드 안 텍스트가 두세 줄을 넘어가면 가독성이 폭락한다.
>
> **원칙: 짧은 카피만 수평 그리드. 그 외는 모두 수직 스택.**

### 빠른 결정 룰

| 한 카드의 본문 텍스트 길이 | 권장 배치 | 비고 |
|---|---|---|
| **단어 1~2개 / ≤ 12자 / 1줄** | `.grid-2`, `.grid-3` 수평 OK | 라벨·태그·옵션명 |
| **짧은 문장 / 13~30자 / 1~2줄** | `.grid-2` 까지 OK, `.grid-3`는 위험 | 짧은 슬로건, 짧은 설명 |
| **2줄 이상 / 30자 초과** | **수직 스택 (`.stack-cards`) 권장** | 본문 설명, 페인포인트, 효과 |
| **여러 문장 / 50자 초과** | **수직 스택 필수** | 스토리, 상세 설명, 페인포인트 풀이 |
| **숫자 강조 1개** | `stat-item` 단독 또는 `.grid-3` | 통계 카드 (숫자만 큼) |

### 의사결정 트리

```
이 섹션이 카드 N개를 보여준다면…
│
├─ 카드당 본문이 12자 이하 (한 줄 라벨 수준)?
│   → grid-2 / grid-3 / grid-4 OK
│
├─ 카드당 본문이 13~30자, 1~2줄?
│   → grid-2 OK, grid-3는 카드 폭 ~210px 가깝다 → 시각적 균형 검토
│
└─ 그 외 (2줄 이상, 또는 강조 단어가 많음)
    → 수직 스택 (.stack-cards) 사용
```

### 카드 + 이미지 결합 (.stack-card.has-image)

카드 안의 텍스트가 길어 그대로 두고 싶지만, 위에 비주얼이 곁들여지면 직관 전달이 강해질 때 사용. 카드 상단에 풀-블리드 이미지가 들어가고 그 아래 텍스트가 배치되는 패턴.

```html
<ul class="stack-cards">
    <li class="card stack-card has-image">
        <img class="card-image" src="../assets/generated/dual-front.png" alt="...">
        <div class="card-body">
            <span class="badge">앞면 · 장모</span>
            <h3 class="section-subtitle">넓게 훑기</h3>
            <p>길고 부드러운 실리콘 모가 그릇 표면을 넓게 감쌉니다...</p>
        </div>
    </li>
</ul>
```

**언제 쓰나:**
- 카드의 텍스트 정보는 유지해야 하지만 인접한 `.full-image` 슬롯이 따로 있어 페이지가 단조로워질 때 — 별도 슬롯을 없애고 카드 안으로 흡수
- 텍스트가 추상적이고 비주얼 한 장으로 즉시 이해가 되는 콘텐츠 (예: "앞면 · 장모 → 사진 한 장이 글보다 빠름")

**주의:**
- `.has-image`를 붙이면 카드의 padding이 0이 됨 → 내부 텍스트는 반드시 `.card-body` 래퍼로 감싸야 함
- 이미지 안에 텍스트가 들어가면 카드 안 텍스트와 중복될 수 있으니, 이미지는 텍스트 없는 비주얼 (SUPPORT 케이스)로 생성

### 수직 스택 (.stack-cards) 패턴

본문 폭(80% = ~688px) 전체를 한 카드가 사용. 카드들이 위에서 아래로 쌓임:

```html
<section id="features" class="content-section">
    <h2 class="section-title">
        <span class="block">알파를 고른</span>
        <span class="block accent">3가지 이유</span>
    </h2>
    <ul class="stack-cards">
        <li class="card stack-card">
            <span class="badge">01</span>
            <h3 class="section-subtitle">양면 디자인</h3>
            <p>부드러운 면과 단단한 면을 한 장에. 손목 한 번 뒤집으면 코팅팬용과 욕실용을 오갑니다.</p>
        </li>
        <li class="card stack-card">
            <span class="badge">02</span>
            <h3 class="section-subtitle">실리콘 100% · KC 인증</h3>
            <p>BPA 무, 환경호르몬 무. 끓는 물 열탕 소독까지 가능합니다.</p>
        </li>
        <li class="card stack-card">
            <span class="badge">03</span>
            <h3 class="section-subtitle">다용도 반영구</h3>
            <p>주방 설거지부터 욕실 청소까지. 일반 스펀지의 20배 수명.</p>
        </li>
    </ul>
</section>
```

```css
.stack-cards {
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.stack-card {
    /* .card 클래스가 이미 처리: 배경/보더/그림자 */
    padding: 36px 40px;
}
.stack-card .badge {
    display: inline-block;
    margin-bottom: 16px;
}
.stack-card .section-subtitle {
    margin-bottom: 12px;
}
.stack-card p {
    line-height: 1.7;
}
```

### 가로형 stat-card-horizontal (또 다른 수직 친화 패턴)

숫자 + 라벨처럼 좁아도 한 줄로 처리할 수 있는 경우는 §6 참조.

### 어떤 콘텐츠가 어떤 그리드?

| 콘텐츠 예시 | 권장 |
|---|---|
| "WHITE / GRAY / MINT" (옵션 라벨 3개) | `.grid-3` |
| "01 / 02 / 03 + 한 줄 설명" | `.grid-3` 또는 `.stack-cards` 둘 다 가능, 텍스트가 짧으면 grid 우선 |
| "99.9% / 6개월 / 70℃" (통계 3개) | `.stats-grid` (숫자 자체가 큼) |
| "특징명 + 1~2문장 설명" 카드 3~4개 | **`.stack-cards`** |
| "페인포인트 체크리스트" | `.checklist` (이미 수직) |
| "리뷰 카드 + 별점 + 한 단락" | **`.stack-cards`** |
| FAQ 질문/답변 | **`.stack-cards`** 또는 details |
| "소재 항목 + 설명" 4개 | 항목당 1줄이면 grid-2x2 OK, 2줄 넘으면 `.stack-cards` |

### 안티패턴 (절대 금지)

```html
<!-- ❌ BAD: 본문 2줄 이상인데 grid-3로 폭 강제 좁힘 -->
<div class="grid-3">
    <div class="card">
        <h3>설거지</h3>
        <p>모든 식기·조리도구.<br>코팅팬도 OK.</p>
    </div>
    <div class="card">
        <h3>과일·채소 세척</h3>
        <p>식품에 안전한 실리콘.<br>잔여물 걱정 없이.</p>
    </div>
    <div class="card">
        <h3>욕실·싱크대</h3>
        <p>뻑뻑한 면으로<br>물때까지 닦입니다.</p>
    </div>
</div>
<!-- → grid-3 카드폭 ~210px. <br>로 줄바꿈 강제 = 카피가 좁혀져 보이고 답답함 -->

<!-- ✅ GOOD: 수직 스택, 한 카드가 전체 본문 폭 사용 -->
<ul class="stack-cards">
    <li class="card stack-card">
        <h3>설거지</h3>
        <p>모든 식기·조리도구를 부드러운 면으로. 코팅팬·강화유리도 흠집 걱정 없습니다.</p>
    </li>
    <li class="card stack-card">
        <h3>과일·채소 세척</h3>
        <p>식품 접촉 등급 실리콘이라 잔여물 걱정 없이 안심하고 사용하세요.</p>
    </li>
    <li class="card stack-card">
        <h3>욕실·싱크대 청소</h3>
        <p>뻑뻑한 면을 활용하면 물때·찌든 때까지 깔끔하게 닦입니다.</p>
    </li>
</ul>
```

---

## 6. Grid System for Cards/Badges (CRITICAL - 카드/뱃지 그리드)

> ⚠️ 이 섹션의 그리드 패턴들은 **§5의 결정 룰을 통과한** 경우(짧은 카피, 라벨, 옵션 등)에만 사용. 그 외에는 `.stack-cards`를 우선 고려하세요.

### 문제 상황

80% 콘텐츠 영역에서 카드/뱃지가 어색하게 배치되는 문제:

```
┌─────────────────────────────────────┐
│ 10% │ [1] [2] [3] │ 10% │           │ ← 3개는 OK
│ 10% │ [1] [2] [3] [밀림] │ 10% │    │ ← 4개: 1개가 아래로 밀림 ❌
└─────────────────────────────────────┘
```

### 해결책 1: Full-Width Grid Section (권장)

카드/뱃지 영역만 full-width로 확장:

```html
<!-- 콘텐츠 섹션 -->
<section id="features" class="content-section">
    <h2>주요 특징</h2>
    <p>설명 텍스트...</p>
</section>

<!-- 카드 그리드는 별도 full-width 섹션 -->
<div id="features-grid" class="full-width-grid">
    <div class="grid-inner grid-4">
        <div class="grid-card">...</div>
        <div class="grid-card">...</div>
        <div class="grid-card">...</div>
        <div class="grid-card">...</div>
    </div>
</div>
```

```css
/* Full-Width Grid Section */
.full-width-grid {
    width: 100%;
    padding: 40px 5%;  /* 좌우 5%만 → 실제 90% 사용 */
}

.grid-inner {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}
```

### 개수별 Grid 클래스

```css
/* 2개 그리드: 한 줄 배치 */
.grid-2 .grid-card {
    flex: 0 0 calc(50% - 10px);
    max-width: calc(50% - 10px);
}

/* 3개 그리드: 한 줄 배치 */
.grid-3 .grid-card {
    flex: 0 0 calc(33.333% - 14px);
    max-width: calc(33.333% - 14px);
}

/* 4개 그리드: 2x2 배치 */
.grid-4 .grid-card {
    flex: 0 0 calc(50% - 10px);  /* 2열 */
    max-width: calc(50% - 10px);
}

/* 5개 그리드: 3-2 교차 배치 */
.grid-5 {
    max-width: 640px;  /* 중앙 정렬을 위한 제한 */
    margin: 0 auto;
}
.grid-5 .grid-card {
    flex: 0 0 calc(33.333% - 14px);  /* 3열 기준 */
    max-width: calc(33.333% - 14px);
}
/* 4,5번째 카드는 자동으로 2열 중앙 정렬 */
```

### 해결책 2: 강제 2열 배치

80% 영역 내에서 무조건 2열로 배치:

```css
.grid-2col {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}
```

### 개수별 권장 레이아웃

| 개수 | 레이아웃 | 방법 |
|------|----------|------|
| 2개 | 1x2 (한 줄) | `.grid-2` - flex 한 줄 |
| 3개 | 1x3 (한 줄) | `.grid-3` - flex 한 줄 또는 full-width |
| 4개 | **2x2** | `.grid-4` - 반드시 2열 배치 |
| 5개 | **3+2 교차** | `.grid-5` - 3열 기준, 중앙 정렬 |
| 6개 | 2x3 또는 3x2 | `.grid-6` - 상황에 따라 선택 |

### 5개 카드 3-2 교차 배치 상세

```
┌─────────────────────────────────────┐
│      [카드1] [카드2] [카드3]         │ ← 3개 중앙 정렬
│         [카드4] [카드5]              │ ← 2개 중앙 정렬
└─────────────────────────────────────┘
```

```css
.grid-5-centered {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    max-width: 580px;  /* 3개 카드 너비 제한 */
    margin: 0 auto;
}

.grid-5-centered .grid-card {
    flex: 0 0 170px;  /* 고정 너비 */
    max-width: 170px;
}
```

---

## 6. Card Text Readability (CRITICAL - 카드 가독성)

### 문제 상황

카드 내 텍스트가 한 글자씩 줄바꿈되는 문제:

```
┌─────────┐  ┌─────────┐  ┌─────────┐
│   ⭐    │  │   📦    │  │   🔄    │
│   4.    │  │  18,    │  │   38   │  ← 숫자가 쪼개짐
│   6     │  │  500    │  │   %    │
│ 평 균   │  │   +     │  │ 재 구  │  ← 한글이 한 글자씩 줄바꿈
│ 평 점   │  │ 누 적   │  │ 매 율  │
│         │  │ 판 매   │  │        │
└─────────┘  └─────────┘  └─────────┘
```

### 해결책: 수평 레이아웃 카드

좁은 카드에 여러 줄 텍스트를 넣지 말고, **수평으로 배치**:

```html
<!-- ❌ BAD - 세로 중앙 정렬 좁은 카드 -->
<div class="grid-card">
    <span class="icon">⭐</span>
    <span class="value">4.6</span>
    <span class="label">평균 평점</span>
</div>

<!-- ✅ GOOD - 수평 레이아웃 와이드 카드 -->
<div class="stat-card-horizontal">
    <span class="icon">⭐</span>
    <div class="stat-content">
        <span class="value">4.6</span>
        <span class="label">평균 평점</span>
    </div>
</div>
```

### 수평 레이아웃 CSS

```css
/* 수평 레이아웃 Stats 카드 */
.stat-card-horizontal {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 24px 28px;
    background: var(--bg-secondary);
    border-radius: 12px;
}
.stat-card-horizontal .icon {
    font-size: 36px;
    flex-shrink: 0;
}
.stat-card-horizontal .stat-content {
    text-align: left;
}
.stat-card-horizontal .value {
    font-size: var(--font-xl);
    font-weight: 800;
    display: block;
    white-space: nowrap;  /* 숫자 줄바꿈 방지 */
}
.stat-card-horizontal .label {
    font-size: var(--font-sm);
    color: var(--text-secondary);
    white-space: nowrap;  /* 라벨 줄바꿈 방지 */
}
```

### 2열 그리드 (좁은 카드 대신)

4개 이상 카드는 3~4열 배치하지 말고 **2열 배치**:

```css
/* 2열 와이드 카드 그리드 */
.stats-grid-2col {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
}
.stats-grid-2col .stat-card-horizontal {
    min-width: 0;  /* grid overflow 방지 */
}
```

### 텍스트 줄바꿈 방지 규칙

| 요소 | CSS 규칙 |
|------|----------|
| 숫자/가격 | `white-space: nowrap` |
| 짧은 라벨 | `white-space: nowrap` |
| 긴 설명 | `min-width: 120px` + `text-align: left` |
| 체크리스트 항목 | 수평 레이아웃 + `text-align: left` |

### 카드 최소 너비 규칙

```css
/* 세로 중앙 정렬 카드 사용 시 최소 너비 */
.grid-card {
    min-width: 160px;  /* 최소 160px 보장 */
}

/* 텍스트가 긴 경우 수평 레이아웃 필수 */
.grid-card-with-description {
    min-width: 200px;
    text-align: left;
}
```

---

## 7. Section Label Alignment (CRITICAL - 레이블 정렬)

### 문제 상황

섹션 레이블과 타이틀의 정렬이 불일치하는 문제:

```
LENOVO CARES              ← 레이블이 왼쪽 정렬됨
    그 마음,              ← 타이틀은 중앙 정렬
    레노버가 알고 있습니다
```

**원인:** `.section-label`이 `display: inline-block`일 때 개별 요소에 `text-align: center`를 적용해도 자기 내부 텍스트만 정렬됨

### 해결책: block + margin auto (REQUIRED)

```css
/* ✅ GOOD - block + margin auto로 중앙 정렬 */
.section-label {
    display: block;
    width: fit-content;
    margin: 0 auto 20px auto;  /* 상: 0, 좌우: auto(중앙), 하: 20px */
    font-size: var(--font-xs);
    font-weight: 600;
    letter-spacing: 2px;
    color: var(--text-muted);
    text-align: center;
}

.section-title {
    text-align: center;
    margin-bottom: 32px;
}

/* 본문은 기본 왼쪽 정렬 유지 */
.body-text {
    text-align: left;  /* 또는 지정 안함 */
}
```

### 올바른 HTML 구조

```html
<!-- ✅ GOOD - 각 요소가 독립적으로 중앙 정렬 -->
<section class="content-section">
    <p class="section-label">LENOVO CARES</p>
    <h2 class="section-title">그 마음, 레노버가 알고 있습니다</h2>
    <p class="body-text">본문은 왼쪽 정렬 유지...</p>  <!-- 영향 없음 -->
</section>
```

### 왜 부모에 text-center를 적용하면 안 되는가

```css
/* ❌ BAD - 부모에 text-center 적용 시 모든 자식이 중앙 정렬됨 */
.content-section.text-center {
    text-align: center;
}
/* → 본문 텍스트, 리스트 등 모든 자식이 의도치 않게 중앙 정렬 */
```

---

## Output Checklist (레이아웃 검증)

HTML 출력 전 확인:

**기본 레이아웃:**
- [ ] Max width 860px
- [ ] `box-sizing: border-box` on all elements
- [ ] `.detail-page` has `overflow-x: hidden`
- [ ] Content sections: `padding: 0 10%` only (no margin, no width)
- [ ] Images in separate `.full-image` sections

**Section IDs:**
- [ ] 모든 `<section>` 요소에 고유 id 부여됨
- [ ] 모든 `.full-image` 요소에 고유 id 부여됨
- [ ] ID 명명 규칙 준수 (영문 소문자, 하이픈 구분)
- [ ] 중복 ID 없음

**Grid Layout:**
- [ ] 4개 카드 → 2x2 배치 (3-1 밀림 방지)
- [ ] 5개 카드 → 3+2 교차 중앙 정렬
- [ ] 카드 그리드는 `.full-width-grid` 또는 `.grid-2col` 사용

**Card Text Readability:**
- [ ] Stats 카드(숫자+라벨)는 수평 레이아웃 사용
- [ ] 숫자/가격에 `white-space: nowrap` 적용
- [ ] 좁은 카드에 여러 줄 텍스트 금지

**Section Label Alignment:**
- [ ] `.section-label`에 `display: block` + `width: fit-content` + `margin: 0 auto` 적용
- [ ] `.section-title`에 `text-align: center` 적용
- [ ] 부모 섹션에 `text-center` 적용 금지
