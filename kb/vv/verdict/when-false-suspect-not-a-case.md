---
id: https://agentic-knowledge-base.dev/id/chunk/bdeee674-eb23-4c3c-a3b5-40716acc8521
type: annotation
level: executable
title_ko: when 이 거짓인 링크가 suspect 로 유도되는 것은 손으로 재현했으나 vv_run 케이스로 감쌀 수 없다
title: A when-false link being derived to suspect was reproduced by hand but cannot be wrapped as a vv_run case
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-04T20:34:00+09:00}
---
issue (non-blocking): `assume_check` 가 `vv_run` 의 읽기 전용 검증기 아홉에 없어 이 자극은 케이스가 아니라 주석으로만 남는다.

대상: https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf

본문: `tools/vv_run.py` 의 `READ_ONLY_VERIFIERS` 는 아홉이고 `assume_check` 는 그 안에 없어 `classify()` 가 그 명령을 실행 대상이 아니라 SKIP 으로 분류하므로 케이스로 감쌀 수 없는 자극(`agt:stimulusNotWrappableAsCase`)이라 케이스에 넣어도 판정은 언제나 `skip` 이지 `pass`·`fail` 이 아니다. 2026-09-26 에 `-space` 청크(확정 링크, `when: "in(cond-build-system)"`, 지지 증거 `runResult`) 로 `python3 tools/assume_check.py --break cond-build-system <ttl>` 을 직접 실행하니 종료 코드 1, 결과 줄 "`when` 이 거짓인 링크 있음", 링크 행 `confirmed → suspect · when 거짓 — in(cond-build-system)` 이 나왔다. `--break` 를 뺀 같은 자극의 재실행은 `cond-build-system` 이 실제 환경에서 `in` 으로 판정되어 링크가 `confirmed` 를 유지하고 종료 코드 0 을 냈다. 바뀐 것은 그 조건 하나의 진위뿐이라 최소 자극이다.

제안: `assume_check` 를 `READ_ONLY_VERIFIERS` 에 더하거나 `--break` 인자를 가진 명령의 별도 허용 형태를 두면, 위 자극을 `files`(-space 청크 내용)·`expect`(`exit: 1`·`contains: suspect`) 를 가진 케이스로 옮길 수 있다. 이 변경은 `tools/vv_run.py` 라 vnv 의 write plane 밖이다.

해소: 해소 — `assume_check` 가 `READ_ONLY_VERIFIERS` 열이 되어(developer, 2026-09-26) 이 자극을 케이스 `kb/vv/case/when-false-suspect.md` 로 옮겼다. `python3 tools/vv_run.py --case when-false-suspect` 실행에서 `pass`(명령 2 · 건너뜀 0 · 기대 대조 2/2)를 확인했다.
