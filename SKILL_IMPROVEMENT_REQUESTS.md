# Skill Improvement Requests

이 문서는 스킬 개선 요청을 최종 반영 전까지 누적하는 작업 메모다. 사용자가 추가로 지시하는 개선사항을 이 파일에 먼저 기록하고, 최종 개선 단계에서 관련 `SKILL.md`, references, scripts, `PROJECT_STRUCTURE_AI_CONTEXT.md`에 반영한다.

## 기준 프로젝트

- 테스트 상세페이지: `projects/06041615_magnetic-doorstopper/`
- 최종 HTML: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v2.html`
- 기준 상품: 자석도어스토퍼

## 누적 개선 요청

### 1. 콘텐츠 영역 기본 비율

**요청일**: 2026-06-04

**사용자 요청**:
섹션에서 설명하려는 하나의 콘텐츠는 기본적으로 `9:16` 비율로 영역이 설정되어야 한다. 이유는 상세페이지가 모바일 우선이기 때문이다.

**의도**:
- 상세페이지를 모바일 화면에서 먼저 소비하는 구조로 설계한다.
- 하나의 설명 단위가 모바일 상세페이지에서 한 화면 단위로 읽히도록 한다.
- 텍스트 섹션, 타이포 이미지, SUPPORT 이미지 등 주요 콘텐츠 블록의 기본 시각 프레임을 세로형으로 맞춘다.

**최종 반영 후보**:
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/layout-rules.md`
- `danho-detailpage-coding/references/image-handling.md`
- `danho-imageprompt-helper/SKILL.md`
- `danho-imageprompt-helper/references/native-image-generation.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 주요 설명 콘텐츠 블록의 기본 프레임은 `aspect-ratio: 9 / 16`.
- 상세페이지 이미지는 기본적으로 `9:16` 세로형을 우선한다.
- 한 섹션이 여러 메시지를 담으면, 메시지 단위로 9:16 콘텐츠 블록을 분리한다.
- 예외는 표, FAQ, 가격/옵션, 긴 비교표처럼 정보 밀도가 높아 고정 비율이 오히려 읽기를 해치는 섹션으로 제한한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v2.html`
- `full-image` 블록에 `aspect-ratio: 9 / 16` 적용.
- 설명형 `content-section` 기본 높이를 `min-height: min(1528px, 177.78vw)`로 설정해 860px 상세페이지 폭 기준 9:16에 맞춤.
- `compare`, `proof`, `options`, `faq`, `footer`는 정보 밀도 때문에 `section-auto` 예외 처리.
- 타이포 이미지(`hook`, `promise`, `cta`)는 9:16 프레임 안에서 글자 잘림을 막기 위해 `object-fit: contain` 적용.

### 2. 9:16 내부 콘텐츠 레이아웃 설계

**요청일**: 2026-06-04

**사용자 요청**:
단순히 섹션 비율만 `9:16`으로 만드는 것이 아니라, 그 안의 콘텐츠 레이아웃도 `9:16` 비율을 고려해서 만들어야 한다. 기존 HTML 템플릿이 원인이라면 템플릿도 개선해야 한다.

**의도**:
- 모바일 상세페이지의 한 화면을 하나의 완성된 콘텐츠 카드처럼 설계한다.
- 9:16 프레임 안에서 헤드라인, 설명, 리스트/카드, 여백, 강조 요소가 균형 있게 배치되어야 한다.
- 기존 템플릿의 단순 `padding + vertical text flow` 방식은 9:16 모바일 콘텐츠에 충분하지 않다.

**최종 반영 후보**:
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/layout-rules.md`
- `danho-detailpage-coding/references/design-patterns.md`
- `danho-detailpage-coding/scripts/build.py`
- `danho-detailpage-coding/references/css-examples.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 9:16 섹션은 단순 `min-height`가 아니라 내부 wrapper를 가진다. 예: `.story-frame`, `.story-kicker`, `.story-title`, `.story-body`, `.story-grid`, `.story-bottom`.
- 9:16 프레임 내부는 상단 메시지, 중앙 핵심 콘텐츠, 하단 보조 정보/증거로 나눈다.
- 한 섹션 안의 콘텐츠 양이 프레임을 초과하면 같은 섹션을 여러 9:16 프레임으로 분리한다.
- 템플릿 기본 CSS에 모바일 스토리 프레임 컴포넌트를 추가해야 한다.
- 정보형 예외 섹션도 예외 이유를 명시하고, 가능한 경우 내부 카드 단위는 9:16 또는 세로 카드 흐름을 유지한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v2.html`
- 기존 `텍스트 섹션 + 별도 이미지 섹션` 구조를 제거하고, SUPPORT 섹션을 `이미지 배경 + scrim + 텍스트 오버레이 카드` 구조로 통합.
- 모든 `<section>`이 `panel` 클래스를 갖도록 정리해 9:16 패널 기준을 일관화.
- `pain`, `install`, `rental`, `stroller`, `adjustable`, `material` 6개 SUPPORT 섹션을 혼합형 패널로 재구성.
- `compare`, `proof`, `options`, `faq`도 별도 자동 높이 예외가 아니라 9:16 정보 패널로 재구성.
- 검증 결과: 이미지 9개, 누락 0개, 섹션 14개 모두 panel 적용, 분리된 SUPPORT 이미지 div 0개.

### 3. 상세페이지 섹션별 디자인 리듬 차별화

**요청일**: 2026-06-04

**사용자 요청**:
상세페이지의 각 섹션이 동일한 디자인과 레이아웃으로 반복되면 안 된다. 상세페이지 디자인 관련 내용을 웹검색으로 사전 조사하고, 그 결과를 반영한 디자인으로 개선해야 한다.

**리서치 기반 의도**:
- 모바일 상세페이지는 작은 화면에서 핵심 구매 정보, 상품 이미지, 적합 조건, 신뢰 요소가 빠르게 파악되어야 한다.
- 섹션은 같은 템플릿을 반복하기보다 구매 의사결정 흐름에 따라 역할이 달라야 한다.
- 이미지, 카피, 비교, 후기, FAQ, 옵션 정보는 각각 다른 시각 구조로 설계해 스크롤 리듬을 만든다.

**최종 반영 후보**:
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/layout-rules.md`
- `danho-detailpage-coding/references/design-patterns.md`
- `danho-detailpage-coding/references/css-examples.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 같은 `9:16` 패널 안에서도 섹션 역할별 레이아웃 패턴을 분리한다.
- 권장 패턴 예시:
  - 구매 판단 요약: 제품명, 가격, 적합 조건, 구성 정보를 초반에 노출.
  - 문제 제기: 생활 이미지 위에 이슈 리스트를 겹쳐 배치.
  - 설치 설명: 이미지 배경 위 단계 카드 또는 순서형 모듈.
  - 원상복구/전세집: 제거 후 상태, 타공/접착 회피를 증거형 카드로 표시.
  - 생활 장면: 풀블리드 이미지와 스토리 밴드 오버레이.
  - 소재/디테일: 제품 이미지를 크게 두고 기능 콜아웃을 배치.
  - 비교: 표 대신 모바일에서 읽기 쉬운 비교 카드 구조 우선.
  - 후기/신뢰: 서로 다른 위치의 리뷰 카드로 리듬을 만든다.
  - 옵션/FAQ: 구매 직전 정보로 하단에 배치하되 각각 독립된 UI 패턴을 사용.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v2.html`
- 초반에 `decision` 패널을 추가해 제품명, 가격, 구매 전 적합 조건을 노출.
- SUPPORT 섹션 6개는 서로 다른 패턴으로 변경: 문제 리스트, 설치 3단계, 원상복구 증거 리본, 생활 스토리 밴드, 높이 조절 게이지, 소재 콜아웃.
- 정보 섹션 4개도 비교 카드, 엇갈린 후기 카드, 상품 옵션 카드, Q&A 리스트로 패턴을 분리.
- 카드 반경은 8px 이하로 정리하고, 모바일 패널 안에서 텍스트와 이미지가 분리되어 떠 보이지 않도록 오버레이/혼합 구조를 사용.

### 4. 내부 섹션 라벨 노출 금지

**요청일**: 2026-06-04

**사용자 요청**:
`모바일 구매 판단 요약`, `불편의 순간`, `설치 방식` 같은 라벨이 상세페이지 디자인에 노출되면 안 된다.

**의도**:
- 섹션 역할을 설명하는 내부 기획용 라벨은 최종 상세페이지 화면에 표시하지 않는다.
- 사용자는 라벨을 읽는 것이 아니라 헤드라인, 이미지, 카드, 비교 구조를 통해 메시지를 이해해야 한다.
- `kicker`, `badge`, `label` 같은 UI는 프로모션 문구나 실제 상품 속성일 때만 제한적으로 사용한다.

**최종 반영 후보**:
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/layout-rules.md`
- `danho-detailpage-coding/references/design-patterns.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 최종 HTML에는 내부 섹션 타입을 직접 노출하는 라벨을 넣지 않는다.
- 예: `문제`, `설치 방식`, `소재감`, `FAQ`, `구매 전 확인`, `모바일 구매 판단 요약` 같은 분류명은 화면 밖 기획 문서나 주석에만 둔다.
- 필요 시 실제 판매 카피로 자연스럽게 녹인다. 예: `자석 부착`, `무타공`, `본품 1개`처럼 구매 판단에 직접 필요한 속성 배지는 허용.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v2.html`
- 화면에 노출되던 모든 `.kicker` 요소와 관련 CSS를 제거.
- 섹션 식별 주석은 `split_sections.py` 산출물 생성을 위한 비노출 메타데이터로 유지.

### 5. 균등 분배 템플릿 금지 및 포스터형 패널 구성

**요청일**: 2026-06-04

**사용자 요청**:
하나의 섹션에서 콘텐츠 사이 간격이 너무 떨어져 미완성처럼 보인다. 상세페이지 디자인은 의도된 페이지 디자인처럼 보여야 하며, 기존 템플릿과 무관하게 다시 만들어야 한다.

**의도**:
- `grid-template-rows: auto 1fr auto` 같은 균등 분배형 템플릿은 모바일 상세페이지에서 빈 공간을 크게 만들 수 있다.
- 한 화면 안에서 이미지, 헤드라인, 카드, 보조 정보가 서로 분리되어 떠 있지 않고 하나의 설계된 장면처럼 물려야 한다.
- 9:16 비율을 유지하되, 내부 레이아웃은 포스터/에디토리얼 광고처럼 밀도 있게 구성한다.

**최종 반영 후보**:
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/layout-rules.md`
- `danho-detailpage-coding/references/design-patterns.md`
- `danho-detailpage-coding/references/css-examples.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 기본 상세페이지 템플릿에서 상단/중앙/하단 균등 분배 구조를 기본값으로 두지 않는다.
- 9:16 패널은 절대 배치, 이미지 크롭, 오버레이 카드, 제품 이미지 배경, 하단 보드 등 섹션별 조합으로 설계한다.
- 텍스트 블록과 이미지 사이의 큰 빈 공간이 생기면 실패로 본다.
- 정보 섹션도 단순 텍스트 카드가 아니라 제품 이미지, 가격, 비교행, 리뷰 스택, Q&A 카드가 화면 안에서 조밀하게 결합되어야 한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v2.html`
- 기존 `.layer` 균등 그리드 중심 구조를 제거하고, `.copy`, `.card`, `.media`의 절대 배치 기반 포스터형 패널로 재작성.
- SUPPORT 섹션은 이미지 위에 하단 보드/스텝 카드/증거 타일/스토리 밴드/조절 카드/소재 콜아웃을 붙여 시각적으로 한 화면 안에 결합.
- 비교, 후기, 옵션, FAQ도 배경 제품 이미지와 카드 스택을 사용해 간격이 벌어지지 않도록 재구성.
- 이후 레이아웃 깨짐 확인 과정에서 `left/right/bottom`만 있고 `position:absolute`가 빠진 요소가 실제 렌더에서 겹침을 만들 수 있음을 확인. 위치 속성을 쓰는 오버레이 요소는 반드시 `position`과 `z-index`까지 함께 검증해야 한다.
- 정보량이 많은 후반 섹션(`compare`, `proof`, `options`, `faq`)은 절대 배치보다 `info-wrap` 흐름형 포스터 레이아웃이 더 안정적이다.
- Playwright 모바일 393px 렌더 검사로 주요 섹션 11개에서 패널 밖 이탈과 요소 겹침 0건을 확인.
- 공통 `.card`가 `position:absolute`를 갖는 구조에서는 후반 정보 카드가 의도치 않게 절대 배치를 상속할 수 있다. 흐름형 카드에는 `position: relative`를 명시하거나, 공통 카드 클래스에 위치 속성을 두지 않는 방향으로 템플릿을 개선해야 한다.
- `options`처럼 상품명, 가격, 제품 이미지, 옵션, 주의 문구가 함께 있는 구매 정보 섹션은 이미지 블록과 가격 카드를 분리하지 말고 하나의 구매 카드 내부에 통합하는 편이 안정적이다.

### 6. 콘텐츠 부족 섹션 3:4 전환 및 마지막 타이포 이미지 마감

**요청일**: 2026-06-04

**사용자 요청**:
섹션에 아직 여백이 있는 곳이 있다. 콘텐츠 내용이 부족한 섹션은 `3:4` 비율로 수정하여 의도 없는 여백이 생기지 않게 한다. 마지막 섹션의 단순 텍스트도 히어로 이미지처럼 마지막 인상을 남기는 타이포 오버레이 이미지로 만들어야 한다.

**의도**:
- 모든 섹션을 무조건 `9:16`으로 고정하지 않는다.
- 메시지 밀도가 낮은 정보 섹션은 더 짧은 `3:4` 비율을 사용해 완성된 카드처럼 보이게 한다.
- 마지막 마감 섹션은 텍스트만 남기지 말고 이미지와 타이포가 결합된 완성 이미지로 처리한다.

