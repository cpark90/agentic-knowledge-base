---
id: https://agentic-knowledge-base.dev/id/chunk/8f1a0310-bc32-4cfd-a35e-575068d96699
type: decision
level: logical
title_ko: v1의 scene·situation·scenario 3분리 폐기
title: The v1 scene, situation, scenario split is retired
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/52124ca7-97f8-4b5e-818f-1574ab131484
---
**대안** — **v1의 scene·situation·scenario 3분리는 폐기되었다.** 관측자 관점의
유무로 세 시간열 개체를 두던 안(scene = 시점 스냅샷, situation = 스코프로 거른
부분, scenario = scene의 시간열 + 행동 + 트리거)은 v3에서 쓰지 않는다.

폐기 사유와 자리 이동:

- scene은 상태를 개체로 열거하는 안이라 위 근거의 비용을 그대로 받는다. 그
  자리는 저장하지 않는 식별자인 **리비전**이 대신한다.
- situation은 인지 측정의 단위였으나, 같은 역할을 스코프 × level 창의 질의
  결과인 **작업 집합**이 맡는다. 질의로 두면 창을 바꿔 다시 잴 수 있다.
- scenario는 개발 KB에서 사라지고 **V&V KB의 `decision` plane 청크**(자극
  명세)로 옮겼다 (0.0절 용어표, Part VIII).

**대안** — 스냅샷을 저장하되 차분만 보관하는 안. 기각 — 차분 연쇄는
`prov:wasRevisionOf`가 이미 제공하고, 그 위에 스냅샷 개체를 얹으면 두 개의
시간 표현이 공존하게 된다.
