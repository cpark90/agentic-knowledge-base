---
id: https://agentic-knowledge-base.dev/id/chunk/6d639dc6-071c-4811-ad30-19018e5b8984
type: decision
level: concrete
title_ko: 규범 문서 규약 — 링크 타입은 참조·의미 의존·관련성 세 족과 구성 관계로 정렬하고 전파는 족 단위로 정한다
title: Normative-document conventions — Link types are arranged into three families, references, semantic dependence and relatedness, plus composition, and propagation is set per family
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T00:47:22+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T00:47:22+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b6248cd7-b607-4c13-adde-c2ee0f57a5a3
---
**규약** — `p10-link-families`의 결론을 규범 문서에 싣는 문장이다.

규약: `agt:references` | 본문이 식별자로 가리킨다 | `cites` · `targets` · `usesDefinition`(정의에서 같은 모듈의 정의로 가는 링크이며 추출기가 AST의 최상위 이름 참조에서 낸다, 2026-09-30) | 대상이 바뀌면 출발점이 `suspect`가 된다
규약: `agt:semanticallyDependsOn` | 빼면 의미상 불완전하다 | `refines` · `satisfies` · `constrains` · `verifies` · `derivesFrom` · `usesConcept` · `assumes` · `generates` · `allocates` | 위와 같다. 다만 지식 종류의 단방향 안에서만 전파한다
규약: `agt:relatedTo` | 참조·의미 의존 어느 족에도 들지 않는 관련성 | `coUpdatesWith` · `conflictsWith` · `overlapsWith`(가장 약한 잎이며 이름 없는 관련성의 자리다, 2026-09-26) | 대칭이므로 양쪽이 `suspect`가 된다
규약: (구성 관계) | 함께 읽힘·순서 | `hasDirectPart` | 부분이 무효면 전체가 `suspect`가 된다
