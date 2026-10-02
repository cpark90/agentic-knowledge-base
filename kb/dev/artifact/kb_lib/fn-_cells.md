---
id: https://agentic-knowledge-base.dev/id/chunk/e0b9b281-fec0-43a8-ab40-b41e13278f6a
type: artifact
level: executable
title_ko: 함수 _cells (tools/kb_lib.py)
title: function _cells in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee34751d-8520-4de7-a22b-b2a1136b9dbf
---
**함수** — `_cells(line)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]
```
<!-- 인용 끝 -->
