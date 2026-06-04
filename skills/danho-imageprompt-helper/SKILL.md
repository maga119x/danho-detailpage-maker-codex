---
name: danho-imageprompt-helper
description: 상세페이지용 이미지 프롬프트 생성 + Codex 네이티브 이미지 생성. v1-textonly.html과 image-plan.md를 입력으로 받아 REPLACE/SUPPORT 케이스를 구분하고, HTML 카피와의 중복을 방지한다. 트리거 - 이미지 프롬프트 만들어줘, 이미지 생성해줘, 배너 만들어줘, gpt-image, native image generation.
---

# Image Prompt Helper + Native Image Generation (v3 Text-First)

상세페이지에 필요한 이미지 프롬프트를 생성하고, 사용자가 이미지 생성을 승인하면 **Codex의 네이티브 이미지 생성 기능**으로 이미지를 만든다.

기존 `generate_banner.py` + `OPENAI_API_KEY` 방식은 legacy fallback이다. 이 스킬의 기본 경로에서는 별도 API 키, `.env`, curl 호출, 외부 이미지 생성 스크립트를 요구하지 않는다.

**v3 핵심 원칙**: 이미지 프롬프트는 **이미 작성된 HTML (`v1-textonly.html`)**에서 카피를 추출해 만든다. `PLANNING.md`를 직접 보고 카피를 재작성하면 HTML과 표현이 달라져 중복과 불일치가 생길 수 있다.

> 중복 방지의 두 축
> 1. **REPLACE 케이스**: HTML 섹션의 카피를 그대로 추출해 이미지 안 텍스트로 삽입. Phase B에서 해당 HTML `<section>`은 삭제된다.
> 2. **SUPPORT 케이스**: 프롬프트에 `no text, no Korean caption, no overlay text`를 명시. 이미지는 HTML 텍스트를 보조하는 순수 비주얼이어야 한다.
> 상세: [../danho-detailpage-coding/references/text-image-deduplication.md](../danho-detailpage-coding/references/text-image-deduplication.md)

## 입력

- `DESIGN.md` — 디자인 시스템: 컬러, 무드, 폰트, 부정 프롬프트
- `build/<프로젝트명>-v1-textonly.html` — 1차 코딩 결과물: 모든 카피의 source of truth
- `image-plan.md` — 섹션별 `REPLACE` / `SUPPORT` / `NONE` 결정, 사용자 합의 완료 상태

## 출력

- `prompts/banners.md` — REPLACE 중심 디자인 배너 프롬프트
- `prompts/photos.md` — SUPPORT 중심 사진/비주얼 프롬프트
- `assets/generated/*.png` — Codex 네이티브 이미지 생성 결과를 저장할 위치
- `assets/generated/manifest.md` — 생성 이미지와 원본 프롬프트 추적 기록

## 워크플로우

```
1. DESIGN.md + v1-textonly.html + image-plan.md 로드
   ↓
2. image-plan.md의 케이스를 기준으로 섹션 분류
   ↓
3. REPLACE: HTML에서 카피를 그대로 추출해 이미지 텍스트로 사용
   SUPPORT: HTML 카피를 프롬프트에 넣지 않고 no-text 정책 명시
   NONE: 프롬프트/이미지 생성 없음
   ↓
4. prompts/banners.md, prompts/photos.md 작성
   ↓
5. 사용자 승인 후 Codex 네이티브 이미지 생성 기능 호출
   ↓
6. 생성 이미지를 assets/generated/에 저장하고 manifest.md 기록
```

## 사전 검증

진행 전 반드시 확인:

- [ ] `build/<프로젝트>-v1-textonly.html` 존재
- [ ] `image-plan.md` 존재
- [ ] `image-plan.md`가 사용자와 합의됨
- [ ] 각 행의 케이스가 `REPLACE` / `SUPPORT` / `NONE` 중 하나
- [ ] REPLACE 행의 섹션 id가 v1 HTML의 `<section id="...">`와 일치

