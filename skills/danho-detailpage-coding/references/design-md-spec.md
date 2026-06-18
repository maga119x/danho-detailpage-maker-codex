# DESIGN.md 디자인 시스템 스펙 (상세페이지용)

> Google Stitch가 오픈소스화한 [DESIGN.md alpha 스펙](https://github.com/google-labs-code/design.md)을 한국 이커머스 상세페이지 도메인에 맞춰 확장한 규격.

## 위치와 역할

- **파일명**: `DESIGN.md`
- **위치**: `projects/MMDDHHmm_<프로젝트명>/DESIGN.md` (프로젝트 루트)
- **역할**: 해당 프로젝트의 **단일 디자인 시스템 진실 소스(single source of truth)**.
  - planning 스킬 → 기획 시 DESIGN.md를 함께 생성/선택
  - imageprompt 스킬 → DESIGN.md의 컬러/타이포/무드를 프롬프트에 자동 주입
  - coding 스킬 (build.py) → DESIGN.md를 파싱해 CSS variables, BASE CSS, 컴포넌트 클래스 자동 생성

## 파일 구조

```
---
<YAML frontmatter — 머신리더블 토큰>
---

<마크다운 본문 — 9개 표준 섹션>
```

## YAML frontmatter 규격

```yaml
version: alpha
name: <브랜드/프로젝트 이름>
description: <한 줄 컨셉>

colors:                  # 시맨틱 컬러 토큰
  primary: "#hex"        # 메인 강조색 (CTA, 핵심 헤드라인)
  secondary: "#hex"      # 보조 강조색
  tertiary: "#hex"       # 액센트 (강조 텍스트, 작은 포인트)
  surface: "#hex"        # 카드/표면 배경
  bg: "#hex"             # 페이지 기본 배경
  bg-var-1: "#hex"       # 섹션 배경 변형 1
  bg-var-2: "#hex"       # 섹션 배경 변형 2
  bg-inverted: "#hex"    # 반전 섹션 배경
  text: "#hex"           # 기본 본문 색
  text-secondary: "#hex"
  text-muted: "#hex"
  text-inverted: "#hex"
  border: "#hex"         # 보더 (rgba 가능)
  border-accent: "#hex"

typography:              # 타이포그래피 토큰
  display:
    fontFamily: Paperlogy
    fontSize: clamp(2.5rem, 10vw, 4rem) # 40-64px
    fontWeight: 800
    lineHeight: 1.1
  h1:
    fontFamily: Paperlogy
    fontSize: clamp(2.25rem, 9vw, 3.4rem) # 36-54px
    fontWeight: 800
    lineHeight: 1.2
  h2:
    fontFamily: Paperlogy
    fontSize: clamp(1.75rem, 7vw, 2.75rem) # 28-44px
    fontWeight: 700
    lineHeight: 1.3
  h3:
    fontFamily: Paperlogy
    fontSize: clamp(1.25rem, 5vw, 1.875rem) # 20-30px
    fontWeight: 700
  body-lg:
    fontFamily: Paperlogy
    fontSize: clamp(1.0625rem, 4vw, 1.375rem) # 17-22px
    fontWeight: 500
  body-md:
    fontFamily: Paperlogy
    fontSize: clamp(1rem, 3.7vw, 1.125rem) # 16-18px body
    fontWeight: 500
    lineHeight: 1.6
  body-sm:
    fontFamily: Paperlogy
    fontSize: clamp(1rem, 3.4vw, 1.0625rem) # 16-17px
    fontWeight: 500
  caption:
    fontFamily: Paperlogy
    fontSize: clamp(1rem, 3.2vw, 1rem) # 16px
    fontWeight: 500
  micro:
    fontFamily: Paperlogy
    fontSize: clamp(.875rem, 3vw, .9375rem) # 14-15px, legal/spec footnotes only
    fontWeight: 500

rounded:                 # 라운드 토큰
  sm: 6px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 999px

spacing:                 # 간격 토큰 (8px 그리드)
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  2xl: 96px
  section: clamp(56px, 14vw, 112px) # mobile-readable section padding

elevation:               # 그림자 토큰
  sm: "0 2px 6px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.04)"
  md: "0 6px 16px rgba(0,0,0,0.1), 0 3px 6px rgba(0,0,0,0.06)"
  lg: "0 12px 32px rgba(0,0,0,0.14), 0 6px 12px rgba(0,0,0,0.08)"
  accent: "0 4px 16px rgba(0,0,0,0.2)"

mood:                    # 이미지 프롬프트 생성용 분위기 키워드
  keywords: ["premium minimalist", "clean modern", "trustworthy"]
  negative: ["no watermarks", "no cheap infographic", "no generic stock"]

components:              # 컴포넌트 토큰 (CSS 클래스로 자동 변환됨)
  hero-headline:
    typography: "{typography.display}"
    textColor: "{colors.primary}"
  section-title:
    typography: "{typography.h2}"
    textColor: "{colors.text}"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
    elevation: "{elevation.md}"
    border: "1px solid {colors.border}"
  checklist-item:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.border}"
  closing-note:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.bg}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} 0"
  stat-value:
    typography: "{typography.h1}"
    textColor: "{colors.primary}"
  badge:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
    border: "1px solid {colors.border}"
```

### 토큰 참조 규칙

- 다른 토큰 참조 시 중괄호 사용: `{colors.primary}`, `{typography.h1}`, `{spacing.md}`
- 다중 값 (예: `padding`)에 토큰을 섞을 수 있음: `"{spacing.xs} {spacing.sm}"`
- 정의되지 않은 토큰 참조는 빌드 시 에러

### CSS variables 변환 규칙

build.py가 frontmatter를 다음 규칙으로 CSS variables로 변환합니다:

| YAML 키 경로 | 생성되는 CSS variable |
|---|---|
| `colors.primary` | `--color-primary` |
| `colors.bg-var-1` | `--color-bg-var-1` |
| `typography.h1.fontSize` | `--font-h1-size` |
| `typography.h1.fontWeight` | `--font-h1-weight` |
| `typography.h1.fontFamily` | `--font-h1-family` |
| `typography.h1.lineHeight` | `--font-h1-line-height` |
| `rounded.md` | `--rounded-md` |
| `spacing.md` | `--space-md` |
| `elevation.md` | `--shadow-md` |

### components 토큰 → CSS class 변환

components 아래 각 항목은 동일 이름의 CSS class로 변환됩니다:

```yaml
components:
  closing-note:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.bg}"
    rounded: "{rounded.sm}"
    padding: "16px 0"
```

→

```css
.closing-note {
    background: var(--color-primary);
    color: var(--color-bg);
    border-radius: var(--rounded-sm);
    padding: 16px 0;
}
```

지원되는 컴포넌트 속성:
- `backgroundColor` → `background`
- `textColor` → `color`
- `typography` → `font-family`, `font-size`, `font-weight`, `line-height` (참조한 typography 토큰 전체 적용)
- `rounded` → `border-radius`
- `padding`, `margin`, `width`, `height` → 동일
- `elevation` → `box-shadow`
- `border` → `border` (CSS 문법 그대로)

## 마크다운 본문: 9개 표준 섹션

YAML frontmatter 아래 본문은 9개 표준 `##` 섹션 순서로 작성합니다. 본문은 사람이 읽는 디자인 의도/철학 설명이며, 빌드 시에는 무시됩니다 (단 imageprompt 스킬은 Overview/Colors/Typography 본문을 프롬프트 컨텍스트로 활용).

```markdown
## Overview
브랜드 콘셉트 한 줄 + 분위기 키워드 3~5개.

## Colors
컬러 팔레트 사용 의도. 어떤 섹션에 어떤 컬러를 쓰는지.

## Typography
폰트 선정 이유, 위계 (display > h1 > h2 > body).

## Layout
8px 그리드, 860px 최대 폭, 섹션당 padding 120px 10% 같은 레이아웃 규칙.

## Elevation & Depth
입체감 부여 원칙. 모든 카드는 elevation.md 이상. 마지막 마감은 버튼이나 구성 확인 cue가 아니라 상품/결과 인상을 정리하는 `closing-note`로 처리.

## Shapes
라운드 사용 패턴. 카드는 lg, 작은 배지는 sm. 마지막 마감에 버튼형 pill/rounded rectangle을 쓰지 않음.

## Components
주요 컴포넌트 사용 가이드. 어떤 섹션에 어떤 컴포넌트.

## Do's and Don'ts
✅ 본문 32px / 섹션 제목 52px
✅ 모든 카드는 shadow + border 동시 적용
❌ NO :hover, transition, animation
❌ NO JavaScript
❌ 텍스트 체크박스 기호(☐/□) 사용 금지 → check-box 클래스로

## Notes
기타 메모.
```

## 검증

build.py 실행 시 `scripts/design_md.py` 가 다음을 검증합니다:

- YAML frontmatter 존재 여부
- 필수 키: `colors.primary`, `colors.bg`, `colors.text`, `typography.body-md`
- 토큰 참조 유효성 (정의되지 않은 토큰 참조 시 에러)
- 9개 표준 섹션 누락은 경고 (에러 아님)

## 프리셋

`references/design-md-presets/` 에 6개 기본 프리셋 제공:

| 프리셋 | 적합 카테고리 |
|---|---|
| `clean-minimal.design.md` | 테크, 전자제품 |
| `dark-luxury.design.md` | 주얼리, 프리미엄 |
| `warm-natural.design.md` | 유기농, 웰니스, 스킨케어 |
| `soft-modern.design.md` | 패션, 라이프스타일 |
| `fresh-vibrant.design.md` | 식품, 건강식품 |
| `heritage.design.md` | 전통, 한복, 공예품 |

사용법:
```bash
# 프리셋을 프로젝트 루트로 복사
cp <danho-detailpage-coding-skill-dir>/references/design-md-presets/dark-luxury.design.md \
   projects/01241530_my-product/DESIGN.md

# 그 다음 name/description/components 등을 프로젝트에 맞춰 수정
```

또는 planning 스킬이 사용자와 인터뷰 후 자동으로 프리셋을 복사하고 커스터마이징해줍니다.
