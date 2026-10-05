---
id: https://agentic-knowledge-base.dev/id/chunk/cdf76c66-5003-405d-8fc1-4fbcafb8c586
type: decision
level: concrete
title_ko: 하네스가 가진 역할마다 대응 스코프가 있고 그 스코프가 하네스에 담긴다
title: Every role a harness has owns a matching scope, and the harness holds that scope
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:33:13+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6c636d-2b87-4b60-b355-4ff49437f478
composite: {id: https://agentic-knowledge-base.dev/id/composite/ec6c636d-2b87-4b60-b355-4ff49437f478, title_ko: 카탈로그 완전성, title: Catalog completeness}
---
**결론** — 카탈로그(`kg/catalog-kg.ttl`)는 완전해야 한다. 하네스가 `agt:hasRole` 하는 모든 역할은 대응 스코프를 갖고, 그 스코프는 `agt:grants`로 하네스에 담겨 그 역할의 에이전트에게 주어진다.

- 대응은 슬러그로 정한다. 역할 `id:role-<x>`의 스코프는 `id:scope-<x>`다.
- 역할을 더하면 스코프도 같은 커밋에서 더한다.
- 게이트 `catalog`(`tools/validate.py`)가 이것을 강제한다. 대응 스코프가 없거나 그 스코프가 `agt:grants`로 하네스에 담기지 않으면 FAIL이다.
