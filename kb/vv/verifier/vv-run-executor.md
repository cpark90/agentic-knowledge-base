---
id: https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf
type: artifact
level: executable
title_ko: 케이스의 양성 명령을 실행해 pass·fail·skip 을 내는 검증기는 tools/vv_run.py 다
title: The verifier that runs each case's positive commands and yields pass, fail or skip is tools/vv_run.py
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-22T23:40:00+09:00}
---
**검증기** — 케이스(`kb/vv/case/`)의 `**실행 명령**` 줄을 읽어 명령을 `;`·`&&` 로 나누고 케이스마다 판정을 내는 검증기는 `tools/vv_run.py` 다. 진입점은 `bazel run //tools:vv_run` 이고 보고는 저장하지 않는 생성 문서다.

**적용하는 기준** — 실행한 명령이 하나라도 비영 종료면 `fail`, 명령 전부를 실행해 전부 종료 0 이면 `pass`, 건너뛴 명령이 있거나 실행한 명령이 없으면 `skip` 이다. 판정 어휘 셋의 정의처는 `tools/kb_lib.py` 의 `RUN_VERDICTS` 다.

**실행 범위** — 허용 목록은 `bazel test`·`bazel build`·`bazel query`·`python3 tools/gen_build.py --check` 넷이고 전부 읽기 전용이다. 임시 파일 자극(`/tmp/vv-*`)과 `bazel run` 으로 시작하는 명령은 실행하지 않고 건너뛴다.

**재현 기록** — 명령마다 종료 코드와 소요를 적고 리비전·워킹트리 변경 여부·bazel 버전·python 버전·플랫폼을 초기 상태로 남긴다. 난수 seed 는 없다.

**산출** — `--record` 는 실행 기록을 `kb/vv/run/run-<UTC>.md` 에 관측으로 쓰고 이미 있는 파일을 덮지 않는다. 그 기록의 `generated.by` 는 역할이 아니라 `process:vv_run` 이라 writer 검사 밖이다.

**검증 대응물** — 없음. `verifies` 의 대상은 같은 수준의 개발 항목이어야 하는데 개발 KB 에 `executable` 수준의 항목이 하나도 없다.
