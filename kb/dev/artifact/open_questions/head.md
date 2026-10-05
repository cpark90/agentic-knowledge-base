---
id: https://agentic-knowledge-base.dev/id/chunk/611551cc-ec21-4187-a12d-6a843751700f
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/open_questions.py)
title: module head agt in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/4fe6beea-c6ab-454b-bad0-2cfede25066c
---
**모듈 머리** — `tools/open_questions.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
SLOT = "미확정"  # 선택 슬롯의 표지 — 값 어휘의 정의처는 chunk2kg.BODY_SLOT_KEYWORDS 다
# `미확정: <질문>. 상세는 `<값>`[·`<값>`]다.` — 상세 절은 선택이다. 질문만 적은 슬롯도 집계 대상이다
SLOT_LINE = re.compile(r"^" + SLOT + r":\s*(.+)$")
DETAIL = re.compile(r"상세는\s*((?:`[^`]+`\s*[·,]?\s*)+)다\.?\s*$")
TICK = re.compile(r"`([^`]+)`")
# 후보 링크의 상태 → 본문 `state:` 어휘 (space2kg 가 쓴 사상의 역)
STATE_OF_LINK = {link: state for state, (_, link) in kb_lib.SPACE_STATE_LINK.items()}
```
<!-- 인용 끝 -->