**최종 반영 후보**:
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/layout-rules.md`
- `danho-detailpage-coding/references/design-patterns.md`
- `danho-imageprompt-helper/references/native-image-generation.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 기본 설명형 섹션은 `9:16`, 정보량이 적은 후반 정보 섹션은 `3:4`를 허용한다.
- 3:4 대상은 기계적으로 정하지 말고 실제 콘텐츠 밀도와 렌더 여백을 기준으로 판단한다.
- 마지막 CTA/마감 섹션은 가능하면 타이포 오버레이 이미지로 처리해 상세페이지의 끝 인상을 만든다.
- 사용자가 이미지 모델 생성을 명시하면 브라우저 합성/HTML 렌더 이미지가 아니라 이미지 모델로 생성한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v2.html`
- `compare`, `proof`, `options`, `faq`에 `compact-panel`을 추가해 `aspect-ratio: 3 / 4` 적용.
- 마지막 `footer` 섹션을 `final-typography-overlay.png` 이미지 전체 삽입으로 교체.
- Playwright 모바일 393px 렌더 검사에서 3:4 섹션 4개 모두 ratio 0.75, 패널 밖 이탈 0건 확인.

### 7. 상세페이지 기획 흐름 단절 방지

**요청일**: 2026-06-04

**사용자 요청**:
기획 스킬을 사용해 기획을 다시 해야 한다. 현재 상세페이지 구성은 섹션 간 연결감이 너무 떨어진다.

**의도**:
- 기능 항목을 병렬 나열하는 방식으로 상세페이지를 구성하지 않는다.
- 고객이 스크롤하며 납득하는 의사결정 흐름을 먼저 설계한다.
- 생활 장면, 문제, 기존 해결 방식의 부담, 제품 방식의 전환, 구매 전 조건 확인, 사용 확신, 비교, 구매 행동이 자연스럽게 이어져야 한다.

**최종 반영 후보**:
- `danho-detailpage-planning/SKILL.md`
- `danho-detailpage-planning/references/persuasion-framework.md`
- `danho-detailpage-planning/references/genre-composition.md`
- `danho-detailpage-planning/references/section-library.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 기획 단계의 섹션 구성표에는 각 섹션의 `설득 역할` 또는 `이전 섹션과의 연결 이유`를 명시한다.
- 기능별 섹션을 만들기 전에 먼저 핵심 구매 불안을 정리한다. 예: 사용 조건, 설치 부담, 원상복구, 실제 사용 장면, 가격·구성.
- 비슷한 생활 장면은 분산하지 말고 하나의 흐름 섹션으로 묶는다. 예: 환기, 유모차, 짐 이동은 `daily-use`로 통합.
- 구매 조건 확인 섹션은 후반 FAQ에만 두지 말고 초반 판단 구간에 배치한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/PLANNING.md`
- 기존 14개 기능 나열형 기획을 16개 설득 흐름형 기획으로 재작성.
- 새 흐름: `hook → scene-problem → blocker → answer → fit-check → install-flow → no-damage → daily-use → control → fit-adjust → material → compare → review-proof → options → faq → final-cta`.

### 8. 이미지 모델 생성 후 한글 타이포 검증과 HTML 오버레이 fallback

**요청일**: 2026-06-04

**사용자 요청**:
새 기획을 바탕으로 이미지를 생성해서 최종 버전을 만든다.

**의도**:
- 이미지 모델로 생성한 상세페이지 이미지를 최종 HTML에 반영한다.
- REPLACE 이미지의 한글 카피는 반드시 육안 검증한다.
- 한글 타이포가 부정확하면 해당 이미지를 그대로 쓰지 않고, 텍스트 없는 이미지 배경 + 정확한 HTML 오버레이로 전환한다.

**최종 반영 후보**:
- `danho-imageprompt-helper/SKILL.md`
- `danho-imageprompt-helper/references/native-image-generation.md`
- `danho-detailpage-coding/references/text-image-deduplication.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- REPLACE로 계획한 섹션이라도 이미지 모델의 한글 텍스트가 틀리면 SUPPORT로 재분류할 수 있다.
- 이 경우 이미지 모델로 생성한 텍스트 없는 제품/장면 이미지를 배경으로 쓰고, 원본 HTML 카피를 오버레이해 정확도를 보장한다.
- SUPPORT 이미지는 반드시 `no text, no Korean caption, no overlay text` 정책을 유지한다.
- 최종 HTML은 Playwright 모바일 렌더로 이미지 로딩, 섹션 비율, overflow를 검증한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v4-final.html`
- 새 생성 이미지: `answer-background.png`, `blocker-rental-concern.png`, `control-foot-use.png`.
- `answer`는 REPLACE 타이포 생성 결과의 한글이 부정확하여, 텍스트 없는 배경 이미지 + HTML 오버레이로 변경.
- 최종 검증: 16개 섹션, 이미지 11개 + CSS 배경 1개 누락 0, 모바일 렌더 overflow 0, `:hover`/`transition`/`animation`/`script` 없음.

### 9. 섹션 전체를 이미지 모델 생성 디자인 이미지로 제작

**요청일**: 2026-06-04

**사용자 요청**:
각 섹션을 페이지 렌더링으로 이미지화하는 것이 아니라, 이미지 모델로 내용과 디자인을 포함한 상세페이지 섹션 이미지를 생성해야 한다.

**의도**:
- HTML/CSS로 디자인을 만든 뒤 캡처하지 않는다.
- 이미지 모델이 각 섹션의 배경, 제품 장면, 타이포, 카드, 아이콘, 정보 구성을 포함한 하나의 완성 이미지로 생성해야 한다.
- 최종 HTML은 생성된 섹션 이미지를 순서대로 배치하는 형태가 될 수 있다.

**최종 반영 후보**:
- `danho-imageprompt-helper/SKILL.md`
- `danho-imageprompt-helper/references/native-image-generation.md`
- `danho-detailpage-coding/references/image-handling.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 사용자가 “디자인된 이미지를 생성”한다고 말하면, 브라우저 렌더/HTML 합성 PNG가 아니라 이미지 모델 직접 생성으로 처리한다.
- 각 섹션 프롬프트에는 `complete Korean ecommerce product detail page section image`, `include content and design`, `not a plain photo`를 명시한다.
- 생성 결과는 `assets/generated/ai-section-designs/` 같은 별도 폴더에 저장한다.
- 최종 HTML은 각 섹션 이미지를 `<section>`으로 감싸서 순서대로 배치한다.
- 한글 오탈자는 이미지 모델 한계가 있으므로, 생성 후 육안 검토 및 필요한 경우 문구를 짧게 바꾸어 재생성한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v5-ai-section-images.html`
- 생성 폴더: `projects/06041615_magnetic-doorstopper/assets/generated/ai-section-designs/`
- 16개 섹션 이미지를 이미지 모델로 생성/저장하고 최종 HTML에 배치.
- FAQ의 `붙나요`는 이미지 모델이 반복적으로 `불나요`로 오생성하여, 같은 의미의 짧은 문구(`철문·방화문 가능`, `접착제 사용 안 함`, `떼어 이동 가능`)로 재생성.
- 검증 결과: 이미지 16개, 누락 0개, 섹션 16개, 모바일 렌더 이미지 로딩 정상.

### 10. 이미지 모델 생성 섹션과 HTML 코딩 섹션의 하이브리드 운영

**요청일**: 2026-06-04

**사용자 요청**:
당시에는 전체 섹션을 이미지 모델 생성 디자인 이미지와 HTML 코딩 섹션으로 같은 비중에 가깝게 구성해 하이브리드 버전을 제작하자는 요청이었다.

**현재 상태**: 2026-06-18의 36번 규칙으로 고정 비율 운영은 폐기했다. 이 항목은 당시 하이브리드 구조를 도입한 이력으로만 본다.

**의도**:
- 모든 섹션을 이미지로 고정하면 수정성과 정보 정확도가 떨어질 수 있다.
- 반대로 모든 섹션을 HTML로 만들면 감성적 장면, 강한 타이포, 완성된 배너 인상이 약해질 수 있다.
- 시각적 설득이 중요한 섹션은 이미지 모델 생성 디자인 이미지로, 가격·FAQ·비교·조건처럼 정확성과 수정성이 중요한 섹션은 HTML로 유지한다.

**최종 반영 후보**:
- `danho-detailpage-planning/SKILL.md`
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/image-handling.md`
- `danho-detailpage-coding/references/text-image-deduplication.md`
- `danho-imageprompt-helper/references/native-image-generation.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 이미지 모델 생성 우선 섹션: 첫인상 hook, 생활 문제 장면, 구매 불안, 제품의 해법 전환, 원상복구/무타공 인상, 일상 사용 장면, 발 조작 장면, 마지막 CTA.
- HTML 코딩 우선 섹션: 구매 전 조건 체크, 설치 단계, 높이/호환 조건, 소재 상세, 비교표, 후기, 상품 옵션/가격, FAQ.
- 당시 테스트에서는 사용자가 지정한 하이브리드 비율을 따랐다. 현재 운영은 36번 규칙에 따라 고정 비율 없이 `image-plan.md`가 필요한 이미지 수량을 정한다.
- 이미지 섹션은 `<section class="image-section"><img class="section-image">` 구조로 단순화하고, HTML 섹션은 기존 `panel`/`compact-panel` 규칙을 유지한다.
- 이미지 모델 안의 한글 텍스트가 틀릴 위험이 큰 긴 문장, 가격, 조건, FAQ 답변은 이미지가 아니라 HTML로 처리한다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v6-hybrid.html`
- 이미지 섹션 8개: `hook`, `scene-problem`, `blocker`, `answer`, `no-damage`, `daily-use`, `control`, `final-cta`.
- HTML 섹션 8개: `fit-check`, `install-flow`, `fit-adjust`, `material`, `compare`, `review-proof`, `options`, `faq`.
- 이미지 섹션 소스: `projects/06041615_magnetic-doorstopper/assets/generated/ai-section-designs/`.

### 11. 9:16 고정 섹션 취소 및 여백형 하이브리드 레이아웃

**요청일**: 2026-06-05

**사용자 요청**:
섹션을 `9:16`으로 고정하는 방식을 취소한다. 대신 섹션 상하단에 충분한 여백을 두고, 이모지나 말풍선 같은 다양한 시각 요소를 적극 활용한다. HTML을 활용하는 부분도 HTML만 쓰라는 뜻이 아니며, 이미지가 소비자 설득에 효과적이면 HTML 코딩 섹션 안에도 이미지를 함께 사용한다.

**의도**:
- 모바일 우선이더라도 섹션 높이를 특정 비율로 강제하지 않는다.
- 콘텐츠 양과 설득 역할에 따라 자연 높이 섹션을 만들고, 상하 padding으로 호흡을 만든다.
- HTML 섹션은 텍스트 정보만 쌓는 구간이 아니라 이미지, 제품 컷, 말풍선, 이모지 배지, 비교 카드가 결합된 설득형 레이아웃이어야 한다.
- `이미지 섹션 vs HTML 섹션`을 `이미지만 사용 vs 텍스트만 사용`으로 오해하지 않는다.

