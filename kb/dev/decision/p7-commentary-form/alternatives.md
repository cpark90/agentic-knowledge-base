---
id: https://agentic-knowledge-base.dev/id/chunk/a5c4792e-7e54-40c3-9a33-47b1164ccbf4
type: decision
level: logical
title_ko: 자유 서술 주석·전부 차단·심각도 숫자 안은 기각된다
title: Free-form comments, blocking everything, and numeric severity are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-26T15:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/54cd62d1-0efa-4a35-b379-20d8880cc3be
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 라벨 없이 자유 서술로 쓴다 | 행동의 크기를 읽는 쪽이 추측한다. 집계도 불가능하다 |
| 모든 주석이 게이트를 막는다 | 리뷰가 병목이 된다. 칭찬과 취향까지 진행을 막는다 |
| 심각도를 숫자(1~5)로 매긴다 | 숫자는 사람마다 다른 지점에서 갈린다. 판정자 척도를 상황으로 적게 한 `p8-judge-question-form`과 같은 이유로 기각한다 |
| 라벨 어휘를 이 저장소가 새로 만든다 | 지어낸 용어를 쓰지 않는다(§0). Conventional Comments가 같은 자리를 이미 덮는다 |
