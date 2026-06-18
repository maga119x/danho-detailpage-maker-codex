# Static Design Principle (정적 디자인 원칙)

**상세페이지의 모든 디자인은 정적 상태에서 완성되어야 합니다.**

---

## CRITICAL: 정적 디자인 필수 규칙

호버, 애니메이션, 트랜지션 효과를 **절대 사용하지 않습니다.**

| 금지 항목 | 설명 |
|----------|------|
| `:hover` | 마우스 오버 시 스타일 변경 금지 |
| `:focus` | 포커스 시 스타일 변경 금지 |
| `transition` | 전환 효과 금지 |
| `animation` | 애니메이션 금지 |
| `@keyframes` | 키프레임 애니메이션 금지 |
| JavaScript | 인터랙션 스크립트 금지 |

---

## 왜 정적 디자인인가?

### 1. 호버 효과의 문제점
- 호버 시에만 보이는 효과는 **정적 상태에서 디자인이 허전해 보임**
- 카드, 마감 노트 등이 평범하고 밋밋하게 보이는 원인

### 2. 이커머스 상세페이지 특성
- 사용자는 **스크롤하며 읽는 콘텐츠** → 인터랙션 불필요
- 긴 스크롤 페이지에서 호버 효과는 의미 없음

### 3. 모바일 사용자 고려
- 모바일 사용자는 **호버 불가능** → 호버 효과는 무의미
- 터치 기반 환경에서 호버는 작동하지 않음

---

## Static Alternatives (정적 대안)

호버 효과 대신 **기본 상태에서 디자인을 완성**합니다.

| 호버 효과 대신 | 정적 대안 |
|---------------|----------|
| `hover: scale` | 기본 상태에서 적절한 크기와 여백 |
| `hover: shadow` | 기본 상태에서 `box-shadow` 적용 |
| `hover: border` | 기본 상태에서 `border` 표시 |
| `hover: background` | 기본 상태에서 배경색 구분 |
| `transition` | 사용 금지 |
| `animation` | 사용 금지 |

---

## FORBIDDEN CSS (금지된 CSS)

아래 CSS 패턴은 **절대 사용하지 않습니다.**

```css
/* ❌ FORBIDDEN - 호버 효과 */
.card:hover {
    transform: scale(1.05);
}

.interactive-control:hover {
    background: #333;
}

.link:hover {
    color: #0066cc;
}

/* ❌ FORBIDDEN - 트랜지션 */
.element {
    transition: all 0.3s;
}

.card {
    transition: transform 0.2s ease;
}

.interactive-control {
    transition: background-color 0.3s, box-shadow 0.3s;
}

/* ❌ FORBIDDEN - 애니메이션 */
* {
    animation: fadeIn 0.5s;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.element {
    animation: pulse 2s infinite;
}

/* ❌ FORBIDDEN - 포커스 스타일 변경 */
.input:focus {
    border-color: #0066cc;
    box-shadow: 0 0 5px rgba(0, 102, 204, 0.5);
}
```

---

## REQUIRED CSS (필수 CSS)

기본 상태에서 완성된 디자인을 위한 CSS 패턴입니다.

### 카드 컴포넌트

```css
/* ✅ REQUIRED - 기본 상태에서 완성된 카드 */
.card {
    background: #f8f9fa;
    border: 1px solid #e0e0e0;  /* 테두리로 영역 명확화 */
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);  /* 그림자로 깊이감 */
    padding: 24px;
}

/* 그라데이션 배경으로 입체감 추가 */
.card-elevated {
    background: linear-gradient(180deg, #ffffff 0%, #fafafa 100%);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 12px;
    box-shadow:
        0 4px 12px rgba(0,0,0,0.08),
        0 2px 4px rgba(0,0,0,0.04);
}
```

### 정적 마감 노트 컴포넌트

```css
/* ✅ REQUIRED - Static closing note (구매 행동 문구가 아닌 마감 인상) */
.closing-note {
    display: block;
    color: #1a1a1a;
    font-weight: 700;
    letter-spacing: 0;
    padding: 18px 0 0;
    border-top: 1px solid rgba(0,0,0,0.14);
}
```

### 그림자 시스템 (Shadow Levels)

```css
:root {
    /* Level 1: 살짝 떠있음 (기본 카드, 뱃지) */
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);

    /* Level 2: 중간 높이 (강조 카드, 입력 정보) */
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04);

    /* Level 3: 높이 떠있음 (CTA, 중요 요소) */
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06);

    /* Level 4: 최상위 (모달, 팝업) */
    --shadow-xl: 0 16px 48px rgba(0,0,0,0.16), 0 8px 16px rgba(0,0,0,0.08);
}
```

### 섹션 배경 입체감

```css
/* ✅ REQUIRED - 움푹 들어간 섹션 */
.inset-section {
    background: linear-gradient(180deg, #f0f0f0 0%, #f8f8f8 100%);
    box-shadow: inset 0 2px 8px rgba(0,0,0,0.06);
}

/* ✅ REQUIRED - 떠있는 콘텐츠 박스 */
.elevated-box {
    background: #ffffff;
    border-radius: 16px;
    box-shadow:
        0 8px 32px rgba(0,0,0,0.1),
        0 4px 12px rgba(0,0,0,0.05);
}
```

### Dark Theme 카드

```css
/* ✅ REQUIRED - 다크 테마 카드 */
.dark-theme .card {
    background: linear-gradient(180deg, #1a1a1a 0%, #141414 100%);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow:
        0 4px 12px rgba(0,0,0,0.3),
        0 2px 4px rgba(0,0,0,0.2);
}
```

---

## 요소별 입체감 적용 가이드

| 요소 | Shadow | Border | Gradient |
|------|--------|--------|----------|
| 카드 | `--shadow-md` | 1px solid | 배경 subtle |
| 뱃지 | `--shadow-sm` | optional | subtle |
| 입력 필드 | inset shadow | 1px solid | none |
| 섹션 구분 | `--shadow-sm` | bottom only | none |
| 마감 인상 박스 | `--shadow-lg` | accent color | diagonal |

---

## Output Checklist (정적 디자인)

HTML 제출 전 확인 사항:

- [ ] NO JavaScript
- [ ] NO CSS animations (`@keyframes`, `animation`)
- [ ] NO CSS transitions (`transition`)
- [ ] NO `:hover` effects (스타일 변경 금지)
- [ ] NO `:focus` effects (스타일 변경 금지)
- [ ] 모든 디자인 요소가 기본 상태에서 완성되어 보임
- [ ] 카드에 기본 상태 `box-shadow`, `border` 적용됨
- [ ] 버튼 UI, `.cta-button`, 링크 버튼, 버튼처럼 보이는 둥근 CTA 그래픽이 없음
- [ ] 마지막 영역은 상품/결과 마감 문구, 제품 이미지, 구분선으로 마무리되며 옵션/혜택/주문 cue를 포함하지 않음
