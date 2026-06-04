---
name: danho-detailpage-planning
description: Plan and write copy for Korean e-commerce product detail pages (상세페이지 기획). Use when users need help planning page structure, writing persuasive Korean copy, or creating content strategy for product pages. Outputs PLANNING.md (텍스트 중심) + DESIGN.md (디자인 시스템). Triggers on "상세페이지 기획", "상세페이지 카피", "제품 페이지 구성", "랜딩페이지 기획".
---

# Korean Product Detail Page Planning (v3 Text-First)

한국 이커머스 상세페이지의 설득력 있는 콘텐츠와 구조를 기획.

**v3 핵심 원칙**: 기획 단계에서는 **이미지 슬롯을 미리 분리하지 않는다.** 모든 콘텐츠를 텍스트 섹션으로만 작성하고, 각 섹션에는 "이미지 변환 후보" 메모만 남긴다. 이미지의 종류·위치·텍스트 포함 여부는 코딩 1차(텍스트-온리) 완료 후에 image-plan.md에서 확정한다.

> 🚨 **왜 이렇게 바뀌었나**: v2에서는 PLANNING.md의 같은 카피가 이미지 프롬프트와 HTML에 둘 다 들어가서, 동일 페이지의 인접한 위치에 같은 한글 카피가 두 번 노출되는 사고가 빈번했다. v3은 카피의 source-of-truth를 HTML 한 곳으로 고정한다.
> 상세: [../danho-detailpage-coding/references/text-image-deduplication.md](../danho-detailpage-coding/references/text-image-deduplication.md)

**이 스킬은 두 가지 산출물을 생성합니다:**
1. **`PLANNING.md`** — 섹션별 텍스트 카피 (이미지 분리 금지, 변환 후보 마킹만)
2. **`DESIGN.md`** — 디자인 시스템 (프리셋 선택 후 브랜드명/컴포넌트 일부 커스터마이징)

이후:
- HTML/CSS 구현 (1차 텍스트-온리)은 `danho-detailpage-coding` 스킬
- 이미지 변환 계획 수립 → 이미지 프롬프트/생성은 `danho-imageprompt-helper` 스킬
- 이미지 반영 (2차)은 다시 `danho-detailpage-coding` 스킬

명령 예시의 `<danho-detailpage-coding-skill-dir>`는 `danho-detailpage-coding/SKILL.md`가 들어 있는 실제 디렉터리로 치환하세요. 플러그인 설치 위치는 환경마다 달라질 수 있으므로 전역 고정 경로를 가정하지 않습니다.

## Quick Reference

| 참조 문서 | 용도 |
|----------|------|
| [korean-headline-rules.md](references/korean-headline-rules.md) | **한국어 헤드라인 카피 규칙 (마침표 금지) ⭐ 작성 전 필독** |
| [product-naming-consistency.md](references/product-naming-consistency.md) | **제품 호칭 일관성 룰 (풀네임/단축형/브랜드 단독 3계층) ⭐ PLANNING 필수 블록** |
| [section-library.md](references/section-library.md) | 16개 섹션 모듈 상세 |
| [genre-composition.md](references/genre-composition.md) | 9개 장르별 구성표 |
| [image-guidelines.md](references/image-guidelines.md) | 이미지 수량/배치 가이드 |
| [persuasion-framework.md](references/persuasion-framework.md) | 다단계 설득 구조 |
| [output-format.md](references/output-format.md) | PLANNING.md 양식 |
| [copy-templates.md](references/copy-templates.md) | 카피라이팅 템플릿 |
| [../danho-detailpage-coding/references/design-md-spec.md](../danho-detailpage-coding/references/design-md-spec.md) | DESIGN.md 작성 규격 |
| [../danho-detailpage-coding/references/design-md-presets/](../danho-detailpage-coding/references/design-md-presets/) | 6개 디자인 프리셋 |

---

## Workflow

### Step 1: Information Gathering

**모든 필수 정보가 들어올 때까지 PLANNING.md 작성을 시작하지 마세요.**

