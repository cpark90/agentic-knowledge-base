---
id: https://agentic-knowledge-base.dev/id/chunk/6d639dc6-071c-4811-ad30-19018e5b8984
type: decision
level: concrete
title_ko: 규범 문서 규약 — 링크 타입은 참조·의미 의존·관련성 세 족과 구성 관계로 정렬하고 전파는 족 단위로 정한다
title: Normative-document conventions — Link types are arranged into three families, references, semantic dependence and relatedness, plus composition, and propagation is set per family
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b6248cd7-b607-4c13-adde-c2ee0f57a5a3
---
**규약** — `p10-link-families`의 결론을 규범 문서에 싣는 문장이다.

규약: `agt:references` | 본문이 식별자로 가리킴 | `cites` · `targets` · `usesDefinition`(2026-09-30 — 정의 → 같은 모듈의 정의, 추출기가 AST 의 최상위 이름 참조에서 낸다) | 대상 변경 → 출발점 `suspect`
규약: `agt:semanticallyDependsOn` | 빼면 의미상 불완전 | `refines` · `satisfies` · `constrains` · `verifies` · `derivesFrom` · `usesConcept` · `assumes` · `generates` · `allocates` | 같음. plane 단방향 안에서만
규약: `agt:relatedTo` | 참조·의미 의존 어느 족에도 들지 않는 관련성 | `coUpdatesWith` · `conflictsWith` · `overlapsWith`(2026-09-26 — 가장 약한 잎, 이름 없는 관련성의 자리) | 대칭 — 양쪽 `suspect`
규약: (구성 관계) | 함께 읽힘·순서 | `hasDirectPart` | 부분이 무효면 전체 `suspect`
