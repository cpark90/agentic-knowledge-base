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
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}, {by: developer/claude-opus-5-5, at: 2026-10-24T22:08:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f
composite: {id: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f, title_ko: 신뢰 등급과 검증 시각, title: Trust tier and verification time}
---
**결론** — 신뢰 등급은 누가 만들고 누가 검증했는가다. 행위자 표기는 OKF를 따른다. 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`, 프로세스는 `process:<id>`다. 등급은 저장하지 않고 질의로 얻는다.

등급은 현재 내용 이후(`at ≥ generated.at`)의 `verified` 항목만 센다. `verified`는 판정 이력이라 누적되고(`p2-judgement-history-in-verified`), 옛 내용에 찍힌 항목은 등급에 들지 않는다. 그래프의 `agt:verifiedBy`는 그 항목의 주체만 담는다.

| 등급 | 조건 |
|---|---|
| 미검증 | 현재 내용 이후의 항목이 없다 |
| 기계 확인 | 현재 내용 이후의 항목이 있고 그중 `human:` 항목이 없다 |
| 사람 검토 | 현재 내용 이후의 항목에 `human:` 항목이 있다 |

shape `trust-shapes.ttl`의 검사 둘이 이 위에 선다.

- `generated.by`는 필수다. `agt:generatedBy`가 정확히 하나여야 한다. 누가 만들었는지 없는 항목은 만들 수 없다.
- 가장 늦은 `agt:verifiedAt` ≥ `prov:generatedAtTime`이다. 검증 뒤에 내용이 바뀌고 재검증 항목이 없으면 FAIL이다. 검증 시각이 없으면 미검증이고 검사 대상이 아니다.

검증하지 않은 것을 `verified`에 적지 않는다. 미검증이 정직한 상태다. `artifact` 지식 종류의 `verified`는 사람 도장이 아니라 테스트 통과 도장이다(`p7-code-extraction-direction`).

**게이트** `shacl`(trust, 노트 2.12절 신뢰 등급) — 두 검사의 위반은 `validate`가 `FAIL [shacl]`로 낸다. 해소는 검토 뒤 재검증 항목을 `verified` 목록에 덧붙여 가장 늦은 `verified.at`이 `generated.at` 이후가 되게 하는 것이다. 목록을 덮어쓰지 않는다.
