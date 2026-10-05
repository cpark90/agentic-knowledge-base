---
id: https://agentic-knowledge-base.dev/id/chunk/da052bc7-f604-4c8d-9324-ddd5251e0474
type: decision
level: logical
title_ko: 둘째 수준이 코어에 있어야 갈래별 커버리지를 셀 수 있고 제안 큐가 그 목록을 승인 아래에서 늘린다
title: A core second level is what makes per-branch coverage countable, and the proposal queue grows that list under approval
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:13:20+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4f241f3b-cc00-43cb-b95e-bf55e145270e
---
**근거** (노트 0.4절, 3.9절) — 세 갈래와 판정 등급의 근거는 옛 결정에서 그대로 승계한다.

- 둘째 수준을 코어에 두면 ODD 속성이 빠짐없이 분류되어 **갈래별 커버리지를 셀 수 있다.** 셋째 수준까지 코어에 두면 프로젝트마다 맞지 않아 강제가 깨진다.
- 판정 등급을 하위 분류마다 붙이는 이유는 ODD 이탈 감지의 실효성이 등급의 분포로 결정되기 때문이다. 대부분 A(기계 판정)지만 코딩 규약은 B(린터), 아키텍처 스타일과 외부 행위자는 C다.
- 시간 제약이 동적 갈래에 들어온 것은 0.5절이 시간열 개체를 없앤 결과다. 선행·배타·시한을 형식화할 자리가 ODD 어휘밖에 남지 않았고, 판정은 실행 기록의 시각 순서로 하므로 등급 A다.
- 환경 조건의 "시간"(시간대·배포 창·마감)과 동적 요소의 "시간 제약"은 다른 개념이다. 전자는 밖에서 주어지는 조건, 후자는 작업 간 순서·배타 요구다.

둘째 수준을 확장 가능으로 바꾸는 근거는 둘이다.

- 노트 0.4절 `[확정]` 원문이 "목록은 확장 가능하되 셋째 수준 이하는 프로젝트별로 둔다"이다. 옛 결론의 "고정"은 이 문장과 반대였고, 1-② 충실도 감사(2026-10-03)가 이 문장 하나를 판정 불가로 남겼다.
- 유저가 Q11에서 제안 큐 경유 확장을 골랐다. 확장은 승인을 거치므로 코어 목록이 커버리지 계산의 기준으로 남는다. 제안 큐는 에이전트가 어휘를 직접 고치지 않게 하는 기존 경로다(`p2-term-proposal-workflow`).
