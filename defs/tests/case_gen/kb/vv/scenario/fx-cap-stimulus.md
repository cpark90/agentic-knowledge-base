---
id: https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c001
type: decision
level: logical
title_ko: 고정물 논리 시나리오 자극 — 크기와 종류를 바꾼 청크의 검사
title: Fixture logical scenario stimulus — checking a chunk of varied size and kind
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T00:00:00+09:00}
---
**자극** — 크기 `tokens`와 종류 `kind`를 바꾼 청크 하나를 검사에 넣는다. `flag`는 ODD 밖 변수다.

```yaml
keep:
  tokens: {odd: outside, range: [1, 1092], domain: [1, 2000]}
  kind: {odd: "id:cond-repo-layout", values: [plain, nested], reject: [cyclic]}
  flag: {odd: outside, values: ["on", "off"]}
cover:
  - {rule: boundary, vars: [tokens]}
  - {rule: equivalence, vars: [tokens, kind]}
  - {rule: pairwise, vars: [kind, flag]}
  - {rule: factor, var: kind, factors: {"agt:fxCycle": cyclic}}
  - {rule: observed, run: kb/vv/run/fx-run.md, values: {tokens: 7, kind: nested}}
seed: 11
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c002
  verifies: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c003]
  title_ko: "크기 ${tokens}·종류 ${kind}·표시 ${flag}의 고정물 청크 검사"
  title: "Checking a fixture chunk of size ${tokens}, kind ${kind} and flag ${flag}"
  summary: "크기 ${tokens}의 `${kind}` 청크 하나를 검사한다."
  stimulus: "임시 파일 하나다. 이름은 `fx.md`이고 경로는 검증기가 정한다."
  files:
    fx.md: "size ${tokens}\nkind ${kind}\nflag ${flag}\n"
  command: "python3 tools/chunk_lint.py --chunks {{fx.md}}; bazel test //kg:gate_test"
  accept:
    prose: "검사가 통과하고 게이트도 통과한다."
    expect: [{exit: 0}, {exit: 0}]
  reject:
    prose: "검사가 `FAIL [chunk]`로 거부하고 게이트는 통과한다."
    expect: [{exit: 1, contains: ["FAIL [chunk]"]}, {exit: 0}]
```
