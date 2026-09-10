---
id: https://agentic-knowledge-base.dev/id/chunk/39b345d8-1e30-4562-b1af-fd06c950b2bc
type: decision
level: concrete
title_ko: 실행 기록과 검증 산출물은 태그 집합으로 분류한다
title: Run records and V&V artifacts are classified by tag sets
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0012]
part_of: https://agentic-knowledge-base.dev/id/composite/49901d72-dedc-4f2c-a4ca-5ab543eea90c
composite: {id: https://agentic-knowledge-base.dev/id/composite/49901d72-dedc-4f2c-a4ca-5ab543eea90c, title_ko: 분류는 계층이 아니라 태그로 한다, title: Classification is by tags, not a hierarchy}
---
**결론** — 실행 기록과 검증 산출물의 분류는 **계층이 아니라 태그**로 한다.
태그는 메타 속성이고 범주는 태그 집합이다. 범주는 서로 배타적일 필요가 없고,
태그 집합의 포함 관계가 범주의 포함 관계가 된다.

**태그는 범주를 갖고, 태그 값은 온톨로지 개념이어야 한다.** 범주 없이 두면
태그가 무한히 늘고 검색이 불가능해진다. 범주와 값의 출처는 다음과 같다.

- **행위자** — 에이전트 카탈로그 역할·유저·외부 서비스 (`role:developer`)
- **조건** — ODD 속성과 값 (`env:offline`)
- **목적** — 고정 어휘 (regression / exploration / acceptance / performance /
  recovery)
- **결함 요인** — `defect` 어휘 (`factor:interaction/timing`)
- **출처** — 고정 어휘 (observed / designed / imported)
- **ODD 관계** — 고정 어휘 (inside / boundary / outside, 3.3절)
- **환경** — 검증 환경 계층 (unit / model / sil / hil / staging /
  production, 7.9절)
- **대상** — 고정 어휘 (product / agent)
- **level** — 계층 (`level:logical`)

**범주 자체의 추가는 온톨로지 확장이고, 태그 값의 추가는 그 범주의 출처 어휘
확장이다.**