#### Pre-Planning Checklist

| 필수도 | 항목 | 확인 |
|--------|------|------|
| ⭐⭐⭐ | 제품명 & 가격 | ☐ |
| ⭐⭐⭐ | **제품 호칭 3계층 (풀네임/단축형/브랜드 단독)** ⭐ | ☐ |
| ⭐⭐⭐ | 브랜드명 & 톤앤매너 | ☐ |
| ⭐⭐⭐ | 타겟 고객층 & 페인포인트 | ☐ |
| ⭐⭐⭐ | 핵심 셀링포인트 | ☐ |
| ⭐⭐ | 제품 카테고리/장르 | ☐ |
| ⭐⭐ | 소재/성분 정보 | ☐ |
| ⭐ | 제품 스토리 | ☐ |
| ⭐ | 보유 이미지 목록 | ☐ |

**⭐⭐⭐ 항목 중 3개 이상 누락 시 기획 진행 불가** → 정보 요청 템플릿 사용

#### Request Template

```
상세페이지 기획을 위해 정보가 필요합니다:

📦 제품 정보
- 제품명:
- 가격:
- 카테고리: (뷰티/패션/식품/가전/건강기능식품/인테리어/기타)
- 소재/성분:
- 사이즈/규격:
- 구성품:
- 옵션:

🏷️ 브랜드 정보
- 브랜드명 (한글/영문):
- 브랜드 슬로건:
- 톤앤매너 (고급/캐주얼/전문적/자연친화/귀여움):

👥 타겟 & 마케팅
- 주요 고객층:
- 고객이 겪는 고민:
- 핵심 셀링포인트:
- 고객이 가질 수 있는 의심/우려:

📸 이미지
- 보유 이미지 종류:
```

---

### Step 2: 디자인 시스템 결정 (DESIGN.md)

카테고리/톤앤매너에 따라 **프리셋 선택**:

| 카테고리/톤 | 추천 프리셋 |
|---|---|
| 테크, 전자제품 | `clean-minimal` |
| 주얼리, 시계, 프리미엄 | `dark-luxury` |
| 유기농, 웰니스, 스킨케어 | `warm-natural` |
| 패션, 라이프스타일, 코스메틱 | `soft-modern` |
| 식품, 음료, 건강기능식품 | `fresh-vibrant` |
| 전통, 한복, 공예품 | `heritage` |

#### 프리셋 → 프로젝트 DESIGN.md 복사

```bash
# 프로젝트 폴더 생성 (날짜/시간 접두사)
mkdir -p projects/$(date +%m%d%H%M)_<프로젝트명>/{prompts,assets/{inbox,generated},build/sections}

# 프리셋 복사
cp <danho-detailpage-coding-skill-dir>/references/design-md-presets/<프리셋명>.design.md \
   projects/<폴더명>/DESIGN.md
```

#### DESIGN.md 커스터마이징 (선택)

복사 후 다음을 프로젝트에 맞춰 수정:
- `name`: 브랜드명
- `description`: 한 줄 컨셉
- 필요 시 `colors.primary` 등 1~2개 컬러만 브랜드 컬러로 교체
- 본문의 `## Overview` 단락에 브랜드 보이스 정리

> ⚠️ **컬러 토큰을 너무 많이 바꾸지 마세요.** 프리셋의 컬러 시스템은 균형이 맞춰져 있습니다. 액센트(`primary`) 한두 개만 브랜드 컬러로 교체하는 정도가 안전합니다.

---

### Step 3: Genre Selection & Section Composition

1. **장르 식별**: 뷰티/건강기능식품/패션/가전/식품/인테리어/선물/크라우드펀딩/장인 중 선택
2. **섹션 구성**: `genre-composition.md` 참조 — 장르별 권장 순서 적용
3. **단계 분할**: 핵심 설득 포인트는 2~3단계로 분할 (`persuasion-framework.md`)

#### 섹션 수 가이드

| 구분 | 섹션 수 |
|------|---------|
| 최소 | 12개 이상 |
| 권장 | 15~18개 |
| 최대 | 25개 이하 |

