---
id: https://agentic-knowledge-base.dev/id/chunk/e0eabf1c-ab57-47f1-b10e-870f8299aa26
type: contract
level: logical
title_ko: 인터프리터 경계는 gate_test 의 writer 검사와 channel_lint_test 로 판정하고 어긴 단위 지식과 메시지는 FAIL [writer] 와 FAIL [channel] 로 끝난다
former_title_ko: ["인터프리터 경계는 gate_test 의 writer 검사와 channel_lint_test 로 판정하고 어긴 지식 항목과 메시지는 FAIL [writer] 와 FAIL [channel] 로 끝난다"]
title: The interpreter boundary is judged by the writer check in gate_test and by channel_lint_test, and a violating knowledge item or message ends in FAIL [writer] or FAIL [channel]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
verified: [{by: vnv/claude-opus-5-5, at: 2026-10-24T03:32:01+09:00}, {by: vnv/claude-opus-5-5, at: 2026-10-24T22:39:25+09:00}, {by: vnv/claude-opus-5-5, at: 2026-10-25T00:43:01+09:00}, {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/95634e87-4ff2-44cd-a23f-0b2078e91769]
---
**합격 기준** — 기준 종류는 **불변식**이다. 커밋된 모든 메시지의 from 과 to 가 hci 와 orchestrator 중 서로 다른 둘이고, 쓰기 지식 종류가 없는 역할(interpreter 와 그 하위 역할 hci)이 만든 모든 단위 지식에 쓰기 권한 있는 역할의 verified 가 있다. 기준을 새로 만들지 않고 이미 도는 두 게이트를 판정 술어로 쓴다.

**판정 술어**

- 양성: `bazel test //kg:gate_test //harness:channel_lint_test` 가 PASS 다.
- 음성(발신자 어휘): from 이나 to 가 hci 와 orchestrator 밖인 메시지는 `FAIL [channel] … from '<값>' 는 어휘 밖이다 (hci|orchestrator)` 로 끝나고 종료 코드가 1 이다.
- 음성(단일 작성자): orchestrator 수신함의 메시지가 to: orchestrator 가 아니면 `단일 작성자 위반` 이, from 과 to 가 같으면 `from 과 to 가 같다` 가 나온다.
- 음성(직접 쓰기): generated.by 가 `interpreter/<모델>` 이나 `hci/<모델>` 이고 verified 가 없는 단위 지식은 `FAIL [writer] … 생성자 … 의 역할 <역할> 는 KB … 쓰기 권한이 없다` 로 끝난다.
- 판정 밖: 역할이 아닌 생성자의 단위 지식은 `info [writer]` 줄로만 세어지고 통과한다. 채널의 `agt:ownedBy`(orchestrator 수신함은 interpreter) 와 채널 게이트의 역할 어휘(hci 와 orchestrator, 1단계에서 그대로)는 대조하지 않는다.

**등급** — B 다. 네 갈래는 `bazel test //...` 안에서 기계가 판정하지만, 판정 밖의 두 자리가 남아 외부 대상의 직접 쓰기를 기계가 전부 막지는 않는다. 두 자리는 채널 게이트의 역할 어휘를 카탈로그에 맞추고 MCP 서버를 들이는 이후 단계에서 닫는다.
