---
id: https://agentic-knowledge-base.dev/id/chunk/602ace1f-da3e-411a-84a5-e86d54a3320a
type: norm
level: logical
title_ko: docs/rules.md 절 development의 이어짐 — 추출 범위와 정의 사이의 호출, 개발 KB 규칙 표
former_title_ko: ["docs/rules.md 절 development의 이어짐 — 정의 사이의 호출과 개발 KB 규칙 표"]
title: docs/rules.md development section continued — extraction range, calls between definitions, and the development KB rule table
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-28T17:24:31+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9740d5da-ea8e-4ebd-8e50-1e287cdba400
continues: true
form: table
columns: [규칙, 내용, 결정]
link_column: 결정
items: [p7-dev-plane-substance#3, p7-alternatives-mandatory#2, p7-decision-spans-three-levels#1, p6-transition-gates#1, p7-contract-first#1, p7-schema-derivation#1, p6-executable-splits-by-kb#1, p7-developer-requires-concrete#1, p7-decision-supersession#1, p7-dev-kb-completion#1, p7-dev-roles-and-scopes#1]
---
**추출할 파일은 원리가 정하고 목록은 그 실현이다** (유저 답 Q192-a, [`p7-extraction-range-by-principle`](../../decision/p7-extraction-range-by-principle/conclusion.md)).
규칙을 강제하거나 질의로 답하는 코드 파일은 추출하고, 빌드 배선과 시험, 하네스 운영 스크립트는 추출하지 않는다. 그 실현이
`defs/kb.bzl`의 `EXTRACTED_SOURCES`와 `EXTRACTED_QUERY_DIRS`, `EXTRACTED_STARLARK`이다. `EXTRACTED_SOURCES`는 `RESIDENCY`와
같은 해법으로 둔 단일 정의 위치다(2026-10-01). `BUILD.bazel`은 그 리터럴을 load하고 `kb_lib.load_extracted_sources`가
`ast.literal_eval`로 읽으므로 상수를 둘로 두지 않는다. 또한 `check_extracted_sources`가 등록부 사이드카의 집합과 그 목록이
같은지를 로드 시점에 강제하므로, 둘이 갈리면 bazel 명령이 바로 실패한다. 코드 파일마다 드리프트 테스트
`//:extract_drift_<모듈>`이 있고 그 묶음은 `//:extract_drift_test`다.

**정의 사이의 호출은 지식으로 올라오지 않는다** (유저 답 Q191-a, 2026-11-28). 2026-09-30부터 2026-11-28까지는 정의 항목의
선택 키 `uses`가 같은 모듈과 `USES_TARGETS`가 선언한 모듈의 최상위 정의를 가리켜 `agt:usesDefinition`으로 올라왔다. 코드
추출이 정의 단위 항목을 내지 않게 되면서 추출기는 이 속성을 방출하지 않는다. 속성은 온톨로지에 남고, `USES_TARGETS`와
`revalidate`의 호출부 열은 입력 없이 남는다. 호출 관계는 소스에서 읽는다.
