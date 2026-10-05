---
id: https://agentic-knowledge-base.dev/id/chunk/46331050-051b-4054-8445-63ffee582cf9
type: annotation
level: logical
title_ko: doccheck --report 는 위치 인자를 쓰지 않고 vv_run 의 자극은 루트 밖에 놓여 이 기준의 케이스를 세울 수 없다
title: doccheck --report ignores positional arguments, and vv_run's stimulus sits outside the root, so this criterion's case cannot stand
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/b173e680-0135-4d83-9e0f-d8fb77d77407]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-04T20:36:37+09:00}
---
issue (non-blocking): 기준 `document-table-matches-generated` 의 음성·통제 쌍 케이스(`p8-machine-readable-case`)를 세우려 했으나 두 설계가 막는다.

대상: https://agentic-knowledge-base.dev/id/chunk/b173e680-0135-4d83-9e0f-d8fb77d77407

본문: `doccheck.py` 의 `--report` 는 `args.files` 를 읽지 않고 `REPORT_DOCS` 네 문서만 보므로, 임의 경로를 줘도 그대로 종료 0 이다
(`python3 tools/doccheck.py --report --root . nonexistent-file.md` 실측). 같은 도구의 `to_rel()` 은 `--root` 밖의 파일을
`FAIL [doccheck]`(`EXIT_CONFIG`)로 거부하는 반면 `vv_run.py` 의 `materialize()` 는 자극을 언제나 워크스페이스 밖
`tempfile.mkdtemp()` 에 쓰고 `files` 의 이름도 단순 파일명(경로 없음)만 허용한다. 두 설계가 겹쳐 doccheck 를 대상으로 한 파일
자극은 `--report` 여부와 무관하게 케이스로 감쌀 수 없는 자극(`agt:stimulusNotWrappableAsCase`)이라 케이스가 구조적으로 서지 않는다.

제안: `doccheck.py --report` 가 `args.files` 를 받으면 `REPORT_DOCS` 대신 그 목록을 대조 대상으로 쓰게 하거나, `--root` 와 무관하게
절대 경로 한두 개를 보고 대상으로 받는 옵션을 추가하면 자극을 꾸밀 수 있다. 이 변경은 `tools/doccheck.py` 라 vnv 의 write plane
밖이다 — developer 가 받는다. 받지 않더라도 등급은 바뀌지 않는다: `--report` 는 설계상 상시 종료 0 인 보고 도구라
(`--report` 는 판정이 아니므로 어긋난 쌍이 있어도 종료 0 이다) `bazel test //...` 의 게이트가 될 수 없고, 등급 A 는 "사람 해석
없는 게이트 판정"을 요구한다. 케이스가 생겨도 그 판정은 `vv_run` 수준의 문구 대조이지 `bazel test` 게이트가 아니므로 기준은
B 에 머문다.

해소: 해소 — developer가 `--report`에 파일 목록을 받게 해 케이스가 섰다, 2026-10-01(`kb/vv/case/document-table-matches-generated.md`).
