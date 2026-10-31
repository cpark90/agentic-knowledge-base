---
id: https://agentic-knowledge-base.dev/id/chunk/e9c81f92-b685-49ff-ba97-29641ccd945d
type: decision
level: logical
title_ko: 단위 지식 상한은 컨텍스트 예산의 1/5이고 단위 지식은 네 분야의 합류점이다
former_title_ko: ["청크 상한은 컨텍스트 예산의 1/5이고 청크는 네 분야의 합류점이다", "지식 항목 상한은 컨텍스트 예산의 1/5이고 지식 항목은 네 분야의 합류점이다"]
title: The chunk limit is one fifth of the context budget; four fields converge on the chunk
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:14:02+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/dd76498b-2cca-4b79-a1fe-ce5a4d33c0ca
---
**근거** (노트 4.1절)

- **예산의 1/5** — 1.1절 컨텍스트 예산의 약 1/5. 에이전트가 한 번에 4~5개
  단위 지식을 조망할 수 있는 크기로 잡은 값이다. 처음에는 200줄의 1/5인 42줄이었고
  2026-10-01에 같은 도출을 토큰으로 옮겨 1,092 토큰이 됐다(`p1-chunk-unit-is-tokens`).
- **지어내지 않는다** — 정보를 담는 인공물이 무엇인지는 상위 온톨로지가 이미
  정의했으므로 그 하위 클래스로 두기만 한다.
- 같은 개념이 네 분야에서 독립적으로, 이름까지 같게 정립되었다. 각 분야의
  장치가 이 체계의 다른 부품으로 흡수된다.

| 분야 | 이름 | 흡수된 곳 |
|---|---|---|
| 인지과학 | chunk (7±2) | 단위 지식 상한과 구성 상한(4.5절)의 근거 |
| 구조적 글쓰기 | information block | 단위 지식 shape (4.4절) |
| 문학적 프로그래밍 | chunk | 뷰 질의 (4.6절) |
| 모듈형 문서 | topic | 지식 종류 하위 클래스 (4.2절) |

- `Chunk`와 `Composite`를 disjoint로 두면 "본문을 가진 것"과 "부분만 가진 것"의
  구분이 shape 수준에서 갈린다.