---

### Step 4: Content Writing

각 섹션별 콘텐츠 작성:
- **섹션 상세**: `section-library.md`
- **카피 템플릿**: `copy-templates.md`

#### 핵심 작성 원칙

1. **기능 → 효과 → 감정** 순서
2. 전문 용어는 쉽게 풀어서
3. 구체적 수치/증거 활용
4. 경쟁 제품과 차별점 부각
5. **체크박스 기호 사용 금지** (`☐`, `□`) → 코딩 시 `.check-box` 클래스로 자동 변환
6. **헤드라인 끝 마침표(.) 금지** — 한국 광고/이커머스 카피 관례. h1·h2·h3·CTA·badge·슬로건성 desc 모두 마침표 없이 끝. 본문 paragraph만 마침표 정상. 상세: [korean-headline-rules.md](references/korean-headline-rules.md) ⭐
   - ❌ "초벌이 가벼워집니다.", "두 가지 면.", "사용 후기."
   - ✅ "초벌이 가벼워집니다", "두 가지 면", "사용 후기"
   - ✅ 물음표/느낌표는 허용: "왜 초벌은 남을까요?", "지금 만나보세요!"
7. **제품 호칭 일관성** — PLANNING.md에 정의한 단축형을 본문 전체에 일관 사용. 브랜드 단독("알파"만) 표기는 푸터·로고에서만, 본문 금지. 상세: [product-naming-consistency.md](references/product-naming-consistency.md) ⭐
   - ❌ "알파를 고른 3가지 이유", "알파는 식세기 앞 단계에..."
   - ✅ "알파 실리콘 수세미를 고른 3가지 이유", "알파 실리콘 수세미는 식세기 앞 단계에..."
   - 첫 등장은 풀네임, 반복 호칭은 단축형 권장

---

### Step 5: 이미지 변환 후보 마킹 (이미지 분리 금지)

**v3에서는 이미지 슬롯을 별도 섹션으로 분리하지 않습니다.** 대신 각 콘텐츠 섹션에 한 줄 메모로 "이미지 변환 후보 등급"만 표시합니다. 실제 이미지의 종류·위치·텍스트 포함 여부는 코딩 1차 완료 후 image-plan.md에서 결정됩니다.

#### 마킹 표기

각 섹션 끝에 한 줄 추가:

```
**이미지 변환 후보**: REPLACE_CANDIDATE | SUPPORT_CANDIDATE | NONE
```

| 등급 | 의미 | 적합 |
|---|---|---|
| **REPLACE_CANDIDATE** | 카피가 짧고 강렬해서 이미지 안 텍스트로 임팩트 있게 보여주면 좋을 후보 | HOOK, HERO, EMPATHY 슬로건, 최종 CTA 헤드라인 |
| **SUPPORT_CANDIDATE** | 텍스트는 유지되고, 비주얼(텍스트 없는 사진)을 곁들이면 좋을 후보 | FEATURES, MATERIALS, USAGE, REVIEWS, STORY |
| **NONE** | 텍스트만으로 충분, 이미지 불필요 | FAQ, SPECS, FOOTER, OPTIONS 본문, 가격표 |

> ⚠️ 이건 **후보 마킹**일 뿐 확정이 아닙니다. HTML 완성 후 image-plan.md 단계에서 사용자와 함께 최종 결정합니다.

#### 카피 작성 시 유의

REPLACE_CANDIDATE로 마킹할 섹션은:
- 카피가 **짧고 시각적**일 것 (1~2줄, 30자 이내 헤드라인)
- 카피 자체가 정보가 아니라 **감정·임팩트** 전달 목적일 것
- 이 카피가 4단계에서 이미지 안에 들어가게 됨 → **HTML과 이미지 안에서 동일하게 사용**되므로, 어색하지 않은 표현 사용

