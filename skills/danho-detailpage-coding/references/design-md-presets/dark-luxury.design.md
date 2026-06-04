---
version: alpha
name: Dark Luxury
description: 주얼리/시계/프리미엄 액세서리용 - 다크 배경 + 골드 액센트 럭셔리

colors:
  primary: "#c9a962"
  secondary: "#d4b574"
  tertiary: "#e8d5a8"
  surface: "#2a2a2a"
  bg: "#0a0a0a"
  bg-var-1: "#141414"
  bg-var-2: "#1e1e1e"
  bg-var-3: "#2a2a2a"
  bg-inverted: "#faf7f2"
  text: "#ffffff"
  text-secondary: "#e8e4de"
  text-muted: "#9a9590"
  text-dim: "#6a6560"
  text-inverted: "#1a1a1a"
  text-inverted-secondary: "#4a4a4a"
  border: "rgba(255, 255, 255, 0.1)"
  border-accent: "rgba(201, 169, 98, 0.3)"
  earth-brown: "#3d2b1f"

typography:
  display:
    fontFamily: Paperlogy
    fontSize: 6.25rem
    fontWeight: 800
    lineHeight: 1.1
  h1:
    fontFamily: Paperlogy
    fontSize: 4.25rem
    fontWeight: 800
    lineHeight: 1.2
  h2:
    fontFamily: Paperlogy
    fontSize: 3.25rem
    fontWeight: 700
    lineHeight: 1.3
  h3:
    fontFamily: Paperlogy
    fontSize: 2.625rem
    fontWeight: 700
  body-lg:
    fontFamily: Paperlogy
    fontSize: 2.25rem
    fontWeight: 500
  body-md:
    fontFamily: Paperlogy
    fontSize: 2rem
    fontWeight: 500
    lineHeight: 1.6
  body-sm:
    fontFamily: Paperlogy
    fontSize: 1.75rem
    fontWeight: 500
  caption:
    fontFamily: Paperlogy
    fontSize: 1.5rem
    fontWeight: 500

rounded:
  sm: 6px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 999px

spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  2xl: 96px
  section: 120px

elevation:
  sm: "0 2px 6px rgba(0,0,0,0.2), 0 1px 3px rgba(0,0,0,0.15)"
  md: "0 6px 16px rgba(0,0,0,0.25), 0 3px 6px rgba(0,0,0,0.2)"
  lg: "0 12px 32px rgba(0,0,0,0.35), 0 6px 12px rgba(0,0,0,0.25)"
  accent: "0 4px 16px rgba(201, 169, 98, 0.3)"

mood:
  keywords: ["premium luxury", "dark elegant", "gold accent", "sophisticated"]
  negative: ["no watermarks", "no cheap infographic style", "no bright cheerful colors", "no flat illustration"]

components:
  hero-headline:
    typography: "{typography.display}"
    textColor: "{colors.primary}"
  section-title:
    typography: "{typography.h2}"
    textColor: "{colors.text}"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 32px
    elevation: "{elevation.md}"
    border: "1px solid {colors.border}"
  checklist-item:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px
    border: "1px solid {colors.border}"
    elevation: "{elevation.sm}"
  cta-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.bg}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.lg}"
    padding: "28px 80px"
    elevation: "{elevation.lg}"
  stat-value:
    typography: "{typography.h1}"
    textColor: "{colors.primary}"
  badge:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    border: "1px solid {colors.border-accent}"
    elevation: "{elevation.sm}"
---

## Overview
딥블랙 + 골드의 클래식 럭셔리 조합. 모든 시각적 노이즈를 제거하고 제품 자체의 광택과 디테일이 부각되도록 한다. 어두운 배경은 골드 액센트를 한층 빛나게 한다.

## Colors
배경은 거의 검정(#0a0a0a) 단계적으로 미세하게 밝아짐. 골드(#c9a962)가 유일한 강조색. 텍스트는 백색 위계 4단계로 정보 깊이 표현.

## Typography
Paperlogy 사용. 본문 32px는 다른 테마와 동일하지만, 헤드라인에 골드 그라데이션/네온 효과를 강하게 적용해 임팩트 극대화.

## Layout
860px 컨테이너. 다크 테마 특성상 섹션 간 배경 변화는 명도 미세 조정(`bg` → `bg-var-1` → `bg-var-2`). 중간에 `bg-inverted`(라이트) 섹션으로 시선 전환.

## Elevation & Depth
다른 테마 대비 그림자를 진하게(opacity 0.2~0.35). 골드 액센트 요소는 `elevation.accent`로 골드 글로우.

## Shapes
라운드 12~16px 기본. 카드는 절제된 모서리. CTA도 사각형 라운드.

## Components
- `cta-button`: 골드 배경, 블랙 텍스트
- `badge`: 골드 보더, 골드 텍스트
- `section-title`: 골드 그라데이션 + 네온 글로우 효과 적용 권장
- 배경 변화: `bg` → `bg-var-1` → `bg-var-2` → `bg-inverted`(중간 한 번)

## Do's and Don'ts
✅ 헤드라인에 골드 그라데이션 + glow
✅ 카드는 surface(#2a2a2a) + subtle 보더
✅ 배경 변화는 명도만 (색조 변화 X)
❌ NO 그라데이션 + 네온 동시 적용 (둘 중 하나만)
❌ NO 밝은 색상 (골드 외엔 액센트 컬러 사용 금지)
❌ NO 텍스트 체크박스 기호

## Notes
주얼리, 시계, 향수, 프리미엄 가전, 명상/스피리추얼 제품에 적합. 식품·캐주얼 패션엔 부적합.
