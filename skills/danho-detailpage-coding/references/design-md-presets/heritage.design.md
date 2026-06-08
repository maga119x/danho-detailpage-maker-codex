---
version: alpha
name: Heritage
description: 전통/한복/공예품 - 한지 베이지 + 진사 빨강 헤리티지

colors:
  primary: "#8b0000"
  secondary: "#b22222"
  tertiary: "#cd5c5c"
  surface: "#faf8f5"
  bg: "#f8f4ef"
  bg-var-1: "#efe8de"
  bg-var-2: "#e5dace"
  bg-var-3: "#d8cbb8"
  bg-inverted: "#2c1810"
  text: "#2c1810"
  text-secondary: "#4a3228"
  text-muted: "#7a6458"
  text-dim: "#a89888"
  text-inverted: "#f8f4ef"
  text-inverted-secondary: "#d8cbb8"
  border: "rgba(44, 24, 16, 0.1)"
  border-accent: "rgba(139, 0, 0, 0.3)"
  navy-blue: "#1a2a4a"

typography:
  display:
    fontFamily: Paperlogy
    fontSize: clamp(2.5rem, 10vw, 4rem)
    fontWeight: 800
    lineHeight: 1.1
  h1:
    fontFamily: Paperlogy
    fontSize: clamp(2.25rem, 9vw, 3.4rem)
    fontWeight: 800
    lineHeight: 1.2
  h2:
    fontFamily: Paperlogy
    fontSize: clamp(1.75rem, 7vw, 2.75rem)
    fontWeight: 700
    lineHeight: 1.3
  h3:
    fontFamily: Paperlogy
    fontSize: clamp(1.25rem, 5vw, 1.875rem)
    fontWeight: 700
  body-lg:
    fontFamily: Paperlogy
    fontSize: clamp(1.0625rem, 4vw, 1.375rem)
    fontWeight: 500
  body-md:
    fontFamily: Paperlogy
    fontSize: clamp(1rem, 3.7vw, 1.125rem)
    fontWeight: 500
    lineHeight: 1.6
  body-sm:
    fontFamily: Paperlogy
    fontSize: clamp(.875rem, 3.2vw, 1rem)
    fontWeight: 500
  caption:
    fontFamily: Paperlogy
    fontSize: .8125rem
    fontWeight: 500

rounded:
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 999px

spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  2xl: 96px
  section: clamp(56px, 14vw, 112px)

elevation:
  sm: "0 2px 4px rgba(44, 24, 16, 0.08), 0 1px 2px rgba(44, 24, 16, 0.04)"
  md: "0 4px 12px rgba(44, 24, 16, 0.1), 0 2px 4px rgba(44, 24, 16, 0.06)"
  lg: "0 8px 24px rgba(44, 24, 16, 0.14), 0 4px 8px rgba(44, 24, 16, 0.08)"
  accent: "0 4px 12px rgba(139, 0, 0, 0.2)"

mood:
  keywords: ["korean heritage", "traditional craft", "hanji paper", "deep red accent"]
  negative: ["no watermarks", "no modern minimalism", "no neon", "no western aesthetic"]

components:
  hero-headline:
    typography: "{typography.display}"
    textColor: "{colors.primary}"
  section-title:
    typography: "{typography.h2}"
    textColor: "{colors.text}"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 32px
    elevation: "{elevation.md}"
    border: "1px solid {colors.border}"
  checklist-item:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 24px
    border: "1px solid {colors.border}"
    elevation: "{elevation.sm}"
  cta-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.bg}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.md}"
    padding: "28px 80px"
    elevation: "{elevation.lg}"
  stat-value:
    typography: "{typography.h1}"
    textColor: "{colors.primary}"
  badge:
    backgroundColor: "{colors.bg-var-1}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    border: "1px solid {colors.border-accent}"
    elevation: "{elevation.sm}"
---

## Overview
한지의 질감과 진사(辰沙)의 깊은 빨강. 전통 공예의 장인 정신을 시각화. 절제되고 묵직한 위엄을 추구한다.

## Colors
배경은 #f8f4ef 한지빛. 단계적으로 짙어지는 베이지. 메인 액센트는 깊은 빨강(#8b0000) — 단청에서 영감. 네이비 블루(#1a2a4a)를 두번째 강조로.

## Typography
Paperlogy. 본문 32px. 헤드라인은 강한 굵기에 미세한 shadow (네온 X).

## Layout
860px. 배경 변화는 베이지 명도 변화 위주.

## Elevation & Depth
중간 강도 그림자. 카드는 모두 elevation.md. 한지 질감의 묵직함.

## Shapes
라운드 4~12px (다른 테마 대비 작게). 전통적 직선미 강조. CTA도 사각형 가까운 라운드.

## Components
- `cta-button`: 진사 빨강 배경, 한지 베이지 텍스트
- `badge`: 옅은 베이지 배경 + 빨강 보더/텍스트
- 배경 변화: `bg` → `bg-var-1` → `bg-var-2` 한지 명도 순환

## Do's and Don'ts
✅ 헤드라인 빨강 단색 + title-shadow
✅ 직선미 (라운드는 작게)
✅ 한자 또는 한글 헤리티지 폰트 추가 권장
❌ NO 네온/형광 효과
❌ NO 강한 그라데이션
❌ NO 모던 미니멀 (장식 적당히 살리기)
❌ NO 텍스트 체크박스 기호

## Notes
한복, 도자기, 다도, 전통주, 공예품, 한방 제품에 적합. 모던 테크 제품엔 부적합.

