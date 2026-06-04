# Title Text Effects (타이틀 텍스트 효과)

h1, h2 메인 타이틀에 적용하는 필수 텍스트 효과 가이드입니다.

---

## 1. Title Text Effects (REQUIRED)

**h1, h2 급 메인 타이틀에는 테마별 텍스트 효과를 반드시 적용해야 합니다.**
효과 미적용 시 Output Checklist에서 실패 처리됩니다.

---

## 2. Gradient vs Neon 상호 배타 규칙 (CRITICAL)

**그라데이션 타이틀에 네온 효과를 함께 적용하면 가독성이 저하됩니다.**

| 타이틀 유형 | 허용 효과 | 금지 효과 |
|-------------|-----------|-----------|
| **그라데이션 타이틀** | 쉐도우 (text-shadow) | 네온 글로우 |
| **단색 타이틀** | 네온 글로우, 쉐도우 | - |

```css
/* 올바른 조합 */
.title-gradient { /* 그라데이션 */ }
.title-gradient.title-shadow { /* 그라데이션 + 쉐도우 OK */ }

/* 금지 조합 - 가독성 저하 */
.title-gradient.title-neon { /* 그라데이션 + 네온 금지! */ }
.title-neon-gradient { /* 이 클래스 사용 금지! */ }

/* 단색 타이틀에만 네온 허용 */
.title-solid.title-neon { /* 단색 + 네온 OK */ }
```

---

## 3. Tonal Gradient (제한적 그라데이션)

**색조(Hue)는 유지하면서 채도/명도만 변화시키는 그라데이션.**
같은 색상 영역 내에서 미묘한 변화를 주어 고급스러운 느낌을 연출합니다.

### Clean Minimal - 다크 그레이 그라데이션

