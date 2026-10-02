---
id: https://agentic-knowledge-base.dev/id/chunk/f25447a7-4301-4ae4-b0a6-d22f459cd775
type: artifact
level: executable
title_ko: 함수 load_graph (tools/kb_lib.py)
title: function load_graph in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294
---
**함수** — `load_graph(path)` 다. TTL 파일 하나를 파싱한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_graph(path: str | Path) -> Graph:
    """TTL 파일 하나를 파싱한다. 파싱 실패는 그 자체가 게이트 실패다."""
    g = Graph()
    g.parse(str(path), format="turtle")
    return g
```
<!-- 인용 끝 -->
