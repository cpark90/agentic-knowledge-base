---
id: https://agentic-knowledge-base.dev/id/chunk/3ab6d43d-0193-4275-bb9f-5246da93b88a
type: agt:Space
level: logical
title_ko: 청크 상한의 컨텍스트 예산 전제가 실측으로 성립하는가
title: Whether the context-budget premise of the chunk limit holds under measurement
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T01:15:39+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 청크 상한은 에이전트가 한 번에 파악하는 맥락의 예산과 그중 지식 본문은 잔여라는 전제 위에 있다. 예산 5,418 토큰은 옛 200줄의 환산이고 저작 산문 상한 1,092 토큰은 그 1/5이다(원문은 200줄·42줄로 물었다). 하네스 지시·작업 집합·툴 출력·대화 이력이 실제로 얼마를 차지하는지 재지 않으면 상한이 맞는지, 더 작아야 하는지, 상한 자체가 무의미한지 알 수 없다. 요구 `r-014`에서 이 전제를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — 예산은 다섯 항목이고 항목마다 통제 수단이 있으며 지식 본문만 잔여다(`p1-context-budget-items`). 실측 필요는 그 결정의 미확정에 남아 있다. 툴 출력은 라벨 목록이 기본인 읽기 응답이(`p5-plane-assignment-tool-surface`), 대화 이력은 스코프로 거른 작업 집합만 전달하는 dispatch가(`p11-execution-mode-and-workset`) 통제한다. 단위는 토큰이고 예산과 상한은 옛 도출(예산 ÷ 5)을 고정해 환산한 값이며 줄 유지안은 기각됐다(`p1-chunk-unit-is-tokens`).

현재 상태(2026-10-05 실측, 계수기 `o200k_base`) — orchestrator 세션의 하네스 지시는 `CLAUDE.md` 777 · `AGENTS.md` 5,905 · `STYLEGUIDE.md` 13,419 · 역할 정의 1,788로 21,889 토큰이고 예산의 4.0배다. 앵커 없는 developer 작업 집합 뷰는 59,914 토큰으로 예산을 넘고 앵커를 준 vnv 뷰는 1,978 토큰이다. 앵커별 작업 집합의 예산 준수율은 역할별 97.5~97.8%다. 툴 출력과 대화 이력은 잰 기록이 없다. 살아 있는 청크 2,251개 중 본문이 상한의 9/10을 넘는 것은 12개(0.5%)다.

답이 가르는 것 — 상한 1,092 토큰의 근거가 유지되는지가 갈린다. 예산 5,418 토큰을 컨텍스트 창과 다른 것, 즉 한 판단에 조망하는 단위로 정의해야 하는지도 갈린다.

선택지 — A는 하네스 지시부터 압축하고 항목별로 재는 안이다(`p1-budget-measure-items-first`). B는 예산을 조망 단위로 재정의해 컨텍스트 창과 분리하는 안이다(`p1-budget-redefined-as-view-unit`). C는 실측 없이 상한을 유지하는 안이고 근거가 경험칙에 머문다(`p1-budget-limit-kept-unmeasured`). 관련 결정은 `p1-chunk-unit-is-tokens`다. 그 결론은 예산을 옛 200줄의 환산으로 얻었다고 적고 예산을 조망 단위로 재정의하는 문장을 적지 않는다. 그 대안 청크가 기각한 것은 줄 단위 유지이고 실측 없는 상한 유지가 아니다. 그래서 두 청크를 B의 확정이나 C의 배제로 들지 않는다(Q65-b). 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/156bd463-2ceb-42ec-af19-e8e2abb4dc32
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/952def48-656a-4710-a506-c88d20c1468d
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/ae62aa1a-37da-47e5-9076-c837fa67d674
    state: open
```