하나라도 누락되면 이미지 프롬프트/생성 단계로 넘어가지 않는다.

## DESIGN.md 로드 기준

프로젝트 루트의 `DESIGN.md`에서 다음을 추출한다.

- `colors.primary`, `colors.secondary`, `colors.tertiary`
- `mood.keywords`
- `mood.negative`
- `typography.fontFamily`
- Overview 본문의 브랜드 보이스

## 케이스별 프롬프트 규칙

| 케이스 | 출력 파일 | 이미지 텍스트 정책 | HTML 처리 |
|---|---|---|---|
| `REPLACE` | `prompts/banners.md` | HTML 카피를 그대로 이미지 안에 포함 가능 | Phase B에서 원본 section 삭제 |
| `SUPPORT` | `prompts/photos.md` 또는 `prompts/banners.md` | 텍스트 금지. `no text, no Korean caption, no overlay text` 필수 | HTML 유지 + 이미지 추가 |
| `NONE` | 생성 안 함 | 이미지 없음 | HTML 유지 |

### REPLACE 프롬프트

구조:

```text
[Design style] + [Layout structure] + [Product/visual element] + [Exact Korean text from HTML] + [Color scheme] + [Mood] + [Aspect ratio]
```

규칙:

- 카피는 HTML `<h1>`, `<h2>`, `<p>`에서 그대로 추출한다.
- 요약, 재작성, 의역을 금지한다.
- `<span class="block">`은 줄바꿈 의도로 해석한다.
- `**REPLACE_SOURCE**: v1-textonly.html#section-id`를 반드시 기록한다.
- 이미지 생성 후 Phase B에서 제거할 원본 섹션 id를 명확히 남긴다.

예시:

```text
Premium Korean ecommerce hero banner for a silicone kitchen scrubber, clean modern layout, product centered with soft studio light.
Korean text line 1 exactly: "버려도 죄책감 없는"
Korean text line 2 exactly: "항균 실리콘 수세미"
Use bold rounded sans-serif Korean typography, primary accent color from DESIGN.md, 3:4 vertical detail-page composition.
```

### SUPPORT 프롬프트

구조:

```text
[Style] + [Subject] + [Action/Pose] + [Setting] + [Composition] + [Lighting] + [Texture] + [Color] + [Camera] + [No-text policy]
```

규칙:

- HTML 섹션의 카피를 프롬프트에 넣지 않는다.
- 프롬프트 끝에 다음 문구를 반드시 포함한다:
  `no text, no Korean caption, no overlay text, no signage with letters, pure visual`
- negative에도 텍스트 금지를 반복한다.

예시:

```text
Lifestyle kitchen scene, hands washing dishes with a white silicone scrubber, bright natural light, clean countertop, realistic product photography, shallow depth of field, 3:4 vertical composition, no text, no Korean caption, no overlay text, no signage with letters, pure visual.
```

## 출력 문서 형식

### prompts/banners.md

~~~markdown
# 이미지 프롬프트 - 배너 (Codex native image generation)

## 공통사항
- 생성 방식: Codex native image generation
- 저장 위치: assets/generated/
- 브랜드 컬러: <DESIGN.md colors.primary, secondary, tertiary>
- 무드: <DESIGN.md mood.keywords>
- 비율: 3:4
- 제외: <DESIGN.md mood.negative>

---

## 1. hero
**케이스**: REPLACE
**용도**: 히어로 배너
**REPLACE_SOURCE**: v1-textonly.html#hero
**출력 파일명**: hero.png
**권장 비율**: 3:4

```prompt
Premium Korean ecommerce hero banner...
Korean text line 1 exactly: "버려도 죄책감 없는"
Korean text line 2 exactly: "항균 실리콘 수세미"
```

**Phase B 처리**: `<section id="hero">` 삭제 후 `assets/generated/hero.png` 삽입
~~~

