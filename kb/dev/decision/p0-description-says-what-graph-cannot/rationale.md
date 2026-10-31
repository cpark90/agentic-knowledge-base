---
id: https://agentic-knowledge-base.dev/id/chunk/968be327-2883-46cd-8625-3cd471c024ea
type: decision
level: concrete
title_ko: 검색으로 노드를 만난 쪽의 질문은 이것을 써야 하는가이고 서술이 곧 검색의 재료다
title: Whoever meets a node by search asks whether to use it, and descriptions are the material of retrieval
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0161-definition-says-why-and-when.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:43:01+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:43:01+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/32c36837-41f4-4fe9-9179-5de0af953140
---
**근거** — 출처는 harness-functional `ONTOLOGYSTYLE`의 §1과 §1d다.

- 검색으로 노드를 만난 사람과 에이전트의 질문은 이것이 무엇인가가 아니라 **이것을 써야 하는가**다. 선택 근거가 서술에 없으면 그 판단을 위해 다시 그래프를 헤매야 하고, 결국 못 고르고 새로 만든다. 이것이 `p4-search-before-authoring`의 실패 경로다.
- 쓰지 않을 것을 명시한다. 라벨 재진술("코딩 하네스는 코딩 하네스다")과 수정 이력, 리뷰 대화, 주석 처리된 죽은 선언은 발견하면 삭제한다. 남겨 두면 서술 예산만 먹고 검색 정밀도를 떨어뜨리며, 이력은 버전 관리가 갖는다.
- 서술 텍스트가 검색과 뷰의 실제 재료이므로 이 내용 규칙이 곧 검색 품질 규칙이다. 그래서 좋은 라벨과 좋은 정의가 주석보다 낫다.

이 저장소에서는 세 축이 나뉜다. 개념 정의의 **형식**은 속과 종차(`p0-genus-differentia-definition`)가, 개체 서술의 **내용**은 이 규칙이, 서술의 **크기**는 토큰 대역(`p1-node-text-token-band`)이 정한다.
