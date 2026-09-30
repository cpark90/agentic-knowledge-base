---
id: https://agentic-knowledge-base.dev/id/chunk/4600b6bb-eddb-4832-9854-1c587f7929d9
type: artifact
level: executable
title_ko: 함수 as_dt (tools/weave.py)
title: function as_dt in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
---
**함수** — `as_dt(value)` 다. ISO 8601 → aware datetime (시간대 없는 값은 UTC 로 본다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def as_dt(value: str):
    """ISO 8601 → aware datetime (시간대 없는 값은 UTC 로 본다). 파싱 불가면 None."""
    try:
        d = datetime.fromisoformat(value)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
```
<!-- 인용 끝 -->
