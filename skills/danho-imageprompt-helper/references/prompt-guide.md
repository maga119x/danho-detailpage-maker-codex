# 나노 바나나 프로 프롬프트 가이드

## 목차
1. [프롬프트 원칙](#프롬프트-원칙)
2. [이미지 유형별 구조](#이미지-유형별-구조)
3. [스타일 키워드](#스타일-키워드)
4. [레이아웃 패턴](#레이아웃-패턴)
5. [한글 텍스트 지정](#한글-텍스트-지정)
6. [조명 및 색상](#조명-및-색상)
7. [피해야 할 실수](#피해야-할-실수)

---

## 프롬프트 원칙

### 자연스러운 문장으로 작성
```
❌ "dog, sunset, beach, realistic"
✅ "A golden retriever sitting on a sandy beach during sunset, photorealistic style"
```

### 명확하고 구체적으로
```
❌ "a cat"
✅ "a fluffy orange British shorthair kitten sitting on a marble countertop, soft morning light"
```

### 명령어 스타일 사용
```
❌ "Could you please create..."
✅ "Create a cinematic portrait..."
```

### 제약 조건 명시
원하지 않는 것도 명시:
- "No text except the title"
- "No cheap infographic style"

---

## 이미지 유형별 구조

### 사진 (Photo)
실제 촬영한 듯한 사실적 이미지

```
[Style] + [Subject] + [Action/Pose] + [Setting] + [Composition] + [Lighting] + [Material/Texture] + [Color] + [Camera] + [Aspect Ratio] + [Negative]
```

**필수 요소**: 앵글/구도, 조명, 재질, 배경, 비율

**제품 사진 예시**:
```
Premium wireless earbuds case on white marble surface with soft shadows, 45-degree angle view, studio lighting with soft key light and fill, glossy plastic with metallic accents, minimalist product photography, 85mm macro lens, shallow depth of field, 3:4 vertical aspect ratio, no reflections, no dust, no fingerprints
```

**인물/모델 예시**:
```
Lifestyle portrait of young Korean woman in casual sweater, relaxed natural pose looking away from camera, bright minimalist interior with large window, shot on 85mm f/1.4 lens, soft natural window light, warm inviting mood, clean background bokeh, 3:4 vertical aspect ratio, no harsh shadows
```

### 디자인 (Web Poster / Hero Design)
상세페이지 히어로/섹션 그래픽

```
[Design Style] + [Layout Structure] + [Visual Element] + [Korean Text Spec] + [Color Scheme] + [Mood] + [Aspect Ratio] + [Negative]
```

**핵심**: 인포그래픽 ❌ → 미니멀 웹포스터/히어로 디자인 ✅

**예시**:
```
Modern luxury skincare e-commerce hero design, clean minimalist web poster layout with soft gradient background in pale pink to white, left side elegant glass serum bottle with water droplets and soft studio lighting, right side text area with Korean headline "촉촉한 피부의 비밀" in refined sans-serif font large scale, subtle botanical leaf accents, premium brand aesthetic, soft diffused lighting, 3:4 vertical aspect ratio, no cluttered elements, no cheap infographic style
```

### 오버레이 (Image Overlay Typography)
배경 이미지 위 텍스트 오버레이

```
[Background Image] + [Overlay Treatment] + [Korean Text Spec] + [Typography Style] + [Mood] + [Aspect Ratio] + [Negative]
```

**오버레이 처리 옵션**:
| 옵션 | 영문 표현 | 용도 |
|------|----------|------|
| 하단 그라데이션 | dark gradient overlay from bottom | 하단 텍스트 |
| 전체 다크닝 | subtle dark overlay for readability | 중앙 텍스트 |
| 비네팅 | vignette effect with center focus | 중앙 강조 |
| 듀오톤 | duotone color overlay | 브랜드 컬러 |
| 블러 | soft gaussian blur background | 텍스트 부각 |

**예시**:
```
Full-bleed serene forest landscape with morning mist and soft sunlight filtering through trees, subtle dark gradient overlay from bottom for text readability, Korean headline "당신의 시간을 되찾으세요" in elegant serif font centered extra-large scale, gentle warm tones with green and golden accents, peaceful healing mood, cinematic atmosphere, 3:4 vertical aspect ratio, no harsh contrast, no busy background elements
```

---

## 스타일 키워드

### 디자인 스타일

| 스타일 | 키워드 |
|--------|--------|
| 모던/미니멀 | `minimalist web poster, clean layout, premium UI design, generous white space, subtle shadows` |
| 고급/럭셔리 | `luxury e-commerce hero design, premium brand aesthetic, sophisticated layout, elegant composition, refined color palette` |
| 활기/다이나믹 | `dynamic promotional poster, vibrant marketing design, energetic layout, bold color contrast, diagonal compositions` |
| 내추럴/오가닉 | `organic natural aesthetic, soft earthy tones, warm lifestyle poster, botanical accents, handcrafted feeling` |
| 테크/미래적 | `futuristic tech hero design, sleek digital aesthetic, modern gradient design, geometric patterns, neon accents` |

---

## 레이아웃 패턴

### 분할 레이아웃
```
split composition: left side product/visual, right side text area
vertical split: top 40% image, bottom 60% content
diagonal split composition with dynamic angle
```

### 중앙 집중형
```
centered layout with hero product and text overlay
symmetrical composition with central focal point
circular composition with product at center
```

### 오버레이형
```
full-bleed background image with text overlay
gradient overlay on photograph with headline
blurred background with sharp foreground text
```

---

## 한글 텍스트 지정

### 기본 패턴
```
Korean text "[한글 내용]" in [폰트 스타일] at [위치], [크기] scale
```

### 폰트 스타일
| 스타일 | 영문 | 용도 |
|--------|------|------|
| 고딕 | bold sans-serif | 대부분 헤드라인 |
| 명조 | elegant serif | 고급 브랜드 |
| 둥근고딕 | rounded sans-serif | 캐주얼 |
| 손글씨 | handwritten style | 오가닉 |
| 임팩트 | impact condensed bold | 할인 강조 |

### 위치
```
at center / at top-left / at top-right / at bottom-left / at bottom-right
as overlay on [element]
```

### 크기
```
extra-large scale (메인 헤드라인)
large scale (서브 헤드라인)
medium scale (본문급)
small scale (부가 정보)
```

---

## 조명 및 색상

### 조명 키워드

| 자연광 | 스튜디오 | 분위기 |
|--------|----------|--------|
| Golden hour | Soft key light | Dramatic shadows |
| Soft morning light | Softbox diffused | Volumetric rays |
| Backlight rim | Ring light | Rembrandt lighting |
| Overcast diffused | Beauty dish | High contrast |

### 색상 팔레트

| 무드 | 색상 조합 |
|------|----------|
| 고급/럭셔리 | black, gold, cream, deep burgundy |
| 클린/미니멀 | white, light gray, soft beige |
| 활기/에너지 | orange, yellow, vibrant coral |
| 차분/신뢰 | navy, teal, slate gray |
| 자연/오가닉 | sage green, terracotta, cream |
| 테크/모던 | electric blue, purple gradient, dark gray |

---

## 피해야 할 실수

| 실수 | 잘못된 예 | 올바른 예 |
|------|----------|----------|
| 비율 누락 | (비율 없음) | `3:4 vertical aspect ratio` |
| 언어 미지정 | `text "할인"` | `Korean text "할인"` |
| 인포그래픽 요청 | `infographic about...` | `minimalist web poster design for...` |
| 레이아웃 미지정 | `banner with product and text` | `split layout: left product, right text` |
| 조명 누락 | (조명 없음) | `studio lighting` 또는 `natural light` |
| 스타일 충돌 | `realistic anime watercolor` | 하나의 명확한 스타일 |
| 과부하 | 20개 이상 지시사항 | 핵심 10-15개 이내 |
