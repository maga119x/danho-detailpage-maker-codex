# 3D Depth Design (입체감 디자인)

**모든 UI 요소에 입체감을 부여하여 시각적 깊이감을 표현합니다.**

---

## 입체감의 3요소

```
┌─────────────────────────────────────┐
│  1. SHADOW (그림자) - 떠있는 느낌    │
│  2. BORDER (테두리) - 경계 명확화    │
│  3. GRADIENT (그라데이션) - 표면감   │
└─────────────────────────────────────┘
```

| 요소 | 역할 | 효과 |
|------|------|------|
| **Shadow** | 요소가 떠있는 느낌 | 깊이감, 레이어 구분 |
| **Border** | 영역 경계 명확화 | 구조 강조, 분리감 |
| **Gradient** | 표면의 질감 표현 | 입체감, 고급스러움 |

---

## Shadow System (레이어별 그림자)

### CSS 변수 정의

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

### Shadow Level 비교

| Level | 변수 | 높이 느낌 | 용도 |
|-------|------|-----------|------|
| **sm** | `--shadow-sm` | 살짝 떠있음 | 기본 카드, 뱃지, 태그 |
| **md** | `--shadow-md` | 중간 높이 | 강조 카드, 입력 정보 |
| **lg** | `--shadow-lg` | 높이 떠있음 | 중요 카드, 증거 박스 |
| **xl** | `--shadow-xl` | 최상위 | 모달, 팝업, 오버레이 |

---

## 요소별 입체감 적용 (REQUIRED)

| 요소 | Shadow | Border | Gradient |
|------|--------|--------|----------|
| 카드 | `--shadow-md` | 1px solid | 배경 subtle |
| 뱃지 | `--shadow-sm` | optional | subtle |
| 입력 필드 | inset shadow | 1px solid | none |
| 섹션 구분 | `--shadow-sm` | bottom only | none |
| 마감 인상 박스 | `--shadow-lg` | accent color | diagonal |

---

## CSS 코드 예시

### 카드 입체감

```css
/* Light Theme 카드 */
.card {
    background: linear-gradient(180deg, #ffffff 0%, #fafafa 100%);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 12px;
    box-shadow:
        0 4px 12px rgba(0,0,0,0.08),
        0 2px 4px rgba(0,0,0,0.04);
}

/* Dark Theme 카드 */
.dark-theme .card {
    background: linear-gradient(180deg, #1a1a1a 0%, #141414 100%);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow:
        0 4px 12px rgba(0,0,0,0.3),
        0 2px 4px rgba(0,0,0,0.2);
}
```

### 정적 마감 노트

```css
.closing-note {
    display: block;
    border-top: 1px solid rgba(0,0,0,0.14);
    padding-top: 18px;
    font-weight: 700;
    color: var(--color-primary);
}
```

### 섹션 배경 입체감

```css
/* 움푹 들어간 섹션 */
.inset-section {
    background: linear-gradient(180deg, #f0f0f0 0%, #f8f8f8 100%);
    box-shadow: inset 0 2px 8px rgba(0,0,0,0.06);
}

/* 떠있는 콘텐츠 박스 */
.elevated-box {
    background: #ffffff;
    border-radius: 16px;
    box-shadow:
        0 8px 32px rgba(0,0,0,0.1),
        0 4px 12px rgba(0,0,0,0.05);
}
```

---

## 테마별 입체감 조정

### 비교표

| 테마 | Shadow 강도 | Border 색상 | Gradient 방향 |
|------|-------------|-------------|---------------|
| **Clean Minimal** | 약함 (0.06~0.1) | rgba(0,0,0,0.08) | 180deg (위→아래) |
| **Dark Luxury** | 강함 (0.2~0.3) | rgba(255,255,255,0.08) | 135deg (대각선) |
| **Warm Natural** | 중간 (0.08~0.12) | rgba(139,115,85,0.15) | 180deg |

### Clean Minimal (약한 입체감)

밝은 테마에서는 그림자를 약하게 적용하여 **미니멀한 느낌**을 유지합니다.

