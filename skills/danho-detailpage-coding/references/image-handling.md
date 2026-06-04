# Image Handling Reference (이미지 처리 가이드)

이미지 배치, 플레이스홀더 처리, 비율 규칙에 대한 상세 가이드입니다.

---

## 1. Flexible Image Placement (유연한 이미지 배치)

**이미지는 섹션 끝에만 있을 필요가 없습니다.** 기획서의 📍위치 지정에 따라 유연하게 배치합니다.

### 위치 지정 패턴

| 위치 | 효과 | 권장 섹션 | HTML 순서 |
|------|------|-----------|-----------|
| 📍후 | 설명 후 증거 제시 | HERO, FAQ, OPTIONS, DOUBT BREAKER | `<section>` → `<div.full-image>` |
| 📍전 | 시각적 임팩트 먼저 | EMPATHY, TARGET, MATERIALS, FOUNDER, CTA | `<div.full-image>` → `<section>` |
| 📍사이 | 단락 구분, 리듬감 | REVIEWS, STORY | `<section>` → `<div.full-image>` → `<section>` |
| 📍교차 | 각 포인트별 설득 | FEATURES, CRAFTSMANSHIP | `<div.full-image>` → `<section>` 반복 |

---

## 2. Image as Separate Element (이미지 분리 규칙)

### CRITICAL: 이미지는 항상 별도 요소로

**콘텐츠 섹션 안에 이미지를 직접 넣지 않습니다.** 위치만 다를 뿐, 이미지는 항상 `.full-image` 컨테이너로 분리합니다.

```html
<!-- ❌ BAD - 이미지가 섹션 안에 있음 -->
<section class="content-section">
    <h2>제목</h2>
    <img src="...">  <!-- 잘못됨! -->
    <p>설명...</p>
</section>

<!-- ✅ GOOD - 텍스트 전 배치 -->
<div id="image-empathy" class="full-image">
    <img src="..." alt="...">
</div>
<section id="empathy" class="content-section">
    <h2>제목</h2>
    <p>설명...</p>
</section>

<!-- ✅ GOOD - 텍스트 후 배치 (기존 패턴) -->
<section id="hero" class="content-section">
    <h2>제목</h2>
    <p>설명...</p>
</section>
<div id="image-hero" class="full-image">
    <img src="..." alt="...">
</div>
```

### 이미지 섹션 CSS

```css
.full-image {
    width: 100%;
    padding: 0;
    margin: 0;
}

.full-image img {
    width: 100%;
    max-width: 100%;
    height: auto;
    display: block;
}
```

---

## 3. HTML Patterns by Position Type (위치별 HTML 패턴)

### 📍후 (텍스트 후) - 증거 제시형

```html
<!-- Hero Section -->
<section id="hero" class="hero-section">
    <h1>제품명</h1>
    <p>설명...</p>
</section>
<!-- Hero Image -->
<div id="image-hero" class="full-image">
    <img src="..." alt="...">
</div>
```

### 📍전 (텍스트 전) - 임팩트형, 분위기 전달

```html
<!-- Empathy Image (이미지 먼저) -->
<div id="image-empathy" class="full-image">
    <img src="..." alt="고민하는 사람 분위기 이미지">
</div>
<!-- Empathy Section -->
<section id="empathy" class="content-section">
    <h2>혹시 이런 고민 있으셨나요?</h2>
    <p>체크리스트...</p>
</section>
```

### 📍사이 (텍스트 사이) - 리뷰, 스토리 구간 분리

```html
<!-- Reviews Section Part 1 -->
<section id="reviews-intro" class="content-section-sm">
    <p class="section-label">REAL REVIEWS</p>
    <h2>실제 사용 후기</h2>
</section>
<!-- Reviews Image -->
<div id="image-reviews" class="full-image">
    <img src="..." alt="리뷰 캡처">
</div>
<!-- Reviews Section Part 2 -->
<section id="reviews-content" class="content-section">
    <div class="review-card">★★★★★ "정말 좋아요..."</div>
    <div class="review-card">★★★★★ "재구매 의사 있어요..."</div>
</section>
```

### 📍교차 (기능/과정별 교차) - FEATURES, CRAFTSMANSHIP 권장

```html
<!-- Feature 1 Image -->
<div id="image-feature-1" class="full-image">
    <img src="..." alt="노이즈 캔슬링 시각화">
</div>
<!-- Feature 1 Section -->
<section id="feature-1" class="content-section">
    <h3>액티브 노이즈 캔슬링</h3>
    <p>주변 소음을 95% 차단합니다.</p>
</section>
<!-- Feature 2 Image -->
<div id="image-feature-2" class="full-image">
    <img src="..." alt="배터리 시각화">
</div>
<!-- Feature 2 Section -->
<section id="feature-2" class="content-section">
    <h3>30시간 배터리</h3>
    <p>충전 걱정 없이 일주일을 사용하세요.</p>
</section>
```

---

## 4. Placeholder Image Handling (플레이스홀더 처리)

이미지가 없는 경우 **반드시** 플레이스홀더 키워드를 사용하고, 최종 단계에서 스크립트로 **실제 이미지 파일**을 생성합니다.

### 키워드 형식

