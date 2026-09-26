---
id: https://agentic-knowledge-base.dev/id/chunk/e1618552-eb22-4d96-9d01-ff6f54e07613
type: contract
level: logical
title_ko: 두 대상의 검증은 산출물 기준을 겨눈 사슬과 역할·스코프를 겨눈 사슬이 둘 다 있는지 사람이 확인한다
title: Verification of both targets is confirmed by a person checking that a chain aimed at output criteria and a chain aimed at roles and scopes both exist
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-24T11:55:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/cbcb6272-8151-49d5-b868-71be8559ba2e]
---
**합격 기준** — 기준 종류는 **사람 확인**이다. 산출물의 기준을 정한 결정을 겨누는 사슬이 하나 이상이고 역할·스코프·작업 집합을 정한 결정을 겨누는 사슬이 하나 이상인지를 사람이 본다. 두 사슬의 `verifies` 도착점은 둘 다 개발 KB 청크이므로 도착점의 종류로는 갈리지 않는다.

**확인 절차**

1. `bazel build //kg:audit` 의 `검증 현황` 절에서 사슬 수와 케이스까지 이어진 목표 수를 읽는다.
1. `kb/vv/goal/` 에서 카탈로그 역할의 책임을 관측 대상으로 적은 검증 목표를 센다. 2026-09-24 실측은 `agent-catalog-complete` 하나다.
1. 그 사슬의 케이스가 `verifies` 하는 개발 KB 청크가 역할·스코프를 정한 결정인지 본다. 2026-09-24 실측의 도착점은 `p11-agent-catalog-derives-scope` 와 `p11-dev-profile-role-permissions` 의 결론이다.
1. 제품 쪽에서 같은 절차를 밟아 도착점이 산출물의 기준을 정한 결정인지 본다. 둘 다 있으면 성립이다.

**등급** — C 다. 사슬 수는 기계가 세지만 도착점이 무엇을 정한 결정인지는 사람이 판정한다.

케이스를 두지 않는다. 어느 검증 목표가 에이전트 쪽인지를 가르는 표시가 그래프에 없어 기대를 기계가 대조할 수 없다. 그 표시가 생기면 케이스를 둔다. 판정의 원본은 `tools/weave.py` 의 `render_audit` 과 `kb/dev/decision/p8-agent-verification-target/conclusion.md` 다.
