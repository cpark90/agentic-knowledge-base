---
id: https://agentic-knowledge-base.dev/id/chunk/9a10d17d-c778-4340-b082-b27d4e75e275
type: artifact
level: executable
title_ko: 함수 _around (tools/kb_lib.py)
title: function _around in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/99dbbf72-57fc-4b1b-91bd-ef07be848f6e
---
**함수** — `_around(seg, start, end, width)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _around(seg: str, start: int, end: int, width: int = 24) -> str:
    return seg[max(0, start - width):end + width].strip()
```
<!-- 인용 끝 -->
