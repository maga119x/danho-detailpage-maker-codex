# Text-Image Deduplication (텍스트-이미지 중복 방지)

> ⚠️ **이 가이드는 v3 워크플로우의 핵심입니다.**
> 이미지(특히 REPLACE 배너) 안에 들어가는 한글 카피와 HTML 섹션의 카피가 **인접한 위치에서 중복되는 문제**를 방지합니다.

---

## 1. 문제 정의

### 중복이 발생하는 메커니즘

```
[기획서]
  hero 섹션 카피: "버려도 죄책감 없는 항균 실리콘 수세미"
       │
       ├──→ [이미지 프롬프트] "...with Korean headline '버려도 죄책감 없는 항균 실리콘 수세미'..."
       │      └──→ assets/generated/hero.png (이미지 안에 카피 삽입)
       │
       └──→ [HTML] <h1>버려도 죄책감 없는 항균 실리콘 수세미</h1>

  결과: 동일한 카피가 동일 페이지의 인접한 위치에서 두 번 노출 → 시각적 어색함, 정보 중복
```

### 실제 사례 (알파셀러2주차 v1)

| 위치 | 이미지 안 텍스트 | 인접 HTML 텍스트 | 판정 |
|---|---|---|---|
| 04 image-hero + 05 hero | "버려도 죄책감 없는 항균 실리콘 수세미" | `<h1>버려도 죄책감 없는 / 항균 실리콘 수세미</h1>` | ❌ 완전 중복 |
| 02 image-empathy + 01 hook | "수세미에서 냄새가 난다고요?" | `<h2>수세미에서 냄새가 난다고요?</h2>` | ❌ 완전 중복 |
| 13 image-options + 12 options | "WHITE \| GRAY \| MINT" | "화이트 / 그레이 / 민트" | ⚠️ 의미 중복 |

---

## 2. 핵심 원칙

### Rule 1: HTML이 Single Source of Truth

모든 카피는 먼저 **HTML에 작성**된다. 이미지는 그 카피를 보강하거나 대체할 뿐이지, 카피의 출발점이 아니다.

### Rule 2: 한 카피는 한 곳에만

페이지의 인접한 두 슬롯(텍스트 섹션 + 그 옆 이미지 섹션)에 **같은 의미의 한글 카피가 두 번** 들어가면 안 된다.

### Rule 3: 섹션마다 역할 선택

각 슬롯은 셋 중 하나의 역할만 가진다:

| 케이스 | 텍스트 섹션(HTML) | 이미지 섹션 | 사용 시점 |
|:------:|---|---|---|
| **REPLACE** | ❌ 제거 (또는 alt만) | ✅ 한글 카피 포함 | 카피의 시각적 임팩트가 중요한 헤드라인, 슬로건 |
| **SUPPORT** | ✅ 유지 | ✅ 텍스트 없음 (비주얼만) | 텍스트가 설명이고 이미지는 증거/분위기일 때 |
| **TEXT-ONLY** | ✅ 유지 | ❌ 없음 | FAQ, 체크리스트, 통계, 가격 등 |

---

## 3. 의사결정 트리

```
이 섹션의 카피는…
│
├─ 짧고 강렬한 헤드라인/슬로건이고, 비주얼과 함께 보여주면 임팩트가 커진다
│   → REPLACE
│   → HTML <section>은 제거, 이미지 1장에 카피 포함
│
├─ 설명/근거/리스트이고, 이미지는 분위기/사용장면/디테일 보조
│   → SUPPORT
│   → HTML <section> 유지, 이미지는 텍스트 없이 비주얼만 (`no text, no caption` 명시)
│
└─ 정보 밀도가 높은 텍스트(FAQ, 통계, 옵션, CTA 등)
    → TEXT-ONLY
    → HTML <section>만, 이미지 슬롯 없음
```

### 예시 적용 (알파셀러2주차)

| # | 섹션 | 원래 v1 | 권장 v2 |
|:-:|---|---|---|
| 01 | hook ("수세미에서 냄새가...") | HTML+이미지 동시 | **REPLACE** → 이미지만, HTML 섹션 제거 |
| 03 | problem (3대 문제 체크리스트) | HTML만 | **TEXT-ONLY** (그대로) |
| 04+05 | hero image + hero headline | HTML+이미지 동시 | **REPLACE** → 이미지만, HTML hero 섹션 제거 |
| 06 | features (3대 핵심 기능 카드) | HTML만 | **TEXT-ONLY** 또는 **SUPPORT** (텍스트 없는 디테일컷 추가) |
| 09 | image-usage (사용 장면) | 이미지만 | **SUPPORT** (텍스트 없는 라이프스타일 컷) |
| 12+13 | options + image | HTML+이미지 동시 | **SUPPORT** → 텍스트는 한글로 유지, 이미지는 컬러 라인업만 (영문 라벨 제거) |
| 15 | faq | HTML만 | **TEXT-ONLY** |
| 16 | cta | HTML만 | **TEXT-ONLY** |

