---
id: https://agentic-knowledge-base.dev/id/chunk/0d94f5a5-2678-4f1b-9143-2847818c4669
type: artifact
level: executable
title_ko: 함수 created_at (tools/channel_lint.py)
title: function created_at in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/30c94888-c0b3-4616-8c73-db2b38068fb2
---
**함수** — `created_at(value, tz)` 다. `created` → 시각.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def created_at(value: str, tz) -> datetime.datetime | None:
    """`created` → 시각. 날짜뿐이면(질문지) 그날 0시(tz)로 읽는다. 읽을 수 없으면 None."""
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return datetime.datetime.combine(datetime.date.fromisoformat(value), datetime.time(), tz)
        when = datetime.datetime.fromisoformat(value)
    except ValueError:
        return None
    return when if when.tzinfo else when.replace(tzinfo=tz)
```
<!-- 인용 끝 -->
