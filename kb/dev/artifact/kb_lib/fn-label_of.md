---
id: https://agentic-knowledge-base.dev/id/chunk/104f7d3c-d114-46c9-aab7-b44761117813
type: artifact
level: executable
title_ko: 함수 label_of (tools/kb_lib.py)
title: function label_of in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/cfe0afad-9ee7-4e4c-9283-5fddef1781ff
---
**함수** — `label_of(g, node, lang)` 다. 개체의 rdfs:label — 요청 언어 → 다른 언어 → 축약 IRI 순.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_of(g: Graph, node, lang: str = "ko") -> str:
    """개체의 rdfs:label — 요청 언어 → 다른 언어 → 축약 IRI 순. 라벨이 인터페이스다 (p4-label-is-the-interface)."""
    labels = list(g.objects(node, RDFS.label))
    for lab in labels:
        if getattr(lab, "language", None) == lang:
            return str(lab)
    return str(labels[0]) if labels else compact_iri(str(node))
```
<!-- 인용 끝 -->
