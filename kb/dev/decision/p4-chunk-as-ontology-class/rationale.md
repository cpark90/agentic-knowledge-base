---
id: https://agentic-knowledge-base.dev/id/chunk/e9c81f92-b685-49ff-ba97-29641ccd945d
type: decision
level: logical
title_ko: 42줄은 200줄 컨텍스트의 1/5이고 청크는 네 분야의 합류점이다
title: 42 lines is one fifth of the 200-line context; four fields converge on the chunk
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/dd76498b-2cca-4b79-a1fe-ce5a4d33c0ca
---
**근거** (노트 4.1절)

- **42줄** — 1.1절 컨텍스트 한계 200줄의 약 1/5. 에이전트가 한 번에 4~5개
  청크를 조망할 수 있는 크기로 잡은 값이다.
- **지어내지 않는다** — 정보를 담는 인공물이 무엇인지는 상위 온톨로지가 이미
  정의했으므로 그 하위 클래스로 두기만 한다.
- 같은 개념이 네 분야에서 독립적으로, 이름까지 같게 정립되었다. 각 분야의
  장치가 이 체계의 다른 부품으로 흡수된다.

| 분야 | 이름 | 흡수된 곳 |
|---|---|---|
| 인지과학 | chunk (7±2) | 42줄과 구성 상한(4.5절)의 근거 |
| 구조적 글쓰기 | information block | 청크 shape (4.4절) |
| 문학적 프로그래밍 | chunk | 뷰 질의 (4.6절) |
| 모듈형 문서 | topic | plane 하위 클래스 (4.2절) |

- `Chunk`와 `Composite`를 disjoint로 두면 "본문을 가진 것"과 "부분만 가진 것"의
  구분이 shape 수준에서 갈린다.
