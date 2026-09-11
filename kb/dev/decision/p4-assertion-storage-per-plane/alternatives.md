---
id: https://agentic-knowledge-base.dev/id/chunk/11d95e06-7e04-4ee8-9bd7-1796a2a43ead
type: decision
level: logical
title_ko: plane별 assertion 형식 초안 — 아직 미확정
title: Draft assertion formats per plane, still undecided
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/8d3c07da-293b-47cd-861a-44cfd81449b3
---
**대안** — `[안]` 4.12절의 plane별 assertion 형식 초안. **미확정이다.**

| plane | 형식 | 42줄의 단위 |
|---|---|---|
| `requirement` | EARS 산문. 이해관계자·관심사 필드 | 줄 |
| `decision` | 구조화 산문. 역할 태그(결론/근거/대안) + 본문 | 줄 |
| `contract` | 언어 네이티브 선언 | 줄 |
| `schema` | 스키마 언어 (JSON Schema, protobuf 등) | 줄 |
| `artifact` | 언어 네이티브 코드. 역할 태그(구현/검증) | 줄 |
| `annotation` | 산문 + 대상 청크 IRI | 줄 |
| `memory` | 구조화 관측 (시각, 행동, 작업 집합 요약) | 항목 |

`memory`의 42줄이 줄이 아니라 항목 수여야 할 수 있다는 것이 이 초안이 확정되지
못한 이유다 — 4.9절의 "42줄이 모든 plane에 적정한가"와 같은 문제다.
