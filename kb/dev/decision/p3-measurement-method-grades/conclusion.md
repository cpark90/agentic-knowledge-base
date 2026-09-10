---
id: https://agentic-knowledge-base.dev/id/chunk/2df65a05-0d25-4b3c-aae9-8da6dd82218f
type: decision
level: concrete
title_ko: 판정 방법을 A~D로 등급화하고 D는 ODD에 넣지 않는다
title: Grade check methods A-D; grade D never enters the ODD
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0064]
part_of: https://agentic-knowledge-base.dev/id/composite/09270524-0ea3-40bb-8360-178681e7cbca
composite: {id: https://agentic-knowledge-base.dev/id/composite/09270524-0ea3-40bb-8360-178681e7cbca, title_ko: 판정 방법의 등급, title: Grading measurement methods}
---
**결론** — 3.2절 "모든 속성은 판정 방법을 갖는다"를 등급화한다.

| 등급 | 판정 방법 | 예 | `unverified` 위험 |
|---|---|---|---|
| A | 기계가 즉시 판정. 질의 하나 | 언어 버전, 의존성 버전, 헬스체크 | 없음 |
| B | 기계가 판정하되 비용이 있음 | 테스트 실행, 벤치마크 | 낮음 — 주기 판정 |
| C | 사람이 판정 | "고객이 이 기능을 원한다" | 높음 — 주기 재확인 필요 |
| D | 판정 불가 | "경쟁사가 먼저 출시하지 않는다" | 항상 `unverified` |

**D 등급 속성은 ODD에 넣지 않는다.** 가정으로 기록하되, 무효화 트리거가 될 수 없음을 안다.

등급이 낮은 속성이 많으면 ODD 이탈을 놓친다 — 등급 분포가 ODD 품질 지표다.
