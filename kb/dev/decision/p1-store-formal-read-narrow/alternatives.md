---
id: https://agentic-knowledge-base.dev/id/chunk/d4d6d54b-2fba-4d88-8cb3-957874cc7473
type: decision
level: concrete
title_ko: 텍스트 RAG나 벡터 DB만 쓰는 안은 택하지 않는다
title: Text RAG or a vector DB alone is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0013-store-formal-read-narrow.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:02:46+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:02:46+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/72187560-4939-4225-8319-7c8e0345b251
---
**대안** — 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 텍스트 RAG나 벡터 DB만 쓴다 | 연결성 보장이 없어 고아 지식과 중복 지식이 나쁜 답을 낼 때까지 보이지 않는다. 반면 형식 층은 그 결함을 빌드 실패로 만들고, 뷰 층이 RAG 수준의 편의를 제공한다 |
