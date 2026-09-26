---
id: https://agentic-knowledge-base.dev/id/chunk/851ddbad-257f-4b76-afec-adc62b374c3a
type: annotation
level: executable
title_ko: 케이스 실행 검증기의 판정 근거는 종료 코드뿐이고 기대 문구를 대조하지 않는다
title: The case-running verifier judges on exit codes alone and never compares the expected text
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf]
generated: {by: vnv/claude-opus-5, at: 2026-09-23T02:10:00+09:00}
---
thought (non-blocking): 이 검증기는 명령의 종료 코드만 보고 케이스가 적은 기대 문구를 읽지 않는다.

대상: https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf

본문: 2026-09-22 실행에서 케이스 28 건의 명령 46 건 가운데 44 건이 실행됐고 판정의 근거는 각 명령의 종료 코드였다. 케이스 본문의 `**기대**` 절에 적힌 문구는 어디에서도 대조되지 않는다. 같은 저장소의 `failure_test` 는 `expected` 문구를 대조하므로 두 검증기의 엄격도가 다르다.

제안: 케이스의 `**기대**` 절에서 대조할 문구를 코드 스팬으로 표시하고 검증기가 그 문구를 명령 출력에서 찾아 판정에 더한다.

해소: 해소 — 검증기가 `expect` 의 `contains` 를 출력에서 대조하게 되어 2026-09-23 실행에서 옮긴 케이스 둘의 명령 4 건 전부가 종료 코드와 문구 둘 다로 판정됐다.
