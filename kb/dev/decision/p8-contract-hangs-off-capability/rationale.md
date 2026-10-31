---
id: https://agentic-knowledge-base.dev/id/chunk/89ed49c3-1dce-4dee-a038-566f05d300e6
type: decision
level: concrete
title_ko: 계약을 구현에 매달면 교체가 무해했다는 주장을 검증할 수 없다
title: A contract hung on the implementation makes the claim of a harmless swap unverifiable
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0181-contract-hangs-off-capability.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:05:23+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/bc99c810-3637-44a9-b446-350ceb648180
---
**근거** — 출처는 harness-concrete `docs/odr-contract-verify.md`다.

- 계약을 구현에 매달면 구현을 바꿀 때 계약도 따라 바뀐다. 그 순간 바뀐 것이 구현인지 기준인지를 구별할 수 없고, **교체가 무해했다는 주장을 검증할 수 없게** 된다.
- 기준이 명세에서만 오므로 판정은 **바인딩 독립**이다. 같은 계약이 서로 다른 두 구현에서 항목별로 동일한 판정을 내는 것이 기술 독립성의 유일한 실증 형태이고, 그 실험을 할 수 있어야 주장이 주장으로만 남지 않는다.
- 계약은 능력별로 선택해 붙인다(opt-in). 계약이 하나도 없는 대상은 **공허하게 통과**한다고 명시한다. 없는 계약을 있는 것처럼 세면 커버리지가 부풀고, 반대로 실패로 처리하면 아직 계약이 없는 능력을 표현할 수 없기 때문이다.
- 판정기는 명세와 산출물을 **읽기만** 한다. 어느 쪽도 고치지 않으므로 의존이 한 방향으로 남고, 판정 결과가 판정 대상을 바꾸는 순환이 없다.

이 결정은 합격 기준을 시나리오와 분리해 별도 단위 지식에 두고 `verifies` 링크에 매다는 규칙(`p8-pass-criteria`)과 같은 분리다. 그래서 무엇을 자극하는가와 무엇으로 판정하는가를 각각 제자리에 둔다.
