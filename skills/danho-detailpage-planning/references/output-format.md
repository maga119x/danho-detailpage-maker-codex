# PLANNING.md Output Format

Use this format for current Danho projects.

## Template

```markdown
# {제품명} 상세페이지 기획서

## 1. 기본 정보

| 항목 | 내용 |
|---|---|
| 제품명 |  |
| 제품 호칭 풀네임 |  |
| 제품 호칭 단축형 |  |
| 브랜드 단독 표기 |  |
| 가격 |  |
| 카테고리 |  |
| 타겟 |  |
| 핵심 페인포인트 |  |
| 핵심 셀링포인트 |  |
| 핵심 메시지 |  |
| 톤앤매너 |  |
| 디자인 프리셋 |  |

## 2. 섹션 구성표

| # | 섹션 id | 목적 | 설득 역할 | 이전 섹션과 연결 이유 | 이미지 변환 후보 |
|---:|---|---|---|---|---|
| 01 | hook | 첫인상 | 감각 | 시작 | REPLACE_CANDIDATE |
| 02 | scene-problem | 실제 장면 | 공감 | hook의 약속을 생활 상황으로 구체화 | SUPPORT_CANDIDATE |

## 3. 단계 분할

| 단계 | 비중 | 적용 섹션 | 설계 의도 |
|---|---:|---|---|
| 문제 인식 | 20% | hook, scene-problem, blocker | 고객 불편을 생활 장면으로 묶음 |

## 4. 섹션별 콘텐츠

### 01. hook

**헤드라인**  
...

**본문**  
...

**핵심 속성**
- ...

**이미지 변환 후보**: REPLACE_CANDIDATE

### 02. fit-check

**헤드라인**  
...

**체크 포인트**
- ...

**이미지 변환 후보**: SUPPORT_CANDIDATE

## 5. 이미지 변환 후보 요약

| 후보 | 개수 | 의미 |
|---|---:|---|
| REPLACE_CANDIDATE |  | 통 이미지 후보 |
| SUPPORT_CANDIDATE |  | HTML+이미지 혼합 후보 |
| NONE |  | HTML 중심 후보 |

## 6. 기획 메모

- 주요 구매 불안:
- 초반에 해결해야 할 조건:
- 통 이미지로 강하게 보여줄 장면:
- HTML로 정확히 유지할 정보:
```

## Rules

- Do not create separate image-only planning sections.
- Do not create image count tables in planning.
- Mark only image conversion candidates; final image roles are decided in `image-plan.md`.
- Include connection reasons so the page does not become a feature list.
- Keep internal labels in tables only. Visible copy must be consumer-facing.
- Use product naming consistently.
- Keep prices, options, compatibility, limits, and FAQ explicit and editable.
