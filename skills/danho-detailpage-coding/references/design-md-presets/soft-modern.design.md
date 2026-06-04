---
version: alpha
name: Soft Modern
description: 패션/라이프스타일/코스메틱 - 부드러운 뉴트럴+블러시 핑크

colors:
  primary: "#b8977e"
  secondary: "#d4b8a0"
  tertiary: "#e8d4c4"
  surface: "#ffffff"
  bg: "#fafafa"
  bg-var-1: "#f5f5f5"
  bg-var-2: "#eeeeee"
  bg-var-3: "#f0e4e0"
  bg-inverted: "#2d2d2d"
  text: "#2d2d2d"
  text-secondary: "#4f4f4f"
  text-muted: "#7a7a7a"
  text-dim: "#a0a0a0"
  text-inverted: "#ffffff"
  text-inverted-secondary: "#d4d4d4"
  border: "rgba(0, 0, 0, 0.08)"
  border-accent: "rgba(184, 151, 126, 0.3)"
  blush-pink: "#f0e4e0"

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
  sm: 8px
  md: 16px
  lg: 20px
  xl: 28px
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
  sm: "0 2px 4px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)"
  md: "0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04)"
  lg: "0 8px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06)"
  accent: "0 4px 12px rgba(184, 151, 126, 0.2)"

mood:
  keywords: ["soft modern", "feminine elegant", "blush warm", "lifestyle aesthetic"]
  negative: ["no watermarks", "no harsh contrast", "no neon colors", "no aggressive typography"]

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
  cta-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.bg}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.xl}"
    padding: "28px 80px"
    elevation: "{elevation.lg}"
  stat-value:
    typography: "{typography.h1}"
    textColor: "{colors.primary}"
  badge:
    backgroundColor: "{colors.blush-pink}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    border: "1px solid {colors.border-accent}"
    elevation: "{elevation.sm}"
---

## Overview
뉴트럴 그레이 베이스에 블러시 핑크 액센트. 여성 라이프스타일 제품에 적합한 부드럽고 세련된 톤.

## Colors
배경은 #fafafa 거의 화이트. 액센트 #b8977e는 베이지 핑크. 블러시 핑크(#f0e4e0)를 배경 변화에 사용해 따뜻함 추가.

## Typography
Paperlogy. 본문 32px. 헤드라인 굵기는 다른 테마와 동일하지만 톤이 부드러움.

## Layout
860px. 배경 변화 (`bg` → `bg-var-1` → `bg-var-3`(블러시 핑크)) 순환.

## Elevation & Depth
은은한 그림자. clean-minimal과 유사한 강도.

## Shapes
라운드 16~20px (clean-minimal보다 더 둥글게). CTA는 xl(28px)로 더 둥근 느낌.

## Components
- `cta-button`: 베이지 핑크 배경, 화이트 텍스트, 둥근 모서리(rounded.xl)
- `badge`: 블러시 핑크 배경
- 배경 변화: `bg` → `bg-var-1` → `bg-var-3`(블러시) 순환

## Do's and Don'ts
✅ 라운드 더 둥글게 (16~20px)
✅ 블러시 핑크 적극 활용
✅ 부드러운 그림자
❌ NO 강한 대비
❌ NO 검정 액센트
❌ NO 텍스트 체크박스 기호

## Notes
여성 패션, 코스메틱, 라이프스타일, 인테리어 소품에 적합.
