---
id: https://agentic-knowledge-base.dev/id/chunk/2b6adf1a-07f9-41ca-b86b-44bcb3041a2a
type: artifact
level: executable
title_ko: 모듈 머리 gate (tools/channel_lint.py)
title: module head gate in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T11:29:42Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/60faade0-d3e7-4ad4-8bf6-371be22956c3, https://agentic-knowledge-base.dev/id/chunk/f1d4cbae-2b57-4b96-826f-536b132cd624]
part_of: https://agentic-knowledge-base.dev/id/composite/84c1731c-46ae-469d-a2b2-a52d6615da86
---
**모듈 머리** — `tools/channel_lint.py` 의 모듈 머리 `gate` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
GATE = "channel"
USER, AGENTS, INQUIRIES, HANDOFF = "user", "agents", "inquiries", "handoff"
STATES = {
    USER: {"open", "approved", "rejected"},
    AGENTS: {"open", "relayed", "answered", "closed"},
    INQUIRIES: {"open", "answered", "closed"},
    HANDOFF: {"open", "closed"},
}
VERDICTS = {"apply", "apply-with-changes", "needs-decision"}
RETURNABLE = {"apply", "apply-with-changes"}  # needs-decision 은 유저에게 돌아가는 것이라 agents 짝을 기다리지 않는다
HANDOFF_SECTIONS = ("## 파급효과", "## 반영 계획", "## 확인 못 한 것", "## 판정")
HCI_REFLECTED = re.compile(r"hci 반영|hci ?가 ?(반영|수행)", re.M)  # 서술형만 — 괄호 서명 "(hci, 날짜)" 는 잡지 않는다 (유저 승인 2026-09-12)
TAKEN_OVER = re.compile(r"^인수:\s*(orchestrator|developer|vnv)", re.M)
ANSWERED = re.compile(r"^\*\*유저\(", re.M)
PLACEHOLDER = re.compile(r"\((유저가 채움|hci가 유저의 답을 채움)")
```
<!-- 인용 끝 -->
