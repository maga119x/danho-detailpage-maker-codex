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
전체 섹션 중 50%는 이미지 모델 생성 디자인 이미지로, 50%는 HTML 코딩으로 구성한다. 어떤 방식이 유리한지는 Codex가 판단해 하이브리드 버전을 제작한다.

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
- 하이브리드 비율은 사용자가 지정한 비율을 따르되, 섹션 수가 홀수일 때는 정보 정확성이 필요한 섹션을 HTML 쪽에 우선 배치한다.
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
- 하이브리드 구성에서도 절반 정도는 완성된 디자인 통 이미지 섹션이어야 한다.
- 통 이미지 섹션은 이미지 모델이 만든 배경, 타이포, 카드, 아이콘이 포함된 완성 이미지 1장을 `<section>`에 그대로 배치한다.
- HTML 혼합 섹션은 문구 정확도와 수정성이 중요한 조건, 설치, 비교, 가격, FAQ 영역에 우선 적용한다.
- 테스트 적용 기준: 통 이미지 8개(`hook`, `scene-problem`, `blocker`, `answer`, `no-damage`, `daily-use`, `control`, `final-cta`) + HTML 혼합 8개(`fit-check`, `install-flow`, `fit-adjust`, `material`, `compare`, `review-proof`, `options`, `faq`).

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
