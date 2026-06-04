# CSS Examples Reference

## ⚠️ Static Design Principle

**모든 CSS는 정적 상태에서 완성된 디자인이어야 합니다.**

```css
/* ❌ FORBIDDEN */
:hover, :focus { /* 스타일 변경 */ }
transition: any;
animation: any;
@keyframes { }

/* ✅ REQUIRED - 기본 상태에서 완성 */
.card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
```

---

## 🎨 3D Depth System (입체감)

**모든 UI 요소에 입체감을 부여하여 시각적 깊이감을 표현합니다.**

### Shadow Variables (필수 정의)

```css
:root {
    /* Shadow System */
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06);
    --shadow-xl: 0 16px 48px rgba(0,0,0,0.16), 0 8px 16px rgba(0,0,0,0.08);

    /* Inset Shadow (움푹 들어간 느낌) */
    --shadow-inset: inset 0 2px 4px rgba(0,0,0,0.06);
    --shadow-inset-lg: inset 0 4px 8px rgba(0,0,0,0.1);
}
```

### 입체감 카드 (3D Card)

```css
.card-3d {
    background: linear-gradient(180deg, #ffffff 0%, #fafafa 100%);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 12px;
    padding: 24px;
    box-shadow: var(--shadow-md);
}

/* 강조 카드 (더 높이 떠있음) */
.card-3d-elevated {
    background: linear-gradient(180deg, #ffffff 0%, #f8f8f8 100%);
    border: 1px solid rgba(0,0,0,0.06);
    border-radius: 16px;
    padding: 32px;
    box-shadow: var(--shadow-lg);
}

/* Dark Theme 카드 */
.dark-theme .card-3d {
    background: linear-gradient(180deg, #1a1a1a 0%, #141414 100%);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3), 0 2px 4px rgba(0,0,0,0.2);
}
```

### 입체감 버튼 (3D Button)

```css
/* Primary - 볼록한 버튼 */
.btn-3d-primary {
    display: inline-block;
    background: linear-gradient(180deg, #2a2a2a 0%, #000000 100%);
    color: #ffffff;
    padding: 16px 32px;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    box-shadow:
        0 4px 12px rgba(0,0,0,0.25),
        0 2px 4px rgba(0,0,0,0.15),
        inset 0 1px 0 rgba(255,255,255,0.1);
}

/* Secondary - 살짝 떠있는 버튼 */
.btn-3d-secondary {
    display: inline-block;
    background: linear-gradient(180deg, #ffffff 0%, #f5f5f5 100%);
    color: #1a1a1a;
    padding: 16px 32px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-weight: 600;
    box-shadow:
        0 2px 8px rgba(0,0,0,0.08),
        inset 0 1px 0 rgba(255,255,255,0.8);
}

/* Gold (Dark Luxury) - 프리미엄 버튼 */
.btn-3d-gold {
    background: linear-gradient(180deg, #d4b574 0%, #c9a962 100%);
    color: #0a0a0a;
    border: none;
    border-radius: 8px;
    box-shadow:
        0 4px 16px rgba(201, 169, 98, 0.35),
        0 2px 4px rgba(201, 169, 98, 0.2),
        inset 0 1px 0 rgba(255,255,255,0.2);
}
```

### 입체감 섹션 배경

```css
/* 움푹 들어간 섹션 */
.section-inset {
    background: linear-gradient(180deg, #f0f0f0 0%, #f8f8f8 100%);
    box-shadow: var(--shadow-inset);
    padding: 60px 10%;
}

/* 떠있는 콘텐츠 박스 */
.box-elevated {
    background: #ffffff;
    border-radius: 16px;
    padding: 40px;
    box-shadow: var(--shadow-lg);
}

/* 섹션 구분선 (subtle) */
.section-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg,
        transparent 0%,
        rgba(0,0,0,0.1) 20%,
        rgba(0,0,0,0.1) 80%,
        transparent 100%
    );
    margin: 60px 0;
}
```

### 입체감 뱃지

```css
.badge-3d {
    display: inline-block;
    background: linear-gradient(180deg, #333333 0%, #1a1a1a 100%);
    color: #ffffff;
    padding: 8px 16px;
    border-radius: 4px;
    font-size: var(--font-xs);
    font-weight: 600;
    box-shadow: var(--shadow-sm);
}

.badge-3d-light {
    background: linear-gradient(180deg, #ffffff 0%, #f8f8f8 100%);
    color: #1a1a1a;
    border: 1px solid rgba(0,0,0,0.1);
    box-shadow: var(--shadow-sm);
}

.badge-3d-gold {
    background: linear-gradient(135deg, #d4b574 0%, #c9a962 50%, #b8956a 100%);
    color: #0a0a0a;
    box-shadow: 0 2px 8px rgba(201, 169, 98, 0.3);
}
```

### 입체감 입력 필드

```css
.input-3d {
    background: #ffffff;
    border: 1px solid rgba(0,0,0,0.15);
    border-radius: 8px;
    padding: 14px 18px;
    font-size: var(--font-base);
    box-shadow: var(--shadow-inset);
}

/* Dark Theme */
.dark-theme .input-3d {
    background: #0a0a0a;
    border: 1px solid rgba(255,255,255,0.1);
    color: #ffffff;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
}
```

### 테마별 Shadow 강도

