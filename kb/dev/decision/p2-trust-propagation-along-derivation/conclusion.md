---
id: https://agentic-knowledge-base.dev/id/chunk/7ebc849c-91bf-44fa-93e4-9b9090a2ea5b
type: decision
level: concrete
title_ko: 신뢰 등급은 derives-from과 sources를 따라 전파된다
title: Trust grade propagates along derives-from and sources
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
part_of: https://agentic-knowledge-base.dev/id/composite/34cd97d1-50df-4db6-8511-fd10b918eaf3
composite: {id: https://agentic-knowledge-base.dev/id/composite/34cd97d1-50df-4db6-8511-fd10b918eaf3, title_ko: 신뢰 등급의 전파, title: Trust propagation along the derivation chain}
---
**결론** — 지금은 가정의 참거짓만 `assumes`로 전파된다. **출처의 신뢰 등급(구축 / 복원 / 외부 유입)도 `derives-from`과 `sources`를 따라 전파한다.**

외부에서 들어온 관측에서 파생된 청크가 **확정으로 승격되려면 파생 연쇄 어딘가에 사람 승인이나 검증 통과가 있어야 한다.**

이것을 2.5절 verify 질의로 쓴다 — **"확정 상태이면서 파생 연쇄 전체가 `origin:imported`인 청크"가 존재하면 실패.** 검사 게이트(행동 사영)는 민감한 행동을 판정할 때 이 등급을 참조한다.