**최종 반영 후보**:
- `danho-detailpage-coding/SKILL.md`
- `danho-detailpage-coding/references/layout-rules.md`
- `danho-detailpage-coding/references/design-patterns.md`
- `danho-detailpage-coding/references/image-handling.md`
- `danho-detailpage-coding/references/css-examples.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

**반영 방향 초안**:
- 기본 섹션 CSS에서 `aspect-ratio: 9 / 16`을 제거하고, `padding-block` 중심의 자연 높이 구조를 기본값으로 한다.
- 섹션별 콘텐츠 밀도에 따라 이미지 크기, 카드 개수, 말풍선 수, 상하 여백을 조절한다.
- HTML 코딩 섹션에도 SUPPORT 이미지, 제품 컷, 생활 장면 이미지를 적극 배치한다.
- 이모지와 말풍선은 소비자 발화, 사용 상황, 확인 포인트, 구매 전 질문을 빠르게 읽히게 하는 장치로 사용한다.
- 단, 내부 기획 라벨을 그대로 노출하지 않고 실제 소비자가 이해할 수 있는 판매 문구로 바꾼다.

**테스트 적용 메모**:
- 적용 파일: `projects/06041615_magnetic-doorstopper/build/06041615_magnetic-doorstopper-v6-hybrid.html`
- 기존 `panel`, `compact-panel`, `image-section` 중심 구조를 제거하고 `section-block` 자연 높이 구조로 재작성.
- 모든 주요 섹션에 제품/생활/비교 이미지를 결합하고, 말풍선(`bubble`)과 이모지 배지(`eyebrow`, `badge`)를 적극 사용.
- `aspect-ratio` 고정 규칙 제거.

**추가 조정 메모**:
- 고정 비율 제거는 유지하되, 상세페이지 섹션은 가로형/짧은 카드처럼 보이면 안 된다.
- 자연 높이 섹션에도 모바일 기준 충분한 `min-height`와 큰 이미지 영역을 부여해 세로가 긴 상세페이지 리듬을 만든다.
- 이는 `9:16` 같은 정확한 비율 고정이 아니라, 콘텐츠가 적은 섹션도 세로형 인상을 잃지 않게 하는 최소 세로감 확보 규칙이다.

**재설계 메모**:
- 세로형 기준을 적용할 때는 단순히 높이나 비율 수치만 바꾸지 않는다.
- 섹션 구조 자체를 `상단 핵심 카피 → 큰 세로 이미지/장면 → 말풍선/증거/체크 카드` 흐름으로 다시 설계한다.
- 2열 레이아웃을 늘려 세로감을 만드는 방식은 피하고, 상세페이지 본문처럼 한 방향으로 읽히는 스토리보드 구성을 우선한다.
- 적용 파일을 다시 작성하여 `grid-2` 중심 구조를 제거하고, 각 섹션을 세로형 소비 흐름에 맞는 독립 모듈로 재구성했다.

**하이브리드 통 이미지 조정 메모**:
- 최신 36번 규칙 이후에는 절반 구성 같은 고정 비율을 쓰지 않는다. 완성된 디자인 통 이미지 섹션은 필요한 만큼 사용한다.
- 통 이미지 섹션은 이미지 모델이 만든 배경, 타이포, 카드, 아이콘이 포함된 완성 이미지 1장을 `<section>`에 그대로 배치한다.
- HTML 혼합 섹션은 문구 정확도와 수정성이 중요한 조건, 설치, 비교, 가격, FAQ 영역에 우선 적용한다.
- 당시 테스트 적용 기준은 통 이미지 8개 + HTML 혼합 8개였지만, 현재 산출물 기준은 고정 장수가 아니라 승인된 `image-plan.md`의 필요 수량이다.

**컬러 시스템 조정 메모**:
- 상업 상세페이지 HTML 요소에는 많은 색상을 동시에 쓰지 않는다.
- 컬러는 역할 기반 토큰으로 제한한다. 권장 구조는 `Key`(짙은 네이비/본문·다크 배경), `Main`(브랜드/핵심 강조), `Sub`(중립 배경·보조 면), `Exception`(주의·사용 불가 조건)이다.
- 초록, 노랑, 빨강, 보라 같은 accent를 일반 강조에 섞어 쓰지 않는다. 상황성 의미가 있는 경우에만 예외 컬러를 사용한다.
- 말풍선, 배지, 체크 마크는 서로 다른 색으로 구분하지 말고 같은 Main/Sub 계열 안에서 농도와 테두리로 위계를 만든다.
- 테스트 적용: `--green`, `--red` 계열 일반 강조 제거. `--main` 블루와 `--key` 네이비 중심으로 통일하고, `--exception` 앰버는 사용 불가 조건 안내에만 유지.

### 12. 한국 상세페이지 카피 문체 개선

**요청일**: 2026-06-05

**사용자 요청**:
기획 단계 스킬에서 생성되는 한국어 카피가 실제 한국 상세페이지에서 쓰기 어색하다. 예를 들어 "구매 전에는 / 이 조건만 먼저 확인하세요 / 자석이 붙는 문이라면 설치 방식은 간단합니다."는 보고서식 문장에 가깝고, 실제 판매 페이지에서는 "구매전에 꼭 이 부분을 확인해주세요! / 자석이 붙는 문이라면 간단하게 설치할 수 있습니다!"처럼 더 자연스럽고 고객-facing한 표현이 필요하다.

**원인 가설**:
- `danho-detailpage-planning`은 설득 흐름과 섹션 역할은 잘 잡지만, 한국 커머스 문체를 검증하는 별도 규칙이 부족하다.
- 현재 `copy-templates.md`에는 "비밀, 이제 공개합니다", "당신의 ..."처럼 번역투/광고 교본식 표현이 많아 생활용품 상세페이지에 부자연스럽다.
- 헤드라인 마침표 규칙은 있으나, `~하세요`, `~합니다`, `~해주세요`, `~할 수 있습니다`를 어떤 카피 레벨에 써야 하는지 구분하지 않는다.
- 내부 기획 문장과 소비자-facing 문장이 분리되지 않아 "설치 방식은 간단합니다"처럼 설명문을 그대로 헤드라인/서브카피로 올리는 문제가 생긴다.

**개선 방향 초안**:
- 새 참조 문서 `references/korean-commerce-copy-style.md`를 추가한다.
- 기획 스킬의 `Copy Rules`에 "한국 커머스 문체 검수" 단계를 추가한다.
- 섹션별 카피를 `display_copy`와 `planner_note`로 분리한다. `display_copy`는 실제 상세페이지 노출 문장만 허용한다.
- 기본 톤은 친근한 존댓말/권유형으로 둔다. 예: `확인해 주세요`, `사용할 수 있어요`, `걱정 없이 쓰세요`, `간단하게 붙이면 끝`.
- 단, 스펙/정책/FAQ는 정확한 안내형 문체를 유지한다. 예: `사용할 수 없습니다`, `교환이 가능합니다`.
- 헤드라인은 짧고 구어감 있게, 서브카피는 행동/혜택 중심으로 쓴다.
- 기능 설명은 `기능명 → 고객 행동 → 생활 변화` 순서로 고친다.
- "이 조건만 먼저 확인하세요" 같은 명령형은 "구매 전, 이 부분만 확인해 주세요!"처럼 소비자가 실제로 보는 안내 톤으로 변환한다.

**나쁜 예 → 좋은 예**:
- "구매 전에는 / 이 조건만 먼저 확인하세요" → "구매 전, 이 부분만 꼭 확인해 주세요!"
- "자석이 붙는 문이라면 설치 방식은 간단합니다." → "자석이 붙는 문이라면 간단하게 설치할 수 있어요."
- "세 단계면 충분합니다" → "붙이고, 내리고, 바로 고정하세요"
- "떼어낸 뒤가 더 중요합니다" → "나중에 떼어도 자국 걱정을 줄였어요"
- "생활 장면에서 설득됩니다" → "짐 들고 들어올 때, 문이 다시 닫히지 않게"

**반영 후보 파일**:
- `skills/danho-detailpage-planning/SKILL.md`
- `skills/danho-detailpage-planning/references/copy-templates.md`
- `skills/danho-detailpage-planning/references/korean-headline-rules.md`
- `skills/danho-detailpage-planning/references/output-format.md`
- 신규 `skills/danho-detailpage-planning/references/korean-commerce-copy-style.md`

### 13. 이미지 생성 병렬 배치 처리

**요청일**: 2026-06-05

**사용자 요청**:
기획이 끝난 뒤 이미지를 한 장씩 생성하면 너무 오래 걸린다. 이미지 생성 단계는 병렬로 처리할 수 있게 개선한다.

**원인 분석**:
- 현재 `danho-imageprompt-helper` 워크플로우는 "프롬프트 작성 → 이미지 생성"만 적혀 있어 실제 운영에서 한 장씩 순차 처리하는 방식으로 해석될 수 있다.
- 하지만 `image-plan.md`, 프롬프트, 파일명이 확정된 뒤의 섹션 이미지는 대부분 서로 독립적이다.
- 따라서 생성 자체는 병렬 배치로 처리하고, 검수와 재시도만 개별 항목 기준으로 하면 전체 시간이 줄어든다.

**개선 방향**:
- 모든 프롬프트와 저장 파일명을 먼저 확정한다.
- 사용자 승인 후 생성 큐를 만든다.
- 텍스트 없는 `HTML_MIXED` 보조 이미지는 큰 배치로 병렬 생성한다.
- 한글 타이포가 들어가는 `FULL_IMAGE` 섹션은 작은 배치로 병렬 생성하고, 배치마다 한글 오탈자/잘림/랜덤 텍스트를 검수한다.
- 실패한 이미지만 재생성하고, 통과한 이미지는 유지한다.
- `assets/generated/manifest.md`에 `batch`, `queued/generated/accepted/retry/fallback_html` 상태를 기록한다.

**반영 파일**:
- `skills/danho-imageprompt-helper/SKILL.md`
- `skills/danho-imageprompt-helper/references/native-image-generation.md`
- `skills/danho-detailpage-workflow/SKILL.md`
- `PROJECT_STRUCTURE_AI_CONTEXT.md`

### 14. HTML-first 상세페이지 코딩과 모바일 가독성 타이포 강제

**요청일**: 2026-06-06

**사용자 요청**:
플러그인으로 새 상세페이지를 만들었을 때 기본 폰트 사이즈와 디자인 가이드가 지켜지지 않았다. `413px 모바일 사이즈`는 실제 고정 폭이 아니라 모바일에서 잘 보이는 가독성 있는 폰트와 레이아웃을 의미한 것이다. 기획 후 코딩을 진행하니 단순 웹페이지처럼 나오는 문제가 심각하므로, 반드시 HTML 기반으로 상세페이지 레이아웃을 먼저 잡고 이후 디자인 이미지를 생성해 교체하는 방식으로 스킬을 개선해야 한다.

**원인 분석**:
- `danho-detailpage-coding` 스킬에는 "상세페이지처럼 보여야 한다"는 방향은 있으나 구체적인 폰트 사이즈 기준과 모바일 검증 기준이 약했다.
- 기본 `DESIGN.md` 프리셋의 본문 폰트가 `2rem` 등으로 설정되어 있어 모바일 상세페이지 기준보다 과하게 크거나 위계가 불안정해질 수 있었다.
- 빌드 스크립트 기본 CSS도 2열/3열 그리드와 일반 웹 섹션 유틸리티 중심이라, 기획서를 단순 웹페이지로 옮겨도 실패로 잡히지 않았다.
- 이미지 생성은 HTML 레이아웃 이후에 와야 하는데, 스킬 규칙이 이 순서를 충분히 강제하지 않았다.

**반영 내용**:
- `references/detailpage-typography.md` 추가: 모바일 가독성 기준 폰트 스케일, line-height, spacing 정의.
- `references/html-first-detailpage-build.md` 추가: `HTML 상세페이지 레이아웃 → image-plan → 이미지 생성 → FULL_IMAGE 교체` 순서 강제.
- `danho-detailpage-coding/SKILL.md`에 HTML-first, 모바일 가독성, 단순 웹페이지 금지 규칙 추가.
- `danho-detailpage-workflow/SKILL.md`에 기획 직후 이미지 생성 금지, Phase A HTML 상세페이지 레이아웃 선행 규칙 추가.
- `build.py` 기본 CSS의 본문/헤드라인/카드/가격 폰트 fallback을 상세페이지용 `clamp()` 스케일로 변경.
- 6개 DESIGN.md 프리셋의 타이포 토큰을 모바일 가독성 기준으로 변경.
- `output-checklist.md`, `layout-rules.md`, `mobile-hybrid-layout.md`, `image-handling.md` 검증 항목 보강.

### 15. 사용자 제공 제품 이미지의 레퍼런스 기반 생성 규칙

**요청일**: 2026-06-07

**사용자 요청**:
제품 이미지 생성 시 사용자가 제공한 이미지가 있으면 해당 이미지를 레퍼런스로 삼아 제품 일관성을 유지한 채 새 이미지를 생성해야 한다. 테스트 중에는 사용자의 이미지만 그대로 사용하는 경우가 있었으므로, 스킬이 제대로 설계되어 있는지 확인하고 개선해야 한다.

**원인 분석**:
- `danho-imageprompt-helper`에는 `Existing assets, if any` 정도만 있어 사용자 이미지를 직접 사용 이미지와 생성 레퍼런스로 구분하지 못했다.
- legacy API 스크립트에는 reference image 처리 기능이 있지만, Codex native image generation 문서에는 레퍼런스 이미지 사용 규칙이 빠져 있었다.
- `image-plan.md`에 reference assets/source mode 컬럼이 없어 원본 이미지 직접 사용과 레퍼런스 기반 생성이 구분되지 않았다.

**반영 내용**:
- `skills/danho-imageprompt-helper/references/product-reference-images.md` 추가.
- 사용자 제공 제품 이미지는 기본적으로 `PRODUCT_REFERENCE`로 취급한다.
- `USER_IMAGE_DIRECT`로 명시된 경우에만 `assets/inbox/` 원본 이미지를 최종 HTML에 직접 사용할 수 있다.
- 제품/라이프스타일 생성 이미지는 `assets/inbox/` 제품 이미지를 reference input으로 사용하고 `assets/generated/`에 새 결과를 저장한다.
- 프롬프트에 제품 silhouette, proportions, material, color, finish, distinctive details 보존 규칙을 포함한다.
- `image-plan.md` 템플릿에 `reference assets`, `source mode` 컬럼을 추가한다.
- 최종 검증에서 `assets/inbox/` 직접 사용 여부와 제품 일관성 보존 여부를 확인한다.

### 16. 배포 파일 생성 정책과 설치 스크립트 제거

**요청일**: 2026-06-07

**사용자 요청**:
배포판은 사용자가 명시적으로 요청할 때만 만든다. 설치 스크립트는 쓸모 없으므로 배포 패키지에서 제거한다.

**반영 내용**:
- `packaging/install.ps1` 삭제.
- `packaging/install.sh` 삭제.
- `packaging/README_INSTALL.md`를 수동 설치 안내만 남기도록 정리.
- 기존 `dist/danho-detailpage-maker-codex-0.1.0.zip`에서 설치 스크립트를 제거하고 `README_INSTALL.md`만 남긴 형태로 갱신.

**운영 규칙**:
- 스킬 수정, 문서 수정, 코드 수정만으로는 배포 zip을 자동 재생성하지 않는다.
- 사용자가 "배포 파일 만들어줘", "zip 만들어줘", "배포판 갱신해줘"처럼 명시했을 때만 `dist/` 패키지를 생성 또는 갱신한다.

### 17. 기획 후 카피라이터 검수 루틴 추가

**요청일**: 2026-06-09

**사용자 요청**:
기획 단계에서 생성되는 카피가 자연스러운 한국어가 아니라 AI-slop처럼 보인다. 기획 후 자연스러운 한국어와 소비자 심리학이 반영된 카피인지 재검토하고 개선하는 루틴을 추가해야 한다. 제품의 메리트를 강조하는 언어가 아니라 소비자가 얻는 베네핏을 강조해야 하며, 로버트 치알디니의 설득의 심리학과 도널드 밀러의 무기가 되는 스토리의 원칙을 참고해 카피라이팅하도록 개선한다.

**원인 분석**:
- `danho-detailpage-planning`이 설득 흐름과 섹션 역할은 만들지만, 노출 카피만 별도로 검수하는 단계가 없었다.
- 기존 `copy-templates.md`에 "비밀 공개", "단 하나의", "당신의 ... 바꿔줄", "수많은 분들이 선택한 이유"처럼 한국 상세페이지에서 어색하거나 근거 없는 표현을 유도하는 템플릿이 있었다.
- 제품 기능/메리트를 고객 상황과 베네핏으로 변환하는 명시적 루틴이 없었다.
- 치알디니식 설득 원칙을 실제 근거 없이 쓰면 가짜 후기, 가짜 희소성, 가짜 권위로 흐를 수 있으므로 윤리적 사용 제한이 필요했다.

**반영 내용**:
- 신규 스킬 `skills/danho-detailpage-copywriter/` 추가.
- 기획 후 `COPY_REVIEW.md`를 만들고, `PLANNING.md`의 visible copy를 패치한 뒤 코딩하도록 `danho-detailpage-workflow` 순서를 변경.
- `danho-detailpage-planning`에서 계획 카피를 초안으로 취급하고, `danho-detailpage-copywriter` 검수를 통과한 카피만 코딩 단계로 넘기도록 규칙 추가.
- 신규 참조 문서:
  - `consumer-benefit-copy.md`: 기능/메리트 -> 소비자 걱정 -> 일상 장면 -> 베네핏 -> 근거 변환
  - `persuasion-storybrand-check.md`: 치알디니 원칙의 윤리적 적용, 고객을 주인공으로 두는 StoryBrand식 여정 체크
  - `copy-review-format.md`: `COPY_REVIEW.md` 산출물 형식
- `copy-templates.md`의 어색한 훅/전환/브랜드 문구를 소비자 상황과 베네핏 중심 문장으로 교체.

**운영 규칙**:
- 신규 상세페이지 제작은 `planning -> copywriter review -> coding phase A` 순서를 따른다.
- 고객이 실제로 얻는 변화가 문장 앞에 와야 하며, 제품 기능은 그 변화를 가능하게 하는 근거로 배치한다.
- 사회적 증거, 권위, 희소성은 실제 자료가 있을 때만 사용한다.
- 카피가 한국 고객에게 자연스럽게 말로 전달되지 않으면 코딩 전에 다시 쓴다.

### 18. 한국어 화용론 기반 카피 문맥 추론 강화

**요청일**: 2026-06-09

**사용자 요청**:
첨부 조사 자료를 바탕으로 카피라이터 스킬을 더 개선한다. 한국어 표현이 여전히 어색하므로, 단순히 사용자에게 묻기보다 상품 기획에 알맞은 정보들을 알아서 채운 뒤 재검토하고 수정하는 방향이 필요하다.

**원인 분석**:
- "자연스러운 한국어"라는 지시만으로는 화자/청자/관계/매체/말높임/톤이 고정되지 않아 모델이 무난한 번역투나 보고서식 문장으로 되돌아갈 수 있다.
- 기존 카피라이터 스킬은 소비자 베네핏과 윤리적 설득은 다뤘지만, 한국어 화용론 관점의 문맥 추론과 높임말 일관성 검수가 약했다.
- 기획 단계에서 타겟/톤이 누락되면 바로 질문하거나 모호한 기본값을 쓰는 문제가 있어, 상품 카테고리와 구매 상황에서 합리적 기본값을 추론하는 루틴이 필요했다.

**반영 내용**:
- `danho-detailpage-copywriter/SKILL.md`에 `Autonomous Context Inference` 추가.
- 카피라이터 워크플로우를 `카피 문맥 추론 -> visible copy 추출 -> 베네핏 패스 -> 한국어 에디터 패스 -> 윤리적 설득 패스 -> PLANNING.md 패치`로 변경.
- 신규 참조 문서 `korean-pragmatic-style.md` 추가:
  - 화자/청자/관계/매체/말높임/톤 기본값
  - 번역투, 과한 수동태, 과한 명사화, 명사구 나열, 높임말 혼용 제거 규칙
  - few-shot 한국어 before/after 예시
- `COPY_REVIEW.md` 형식에 `Copy Context`, `Assumption Log`, `Korean Naturalness Audit` 추가.
- `PLANNING.md` 출력 형식에 `카피 문맥`, `추론 메모` 섹션 추가.
- `danho-detailpage-planning`에서 비핵심 카피 문맥은 묻지 말고 추론하며, 사실 정확도에 필요한 정보만 질문하도록 수정.

**운영 규칙**:
- 신규 기획은 상품명/가격/구성/호환/법적 주장 같은 사실 블로커가 아니면 멈춰서 묻지 않는다.
- 카피라이터는 상품 카테고리와 구매 상황을 바탕으로 화자, 청자, 관계, 매체, 말높임, 톤을 먼저 정한다.
- 최종 카피는 한국어 원어민 편집자가 손본 문장처럼 번역투, 명사화, 높임말 혼용을 제거한 뒤 PLANNING.md에 반영한다.

### 19. 이미지 생성 레거시/API fallback 제거

**요청일**: 2026-06-09

**사용자 요청**:
이미지 생성 시 스킬이 자꾸 직접 이미지를 그려보거나 API를 사용하려고 한다. 이미지 생성은 Codex 자체 이미지 생성 모델(gpt-image-2)을 사용해 네이티브로 처리해야 하므로, 이미지 생성 스킬에 남은 레거시를 점검하고 수정한다.

**원인 분석**:
- `danho-imageprompt-helper`에 `Legacy Fallback` 섹션이 남아 있어 사용자가 명시하면 API 스크립트를 써도 되는 것처럼 해석될 수 있었다.
- `scripts/generate_banner.py`가 스킬 폴더에 남아 있어 Codex가 로컬 API 생성 경로를 후보로 볼 수 있었다.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`에도 `generate_banner.py`와 API fallback 설명이 남아 있어 AI 파싱 시 레거시 경로가 다시 살아날 수 있었다.
- HTML 렌더 캡처, SVG/canvas/PIL 드로잉, placeholder 이미지를 생성 이미지 대체물로 쓰지 말라는 금지 규칙이 충분히 강하지 않았다.