```css
/* Clean Minimal - 약한 그림자 */
.minimal-theme {
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02);
    --shadow-md: 0 3px 8px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.03);
    --shadow-lg: 0 6px 16px rgba(0,0,0,0.08), 0 3px 6px rgba(0,0,0,0.04);
}

/* Dark Luxury - 강한 그림자 */
.dark-theme {
    --shadow-sm: 0 2px 6px rgba(0,0,0,0.2), 0 1px 3px rgba(0,0,0,0.15);
    --shadow-md: 0 6px 16px rgba(0,0,0,0.25), 0 3px 6px rgba(0,0,0,0.2);
    --shadow-lg: 0 12px 32px rgba(0,0,0,0.35), 0 6px 12px rgba(0,0,0,0.25);
}

/* Warm Natural - 중간 그림자 (따뜻한 톤) */
.warm-theme {
    --shadow-sm: 0 2px 4px rgba(139,115,85,0.08), 0 1px 2px rgba(139,115,85,0.05);
    --shadow-md: 0 4px 12px rgba(139,115,85,0.1), 0 2px 4px rgba(139,115,85,0.06);
    --shadow-lg: 0 8px 24px rgba(139,115,85,0.15), 0 4px 8px rgba(139,115,85,0.08);
}
```

---

## Layout Base

### Global Overflow Prevention (REQUIRED)
```css
*, *::before, *::after { box-sizing: border-box; }

.detail-page {
    max-width: 860px;
    margin: 0 auto;
    overflow-x: hidden;
}

.detail-page * { max-width: 100%; }

img {
    max-width: 100%;
    height: auto;
    display: block;
}
```

### Content Section (80% width)
```css
.content-section,
.text-section {
    padding: 120px 10%;  /* 상하 120px, 좌우 10% → 콘텐츠 80% */
    /* width, margin 지정하지 않음 */
}
```

### Full-width Image Section
```css
.full-image {
    width: 100%;
    padding: 0;
    margin: 0;
}
.full-image img {
    width: 100%;
    height: auto;
    display: block;
}
```

---

## Grid System (카드/뱃지 레이아웃)

### Full-Width Grid Section
카드/뱃지 영역을 80% 제한에서 벗어나 넓게 배치:

```css
.full-width-grid {
    width: 100%;
    padding: 40px 5%;  /* 좌우 5%만 → 90% 사용 */
}

.grid-inner {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}

.grid-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border-radius: 12px;
    padding: 28px;
    text-align: center;
    /* ⚠️ CRITICAL: 카드 내 텍스트 색상 명시 필수 */
    color: #1a1a1a;  /* 밝은 배경 카드 → 어두운 텍스트 */
}

.grid-card .card-title {
    color: #1a1a1a;  /* 제목은 어두운 색 */
    font-weight: 600;
}

.grid-card .card-text {
    color: #4a4a4a;  /* 본문은 중간 톤 */
}
```

### 개수별 그리드 클래스

```css
/* 2개: 한 줄 배치 */
.grid-2 .grid-card {
    flex: 0 0 calc(50% - 10px);
    max-width: calc(50% - 10px);
}

/* 3개: 한 줄 배치 */
.grid-3 .grid-card {
    flex: 0 0 calc(33.333% - 14px);
    max-width: calc(33.333% - 14px);
}

/* 4개: 2x2 배치 (CRITICAL - 3-1 밀림 방지) */
.grid-4 .grid-card {
    flex: 0 0 calc(50% - 10px);
    max-width: calc(50% - 10px);
}

/* 5개: 3-2 교차 중앙 정렬 */
.grid-5 {
    max-width: 600px;
    margin: 0 auto;
}
.grid-5 .grid-card {
    flex: 0 0 calc(33.333% - 14px);
    max-width: 180px;
}

/* 6개: 3x2 또는 2x3 */
.grid-6 .grid-card {
    flex: 0 0 calc(33.333% - 14px);
    max-width: calc(33.333% - 14px);
}
```

### 콘텐츠 섹션 내 2열 그리드
80% 영역 내에서 강제 2열 배치:

```css
.grid-2col {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.grid-2col .grid-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border-radius: 12px;
    padding: 28px;
}
```

### 사용 예시

```html
<!-- 4개 카드: full-width 2x2 -->
<div class="full-width-grid">
    <div class="grid-inner grid-4">
        <div class="grid-card">
            <span class="card-icon">🎯</span>
            <p class="card-title">특징 1</p>
        </div>
        <div class="grid-card">
            <span class="card-icon">💎</span>
            <p class="card-title">특징 2</p>
        </div>
        <div class="grid-card">
            <span class="card-icon">⚡</span>
            <p class="card-title">특징 3</p>
        </div>
        <div class="grid-card">
            <span class="card-icon">🛡️</span>
            <p class="card-title">특징 4</p>
        </div>
    </div>
</div>

<!-- 5개 카드: 3-2 교차 중앙 정렬 -->
<div class="full-width-grid">
    <div class="grid-inner grid-5">
        <div class="grid-card">카드 1</div>
        <div class="grid-card">카드 2</div>
        <div class="grid-card">카드 3</div>
        <div class="grid-card">카드 4</div>
        <div class="grid-card">카드 5</div>
    </div>
</div>
```

### ⚠️ 타겟 고객/페르소나 카드 (CRITICAL - 가독성)

**긴 설명이 포함된 6개 카드는 3열 배치 시 가독성 문제 발생**

