---
id: https://agentic-knowledge-base.dev/id/chunk/9b3078aa-b8a4-4236-93cc-19e10eaf6017
type: decision
level: logical
title_ko: 굵은 span을 자리와 무관하게 표지로 읽는 안과 등록 순서로 겹침을 가리는 안은 기각된다
title: Reading bold spans as markers regardless of position, and resolving overlaps by registration order, are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e1fb54c7-56d8-4864-b56b-cbd7327217d1
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 표지 낱말로 시작하는 굵은 span을 자리와 무관하게 슬롯으로 읽는다 | 2026-09-29 이전의 방출이다. 본문 중간의 강조 네 곳이 슬롯으로 잡혔다 |
| 접두가 겹치는 표지를 허용하고 등록 순서로 우선을 정한다 | 자리가 같을 때의 승자가 튜플 순서에 기댄다. 그 순서 의존은 다음 표지 추가마다 같은 사고를 낼 수 있는 잠복 결함이다 |
