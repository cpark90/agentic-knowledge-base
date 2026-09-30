---
id: https://agentic-knowledge-base.dev/id/chunk/07b3db3b-4826-4478-878d-5e9c9d7d4ae0
type: artifact
level: executable
title_ko: 함수 render_query (tools/query.py)
title: function render_query in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/4358cd56-6be2-4ce1-9f2f-9fb0ed47b5d3
---
**함수** — `render_query(g, q, bindings, limit, labels)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_query(g: Graph, q: CqQuery, bindings: dict, limit: int, labels: bool) -> list[str]:
    cols, rows = run(g, q, bindings)
    shown = rows if limit <= 0 else rows[:limit]
    out = [f"## {q.id} — {q.question}", f"{FORM_PREFIX}{q.form}" if q.form else "", ""]
    if cols:
        out += table(cols, [[cell(g, t, labels) for t in r] for r in shown])
    tail = f"행 {len(rows)}"
    if len(shown) < len(rows):
        tail += f" (표시 {len(shown)} — --limit 0 이 전부)"
    if bindings:
        tail += " · bind " + ", ".join(f"?{k}={kb_lib.compact_iri(str(v))}" for k, v in bindings.items())
    out += ["", tail]
    return [ln for ln in out if ln is not None]
```
<!-- 인용 끝 -->