```
{{PLACEHOLDER:설명:너비:높이:테마}}
```

| 파라미터 | 필수 | 기본값 | 설명 |
|----------|------|--------|------|
| 설명 | 필수 | - | 이미지 설명 (한글/영문) |
| 너비 | 선택 | 860 | 이미지 너비 (px) |
| 높이 | 선택 | 600 | 이미지 높이 (px) |
| 테마 | 선택 | light | light / dark / warm |

### 코딩 시 사용 예시

```html
<div class="full-image">
    <img src="{{PLACEHOLDER:메인 제품 이미지:860:860:light}}" alt="메인 제품 이미지">
</div>

<div class="full-image">
    <img src="{{PLACEHOLDER:라이프스타일 컷:860:573:warm}}" alt="사용 장면">
</div>

<div class="full-image">
    <img src="{{PLACEHOLDER:제품 상세:860:645:dark}}" alt="상세 디테일">
</div>
```

### 플레이스홀더 이미지 생성 (필수 - 최종 단계)

HTML 코딩 완료 후, 스크립트로 **실제 PNG 파일**을 생성하고 assets 디렉토리에 저장:

```bash
# 기본 사용 - 프로젝트 디렉토리 지정
python scripts/generate_placeholders_to_assets.py projects/01251245_sleep-asmr-earphone

# 미리보기 (파일 수정 없이)
python scripts/generate_placeholders_to_assets.py projects/my-product --dry-run
```

### 스크립트 동작 방식

1. `build/` 디렉토리의 HTML 파일 스캔
2. `{{PLACEHOLDER:...}}` 키워드 모두 탐지
3. 각 키워드에 대해 PNG 이미지 생성
4. `assets/placeholders/` 디렉토리에 파일 저장
5. HTML 업데이트: 키워드 → 상대 경로 (`../assets/placeholders/xxx.png`)

### 생성되는 파일 구조

```
projects/01251245_sleep-asmr-earphone/
├── build/
│   └── sleep-asmr-earphone.html  # 경로가 업데이트된 HTML
└── assets/
    └── placeholders/
        ├── placeholder_01_메인_제품_이미지_a1b2c3.png
        ├── placeholder_02_라이프스타일_컷_d4e5f6.png
        └── placeholder_03_제품_상세_g7h8i9.png
```

### 기존 base64 방식 (레거시)

인라인 base64 변환이 필요한 경우 기존 스크립트 사용 가능:

```bash
python scripts/replace_placeholders.py output.html
```

---

## 5. Image Ratio Rules (이미지 비율 규칙)

### 권장 비율: 1:1, 3:2, 4:3만 사용

**금지 비율: 16:9** (상세페이지에 부적합 - 가로로 너무 길어 스크롤 시 시각적 임팩트 감소)

| 비율 | 크기 | 용도 | 플레이스홀더 예시 |
|------|------|------|------------------|
| **1:1** | 860x860 | 히어로 메인, 제품 정면, 썸네일 | `{{PLACEHOLDER:메인 제품:860:860:light}}` |
| **3:2** | 860x573 | 라이프스타일, 사용 장면, 스토리 | `{{PLACEHOLDER:라이프스타일:860:573:light}}` |
| **4:3** | 860x645 | 상세 컷, 디테일, 패키지, 구성품 | `{{PLACEHOLDER:제품 상세:860:645:light}}` |

### 비율별 상세 권장 용도

#### 1:1 (정사각형) - 860x860
- 제품 메인 이미지 (히어로)
- 썸네일 이미지
- SNS 공유용 대표 이미지
- 제품 정면/측면 컷

#### 3:2 - 860x573
- 라이프스타일 컷
- 사용 환경/장면 이미지
- 스토리텔링 이미지
- 브랜드 분위기 전달

#### 4:3 - 860x645
- 상세 디테일 컷
- 패키지 이미지
- 구성품 나열
- 클로즈업 샷
- 비교 이미지 (전/후)

---

## 6. Output Checklist (이미지 관련)

### Layout
- [ ] Images in separate `.full-image` sections
- [ ] All images as `<img>` tags (NOT background-image)
- [ ] All images have `max-width: 100%`

### Flexible Image Placement
- [ ] 기획서의 📍위치 지정에 따라 이미지 배치됨
- [ ] 📍전 (텍스트 전): `<div.full-image>` → `<section>` 순서
- [ ] 📍후 (텍스트 후): `<section>` → `<div.full-image>` 순서
- [ ] 📍사이 (텍스트 사이): `<section>` → `<div.full-image>` → `<section>` 구조
- [ ] 📍교차: 이미지 → 텍스트 → 이미지 → 텍스트 반복
- [ ] 이미지가 `<section>` 안에 직접 포함되지 않음 (항상 별도 `.full-image` 컨테이너)

### Image Ratio
- [ ] 16:9 비율 사용 안함
- [ ] 1:1, 3:2, 4:3 비율만 사용

### Placeholder Conversion
- [ ] Placeholder images generated: `python scripts/generate_placeholders_to_assets.py [project_dir]`
- [ ] Generated images saved to `assets/placeholders/` directory
- [ ] HTML paths updated to relative paths (`../assets/placeholders/xxx.png`)
