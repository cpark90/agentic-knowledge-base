---
id: https://agentic-knowledge-base.dev/id/chunk/95634e87-4ff2-44cd-a23f-0b2078e91769
type: requirement
level: functional
pattern: ubiquitous
title_ko: 외부 대상의 요청은 인터프리터의 채널을 거쳐서만 orchestrator 에 닿고 외부 대상이 단위 지식을 직접 쓰는 경로가 없다
former_title_ko: ["외부 대상의 요청은 인터프리터의 채널을 거쳐서만 orchestrator 에 닿고 외부 대상이 지식 항목을 직접 쓰는 경로가 없다"]
title: Requests of external parties reach the orchestrator only through the channels of the interpreter, and no path lets an external party write a knowledge item directly
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
verified: [{by: vnv/claude-opus-5-5, at: 2026-10-24T03:32:01+09:00}, {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/e461c8ed-196f-4eac-9cff-4052d5833776]
---
**검증 목표** — 외부 대상의 요청은 인터프리터 역할이 가진 채널을 거쳐서만 orchestrator 에 닿고 외부 대상이 단위 지식을 직접 쓰는 경로가 없다는 것이, 카탈로그의 채널 소유와 채널 게이트, writer 게이트로 강제된다는 것이 보여져야 한다. 카탈로그는 역할 `interpreter` 를 두고 유저 대상의 `hci` 를 그 하위 역할로 두며, 그 일반화는 결정 `p11-interpreter-generalizes-hci` 가 정한다.

- **이해관계자**: 검증자 · **관심사**: 지식 베이스의 서비스 경계

**무엇을 관측하면 성립하는가**

- 카탈로그 `kg/catalog-kg.ttl` 에서 orchestrator 수신함 `id:chan-to-orchestrator` 의 `agt:ownedBy` 는 `id:role-interpreter` 이고, 유저 채널 `id:chan-user-feedback` 의 `agt:ownedBy` 는 그 하위 역할 `id:role-hci` 다.
- 채널 게이트 `channel`(`tools/channel_lint.py`)이 메시지의 from 과 to 를 hci 와 orchestrator 로 한정하고 둘이 같지 않게 하므로, orchestrator 수신함에 쓰는 발신자는 hci 뿐이고 task 는 hci 에서 orchestrator 로만 간다.
- 역할 `interpreter` 와 `hci` 는 `agt:writes` 를 갖지 않고, writer 게이트(`tools/validate.py` 의 `check_writer`)는 두 역할이 만든 단위 지식을 쓰기 권한 있는 역할의 verified 없이 거부한다.
- `bazel test //kg:gate_test //harness:channel_lint_test` 가 PASS 다.

1단계에서는 interpreter 세션이 hci 이름으로 메시지를 쓰므로 채널 게이트의 역할 어휘는 hci 와 orchestrator 그대로다. 다만 두 자리는 아직 열려 있다. writer 게이트는 역할이 아닌 생성자(`claude/…` 와 `process:…`)를 검사하지 않고 정보 줄만 내며, 채널의 `agt:ownedBy` 를 카탈로그와 대조하는 게이트는 없고 채널 게이트의 역할 목록은 코드 상수다. 외부 대상을 받는 MCP 서버와 교환함, 채널 게이트의 역할 어휘를 카탈로그의 interpreter 로 옮기는 일은 이후 단계의 일이다.
