---
id: https://agentic-knowledge-base.dev/id/chunk/2c9c6ae8-c825-45f2-9153-9abb00a149fb
type: artifact
level: executable
title_ko: //kg:gate_test를 캐시 없이 두 번 돌리면 둘 다 PASS이고 실행 기록에 리비전·환경·seed 없음이 적힌다
title: Running //kg:gate_test twice without cache passes both times and the run record carries revision, environment and no seed
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/60b9e928-9226-4449-b92f-014597e9ff98]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 게이트 테스트 하나를 같은 리비전에서 캐시 없이 두 번 실행하는 것을 자극으로 쓴다.

**자극** — `//kg:gate_test`다. 입력은 head 그래프·참조 그래프·시드·ODD·온톨로지·표준 어휘 원문·verify 질의이고 전부 선언된 파일이다. `--runs_per_test=2`가 같은 액션을 두 번 예약하고 `--cache_test_results=no`가 앞 결과의 재사용을 막는다.

```yaml
target:   //kg:gate_test
flags:    [--runs_per_test=2, --cache_test_results=no]
revision: 같은 워킹트리 — 두 실행 사이에 파일을 고치지 않는다
```

**기대** — 요약이 `Executed 1 out of 1 test: 1 test passes.`이고 두 실행(`run_1_of_2`·`run_2_of_2`)의 로그가 둘 다 PASS다. 종료 코드가 0이다. 이 케이스를 `vv_run`으로 돌린 실행 기록에는 리비전·bazel·python·OS·`seed 없음`이 적힌다.

**실행 명령** — `bazel test //kg:gate_test --runs_per_test=2 --cache_test_results=no`

**판정 범위** — 재현성의 최소 표본은 같은 입력의 두 실행이다. 두 번이면 일치·불일치가 갈리고 세 번째는 분기를 늘리지 않는다. `//kg:gate_test`를 고른 이유는 입력이 가장 많은 검증기라 비결정성이 있다면 여기서 드러난다는 데 있다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p8-reproducibility` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
