---
id: https://agentic-knowledge-base.dev/id/chunk/b8daf558-7bb8-5b5d-95ba-e6f5c305feb2
type: schema
level: concrete
title_ko: 본문이 상한 1092토큰을 넘는 고정물이 chunk_lint에서 FAIL [chunk]로 거부되고 token_budget_test와 커밋된 청크의 세 lint 게이트가 통과한다
title: A fixture whose body exceeds the 1092-token limit is rejected by chunk_lint as FAIL [chunk] while token_budget_test and the three lint gates over committed chunks pass
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T22:47:36+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/07d19d32-971d-4e08-89c4-f4d985d4471b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393, https://agentic-knowledge-base.dev/id/chunk/4eef1ba8-9095-4b69-aa55-69ca65ff7a35]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/8f2ba433-6442-5a41-a86b-5f8d763486f2]
---
**케이스** — 경계 양쪽의 커밋된 고정물 둘로 `chunk_lint`의 거부를 직접 대조하고, 같은 경계와 어휘 변조 거부를 `//defs/tests:token_budget_test`로, 커밋된 청크 전체를 세 lint 게이트로 본다.

**자극** — 커밋된 고정물 둘(`defs/tests/fx_token_at.md`·`defs/tests/fx_token_over.md`)과 빌드 타깃 `//defs/tests:token_budget_test`·`//chunks:lint_test`·`//kb/dev:lint_test`·`//kg:gate_test`다. 어휘 파일 경로는 vv_run이 `KB_TOKENIZER_VOCAB`(절대 경로)로 넘긴다.

**기대** — `chunk_lint`는 1,092토큰 고정물에 침묵하고 1,093토큰 고정물을 `FAIL [chunk]`로 거부하며 종료 코드가 1이다. `token_budget_test`(경계 수락·경계 거부·게이트의 어휘 불일치 거부·변조 어휘 거부)는 PASS다. 커밋된 청크는 세 lint 게이트를 통과한다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [chunk]"
      - "본문 1093토큰 > 1092토큰"
  - exit: 0
  - exit: 0
```

**실행 명령** — `python3 tools/chunk_lint.py --chunks defs/tests/fx_token_at.md defs/tests/fx_token_over.md; bazel test //defs/tests:token_budget_test; bazel test //chunks:lint_test //kb/dev:lint_test //kg:gate_test`

**표본 근거** — `sampling:equivalence` · seed `1` · 시나리오 `token-budget`. 값은 `limit=1092`이고 판정 부류는 `accept`(keep 안)다.
