---
id: https://agentic-knowledge-base.dev/id/chunk/bee4f5da-0ec3-48fd-831b-d4d7f6ab5389
type: decision
level: concrete
title_ko: 실패 모드 셋(고아, drift, rot)마다 독립된 기계적 방어선을 둔다
title: Each of the three failure modes (orphans, drift, rot) gets an independent mechanical defence
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0014-three-failure-modes.md, id: https://agentic-knowledge-base.dev/id/chunk-d0014, title_ko: "실패 모드 셋(고아·drift·rot)마다 독립된 기계적 방어선을 둔다", title: "Each of the three failure modes, orphans, drift and rot, gets an independent mechanical defense"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0014]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/ea65a62f-fb81-43aa-878a-09fcb883fdfd
composite: {id: https://agentic-knowledge-base.dev/id/composite/ea65a62f-fb81-43aa-878a-09fcb883fdfd, title_ko: 세 실패 모드의 방어선, title: Defences against three failure modes}
---
**결론** — 자라는 지식그래프의 실패 모드는 셋이고, 실패 모드마다 독립된 기계적 방어선을 게이트로 둔다.

| 실패 모드 | 방어선 | 강제 |
|---|---|---|
| 고아(orphaned nodes) | 구조 검증이다. 연결성 shape와 전역 도달성 BFS, capability 충족을 본다 | 빌드 실패 |
| 어휘 분화(context drift) | 통제 어휘다. 스키마가 유일한 어휘이고, 라벨은 유일하며 동의어는 altLabel로 붙인다. 간선은 타입을 갖고 추론으로 정규화한다 | 빌드 실패 |
| 컨텍스트 부패(context rot) | 유계 뷰다. 관련도 순위와 토큰 예산 상한을 둔다 | 읽기 경로 |