#### 문제: 3열 좁은 카드 (❌ AVOID)
```
┌─────────┐ ┌─────────┐ ┌─────────┐
│   😴    │ │   🎧    │ │   👶    │
│불 면 증 │ │ A S M R │ │육 아 중 │  ← 제목이 한 글자씩 줄바꿈
│으 로   │ │청 취 를 │ │인 부 모 │
│고 생   │ │즐 기 시 │ │님       │
│하 시   │ │는 분    │ │         │
│는 분   │ │         │ │아 기 재 │  ← 설명도 한 글자씩 줄바꿈
│         │ │장 시 간 │ │울 때   │
│A S M R │ │들 기    │ │자 장 가 │
│과...    │ │편 한    │ │나...    │
└─────────┘ └─────────┘ └─────────┘
```

#### 해결책 1: 2열 와이드 카드 (✅ RECOMMENDED)
```
┌────────────────────────────────┐ ┌────────────────────────────────┐
│ 😴 불면증으로 고생하시는 분    │ │ 🎧 ASMR 청취를 즐기시는 분     │
│    ASMR과 백색소음으로 편안한  │ │    장시간 듣기 편한 이어폰을   │
│    숙면을 취하고 싶으신 분     │ │    찾으시는 분                 │
└────────────────────────────────┘ └────────────────────────────────┘
┌────────────────────────────────┐ ┌────────────────────────────────┐
│ 👶 육아 중인 부모님            │ │ 🏢 기숙사/자취생               │
│    아기 재울 때 자장가나 백색  │ │    주변 소음을 차단하고 조용히 │
│    소음을 들려주고 싶으신 분   │ │    쉬고 싶으신 분              │
└────────────────────────────────┘ └────────────────────────────────┘
```

```html
<div class="persona-grid-2col">
    <div class="persona-card">
        <div class="persona-header">
            <span class="persona-icon">😴</span>
            <h4 class="persona-title">불면증으로 고생하시는 분</h4>
        </div>
        <p class="persona-desc">ASMR과 백색소음으로 편안한 숙면을 취하고 싶으신 분</p>
    </div>
    <!-- 나머지 카드들... -->
</div>
```

```css
/* 타겟 고객 카드 - 2열 레이아웃 (RECOMMENDED) */
.persona-grid-2col {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    width: 100%;
}

.persona-card {
    padding: 24px;
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
}

.persona-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}

.persona-icon {
    font-size: 32px;
    flex-shrink: 0;
    line-height: 1;
}

.persona-title {
    font-size: var(--font-md);
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
    line-height: 1.3;
}

.persona-desc {
    font-size: var(--font-base);
    color: var(--text-secondary);
    margin: 0;
    line-height: 1.5;
    text-align: left;
}
```

#### 해결책 2: 리스트 형태 (텍스트가 매우 긴 경우)

```html
<ul class="persona-list">
    <li class="persona-item">
        <span class="persona-icon">😴</span>
        <div class="persona-content">
            <strong class="persona-title">불면증으로 고생하시는 분</strong>
            <span class="persona-desc">ASMR과 백색소음으로 편안한 숙면을 취하고 싶으신 분</span>
        </div>
    </li>
    <!-- 나머지 항목들... -->
</ul>
```

```css
/* 타겟 고객 리스트 형태 */
.persona-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.persona-item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 24px;
    background: var(--bg-secondary);
    border-radius: 12px;
}

.persona-item .persona-icon {
    font-size: 36px;
    flex-shrink: 0;
    line-height: 1;
}

.persona-item .persona-content {
    text-align: left;
}

.persona-item .persona-title {
    font-size: var(--font-md);
    font-weight: 700;
    color: var(--text-primary);
    display: block;
    margin-bottom: 6px;
}

.persona-item .persona-desc {
    font-size: var(--font-base);
    color: var(--text-secondary);
    line-height: 1.5;
}
```

### ⚠️ 소재/재료 카드 (CRITICAL - 가독성)

**소재명 + 설명이 있는 카드는 세로 중앙 정렬 시 가독성 저하**

#### 문제: 좁은 세로 카드 (❌ AVOID)
```
┌─────────┐  ┌─────────┐  ┌─────────┐
│   🧴    │  │   🎨    │  │   🔌    │
│의 료    │  │무 광    │  │고 급    │  ← 제목 한 글자씩
│용 실    │  │A B S    │  │T P E    │
│리 콘    │  │하 우    │  │케 이    │
│이 어    │  │징       │  │블       │
│팁       │  │         │  │         │
│         │  │가 벼    │  │꼬 임    │  ← 설명 한 글자씩
│피 부    │  │지 만    │  │방 지    │
│알 레    │  │내 구    │  │처 리    │
│르 기    │  │성 이    │  │로       │
│테 스    │  │뛰 어    │  │오 래    │
│트 완    │  │난       │  │사 용    │
│료...    │  │소 재    │  │해 도    │
└─────────┘  └─────────┘  └─────────┘
```

#### 해결: 수평 레이아웃 1열 카드 (✅ RECOMMENDED)
```
┌──────────────────────────────────────────────────────────────┐
│ 🧴 의료용 실리콘 이어팁                                      │
│    피부 알레르기 테스트 완료. 장시간 착용해도 자극 없는      │
│    부드러운 실리콘 소재.                                     │
└──────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────┐
│ 🎨 무광 ABS 하우징                                           │
│    가볍지만 내구성이 뛰어난 소재. 땀과 습기에 강해 위생적.   │
└──────────────────────────────────────────────────────────────┘
```

