---
id: https://agentic-knowledge-base.dev/id/chunk/af69ce06-f9ea-4d33-925e-a9d15a919ab6
type: artifact
level: executable
title_ko: 함수 run (tools/query.py)
title: function run in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/804dd9bd-ceaa-4ecc-9233-ef543578feb9
---
**함수** — `run(g, q, bindings)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def run(g: Graph, q: CqQuery, bindings: dict) -> tuple[list[str], list[tuple]]:
    res = g.query(q.prepared, initBindings=bindings)
    cols = [str(v) for v in res.vars] if res.vars else []
    return cols, [tuple(row) for row in res]
```
<!-- 인용 끝 -->
