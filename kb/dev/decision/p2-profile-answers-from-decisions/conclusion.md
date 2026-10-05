---
id: https://agentic-knowledge-base.dev/id/chunk/5cbd9aae-f117-4cfe-a4c0-9781137a95a8
type: decision
level: concrete
title_ko: 프로파일의 확장점마다 답은 결정에서 읽고 결정이 없으면 결정을 먼저 만든다
title: Each profile extension point takes its answer from a decision, and a missing decision is made first
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:22:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2b47645a-4247-4eb8-a741-7a7a41d206cf
composite: {id: https://agentic-knowledge-base.dev/id/composite/2b47645a-4247-4eb8-a741-7a7a41d206cf, title_ko: 프로파일의 답은 결정에서 온다, title: Profile answers come from decisions}
---
**결론** — 프로파일을 구축할 때 코어가 열거한 확장점(`p2-skeleton-and-domain-profile` 표)마다 그 답을 **결정에서 읽는다.** 답을 주는 결정이 없으면 모듈에 적기 전에 **결정을 먼저 만들고**, 그 결정은 유저 승인을 거친다.

- 개발 프로파일의 원천은 `p7-dev-plane-substance`(실체·판정 도구·EARS 패턴)와 `pe-anchor-is-bazel-label`(앵커 해석기)이다.
- 이 단계는 프로파일 구축 절차의 둘째 단계다. 확장점 열거 다음이고 모듈 작성 앞이다.
- 결정의 승인은 `decision` plane의 판정 방식(`p7-dev-plane-substance` — 논증 구조 검사 + 유저 승인)을 따른다. 이 결정은 승인 절차를 새로 정하지 않는다.