```css
/* Clean Minimal - 카드 */
.clean-minimal .card {
    background: linear-gradient(180deg, #ffffff 0%, #fafafa 100%);
    border: 1px solid rgba(0,0,0,0.08);
    box-shadow:
        0 2px 8px rgba(0,0,0,0.06),
        0 1px 2px rgba(0,0,0,0.04);
}

/* Clean Minimal - 정적 마감 노트 */
.clean-minimal .closing-note {
    color: #2a2a2a;
    border-top: 1px solid rgba(0,0,0,0.14);
    box-shadow: none;
}

/* Clean Minimal - 섹션 구분 */
.clean-minimal .section-divider {
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-bottom: 1px solid rgba(0,0,0,0.06);
}
```

### Dark Luxury (강한 입체감)

어두운 배경에서는 그림자를 **강하게** 적용하고, **대각선 그라데이션**으로 고급스러움을 연출합니다.

```css
/* Dark Luxury - 카드 */
.dark-luxury .card {
    background: linear-gradient(135deg, #1a1a1a 0%, #141414 100%);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow:
        0 8px 24px rgba(0,0,0,0.3),
        0 4px 8px rgba(0,0,0,0.2);
}

/* Dark Luxury - 골드 액센트 마감 노트 */
.dark-luxury .closing-note {
    color: #c9a962;
    border-top: 1px solid rgba(201,169,98,0.35);
    box-shadow: none;
}

/* Dark Luxury - 마감 인상 박스 */
.dark-luxury .closing-box {
    background: linear-gradient(135deg, #1e1e1e 0%, #0a0a0a 100%);
    border: 1px solid rgba(201,169,98,0.3);
    box-shadow:
        0 12px 36px rgba(0,0,0,0.4),
        0 6px 12px rgba(0,0,0,0.25),
        inset 0 1px 0 rgba(255,255,255,0.05);
}
```

### Warm Natural (중간 입체감)

따뜻한 톤의 테마에서는 **부드러운 그림자**와 **브라운 계열 테두리**를 사용합니다.

```css
/* Warm Natural - 카드 */
.warm-natural .card {
    background: linear-gradient(180deg, #faf7f2 0%, #f5efe6 100%);
    border: 1px solid rgba(139,115,85,0.15);
    box-shadow:
        0 4px 16px rgba(139,115,85,0.1),
        0 2px 6px rgba(139,115,85,0.06);
}

/* Warm Natural - 정적 마감 노트 */
.warm-natural .closing-note {
    color: #8b7355;
    border-top: 1px solid rgba(139,115,85,0.22);
    box-shadow: none;
}

/* Warm Natural - 섹션 구분 */
.warm-natural .section-divider {
    box-shadow: 0 2px 8px rgba(139,115,85,0.08);
    border-bottom: 1px solid rgba(139,115,85,0.12);
}
```

---

## 입체감 적용 체크리스트

**카드:**
- [ ] `box-shadow` 적용됨 (최소 `--shadow-sm`)
- [ ] `border` 적용됨 (1px solid)
- [ ] `background` 그라데이션 적용됨

**버튼 금지:**
- [ ] `<button>`, `.cta-button`, 링크 버튼, 버튼형 rounded rectangle 사용 안 함
- [ ] 마지막 클로징은 정적 마감 문구/구분선/제품 이미지로 처리되며 옵션/혜택/주문 cue를 포함하지 않음

**마감 인상 영역:**
- [ ] `--shadow-lg` 이상 적용됨
- [ ] 배경 그라데이션 적용됨
- [ ] 구매/옵션/혜택 확인 문구 없이 상품/결과 인상으로 닫힘

**섹션:**
- [ ] 섹션 구분에 subtle shadow 사용됨
- [ ] 반전 섹션에서 shadow 색상 조정됨

**테마 적용:**
- [ ] Clean Minimal: 약한 그림자 (0.06~0.1)
- [ ] Dark Luxury: 강한 그림자 (0.2~0.3)
- [ ] Warm Natural: 중간 그림자 (0.08~0.12)