**반영 내용**:
- `skills/danho-imageprompt-helper/scripts/generate_banner.py` 삭제.
- `danho-imageprompt-helper/SKILL.md`에서 API fallback 섹션 제거 및 `Hard Prohibitions` 추가.
- `native-image-generation.md`를 Codex 네이티브 이미지 생성 전용 문서로 수정.
- `danho-detailpage-workflow/SKILL.md`에서 legacy API fallback 허용 문구 제거.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`에서 `generate_banner.py` 항목과 API fallback 설명 제거.
- `image-plan-template.md`에서 이전 역할명 매핑을 제거하고 `FULL_IMAGE`, `HTML_MIXED`, `HTML_ONLY`만 사용하도록 정리.

**운영 규칙**:
- 이미지 생성은 Codex 네이티브 이미지 생성 기능만 사용한다.
- `OPENAI_API_KEY`, curl, 직접 OpenAI API 호출, 로컬 생성 스크립트는 사용하지 않는다.
- 브라우저 렌더 캡처, HTML/CSS/SVG/canvas/PIL 드로잉, placeholder는 생성 이미지 대체물이 아니다.
- 네이티브 이미지 생성 기능을 사용할 수 없으면 API로 우회하지 말고, 프롬프트 준비 상태와 차단 사유를 보고한다.

### 20. 소비자 주어 기반 카피라이팅 강화

**요청일**: 2026-06-10

**사용자 요청**:
같은 말이라도 카피라이트는 소비자의 시각에서 쓰여야 한다. 개선된 카피라이터 스킬 결과가 여전히 판매자 시각이고, 주어가 판매자가 아닌 소비자여야 한다. 도널드 밀러의 브랜드 스토리 프레임워크 법칙을 참조해 스킬을 개선한다.

**원인 분석**:
- 기존 스킬에는 "customer is hero" 원칙이 있었지만, 문장 단위에서 실제 주어/시점이 소비자인지 검사하는 단계가 부족했다.
- `제품은 제공합니다`, `저희는 만들었습니다`, `브랜드가 해결합니다`처럼 판매자/제품 중심 문장이 베네핏 문장처럼 보이지만 실제로는 판매자 관점으로 남을 수 있었다.
- StoryBrand식으로는 고객이 주인공이고 브랜드/제품은 가이드 또는 도구여야 하므로, 카피 문장의 중심도 소비자의 상황/행동/걱정/결과가 되어야 한다.

**반영 내용**:
- `danho-detailpage-copywriter/SKILL.md`에 `Perspective pass` 추가.
- `consumer-benefit-copy.md`에 `Perspective Rule`과 판매자 중심 -> 소비자 중심 변환 예시 추가.
- `persuasion-storybrand-check.md`에 `Customer-As-Subject Rule` 추가.
- `COPY_REVIEW.md` 형식에 `buyer-centered subject` 검수 항목 추가.
- `danho-detailpage-planning`과 `danho-detailpage-workflow`에 buyer-centered visible copy 규칙 추가.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`에 `buyer_as_subject_brand_as_guide` 원칙 추가.

**운영 규칙**:
- 판매 카피의 의미상 주어는 소비자의 상황, 행동, 걱정, 생활 루틴, 원하는 결과여야 한다.
- 판매자/브랜드/제품은 스펙, 호환, 안전, 증거 같은 사실 안내에서만 주어로 허용한다.
- `개발했습니다`, `제공합니다`, `담았습니다`, `설계했습니다` 같은 판매자 성취 문장은 소비자의 결과 문장으로 바꾼다.

### 21. 모바일 스캔 이해도 기반 상세페이지 기획·카피 점수 게이트

**요청일**: 2026-06-10

**사용자 요청**:
한국 소비자가 상세페이지를 가볍게 훑고 `이것이 무엇인지`, `나에게 어떤 베네핏이 있는지`, `구매하려면 어떻게 해야 하는지`를 빠르게 이해해야 한다. 리서치 기반으로 상세페이지 기획과 한국어 표현을 전반적으로 개선하고, 테스트 상세페이지를 만들어 섹션별 평가 점수가 개선될 때까지 스킬을 개선한다.

**원인 분석**:
- 기존 기획/카피 스킬은 자연스러운 한국어, 소비자 베네핏, 소비자 주어 원칙을 갖고 있었지만 점수 기반 통과 기준이 없었다.
- `COPY_REVIEW.md`가 있어도 섹션별로 무엇이 실패했고 몇 점까지 개선됐는지 추적하기 어려웠다.
- 모바일 쇼핑 사용자는 정독 전에 훑어보므로 초반 1-2줄과 첫 3개 섹션에서 제품 정체, 핵심 베네핏, 구매 조건을 바로 답해야 한다.

**반영 내용**:
- `danho-detailpage-planning`에 3초 모바일 스캔 설계를 추가했다.
- `PLANNING.md` 출력 형식에 `3초 스캔 설계`와 섹션별 `스캔 답변` 컬럼을 추가했다.
- `danho-detailpage-copywriter`에 섹션별 점수표, 페이지 수준 구매 이해도, 재작성 루프, 최종 통과 사유를 필수화했다.
- 신규 참조 문서 `mobile-scan-purchase-audit.md`와 `korean-commerce-expression-bank.md`를 추가했다.
- `consumer-benefit-copy.md`와 `copy-templates.md`를 보강해 첫 줄 베네핏, 자연스러운 한국 커머스 표현, 가짜 후기/권위/희소성 금지를 강화했다.
- 테스트 프로젝트 `projects/0610_skill-copy-audit-doorstopper/`에 `PLANNING.md`, `COPY_REVIEW.md`, `SKILL_TEST_REPORT.md`를 생성했다.

**운영 규칙**:
- 신규 기획은 첫 3개 섹션 안에서 제품 정체, 핵심 베네핏, 구매 전 확인 조건을 답해야 한다.
- `COPY_REVIEW.md`는 섹션 평균 8점 이상, 핵심 항목 7점 이상, 페이지 수준 정체/베네핏/구매 행동 이해도 각각 8점 이상을 통과해야 한다.
- 통과 전에는 HTML 코딩 단계로 넘어가지 않는다.
- 스킬 개선 검증 시 기본 테스트 상품은 `무타공 자석 도어스토퍼`로 두고, `SKILL_TEST_REPORT.md`에 개선 전 위험과 개선 후 점수를 기록한다.

### 22. 와디즈식 공감 설득 프롬프트 분석 반영

**요청일**: 2026-06-10

**사용자 요청**:
이전 중식도 테스트 기획이 구매욕구를 만들지 못해 형편없었다. 사용자가 예전에 쓰던 와디즈 스타일 상세페이지 기획 프롬프트를 분석해, 소비자가 구매하고 싶어지는 상세페이지 기획 스킬로 개선한다. 와디즈 스타일은 기본적으로 공감 설득에 강하므로 이를 반영한다.

**원인 분석**:
- 기존 스킬은 모바일 이해도와 카피 자연스러움은 점수화했지만, 구매욕구를 만드는 긴 빌드업이 약했다.
- 첨부 프롬프트의 강점은 `생생한 문제 공감 -> 기존 방식의 한계 -> 탄생/진정성 -> 핵심 솔루션 -> 기능별 문제/해결/이득 -> 특장점 -> 신뢰 -> 스펙/사용법 -> 추천 대상 -> Q&A -> CTA`의 감정-논리 복합 흐름이다.
- 현재 테스트 기획은 정보가 명확해도 "왜 지금 사고 싶어지는가"가 약할 수 있었다.

