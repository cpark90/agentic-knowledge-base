---
id: https://agentic-knowledge-base.dev/id/chunk/37e5d11c-da21-4507-ba87-e96d60225f6f
type: annotation
level: concrete
title_ko: 음성 자극을 건너뛴 케이스 둘은 게이트가 거부한다는 절반을 보이지 못한다
title: The two cases whose negative stimulus was skipped fail to show the rejecting half of the gate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/a45a0511-d839-4219-9c67-b417be2d8f51, https://agentic-knowledge-base.dev/id/chunk/ee329895-169a-4bf2-bd1a-94dcc44345e3]
generated: {by: vnv/claude-opus-5, at: 2026-09-22T23:46:00+09:00}
---
issue (non-blocking): 두 케이스의 음성 명령이 실행되지 않아 게이트가 거부한다는 절반이 비어 있다.

대상: https://agentic-knowledge-base.dev/id/chunk/a45a0511-d839-4219-9c67-b417be2d8f51 · https://agentic-knowledge-base.dev/id/chunk/ee329895-169a-4bf2-bd1a-94dcc44345e3

본문: 2026-09-22 실행에서 두 케이스의 음성 명령이 사유 `임시 파일 자극 — 프로즈에 구조만 있어 자동 생성 불가` 로 건너뛰어졌다. 남은 양성 명령만 종료 0 이라 두 케이스의 판정은 `pass` 가 아니라 `skip` 이다. 자극인 임시 파일의 구조가 케이스 본문의 산문과 코드 블록에만 있어 검증기가 그것을 만들 수 없다.

제안: 케이스 본문의 자극 블록을 `vv_run` 이 읽어 임시 파일로 쓸 수 있는 형식으로 정하고 음성 명령의 기대 종료 코드를 같은 블록에 적는다.

해소: 열림 — 자극 형식을 정하는 일이 케이스 저작 규약과 검증기 양쪽을 건드린다.
