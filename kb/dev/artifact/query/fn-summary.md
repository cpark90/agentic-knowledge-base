---
id: https://agentic-knowledge-base.dev/id/chunk/01f3ebf5-d8ae-43ce-94b0-5cc0537f8dd0
type: artifact
level: executable
title_ko: 함수 summary (tools/query.py)
title: function summary in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/4358cd56-6be2-4ce1-9f2f-9fb0ed47b5d3
---
**함수** — `summary(g, queries, bindings)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def summary(g: Graph, queries: list[CqQuery], bindings: dict) -> tuple[list[str], list[tuple[CqQuery, list[str], list[tuple]]]]:
    results = []
    for q in queries:
        cols, rows = run(g, q, bindings)
        results.append((q, cols, rows))
    lines = table(["CQ", "질문", "행"], [[q.id, q.question.replace("|", "\\|"), str(len(rows))] for q, _, rows in results])
    return lines, results
```
<!-- 인용 끝 -->