**반영 내용**:
- 신규 참조 문서 `skills/danho-detailpage-planning/references/wadiz-empathy-conversion-flow.md` 추가.
- `danho-detailpage-planning/SKILL.md`에 `Draft Planning`/`Final Planning` 모드와 와디즈식 공감 전환 맵 작성 단계를 추가.
- `output-format.md`에 `공감 설득 맵`, `핵심 베네핏 모듈`, 섹션별 `비주얼 역할`, `증거/자료 필요 로그`를 추가.
- `detail-flow-rules.md`에 와디즈식 공감 흐름을 추가하고, 기존 방식의 한계와 탄생/진정성 섹션을 안전하게 다루는 규칙을 추가.
- `mobile-scan-purchase-audit.md`와 `copy-review-format.md`에 `empathy_depth`, `purchase_desire` 평가 항목을 추가.
- `danho-detailpage-copywriter/SKILL.md`와 `danho-detailpage-workflow/SKILL.md`에 공감 깊이와 구매 욕구 점수 게이트를 추가.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`를 `v7_empathy_conversion_scored_detail` 흐름으로 갱신.

**운영 규칙**:
- 공감 설득이 중요한 상품은 단순 기능 나열로 시작하지 않는다.
- 구매욕구는 생생한 문제 장면과 기존 해결 방식의 불만족을 먼저 만든 뒤 제품을 해결책으로 제시한다.
- 최소 3개 핵심 베네핏 모듈을 `고객 장면 -> 불편/감정 -> 제품 메커니즘 -> 고객 변화 -> 증거/제한 -> 비주얼 역할`로 설계한다.
- 신뢰 근거가 없으면 후기, 인증, 수상, 전문가 권위, 희소성, 수치 claim을 만들지 말고 `NEEDS_PROOF` 또는 안전한 표현으로 처리한다.
- 와디즈식 공감 페이지는 문제/해결/베네핏/CTA 섹션의 공감 깊이와 구매 욕구 점수가 각각 8점 이상이어야 한다.

### 23. 제공 기획 문장 보존 금지와 소스 브리프 정규화

**요청일**: 2026-06-10

**사용자 요청**:
제품 기획이 있다고 해서 그 문장을 그대로 따르지 말고, 기획 스킬과 카피라이터 스킬이 소비자가 구매하고 싶어지는 상세페이지 카피로 다시 만들어야 한다. `요리 좀 해보고 싶은 남자에게, 첫 칼은 중식도면 충분합니다`, `의외로 칼부터 답답합니다`, `"요리 장비"처럼 느껴지지 않았던 걸지도 모릅니다`, `일반 식도는 익숙합니다`, `칼 하나가 아닙니다` 같은 어색한 표현이 다시 통과되면 안 된다.

**원인 분석**:
- 기존 산출물은 사용자가 제공한 제품 기획을 전략 브리프가 아니라 visible copy 후보처럼 취급했다.
- `COPY_REVIEW.md`의 점수표가 자연스러움은 평가했지만, 소스 문장을 그대로 보존했는지 별도 점수로 잡지 못했다.
- 기획의 핵심 전략인 남성 타겟, 장비 욕구, 세트 가치, 가격 방어는 살려야 하지만, 소스 문장 구조와 슬로건은 한국 소비자용 카피로 새로 써야 한다.

**반영 내용**:
- `skills/danho-detailpage-planning/references/source-brief-normalization.md` 추가.
- `danho-detailpage-planning/SKILL.md`에 소스 브리프 정규화 단계를 추가하고, 제공 기획의 문장을 visible copy에 그대로 쓰지 않도록 규칙화.
- `PLANNING.md` 출력 형식에 `소스 브리프 정규화` 표를 추가.
- `danho-detailpage-copywriter/SKILL.md`에 source normalization pass, source-copy overpreservation 진단, source_independence 점수 게이트 추가.
- `copy-review-format.md`에 `Source Phrase Audit`과 `source_independence` 컬럼 추가.
- `mobile-scan-purchase-audit.md`에 source_independence 루브릭과 pass/fail 기준 추가.
- `korean-commerce-expression-bank.md`에 소스 브리프 문장 -> 구매자 카피 변환 예시 추가.
- `danho-detailpage-workflow/SKILL.md`와 `PROJECT_STRUCTURE_AI_CONTEXT.md`에 소스 문장 보존 금지와 코딩 전 차단 규칙 추가.
- 테스트 프로젝트 `projects/0610_mens-cleaver-starter-set/`의 `PLANNING.md`, `COPY_REVIEW.md`, `SKILL_TEST_REPORT.md`를 새 기준으로 재작성.

**운영 규칙**:
- 사용자가 제공한 제품 기획, 프롬프트, 메모, 초안 카피는 `fixed fact`, `strategy`, `evidence`, `draft copy`, `visual direction`, `risk`로 먼저 분리한다.
- `draft copy`와 전략 라벨은 exact phrase로 visible copy에 들어가면 실패다.
- `COPY_REVIEW.md`는 소스 기획이 있을 때 반드시 `Source Phrase Audit`을 포함해야 한다.
- 소스 기획이 있는 신규 페이지는 모든 섹션의 `source_independence` 점수가 8점 이상이어야 한다.
- 소스 문장이 어색하다는 사용자 피드백이 나오면 그 문장만 고치지 말고, 같은 패턴이 전체 페이지에 남아 있는지 검색하고 전부 재작성한다.

### 24. 한국어 상세페이지 표현 폴리싱 게이트 추가

**요청일**: 2026-06-10

**사용자 요청**:
어색한 한국어 표현의 교정본을 첨부했다. `고기 썰고, 파 다지고, 마늘 으깨는 요리부터`, `도구가 체감됩니다`, `묵직한 실루엣`, `리듬 있게 손질`, `본품`, `관리 구성`, `최종 상품 스펙`, `제공 이미지`, `추가 확인 필요`처럼 의미는 통하지만 한국 상세페이지 말투로는 어색한 표현을 분석해 스킬을 개선한다.

**원인 분석**:
- 기존 `korean_naturalness` 점수는 너무 넓어서, 의미가 통하는 문장을 높은 점수로 통과시킬 위험이 있었다.
- 한국어 광고 카피에서는 헤드라인이 짧더라도 완결감이 있어야 하는데, `~요리부터`처럼 끊긴 표현이 통과됐다.
- `체감됩니다`, `느껴집니다`가 잘못된 명사 주어와 결합해 번역체/AI 작성 티를 만들었다.
- `본품`, `관리 구성`, `스펙`, `강재` 같은 사양서/내부어가 소비자용 카피에 섞였다.
- 가격 69,000원이 여러 곳에 반복되어 오히려 비싸다는 인식을 만들 수 있었다.
- 안전 면책과 제작 메모가 FAQ/본문에 섞이며 구매 불안을 키웠다.

**반영 내용**:
- 신규 참조 문서 `skills/danho-detailpage-copywriter/references/korean-copy-polish-rules.md` 추가.
- `danho-detailpage-copywriter/SKILL.md`에 Korean polish pass와 `expression_polish` 점수 게이트 추가.
- `copy-review-format.md`에 `Expression Polish Audit`과 `expression_polish` 컬럼 추가.
- `mobile-scan-purchase-audit.md`에 expression polish 루브릭과 통과 기준 추가.
- `korean-commerce-expression-bank.md`와 `korean-pragmatic-style.md`에 교정본 기반 before/after 예시 추가.
- `danho-detailpage-planning/SKILL.md`와 `output-format.md`에 제작 메모/visible copy 분리, 가격 반복 제한, 안전 문구 통합 규칙 추가.
- `danho-detailpage-workflow/SKILL.md`와 `PROJECT_STRUCTURE_AI_CONTEXT.md`에 expression polish 감사가 없으면 코딩 금지 규칙 추가.
- 테스트 프로젝트 `projects/0610_mens-cleaver-starter-set/`의 `PLANNING.md`, `COPY_REVIEW.md`, `SKILL_TEST_REPORT.md`를 expression polish 기준으로 재작성.

**운영 규칙**:
- 신규 상세페이지는 `korean_naturalness`와 별도로 `expression_polish`를 점수화한다.
- 미완성 헤드라인, 잘못된 `체감/느껴짐` 결합, 사양서/내부 용어, 제작 메모, 과도한 가격/안전 문구 반복이 남으면 revise다.
- 가격은 핵심 구매 판단 지점 2-3곳에만 배치한다.
- 안전 면책은 한 섹션에 차분하게 모으고, FAQ에서는 불안을 키우는 방어적 문장을 피한다.
- 제작용 메모는 기획 메모나 증거/자료 필요 로그로 분리하고, 소비자용 본문/FAQ/CTA에 섞지 않는다.

### 25. 상세페이지 직접 가격 표기 금지

**요청일**: 2026-06-11

**사용자 요청**:
상세페이지에서는 직접적인 가격을 표기하지 않는 규칙을 추가한다. 프로모션, 쿠폰, 채널별 할인으로 가격이 바뀔 수 있는데 상세페이지 이미지나 HTML에 가격이 디자인되어 있으면 매번 수정하기 어렵다.

**원인 분석**:
- 기존 규칙은 가격 과노출을 줄이는 수준이었고, hero/가격 근거/CTA에 2-3회 가격을 허용했다.
- 실제 운영에서는 가격이 프로모션에 따라 바뀌므로, 숫자 가격이 이미지/HTML/CTA에 박히면 유지보수 리스크가 크다.
- 상세페이지는 구성 가치와 구매 이유를 설득하고, 현재 판매가는 구매 페이지/옵션 영역에서 확인시키는 편이 운영상 안전하다.

**반영 내용**:
- `danho-detailpage-planning/SKILL.md`와 `output-format.md`에 visible copy 직접 가격 표기 금지 규칙 추가.
- `danho-detailpage-copywriter/SKILL.md`, `korean-copy-polish-rules.md`, `mobile-scan-purchase-audit.md`, `copy-review-format.md`에 직접 가격 표기 fail 조건 추가.
- `danho-detailpage-workflow/SKILL.md`에 숫자 가격이 남아 있으면 코딩 금지 규칙 추가.
- `danho-detailpage-coding` 참조 문서의 `price panel` 개념을 `current-price guidance panel`로 변경.
- `danho-imageprompt-helper`에 생성 이미지 안 직접 가격 금지 규칙 추가.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`에 내부 가격 정보와 visible copy 가격 표기 금지 원칙 반영.
- 테스트 프로젝트 `projects/0610_mens-cleaver-starter-set/`의 visible copy에서 `69,000원`을 제거하고 현재 판매가/프로모션은 구매 채널에서 확인하도록 변경.

**운영 규칙**:
- 숫자 가격은 `기본 정보`, `config.json`, 내부 기획 메모, proof log에는 보관할 수 있다.
- 숫자 가격은 상세페이지 visible copy, CTA, 비교표, HTML 섹션, 생성 이미지 텍스트에 넣지 않는다.
- 가격 관련 구매 행동은 `현재 판매가는 구매 페이지에서 확인해 주세요`, `프로모션과 옵션은 구매 페이지에서 확인해 주세요`, `세트 구성과 혜택을 구매 페이지에서 확인해 주세요`처럼 안내한다.
- 사용자가 명시적으로 가격 노출을 요구하지 않는 한, 직접 가격 표기는 실패로 처리한다.

### 26. 상세페이지 마이크로 폴리싱 게이트 추가

**요청일**: 2026-06-11

**사용자 요청**:
수정본은 전반적으로 자연스러워졌지만, CTA cue 두 개가 모두 `보기`로 끝나는 문제, 문제 카드 리듬 불일치, `손질/다듬기` 용어 혼용, 비교표/사용 라벨의 미세한 어긋남, FAQ의 동문서답, 마지막 정적 CTA cue 누락 가능성처럼 전환에 영향을 주는 미세 표현을 스킬에 반영한다.

**원인 분석**:
- 기존 표현 폴리싱은 비문, 번역투, 내부어, 가격, 제작 메모 같은 큰 문제를 잘 잡았지만, 같은 페이지 안의 리듬과 용어 일관성은 별도 실패 조건으로 강제하지 않았다.
- CTA는 문장 자체가 자연스러워도 두 정적 cue의 행동이 같아 보이면 구매자가 다음 행동을 구분하기 어렵다.
- FAQ는 문체가 자연스러워도 질문에 먼저 답하지 않으면 구매 불안을 해소하지 못한다.
- 병렬 카드, 짧은 사용 라벨, 비교표 문장은 모바일에서 훑을 때 리듬이 깨지면 AI 작성 티가 나고 이해 속도가 떨어진다.

**반영 내용**:
- `korean-copy-polish-rules.md`에 Micro-Polish Gate를 추가했다.
- `danho-detailpage-copywriter/SKILL.md`에 CTA-action duplication, inconsistent action vocabulary, list rhythm breaks, FAQ non-answers, missing final static CTA cue 진단과 실패 조건을 추가했다.
- `copy-review-format.md`의 Expression Polish Audit과 Final Checks에 CTA 동작 구분, 행동 용어 일관성, 병렬 리듬, FAQ 직접 답변, final CTA cue 존재를 추가했다.
- `mobile-scan-purchase-audit.md`의 expression_polish 루브릭에 위 항목들을 포함했다.
- `danho-detailpage-planning/SKILL.md`와 `output-format.md`에 초안 작성 단계에서 CTA/용어/리듬/FAQ/final CTA를 먼저 정리하도록 규칙화했다.
- `danho-detailpage-workflow/SKILL.md`와 `PROJECT_STRUCTURE_AI_CONTEXT.md`에 해당 문제가 남으면 코딩 금지 규칙을 추가했다.
- 테스트 프로젝트 `projects/0610_mens-cleaver-starter-set/`의 `PLANNING.md`, `COPY_REVIEW.md`, `SKILL_TEST_REPORT.md`에 이번 미세 교정 내용을 반영했다.

**운영 규칙**:
- CTA 두 개가 나란히 있을 때는 같은 일반 동사로 끝내지 않고 서로 다른 행동을 맡긴다.
- 같은 행동은 같은 용어로 부른다. 예: 한 페이지 안에서 같은 조리 동작을 `손질`과 `다듬기`로 흔들지 않는다.
- 병렬 카드와 짧은 사용 라벨은 어미, 길이, 호흡을 맞춘다.
- FAQ는 질문에 먼저 답한 뒤 조건이나 확인 안내를 덧붙인다.
- 마지막 CTA 섹션은 헤드라인/본문만 두지 않고 정적 CTA cue 또는 옵션/구성 확인 cue를 포함한다.

### 27. 전환 욕망 설계와 증거 비주얼 게이트 추가

**요청일**: 2026-06-11

**사용자 요청**:
첨부된 상세페이지 기획 피드백을 분석해 스킬을 개선한다. 샘플은 특정 상품이지만, 스킬이 특정 상품 맞춤형이 되면 안 되므로 메타적으로 반영한다.

**원인 분석**:
- 이전 개선은 한국어 자연스러움, 소스 문구 독립성, CTA/FAQ/리듬 같은 표현 품질을 크게 올렸지만, 자연스러운 문장이 곧 전환력 있는 문장은 아니었다.
- 기능과 사용 장면을 반복해도 구매자가 얻고 싶은 after 상태, 자기 인식, 욕망이 잡히지 않으면 카피가 일을 하지 않는다.
- 가격 직접 표기 금지 규칙은 유지해야 하지만, `구매 페이지에서 확인`만 반복하면 가치 설득이 비어 보일 수 있다.
- 정직한 유보 표현이 여러 섹션에 흩어지면 신뢰보다 불안을 만들 수 있다.
- 전환이 중요한 섹션은 제품 단독 컷보다 before/after, 사용 시연, 메커니즘, 가치 구성, 신뢰 증거 비주얼이 필요하다.