```css
.title-gradient {
    background: linear-gradient(135deg, #1a1a1a 0%, #3d3d3d 50%, #1a1a1a 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

### Dark Luxury - 골드 그라데이션

```css
.title-gradient {
    background: linear-gradient(135deg, #c9a962 0%, #e8d5a3 30%, #c9a962 60%, #a68b4b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

### Warm Natural - 브라운 그라데이션

```css
.title-gradient {
    background: linear-gradient(135deg, #8b7355 0%, #a69076 50%, #8b7355 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

---

## 4. Text Shadow (텍스트 쉐도우)

**입체감과 깊이를 더하는 그림자 효과.**

### Clean Minimal - 미니멀 쉐도우

```css
.title-shadow {
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 4px 8px rgba(0, 0, 0, 0.05);
}
```

### Dark Luxury - 골드 글로우 쉐도우

```css
.title-shadow {
    text-shadow: 0 2px 4px rgba(201, 169, 98, 0.3), 0 4px 12px rgba(201, 169, 98, 0.2);
}
```

### Warm Natural - 소프트 쉐도우

```css
.title-shadow {
    text-shadow: 0 2px 6px rgba(139, 115, 85, 0.2), 0 4px 10px rgba(139, 115, 85, 0.1);
}
```

---

## 5. Glow/Neon Effects (글로우/네온 효과)

**네온 효과는 단색 타이틀에만 적용. 그라데이션 타이틀에는 쉐도우만 사용.**

### Clean Minimal - 서브틀 글로우

```css
.title-glow {
    text-shadow: 0 0 10px rgba(26, 26, 26, 0.2), 0 0 20px rgba(26, 26, 26, 0.1);
}
```

### Dark Luxury - 네온 글로우 (단색 타이틀 전용!)

```css
.title-neon {
    color: #c9a962;  /* 단색 골드 */
    text-shadow:
        0 0 5px rgba(201, 169, 98, 0.8),
        0 0 10px rgba(201, 169, 98, 0.6),
        0 0 20px rgba(201, 169, 98, 0.4),
        0 0 40px rgba(201, 169, 98, 0.2);
}
```

### Dark Luxury - 골드 글로우 (h2, h3용)

```css
.title-glow {
    text-shadow:
        0 0 5px rgba(201, 169, 98, 0.5),
        0 0 15px rgba(201, 169, 98, 0.3),
        0 0 30px rgba(201, 169, 98, 0.2);
}
```

### Dark Luxury - 강렬한 네온 (단색 히어로 타이틀 전용)

```css
.title-neon-intense {
    color: #c9a962;  /* 단색 골드 필수 */
    text-shadow:
        0 0 5px rgba(201, 169, 98, 1),
        0 0 10px rgba(201, 169, 98, 0.8),
        0 0 20px rgba(201, 169, 98, 0.6),
        0 0 40px rgba(201, 169, 98, 0.4),
        0 0 80px rgba(201, 169, 98, 0.2);
}
```

### Dark Luxury - 그라데이션 타이틀용 쉐도우

그라데이션 타이틀에는 네온 대신 쉐도우로 입체감 부여:

```css
.title-gradient-shadow {
    background: linear-gradient(135deg, #c9a962 0%, #e8d5a3 30%, #c9a962 60%, #a68b4b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));  /* 쉐도우만! 글로우 아님 */
}
```

### Warm Natural - 웜 글로우

```css
.title-glow {
    text-shadow: 0 0 12px rgba(139, 115, 85, 0.3), 0 0 24px rgba(139, 115, 85, 0.15);
}
```

---

## 6. 테마별 필수 클래스 매핑

| 테마 | h1 클래스 | h2 클래스 | h3 클래스 |
|------|-----------|-----------|-----------|
| Clean Minimal | `title-gradient title-shadow` | `title-shadow` | - |
| Dark Luxury (그라데이션) | `title-gradient-shadow` | `title-glow` | `title-glow` (선택) |
| Dark Luxury (단색+네온) | `title-neon` 또는 `title-neon-intense` | `title-glow` | `title-glow` (선택) |
| Warm Natural | `title-gradient title-shadow` | `title-shadow` | - |

### 테마별 헤딩 효과 요약

| 테마 | h1 (히어로) | h2 (섹션 타이틀) | h3 (서브 타이틀) |
|------|-------------|------------------|------------------|
| Clean Minimal | 그라데이션 + 쉐도우 | 미니멀 쉐도우 | - |
| Dark Luxury | 골드 그라데이션 + 쉐도우 **또는** 단색 골드 + 네온 | 골드 쉐도우 | 서브틀 글로우 |
| Warm Natural | 브라운 그라데이션 + 소프트 쉐도우 | 소프트 쉐도우 | - |

---

## 7. 조합 예시 (HTML)

### Clean Minimal: 그라데이션 + 쉐도우 조합

```html
<h1 class="title-gradient title-shadow">프리미엄 품질의 차이</h1>
<h2 class="title-shadow">주요 특징</h2>
```

### Dark Luxury 옵션 A: 그라데이션 + 쉐도우 (네온 없음!)

```html
<h1 class="title-gradient-shadow">럭셔리한 경험</h1>
<h2 class="title-glow">프리미엄 디테일</h2>
```

### Dark Luxury 옵션 B: 단색 + 네온 (그라데이션 없음!)

```html
<h1 class="title-neon">럭셔리한 경험</h1>
<h2 class="title-glow">프리미엄 디테일</h2>
```

### Warm Natural: 브라운 그라데이션 + 소프트 쉐도우

```html
<h1 class="title-gradient title-shadow">자연의 따스함</h1>
<h2 class="title-shadow">특별한 재료</h2>
```

### 금지된 조합

```html
<!-- 금지: 그라데이션 + 네온 동시 적용 -->
<!-- <h1 class="title-gradient title-neon">가독성 저하!</h1> -->
```

---

## 필수 적용 규칙 요약

1. **h1, h2에 효과 미적용 시 Output Checklist 실패**
2. **본문 텍스트(p, li)에는 효과 적용 금지**
3. **그라데이션 + 네온 동시 적용 금지** (가독성 저하)
4. 그라데이션 타이틀 → 쉐도우만 허용
5. 단색 타이틀 → 네온 효과 허용

---

## Output Checklist (타이틀 효과)

- [ ] h1, h2 타이틀에 테마별 효과 **필수** 적용됨
- [ ] Clean Minimal: h1에 `title-gradient title-shadow`, h2에 `title-shadow`
- [ ] Dark Luxury (그라데이션): h1에 `title-gradient-shadow`, h2에 `title-glow`
- [ ] Dark Luxury (단색+네온): h1에 `title-neon`, h2에 `title-glow`
- [ ] Warm Natural: h1에 `title-gradient title-shadow`, h2에 `title-shadow`
- [ ] **그라데이션 + 네온 동시 적용 금지** (가독성 저하)
- [ ] 본문 텍스트(p, li)에는 효과 미적용