```html
<div class="material-list">
    <div class="material-card">
        <span class="material-icon">🧴</span>
        <div class="material-content">
            <h4 class="material-title">의료용 실리콘 이어팁</h4>
            <p class="material-desc">피부 알레르기 테스트 완료. 장시간 착용해도 자극 없는 부드러운 실리콘 소재.</p>
        </div>
    </div>
    <!-- 나머지 카드들... -->
</div>
```

```css
/* 소재/재료 카드 - 1열 수평 레이아웃 */
.material-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    width: 100%;
}

.material-card {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    padding: 28px;
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
}

.material-icon {
    font-size: 40px;
    flex-shrink: 0;
    line-height: 1;
}

.material-content {
    text-align: left;
    flex: 1;
}

.material-title {
    font-size: var(--font-lg);
    font-weight: 700;
    color: var(--text-primary);
    margin: 0 0 8px 0;
}

.material-desc {
    font-size: var(--font-base);
    color: var(--text-secondary);
    margin: 0;
    line-height: 1.6;
}
```

### 카드 레이아웃 선택 가이드

| 콘텐츠 유형 | 권장 레이아웃 | 근거 |
|-------------|---------------|------|
| 숫자 + 짧은 라벨 (Stats) | 수평 2열 | 숫자 줄바꿈 방지 |
| 이모지 + 짧은 제목 (2~3자) | 세로 3열 OK | 제목이 짧으면 가능 |
| 이모지 + 긴 제목 (4자 이상) | 수평 2열 | 제목 줄바꿈 방지 |
| 제목 + 설명 (1줄) | 수평 2열 | 설명 가독성 |
| 제목 + 설명 (2줄 이상) | 수평 1열 리스트 | 긴 텍스트 가독성 |
| 비교 카드 (X vs ✓) | 2열 고정 | 대비 명확 |

### 비교 카드 (Comparison Cards) - X vs ✓ 패턴

**⚠️ CRITICAL: 비교 카드에서 밝은 배경 + 밝은 텍스트 조합 금지**

```html
<!-- 무선 이어폰 vs 유선 이어폰 비교 예시 -->
<div class="comparison-grid">
    <div class="comparison-card card-negative">
        <span class="card-icon">❌</span>
        <h4 class="card-title">무선 이어폰</h4>
        <ul class="card-list">
            <li>배터리 충전 필요</li>
            <li>블루투스 연결 끊김</li>
            <li>이불 속 분실 위험</li>
        </ul>
    </div>
    <div class="comparison-card card-positive">
        <span class="card-icon">✓</span>
        <h4 class="card-title">유선 이어폰</h4>
        <ul class="card-list">
            <li>꽂으면 즉시 사용</li>
            <li>끊김 없는 안정성</li>
            <li>분실 걱정 없음</li>
        </ul>
    </div>
</div>
```

```css
.comparison-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.comparison-card {
    padding: 28px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

/* ❌ 부정 카드 - 연한 빨강 배경 */
.card-negative {
    background: #ffe4e4;
    border: 1px solid #ffcccc;
}
.card-negative .card-icon {
    color: #dc3545;  /* 진한 빨강 아이콘 */
    font-size: 32px;
}
.card-negative .card-title {
    color: #dc3545;  /* 진한 빨강 제목 */
    font-weight: 700;
}
.card-negative .card-list li {
    color: #4a4a4a;  /* ⚠️ CRITICAL: 본문은 어두운 회색 (밝은 색 금지!) */
}

/* ✓ 긍정 카드 - 연한 노랑/초록 배경 */
.card-positive {
    background: #fff3cd;
    border: 1px solid #ffe69c;
}
.card-positive .card-icon {
    color: #28a745;  /* 진한 초록 아이콘 */
    font-size: 32px;
}
.card-positive .card-title {
    color: #28a745;  /* 진한 초록 제목 */
    font-weight: 700;
}
.card-positive .card-list li {
    color: #4a4a4a;  /* ⚠️ CRITICAL: 본문은 어두운 회색 (밝은 색 금지!) */
}

/* 리스트 기본 스타일 */
.card-list {
    list-style: none;
    padding: 0;
    margin: 16px 0 0 0;
}
.card-list li {
    padding: 8px 0;
    font-size: var(--font-base);
    line-height: 1.5;
}
```

### 카드 텍스트 색상 Quick Reference

| 카드 배경 | 제목 색상 | 본문 색상 | 비고 |
|----------|----------|----------|------|
| `#f8f9fa` (밝은 회색) | `#1a1a1a` | `#4a4a4a` | 표준 밝은 카드 |
| `#ffe4e4` (연한 빨강) | `#dc3545` | `#4a4a4a` | 부정/경고 카드 |
| `#fff3cd` (연한 노랑) | `#28a745` | `#4a4a4a` | 긍정/성공 카드 |
| `#e8f5e8` (연한 초록) | `#2e8b57` | `#2d5a2d` | Fresh Vibrant |
| `#141414` (다크) | `#c9a962` (골드) | `#ffffff` | Dark Luxury |
| `#3d3028` (다크 브라운) | `#faf7f2` | `#e8e4de` | Warm Natural 반전 |

---

## Typography

