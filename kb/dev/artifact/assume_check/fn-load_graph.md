---
id: https://agentic-knowledge-base.dev/id/chunk/a49b0fbe-30fd-4d2c-8b92-f99763bd47af
type: artifact
level: executable
title_ko: 함수 load_graph (tools/assume_check.py)
title: function load_graph in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b33ba404-d208-425c-9ca3-34d8bec67ead
---
**함수** — `load_graph(paths, root)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_graph(paths: list[str], root: Path) -> tuple[Graph, list[str]]:
    g, missing = Graph(), []
    for p in paths:
        f = resolve(p, root)
        if f is None:
            missing.append(p)
            continue
        g.parse(str(f), format="turtle")
    return g, missing
```
<!-- 인용 끝 -->
