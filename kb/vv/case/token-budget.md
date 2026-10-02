---
id: https://agentic-knowledge-base.dev/id/chunk/532a1351-697b-48d6-b36f-9c567c61bd68
type: schema
level: concrete
title_ko: 1,093토큰 청크가 chunk_lint에서 거부되고 developer의 token_budget_test가 경계·어휘 변조를 함께 거부한다
title: A 1,093-token chunk is rejected by chunk_lint and developer's token_budget_test also rejects the boundary and a tampered vocabulary
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T21:06:50+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/07d19d32-971d-4e08-89c4-f4d985d4471b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393]
---
**케이스** — developer 고정물 `defs/tests/fx_token_at.md`(1,092토큰)·`fx_token_over.md`(1,093토큰)로 `chunk_lint`의 FAIL/PASS를 직접 대조하고, 같은 경계와 어휘 변조 거부를 developer의 `//defs/tests:token_budget_test`로 함께 본다. 이 케이스는 고정물을 `files:`로 복제하지 않는다 — 1,093토큰 분량을 인라인하면 그 자체가 상한을 넘고, 변조된 어휘 파일(3.6MB)을 인라인하는 것도 같은 이유로 불가능하다.

**자극** — 커밋된 고정물 둘(`defs/tests/fx_token_at.md`·`fx_token_over.md`)과 developer 빌드 타깃 `//defs/tests:token_budget_test`다. 어휘 파일 경로는 vv_run이 `KB_TOKENIZER_VOCAB`(절대 경로)로 넘긴다 — `--vocab` 조각과 선행 `bazel build @tiktoken_o200k_base//file`이 명령에서 빠진다(2026-10-01).

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [chunk]"
      - "본문 1093토큰 > 1092토큰"
  - exit: 0
```

**기대** — `chunk_lint`는 1,093토큰 고정물에 `FAIL [chunk]`로 거부하고 종료 코드가 1이다. `token_budget_test`(accepted·rejected·gate_vocab_rejected·tokenizer_vocab_rejected 네 하위)는 PASS다 — 경계 수락·경계 거부·게이트의 어휘 불일치 거부·변조 어휘 거부를 하나로 묶는다.

**실행 명령** — `python3 tools/chunk_lint.py --chunks defs/tests/fx_token_at.md defs/tests/fx_token_over.md; bazel test //defs/tests:token_budget_test`

**표본 근거** — 자극은 1,092·1,093 경계 하나만 건드린다. 두 값이 같은 고정물이므로 developer의 `token_budget_test`와 이 케이스가 같은 경계를 대조하고, 어긋나면 게이트와 V&V의 기대가 갈렸다는 뜻이다. **확인 못 한 것(developer 요청)** — 둘이다. (1) 지시된 형태 `python3 tools/chunk_lint.py --chunks {{…}} --vocab <경로>`(`files:`로 자극을 담는 형태)는 1,093토큰 고정물을 그대로 인라인하면 이 케이스 자신이 schema plane 상한(1,092)을 넘어 실행할 수 없다 — 커밋된 고정물을 직접 가리키는 형태로 대신한다. (2) 어휘 변조 거부(`tokenizer_vocab_rejected`·`token_budget_gate_vocab_rejected`)는 변조 어휘 파일을 셸로 만드는데(`cp`+`echo`) vv_run의 허용 명령에 파일 변형 수단이 없어 `bazel test //defs/tests:token_budget_test`로 대신 본다 — 직접적인 `python3 tools/validate.py --vocab <변조 경로>` 형태는 세울 수 없다.
