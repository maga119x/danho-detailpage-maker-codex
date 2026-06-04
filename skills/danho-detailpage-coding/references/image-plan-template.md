# image-plan.md 작성 양식

> **이 문서의 위치**: `projects/<프로젝트>/image-plan.md`
> **작성 시점**: Phase A (텍스트-온리 빌드) 완료 후, Phase B (이미지 대체 빌드) 전
> **작성자**: Codex + 사용자 (반드시 사용자 합의)

---

## 양식 (이 블록을 복사해 사용)

```markdown
# Image Plan — [프로젝트명]

## 결정 요약

| 케이스 | 개수 | 설명 |
|:------:|:---:|---|
| REPLACE | N개 | HTML 섹션을 이미지로 대체. 이미지 안에 한글 카피 포함 |
| SUPPORT | N개 | HTML 텍스트 유지 + 텍스트 없는 비주얼 이미지 추가 |
| NONE    | N개 | 텍스트만, 이미지 없음 |
| **총** | **N개** | (v1-textonly.html의 섹션 수와 일치) |

**예상 이미지 생성 수**:
- Codex 네이티브 생성 (REPLACE + SUPPORT 일부): N장
- 수동 (촬영/사용자 제공, SUPPORT 일부): N장

---

## 섹션별 결정

| # | 섹션 id | v1 카피 요약 | 케이스 | 이미지 종류 | 이미지 위치 | HTML 텍스트 처리 | 비고 |
|:-:|---|---|:---:|---|---|---|---|
| 01 | hook | "수세미에서 냄새가..." | REPLACE | banner | 단독 | 섹션 전체 삭제 | 슬로건 임팩트 |
| 02 | problem | 3대 문제 체크리스트 | NONE | - | - | 그대로 | 정보형 |
| 03 | hero | "버려도 죄책감 없는..." | REPLACE | banner | 단독 | 섹션 전체 삭제 | 메인 헤드라인 |
| 04 | features | 3대 핵심 기능 카드 | SUPPORT | photo | 텍스트 후 | 그대로 + 이미지 추가 | 디테일컷 |
| 05 | materials | 식약처 인증 LSR | SUPPORT | photo | 텍스트 전 | 그대로 + 이미지 추가 | 소재 질감 |
| 06 | benefits | 4가지 변화 | NONE | - | - | 그대로 | 체크리스트 |
| 07 | options | 컬러 + 구성 | NONE | - | - | 그대로 | 정보형 |
| 08 | reviews | 후기 3개 | NONE | - | - | 그대로 | 리뷰 카드 |
| 09 | faq | Q&A 5개 | NONE | - | - | 그대로 | FAQ |
| 10 | cta | 가격 + 구매 | NONE | - | - | 그대로 | 가격표 |

---

## 케이스별 추가 메모

### REPLACE 섹션들

각 REPLACE 섹션의 **HTML 카피 원문**을 그대로 기록 (imageprompt 스킬이 이걸 그대로 프롬프트에 삽입).

#### #01 hook
```
수세미에서 냄새가 난다고요?
일주일도 안 됐는데 말이에요.
```
- 폰트 스타일 힌트: bold sans-serif, large
- 위치: 중앙 상단

#### #03 hero
```
버려도 죄책감 없는
항균 실리콘 수세미
```
- 폰트 스타일 힌트: 상단 bold sans-serif, 하단 accent color + 더 크게
- 세부: "세균 99.9% 차단, 6개월 사용" 은 이미지 하단에 작은 sub-text로

### SUPPORT 섹션들

각 SUPPORT 섹션의 비주얼 컨셉 (텍스트는 절대 들어가지 않음).

#### #04 features
- 비주얼 컨셉: 항균 시각화 (현미경 뷰 또는 청결한 표면)
- 위치: 텍스트 후 (설명 → 이미지로 증거)
- 금지: 한글, 영문, 캡션, 차트 라벨

#### #05 materials
- 비주얼 컨셉: 실리콘 소재 클로즈업 (매끄러운 질감, 부드러운 빛)
- 위치: 텍스트 전 (이미지로 임팩트 → 설명)
- 금지: 한글, 영문, 인증 마크 텍스트

---

## 검증 체크리스트

이 image-plan.md를 imageprompt 스킬에 넘기기 전 확인:

- [ ] 모든 섹션이 v1-textonly.html의 `<section id>`와 1:1 매칭
- [ ] REPLACE 섹션마다 카피 원문이 v1-textonly.html과 정확히 일치 (재작성/요약 금지)
- [ ] SUPPORT 섹션마다 "텍스트 금지" 명시
- [ ] NONE 섹션은 처리 안 됨이 명확
- [ ] 사용자가 본 결정에 합의함 (이미지 방향과 생성 횟수에 영향을 주기 때문)
- [ ] REPLACE 합계로 v2.html에서 삭제될 HTML 섹션 수 계산 (예: 5개 REPLACE = 5개 `<section>` 삭제)
```

---

## 작성 가이드

### Step 1: v1-textonly.html을 스크롤하며 섹션 단위로 분류

각 `<section id="...">`를 위에서 아래로 보면서 의사결정:

```
이 섹션의 카피는…
├─ 짧고 강렬한 헤드라인/슬로건 → REPLACE
├─ 설명/리스트/카드인데 비주얼이 보강이 될 만하다 → SUPPORT
└─ 정보 밀도가 높다 (FAQ, 통계, 옵션, 가격) → NONE
```

### Step 2: REPLACE 섹션 비율 점검

페이지가 너무 이미지 중심이면 텍스트 정보가 부족해질 수 있음. 권장:

| 페이지 총 섹션 | REPLACE 권장 |
|:---:|:---:|
| ~10개 | 2~3개 |
| ~15개 | 3~5개 |
| ~20개 | 4~6개 |

너무 많으면 SUPPORT로 다운그레이드 (텍스트는 유지, 이미지만 추가).

### Step 3: SUPPORT 이미지 위치 결정

각 SUPPORT 섹션마다 텍스트 전/후/사이 중 하나 선택. 기존 image-handling.md의 가이드를 따라도 됨.

### Step 4: 생성 수량·시간 견적

| 케이스 | 1장당 비용/시간 |
|---|---|
| REPLACE (Codex native image generation) | 생성/검수 시간 |
| SUPPORT (Codex native image generation) | 생성/검수 시간 |
| SUPPORT (외부 촬영) | 시간 + 별도 비용 |

### Step 5: 사용자 합의

image-plan.md 초안을 사용자에게 보여주고 합의. 합의 없이 imageprompt 단계로 넘어가지 마세요.

---

## 이후 단계

image-plan.md 확정 → `danho-imageprompt-helper` 스킬 실행 → Codex 네이티브 이미지 생성 → `danho-detailpage-coding` Phase B 실행
