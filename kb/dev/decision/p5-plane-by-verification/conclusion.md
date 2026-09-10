---
id: https://agentic-knowledge-base.dev/id/chunk/b9e56142-cf12-47ad-b688-5848a39a87fb
type: decision
level: concrete
title_ko: plane은 판정 방식으로 정의되고 코어은 일곱이다
title: Planes are defined by verification mechanism; the skeleton has seven
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0003]
part_of: https://agentic-knowledge-base.dev/id/composite/5b5edf6d-f638-4c16-bc32-f4d8e6ed9785
composite: {id: https://agentic-knowledge-base.dev/id/composite/5b5edf6d-f638-4c16-bc32-f4d8e6ed9785, title_ko: plane 정의, title: Plane definition}
---
**결론** — 종류가 다른 지식을 하나의 컨텍스트에 섞지 않는다. 각 지식이 **"맞다"고
판정되는 메커니즘이 근본적으로 다르기** 때문이다. plane은 온톨로지 `entity/`
모듈의 최상위 분류에 대응하며, 일곱이다.

| 평면 | 식별자 | 판정 방식 | 변경률 | 청크 ID의 해석 |
|---|---|---|---|---|
| **요구** | `requirement` | **이해관계자 합의** | 가장 낮음 | 파일 |
| 결정 | `decision` | 논증의 타당성 (논박 가능) | 낮음 | 파일 |
| 데이터 스키마 | `schema` | 스키마·호환성 검사 | 낮음 | 스키마 경로 |
| 계약 | `contract` | 형식 검사 (결정론적) | 중간 | 도메인 식별자 |
| 실행 산출물 | `artifact` | 실행·실측 | 빠름 | 도메인 식별자 |
| 주석 | `annotation` | 사회적 합의 (해소/승인) | 매우 높음 | standoff 앵커 |
| 작업 메모리 | `memory` | 없음 (휘발성) | 매우 빠름 | 세션 ID + 시점 |

**요구와 주석은 둘 다 합의로 판정되지만 다른 plane이다.** 요구의 합의는
이해관계자가 "이것을 원한다"에 동의하는 것이고, 주석의 합의는 "이 지적이
해소되었다"에 동의하는 것이다. 전자는 계층의 출발점이고 후자는 임의 청크에
붙는다.