**반영 내용**:
- `skills/danho-detailpage-planning/references/conversion-desire-architecture.md`를 추가했다.
- `danho-detailpage-planning/SKILL.md`에 전환 욕망 설계 단계, before/after, target desire, 가치 확신, caveat 배치, 증거 비주얼 계획 규칙을 추가했다.
- `PLANNING.md` 출력 형식에 `전환 욕망 설계`와 `비주얼 증거 설계` 표를 추가했다.
- `wadiz-empathy-conversion-flow.md`에 Conversion Desire Layer, confidence/caveat placement, demonstration visual 기준을 추가했다.
- `danho-detailpage-copywriter/SKILL.md`에 polite-but-powerless copy, timid value framing, scattered caveats, decorative-only visual planning 진단을 추가하고 `conversion_force` 점수 게이트를 만들었다.
- `mobile-scan-purchase-audit.md`와 `copy-review-format.md`에 `conversion_force` 컬럼과 Conversion Architecture Audit을 추가했다.
- `danho-detailpage-workflow/SKILL.md`와 `PROJECT_STRUCTURE_AI_CONTEXT.md`에 전환 욕망 설계와 conversion_force 미달 시 코딩 금지 규칙을 추가했다.

**운영 규칙**:
- 기획은 타겟의 인구통계가 아니라 `상황`, `벗어나고 싶은 before`, `얻고 싶은 after`, `되고 싶은 자기 인식`부터 잡는다.
- 핵심 판매 섹션은 자연스러운 표현만으로 통과하지 않는다. before/after, self-identification, 가치 확신, 증거 비주얼, 다음 행동 중 하나를 밀어야 한다.
- 문제는 구매자의 능력 부족이 아니라 현재 도구, 환경, 습관, 정보 부족, 대안의 한계로 프레이밍한다.
- 직접 숫자 가격은 계속 금지한다. 대신 포함 가치, 추가 구매 회피, 번거로움 감소, 대안 대비 이점으로 가치 확신을 만든다.
- 유보와 주의 문구는 스펙, 안전/관리, 호환성, FAQ에 모으고 판매 섹션에는 사실 안에서 자신감 있게 쓴다.
- 핵심 문제와 해결은 가능하면 제품 단독 이미지가 아니라 before/after, 사용 시연, 메커니즘, 구성 가치, 신뢰 증거 비주얼로 설계한다.

### 28. 한국어 우선 사고와 발화 검수 게이트 추가

**요청일**: 2026-06-11

**사용자 요청**:
여전히 한국어 표현이 엉망이다. 원인은 영어권 마케팅 프레임을 한국어로 직역하는 사고 구조에 있으므로, 전략 언어와 표현 언어를 분리하고 한국 소비자 입말 중심으로 스킬을 근본 개선한다.

**원인 분석**:
- `before/after`, `value stack`, `mechanism`, `self-image`, `friction reduction` 같은 영어권 전략 개념이 사고 도구로 끝나지 않고 visible copy에 직역되어 들어갔다.
- 어휘 교체만으로는 해결되지 않았다. `도마 위 동선을 줄이고`, `첫 구매의 선택을 줄였습니다`처럼 문장의 골격 자체가 영어식이었다.
- `단정한`, `실용적인`, `자신감 있는` 같은 추상 톤 지시는 모델을 무난한 번역체 평균값으로 밀어 넣었다.
- 생성과 검수가 한 흐름에 붙어 있어 문장별 발화 가능성을 따로 거르는 관문이 부족했다.

**반영 내용**:
- `skills/danho-detailpage-copywriter/references/korean-first-expression-gate.md`를 추가했다.
- `danho-detailpage-planning/SKILL.md`에 고객 입말 전략, 톤 좌표, spoken Korean gate를 추가했다.
- `output-format.md`에 `고객 입말 전략`, `톤 좌표`, `노출 카피 문장 검수 로그`를 추가했다.
- `danho-detailpage-copywriter/SKILL.md`에 Korean-first strategy pass, Korean sentence skeleton pass, Spoken Korean gate를 추가했다.
- `mobile-scan-purchase-audit.md`에 `spoken_korean_gate` 점수 기준을 추가했다.
- `copy-review-format.md`에 `Korean-First Expression Audit`과 `Sentence Gate Log`를 추가했다.
- `korean-copy-polish-rules.md`에 전략어 누출과 영어식 문장 골격 실패 예시를 추가했다.
- `danho-detailpage-workflow/SKILL.md`와 `PROJECT_STRUCTURE_AI_CONTEXT.md`에 spoken_korean_gate 미달 시 코딩 금지 규칙을 추가했다.

**운영 규칙**:
- 전략은 내부 문서에서만 쓴다. visible copy에는 전략어가 한 단어라도 나오면 revise다.
- `장비감`, `전환`, `before/after`, `메커니즘`, `가치 프레임`, `동선`, `흐름을 줄이다`, `선택을 줄이다`, `구매 저항`, `가격 방어`는 노출 카피 금지어다.
- 전략은 먼저 고객 입말로 바꾼다. 예: `value stack` -> `칼만 오는 게 아니라 같이 필요한 것도 있네`.
- 모든 노출 문장은 Kakao 테스트, 소리 내 읽기 테스트, 판매자 발화 테스트, 전략어 누출 테스트, 문장 골격 테스트를 통과해야 한다.
- 톤은 추상 형용사가 아니라 `누가 누구에게 어떻게 말하는지`와 Good/Bad 문장쌍으로 정의한다.

### 29. 판매채널 비노출과 리뷰 섹션 필수화

**요청일**: 2026-06-11

**사용자 요청**:
상세페이지는 이미 판매채널 안에 있으므로 visible copy에 판매채널을 쓸 필요가 없다. 리뷰 섹션은 반드시 있어야 하며, 리뷰 정보가 없으면 나중에 교체할 더미 리뷰라도 넣어 실제 상세페이지처럼 기획/코딩해야 한다. 고객 화면에 이상한 경고 문구가 나오지 않게 한다.

**원인 분석**:
- 이전 규칙은 가격 직접 표기를 막으면서 `구매 페이지에서 확인`이나 특정 채널명을 대체 문구처럼 쓰게 만들었다.
- 실제 상세페이지에서는 구매자가 이미 옵션/주문 영역 근처에 있으므로, `스마트스토어`, `쿠팡`, `판매 채널` 같은 말은 불필요하고 어색하다.
- 과거 윤리 규칙은 `실제 리뷰 없으면 리뷰 섹션 생략`으로 흐르기 쉬웠고, 그 결과 실제 업로드용 상세페이지의 구매 리듬이 빠졌다.
- `NEEDS_PROOF`, `실제 리뷰 없음`, `교체 예정` 같은 운영 문구가 visible copy에 섞이면 실제 판매 페이지가 아니라 작업물처럼 보인다.

**반영 내용**:
- `skills/danho-detailpage-copywriter/references/channel-review-production-rules.md`를 추가했다.
- `danho-detailpage-planning/SKILL.md`에 판매채널명 비노출, 리뷰 섹션 필수, 더미 리뷰 내부 교체 플래그 규칙을 추가했다.
- `danho-detailpage-copywriter/SKILL.md`에 sales-channel leakage, missing review section, visible placeholder warnings 진단과 실패 조건을 추가했다.
- `copy-review-format.md`에 Production Readiness Audit과 Review Replacement Log를 추가했다.
- `mobile-scan-purchase-audit.md`, `korean-copy-polish-rules.md`, `korean-commerce-expression-bank.md`, `consumer-benefit-copy.md`에 리뷰/채널/옵션 영역 규칙을 반영했다.
- `output-format.md`, `copy-templates.md`, `section-library.md`, `detail-flow-rules.md`, `wadiz-empathy-conversion-flow.md`에 리뷰 섹션 준비와 교체용 리뷰 카드 규칙을 반영했다.
- `danho-detailpage-workflow/SKILL.md`, `danho-detailpage-coding/SKILL.md`, 코딩 체크리스트에 리뷰 섹션 누락 및 visible 내부 경고 노출 시 코딩/납품 실패 규칙을 추가했다.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`의 워크플로우를 `v10_korean_first_channel_hidden_review_required`로 갱신했다.

**운영 규칙**:
- visible copy에는 `스마트스토어`, `쿠팡`, `자사몰`, `판매 채널`, `채널별 구성`을 쓰지 않는다.
- 가격/프로모션은 숫자 가격으로 디자인하지 않고, 필요할 때만 `현재 혜택은 옵션 영역에서 확인해 주세요`처럼 페이지 안의 옵션/주문 영역 기준으로 안내한다.
- 모든 신규 상세페이지에는 리뷰/후기 섹션을 포함한다.
- 실제 리뷰가 없으면 교체용 더미 리뷰 카드를 쓰되 이름, 나이, 지역, 날짜, 별점, 리뷰 수, 구매 수, `실제 구매자` 같은 허위 구체정보를 만들지 않는다.
- 리뷰 교체 상태는 `REVIEW_PLACEHOLDER_REPLACE_REQUIRED`로 내부 로그에만 남긴다.
- visible copy에는 `더미 리뷰`, `실제 리뷰 없음`, `교체 예정`, `업로드 전 교체`, `NEEDS_PROOF`, `REVIEW_PLACEHOLDER_REPLACE_REQUIRED` 같은 작업 문구를 노출하지 않는다.

### 30. KoSEnd 논문 기반 한국어 종결어미 검수 게이트 추가

**요청일**: 2026-06-12

**사용자 요청**:
한국어 교정 관련 스킬에 `Making Sense of Korean Sentences: A Comprehensive Evaluation of LLMs through KoSEnd Dataset` 논문을 반영해 개선한다.

**원인 분석**:
- 이전 교정 규칙은 말투를 `~요`에서 `~니다`로 바꾸는 표면 정중도 조정에 치우칠 위험이 있었다.
- 상세페이지 헤드라인과 본문이 모두 비슷한 종결어미로 끝나면 문법적으로는 맞아도 페이지 전체가 독립 문장 나열처럼 보인다.
- CTA, 요청, 안내, 경고, FAQ 답변은 모두 다른 문장 기능인데, 같은 존댓말 종결로 처리하면 소비자에게 어색하거나 강압적으로 들릴 수 있다.
- 논문은 한국어 종결어미가 문법, 관계, 감정, 사회적 뉘앙스를 함께 담고 있으며, 자연스러운 종결어미가 아예 없을 수 있음을 보여준다.

**반영 내용**:
- `skills/danho-detailpage-copywriter/references/korean-sentence-ending-gate.md`를 추가했다.
- `danho-detailpage-copywriter/SKILL.md`에 sentence-ending fit pass, `sentence_ending_fit` 점수 게이트, 반복 종결 리듬 진단을 추가했다.
- `korean-copy-polish-rules.md`에 문법적으로 맞지만 문맥상 틀린 종결어미와 강제 종결 실패 조건을 추가했다.
- `korean-first-expression-gate.md`에 문장 기능과 종결어미 일치 테스트를 추가했다.
- `mobile-scan-purchase-audit.md`와 `copy-review-format.md`에 `sentence_ending_fit` 점수와 Sentence Ending Audit 표를 추가했다.
- `projects/0612_korean_sentence_ending_test/`에 기본 검증 상품인 무타공 자석 도어스토퍼 테스트 산출물을 만들었다.

**운영 규칙**:
- 종결어미는 정중도 표시가 아니라 의미 선택으로 다룬다.
- 모든 노출 문장은 화자, 청자, 관계, 매체, 섹션 역할, 문장 기능을 먼저 분류한 뒤 종결을 고른다.
- 자연스러운 종결어미가 없으면 `none_fits`로 표시하고 문장을 나누거나 명사구, 체크리스트, CTA 라벨로 바꾼다.
- 헤드라인은 반드시 완결 문장일 필요가 없다. 제품의 의미가 더 선명하면 명사구나 체언형을 우선한다.
- 명령형과 요청형은 CTA, 설치 안내, 주의, FAQ 답변에서 따로 검수한다.
- 인접 섹션이 같은 종결 패턴을 반복하면 자연스러워도 revise다.

### 31. Codex native image preview와 파일 경로 복구 규칙 보강

**요청일**: 2026-06-18

**사용자 요청**:
Codex 내장 이미지 생성으로 preview가 보였는데도 파일을 못 찾는다고 판단한 문제가 있었다. 이전 작업에서는 생성 이미지가 `.codex/generated_images`에서 정상 복구됐으므로, OpenAI 공식 문서와 웹검색으로 Codex 이미지 생성 주의사항을 확인하고 스킬을 개선한다.

**공식 문서 확인 요약**:
- Codex app/CLI 공식 문서는 내장 이미지 생성이 `gpt-image-2`를 사용하며 자연어 또는 `$imagegen`으로 호출할 수 있다고 설명한다.
- OpenAI Image/Responses API 문서는 GPT Image 출력이 이미지 데이터로 반환되고 호출자가 파일로 저장해야 함을 보여준다. 따라서 preview 표시와 프로젝트 파일 저장은 같은 사건이 아니다.
- Codex changelog에는 local image attachments와 standalone image generations가 저장 파일 경로를 모델에 노출하는 개선이 기록되어 있다. 다만 표면/버전/런타임에 따라 agent에게 경로가 실제로 노출되는지 확인해야 한다.
- Codex UI의 `codex-clipboard-*.png`는 대화 화면 캡처일 수 있으므로, preview 존재 증거로만 쓰고 실제 생성 에셋 provenance로 쓰지 않는다.

**반영 내용**:
- `danho-imageprompt-helper/SKILL.md`에 saved path 우선 확인, `generated_images` 복구, 사용자가 실제 생성 파일을 제공한 경우의 `USER_SUPPLIED_NATIVE_OUTPUT`, 대화 스크린샷의 진단 전용 처리 규칙을 추가했다.
- `native-image-generation.md`에 OpenAI 공식 문서 기반 주의사항과 `native_preview_path_unavailable` 판단 순서를 추가했다.
- `collect_codex_generated_images.py`에 `--diagnose` 옵션을 추가해 `.codex/generated_images` 후보와 Temp의 `codex-clipboard-*.png` 캡처를 함께 보여주되, 캡처를 원본 생성 에셋으로 오인하지 않게 했다.
- 실제 Codex 네이티브 이미지 생성 테스트에서 `.codex/generated_images`에 새 파일이 생기지 않았지만, `.codex/sessions/**/*.jsonl`의 `image_generation_end.result` base64 원본을 찾아 PNG로 복구했다.
- `collect_codex_generated_images.py`에 `--copy-latest-session` 옵션을 추가해 session JSONL의 native output을 프로젝트 `assets/generated/` 경로로 디코딩 복사할 수 있게 했다.
- `image-handling.md`와 `output-checklist.md`에 conversation screenshot 금지와 preview 복구 확인 체크를 추가했다.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`의 generated output recovery 규칙을 saved path -> generated_images -> session JSONL -> diagnostic 순서로 갱신했다.

