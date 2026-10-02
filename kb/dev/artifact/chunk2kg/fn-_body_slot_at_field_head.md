---
id: https://agentic-knowledge-base.dev/id/chunk/a88529ad-7941-47a8-a7ae-eb1866d89efc
type: artifact
level: executable
title_ko: 함수 _body_slot_at_field_head (tools/chunk2kg.py)
title: function _body_slot_at_field_head in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d2327845-e19c-432e-bef7-b5d429601fb6
---
**함수** — `_body_slot_at_field_head(line, start)` 다. `start` 위치의 굵은 span 이 그 줄의 "필드 자리"에 있는가 — 줄 머리(불릿 다음) 또는 앞선 필드의 ` · ` 구분자 다음.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _body_slot_at_field_head(line: str, start: int) -> bool:
    """`start` 위치의 굵은 span 이 그 줄의 "필드 자리"에 있는가 — 줄 머리(불릿 다음) 또는 앞선 필드의
    ` · ` 구분자 다음. 표 셀·산문 접속·목록 항목 전체를 감싼 굵기는 이 자리가 아니다(위 BODY_SLOT_SPAN 주석)."""
    prefix = BODY_SLOT_BULLET.sub("", line[:start], count=1)
    while True:
        idx = prefix.find(BODY_SLOT_FIELD_SEP)
        if idx == -1:
            break
        prefix = prefix[idx + len(BODY_SLOT_FIELD_SEP):]
    return prefix.strip() == ""
```
<!-- 인용 끝 -->
