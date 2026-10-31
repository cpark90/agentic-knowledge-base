---
id: https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e
type: decision
level: concrete
title_ko: 모든 지식은 단위 지식의 복합체다
former_title_ko: ["모든 지식 항목은 청크의 복합체다", "모든 지식은 지식 항목의 복합체다"]
title: Every knowledge item is a composite of chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0076-all-knowledge-is-composite.md, id: https://agentic-knowledge-base.dev/id/chunk-d0076, title_ko: "모든 지식 항목은 청크의 구성체다", title: "Every knowledge item is a composite of chunks"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T12:49:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0076]
part_of: https://agentic-knowledge-base.dev/id/composite/b4546452-61a1-4d61-b6c3-8af8a25e0f44
composite: {id: https://agentic-knowledge-base.dev/id/composite/b4546452-61a1-4d61-b6c3-8af8a25e0f44, title_ko: 모든 지식은 복합체다, title: All knowledge is composite}
---
**결론** — 이 체계의 모든 지식은 단위 지식이거나
단위 지식의 복합체다.

| 지식 | 단위 지식 클래스 | 복합체 |
|---|---|---|
| 결정 | `DecisionChunk` — 결론·근거·배제된 대안 | **세 단위 지식의 복합체** |
| 요구 | `RequirementChunk` — 요구 문장 (EARS) | 관심사별 복합체 |
| 합격 기준 | `DecisionChunk`·`ContractChunk` logical — 판정 술어 | 기준 집합 |
| 시나리오 (V&V) | `DecisionChunk` — 자극·요인·배제 자극 | 세 단위 지식의 복합체 |
| 검증기 (V&V) | `ArtifactChunk` executable | 테스트 케이스 열의 `co:List` |
| 시그니처 | `ContractChunk` | 대부분 단위 지식 하나 |
| 스키마 | `SchemaChunk` — 메시지·필드 | 순서 없는 복합체 |
| 모듈 | `ArtifactChunk` — **함수** | 순서 있는 복합체 |
| 리뷰 스레드 | `AnnotationChunk` — 코멘트 | 순서 있는 복합체 |
| ODD | 속성 단위 지식 | 절 복합체의 복합체 |
| 실행 기록 | `MemoryChunk` — 관측, append-only | 시간순 복합체 |
| 온톨로지 모듈 | 개념 정의 단위 지식 | 개념의 복합체 |

개발 프로파일에서 **함수 = 단위 지식**이 `artifact` 지식 종류에 코드 품질을 강제한다.
토큰 상한을 넘는 함수는 `agt:ArtifactTokenBudgetShape`를 통과하지 못하므로 분할 대상이다. 별도
규칙이 아니라 shape의 귀결이다.
