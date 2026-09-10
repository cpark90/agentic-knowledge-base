---
id: https://agentic-knowledge-base.dev/id/chunk/b71b1baa-9d02-4d6f-b152-7a8a292637c1
type: decision
level: concrete
title_ko: V&V KB는 골격의 두 번째 인스턴스다 — 새 plane을 만들지 않는다
title: The V&V KB is a second instance of the skeleton - no new planes
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
part_of: https://agentic-knowledge-base.dev/id/composite/8348f42d-da82-4b6f-b1a0-d31a93ff3d65
composite: {id: https://agentic-knowledge-base.dev/id/composite/8348f42d-da82-4b6f-b1a0-d31a93ff3d65, title_ko: V&V KB의 plane 실체, title: What each plane means in the V&V KB}
---
**결론** — V&V KB는 골격의 **두 번째 인스턴스**다. 일곱 plane의 판정 방식은 같고 실체만 다르다. **새 plane을 만들지 않는다.**

- `requirement` → **검증 목표** — 무엇이 보여져야 하는가. 요구에서 `derives-from`. 합의로 판정
- `decision` → **시나리오** — 어떤 자극으로, 왜. 논증 + ODD 정합
- `contract` → **합격 기준** — 판정식. verifier와 대상 사이의 계약. 형식 검사
- `schema` → **케이스 데이터 형식** — 자극·기대값의 구조. 스키마 검사
- `artifact` → **verifier** — 케이스를 실행해 기준을 적용하는 산출물. 실행
- `annotation` → **판정 논평** — 결함 분류, 이탈 기록. 해소로 판정
- `memory` → **실행 기록** `agt:Run` — 관측, append-only
