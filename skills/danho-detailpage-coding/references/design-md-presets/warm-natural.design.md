---
version: alpha
name: Warm Natural
description: 유기농/웰니스/스킨케어/티 - 따뜻한 베이지+브라운 자연주의

colors:
  primary: "#8b7355"
  secondary: "#a68b6a"
  tertiary: "#c4a882"
  surface: "#ffffff"
  bg: "#faf7f2"
  bg-var-1: "#f5efe6"
  bg-var-2: "#ebe3d6"
  bg-var-3: "#e0d5c4"
  bg-inverted: "#3d3028"
  text: "#3d3028"
  text-secondary: "#5c4d3d"
  text-muted: "#8a7a68"
  text-dim: "#b5a594"
  text-inverted: "#faf7f2"
  text-inverted-secondary: "#e8e4de"
  border: "rgba(139, 115, 85, 0.15)"
  border-accent: "rgba(139, 115, 85, 0.3)"
  forest-green: "#4a5d4a"

typography:
  display:
    fontFamily: Paperlogy
    fontSize: clamp(5rem, 10vw, 8rem)
    fontWeight: 800
    lineHeight: 1.1
  h1:
    fontFamily: Paperlogy
    fontSize: clamp(4.5rem, 9vw, 6.75rem)
    fontWeight: 800
    lineHeight: 1.2
  h2:
    fontFamily: Paperlogy
    fontSize: clamp(3.5rem, 7vw, 5.5rem)
    fontWeight: 700
    lineHeight: 1.3
  h3:
    fontFamily: Paperlogy
    fontSize: clamp(2.5rem, 5vw, 3.75rem)
    fontWeight: 700
  body-lg:
    fontFamily: Paperlogy
    fontSize: clamp(2.25rem, 4vw, 2.75rem)
    fontWeight: 500
  body-md:
    fontFamily: Paperlogy
    fontSize: clamp(2rem, 3.7vw, 2.25rem)
    fontWeight: 500
    lineHeight: 1.6
  body-sm:
    fontFamily: Paperlogy
    fontSize: clamp(1.875rem, 3.4vw, 2.125rem)
    fontWeight: 500
  caption:
    fontFamily: Paperlogy
    fontSize: clamp(1.875rem, 3.2vw, 2rem)
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
  section: clamp(96px, 14vw, 140px)

elevation:
  sm: "0 2px 4px rgba(61, 48, 40, 0.08), 0 1px 2px rgba(61, 48, 40, 0.04)"
  md: "0 4px 12px rgba(61, 48, 40, 0.1), 0 2px 4px rgba(61, 48, 40, 0.06)"
  lg: "0 8px 24px rgba(61, 48, 40, 0.14), 0 4px 8px rgba(61, 48, 40, 0.08)"
  accent: "0 4px 12px rgba(139, 115, 85, 0.2)"

mood:
  keywords: ["warm natural", "organic earthy", "calm healing", "authentic craft"]
  negative: ["no watermarks", "no cheap infographic style", "no neon colors", "no high contrast"]

components:
  hero-headline:
    typography: "{typography.display}"
    textColor: "{colors.text}"
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
  closing-note:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.bg}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 0"
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
크림빛 베이지 + 따뜻한 브라운의 자연주의. 햇빛에 바랜 한지 같은 차분함. 손으로 만든 듯한 진정성을 시각화한다.

## Colors
배경은 #faf7f2 크림. 단계적으로 살짝씩 어두워지는 베이지 톤. 액센트는 #8b7355 흙갈색. 텍스트는 짙은 브라운으로 따뜻하게.

## Typography
Paperlogy. 본문 32px 동일. 헤드라인은 그라데이션 + 부드러운 shadow.

## Layout
860px. 배경 변화 풍부 (`bg` → `bg-var-1` → `bg-var-2` → `bg-inverted` 중간 한 번).

## Elevation & Depth
부드러운 그림자 (brown 톤 rgba). 카드는 모두 elevation.md 적용. 너무 진하지 않게.

## Shapes
라운드 12~16px. 자연주의 무드라 다소 둥근 느낌 강조.

## Components
- `closing-note`: 구매 행동 문구가 아닌 상품/결과 마감 문구. 흙갈색 포인트 텍스트 또는 얇은 구분선과 함께 사용
- `badge`: 옅은 베이지 배경 + 갈색 텍스트
- 배경 변화: `bg` → `bg-var-1` → `bg-var-2` → 중간에 `bg-inverted`(다크) 한 번

## Do's and Don'ts
✅ 헤드라인에 title-gradient + title-shadow
✅ 카드는 화이트 surface + 베이지 보더
✅ 자연 소재 이미지와 잘 어울리는 톤 유지
❌ NO 채도 높은 컬러
❌ NO 검정·진회색 (브라운 톤 유지)
❌ NO 텍스트 체크박스 기호

## Notes
유기농/웰니스/스킨케어/티/허브/홈가드닝 제품에 적합. 테크 제품엔 부적합.
