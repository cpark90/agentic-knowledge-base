---
id: https://agentic-knowledge-base.dev/id/chunk/26cc408f-b53a-4c2e-8ac7-57bde2d2f1c8
type: decision
level: logical
title_ko: 산문에만 있는 규칙은 데이터와 어긋나도 아무도 모른다
title: A rule that lives only in prose can disagree with the data and nobody notices
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-26T16:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/fc9c449c-45c7-4951-929d-b201dd7c2d45
---
**근거** — 2026-09-26 실측이 세 가지를 보였다.

`agt:DesignDecision`의 정의 "기여 없는 설계는 거부된다"는 첫 실측에서 762건 중 759건이 `serves`를 갖지 않아 어긋난 것으로 보였다. 그러나 기여는 `refines ∪ serves`로 요구에 닿는 것이고 759건은 `refines`로 닿는다 — 여집합 질의 CQ-37이 0행이다. 문장이 `serves` 하나로 읽히게 쓰여 있어 실측을 오독하게 만든 것이 문제였다. `agt:supersedes`의 "옛 결정을 충족하던 링크가 전부 suspect가 된다"도 `supersedes` 135건이 있으나 `suspect`는 실물 0이다.

둘째, **같은 문장이 두 가지로 읽힌다.** 복합체의 "부분 수준 동일"은 문언대로면 위반 406쌍이고 시행된 대로면 0건이다. verify 질의 파일의 2026-09-13 주석이 "결정 복합체 188/188이 걸려 범위를 좁혔다"고 적었다 — 데이터에 맞춰 규칙을 좁혔는데 정의문은 그대로였다. 읽기가 갈리는 문장은 사람도 문장만으로 고르지 못한다.

셋째, 실행되지 않는 규칙의 절반은 **한 지점**에서 멈춰 있다. `chunk2kg`가 모든 링크를 `confirmed`로만 내므로 상태 전이를 말하는 정의문 8건이 한 번도 돈 적이 없다. 그것은 정의문 8건의 문제가 아니라 링크 상태 유도 하나의 문제이고, 정의문에 자리를 적어 두면 그 하나가 켜질 때 8건이 함께 실행된다는 사실이 드러난다.

정의문에 자리를 적게 하는 까닭은 `r-016`("편집은 게이트가 판정한다")이다. 게이트가 판정하지 않는 규칙은 요구가 아니라 희망이고, 어느 게이트인지 적혀 있지 않으면 그것이 판정되는지 확인할 길이 없다.
