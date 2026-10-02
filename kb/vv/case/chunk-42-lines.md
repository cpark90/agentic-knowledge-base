---
id: https://agentic-knowledge-base.dev/id/chunk/a45a0511-d839-4219-9c67-b417be2d8f51
type: schema
level: concrete
title_ko: 본문 1,093토큰인 청크가 chunk_lint에서 FAIL [chunk]로 거부되고 커밋된 청크는 세 lint 게이트를 통과한다
title: A chunk with a 1,093-token body is rejected by chunk_lint as FAIL [chunk] and committed chunks pass the three lint gates
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T21:06:50+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/07d19d32-971d-4e08-89c4-f4d985d4471b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/4eef1ba8-9095-4b69-aa55-69ca65ff7a35]
---
**케이스** — 경계값 둘(1,092토큰·1,093토큰)과 커밋된 청크 전체를 자극으로 쓴다. 상한의 단위가 줄에서 토큰으로 바뀌어(2026-10-01, p1-chunk-unit-is-tokens) 경계 자극이 developer 고정물 `defs/tests/fx_token_at.md`(1,092토큰)·`defs/tests/fx_token_over.md`(1,093토큰)로 바뀐다 — 둘 다 `status: deprecated`라 산문·목록 검사 대상이 아니고 본문 상한만 겨눈다. 이 자극은 임시 파일이 아니라 커밋된 파일이라 `files:`로 담지 않는다 — 1,093토큰 분량의 채움 문장을 이 케이스 본문에 인라인하면 그 자체가 상한을 넘어 케이스가 자신이 증명하려는 규칙을 어긴다.

**자극** — 커밋된 고정물 둘, 경로는 `defs/tests/fx_token_at.md`·`defs/tests/fx_token_over.md`다. 토큰 계수기 어휘 파일 경로는 vv_run이 `python3 tools/chunk_lint.py` 로 시작하는 명령의 하위 프로세스에 `KB_TOKENIZER_VOCAB`(절대 경로)로 넘긴다 — 명령 자신은 `--vocab` 조각도 선행 `bazel build @tiktoken_o200k_base//file`도 적지 않는다(2026-10-01).

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [chunk]"
      - "본문 1093토큰 > 1092토큰"
  - exit: 0
```

**기대** — `chunk_lint`는 1,092토큰 고정물에 침묵하고 1,093토큰 고정물에 `FAIL [chunk]`와 "본문 1093토큰 > 1092토큰"으로 거부하며 종료 코드가 1이다. 같은 고정물의 head 그래프는 `agt:tokenCount 1093`이 되어 plane `requirement`의 `…Chunk` shape(`token-budget-shapes.ttl`, 상한 1,092)에 걸린다. 양성 실행 세 타깃은 PASS다.

**실행 명령** — `python3 tools/chunk_lint.py --chunks defs/tests/fx_token_at.md defs/tests/fx_token_over.md; bazel test //chunks:lint_test //kb/dev:lint_test //kg:gate_test`

**표본 근거** — 이 자극이 어기는 규칙은 본문 토큰 상한 하나다. 임계 기준은 경계 양쪽 값으로 판정하고, 1,092는 통과해야 하고 1,093은 실패해야 하므로 두 값이 상한의 위치를 하나로 고정한다 — developer의 `//defs/tests:token_budget_test`(`token_budget_accepted`·`token_budget_rejected`)가 같은 경계를 이미 쓰므로 고정물을 다시 만들지 않고 재사용한다(2026-10-01). `--vocab` 인자는 더 쓰지 않는다 — vv_run이 `python3 tools/chunk_lint.py `로 시작하는 명령(`VERIFIER_PREFIXES`)을 알아보고 하위 프로세스 환경에 `KB_TOKENIZER_VOCAB`를 직접 넣어, 명령 앞에 env var를 붙이는 형태 없이도 `chunk_lint.py`가 같은 고정 어휘를 찾는다(`tools/chunk2kg.py`의 `tokenizer_vocab_path`). **확인 못 한 것** — 이 치환으로 해소된 것(ambient `python3`의 `tiktoken` 부재로 인한 `ModuleNotFoundError`, 이 저장소 실측 2026-10-01)은 vv_run의 `verifier_env()`(인터프리터를 vv_run 자신의 것으로, `PYTHONPATH`를 하네스 pip 폐포로 바꾼다)가 맞다고 전제한다 — 그 교체 자체의 재현은 `//tools:vv_run_env_test` 몫이고 이 케이스는 보지 않는다.
