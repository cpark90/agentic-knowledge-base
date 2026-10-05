---
id: https://agentic-knowledge-base.dev/id/chunk/4b460cbc-fe23-48fd-8ac3-daf8351c98c9
type: contract
level: logical
title_ko: 같은 이름의 지표는 도구가 달라도 같은 값이고 union이 다르면 그 차가 수로 적힌다
title: A same-named metric holds one value across tools and any union gap is written as a number
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:20:18+09:00}
verified: [{by: vnv/claude-opus-5-5, at: 2026-10-04T23:20:47+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/91d72e63-e72e-4803-aaf3-281a81994a31]
---
**합격 기준** — 기준 종류는 **불변식**이다. 같은 리비전에서 도구 `t`가 내는 수치 `m(t, 이름)`에 대해 이름이 같은 두 도구의 값이 같고, 읽는 union이 달라 값이 갈리면 그 차 `|n(t1) − n(t2)|`와 차의 출처 파일이 머리에 적히는 것이 합격이다.

**판정식**

- 차를 적는 자리. 생성 문서 머리 `입력` 줄의 증분 표기 `트리플 <n> (union: chunks +a · base +b · …)`다(유저 답 Q40-a). 구성원 증분은 선언 순서대로 앞 구성원들의 합집합에 더한 트리플 수다.
- 실행. `bazel build //kg:metrics //kg:link_candidates //kg:audit` 뒤 `bazel test //:gendoc_test //defs/tests:gendoc_union_fixture_test`다. 게이트 `gendoc` G4가 문서마다 증분 합 = 총수를 검사하고 고정물 시험이 총수 불일치·증분 없는 옛 표기를 거부한다.
- 음성. 세 문서의 쌍마다 `|n1 − n2|`가 두 union의 대칭차 구성원 증분 합과 다르거나 어느 머리에 증분 표기가 없으면 불합격이다.
- 실측 2026-10-04에 `metrics` 75587 · `link_candidates` 73790 · `audit` 75963이다. 공통 구성원 다섯(`chunks` · `base` · `catalog` · `composite` · `references`)의 증분이 세 문서에서 같다.
- 쌍별 차는 `75587 − 73790 = 1797 = odd 71 + ontology 1726`, `75963 − 75587 = 376 = gates 376`, `75963 − 73790 = 2173 = 71 + 1726 + 376`이다. 세 쌍 모두 같으므로 **합격**이다.
- 양성. 이름이 같은 다른 수치는 갈리지 않는다. `살아 있는 청크`는 세 문서 모두 2225다.

**등급** — B다. 문서마다의 증분 합과 표기 유무는 게이트가 판정한다. A가 아닌 까닭은 쌍별 차와 대칭차 증분 합의 대조를 하는 도구가 없어 검증기 `metric-varies-by-loading-option`이 머리 세 줄로 산술 대조를 한다는 것이다.
