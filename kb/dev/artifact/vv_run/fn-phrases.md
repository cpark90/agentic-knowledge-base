---
id: https://agentic-knowledge-base.dev/id/chunk/13d0468f-ac80-47c0-9d27-cafd3ef8ffaf
type: artifact
level: executable
title_ko: 함수 phrases (tools/vv_run.py)
title: function phrases in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `phrases(value)` 다. `contains` 의 값 → 문구 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def phrases(value) -> list[str]:
    """`contains` 의 값 → 문구 목록. 문구 하나는 문자열로도 적는다."""
    return [value] if isinstance(value, str) else list(value or [])
```
<!-- 인용 끝 -->
