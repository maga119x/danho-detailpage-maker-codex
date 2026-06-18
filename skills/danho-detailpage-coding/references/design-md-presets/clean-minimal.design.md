---
version: alpha
name: Clean Minimal
description: 테크/전자제품용 - 모던하고 신뢰감 있는 미니멀 디자인

colors:
  primary: "#000000"
  secondary: "#333333"
  tertiary: "#666666"
  surface: "#ffffff"
  bg: "#ffffff"
  bg-var-1: "#f8f9fa"
  bg-var-2: "#f1f3f4"
  bg-var-3: "#e9ecef"
  bg-inverted: "#1a1a1a"
  text: "#1a1a1a"
  text-secondary: "#4a4a4a"
  text-muted: "#767676"
  text-dim: "#9a9a9a"
  text-inverted: "#ffffff"
  text-inverted-secondary: "#e0e0e0"
  border: "#e5e5e5"
  border-accent: "rgba(0, 0, 0, 0.1)"

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
  section: clamp(56px, 14vw, 112px)

elevation:
  sm: "0 2px 4px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)"
  md: "0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04)"
  lg: "0 8px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06)"
  accent: "0 4px 12px rgba(0,0,0,0.1)"

mood:
  keywords: ["clean minimalist", "modern tech", "trustworthy", "premium quality"]
  negative: ["no watermarks", "no cheap infographic style", "no generic stock imagery", "no cluttered elements"]

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
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    border: "1px solid {colors.border}"
    elevation: "{elevation.sm}"
---

## Overview
모던 테크 제품을 위한 화이트 기반 미니멀 디자인. 신뢰감과 깔끔함을 무기로 한다. 컬러 사용을 최소화하고, 타이포그래피와 여백으로 구조를 만든다.

## Colors
순백색 배경에 검정 액센트. 회색 톤 4단계(`text` → `text-secondary` → `text-muted` → `text-dim`)로 위계를 표현. 컬러 강조 없이 텍스트 크기/굵기로 강약 조절.

## Typography
Paperlogy 패밀리 단일 사용. 본문 32px(`body-md`)을 기준으로, 섹션 제목은 52px(`h2`), 메인 헤드라인은 68~100px. 굵기는 500(본문)/700(소제목)/800(헤드라인) 세 단계.

## Layout
860px 최대 폭 컨테이너. 콘텐츠 섹션은 `padding: 120px 10%` 만 사용 (margin/width 금지). 이미지는 별도 `.full-image` 섹션으로 100% 폭.

## Elevation & Depth
은은한 그림자. 모든 카드는 `elevation.md` 이상. `closing-note`는 과하게 떠 보이지 않도록 얇은 구분선과 포인트 텍스트 중심.

## Shapes
라운드 12~16px 기본. CTA도 모서리 둥근 사각형 (pill 사용 안 함). 카드/배지는 단정한 모서리.

## Components
- `closing-note`: 구매 행동 문구가 아닌 상품/결과 마감 문구. 검정 포인트 텍스트 또는 얇은 구분선과 함께 사용
- `checklist-item`: 화이트 카드 + 보더 + 미세 그림자
- `card`: 화이트 + 보더 + `elevation.md`
- 배경 변화: `bg` → `bg-var-1` → `bg-var-2` 순환

## Do's and Don'ts
✅ 본문 32px, 섹션 제목 52px
✅ 모든 카드는 보더 + 그림자
✅ 텍스트는 좌측 정렬이 기본, 헤드라인만 가운데
❌ NO :hover, transition, animation
❌ NO 강한 컬러 (검정·흰색·회색만)
❌ NO 텍스트 체크박스 기호 → check-box 클래스로

## Notes
테크/전자제품/모던 가구 등 "기능과 신뢰"가 핵심인 제품에 적합. 식품·뷰티 같은 감성 제품엔 부적합.

