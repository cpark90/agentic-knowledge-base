---
id: https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a
type: artifact
level: executable
title_ko: 함수 _term (tools/validate.py)
title: function _term in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13
---
**함수** — `_term(g, term)` 다. 클래스·공리의 표기 — agt:·id:·owl:·rdfs: 는 접두사로, 나머지는 IRI 전체로 적는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _term(g: Graph, term) -> str:
    """클래스·공리의 표기 — agt:·id:·owl:·rdfs: 는 접두사로, 나머지는 IRI 전체로 적는다."""
    for prefix, ns in (("agt", AGT), ("id", kb_lib.ID), ("owl", OWL), ("rdfs", RDFS)):
        if str(term).startswith(str(ns)):
            return f"{prefix}:{str(term)[len(str(ns)):]}"
    return f"<{term}>" if isinstance(term, URIRef) else str(term)
```
<!-- 인용 끝 -->
