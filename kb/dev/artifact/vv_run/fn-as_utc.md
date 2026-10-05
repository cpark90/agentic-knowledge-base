---
id: https://agentic-knowledge-base.dev/id/chunk/fae9d002-8656-4bb1-a04e-18a04452ff08
type: artifact
level: executable
title_ko: 함수 as_utc (tools/vv_run.py)
title: function as_utc in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
---
**함수** — `as_utc(value)` 다. frontmatter 의 시각 → aware datetime.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def as_utc(value) -> datetime | None:
    """frontmatter 의 시각 → aware datetime. 시간대 없는 값은 UTC 로 본다. 읽을 수 없으면 None."""
    try:
        d = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
```
<!-- 인용 끝 -->
