---
id: https://agentic-knowledge-base.dev/id/chunk/5eedadfc-b34b-4634-9701-aefb9fbbbd66
type: decision
level: logical
title_ko: 후보가 여럿인 상태가 정상이고 임의 선택이 자료구조에서 막힌다
title: Multiple candidates are the normal state; arbitrary choice is structurally blocked
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/aa7d5c28-822d-4904-9e3f-13920eb41256
---
**근거** (노트 8.3·8.5절) — 이 사상이 주는 것.

**(a) 과도한 추측이 자료구조 수준에서 막힌다.** 후보 링크가 여럿인 상태가 정상이고, 확정은 제약 전파가 나머지를 기각했을 때만 일어난다. 에이전트가 최유력 후보를 임의로 고르는 일이 구조적으로 불가능해진다.

**(b)** 값과 링크의 이중 관리가 사라지고, 후보·확정 메커니즘(9.4절)이 미확정 전반에 재사용된다.

**(c)** 모호성 시각화(12.1절)의 계산이 **후보 링크 수**라는 한 숫자가 된다.

**(d)** 판정 근거 문제가 "성립 가능한가"로 좁혀진다 (9.8절).

**(e)** 기성 솔버·전파 알고리즘을 그대로 쓸 수 있다.
