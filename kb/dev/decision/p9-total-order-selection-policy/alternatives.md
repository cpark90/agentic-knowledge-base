---
id: https://agentic-knowledge-base.dev/id/chunk/a038e9ec-5d1d-4930-80ff-049ee154332d
type: decision
level: concrete
title_ko: 사람의 확인을 기다리는 안은 택하지 않는다
title: Waiting for human confirmation is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0176-deterministic-selection-policy.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:51:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:51:27+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/edb7941d-bfc4-43d0-84ce-b2201e7fddb1
---
**대안** — 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 사람의 확인을 기다린다 | 무인 재생성 경로에서는 불가능하다. 미확정을 **표현**하는 것은 후보 집합(`p9-possibility-as-feasible-set`, `p9-csp-mapping-of-links`)의 일이고, 그 위에서 답을 내는 선택 정책은 별개의 층이다. 그래서 후보를 남기는 것과 자동으로 고르는 것은 충돌하지 않는다 |
