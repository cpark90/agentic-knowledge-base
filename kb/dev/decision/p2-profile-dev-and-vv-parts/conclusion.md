---
id: https://agentic-knowledge-base.dev/id/chunk/cb89e413-b9c8-4f7e-8236-220c3dbbccfb
type: decision
level: concrete
title_ko: 도메인 프로파일은 개발 실체와 V&V 실체 두 부분이고 V&V 쪽을 먼저 또는 나란히 만든다
title: A domain profile has a development part and a V&V part, and the V&V part comes first or alongside
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/d834336a-9ec4-465b-b0e4-f44bc557677f
composite: {id: https://agentic-knowledge-base.dev/id/composite/d834336a-9ec4-465b-b0e4-f44bc557677f, title_ko: 도메인 프로파일의 두 부분, title: The two parts of a domain profile}
---
**결론** — 도메인 프로파일은 두 부분이다(노트 2.11절 `[확정]`).

| 부분 | 담는 것 | 만드는 절차 |
|---|---|---|
| 개발 실체 | plane별 청크·판정 도구·앵커 해석 (노트 부록 D) | 프로파일 템플릿 |
| V&V 실체 | 현상·인과·지표·시나리오 부류·목표 거동 | 위험 분석 G1~G6 (노트 8.21절) |

**V&V 실체는 개발 실체보다 먼저 또는 나란히 만든다.** 개발 실체만 있고 V&V 실체가 없는 프로파일로 V&V를 시작하지 않는다.

두 부분 모두 `p2-skeleton-and-domain-profile`의 규칙을 따른다 — 코어 클래스의 하위 클래스와 shape만 추가한다. V&V 실체를 만드는 절차의 상세는 `p8-risk-analysis-profile`이 정한다. 이 결정은 그 두 결정이 적지 않은 부분의 구성과 순서만 정한다.
