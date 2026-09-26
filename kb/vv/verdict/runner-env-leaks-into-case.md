---
id: https://agentic-knowledge-base.dev/id/chunk/1b6cf1f2-8a75-4a1e-bf1e-62fa0df3b53c
type: annotation
level: executable
title_ko: 실행기를 부르는 방식이 케이스의 판정을 바꿀 수 있었고 두 실행 경로의 대조를 상시로 재는 수단이 아직 없다
title: How the runner is invoked could change a case's verdict and no standing means yet measures the two execution paths against each other
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}, {resource: https://agentic-knowledge-base.dev/id/chunk/2fa82a3a-2e47-4bf8-8d59-2e02da4270dd}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf]
generated: {by: vnv/claude-opus-5, at: 2026-09-26T00:20:00+09:00}
---
issue (non-blocking): 환경 격리는 들어왔으나 그것이 지켜지는지는 사람이 두 번 돌려 대조해야만 보인다.

대상: https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf

본문: `bazel run` 스텁이 `PYTHONSAFEPATH=1` 을 두고(`bazel-bin/tools/vv_run` 626줄) 하위 프로세스가 그것을 물려받으면 케이스의 `python3 tools/validate.py` 가 `ModuleNotFoundError` 로 종료 1 을 내고 변수 없는 같은 명령은 종료 0 을 내는 것을 2026-09-23 에 직접 재현했다. `clean_env` 가 들어온 지금 두 실행 경로는 케이스 28 건의 판정이 전부 `pass` 로 같고 명령 46 건의 종료 코드 열도 같다. 그 대조는 두 경로를 따로 돌려 손으로 맞춘 것이고 케이스로는 잴 수 없다. `vv_run` 이 읽기 전용 검증기 아홉에 없어 중첩 실행은 두 형태 다 SKIP 이기 때문이다.

제안: `//tools:vv_run_test` 같은 테스트 타깃을 두면 케이스가 `bazel test` 허용 목록으로 두 경로의 대조를 부를 수 있다.

해소: 해소 — `//tools:vv_run_env_test`(게이트 `vv-run-env`)가 `bazel test //...` 안에서 격리를 판정해 사람이 두 번 돌려 대조할 일이 없어졌고, 남은 케이스 단위 두 경로 대조는 중첩 bazel 이라 허용 목록 밖이다.
