---
id: https://agentic-knowledge-base.dev/id/chunk/e1618552-eb22-4d96-9d01-ff6f54e07613
type: contract
level: logical
title_ko: 두 대상의 검증은 요구에서 파생된 사슬과 역할 책임에서 파생된 사슬이 둘 다 있는지 사람이 확인한다
title: Verification of both targets is confirmed by a person checking that a chain derived from requirements and a chain derived from role responsibilities both exist
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-22T19:06:46+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/cbcb6272-8151-49d5-b868-71be8559ba2e]
---
**합격 기준** — 기준 종류는 **사람 확인**이다. `goals_product = {g | g derivesFrom r, r ∈ requirement} ≠ ∅` 이고 `goals_agent = {g | g 가 역할 책임에서 파생} ≠ ∅` 이며 두 집합의 `verifies` 도착점이 서로 다른지를 사람이 본다.

**확인 절차**

1. `bazel build //kg:audit` 의 `검증 현황` 절에서 제품 쪽 사슬 수를 읽는다.
1. `kb/vv/goal/` 에서 `derivesFrom` 이 요구가 아니라 역할·하네스 개체를 가리키는 검증 목표를 센다. 2026-09-21 실측은 0 이다.
1. 에이전트 쪽 케이스의 `verifies` 도착점이 `id:h-akb`·`id:scope-*`·`id:role-*` 인지 본다.
1. 둘 다 있으면 성립이다. 하나만 있으면 요구는 아직 성립하지 않는다.

**등급** — C 다. 수는 기계가 세지만 역할 책임에서 파생되었는지는 사람이 판정한다.

케이스를 두지 않는다. 에이전트 쪽 사슬이 없어 양성 표본이 없고, `defs/kb.bzl` 은 `verifies` 의 대상을 개발 KB 청크로 한정해 하네스·스코프 개체를 `verifies` 할 수 없다. 이 구조 제약은 결정 `p8-two-verification-targets` 와 어긋나며 보고로 남긴다. 판정의 원본은 `tools/weave.py` 의 `render_audit` 과 이 절차다.
