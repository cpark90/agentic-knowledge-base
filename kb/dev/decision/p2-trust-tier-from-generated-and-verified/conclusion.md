---
id: https://agentic-knowledge-base.dev/id/chunk/1ed5e4cd-1ab7-4a2a-a110-7ac368e495ee
type: decision
level: concrete
title_ko: 신뢰 등급은 generated.by와 verified에서 질의로 얻고 검증 뒤에 바뀐 항목은 게이트가 거부한다
title: The trust tier is queried from generated.by and verified, and the gate rejects items changed after verification
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:30:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f
composite: {id: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f, title_ko: 신뢰 등급과 검증 시각, title: Trust tier and verification time}
---
**결론** — 신뢰 등급은 누가 만들고 누가 검증했는가다. 행위자 표기는 OKF를 따른다. 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`, 프로세스는 `process:<id>`다. 등급은 저장하지 않고 질의로 얻는다.

| 등급 | 조건 |
|---|---|
| 미검증 | `verified`가 없다 |
| 기계 확인 | `verified`가 있고 `human:` 항목이 없다 |
| 사람 검토 | `verified`에 `human:` 항목이 있다 |

shape `trust-shapes.ttl`의 검사 둘이 이 위에 선다.

- `generated.by`는 필수다. `agt:generatedBy`가 정확히 하나여야 한다. 누가 만들었는지 없는 항목은 만들 수 없다.
- `prov:generatedAtTime ≤ agt:verifiedAt`이다. 검증 뒤에 내용이 바뀌면 FAIL이다.

검증하지 않은 것을 `verified`에 적지 않는다. 미검증이 정직한 상태다. `artifact` plane의 `verified`는 사람 도장이 아니라 테스트 통과 도장이다(`p7-code-extraction-direction`).
