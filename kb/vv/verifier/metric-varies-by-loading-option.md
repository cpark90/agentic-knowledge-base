---
id: https://agentic-knowledge-base.dev/id/chunk/5ed33037-2ebe-55ba-8cac-68f9f60e39b3
type: artifact
level: executable
title_ko: 세 생성 문서의 머리 union 증분 표기가 G4 를 통과하고 쌍마다 트리플 총수의 차가 대칭차 구성원 증분 합과 같다
title: The union increment notation in the heads of three generated documents passes G4, and for each pair the difference in triple totals equals the increment sum of the symmetric-difference members
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/4b460cbc-fe23-48fd-8ac3-daf8351c98c9]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:20:18+09:00}
layer: process
---
**검증기** — 생성 문서 셋과 게이트 하나, 고정물 시험 하나를 자극으로 쓴다.

**자극** — `//kg:metrics` · `//kg:link_candidates` · `//kg:audit`의 머리 `입력` 줄이다. 줄마다 `트리플 <n> (union: <구성원> +<증분> · …)`을 적는다(유저 답 Q40-a).

**기대** — 빌드가 성공하고 `//:gendoc_test`와 `//defs/tests:gendoc_union_fixture_test`가 PASS다. 세 머리에서 공통 구성원의 증분이 같고 쌍마다 `|n1 − n2|`가 한쪽에만 있는 구성원의 증분 합과 같다. 실측 2026-10-04에 75587 · 73790 · 75963이고 차 1797 · 376 · 2173이 각각 `odd`+`ontology` · `gates` · 셋의 합이다.

**실행 명령** — `bazel build //kg:metrics //kg:link_candidates //kg:audit && bazel test //:gendoc_test //defs/tests:gendoc_union_fixture_test`

**판정 범위** — 실행 명령은 문서마다의 증분 합 = 총수(G4)를 판정한다. 쌍별 대조는 증분을 선언 순서대로 앞 구성원들의 합집합에 더하므로 공통 구성원이 같은 순서로 앞에 올 때 성립하고, 그 대조를 하는 도구가 없어 이 검증기가 머리 세 줄로 산술 대조를 한다. 케이스는 없다.

**검증 대응물** — 없음. 같은 `executable` 수준의 개발 항목이 없어 `verifies`를 달 수 없다.