---

## 4. 이미지 프롬프트 차별화

### REPLACE 케이스 — 텍스트 포함 프롬프트

```
[Visual description], top text area with Korean headline "{HTML에서 추출한 카피}" in bold sans-serif font centered large scale
```

- 카피는 **HTML에서 그대로 복사**해서 프롬프트에 넣는다 (재작성 금지 — 카피 변형으로 인한 의미 분기 방지)
- 이 프롬프트가 들어간 섹션은 HTML에서 해당 `<section>`을 **삭제**

### SUPPORT 케이스 — 텍스트 금지 프롬프트

```
[Visual description], minimalist composition, no text overlay, no Korean text, no captions, pure product/lifestyle photography
```

- 프롬프트 끝에 명시적으로 텍스트 금지 표기
- HTML의 텍스트 섹션은 그대로 유지

---

## 5. HTML 패턴별 처리

### REPLACE 처리

```html
<!-- ❌ BEFORE (중복) -->
<div id="image-hero" class="full-image">
    <img src="../assets/generated/hero.png" alt="히어로 이미지">
</div>
<section id="hero" class="content-section">
    <h1 class="hero-headline">
        <span class="block">버려도 죄책감 없는</span>
        <span class="block accent">항균 실리콘 수세미</span>
    </h1>
    <p class="section-desc">세균 99.9% 차단, 6개월 사용.</p>
</section>

<!-- ✅ AFTER (중복 제거: 이미지만 남김) -->
<div id="image-hero" class="full-image">
    <img src="../assets/generated/hero.png"
         alt="버려도 죄책감 없는 항균 실리콘 수세미 - 세균 99.9% 차단, 6개월 사용">
</div>
```

> 💡 카피의 정보 가치는 `alt` 속성과 이미지 안 텍스트로 모두 보존된다. SEO/접근성도 유지.

### SUPPORT 처리

```html
<!-- ✅ 유지: 텍스트 섹션 + 텍스트 없는 비주얼 이미지 -->
<section id="usage" class="content-section">
    <h2 class="section-title">매일의 설거지가 가벼워집니다</h2>
    <p class="section-desc">세제와 함께, 가족의 식기에 안심하고.</p>
</section>
<div id="image-usage" class="full-image">
    <img src="../assets/generated/usage.png"
         alt="실리콘 수세미로 설거지하는 장면">
</div>
```

---

## 6. 빌드 시 검증

`build.py`가 두 가지 신호로 중복을 감지하도록 운영 가이드:

1. **인접 슬롯 동일 텍스트**: `<section>`의 `<h1>/<h2>` 텍스트와 인접 `<div class="full-image">`의 `alt` (또는 image-plan.md의 prompt) 안에 동일 한글 부분문자열이 30자 이상 등장하면 경고
2. **image-plan.md 누락**: REPLACE로 마킹된 섹션이 HTML에 남아있으면 경고

자동화 미구현 시: 사람이 최종 페이지를 스크롤하며 "같은 카피가 두 번 보이는가"를 육안으로 검토.

---

## 7. 워크플로우 안에서의 적용 시점

```
1. PLANNING.md 작성 시
   → 각 섹션을 모두 텍스트로 작성 (이미지 분리 금지)
   → 각 섹션에 "image-conversion: REPLACE | SUPPORT | NONE" 메모

2. 1차 코딩 (텍스트-온리)
   → 모든 카피가 HTML에 들어간 완전한 페이지
   → 이미지 슬롯은 빈 .image-placeholder 박스

3. image-plan.md 작성
   → 위 의사결정 트리로 섹션별 케이스 확정
   → 어떤 카피를 이미지로 옮길지 명시

4. 이미지 프롬프트 생성
   → REPLACE 케이스: HTML 카피 그대로 프롬프트에 삽입
   → SUPPORT 케이스: 텍스트 금지 명시

5. 이미지 생성

6. 2차 코딩 (이미지 대체)
   → REPLACE 섹션: HTML <section> 삭제, <div class="full-image">만 남김
   → SUPPORT 섹션: <section> 유지, <div class="full-image"> 추가
   → TEXT-ONLY 섹션: 그대로
```
