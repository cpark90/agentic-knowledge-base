---
id: https://agentic-knowledge-base.dev/id/chunk/6bb376e1-0a34-4ab6-ba78-df2c0b030043
type: contract
level: logical
title_ko: 실행 기록은 memory·concrete 청크로 게이트를 통과하고 같은 이름의 기록은 다시 쓰이지 않는다
title: A run record passes the gates as a memory-concrete chunk and a record of the same name is never rewritten
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/63187a4f-7908-4cad-8128-60b70edb99bd]
---
**합격 기준** — 기준 종류는 **불변식**이다. `kb/vv/run/`의 모든 파일에 대해 `plane = memory ∧ level = concrete ∧ generated.by = process:vv_run`이 성립하고, 파일 집합은 커지기만 한다.

**판정식**

- 음성(덮어쓰기): 이미 있는 `run-<UTC>.md`와 같은 시각의 `--record`는 `FAIL [vv_run] kb/vv/run/run-<UTC>.md: 이미 있다 — 실행 기록은 append-only 다 (r-026)`로 끝나고 종료 코드가 2(EXIT_CONFIG)다.
- 음성(수준): 실행 기록 타깃의 `level`을 `logical`로 두면 분석이 `수준 허용표 위반 — plane memory 는 level logical 에 살 수 없다` 문구로 실패한다.
- 양성: `bazel test //kb/vv:lint_test //kg:gate_test`가 PASS이고 `bazel build //kb/vv/run/...`이 성공한다. 기록의 케이스 표 머리는 `kb_lib.RUN_CASE_TABLE_HEADER`이고 감사가 그 머리로 표를 찾는다.

**등급** — B다. 판정은 기계가 하되 청크 검사·그래프 검증의 실행 비용이 있다.

기준의 대상은 `kb/vv/run/*.md` 전부이고 판정의 원본은 `tools/vv_run.py`의 `main`, `defs/kb.bzl`의 `_check_residency`, `tools/chunk_lint.py`다. 기록의 리비전·환경 줄은 별도 기준 `reproducible-runs`의 몫이다.