SUPPORT_CANDIDATE 섹션은:
- 텍스트는 정보 전달 (설명, 리스트, 통계)
- 이미지는 비주얼 보조 (사용 장면, 분위기, 디테일컷, 제품샷)
- **이미지에는 텍스트 절대 들어가지 않음** (4단계 imageprompt에서 강제됨)

NONE 섹션은:
- 정보 밀도가 높은 텍스트 (FAQ, 통계, 옵션 비교, 가격 안내)
- 이미지를 넣어도 가치 추가 없음

#### 절대 금지 (v2 잔재)

```
❌ ### 03. image-empathy  ← 이미지를 별도 섹션으로 분리하지 마세요
   **유형**: 이미지
   **size**: 1024x1024
   ...

❌ | 03 | image-empathy | 이미지 | ... | banner / empathy |  ← 섹션 구성표에 이미지 슬롯 분리 금지
```

```
✅ ### 03. empathy
   > 일반 수세미가 가진 3가지 문제
   > - 사용 3일 후 세균 수 100만 마리
   > - 코팅팬에 미세 흠집
   > - 1~2주마다 교체 → 연 26개 폐기
   **이미지 변환 후보**: SUPPORT_CANDIDATE
```

`image-guidelines.md`는 v2 호환 참조 문서이며, v3에서는 위 마킹 가이드를 우선합니다.

---

### Step 6: Output

**산출물 위치:** `projects/MMDDHHmm_<프로젝트명>/`

1. **PLANNING.md** — 기획서 (양식: `output-format.md`)
2. **DESIGN.md** — 프리셋 복사 + 커스터마이징
3. **config.json** — 메타데이터
   ```json
   {
     "title": "브랜드명 | 제품명"
   }
   ```

PLANNING.md 에 반드시 포함 (v3):
1. 기본 정보 (브랜드, 제품, 가격, 톤앤매너, **DESIGN.md 프리셋명**)
2. 섹션 구성표 (장르, 총 섹션 수, 순서) — **이미지 슬롯 분리 금지**
3. 단계 분할 적용 표
4. 섹션별 콘텐츠 (카피 + **이미지 변환 후보 마킹**)
5. 이미지 변환 후보 요약표 (REPLACE_CANDIDATE / SUPPORT_CANDIDATE / NONE 개수)

> ⚠️ v2와 달리, **이미지 수량 검증표는 만들지 않습니다.** 실제 이미지 개수는 image-plan.md 단계에서 확정됩니다.

---

## Next Steps (v3)

기획 완료 후 **반드시 다음 순서로**:

1. **사용자 승인** 받기 (PLANNING.md + DESIGN.md)
2. **1차 코딩 (텍스트-온리)**: `danho-detailpage-coding` 스킬 → Phase A
   - 입력: `PLANNING.md` + `DESIGN.md`
   - 출력: `build/<프로젝트명>-v1-textonly.html`
   - 이 단계에서 페이지는 텍스트만으로도 완전해야 합니다 (이미지 슬롯은 placeholder)
3. **이미지 변환 계획 수립**: `image-plan.md` 작성 (사용자와 합의)
   - 입력: `v1-textonly.html`
   - 출력: `image-plan.md` — 각 섹션을 `REPLACE` / `SUPPORT` / `NONE` 중 하나로 확정
4. **이미지 프롬프트 + Codex 네이티브 이미지 생성**: `danho-imageprompt-helper` 스킬
   - 입력: `v1-textonly.html` + `image-plan.md` + `DESIGN.md`
   - 출력: `prompts/banners.md` + `prompts/photos.md` + `assets/generated/*.png`
5. **2차 코딩 (이미지 대체)**: `danho-detailpage-coding` 스킬 → Phase B
   - 입력: `v1-textonly.html` + `image-plan.md` + `assets/`
   - 출력: `build/<프로젝트명>-v2.html` (REPLACE 섹션의 HTML 텍스트는 제거되고 이미지로 대체)

> ⚠️ 1단계(기획) → 2단계(텍스트-온리 코딩) 사이에 이미지 작업을 끼워넣지 마세요. HTML 카피와 이미지 카피의 중복 사고가 발생합니다.
