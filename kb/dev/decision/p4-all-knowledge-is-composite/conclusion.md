---
id: https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e
type: decision
level: concrete
title_ko: 모든 지식 항목은 청크의 복합체다
title: Every knowledge item is a composite of chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0076]
part_of: https://agentic-knowledge-base.dev/id/composite/b4546452-61a1-4d61-b6c3-8af8a25e0f44
composite: {id: https://agentic-knowledge-base.dev/id/composite/b4546452-61a1-4d61-b6c3-8af8a25e0f44, title_ko: 모든 지식은 복합체다, title: All knowledge is composite}
---
**결론** — 이 체계에 "청크가 아닌 지식 항목"은 없다. 모든 지식 항목은 청크이거나
청크의 복합체다.

| 지식 항목 | 청크 클래스 | 복합체 |
|---|---|---|
| 결정 | `DecisionChunk` — 결론·근거·배제된 대안 | **세 청크의 복합체** |
| 요구 | `RequirementChunk` — 요구 문장 (EARS) | 관심사별 복합체 |
| 합격 기준 | `DecisionChunk`·`ContractChunk` logical — 판정식 | 기준 집합 |
| 시나리오 (V&V) | `DecisionChunk` — 자극·요인·배제 자극 | 세 청크의 복합체 |
| 검증기 (V&V) | `ArtifactChunk` executable | 케이스 열의 `co:List` |
| 시그니처 | `ContractChunk` | 대부분 청크 하나 |
| 스키마 | `SchemaChunk` — 메시지·필드 | 순서 없는 복합체 |
| 모듈 | `ArtifactChunk` — **함수** | 순서 있는 복합체 |
| 리뷰 스레드 | `AnnotationChunk` — 코멘트 | 순서 있는 복합체 |
| ODD | 속성 청크 | 절 복합체의 복합체 |
| 실행 기록 | `MemoryChunk` — 관측, append-only | 시간순 복합체 |
| 온톨로지 모듈 | 개념 정의 청크 | 개념 청크의 복합체 |

개발 프로파일에서 **함수 = 청크**가 `artifact` plane에 코드 품질을 강제한다.
42줄을 넘는 함수는 `agt:ChunkShape`를 통과하지 못하므로 분할 대상이다. 별도
규칙이 아니라 shape의 귀결이다.
