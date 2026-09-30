---
id: https://agentic-knowledge-base.dev/id/chunk/3d72bcbf-9fce-4ada-9c3b-fff4759fa5fd
type: artifact
level: executable
title_ko: 함수 label_of (tools/assume_check.py)
title: function label_of in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/b33ba404-d208-425c-9ca3-34d8bec67ead
---
**함수** — `label_of(g, node)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_of(g: Graph, node) -> str:
    ko = next((str(l) for l in g.objects(node, RDFS.label) if getattr(l, "language", None) == "ko"), None)
    return ko or next((str(l) for l in g.objects(node, RDFS.label)), local(node))
```
<!-- 인용 끝 -->
