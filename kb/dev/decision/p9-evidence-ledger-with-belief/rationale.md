---
id: https://agentic-knowledge-base.dev/id/chunk/a1f1f37b-225c-4bea-8d76-c7e1f074c3d4
type: decision
level: logical
title_ko: 확정은 검사 가능한 규칙에 두고 믿음 정도는 보정될 때까지 곁에 둔다
title: Settlement stays with checkable rules; belief stays alongside until calibrated
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T15:49:15+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/724d0dfe-3f2e-4bc6-bf43-8a3580b089d7
---
**근거** — 유저는 지식 베이스 자체의 확률화를 골랐다(Q87-b). 그러나 확률을 보정할 빈도가 아직 없다는 노트 9.2절의 옛 근거는 측정으로도 그대로다. 증거 1,212건이 모두 지지이고 반박은 설계 공간의 5건, 사람 정답 라벨은 10건이었다(2026-10-22). 그래서 상태 전이, 곧 확정의 권한은 재검증 가능한 증거 기록 규칙에 남긴다. 믿음 정도는 병기하고 선호를 돕는다(Q90-a). 여기서 선호를 돕는다는 것은 개정된 `p9-preference-partial-order`가 정한 대로 부분순서에서 순서가 없는 두 후보의 동률을 깨는 일이다(Q109-b). 반박 증거 경로와 사람 라벨(Q91)이 차면 그 보정이 상태 전이에 들어올 수 있는지를 다시 묻는다.

**개정** — 유저는 증거 종류에 유저 결정을 더했다(유저 결정 Q-0055 Q111-a, 2026-10-24). 설계 공간의 확정 후보는 유저 답으로 정해지는데, 그 답을 적을 종류가 없어 확정 후보 넷이 자기 자신을 근거로 가리켰기 때문이다. 유저 결정을 서열의 맨 앞이 아니라 서열 밖의 확정 권한으로 둔 것은 `p10-candidate-and-confirmed-link`가 확정을 유저 또는 위임된 에이전트의 확인으로 정했기 때문이다. 서열은 확정 근거가 없을 때 후보를 정렬하는 기본 선호이고, 유저의 확인은 정렬이 아니라 확정 자체다. 판정은 유저가 언어모델의 셋째 자리로 더한 것이다(유저 결정 Q-0056 Q118-a, 2026-10-24). 다만 판정을 공동 커버 다음, 임베딩 앞에 두는 서열의 자리는 orchestrator의 제안이고 유저에게 묻지 않았다.
