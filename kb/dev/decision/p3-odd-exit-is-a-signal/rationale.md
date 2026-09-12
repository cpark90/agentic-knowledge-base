---
id: https://agentic-knowledge-base.dev/id/chunk/46f8ee85-30f8-48f6-9000-85dcbfcd230f
type: decision
level: logical
title_ko: 설계 조건과 실행 조건은 어긋나며 그 어긋남이 정보다
title: Design and runtime conditions diverge, and the divergence is information
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ce551363-f48f-40a3-95f8-b35a0ddd377d
---
**근거** (노트 3.5절) — 설계 시점 조건이 실행 시점에도 참이라는 보장은 없다. 어긋남을 결함으로 처리하면 은폐 유인이 생기지만, 신호로 처리하면 그것이 3.6절 확장의 입력이 된다.

무효화 범위가 가정 위반보다 넓은 것이 이 신호의 무게다 — ODD 속성 하나에는 스코프·가정·기준·케이스가 함께 매달려 있다. 그래서 기본 대응이 자동 복구가 아니라 중단과 에스컬레이션이다.

전수조사 없이 무효화 대상을 고를 수 있는 것은 그 속성을 참조하는 항목이 링크로 이미 드러나 있기 때문이다.
