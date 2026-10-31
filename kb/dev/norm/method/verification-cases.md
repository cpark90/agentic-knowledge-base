---
id: https://agentic-knowledge-base.dev/id/chunk/5bf9e568-5eb8-4c6e-b0fb-b59020cea362
type: norm
level: logical
title_ko: docs/method.md 절 검증의 이어짐 — 기계가 읽는 테스트 케이스와 최소 음성 자극, 검증기 격리
title: docs/method.md verification section continued — machine-readable cases, minimal negative stimuli and verifier isolation
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:24:08+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6a4bb0-67a3-435c-bdab-850ae50240c4
continues: true
---
**테스트 케이스는 자극과 기대를 기계가 읽는 형식으로 적는다**([`p8-machine-readable-case`](../../decision/p8-machine-readable-case/conclusion.md),
2026-09-23). 산문 옆의 `yaml` 펜스가 `files`와 `expect`를 담는다.
`files`는 이름에서 내용으로의 대응이고, `expect`는 명령마다 `exit`와 `contains`를 적는다.
검증기는 자극을 임시 디렉토리에 써서 `{{이름}}`을 실제 경로로 바꾼 뒤 실행하고 지운다. 판정은 종료 코드와 문구가 둘 다
맞아야 통과다. 종료 코드만 보면 기대한 사유로 실패했는지 모르고, 다른 이유로 실패한 검증기는 **틀린 것을 검증하기**
때문이다. 건너뛴 명령이 있는 테스트 케이스는 `pass`가 아니라 `skip`이다. 게이트의 값은 무엇을 통과시키는가가 아니라
무엇을 거부하는가에 있다.

**음성 자극은 검사하려는 규칙 하나만 어긴다**([`p8-minimal-negative-stimulus`](../../decision/p8-minimal-negative-stimulus/conclusion.md)).
둘 이상을 어기면 종료 코드가 어느 규칙을 가리키는지 말하지 못하고 `contains` 문구만이 분기를 고정한다. 게이트 메시지는
수정 방향을 알려 주므로 개선되면서 바뀌는데, 그때 종료 코드가 받쳐 주지 않으면 고치는 사람은 새 문구를 무엇에 맞출지
모른다. 그래서 `**표본 근거**`에 그 자극이 어기는 규칙을 적고, 자극이 최소가 되지 않으면 테스트 케이스를 나눈다.
최소성은 자극을 하나씩 빼 보는 실험으로만 확인되므로 게이트가 아니라 표본 근거의 주장이다.

**검증기는 실행기의 파이썬·runfiles 문맥을 물려받지 않는다**([`p8-verifier-env-isolation`](../../decision/p8-verifier-env-isolation/conclusion.md)).
실행기를 부르는 방식이 테스트 케이스의 판정을 바꾸면 재현이 아니기 때문이다. 게이트 `vv-run-env`인 `//tools:vv_run_env_test`가
그 격리를 `bazel test //...` 안에서 상시 판정한다. 이 게이트는 판정 대상을 실행기 전체가 아니라 격리의 동작으로 좁혀
중첩 bazel을 피했다.
