---
id: https://agentic-knowledge-base.dev/id/chunk/0c73f827-eef2-4929-a126-f9b2c056d037
type: artifact
level: executable
title_ko: 함수 now_utc (tools/kb_lib.py)
title: function now_utc in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
---
**함수** — `now_utc()` 다. G3 의 생성 시각 — ISO 8601 UTC 초 해상도.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def now_utc() -> str:
    """G3 의 생성 시각 — ISO 8601 UTC 초 해상도."""
    return utc_stamp(datetime.now(timezone.utc))
```
<!-- 인용 끝 -->