### prompts/photos.md

~~~markdown
# 이미지 프롬프트 - 사진/비주얼 (Codex native image generation)

## 공통사항
- 생성 방식: Codex native image generation
- 저장 위치: assets/generated/
- 텍스트 정책: no text, no Korean caption, no overlay text

---

## 1. usage
**케이스**: SUPPORT
**용도**: 사용 장면 보조 이미지
**출력 파일명**: usage.png
**권장 비율**: 3:4

```prompt
Lifestyle kitchen scene...
no text, no Korean caption, no overlay text, no signage with letters, pure visual.
```

**Phase B 처리**: `<section id="usage">` 유지 + 이미지 추가
~~~

## Codex 네이티브 이미지 생성 절차

사용자가 `prompts/banners.md`와 `prompts/photos.md`를 승인하면 다음 절차를 따른다.

1. 생성할 항목을 `image-plan.md` 순서대로 하나씩 처리한다.
2. 각 항목의 코드 블록 전체를 Codex 네이티브 이미지 생성 기능에 전달한다.
3. REPLACE 항목은 한글 텍스트 정확도가 중요하므로 한 번 생성 후 텍스트 오탈자 여부를 확인한다.
4. SUPPORT 항목은 이미지 안 텍스트가 있는지 확인한다. 텍스트가 보이면 같은 프롬프트에 no-text 정책을 강화해 재생성한다.
5. 생성 결과를 `assets/generated/<출력 파일명>.png`에 둔다.
6. `assets/generated/manifest.md`에 다음 정보를 기록한다.

```markdown
# Generated Image Manifest

| file | case | source | prompt_file | status | notes |
|---|---|---|---|---|---|
| hero.png | REPLACE | v1-textonly.html#hero | prompts/banners.md#hero | accepted | Korean copy verified |
| usage.png | SUPPORT | image-plan.md#usage | prompts/photos.md#usage | accepted | no text visible |
```

> 네이티브 생성 결과를 세션이 파일로 바로 저장할 수 없는 환경이면, 생성된 이미지를 사용자에게 보여주고 사용자가 프로젝트의 `assets/generated/` 또는 `assets/inbox/`에 배치하도록 안내한다. Phase B는 실제 파일이 프로젝트 안에 들어온 뒤 진행한다.

## Legacy fallback

`scripts/generate_banner.py`는 과거 API 방식의 fallback 유틸리티다. 이 스킬의 기본 실행 경로에서는 사용하지 않는다.

fallback 사용 조건:

- 사용자가 명시적으로 API 일괄 생성을 요청함
- `OPENAI_API_KEY`를 직접 제공하거나 환경에 설정되어 있음
- Codex 네이티브 이미지 생성 기능을 사용할 수 없음

fallback을 사용할 때도 `REPLACE` / `SUPPORT` / `NONE` 중복 방지 규칙은 동일하다.

## 워크플로우 안에서의 위치

```
1. danho-detailpage-planning      → PLANNING.md + DESIGN.md
                                     ↓
2. danho-detailpage-coding Phase A → build/<프로젝트>-v1-textonly.html
                                     ↓
3. image-plan.md 작성 + 사용자 합의
                                     ↓
4. danho-imageprompt-helper
   ├ prompts/banners.md 작성
   ├ prompts/photos.md 작성
   ├ Codex native image generation 실행
   └ assets/generated/*.png + manifest.md 기록
                                     ↓
5. danho-detailpage-coding Phase B → build/<프로젝트>-v2.html
```

## 세부 가이드 참조

- 텍스트-이미지 중복 방지: [../danho-detailpage-coding/references/text-image-deduplication.md](../danho-detailpage-coding/references/text-image-deduplication.md)
- 네이티브 이미지 생성 운영 가이드: [references/native-image-generation.md](references/native-image-generation.md)
- 스타일/조명/색상 키워드: [references/prompt-guide.md](references/prompt-guide.md)