### Font Scale (Mobile-First, 모바일 가독성 최적화)
```css
:root {
    --font-xs: 24px;       /* 라벨, 캡션 */
    --font-sm: 28px;       /* 작은 텍스트 */
    --font-base: 32px;     /* 본문 */
    --font-md: 36px;       /* 강조 */
    --font-lg: 42px;       /* 소제목 */
    --font-xl: 52px;       /* 섹션 제목 */
    --font-2xl: 68px;      /* 메인 타이틀 */
    --font-3xl: 84px;      /* 히어로 헤드라인 */
    --font-display: 100px; /* 특별 디스플레이 */
}
```

### Font Weight Usage
```css
body { font-weight: 500; }           /* 기본 본문 */
.subheading { font-weight: 600; }    /* 소제목 */
.section-title { font-weight: 700; } /* 섹션 제목 */
.main-title { font-weight: 800; }    /* 메인 타이틀 */
```

### Word Break Control
```css
.brand-name,
.product-name,
.price,
.badge {
    word-break: keep-all;
    white-space: nowrap;
}

.body-text {
    word-break: keep-all;
    overflow-wrap: break-word;
}

p, h1, h2, h3, h4, h5, h6, span, li {
    overflow-wrap: break-word;
    word-wrap: break-word;
}
```

### ⚠️ Section Label & Title Alignment (CRITICAL)

**섹션 레이블과 타이틀 정렬이 불일치하는 문제 방지**

#### 문제: inline-block 요소에 text-center 직접 적용 (❌)
```
LENOVO CARES              ← 레이블이 왼쪽 정렬됨
    그 마음,              ← 타이틀은 중앙 정렬
    레노버가 알고 있습니다
```

```html
<!-- ❌ BAD - inline-block에 text-center 적용 -->
<section class="content-section">
    <p class="section-label text-center">LENOVO CARES</p>  <!-- 정렬 안됨! -->
    <h2 class="section-title text-center">그 마음, 레노버가...</h2>
</section>
```

```css
/* 원인: inline-block 요소에 text-align은 내부 텍스트만 정렬 */
.section-label {
    display: inline-block;  /* 이 요소 자체는 부모의 정렬을 따름 */
}
```

#### 해결: block + margin auto (✅ REQUIRED)
```
         LENOVO CARES           ← 레이블도 중앙 정렬
           그 마음,             ← 타이틀도 중앙 정렬
    레노버가 알고 있습니다

    본문 텍스트는 왼쪽 정렬...  ← 본문은 영향 없음
```

```html
<!-- ✅ GOOD - 각 요소가 독립적으로 중앙 정렬 -->
<section class="content-section">
    <p class="section-label">LENOVO CARES</p>
    <h2 class="section-title title-gradient title-shadow">그 마음, 레노버가...</h2>
    <p class="body-text">본문 텍스트는 왼쪽 정렬 유지...</p>
</section>
```

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
    text-align: left;
}
```

#### ❌ 왜 부모에 text-center를 적용하면 안 되는가

```html
<!-- ❌ BAD - 부모에 text-center 적용 -->
<section class="content-section text-center">
    <p class="section-label">LENOVO CARES</p>  <!-- 중앙 정렬됨 -->
    <h2 class="section-title">제목...</h2>      <!-- 중앙 정렬됨 -->
    <p class="body-text">본문...</p>            <!-- 본문도 중앙 정렬됨! (의도치 않음) -->
    <ul class="checklist">...</ul>              <!-- 체크리스트도 중앙 정렬됨! -->
</section>
```

부모에 `text-center`를 적용하면 **모든 자식 요소**가 중앙 정렬되어 본문, 리스트 등이 의도치 않게 중앙 정렬됩니다.

#### 필수 CSS 패턴 요약

```css
/* 섹션 레이블 - block + margin auto (REQUIRED) */
.section-label {
    display: block;
    width: fit-content;
    margin: 0 auto 20px auto;
    text-align: center;
}

/* 섹션 타이틀 - text-align center */
.section-title {
    text-align: center;
}

