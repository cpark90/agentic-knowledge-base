---
id: https://agentic-knowledge-base.dev/id/chunk/8f2ba433-6442-5a41-a86b-5f8d763486f2
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 저작 산문 상한 경계에 놓인 커밋된 고정물 둘의 검사
title: Logical scenario stimulus — checking two committed fixtures placed on the authored-prose limit boundary
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T22:47:36+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4aa24cd3-1c85-5727-b2bc-cbc71c5206f9
composite: {id: https://agentic-knowledge-base.dev/id/composite/4aa24cd3-1c85-5727-b2bc-cbc71c5206f9, title_ko: 저작 산문 상한 경계에 놓인 커밋된 고정물 둘의 검사, title: Checking two committed fixtures placed on the authored-prose limit boundary, ordered: [https://agentic-knowledge-base.dev/id/chunk/8f2ba433-6442-5a41-a86b-5f8d763486f2, https://agentic-knowledge-base.dev/id/chunk/ea7b8ff7-428a-5f65-bb8b-5852b43eba61, https://agentic-knowledge-base.dev/id/chunk/c000ae77-7877-5fe8-be4a-dd190f72e6fa]}
---
**자극** — actor는 청크를 저작하는 에이전트이고 action은 상한 경계 양쪽의 커밋된 고정물 둘을 `chunk_lint`로 검사하고 경계·어휘 변조 테스트와 커밋된 청크의 lint 게이트를 도는 것이다. 순서는 `chunk_lint` 실행 → `//defs/tests:token_budget_test` 실행 → 세 lint 게이트 실행이다. 고정물은 developer의 `defs/tests/fx_token_at.md`(1,092토큰)·`defs/tests/fx_token_over.md`(1,093토큰)이고 둘 다 `status: deprecated`라 본문 상한만 겨눈다. `keep()`은 고정 계수기와 커밋된 청크 전체다. 변수는 저작 산문 상한 `limit` 하나이고 ODD 속성 `id:cond-tokenizer-lock`(토크나이저 고정 — 토큰 수는 고정 어휘가 정한다)에 매인다. keep은 값 하나 `1092`다. 고정물은 커밋된 파일이라 `files`로 담지 않는다. 1,093토큰 분량을 인라인하면 케이스 자신이 상한을 넘는다.

```yaml
keep:
  limit: {odd: "id:cond-tokenizer-lock", values: [1092]}
cover:
  - {rule: equivalence, vars: [limit]}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/07d19d32-971d-4e08-89c4-f4d985d4471b
  verifies: [https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393, https://agentic-knowledge-base.dev/id/chunk/4eef1ba8-9095-4b69-aa55-69ca65ff7a35]
  title_ko: "본문이 상한 ${limit}토큰을 넘는 고정물이 chunk_lint에서 FAIL [chunk]로 거부되고 token_budget_test와 커밋된 청크의 세 lint 게이트가 통과한다"
  title: "A fixture whose body exceeds the ${limit}-token limit is rejected by chunk_lint as FAIL [chunk] while token_budget_test and the three lint gates over committed chunks pass"
  summary: "경계 양쪽의 커밋된 고정물 둘로 `chunk_lint`의 거부를 직접 대조하고, 같은 경계와 어휘 변조 거부를 `//defs/tests:token_budget_test`로, 커밋된 청크 전체를 세 lint 게이트로 본다."
  stimulus: "커밋된 고정물 둘(`defs/tests/fx_token_at.md`·`defs/tests/fx_token_over.md`)과 빌드 타깃 `//defs/tests:token_budget_test`·`//chunks:lint_test`·`//kb/dev:lint_test`·`//kg:gate_test`다. 어휘 파일 경로는 vv_run이 `KB_TOKENIZER_VOCAB`(절대 경로)로 넘긴다."
  command: "python3 tools/chunk_lint.py --chunks defs/tests/fx_token_at.md defs/tests/fx_token_over.md; bazel test //defs/tests:token_budget_test; bazel test //chunks:lint_test //kb/dev:lint_test //kg:gate_test"
  accept:
    prose: "`chunk_lint`는 1,092토큰 고정물에 침묵하고 1,093토큰 고정물을 `FAIL [chunk]`로 거부하며 종료 코드가 1이다. `token_budget_test`(경계 수락·경계 거부·게이트의 어휘 불일치 거부·변조 어휘 거부)는 PASS다. 커밋된 청크는 세 lint 게이트를 통과한다."
    expect:
      - {exit: 1, contains: ["FAIL [chunk]", "본문 1093토큰 > ${limit}토큰"]}
      - {exit: 0}
      - {exit: 0}
```
