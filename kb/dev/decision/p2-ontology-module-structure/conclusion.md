---
id: https://agentic-knowledge-base.dev/id/chunk/bb57dfa0-e134-40b7-bbcf-10325fe59a3d
type: decision
level: concrete
title_ko: entity/related와 어휘/형식화로 나눈 모듈을 최상위가 import한다
title: Modules split by entity/related and vocabulary/rules, imported by a thin top
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0048]
part_of: https://agentic-knowledge-base.dev/id/composite/301046f4-6db7-42f5-aea0-ffe4599d4a15
composite: {id: https://agentic-knowledge-base.dev/id/composite/301046f4-6db7-42f5-aea0-ffe4599d4a15, title_ko: 온톨로지의 모듈 구조, title: Ontology module structure}
---
**결론** — 온톨로지는 단일 파일이 아니라 **모듈로 나누고 최상위에서 import하여 합친다.** `project-ontology`는 import만 하는 얇은 최상위다.

- `upper` — 상위 온톨로지 (외부, **수정 금지**)
- `entity/` — plane으로 분류되는 개념. knowledge-item · requirement · decision · contract · schema · artifact · annotation · memory
- `related/` — plane으로 분류되지 않는 횡단 개념. condition(ODD 어휘) · scope · assumption · workset · revision · trace · channel · policy · harness
- `vv/` — V&V KB의 plane 실체 (7.2절), `profile/` — 도메인 프로파일 (2.11절)
- `defect` / `defect-rules` — 결함 어휘와 결함 형식화

**두 분리가 핵심이다.** (a) **entity / related** — 스코프·가정·채널·정책·하네스는 어느 plane에도 속하지 않고 모든 plane과 상호작용한다. (b) **어휘 / 형식화** — 개념과 포섭 관계는 `defect`에, 실행 기록에서 결함을 추론하는 규칙은 `defect-rules`에 둔다.

**경계 규칙** — 모듈은 서로를 import할 수 있어도 다른 모듈의 개념을 정의해 넣을 수 없다. **코어 + 확장** — 확장은 새 모듈 추가로만 하고 기존 모듈을 수정하지 않는다.
