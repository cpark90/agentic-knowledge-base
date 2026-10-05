---
id: https://agentic-knowledge-base.dev/id/chunk/1a599616-9e27-4823-94f2-464c80fb8ef4
type: contract
level: abstract
title_ko: 하네스의 지식 추종은 생성 부분의 드리프트 테스트 PASS 를 필요조건으로 두고 경계의 충분성은 사람이 확인한다
title: The harness following the knowledge takes a PASS of the drift tests on the generated parts as a necessary condition, and a person confirms the sufficiency of the boundary
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-05T13:36:40+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/df934d56-8cc4-4f5f-8cbd-7ae5b6bb89f0]
---
**합격 기준** — 기준 종류는 **사람 확인**이다. 이 기준은 기계 판정식을 갖지 않는다. 판정식이 서려면 "지식에서 생성되는 하네스 부분"의 집합이 닫혀 있어야 하는데 요구가 그 경계를 미확정으로 남겼고, "개선"은 지식 변경 전후의 하네스 동작 비교라 한 리비전의 실행으로 판정되지 않는다. 그래서 수준은 logical 이 아니라 abstract 다(`p8-pass-criteria`).

**확인 절차**

1. 필요조건은 기계가 판정한다. `bazel test //:build_drift_test //:norms_drift_test //:gendoc_test` 가 PASS 다. 하나라도 FAIL 이면 지식이 바뀌었는데 생성 부분이 따라오지 않은 것이고 불합격이다.
1. `bazel test //kg:gate_test` 가 PASS 다. 게이트가 어휘·shape·ODD 를 지식 파일에서 읽는다는 전제가 깨지지 않았다는 확인이다.
1. 충분성은 사람이 확인한다. 하네스 부분(도구 · 게이트 id · 뷰 · skill)마다 원본이 지식 파일인지 도구 코드인지를 표로 적는다. 원본이 지식인 부분 가운데 드리프트 테스트가 없는 것이 있으면 불합격이다.
1. 최근 리비전 창에서 결정·어휘가 바뀐 커밋마다 하네스의 손 수정이 함께 들어갔는지 `git log` 로 본다. 손 수정이 생성 부분에 들어갔으면 불합격이다.
1. 판단을 판정 주석으로 남긴다.

절차 1·2 의 기계 판정은 `harness-follows-knowledge`(logical) 기준이 맡는다.

**등급** — C 다. 필요조건은 기계가 보장하고 경계와 충분성은 사람이 본다.

케이스를 두지 않는다. 필요조건은 이미 게이트로 돌고 충분성은 실행 명령으로 판정되지 않는다.