/* 본문은 왼쪽 정렬 유지 (기본값) */
.body-text {
    /* text-align 지정 안함 또는 left */
}
```

---

## Buttons & Badges

**⚠️ 정적 디자인: 호버 효과 없이 기본 상태에서 완성된 스타일**

### Primary Button
```css
.cta-button {
    display: inline-block;
    background: linear-gradient(180deg, #2a2a2a 0%, #000000 100%);
    color: #ffffff;
    border: none;
    padding: 24px 48px;  /* 증가된 패딩 (터치 영역 확대) */
    font-family: 'Paperlogy', sans-serif;
    font-weight: 600;
    font-size: var(--font-md);
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);  /* 정적 그림자 */
    text-decoration: none;
    /* NO :hover, NO transition */
}
```

### Secondary Button
```css
.cta-button-secondary {
    display: inline-block;
    background: linear-gradient(180deg, #ffffff 0%, #f5f5f5 100%);
    border: 2px solid #e0e0e0;  /* 테두리로 영역 명확화 */
    color: #1a1a1a;
    padding: 24px 48px;  /* 증가된 패딩 (터치 영역 확대) */
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    text-decoration: none;
}
```

### Badge
```css
.badge {
    display: inline-block;
    background: linear-gradient(180deg, #333333 0%, #1a1a1a 100%);
    color: #ffffff;
    padding: 10px 20px;  /* 증가된 패딩 */
    font-size: var(--font-xs);
    font-weight: 600;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.badge-light {
    background: linear-gradient(180deg, #ffffff 0%, #f8f8f8 100%);
    border: 1px solid #e5e5e5;
    color: #1a1a1a;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.badge-outline {
    background: transparent;
    border: 1.5px solid var(--accent-primary);
    color: var(--accent-primary);
}
```

### Dark Luxury Theme Buttons
```css
/* Dark Luxury - CTA Button */
.dark-luxury .cta-button {
    background: linear-gradient(180deg, #d4b574 0%, #c9a962 100%);
    color: #0a0a0a;
    box-shadow: 0 4px 16px rgba(201, 169, 98, 0.3);  /* 골드 글로우 */
}

/* Dark Luxury - Badge */
.dark-luxury .badge {
    background: linear-gradient(180deg, #d4b574 0%, #b8956a 100%);
    color: #0a0a0a;
    box-shadow: 0 2px 8px rgba(201, 169, 98, 0.2);
}
```

---

## Checklist Components

### ⚠️ CRITICAL: 텍스트 체크박스 기호 변환 규칙

**기획서에 `☐`, `□`, `■` 등 텍스트 체크박스 기호가 있으면 반드시 SVG 아이콘으로 변환합니다.**

```
기획서 입력:                     HTML 출력:
☐ 고민 1                   →    <li><span class="check-icon"><svg>...</svg></span><span>고민 1</span></li>
□ 고민 2                   →    <li><span class="check-icon"><svg>...</svg></span><span>고민 2</span></li>
• 고민 3                   →    <li><span class="check-icon"><svg>...</svg></span><span>고민 3</span></li>
```

**절대 금지:**
- `☐`, `□`, `■`, `▢`, `◻` 등 유니코드 체크박스 기호를 텍스트로 출력
- 체크박스 기호를 그대로 HTML에 포함

**필수 변환:**
- 모든 체크리스트 항목은 SVG 아이콘 + 텍스트 조합으로 변환
- 기본 스타일: Style 5 (Bullet Square) 권장 - 스크린샷과 유사한 디자인

---

### Style 1: SVG Circle Check (권장)
```html
<ul class="checklist checklist-circle">
    <li>
        <span class="check-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="11" stroke="currentColor" stroke-width="1.5" fill="none"/>
                <path d="M7 12.5L10.5 16L17 9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </span>
        <span class="check-text">체크리스트 항목</span>
    </li>
</ul>
```

```css
.checklist-circle {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.checklist-circle li { display: flex; align-items: center; gap: 14px; }
.checklist-circle .check-icon { flex-shrink: 0; width: 24px; height: 24px; color: var(--accent-primary); }
.checklist-circle .check-text { font-size: var(--font-base); font-weight: 500; color: var(--text-primary); line-height: 1.5; }
```

### Style 2: Filled Circle Check
```html
<svg width="22" height="22" viewBox="0 0 22 22" fill="none">
    <circle cx="11" cy="11" r="11" fill="currentColor"/>
    <path d="M6 11L9.5 14.5L16 8" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

### Style 3: Minimal Line Check
```html
<svg width="20" height="20" viewBox="0 0 20 20" fill="none">
    <path d="M4 10L8 14L16 6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

### Style 4: Boxed Check
```html
<svg width="18" height="18" viewBox="0 0 18 18" fill="none">
    <rect x="1" y="1" width="16" height="16" rx="3" stroke="currentColor" stroke-width="1.5"/>
    <path d="M5 9L8 12L13 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

```css
.checklist-boxed li {
    background: var(--bg-secondary);
    padding: 16px 20px;
    border-radius: 8px;
}
```

### Style 5: Bullet Square (페인포인트 리스트용 - 권장)

**기획서의 체크리스트/페인포인트 리스트에 사용 (☐, □ 기호 대체)**

```html
<ul class="checklist checklist-bullet">
    <li>
        <span class="bullet-icon">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <rect x="1" y="1" width="14" height="14" rx="2" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
            </svg>
        </span>
        <span class="check-text">잠들기 전 ASMR을 듣고 싶은데 무선 이어폰은 충전이 불안해요</span>
    </li>
    <li>
        <span class="bullet-icon">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <rect x="1" y="1" width="14" height="14" rx="2" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
            </svg>
        </span>
        <span class="check-text">옆 사람 방해 없이 편안하게 수면 음악을 듣고 싶어요</span>
    </li>
</ul>
```

```css
/* 페인포인트/공감 리스트 스타일 (RECOMMENDED for ☐ replacement) */
.checklist-bullet {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.checklist-bullet li {
    display: flex;
    align-items: flex-start;
    gap: 16px;
}

.checklist-bullet .bullet-icon {
    flex-shrink: 0;
    width: 16px;
    height: 16px;
    margin-top: 8px;  /* 텍스트 첫 줄과 정렬 */
    color: var(--text-muted);
}

.checklist-bullet .check-text {
    font-size: var(--font-base);
    font-weight: 500;
    color: var(--text-secondary);
    line-height: 1.6;
}

/* Dark Theme */
.dark-theme .checklist-bullet .bullet-icon {
    color: var(--accent-primary);
}
```

**사용 시나리오:**
- 기획서에 `☐`, `□`, `•` 기호가 있는 페인포인트 리스트
- "혹시 이런 고민 하셨나요?" 섹션
- 공감 체크리스트 영역

---

### Style 6: Emoji Check
```html
<ul class="checklist checklist-emoji">
    <li>
        <span class="check-emoji">✨</span>
        <span class="check-text">새로운&nbsp;시작을 앞두고&nbsp;계신&nbsp;분</span>
    </li>
</ul>
```

```css
.checklist-emoji { list-style: none; padding: 0; display: flex; flex-direction: column; gap: 18px; }
.checklist-emoji li { display: flex; align-items: center; gap: 12px; }
.checklist-emoji .check-emoji { font-size: 22px; line-height: 1; flex-shrink: 0; }
```

### ⚠️ 체크리스트 카드 그리드 - 가독성 주의 (CRITICAL)

**체크리스트를 좁은 카드 그리드로 배치하면 가독성 저하**

#### 문제: 3열 체크리스트 카드 (❌ AVOID)
```
┌─────────┐  ┌─────────┐  ┌─────────┐
│   ✅    │  │   ✅    │  │   ✅    │
│   92    │  │   87    │  │   83    │
│   %     │  │   %     │  │   %     │
│"입 면   │  │"더 깊   │  │"아 침   │  ← 한 글자씩 줄바꿈
│시 간    │  │은 잠    │  │에 개    │
│이 줄    │  │을 잤    │  │운 해    │
│었 어    │  │어 요"   │  │요"      │
│요"      │  │         │  │         │
└─────────┘  └─────────┘  └─────────┘
```

#### 해결: 수평 레이아웃 카드 (✅ RECOMMENDED)
```
┌────────────────────────────────────────────────────────────────┐
│ ✅  92%  "입면 시간이 줄었어요"                                │
└────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────┐
│ ✅  87%  "더 깊은 잠을 잤어요"                                 │
└────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────┐
│ ✅  83%  "아침에 개운해요"                                     │
└────────────────────────────────────────────────────────────────┘
```

```html
<div class="survey-results">
    <div class="survey-card">
        <span class="survey-icon">✅</span>
        <span class="survey-percent">92%</span>
        <span class="survey-text">"입면 시간이 줄었어요"</span>
    </div>
    <div class="survey-card">
        <span class="survey-icon">✅</span>
        <span class="survey-percent">87%</span>
        <span class="survey-text">"더 깊은 잠을 잤어요"</span>
    </div>
    <div class="survey-card">
        <span class="survey-icon">✅</span>
        <span class="survey-percent">83%</span>
        <span class="survey-text">"아침에 개운해요"</span>
    </div>
</div>
```

```css
/* 설문 결과/체크리스트 - 수평 1열 레이아웃 */
.survey-results {
    display: flex;
    flex-direction: column;
    gap: 12px;
    width: 100%;
}

.survey-card {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 20px 24px;
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
}

.survey-icon {
    font-size: 28px;
    flex-shrink: 0;
    line-height: 1;
}

.survey-percent {
    font-size: var(--font-2xl);
    font-weight: 800;
    color: var(--text-primary);
    flex-shrink: 0;
    white-space: nowrap;
    min-width: 80px;
}

.survey-text {
    font-size: var(--font-base);
    color: var(--text-secondary);
    font-style: italic;
}
```

#### 대안: 2열 그리드 (카드 너비 확보)

```css
/* 설문 결과 2열 그리드 (최소 너비 확보) */
.survey-grid-2col {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
}

.survey-card-wide {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 28px 24px;
    background: var(--bg-secondary);
    border-radius: 12px;
    text-align: center;
    min-width: 200px;  /* CRITICAL: 최소 너비 보장 */
}

.survey-card-wide .survey-percent {
    font-size: var(--font-3xl);
    font-weight: 800;
    white-space: nowrap;
    margin-bottom: 8px;
}

.survey-card-wide .survey-text {
    font-size: var(--font-base);
    line-height: 1.4;
    white-space: normal;  /* 텍스트는 자연스럽게 줄바꿈 */
    word-break: keep-all;  /* 단어 단위 줄바꿈 */
}
```

---

## Social Proof Components

### ⚠️ Stats Grid - 가독성 최적화 버전 (RECOMMENDED)

**세로 중앙 정렬 좁은 카드는 가독성 문제를 유발합니다. 수평 레이아웃을 사용하세요.**

#### 문제: 좁은 세로 카드 (❌ AVOID)
```
┌─────────┐  ┌─────────┐
│   ⭐    │  │   📦    │
│   4.    │  │  18,    │  ← 숫자가 쪼개짐
│   6     │  │  500    │
│ 평 균   │  │   +     │  ← 한글 한 글자씩 줄바꿈
│ 평 점   │  │ 누 적   │
└─────────┘  └─────────┘
```

#### 해결: 수평 레이아웃 2열 그리드 (✅ RECOMMENDED)
```
┌──────────────────────────┐  ┌──────────────────────────┐
│ ⭐  4.6                  │  │ 📦  18,500+              │
│     평균 평점            │  │     누적 판매            │
└──────────────────────────┘  └──────────────────────────┘
┌──────────────────────────┐  ┌──────────────────────────┐
│ 🔄  38%                  │  │ 💬  2,847개              │
│     재구매율             │  │     실사용 리뷰          │
└──────────────────────────┘  └──────────────────────────┘
```

```html
<div class="stats-grid-horizontal">
    <div class="stat-card-h">
        <span class="stat-icon">⭐</span>
        <div class="stat-content">
            <span class="stat-value">4.6</span>
            <span class="stat-label">평균 평점</span>
        </div>
    </div>
    <div class="stat-card-h">
        <span class="stat-icon">📦</span>
        <div class="stat-content">
            <span class="stat-value">18,500+</span>
            <span class="stat-label">누적 판매</span>
        </div>
    </div>
    <div class="stat-card-h">
        <span class="stat-icon">🔄</span>
        <div class="stat-content">
            <span class="stat-value">38%</span>
            <span class="stat-label">재구매율</span>
        </div>
    </div>
    <div class="stat-card-h">
        <span class="stat-icon">💬</span>
        <div class="stat-content">
            <span class="stat-value">2,847개</span>
            <span class="stat-label">실사용 리뷰</span>
        </div>
    </div>
</div>
```

```css
/* 수평 레이아웃 Stats Grid (RECOMMENDED) */
.stats-grid-horizontal {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    width: 100%;
}

.stat-card-h {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 24px 28px;
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
}

.stat-card-h .stat-icon {
    font-size: 36px;
    flex-shrink: 0;
    line-height: 1;
}

.stat-card-h .stat-content {
    text-align: left;
    min-width: 0;  /* flex overflow 방지 */
}

.stat-card-h .stat-value {
    font-size: var(--font-xl);
    font-weight: 800;
    color: var(--text-primary);
    display: block;
    white-space: nowrap;  /* 숫자 줄바꿈 방지 (CRITICAL) */
}

.stat-card-h .stat-label {
    font-size: var(--font-sm);
    color: var(--text-secondary);
    display: block;
    margin-top: 4px;
    white-space: nowrap;  /* 라벨 줄바꿈 방지 */
}
```

#### 세로 카드 사용 시 주의 (레거시)
**꼭 세로 카드를 사용해야 한다면 최소 너비를 보장하세요:**

```css
/* 레거시: 세로 중앙 정렬 카드 (가독성 주의) */
.stats-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    width: 100%;
    max-width: 100%;
}

.stat-item {
    flex: 1 1 160px;  /* 최소 160px (100px → 160px 증가) */
    max-width: 200px;  /* 최대 200px (180px → 200px 증가) */
    min-width: 160px;  /* CRITICAL: 최소 너비 보장 */
    padding: 28px 20px;  /* 패딩 증가 */
    text-align: center;
    background: var(--bg-secondary);
    border-radius: 12px;
    box-sizing: border-box;
}

.stat-value {
    font-size: var(--font-2xl);
    font-weight: 800;
    white-space: nowrap;  /* CRITICAL: 숫자 줄바꿈 방지 */
}

.stat-label {
    white-space: nowrap;  /* CRITICAL: 라벨 줄바꿈 방지 */
}
```

### Review Cards
```css
.review-grid {
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
    max-width: 100%;  /* CRITICAL */
}

.review-card {
    width: 100%;
    max-width: 100%;  /* CRITICAL */
    padding: 28px;
    background: var(--bg-secondary);
    border-radius: 12px;
    box-sizing: border-box;  /* CRITICAL */
}

.review-text {
    width: 100%;
    word-break: keep-all;
    overflow-wrap: break-word;  /* CRITICAL */
    color: var(--text-primary);
}
```

### Trust Badges
```css
.trust-badges {
    display: flex;
    flex-wrap: wrap;  /* CRITICAL */
    justify-content: center;
    gap: 16px;
    width: 100%;
    max-width: 100%;
}

.trust-badge {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    background: var(--bg-secondary);
    border-radius: 24px;
    white-space: nowrap;
}

.badge-emoji { font-size: 18px; }
.badge-text { font-size: var(--font-sm); font-weight: 500; color: var(--text-primary); }
```

---

## Hero Section

```css
.hero-section {
    background: linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-tertiary) 100%);
}

.hero-text {
    padding: 100px 10% 80px;
    text-align: center;
}

.hero-image {
    width: 100%;
}

.hero-image img {
    width: 100%;
    height: auto;
    display: block;
}

.brand-mark {
    font-size: var(--font-sm);
    letter-spacing: 2px;
    color: var(--text-muted);
    margin-bottom: 16px;
}

.hero-product-name {
    font-size: var(--font-lg);
    font-weight: 600;
    color: var(--accent-primary);
    margin-bottom: 24px;
}

.main-title {
    font-size: var(--font-2xl);
    font-weight: 800;
    line-height: 1.3;
    color: var(--text-primary);
    margin-bottom: 24px;
}

.hero-tagline {
    font-size: var(--font-md);
    color: var(--text-secondary);
}
```

---

## Utility Classes

```css
.block { display: block; }
.gold, .accent { color: var(--accent-primary); font-weight: 700; }
.highlight { color: var(--text-primary); font-weight: 600; }
.strikethrough { text-decoration: line-through; opacity: 0.6; }
.text-center { text-align: center; }
.text-muted { color: var(--text-muted); }
```

---

## Emoji Icons

```css
.emoji-icon-lg { font-size: 48px; line-height: 1; }
.emoji-icon-xl { font-size: 64px; line-height: 1; }
.emoji-icon-md { font-size: 32px; line-height: 1; }
.emoji-icon-sm { font-size: 20px; line-height: 1; }
```

**Recommended Emoji:**
| Category | Emoji |
|----------|-------|
| 품질/프리미엄 | 💎 ✨ 🏆 👑 ⭐ |
| 배송/서비스 | 🚚 📦 🎁 ✅ 💫 |
| 보증/신뢰 | 🛡️ ✓ 🔒 📜 💯 |
| 재물/행운 | 💰 🍀 🌟 ✨ 🎯 |
| 건강/웰니스 | 🧘 💚 🌿 🌱 ♻️ |
| 시간/긴급 | ⏰ 🔥 ⚡ 🚀 💨 |
