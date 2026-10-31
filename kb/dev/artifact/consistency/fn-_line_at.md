---
id: https://agentic-knowledge-base.dev/id/chunk/cd5413ed-eaa2-466b-b701-bb182e0a5377
type: artifact
level: executable
title_ko: 함수 _line_at (tools/consistency.py)
title: function _line_at in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
---
**함수** — `_line_at(starts, pos)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _line_at(starts: list[tuple[int, int]], pos: int) -> int:
    return max((ln for s, ln in starts if s <= pos), default=starts[0][1])
```
<!-- 인용 끝 -->
