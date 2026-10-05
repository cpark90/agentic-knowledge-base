---
id: https://agentic-knowledge-base.dev/id/chunk/76dd3d85-14b0-4166-9ac3-75140ae7ea66
type: artifact
level: executable
title_ko: 함수 future_at (tools/endorse.py)
title: function future_at in tools/endorse.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-endorse}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e9580aea-56ec-4ca6-a78d-95befb50b334
---
**함수** — `future_at(at)` 다. `--at` 이 읽히지 않거나 지금보다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def future_at(at: str) -> str:
    """`--at` 이 읽히지 않거나 지금보다 뒤이면 거부 사유를, 아니면 빈 문자열을 낸다. 시간대가 없으면 지역 시각으로 읽는다."""
    try:
        when = datetime.fromisoformat(at.strip().replace("Z", "+00:00"))
    except ValueError:
        return f"--at {at!r} 이 ISO 8601 이 아니다"
    when = when.astimezone() if when.tzinfo is None else when
    now = datetime.now(timezone.utc)
    if when > now:
        return f"--at {at} 이 지금({now.isoformat(timespec='seconds')})보다 뒤다 — 도장 시각은 `date -Iseconds` 실측값을 쓴다"
    return ""
```
<!-- 인용 끝 -->
