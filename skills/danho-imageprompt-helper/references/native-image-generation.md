# Codex Native Image Generation Guide

이 문서는 `danho-imageprompt-helper`가 별도 API 스크립트 대신 Codex 네이티브 이미지 생성 기능을 사용할 때의 운영 기준이다.

## 기본 원칙

- 기본 생성 방식은 Codex native image generation이다.
- `generate_banner.py`, `.env`, `OPENAI_API_KEY`, curl API 호출은 기본 경로에서 사용하지 않는다.
- 생성 전에는 반드시 `image-plan.md`가 사용자와 합의되어 있어야 한다.
- 생성 이미지는 최종적으로 프로젝트의 `assets/generated/` 아래에 위치해야 Phase B에서 사용할 수 있다.

## 생성 순서

1. `prompts/banners.md`의 REPLACE 항목을 먼저 생성한다.
2. 한글 텍스트가 들어간 REPLACE 이미지는 오탈자와 줄바꿈을 검수한다.
3. `prompts/photos.md`의 SUPPORT 항목을 생성한다.
4. SUPPORT 이미지는 텍스트, 캡션, 간판, 라벨이 없어야 한다.
5. 승인된 이미지를 `assets/generated/<id>.png`에 둔다.
6. `assets/generated/manifest.md`를 작성한다.

## REPLACE 검수

REPLACE 이미지는 HTML 카피를 대체한다. 따라서 다음을 확인한다.

- 이미지 안 한글이 `v1-textonly.html` 원문과 일치한다.
- 의미가 바뀐 단어, 빠진 조사, 임의 번역이 없다.
- Phase B에서 제거할 HTML 섹션 id가 manifest에 기록되어 있다.

## SUPPORT 검수

SUPPORT 이미지는 텍스트 섹션을 보조한다. 따라서 다음을 확인한다.

- 이미지 안에 한글/영문 텍스트가 없다.
- 제품이나 사용 장면이 섹션 내용과 직접 연결된다.
- HTML 카피를 반복하는 타이포그래피 이미지가 아니다.

## Manifest 형식

```markdown
# Generated Image Manifest

| file | case | source | prompt_file | status | notes |
|---|---|---|---|---|---|
| hero.png | REPLACE | v1-textonly.html#hero | prompts/banners.md#hero | accepted | Korean copy verified |
| usage.png | SUPPORT | image-plan.md#usage | prompts/photos.md#usage | accepted | no text visible |
```

## Native generation unavailable

현재 Codex 세션에서 네이티브 이미지 생성 기능을 사용할 수 없으면 이미지 생성을 중단하고 사용자에게 알려야 한다. 이때 선택지는 두 가지다.

- 사용자가 생성 이미지를 직접 `assets/inbox/` 또는 `assets/generated/`에 넣는다.
- 사용자가 명시적으로 legacy API fallback 사용을 승인하면 `generate_banner.py`를 사용한다.
