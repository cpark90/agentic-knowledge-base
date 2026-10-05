---
id: https://agentic-knowledge-base.dev/id/chunk/cd539cfa-297e-4adb-b0c4-62d713a0882c
type: decision
level: logical
title_ko: 정의문을 순수 서술로 비우거나 전부 공리로 옮기거나 그대로 두는 안은 기각된다
title: Emptying definitions to pure description, moving everything to axioms, and leaving them are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-05T00:30:10+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T00:30:20+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/fc9c449c-45c7-4951-929d-b201dd7c2d45
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 정의문에서 규칙 문장을 전부 빼고 서술만 남긴다 | `STYLEGUIDE.md` §1이 정의에 "왜 존재하고 언제 쓰는가"를 적으라고 정한다. 규칙이 곧 그 답인 개념이 많다. 빼면 정의가 재진술이 된다 |
| 규칙 전부를 OWL 공리로 옮긴다 | 수준 한 단계·토큰 상한·닫힌 어휘는 OWL로 표현되지 않고 shape·질의·분석 시점의 것이다. 의미 판정과 시점 비교는 어디로도 옮길 수 없다 |
| 그대로 둔다 | 실측이 보인 상태다 — `serves` 99.6% 어긋남을 아무도 모른 채 지났다 |
| 데이터에 맞춰 문장을 약화한다 | 두 가지로 읽히는 문장 둘 중 하나(복합체 수준)는 그렇게 했고 그것이 시행된 읽기다. 그러나 `assumes`의 "유일한 링크"는 데이터가 아니라 좁은 읽기가 맞다. 어느 쪽이 맞는지는 문장마다 판정할 일이고 일괄로 정하지 않는다 |
