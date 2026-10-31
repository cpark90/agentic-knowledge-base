---
id: https://agentic-knowledge-base.dev/id/chunk/cdf76c66-5003-405d-8fc1-4fbcafb8c586
type: decision
level: concrete
title_ko: 하네스가 가진 역할마다 대응 적용 범위가 있고 그 적용 범위가 하네스에 담긴다
former_title_ko: ["하네스가 가진 역할마다 대응 스코프가 있고 그 스코프가 하네스에 담긴다"]
title: Every role a harness has owns a matching scope, and the harness holds that scope
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:43+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6c636d-2b87-4b60-b355-4ff49437f478
composite: {id: https://agentic-knowledge-base.dev/id/composite/ec6c636d-2b87-4b60-b355-4ff49437f478, title_ko: 카탈로그 완전성, title: Catalog completeness}
---
**결론** — 카탈로그(`kg/catalog-kg.ttl`)는 완전해야 한다. 하네스가 `agt:hasRole` 하는 모든 역할은 대응 적용 범위를 갖고, 그 적용 범위는 `agt:grants`로 하네스에 담겨 그 역할의 에이전트에게 주어진다.

- 대응은 슬러그로 정한다. 역할 `id:role-<x>`의 적용 범위는 `id:scope-<x>`다.
- 역할을 더하면 적용 범위도 같은 커밋에서 더한다.
- 게이트 `catalog`(`tools/validate.py`)가 이것을 강제한다. 대응 적용 범위가 없거나 그 적용 범위가 `agt:grants`로 하네스에 담기지 않으면 FAIL이다.

게이트 `catalog`(실행 계층 verify, 노트 10.2절)는 대응 적용 범위 말고도 셋을 거부한다. read 지식 종류가 0인 역할, 두 역할이 함께 가진 write 지식 종류, ODD 상한을 넘는 `maxConcurrent` 합이다. 해소는 orchestrator가 `kg/catalog-kg.ttl`이나 ODD를 고치는 것이고, 역할 표를 적은 `AGENTS.md`와 그래프를 같은 커밋에서 일치시킨다.
