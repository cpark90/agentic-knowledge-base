---
id: https://agentic-knowledge-base.dev/id/chunk/7ebc849c-91bf-44fa-93e4-9b9090a2ea5b
type: decision
level: concrete
title_ko: 신뢰 등급은 derives-from과 sources를 따라 전파된다
title: Trust grade propagates along derives-from and sources
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
part_of: https://agentic-knowledge-base.dev/id/composite/34cd97d1-50df-4db6-8511-fd10b918eaf3
composite: {id: https://agentic-knowledge-base.dev/id/composite/34cd97d1-50df-4db6-8511-fd10b918eaf3, title_ko: 신뢰 등급의 전파, title: Trust propagation along the derivation chain}
---
**결론** — 지금은 가정의 참거짓만 `assumes`로 전파된다. **출처의 신뢰 등급(구축 / 복원 / 외부 유입)도 `derives-from`과 `sources`를 따라 전파한다.**

외부에서 들어온 관측에서 파생된 단위 지식이 **확정으로 승격되려면 파생 연쇄 어딘가에 사람 승인이나 검증 통과가 있어야 한다.**

이것을 2.5절 verify 질의로 쓴다 — **"확정 상태이면서 파생 연쇄 전체가 `origin:imported`인 청크"가 존재하면 실패.** 검사 게이트(행동 사영)는 민감한 행동을 판정할 때 이 등급을 참조한다.

**게이트** (노트 4.3절, 2.12절, verify) — 질의 `sources-empty.rq`가 `sources`가 빈 단위 지식을, `imported-chain-confirmed.rq`가 파생 연쇄 전체가 외부 유입인 확정 단위 지식을 거부하고 게이트 id는 `verify`다. 해소는 저작자가 `sources`를 보강하는 것이다.
