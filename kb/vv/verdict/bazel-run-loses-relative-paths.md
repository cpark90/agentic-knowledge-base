---
id: https://agentic-knowledge-base.dev/id/chunk/6649e907-2564-4642-8253-1a1a5b3b649f
type: annotation
level: executable
title_ko: 허용 목록이 받는 bazel run 형태는 워크스페이스 상대 경로 인자를 runfiles 에서 풀어 자극에 닿지 못한다
title: The allow-listed bazel run form resolves workspace-relative arguments inside runfiles and never reaches the stimulus
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf]
generated: {by: vnv/claude-opus-5, at: 2026-09-23T02:30:00+09:00}
---
thought (non-blocking): 음성 명령의 허용 목록은 `python3 tools/<검증기>.py` 와 `bazel run //tools:<검증기>` 를 같은 자격으로 받지만 뒤의 형태는 상대 경로를 가리키는 케이스에서 실행되지 않는다.

대상: https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf

본문: 2026-09-23 측정에서 `bazel run //tools:validate -- --ontology $(ls kb/ontology/*/*/*-ontology.ttl) …` 가 `FAIL [syntax] … 파싱 실패 — [Errno 2] … validate.runfiles/kb/ontology/…` 로 종료 코드 2 를 냈다. 워크스페이스 상대 경로가 runfiles 트리에서 풀려 자극 파일에 닿기 전에 입력 단계에서 멈춘 것이다. `foreign-vocabulary-rejected` 의 명령을 `python3 tools/validate.py` 로 바꾸고서야 음성 명령이 돌았고 케이스가 `pass` 가 됐다.

제안: 허용 목록에서 `bazel run //tools:<검증기>` 형태를 빼거나 그 형태를 쓴 케이스를 `FAIL [vv-case]` 로 실행 전에 거부한다.

해소: 해소 — 허용 목록에서 그 형태가 빠졌고(`VERIFIER_PREFIXES` 는 `python3 tools/<검증기>.py` 아홉뿐이다) 케이스 형식 검사가 같은 형태를 `FAIL [vv-case]` 로 실행 전에 거부하며, 그 형태를 쓰는 케이스는 28건 중 0건이다.
