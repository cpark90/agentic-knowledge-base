---
id: https://agentic-knowledge-base.dev/id/chunk/84e79c94-fc03-485c-906a-edaae9c6f07f
type: artifact
level: executable
title_ko: 절 validate-body-slot-markers (tools/kb_lib.py)
title: section validate-body-slot-markers in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/efdfa170-bf07-4ef8-9d31-b554c7e26f8c
composite: {id: https://agentic-knowledge-base.dev/id/composite/efdfa170-bf07-4ef8-9d31-b554c7e26f8c, title_ko: 절 복합체 validate-body-slot-markers (tools/kb_lib.py), title: section composite validate-body-slot-markers in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/84e79c94-fc03-485c-906a-edaae9c6f07f, https://agentic-knowledge-base.dev/id/chunk/a09e5ab7-1cd6-4c2b-b4e4-88c84095631d, https://agentic-knowledge-base.dev/id/chunk/a5547d6c-a232-4c09-83b0-81eb591e8bc6], part_of: https://agentic-knowledge-base.dev/id/composite/163f6311-4c7b-4d2d-983e-94afa5658211}
---
**절** — `tools/kb_lib.py` 의 절 `validate-body-slot-markers` 다. 본문 슬롯 표지 집합의 정합성 (STYLEGUIDE §4, 2026-09-29 — 표지가 늘어날 때 겹침을 보는 규칙이 없던 공백을 메운다)

**정의** — `validate_body_slot_markers` · `decision_role_marker` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 본문 슬롯 표지 집합의 정합성 (STYLEGUIDE §4, 2026-09-29 — 표지가 늘어날 때 겹침을 보는 규칙이 없던 공백을 메운다) ──
# 정의처는 하나(chunk2kg.BODY_SLOT_MARKERS)이지만 표지를 **늘리는** 사람이 그 파일만 보고 기존 표지와 겹치는지
# 확인할 방법이 없었다 — 어제 자극·요인·배제 자극을 더하면서 본문 중간의 "요인 분류"·"요인별로" 같은 굵은 강조가
# 슬롯으로 잘못 방출된 사고(2026-09-29 실측)가 그 공백의 증거다. 이 검사는 자리 판정(_body_slot_at_field_head)이
# 아니라 **표지 낱말 집합 자체**의 두 위험을 본다 — chunk2kg 를 매번 import 하는 도구(kb_lib 의 모든 소비자)가
# 로드 시점에 자동으로 돈다(단일 정의처의 방어, import 부작용).
#   1. 중복 등록 — 같은 표지 낱말이 튜플에 두 번 있으면 실수로 다시 추가한 것이다.
#   2. 접두 겹침 — 표지 A 가 다른 표지 B 의 문자열 **접두**이면(B.startswith(A)), `_body_slot_at_field_head` 의
#      startswith 매칭이 자리가 같을 때 어느 표지가 이기는지 BODY_SLOT_MARKERS 의 등록 순서에 기대게 된다 — 그
#      순서 의존은 다음 표지 추가마다 다시 사고를 낼 수 있는 잠복 결함이다.
# 실측(2026-09-29): 현재 20개 표지는 둘 다 통과한다. `자극` 은 `배제 자극` 의 **부분 문자열**이지만 `배제 자극` 이
# `배제`로 시작해 `자극`으로 시작하지 않으므로(접두 아님) 위반이 아니다 — `_body_slot_at_field_head` 의 매칭이
# 자리(줄 머리·불릿·` · ` 다음)로 이미 걸러 `배제 자극` 줄에서 `자극` 이 별도로 잡히지 않는다. 이 검사는 그 사실을
# 로드 시점에 **단정**해 둔다 — 다음에 표지를 늘릴 때 접두 관계가 생기면 이 자리에서 바로 죽는다.


validate_body_slot_markers(BODY_SLOT_MARKERS)
```
<!-- 인용 끝 -->