**검증 결과**:
- 테스트 생성 호출: 2026-06-18 10:17:02 KST 이후.
- `.codex/generated_images` 검색 결과: 새 `ig_*.png` 없음.
- session JSONL 복구 원본: `image_generation_end`, call id `ig_079ce45562b0bd30016a3347147984819191fb31e6a9265999`.
- 복구 파일: `test-results/native-image-path-test/recovered-from-session-jsonl.png`.
- 검증: PNG, 1024x1536, SHA-256 `384DB19227C30205B1FB674FD57A6DDC5D79D75ABBC8EF2C5F118F9D8C451E53`.

**운영 규칙**:
- `image_gen.imagegen` preview가 보이면 생성은 성공한 것으로 본다. 문제는 파일 경로 노출/복구다.
- 생성 직후 agent에게 exposed saved path가 있는지 먼저 확인한다.
- exposed path가 없으면 `.codex/generated_images/**/ig_*.png`를 시간 기준으로 찾고 복사한다.
- 그래도 없으면 `.codex/sessions/**/*.jsonl`의 `image_generation_end.result`를 찾아 `SESSION_JSONL_NATIVE_OUTPUT`으로 복구한다.
- 마지막으로 `--diagnose`로 UI clipboard 캡처와 generated output을 구분한다.
- 사용자가 실제 생성 이미지 파일을 첨부하면 project `assets/generated/`로 복사하고 manifest에 `USER_SUPPLIED_NATIVE_OUTPUT`으로 기록할 수 있다.
- 사용자가 첨부한 파일이 대화 화면 캡처라면 최종 에셋으로 쓰지 않는다.

### 32. 필수 FULL_IMAGE 섹션 다운그레이드 금지

**요청일**: 2026-06-18

**사용자 요청**:
상세페이지 구성과 이미지 생성에서 디자인된 풀 이미지 섹션은 반드시 있어야 한다. 한글 타이포 오류를 피하려고 텍스트 없는 이미지 + HTML 오버레이로 우회하는 것이 아니라, 오류가 있으면 재생성하거나 수정해야 한다.

**원인 분석**:
- 기존 규칙은 `FULL_IMAGE`의 중요성을 말하면서도, 한글 타이포 실패 시 `HTML overlay`나 `HTML_MIXED`로 낮추는 fallback을 허용했다.
- 이 fallback은 업로드 안정성에는 유리하지만, 사용자가 요구한 “이미지 모델이 배경·제품·타이포·카드·디자인을 포함해 완성한 섹션”이라는 산출물 기준을 깨뜨린다.
- 따라서 mandatory `FULL_IMAGE`와 선택적 `IMAGE_STORY`/`HTML_MIXED`의 실패 처리 기준을 분리해야 한다.

**반영 내용**:
- `danho-imageprompt-helper/SKILL.md`, `native-image-generation.md`, `prompt-guide.md`에 mandatory `FULL_IMAGE` 다운그레이드 금지 규칙을 추가했다.
- `danho-detailpage-coding/SKILL.md`, `image-handling.md`, `output-checklist.md`에 `FULL_IMAGE`가 한글 오류 때문에 `IMAGE_STORY`, `HTML_MIXED`, textless image, HTML overlay로 조용히 낮아지면 실패로 보도록 추가했다.
- `danho-detailpage-workflow/SKILL.md`와 `PROJECT_STRUCTURE_AI_CONTEXT.md`에 최상위 워크플로우 규칙으로 `FULL_IMAGE_TEXT_QA_BLOCKED`를 추가했다.

**운영 규칙**:
- `image-plan.md`나 사용자가 `FULL_IMAGE`로 지정한 섹션은 필수 풀 이미지 섹션이다.
- 한글 타이포가 틀리면 네이티브 이미지 생성으로 재생성/수정한다.
- 텍스트 없는 이미지 + HTML 오버레이는 mandatory `FULL_IMAGE`의 정상 fallback이 아니다.
- 반복 실패 시 `FULL_IMAGE_TEXT_QA_BLOCKED`로 기록하거나 사용자에게 role 변경 승인을 받아야 한다.

### 33. 상세페이지 버튼 UI 생성 금지

**요청일**: 2026-06-18

**사용자 요청**:
상세페이지 디자인에는 버튼이 들어가면 안 된다. CTA뿐 아니라 전체적으로 버튼을 만들지 않게 스킬을 개선한다.

**원인 분석**:
- 이전 규칙이 final CTA에 `button labels`, `cta-button`, 구매 버튼 문구를 요구했다.
- 이미지 프롬프트도 final CTA에서 button-like labels를 허용해, 생성 이미지 안에 둥근 버튼 그래픽이 들어갔다.
- 상세페이지는 판매 채널의 구매 버튼과 별개인 정적 콘텐츠이므로, 상세페이지 섹션 내부에 클릭 가능한 UI처럼 보이는 버튼을 만들면 업로드용 디자인 기준과 충돌한다.

**반영 내용**:
- `danho-detailpage-workflow`, `planning`, `copywriter`, `coding`, `imageprompt-helper` 스킬 본문에서 CTA 버튼 필수 규칙을 정적 CTA cue 규칙으로 교체했다.
- copy/planning 참고 파일에서 `missing final CTA buttons`, `button labels`, `CTA 버튼 문구`를 `final static CTA cue`로 교체했다.
- coding 디자인 스펙/프리셋/build.py에서 `cta-button` 토큰을 `cta-cue`로 바꾸고 버튼형 CSS 예시를 제거했다.
- image prompt guide에 버튼, link-button, rounded CTA control, button-like label 금지를 추가했다.

**운영 규칙**:
- `<button>`, `.cta-button`, 링크 버튼, 버튼처럼 보이는 둥근 CTA 그래픽은 상세페이지 HTML/이미지에서 만들지 않는다.
- final CTA는 정적 타이포, 제품/결과 이미지, 구분선, 옵션/구성 확인 cue로 마감한다.
- 구매 실행 버튼은 상세페이지가 아니라 판매 채널의 구매 영역이 담당한다.

### 34. 내용이 적은 섹션의 이미지 기반 길이 확보

**요청일**: 2026-06-18

**사용자 요청**:
상세페이지에서 내용이 적은 섹션이 짧은 텍스트, note box, 작은 카드 1-2개만으로 끝나면 안 된다. 이미지가 섹션의 길이와 설득을 맡도록 스킬을 개선한다.

**원인 분석**:
- 기존 규칙은 low-copy result/transition 섹션만 주로 다뤄, 옵션 선택, 보관 안내, 가치 설명, 마무리 섹션처럼 텍스트가 적지만 독립 화면으로 남는 유형을 충분히 잡지 못했다.
- 그래서 `headline -> lead`, `note box`, `1-2 card` 구조가 큰 빈 여백과 함께 남아 상세페이지가 얕고 웹 섹션처럼 보였다.
- 빈 패딩이나 배경색만으로 세로 길이를 늘리는 것은 상세페이지 설득력이 아니라 공백을 늘리는 처리이므로 실패 조건으로 분리해야 한다.

