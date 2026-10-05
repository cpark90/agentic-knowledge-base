---
id: https://agentic-knowledge-base.dev/id/chunk/38ccd259-6eb4-4e0a-b2dc-8f486d6973f3
type: decision
level: concrete
title_ko: 규범 문서 규약 — 지식 베이스는 에이전트의 컨텍스트에 실리는 세 층의 정돈된 위키이고 모든 것은 한 층의 항목이거나 그 투영이다
title: Normative-document conventions — The knowledge base is a tidy three-layer wiki loaded into an agent's context, and everything is an item of one layer or its projection
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c4b958be-e5e4-43b6-b23f-989f628cb07f
---
**규약** — `p0-service-is-a-three-layer-wiki`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **선택 키 `layer: knowledge | methodology | process`는 그 항목이 서비스의 어느 층에서 역할을 갖는가다** (plane과 직교하는 역할 속성). **명시가 없으면 `knowledge`다** — `chunk2kg`가 기본값을 방출하므로 표시 누락이 산발로 세어지지 않는다. 방법론·프로세스는 명시한다. 코드 청크는 손으로 적지 않는다 — 등록부(`tools/<모듈>.chunks.yml`)의 `layer`가 원본이고 추출기가 정의·절·파일 청크 전부로 옮긴다. 값이 어휘 밖이면 `chunk2kg`가 거부하고 개수는 shape `layer-shapes.ttl`이 본다(2026-10-01).
규약: 층 | 선택 키 `layer: knowledge \| methodology \| process`는 항목이 서비스의 어느 층에서 역할을 갖는가다([p0-service-is-a-three-layer-wiki](conclusion.md), 2026-10-01). 층은 plane과 직교하므로 type 제한이 없고, 명시가 없으면 `chunk2kg`가 `agt:inLayer agt:knowledgeLayer`를 방출한다 — 표시 누락이 산발로 세어지지 않아야 하고 층별 집계(CQ-38)의 분모가 항목 전수여야 한다. 코드 청크는 등록부의 `layer`가 원본이다. 값 어휘·개수는 `layer-shapes`
