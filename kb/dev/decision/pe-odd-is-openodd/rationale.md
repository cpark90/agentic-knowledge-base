---
id: https://agentic-knowledge-base.dev/id/chunk/cbc3be30-e73f-4e88-b375-ffd58b0f4119
type: decision
level: logical
title_ko: ODD 의미론을 표준에 맡기면 시나리오 변수와 후보 경계가 공짜로 따라온다
title: Delegating ODD semantics to the standard gives scenario variables and candidate bounds for free
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/f867e42b-0106-4796-8861-4bdc493e15db
---
**근거** (노트 부록 E.4·E.5, 3.3절, 9.10절) — OpenODD 모듈 → `keep()` 내보내기가 3.3절 "시나리오 변수는 ODD 속성"의 표준 구현이고, Range·bound가 후보 집합의 바깥 경계(9.10절)다. 이탈의 의미론(COD ∉ ODD)을 표준이 정의하므로 이 체계는 판정 방법(`checks`)과 명시 제외 기록만 더한다 — `any`/`unknown`과 `exclude_when_unknown`이 6.5절 unverified·restrictive에 그대로 대응한다.