**반영 내용**:
- `SPARSE_SECTION_IMAGE_REQUIRED` 규칙을 `workflow`, `planning`, `pm-reviewer`, `coding`, `imageprompt-helper` 스킬 본문에 추가했다.
- `screen-flow-planning.md`와 `output-format.md`에 `sparse_image_gate` 필드를 추가해 계획 단계에서 sparse 섹션을 표시하도록 했다.
- `mobile-screen-storyboarding.md`, `mobile-hybrid-layout.md`, `image-handling.md`, `proof-proximity-and-page-length.md`, `image-plan-template.md`, `output-checklist.md`에 sparse 섹션 검수와 해결 방식을 추가했다.
- `prompt-guide.md`와 `danho-imageprompt-helper/SKILL.md`에 sparse 섹션용 큰 지원 이미지/풀 이미지 프롬프트 기준을 추가했다.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`에 전역 운영 규칙으로 반영했다.

**운영 규칙**:
- kicker/headline/짧은 lead, note box 1개, 작은 카드 1-2개뿐인 섹션은 `SPARSE_SECTION_IMAGE_REQUIRED`로 본다.
- 옵션, 보관/관리, 가치, 안심, 결과, 전환, 마지막 결정 섹션도 이 규칙의 대상이다.
- 해결 방식은 `FULL_IMAGE`, `IMAGE_STORY`, 큰 `HTML_MIXED` 지원 이미지, 또는 인접 proof/detail 섹션과 병합이다.
- 큰 지원 이미지는 상품, 사용 장면, 옵션/구성, 보관/관리, 비교/증거, 리뷰 맥락처럼 실제 구매 판단을 돕는 이미지여야 한다.
- 빈 패딩, 빈 다크/페일 배경, 작은 장식 썸네일만으로 섹션을 길게 만드는 것은 실패다.

### 35. 첫 1-2번 섹션 오프닝 스토리 브릿지 강화

**요청일**: 2026-06-18

**사용자 요청**:
첫 번째 섹션과 두 번째 섹션이 공통적으로 스토리텔링이 부족하고, 두 번째 섹션이 갑작스럽게 나오는 느낌이다. 이 문제를 해결하려면 분량과 스토리텔링이 늘어나야 한다.

**원인 분석**:
- 기존 규칙은 첫 3개 화면이 정체성/베네핏/구매 조건을 답해야 한다고 했지만, 1번 화면과 2번 화면을 하나의 오프닝 시퀀스로 묶어 검수하지 않았다.
- 그래서 1번 화면은 강한 약속, 2번 화면은 일반적인 문제 제기처럼 따로 작동해 섹션 전환이 갑작스럽게 느껴졌다.
- 카피가 자연스러워도 2번 화면이 1번 화면의 장면, 행동, 감정, 시각 모티프를 이어받지 않으면 공감이 생기지 않는다.

**반영 내용**:
- `OPENING_STORY_BRIDGE_REQUIRED` 게이트를 `planning`, `pm-reviewer`, `copywriter`, `workflow`, `coding`, `imageprompt-helper`에 추가했다.
- `output-format.md`에 `오프닝 스토리 브릿지` 표를 추가해 01번 화면과 02번 화면의 역할, 공유 앵커, 이어지는 감정, 다음 구매 질문, 필요한 분량/비주얼을 기록하게 했다.
- `screen-flow-planning.md`와 `detail-flow-rules.md`에 01번은 약속/결과, 02번은 같은 생활 장면/반복 불편/첫 질문으로 이어져야 한다는 규칙을 추가했다.
- `mobile-scan-purchase-audit.md`와 `persuasion-storybrand-check.md`에 첫 두 화면 연결성을 페이지 레벨 검수로 추가했다.
- `mobile-screen-storyboarding.md`, `output-checklist.md`, `prompt-guide.md`에 HTML과 이미지 프롬프트 모두 1-2번 화면의 공유 장면/모티프를 유지하도록 추가했다.

**운영 규칙**:
- 1번 화면은 상품 정체성, 결과 약속, 강한 첫인상을 만든다.
- 2번 화면은 1번 화면과 같은 구매자 상황, 물건/행동, 장소, 감정, 시각 모티프 중 하나 이상을 이어받아야 한다.
- 2번 화면은 갑자기 일반 문제, 스펙, 기능 설명으로 넘어가면 실패다.
- 2번 화면은 헤드라인과 짧은 문장 하나로 끝내지 말고, 생활 장면, 반복 불편, 감정, 다음 질문 중 2-3개 비트를 담거나 큰 이미지/풀 이미지로 시각적 스토리를 보강한다.

### 36. 이미지 장수 제한 제거

**요청일**: 2026-06-18

**사용자 요청**:
이미지 장수에 제한이 있으면 안 된다. 상세페이지에 필요한 경우 이미지를 충분히 사용할 수 있어야 한다.

**원인 분석**:
- 과거 하이브리드 테스트 기준인 `FULL_IMAGE`와 HTML 섹션의 절반 구성, 섹션 라이브러리의 `이미지: 2~3개` 같은 표기가 실제 운영에서 이미지 장수 상한처럼 해석될 수 있었다.
- sparse 섹션, 옵션/보관/가치/리뷰/비교 섹션은 제품에 따라 필요한 이미지 장수가 크게 달라지므로 고정 수량이나 고정 비율은 상세페이지 품질을 제한한다.
- 이미지 생성 시간이 늘어나는 문제는 큐를 줄이는 방식이 아니라, 승인된 독립 자산을 배치로 나누어 생성하는 방식으로 해결해야 한다.

**반영 내용**:
- `danho-detailpage-workflow`, `planning`, `coding`, `imageprompt-helper` 스킬 본문에 이미지 장수 상한 및 고정 full-image/HTML split 금지 규칙을 추가했다.
- `mobile-hybrid-layout.md`, `image-plan-template.md`, `output-checklist.md`, `prompt-guide.md`의 수량/검수 문구를 `approved image-plan` 기준으로 수정했다.
- `section-library.md`의 `이미지: 0~1개`, `1~2개`, `2~3개`, `없음` 표기를 `필요 수량, 상한 없음` 또는 `필요 시 사용, 상한 없음`으로 교체했다.
- `PROJECT_STRUCTURE_AI_CONTEXT.md`의 human summary, YAML, XML 실행 단계에 `no_image_count_cap_or_forced_split` 규칙을 반영했다.

**운영 규칙**:
- 이미지 장수에는 상한을 두지 않는다.
- `FULL_IMAGE`, `HTML_MIXED` 지원 이미지는 스토리 연결, 증거 밀도, 옵션, 보관/관리, 비교, 리뷰, sparse 섹션 길이, 최종 결정 지원에 필요한 만큼 사용한다.
- 고정 split, 고정 percentage, 생성 호출 절약을 이유로 필요한 이미지를 줄이지 않는다.
- 이미지를 줄일 수 있는 경우는 섹션 역할이 실제로 중복되거나 승인된 `image-plan.md`가 변경된 경우뿐이다.

### 37. 새 작업 디렉토리 AGENT.MD 초기화

**요청일**: 2026-06-18

**사용자 요청**:
플러그인을 설치한 뒤에는 새 디렉토리에서 상세페이지 작업을 진행할 예정이다. 이때 워크플로우를 해당 작업 디렉토리의 `AGENT.MD`에 작성하는 초기화 기능이 필요하다.

**원인 분석**:
- 플러그인 스킬은 설치 캐시에 있지만, 실제 상세페이지 산출물은 별도의 새 작업 디렉토리에서 생성될 수 있다.
- 새 디렉토리에는 Danho 워크플로우, 산출물 위치, 검수 게이트, 이미지 생성 규칙이 로컬 지시로 남아 있지 않아 다음 작업/재개 시 일관성이 떨어질 수 있다.
- `AGENT.MD`를 작업 루트에 생성하면 플러그인 설치 위치와 프로젝트 작업 위치를 분리하면서도 로컬 작업 규칙을 유지할 수 있다.

**반영 내용**:
- `skills/danho/assets/AGENT.MD.template.md`를 추가해 새 작업 루트에 들어갈 워크플로우 체크리스트를 정의했다.
- `skills/danho/scripts/init_workspace.py`를 추가해 현재 작업 디렉토리 또는 지정한 `--target`에 `AGENT.MD`를 생성하도록 했다.
- `danho/SKILL.md`에 새 작업 디렉토리 초기화 규칙을 추가했다.
- `danho-detailpage-workflow/SKILL.md`에 workflow order 0으로 `AGENT.MD` 초기화 단계를 추가했다.
- `agents/openai.yaml` 메타 설명과 `PROJECT_STRUCTURE_AI_CONTEXT.md`의 human summary, YAML, XML, 실행 메모에 초기화 기능을 반영했다.

**운영 규칙**:
- 새 Danho 작업 디렉토리에서 시작하면 상세페이지 프로젝트 산출물을 만들기 전에 루트에 `AGENT.MD`를 생성한다.
- `AGENT.MD`는 `projects/MMDDHHmm_product-name/` 안이 아니라 작업 루트에 둔다.
- 기존 `AGENT.MD`는 사용자가 명시적으로 요청하지 않으면 덮어쓰지 않는다.
- `AGENT.MD`는 로컬 부트스트랩 체크리스트이며, 설치된 `danho-detailpage-workflow` 스킬이 더 최신이거나 구체적이면 스킬을 우선한다.

### 38. 레퍼런스 상세페이지 디자인 에센스 추출 루틴

**요청일**: 2026-06-18

**사용자 요청**:
사용자가 레퍼런스용 상세페이지 디자인 파일을 첨부하면 해당 디자인의 디자인 및 레이아웃 에센스를 추출해서 제작하는 상세페이지 디자인에 참고 사용할 수 있도록 하는 루틴을 추가한다.

**원인 분석**:
- 기존 워크플로우는 제품 이미지 레퍼런스와 생성 이미지 레퍼런스는 다뤘지만, 상세페이지 디자인 파일을 레이아웃/시각 문법 참고자료로 분석하는 별도 단계가 없었다.
- 레퍼런스 디자인을 그대로 복제하면 브랜드/문구/사진/고유 구성을 침해하거나 새 제품의 구매 여정을 망칠 수 있다.
- 따라서 레퍼런스 파일을 원본 에셋이 아니라 `design essence` 입력으로 분리하고, 분석 산출물을 `DESIGN.md`, 모바일 화면 흐름, HTML, 이미지 프롬프트에 연결해야 한다.

**반영 내용**:
- `skills/danho-detailpage-planning/references/reference-design-analysis.md`를 추가해 `REFERENCE_DESIGN_ANALYSIS.md` 산출물 템플릿과 분석 기준을 정의했다.
- `skills/danho-detailpage-planning/scripts/prepare_reference_designs.py`를 추가해 reference design 파일을 `assets/reference-designs/`로 복사하고 긴 이미지를 slice할 수 있게 했다.
- `danho`, `workflow`, `planning`, `pm-reviewer`, `coding`, `imageprompt-helper` 스킬에 레퍼런스 디자인 분석 루틴을 연결했다.
- `output-format.md`, `image-plan-template.md`, `image-handling.md`, `prompt-guide.md`, `product-reference-images.md`, `output-checklist.md`, `AGENT.MD.template.md`, `README.md`, `PROJECT_STRUCTURE_AI_CONTEXT.md`에 관련 규칙을 반영했다.
- 플러그인 버전을 `0.1.1`로 올리고 manifest 설명에 reference design essence extraction을 추가했다.

**운영 규칙**:
- 레퍼런스 상세페이지 디자인 파일은 `assets/reference-designs/`에 보관하고 `assets/inbox/` 제품 이미지와 섞지 않는다.
- 레퍼런스 디자인이 있으면 `REFERENCE_DESIGN_ANALYSIS.md`를 먼저 작성한다.
- 추출 대상은 섹션 리듬, 시각 무게, 여백, 타이포 대비, 카드/비교/후기/구분선 패턴, 이미지 크롭, 전환 방식이다.
- 복제 금지 대상은 브랜드, 로고, 문구, 가격, 제품 이미지, 모델 사진, 정확한 섹션 순서, 정확한 픽셀 레이아웃, 고유 구성이다.
- 이미지 프롬프트에는 `REFERENCE_DESIGN_ANALYSIS.md`의 style anchor만 반영하고, 레퍼런스 파일을 제품 원본으로 취급하지 않는다.

### 39. 필수 디자인 풀 이미지 섹션 생성 누락 방지

**요청일**: 2026-06-18

**사용자 요청**:
상세페이지에는 디자인된 풀 이미지 섹션을 구성하고 해당 디자인 이미지를 생성하는 것이 필수인데, 테스트에서 제작되지 않았다. 원인을 분석하고 해결한다.

**원인 분석**:
- 기존 규칙은 `FULL_IMAGE`로 지정된 섹션을 다운그레이드하지 말라는 사후 규칙은 강했지만, 애초에 신규 상세페이지가 반드시 `FULL_IMAGE`를 계획하고 생성해야 한다는 최소 계약이 약했다.
- `첫 섹션은 디자인된 히어로 이미지가 있으면 full-image` 같은 조건부 문구가 남아 있어, 테스트 시 HTML 텍스트 히어로나 평범한 CTA로 빠질 수 있었다.
- `image-plan.md`에 필수 `FULL_IMAGE` 행이 없어도 imageprompt-helper가 계속 진행할 수 있어, 생성 단계에서 누락을 차단하지 못했다.

**반영 내용**:
- 모든 신규 상세페이지에 `DESIGNED_FULL_IMAGE_REQUIRED` 게이트를 추가했다.
- 최소 계약을 `1번 히어로 FULL_IMAGE + 마지막 상품/결과 클로징 FULL_IMAGE`로 정의했다.
- `planning`, `pm-reviewer`, `coding`, `workflow`, `imageprompt-helper` 스킬에 필수 full-image 누락 실패 조건을 추가했다.
- `screen-flow-planning.md`, `output-format.md`, `image-plan-template.md`, `mobile-hybrid-layout.md`, `image-handling.md`, `output-checklist.md`, `prompt-guide.md`, `native-image-generation.md`, `html-first-detailpage-build.md`, `proof-proximity-and-page-length.md`, `section-library.md`, `AGENT.MD.template.md`, `README.md`, `PROJECT_STRUCTURE_AI_CONTEXT.md`에 같은 기준을 반영했다.
- 플러그인 버전을 `0.1.2`로 올리고 manifest 설명에 mandatory designed full-image sections를 추가했다.

**운영 규칙**:
- 신규 상세페이지의 `image-plan.md`에는 반드시 opening hero와 final product/result closing `FULL_IMAGE` 행이 있어야 한다.
- 두 필수 행이 없으면 이미지 생성으로 넘어가지 말고 `image-plan.md`를 수정한다.
- 마지막 클로징 근처에 옵션/가격/법적/호환성처럼 editable 정보가 필요하면, 그 정보는 인접 HTML 섹션으로 분리하고 별도의 상품/결과 클로징 `FULL_IMAGE`는 유지한다.
- 필수 `FULL_IMAGE`의 한글 타이포가 실패하면 재생성/수정하거나 `FULL_IMAGE_TEXT_QA_BLOCKED`로 기록한다. HTML 오버레이, textless image, `HTML_MIXED`로 조용히 낮추지 않는다.

### 40. 마지막 CTA 버튼/구매 행동 문구 제거

**요청일**: 2026-06-18

**사용자 요청**:
쇼핑몰 상세페이지에 들어갈 디자인이므로 마지막 CTA 버튼이나 그에 상응하는 텍스트는 의미가 없다. 마지막 영역에서 구매 행동 문구를 빼고, 스킬 전반에 반영한다.

**원인 분석**:
- 기존 규칙은 버튼 UI는 금지했지만, `final static CTA/closing`, `CTA cue`, `옵션 확인`, `혜택 확인` 같은 비버튼형 구매 행동 문구를 마지막 섹션에 남길 여지가 있었다.
- 쇼핑몰의 구매 버튼, 옵션 선택, 혜택/쿠폰 표시는 상세페이지 외부의 구매 UI가 담당하므로, 상세페이지 마지막 디자인이 같은 역할을 반복하면 부자연스럽다.
- `cta-cue` 컴포넌트명과 프리셋 토큰이 남아 있어 새 프로젝트에서 CTA처럼 보이는 마감 요소가 다시 생성될 수 있었다.

**반영 내용**:
- 최종 필수 `FULL_IMAGE`를 `final product/result closing`으로 재정의했다.
- 마지막 클로징에는 CTA 버튼, button-equivalent text, 옵션/주문 prompt, 혜택 확인 prompt, `구매하기`, `옵션 확인`, `혜택 확인`, `지금 보기`, `구성 확인`, `장바구니`, `주문` 문구를 넣지 않도록 했다.
- `cta-cue`, `cta-section`, `final-cta` 예시를 `closing-note`, `closing-section`, `final-closing`으로 교체했다.
- `planning`, `copywriter`, `pm-reviewer`, `coding`, `workflow`, `imageprompt-helper`, `AGENT.MD` 템플릿, README, manifest, `PROJECT_STRUCTURE_AI_CONTEXT.md`에 같은 기준을 반영했다.
- 플러그인 버전을 `0.1.3`으로 올렸다.

**운영 규칙**:
- 마지막 화면은 구매 유도가 아니라 제품명, 사용 후 장면, 조용한 결과 확신, 브랜드 톤으로 닫는다.
- 가격/혜택/옵션/호환성처럼 바뀌거나 편집 가능해야 하는 정보는 인접 HTML 정보 섹션에만 둔다.
- 마지막 클로징 `FULL_IMAGE`는 유지하되, 구매 행동을 유도하는 버튼/라벨/문구는 생성하지 않는다.

### 41. 860px 원본 기준 모바일 QA와 개발환경 의존성 축소

**요청일**: 2026-06-18

**사용자 요청**:
모바일 렌더링 검수는 393px/438px 폭으로 직접 렌더링하는 것이 아니라, 폭 860px 원본 상세페이지를 렌더링한 뒤 438px로 줄였을 때 폰트 가독성이 괜찮은지 판단해야 한다. 또한 Playwright, Python, Node 임시 서버가 없는 환경에서도 단순 HTML+CSS 상세페이지 작업이 가능하도록 개발 환경 의존성을 낮춘다.

**원인 분석**:
- 기존 문서가 `393px`, `413px`, `phone width`를 직접 렌더 viewport처럼 지시해, 상세페이지 원본을 축소해 보는 방식이 아니라 작은 웹페이지 reflow 검수가 되었다.
- 기본 `DESIGN.md` 프리셋과 `build.py`의 폰트 토큰이 393px 직접 viewport 기준의 16~18px 본문 크기에 가까워, 860px 원본을 438px로 축소하면 본문이 너무 작아질 수 있었다.
- `split_sections.py`, Playwright 모바일 렌더, Node 임시 서버가 필수처럼 읽히는 문구가 있어, 정적 HTML/CSS 프로젝트임에도 개발환경이 없으면 검수가 막히는 구조로 보였다.

**반영 내용**:
- `danho-detailpage-coding`, `workflow`, `AGENT.MD.template`, README, output checklist, layout/typography/storyboard/hybrid 레퍼런스에 860px source + 438px scaled preview 기준을 추가했다.
- `DESIGN.md` 스펙과 모든 디자인 프리셋, `build.py` 기본 CSS의 타이포그래피를 860px 원본 기준으로 올렸다. 본문 32~36px은 438px preview에서 약 16~18px로 보이도록 맞췄다.
- `split_sections.py`는 Python이 있을 때 쓰는 선택 helper로 낮추고, Python이 없으면 section id/comment 수동 확인으로 진행하도록 했다.
- Playwright/browser automation은 선택 사항으로 낮췄고, 정적 HTML은 상대 경로와 `file://` 직접 열람을 기본으로 하도록 했다.
- Node/npm/dev server/bundler/local HTTP server는 plain HTML 검수에 요구하지 않도록 명시했다.
- 이미지 프롬프트의 tall mobile crop 문구도 `393px-wide phone screen`에서 `860px source composition scaled to 438px preview`로 바꿨다.

**운영 규칙**:
- 새 상세페이지는 860px 원본 상세페이지로 만든다.
- 모바일 가독성 검수는 같은 원본을 438px 폭으로 축소한 preview에서 본다. 393px/438px 직접 viewport reflow는 보조 stress check일 뿐 1차 검수가 아니다.
- 정적 HTML은 `file://`로 열려야 하며, 상대 경로를 사용한다.
- Playwright, Python, Node/npm, dev server, bundler, local HTTP server가 없어도 작업이 멈추면 안 된다.
