---
id: https://agentic-knowledge-base.dev/id/chunk-d0181
type: decision
level: concrete
title_ko: 계약은 구현이 아니라 능력에 매단다
title: Contracts hang off the capability, not the implementation
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-harness-recipes]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 산출물의 합격 기준(계약)은 그것을 실현한 **구현이 아니라 명세
쪽 능력(capability)** 에 매단다. 어느 구현이 그 능력을 실현하든 판정
기준이 같아지고, 구현 교체가 판정 결과를 바꿀 수 없다.

**근거** (harness-concrete docs/odr-contract-verify.md)
- 계약을 구현에 매달면 구현을 바꿀 때 계약도 따라 바뀐다. 그 순간 "바뀐
  것이 구현인가 기준인가"를 구별할 수 없고, **교체가 무해했다는 주장이
  검증 불가능**해진다.
- 기준이 명세에서만 오므로 판정은 **바인딩 독립**이다. 같은 계약이 서로
  다른 두 구현에서 항목별로 동일한 판정을 내는 것이 기술 독립성의 유일한
  실증 형태다 — 그 실험을 할 수 있어야 주장이 주장으로 남지 않는다.
- 계약은 능력별 opt-in이다. 계약이 하나도 없는 대상은 **공허하게 통과**
  한다고 명시한다 — 없는 계약을 있는 것처럼 세면 커버리지가 부풀고,
  반대로 실패로 처리하면 아직 계약이 없는 능력을 표현할 수 없다.
- 판정기는 명세와 산출물을 **읽기만** 한다. 어느 쪽도 고치지 않으므로
  의존이 한 방향으로 남고, 판정 결과가 판정 대상을 바꾸는 순환이 없다.

**이 저장소와의 관계** — 합격 기준을 시나리오와 분리해 별도 청크에 두고
`verifies` 링크에 매다는 규칙(d-0136)과 같은 분리다. 무엇을 자극하는가와
무엇으로 판정하는가를 각각 제 자리에 둔다.
