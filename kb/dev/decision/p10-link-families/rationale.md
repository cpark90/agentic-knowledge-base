---
id: https://agentic-knowledge-base.dev/id/chunk/f0d2eaac-50e3-4ee0-922b-9debdca12368
type: decision
level: logical
title_ko: 세 족과 구성 관계는 LEDGER의 엣지 분류에서 왔고 전파 규칙과 조회 우선순위가 족 단위로 정의된다
title: The three families and composition come from the LEDGER edge classification, and propagation rules and retrieval priority are defined per family
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b6248cd7-b607-4c13-adde-c2ee0f57a5a3
---
**근거** — 세 족과 구성 관계는 문서 편집 의존성 그래프 연구 LEDGER(arXiv 2606.28379)의 엣지 셋(명시적 참조·암묵적 의미 의존·의미적 관련성)과 CONTAINS에서 왔다. 2026-09-04 대조에서 이 체계의 링크 타입은 전부 의존 족이었고 참조·관련성 족이 비어 있었다. 본문의 식별자 인용은 추출만 하면 되는 참조였다. 유저는 2026-09-12에 족 상위 속성안을 포함한 권고 전부를 수용했다.

족을 상위 속성으로 두는 까닭은 전파 규칙과 조회 우선순위가 족 단위로 정의되기 때문이다(`agt:dependsOn`의 정의). 대상이 바뀌면 참조·의미 의존은 출발점만, 관련성은 양쪽을 `suspect`로 만든다. `workset`의 이웃 우선순위도 족 순서다. 순서는 앵커 ≫ references ≫ semanticallyDependsOn ≫ 구성 관계 ≫ relatedTo다.

구성 관계를 링크 족과 가르는 까닭은 통합 기준이 다르기 때문이다. 복합체는 함께 읽힘·순서이고 `relatedTo`는 함께 갱신이다.

잎으로만 확장하는 규칙(2026-09-23, 링크 견고성 E)에서 게이트는 부모 트리플을 함께 생성한다. 그래서 족 단위 질의가 새 잎을 자동으로 본다. 잎의 이름은 추적성 관계 분류(`docs/references.md`)에서 가져온다. 이 규칙 뒤에 더해진 잎은 `overlapsWith`(2026-09-26)와 `usesDefinition`(2026-09-30)이다.
