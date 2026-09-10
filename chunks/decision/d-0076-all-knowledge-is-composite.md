---
id: https://agentic-knowledge-base.dev/id/chunk-d0076
type: decision
level: concrete
title_ko: 모든 지식 항목은 청크의 구성체다
title: Every knowledge item is a composite of chunks
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 이 체계에 "청크가 아닌 지식 항목"은 없다. 모든 지식 항목은
청크이거나 청크의 구성체다. 결정은 결론·근거·대안 세 `agt:DecisionChunk`의
구성체, 모듈은 함수 청크의 순서 있는 구성체, 스키마는 필드 청크의 순서
없는 구성체, 시나리오는 scene 청크의 `co:List`, ODD는 절 구성체의
구성체, 실행 기록은 관측 청크의 시간순 구성체, 온톨로지 모듈은 개념 정의
청크의 구성체다.

**근거** (노트 4.7절)
- 지식 항목마다 다른 구조를 두면 저장·질의·검사가 항목 수만큼 늘어난다.
  하나의 구조 모델(청크 + `part-of` + 순서)로 전부 표현하면 shape 하나,
  질의 하나가 모든 항목에 적용된다.
- 시그니처처럼 대부분 청크 하나로 끝나는 항목도 있다 — 구성체를 강제하는
  것이 아니라 **청크가 최소 부품임을 강제**하는 것이다.

**개발 프로파일에서 함수 = 청크가 코드 품질을 강제한다.** 42줄을 넘는
함수는 `agt:ChunkShape`를 통과하지 못하므로 분할 대상이 된다. 코드 길이
규칙을 따로 두는 것이 아니라 shape의 귀결로 나온다.
