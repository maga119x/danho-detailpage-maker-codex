---
version: alpha
name: Fresh Vibrant
description: 식품/음료/건강기능식품 - 신선 그린+활기찬 액센트

colors:
  primary: "#2e8b57"
  secondary: "#3cb371"
  tertiary: "#90ee90"
  surface: "#ffffff"
  bg: "#ffffff"
  bg-var-1: "#f0f9f0"
  bg-var-2: "#e8f5e8"
  bg-var-3: "#d4ecd4"
  bg-inverted: "#1a3a1a"
  text: "#1a3a1a"
  text-secondary: "#2d5a2d"
  text-muted: "#5a8a5a"
  text-dim: "#8ab88a"
  text-inverted: "#ffffff"
  text-inverted-secondary: "#d4ecd4"
  border: "rgba(46, 139, 87, 0.1)"
  border-accent: "rgba(46, 139, 87, 0.3)"
  citrus-orange: "#ff8c42"

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
    fontSize: clamp(1rem, 3.4vw, 1.0625rem)
    fontWeight: 500
  caption:
    fontFamily: Paperlogy
    fontSize: clamp(1rem, 3.2vw, 1rem)
    fontWeight: 500

rounded:
  sm: 8px
  md: 14px
  lg: 18px
  xl: 28px
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
  sm: "0 2px 4px rgba(26, 58, 26, 0.06), 0 1px 2px rgba(26, 58, 26, 0.04)"
  md: "0 4px 12px rgba(26, 58, 26, 0.08), 0 2px 4px rgba(26, 58, 26, 0.04)"
  lg: "0 8px 24px rgba(26, 58, 26, 0.12), 0 4px 8px rgba(26, 58, 26, 0.06)"
  accent: "0 4px 12px rgba(46, 139, 87, 0.2)"

mood:
  keywords: ["fresh vibrant", "natural healthy", "appetizing energetic", "clean green"]
  negative: ["no watermarks", "no artificial colors", "no dull palette", "no greasy textures"]

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
신선한 채소를 베어물 때의 산뜻함. 식품·건강기능식품의 "안전하고 활기찬" 인상을 그린 톤으로 표현.

## Colors
배경은 화이트, 단계적으로 옅은 그린(#f0f9f0 → #e8f5e8 → #d4ecd4). 메인 액센트는 #2e8b57 깊은 그린. 시트러스 오렌지(#ff8c42)를 강조 포인트로.

## Typography
Paperlogy. 본문 32px. 헤드라인에 그린 그라데이션.

## Layout
860px. 배경 변화 풍부 (화이트 ↔ 옅은 그린 교차).

## Elevation & Depth
부드러운 그린 톤 그림자. 강하지 않게.

## Shapes
라운드 14~18px. 마지막 마감은 버튼형 라운드가 아니라 `closing-note`와 식품 결과 장면으로 부드럽게 처리.

## Components
- `closing-note`: 구매 행동 문구가 아닌 상품/결과 마감 문구. 깊은 그린 포인트 텍스트 또는 얇은 구분선과 함께 사용
- `badge`: 옅은 그린 배경 + 진한 그린 텍스트
- 배경 변화: 화이트 ↔ `bg-var-1`(옅은 그린) ↔ `bg-var-2`(미디엄 그린)

## Do's and Don'ts
✅ 헤드라인 그린 그라데이션
✅ 신선함을 강조하는 옅은 그린 배경 적극 활용
✅ 시트러스 오렌지를 강조 포인트로 (한두 군데만)
❌ NO 어두운 톤 (식품인데 어두우면 식욕 감소)
❌ NO 인공적인 형광 컬러
❌ NO 텍스트 체크박스 기호

## Notes
신선식품, 건강기능식품, 음료, 비타민, 다이어트 제품에 적합.

