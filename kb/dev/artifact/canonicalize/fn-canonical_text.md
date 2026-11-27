---
id: https://agentic-knowledge-base.dev/id/chunk/221ff1dd-1b9e-4518-831b-2c8e960001ac
type: artifact
level: executable
title_ko: 함수 canonical_text (tools/canonicalize.py)
title: function canonical_text in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/639f6e6c-93f1-4f2e-97b5-e3ce99cc31fc]
part_of: https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389
---
**함수** — `canonical_text(path)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def canonical_text(path: Path) -> str:
    g = Graph()
    g.parse(str(path), format="turtle")
    return canonical_graph_text(g)
```
<!-- 인용 끝 -->
