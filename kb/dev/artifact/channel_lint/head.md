---
id: https://agentic-knowledge-base.dev/id/chunk/2b6adf1a-07f9-41ca-b86b-44bcb3041a2a
type: artifact
level: executable
title_ko: 모듈 머리 gate (tools/channel_lint.py)
title: module head gate in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/84c1731c-46ae-469d-a2b2-a52d6615da86
---
**모듈 머리** — `tools/channel_lint.py` 의 모듈 머리 `gate` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
GATE = CHANNEL_GATE
ROLES = ("interpreter", "orchestrator")  # 채널의 역할 어휘 — 수신함 디렉토리·from·to 가 모두 여기서 나온다. 역할을 바꾸면 이 줄만 고친다
ROLE_ALIASES = {"hci": "interpreter"}  # 옛 이름 → 정규 이름. hci 는 interpreter 의 유저 대상 하위 역할이고 옛 메시지(archive)의 from·to 에 남는다
INBOXES = {f"to_{r}": r for r in ROLES}  # 수신함 디렉토리 → 그 수신함의 to (단일 작성자)
ARCHIVE = "archive"
SNAPSHOT_TRIES = 5  # 이동 경쟁에서 디렉토리를 다시 읽는 최대 횟수 — 넘으면 마지막 판정을 그대로 낸다
SETTLE_SECONDS = 0.2  # 다시 읽기 전에 기다리는 시간 — mark.sh 의 rename 과 rm 사이가 지나가게 한다
MSG_FIELDS = ("id", "from", "to", "type", "status", "subject", "created")
MSG_TYPES = {"task", "question", "answer", "result", "knowledge", "status", "ack"}
MSG_STATES = {"new", "read", "in_progress", "done", "blocked"}
DIRECTION = {"task": ("interpreter", "orchestrator"), "result": ("orchestrator", "interpreter"),
             "status": ("orchestrator", "interpreter")}
REPLY_TO = {"answer": "question", "result": "task"}  # re 가 필수인 type → re 대상의 type
CLOSED_BY = {"task": "result", "question": "answer"}  # done 이 되려면 이 type 의 회신이 re 로 가리켜야 한다
TASK_SECTIONS = ("## 배경", "## 목표", "## 완료조건", "## 제약", "## 파급효과", "## 확인 못 한 것")
Q_FIELDS = ("id", "status", "subject", "created")
Q_STATES = {"open", "answered", "closed"}
MSG_ID = re.compile(r"^\d{4}$")
Q_ID = re.compile(r"^Q-\d{4}$")
ANSWER_LINE = re.compile(r"^답:(.*)$", re.M)
DIRECTIVE_ANSWER = re.compile(r"^답:\s*\(유저의 대화 지시")  # 대화 지시 기록 꼴의 표지 — 머리가 이것이면 꼴 전체를 본다
DIRECTIVE_HEAD = re.compile(r"^답: \(유저의 대화 지시 원문, (\d{4}-\d{2}-\d{2})\)(.*)$")
DIRECTIVE_READING = re.compile(r"^(?:#+\s*|>\s*)?hci의 읽기")
QUESTION_HEADING = re.compile(r"^## Q\d+")
HCI_REFLECTED = re.compile(r"hci 반영|hci ?가 ?(반영|수행)", re.M)  # 서술형만 — 괄호 서명 "(hci, 날짜)" 는 잡지 않는다 (유저 승인 2026-09-12)
# 식별자 옆 한글 이름(names)의 시행 시각 — `created` 가 이 시각 이상인 항목에만 건다. 소급하지 않는다 (유저 답 Q103 3번)
NAMES_SINCE = "2026-10-24T08:20:24+09:00"
DECISION_RECORD = re.compile(r"(?:^|/)kb/dev/decision/([^/]+)/conclusion\.md$")  # 결정 기록의 자리 — 디렉토리 이름이 slug 다
NAME_PREDICATES = (RDFS.label, SKOS.prefLabel)  # agt:·id: 의 한글 이름 — @ko 만 읽는다
FORMER_PREDICATE = SKOS.hiddenLabel  # agt:·id: 의 옛 한글 이름 — 과거 표기다(p0-skos-label-synonyms). 이미 보낸 기록에만 받는다
```
<!-- 인용 끝 -->
