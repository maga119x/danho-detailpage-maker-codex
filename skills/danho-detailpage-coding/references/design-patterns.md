# Text-to-Design Patterns

긴 텍스트를 그대로 코딩하지 말고, 반드시 디자인 요소로 변환해야 합니다.

## ⚠️ Static Design Principle

**모든 디자인 패턴은 정적 상태에서 완성되어야 합니다.**

- ❌ `:hover`, `:focus` 효과 사용 금지
- ❌ `transition`, `animation` 사용 금지
- ✅ `border`, `box-shadow`로 기본 상태에서 영역 명확화
- ✅ `background` 색상으로 시각적 구분

---

## 🎨 3D Depth (입체감 적용 원칙)

**모든 UI 요소에 입체감을 부여하여 평면적 디자인을 방지합니다.**

### 입체감 3요소

| 요소 | 역할 | 적용 |
|------|------|------|
| **Shadow** | 떠있는 느낌 | `box-shadow` 다중 레이어 |
| **Border** | 경계 명확화 | `border` + `rgba()` 투명도 |
| **Gradient** | 표면감/질감 | `linear-gradient` 미묘한 변화 |

### 요소별 입체감 적용 기준

```css
/* 기본 카드 */
.card {
    background: linear-gradient(180deg, #ffffff 0%, #fafafa 100%);
    border: 1px solid rgba(0,0,0,0.08);
    box-shadow: 0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04);
}

/* 강조 박스 (CTA, 중요 정보) */
.highlight-box {
    background: linear-gradient(180deg, #ffffff 0%, #f8f8f8 100%);
    border: 2px solid var(--accent-primary);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06);
}

/* 버튼 */
.button {
    background: linear-gradient(180deg, #2a2a2a 0%, #000000 100%);
    box-shadow: 0 4px 12px rgba(0,0,0,0.25), inset 0 1px 0 rgba(255,255,255,0.1);
}
```

### 패턴별 입체감 적용 요약

| 패턴 | Shadow Level | Border | Gradient |
|------|--------------|--------|----------|
| 손실 카드 | `--shadow-md` | 4px left (accent) | subtle |
| 문제 박스 | `--shadow-sm` | 1px all | top→bottom |
| 임팩트 박스 | `--shadow-lg` | none | diagonal |
| 크레덴셜 박스 | `--shadow-md` | 2px accent | subtle |
| CTA 섹션 | `--shadow-lg` | accent | 135deg |
| 그리드 카드 | `--shadow-md` | 1px subtle | top→bottom |

---

## 패턴 선택 가이드

| 텍스트 유형 | 키워드/신호 | 적용 패턴 |
|-------------|-------------|-----------|
| 손실/비용 나열 | "→ ~만원", "손실", "비용" | 패턴 1: 카드 그리드 |
| 문제 정의 | "문제는", "~가 아닙니다" | 패턴 2: 강조 박스 |
| 깨달음/전환 | "깨달음", "알게 됨", "늦었습니다" | 패턴 3: 임팩트 박스 |
| 자격/실적 | "N년간", "N명", "경험" | 패턴 4: 크레덴셜 박스 |
| 결론/CTA | "그래서", "~입니다", 가격 | 패턴 5: 하이라이트 섹션 |
| 대비 구조 | "~가 아니라 ~입니다" | Value Proposition 패턴 |
| 특징/기능 나열 | 3~6개 항목 | 그리드 카드 패턴 |

