---
id: https://agentic-knowledge-base.dev/id/chunk/97dca3e0-2cb6-47e6-a99c-72055dbc1792
type: decision
level: logical
title_ko: 커뮤니티의 자동 채택과 탐지 없음은 둘 다 기각된다
title: Both automatic adoption of communities and no detection are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T00:50:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/165ef75a-d4f3-4de2-aba2-ea3a8efb787a
---
**대안** —

- **커뮤니티를 복합체로 자동 채택한다** — 기각. 구조 밀도가 의도(함께 읽힘·순서)를 대신하게
  되어 근거 없는 할당이 되고, 동질성 규칙을 넘는 군집이 복합체로 들어온다.
- **탐지를 두지 않고 복합체를 손으로만 찾는다** — 기각. 청크가 수백을 넘으면 "통합이 필요한
  것"을 사람이 전수로 살필 수 없다 — 고아율은 재지만 과분할은 아무 지표도 잡지 못한다.
- **커뮤니티를 복합체 대신 링크(`relatedTo`)로만 쓴다** — 보류. plane을 넘는 군집에는 이것이
  맞고, 같은 plane·level 안의 군집은 복합체 후보가 더 정확하다 — 결론은 둘을 나눈다.
