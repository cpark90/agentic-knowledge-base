---
id: https://agentic-knowledge-base.dev/id/chunk/2b6adf1a-07f9-41ca-b86b-44bcb3041a2a
type: artifact
level: executable
title_ko: 모듈 머리 gate (tools/channel_lint.py)
title: module head gate in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/84c1731c-46ae-469d-a2b2-a52d6615da86
---
**모듈 머리** — `tools/channel_lint.py` 의 모듈 머리 `gate` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
GATE = CHANNEL_GATE
ROLES = ("hci", "orchestrator")
INBOXES = {"to_orchestrator": "orchestrator", "to_hci": "hci"}  # 수신함 디렉토리 → 그 수신함의 to (단일 작성자)
ARCHIVE = "archive"
MSG_FIELDS = ("id", "from", "to", "type", "status", "subject", "created")
MSG_TYPES = {"task", "question", "answer", "result", "knowledge", "status", "ack"}
MSG_STATES = {"new", "read", "in_progress", "done", "blocked"}
DIRECTION = {"task": ("hci", "orchestrator"), "result": ("orchestrator", "hci"), "status": ("orchestrator", "hci")}
REPLY_TO = {"answer": "question", "result": "task"}  # re 가 필수인 type → re 대상의 type
CLOSED_BY = {"task": "result", "question": "answer"}  # done 이 되려면 이 type 의 회신이 re 로 가리켜야 한다
TASK_SECTIONS = ("## 배경", "## 목표", "## 완료조건", "## 제약", "## 파급효과", "## 확인 못 한 것")
Q_FIELDS = ("id", "status", "subject", "created")
Q_STATES = {"open", "answered", "closed"}
MSG_ID = re.compile(r"^\d{4}$")
Q_ID = re.compile(r"^Q-\d{4}$")
ANSWER_LINE = re.compile(r"^답:(.*)$", re.M)
HCI_REFLECTED = re.compile(r"hci 반영|hci ?가 ?(반영|수행)", re.M)  # 서술형만 — 괄호 서명 "(hci, 날짜)" 는 잡지 않는다 (유저 승인 2026-09-12)
```
<!-- 인용 끝 -->
