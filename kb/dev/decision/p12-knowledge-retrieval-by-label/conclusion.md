---
id: https://agentic-knowledge-base.dev/id/chunk/595590fa-f40a-4008-92c0-f971f574111b
type: decision
level: concrete
title_ko: 검색은 어휘 앵커로 진입해 구조로 확장하고 인덱스는 라벨과 개념이다
title: Retrieval enters by vocabulary anchor and expands by structure, indexed on labels and concepts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0152-knowledge-retrieval-by-label.md, id: https://agentic-knowledge-base.dev/id/chunk-d0152, title_ko: "검색의 인덱스는 라벨과 개념이다", title: "Retrieval is indexed by labels and concepts"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0152]
part_of: https://agentic-knowledge-base.dev/id/composite/5133b9c7-e45d-462d-ad99-20e3b49ef15c
composite: {id: https://agentic-knowledge-base.dev/id/composite/5133b9c7-e45d-462d-ad99-20e3b49ef15c, title_ko: 지식 검색의 인덱스와 순서, title: The index and order of knowledge retrieval}
---
**결론** — 검색의 단위는 단위 지식이고 인덱스는 **라벨과 온톨로지 개념**이다.
순서는 **어휘 앵커 → 구조 확장** — 라벨 검색으로 진입점 단위 지식을 찾고, 그 단위 지식의
링크·part-of 이웃을 신뢰 순으로 k개까지 펼친다(k는 후보 상한 입력과 같이
7 이하).

| 검색 방식 | 인덱스 | 반환 |
|---|---|---|
| 라벨 검색 | `prefLabel`·`altLabel`·`hiddenLabel` | 단위 지식 라벨 목록 |
| 개념 검색 | 단위 지식이 참조하는 온톨로지 개념 | 그 개념을 쓰는 단위 지식 |
| 구조 검색 | 링크 패턴 | 그래프 질의 결과 |
| 유사도 검색 | 임베딩 | 후보 추림에만. 결과는 라벨 목록 |

**본문 전문 검색은 마지막 수단이다.**
