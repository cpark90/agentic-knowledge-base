---
id: https://agentic-knowledge-base.dev/id/chunk/11d95e06-7e04-4ee8-9bd7-1796a2a43ead
type: decision
level: logical
title_ko: 지식 종류별 assertion 형식 초안 — 아직 미확정
former_title_ko: ["plane별 assertion 형식 초안 — 아직 미확정"]
title: Draft assertion formats per plane, still undecided
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T12:49:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/8d3c07da-293b-47cd-861a-44cfd81449b3
---
**대안** — `[안]` 4.12절의 지식 종류별 assertion 형식 초안. **미확정이다.**

| 지식 종류 | 형식 | 42줄의 단위 |
|---|---|---|
| `requirement` | EARS 산문. 이해관계자·관심사 필드 | 줄 |
| `decision` | 구조화 산문. 역할 태그(결론/근거/대안) + 본문 | 줄 |
| `contract` | 언어 네이티브 선언 | 줄 |
| `schema` | 스키마 언어 (JSON Schema, protobuf 등) | 줄 |
| `artifact` | 언어 네이티브 코드. 역할 태그(구현/검증) | 줄 |
| `annotation` | 산문 + 대상 단위 지식 IRI | 줄 |
| `memory` | 구조화 관측 (시각, 행동, 작업 집합 요약) | 항목 |

**기각** — "42줄의 단위" 열(줄/항목)과 "`memory`의 42줄이 항목 수여야 한다"는 안은 기각됐다. 결정 `p1-chunk-unit-is-tokens`가 답했다. 단위 지식의 크기를 재는 단위는 모든 지식 종류에서 토큰이다.
