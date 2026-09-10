---
id: https://agentic-knowledge-base.dev/id/chunk-d0099
type: decision
level: concrete
title_ko: 제약의 출처 셋과 공리·제약·가정의 구분
title: Three constraint sources and axiom/constraint/assumption distinction
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 후보 링크를 깎는 제약의 출처는 셋으로 고정하고, **공리·제약·
가정은 서로 다른 것**으로 구분해 각각 제 위치에 둔다.

**제약의 출처** (노트 7.3절)
- **온톨로지 공리** — 예: `satisfies`의 정의역은 `contract`·`artifact`뿐.
  위치는 `*-ontology`의 `related/trace`.
- **ODD** — 예: 외부 클라이언트가 있으므로 APIKey 링크 불가.
  위치는 `project-odd`.
- **설계 공간의 국소 제약** — 예: 이 모듈에서는 동기 방식만.
  위치는 `*-space`.

**구분** (7.3절)
- **공리** = 온톨로지 수준에서 항상 성립하는 논리. `*-ontology`, `*-rules`.
- **제약** = 특정 설계 공간에서 후보 링크를 깎는 양립 조건. `*-space`, ODD.
- **가정** = 그 제약 자체가 성립하기 위한 전제. `assumes` 링크.