> 🚨 **그리드 vs 수직 스택의 기본 룰**: 그리드 카드 패턴을 적용하기 전, [layout-rules.md §5 "Content-Length Based Layout Decision"](layout-rules.md#5-content-length-based-layout-decision-critical--콘텐츠-양-기반-배치-결정)을 먼저 확인하세요. **카드당 본문이 2줄을 넘으면 grid-3는 거의 항상 잘못된 선택**이고, `.stack-cards`로 수직 배치해야 합니다.

> 🚨 **한국어 헤드라인 끝 마침표(.) 금지**: 한국 광고/이커머스 카피 관례. PLANNING.md의 카피를 HTML로 옮길 때 헤드라인·슬로건·CTA·badge에서 마침표를 제거하세요.
>
> ```html
> <!-- ❌ BAD -->
> <h2 class="section-title">
>     <span class="block">한 장에</span>
>     <span class="block accent">두 가지 면.</span>
> </h2>
> <h3 class="section-subtitle">사용 후기.</h3>
> <a class="cta-button">지금 만나보세요.</a>
>
> <!-- ✅ GOOD -->
> <h2 class="section-title">
>     <span class="block">한 장에</span>
>     <span class="block accent">두 가지 면</span>
> </h2>
> <h3 class="section-subtitle">사용 후기</h3>
> <a class="cta-button">지금 만나보세요</a>
> ```
>
> 물음표(?)·느낌표(!)·쉼표(,)는 허용. 본문 paragraph(`<p>`)와 FAQ 답변은 일반 문장이므로 마침표 정상.
> 상세: [../../danho-detailpage-planning/references/korean-headline-rules.md](../../danho-detailpage-planning/references/korean-headline-rules.md)

> 🚨 **CTA 가격 강조에는 `.stat-item` 금지**: `.stat-item`은 통계 작은 박스 전용 (max-width 180px). 가격을 표시하려고 사용하면 "9,900원"의 "원"이 줄바꿈되고 라벨도 좁게 깨집니다. CTA 가격은 반드시 **`.price-display` + `.price-value` + `.price-unit` + `.price-meta`** 패턴 사용.
>
> ```html
> <!-- ❌ BAD: 가격을 stat-item에 — 폭 좁아서 줄바꿈 깨짐 -->
> <div class="stat-item">
>     <div class="stat-value">9,900<span class="caption">원</span></div>
>     <div class="stat-label">1세트 (3개입) · 무료배송</div>
> </div>
>
> <!-- ✅ GOOD: price-display 패턴 -->
> <div class="price-display">
>     <div class="price-value">9,900<span class="price-unit">원</span></div>
>     <div class="price-meta">1세트 (3개입) · 무료배송</div>
> </div>
> ```
>
> 또한 CTA에 `.section-inverted`를 함께 쓰면 `.cta-section`의 흰 그라데이션이 검정 배경을 덮어써 **흰 글씨가 흰 배경에 묻혀** 보이지 않는 사고가 발생합니다. CTA 섹션은 `.cta-section`만 사용 (section-inverted와 병행 금지).

---

## 패턴 1: 손실/비용 데이터 → 카드 그리드

**기획서 원문:**
```
잘못된 상품 선택 → 20만원 손실
신뢰 없는 업체 선택 → 15만원 손실
무작정 광고비 → 30만원 손실
```

**HTML 변환:**
```html
<div class="loss-grid">
    <div class="loss-card">
        <span class="loss-icon">📦</span>
        <p class="loss-label">잘못된 상품 선택</p>
        <p class="loss-amount">-20<span class="loss-unit">만원</span></p>
    </div>
    <div class="loss-card">
        <span class="loss-icon">🏭</span>
        <p class="loss-label">신뢰 없는 업체 선택</p>
        <p class="loss-amount">-15<span class="loss-unit">만원</span></p>
    </div>
    <div class="loss-card">
        <span class="loss-icon">📢</span>
        <p class="loss-label">무작정 광고비</p>
        <p class="loss-amount">-30<span class="loss-unit">만원</span></p>
    </div>
</div>
<div class="loss-total">
    <p class="loss-total-label">총 손실</p>
    <p class="loss-total-amount">65<span class="loss-unit">만원</span></p>
</div>
```

**CSS:**
```css
.loss-grid {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin: 40px 0;
}

.loss-card {
    background: linear-gradient(180deg, rgba(255, 59, 48, 0.08) 0%, rgba(255, 59, 48, 0.12) 100%);
    border-left: 4px solid #ff3b30;
    border-radius: 8px;
    padding: 24px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 2px 8px rgba(255, 59, 48, 0.1), 0 1px 3px rgba(0,0,0,0.05);
}

.loss-icon { font-size: 32px; flex-shrink: 0; }
.loss-label { flex: 1; font-size: var(--font-sm); color: var(--text-secondary); }
.loss-amount { font-size: var(--font-xl); font-weight: 700; color: #ff3b30; }
.loss-unit { font-size: var(--font-sm); font-weight: 500; }

.loss-total {
    background: linear-gradient(180deg, var(--bg-tertiary) 0%, var(--bg-secondary) 100%);
    border: 1px solid rgba(0,0,0,0.06);
    border-radius: 12px;
    padding: 32px;
    text-align: center;
    margin-top: 24px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04);
}
.loss-total-label { font-size: var(--font-sm); color: var(--text-muted); margin-bottom: 8px; }
.loss-total-amount { font-size: var(--font-3xl); font-weight: 800; color: #ff3b30; }
```

---

## 패턴 2: 문제 정의 → 강조 박스

**기획서 원문:**
```
문제는 시장이 아닙니다.
문제는 시작하는 사람의 90%가 '망하는 패턴'을 그대로 밟는다는 겁니다.
```

**HTML 변환:**
```html
<div class="problem-box">
    <p class="problem-not">문제는 시장이 아닙니다</p>
    <div class="problem-divider"></div>
    <p class="problem-is">
        문제는 시작하는 사람의 <span class="highlight-number">90%</span>가<br>
        <span class="highlight-text">'망하는 패턴'</span>을 그대로 밟는다는 겁니다
    </p>
</div>
```

**CSS:**
```css
.problem-box {
    background: linear-gradient(180deg, var(--bg-secondary) 0%, var(--bg-tertiary) 100%);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 16px;
    padding: 48px 32px;
    text-align: center;
    margin: 40px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.03);
}

.problem-not { font-size: var(--font-md); color: var(--text-muted); margin-bottom: 24px; }
.problem-divider { width: 60px; height: 2px; background: var(--accent-primary); margin: 0 auto 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.problem-is { font-size: var(--font-lg); font-weight: 600; color: var(--text-primary); line-height: 1.6; }
.highlight-number { font-size: var(--font-2xl); font-weight: 800; color: var(--accent-primary); }
.highlight-text { color: var(--accent-primary); font-weight: 700; }
```

---

## 패턴 3: 깨달음/전환점 → 임팩트 박스

**기획서 원문:**
```
총 65만원을 날리고 나서야
'아, 이렇게 하면 안 되는구나' 깨달습니다.
그때는 이미 늦었습니다.
```

**HTML 변환:**
```html
<div class="realization-box">
    <div class="realization-quote">
        <span class="quote-mark">"</span>
        <p class="quote-text">아, 이렇게 하면 안 되는구나</p>
    </div>
    <p class="realization-context">
        총 <span class="context-number">65만원</span>을 날리고 나서야 깨달습니다
    </p>
    <div class="realization-warning">
        <span class="warning-icon">⚠️</span>
        <p class="warning-text">그때는 이미 늦었습니다</p>
    </div>
</div>
```

**CSS:**
```css
.realization-box {
    background: linear-gradient(135deg, var(--bg-tertiary) 0%, var(--bg-secondary) 100%);
    border-radius: 20px;
    padding: 48px 32px;
    text-align: center;
    margin: 40px 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1), 0 4px 12px rgba(0,0,0,0.05);
}

.realization-quote { position: relative; margin-bottom: 32px; }
.quote-mark {
    font-size: 72px;
    color: var(--accent-primary);
    opacity: 0.3;
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    line-height: 1;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.quote-text { font-size: var(--font-xl); font-weight: 600; color: var(--text-primary); padding-top: 24px; }
.realization-context { font-size: var(--font-base); color: var(--text-secondary); margin-bottom: 32px; }
.context-number { font-size: var(--font-lg); font-weight: 700; color: #ff3b30; }

.realization-warning {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: linear-gradient(180deg, rgba(255, 59, 48, 0.08) 0%, rgba(255, 59, 48, 0.15) 100%);
    border: 1px solid rgba(255, 59, 48, 0.2);
    padding: 16px 32px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(255, 59, 48, 0.15);
}
.warning-icon { font-size: 24px; }
.warning-text { font-size: var(--font-md); font-weight: 700; color: #ff3b30; }
```

---

## 패턴 4: 자격/실적 → 크레덴셜 박스

**기획서 원문:**
```
왜하노는 3년간 500명 이상을 가르치며
'어떻게 하면 망하는지'를 정확히 알게 되었습니다.
```

**HTML 변환:**
```html
<div class="credential-box">
    <div class="credential-stats">
        <div class="credential-stat">
            <span class="stat-value">3<span class="stat-unit">년</span></span>
            <span class="stat-label">경력</span>
        </div>
        <div class="credential-divider"></div>
        <div class="credential-stat">
            <span class="stat-value">500<span class="stat-unit">명+</span></span>
            <span class="stat-label">수강생</span>
        </div>
    </div>
    <p class="credential-insight">
        <span class="insight-highlight">"어떻게 하면 망하는지"</span><br>
        정확히 알게 되었습니다
    </p>
</div>
```

**CSS:**
```css
.credential-box {
    background: linear-gradient(180deg, var(--bg-secondary) 0%, var(--bg-tertiary) 100%);
    border: 2px solid var(--accent-primary);
    border-radius: 16px;
    padding: 48px 32px;
    text-align: center;
    margin: 40px 0;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08), 0 3px 6px rgba(0,0,0,0.04);
}

.credential-stats { display: flex; justify-content: center; align-items: center; gap: 32px; margin-bottom: 32px; }
.credential-stat { text-align: center; }
.stat-value { font-size: var(--font-2xl); font-weight: 800; color: var(--accent-primary); display: block; text-shadow: 0 1px 2px rgba(0,0,0,0.1); }
.stat-unit { font-size: var(--font-lg); font-weight: 600; }
.stat-label { font-size: var(--font-xs); color: var(--text-muted); margin-top: 8px; display: block; }
.credential-divider { width: 1px; height: 60px; background: linear-gradient(180deg, transparent 0%, var(--border-light) 20%, var(--border-light) 80%, transparent 100%); }
.credential-insight { font-size: var(--font-md); color: var(--text-secondary); line-height: 1.6; }
.insight-highlight { font-size: var(--font-lg); font-weight: 700; color: var(--text-primary); }
```

---

## 패턴 5: 결론/CTA → 하이라이트 섹션

**기획서 원문:**
```
그래서 이 패키지는
성공 방법을 가르치는 게 아니라
망하는 루트를 차단하는 겁니다.
99,000원짜리 보험입니다.
```

**HTML 변환:**
```html
<div class="conclusion-section">
    <p class="conclusion-setup">그래서 이 패키지는</p>
    <div class="conclusion-contrast">
        <p class="contrast-not">
            <span class="strikethrough">성공 방법을 가르치는 게</span> 아니라
        </p>
        <p class="contrast-is">
            <span class="emphasis">망하는 루트를 차단</span>하는 겁니다
        </p>
    </div>
    <div class="conclusion-cta">
        <p class="cta-price">
            <span class="price-amount">99,000</span><span class="price-unit">원</span>
        </p>
        <p class="cta-metaphor">짜리 <span class="gold">보험</span>입니다</p>
    </div>
</div>
```

**CSS:**
```css
.conclusion-section {
    background: linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
    padding: 80px 10%;
    text-align: center;
}

.conclusion-setup { font-size: var(--font-base); color: var(--text-muted); margin-bottom: 24px; }
.conclusion-contrast { margin-bottom: 48px; }
.contrast-not { font-size: var(--font-md); color: var(--text-secondary); margin-bottom: 16px; }
.strikethrough { text-decoration: line-through; opacity: 0.6; }
.contrast-is { font-size: var(--font-xl); font-weight: 700; color: var(--text-primary); }
.emphasis { color: var(--accent-primary); }

.conclusion-cta {
    background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-dark, #000) 100%);
    color: var(--text-on-dark);
    padding: 40px;
    display: inline-block;
    border-radius: 16px;
    box-shadow:
        0 8px 32px rgba(0,0,0,0.2),
        0 4px 12px rgba(0,0,0,0.15),
        inset 0 1px 0 rgba(255,255,255,0.1);
}
.cta-price { margin-bottom: 8px; }
.price-amount { font-size: var(--font-3xl); font-weight: 800; text-shadow: 0 2px 4px rgba(0,0,0,0.2); }
.price-unit { font-size: var(--font-lg); font-weight: 600; }
.cta-metaphor { font-size: var(--font-md); }
```

---

## Value Proposition 패턴 (대비 구조)

긴 설명 대신 **짧은 대비 구조**로 표현:

**HTML:**
```html
<section class="value-section">
    <div class="value-contrast">
        <p class="value-setup">그래서 우리는</p>
        <p class="value-not">성공을 약속하지 않습니다</p>

        <p class="value-instead">대신</p>
        <p class="value-do"><span class="highlight">실패를 방지</span>합니다</p>
    </div>

    <div class="value-proof">
        <p class="proof-item">
            <span class="number">99,000원</span>으로
            <span class="number">650,000원</span> 리스크를 차단하고
        </p>
        <p class="proof-item">
            <span class="number">3개월</span>을
            <span class="number">7일</span>로 단축합니다
        </p>
    </div>

    <p class="value-conclusion">
        이건 교육이 아니라 <span class="gold">보험</span>입니다
    </p>
</section>
```

**CSS:**
```css
.value-section { padding: 80px 10%; text-align: center; }
.value-contrast { margin-bottom: 48px; }
.value-setup, .value-instead { font-size: var(--font-base); color: var(--text-secondary); margin-bottom: 8px; }
.value-not { font-size: var(--font-xl); font-weight: 600; color: var(--text-primary); margin-bottom: 32px; }
.value-do { font-size: var(--font-2xl); font-weight: 800; color: var(--text-primary); }
.value-proof { margin: 40px 0; }
.proof-item { font-size: var(--font-lg); font-weight: 500; line-height: 1.8; color: var(--text-secondary); }
.proof-item .number { font-size: var(--font-xl); font-weight: 700; color: var(--accent-primary); }
.value-conclusion { font-size: var(--font-xl); font-weight: 700; margin-top: 48px; }
```

---

## 텍스트 스택 패턴 (문단 분리)

긴 텍스트를 문장별로 분리하여 큰 글씨로 표현:

**HTML:**
```html
<section class="section">
    <div class="text-stack">
        <p class="impact-text">이 패턴, 왜하노가 너무 잘 압니다</p>

        <p class="impact-text">
            구매대행으로 돈 벌고 싶은 마음은 간절한데<br>
            혼자 시작하면 어디서부터 해야 할지 <span class="highlight">막막합니다</span>
        </p>

        <p class="key-message">
            문제는 '시작 방법'이 아닙니다<br>
            문제는 <span class="gold">'망하지 않는 기준'</span>을 모른다는 겁니다
        </p>
    </div>
</section>
```

**CSS:**
```css
.text-stack { display: flex; flex-direction: column; gap: 32px; padding: 60px 10%; }
.impact-text { font-size: var(--font-lg); font-weight: 500; line-height: 1.7; color: var(--text-secondary); text-align: center; }
.key-message { font-size: var(--font-xl); font-weight: 700; line-height: 1.6; color: var(--text-primary); text-align: center; margin-top: 20px; }
.highlight { color: var(--text-primary); font-weight: 600; }
.gold, .accent { color: var(--accent-primary); font-weight: 700; }
```

---

## 그리드 카드 패턴 (특징/기능 나열)

**3~6개 항목을 카드로 배치할 때 사용**

### 4개 항목: 2x2 그리드 (CRITICAL)

```html
<div id="features-grid" class="full-width-grid">
    <div class="grid-inner grid-4">
        <div class="grid-card">
            <span class="card-icon">🎯</span>
            <p class="card-title">정확한 분석</p>
            <p class="card-desc">데이터 기반 의사결정</p>
        </div>
        <div class="grid-card">
            <span class="card-icon">💎</span>
            <p class="card-title">프리미엄 품질</p>
            <p class="card-desc">엄선된 원재료</p>
        </div>
        <div class="grid-card">
            <span class="card-icon">⚡</span>
            <p class="card-title">빠른 배송</p>
            <p class="card-desc">주문 후 24시간 내</p>
        </div>
        <div class="grid-card">
            <span class="card-icon">🛡️</span>
            <p class="card-title">안심 보장</p>
            <p class="card-desc">100% 환불 보장</p>
        </div>
    </div>
</div>
```

**CSS:**
```css
.full-width-grid {
    width: 100%;
    padding: 40px 5%;
}

.grid-inner {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
}

.grid-4 .grid-card {
    flex: 0 0 calc(50% - 8px);
    max-width: calc(50% - 8px);
}

.grid-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    /* NO :hover, NO transition */
}

.card-icon { font-size: 36px; display: block; margin-bottom: 12px; }
.card-title { font-size: var(--font-md); font-weight: 700; color: var(--text-primary); margin-bottom: 8px; }
.card-desc { font-size: var(--font-sm); color: var(--text-secondary); }
```

### 5개 항목: 3+2 교차 중앙 정렬

```html
<div id="benefits-grid" class="full-width-grid">
    <div class="grid-inner grid-5">
        <div class="grid-card">카드 1</div>
        <div class="grid-card">카드 2</div>
        <div class="grid-card">카드 3</div>
        <div class="grid-card">카드 4</div>
        <div class="grid-card">카드 5</div>
    </div>
</div>
```

**CSS:**
```css
.grid-5 {
    max-width: 560px;
    margin: 0 auto;
}

.grid-5 .grid-card {
    flex: 0 0 calc(33.333% - 12px);
    max-width: 170px;
}
/* → 3개가 첫 줄, 2개가 둘째 줄 중앙 정렬 */
```

### 배치 규칙 요약

| 개수 | 배치 | 클래스 |
|------|------|--------|
| 2개 | 1x2 한 줄 | `.grid-2` |
| 3개 | 1x3 한 줄 | `.grid-3` |
| 4개 | **2x2** | `.grid-4` |
| 5개 | **3+2 교차** | `.grid-5` |
| 6개 | 3x2 또는 2x3 | `.grid-6` |

---

## 변환 체크리스트

코딩 전 필수 점검:
- [ ] 5줄 이상 연속 텍스트가 있는가? → 반드시 디자인 패턴 적용
- [ ] 숫자/금액이 포함되어 있는가? → 카드 또는 강조 박스
- [ ] "→" 화살표로 나열되어 있는가? → 카드 그리드
- [ ] 인용/깨달음이 있는가? → 임팩트 박스
- [ ] 자격/실적이 있는가? → 크레덴셜 박스
- [ ] 결론/가격이 있는가? → 하이라이트 섹션
- [ ] 3~6개 특징/기능 나열? → 그리드 카드 패턴 (개수별 배치 규칙 준수)
- [ ] 모든 카드/박스에 기본 border, box-shadow 적용되었는가?
- [ ] :hover, transition, animation 사용하지 않았는가?
