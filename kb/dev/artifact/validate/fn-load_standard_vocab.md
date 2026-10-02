---
id: https://agentic-knowledge-base.dev/id/chunk/fd4f59ff-fa52-4ead-afda-fc34d6efe930
type: artifact
level: executable
title_ko: 함수 load_standard_vocab (tools/validate.py)
title: function load_standard_vocab in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f9f4e245-6a05-4f51-b5b5-532470213ed5]
part_of: https://agentic-knowledge-base.dev/id/composite/2bbdac5b-e7f6-4ca1-b5fd-04c0513178d1
---
**함수** — `load_standard_vocab(paths)` 다. 등록 표준 어휘 원문(PROV-O·SKOS — MODULE.bazel 의 http_file 이 해시 고정으로 가져온다)이 정의하는 용어와, 검사 대상이 되는 네임스페이스.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_standard_vocab(paths: list[str]) -> tuple[set[URIRef], set[str]]:
    """등록 표준 어휘 원문(PROV-O·SKOS — MODULE.bazel 의 http_file 이 해시 고정으로 가져온다)이
    정의하는 용어와, 검사 대상이 되는 네임스페이스.

    네임스페이스는 원문이 정의한 용어에서 파생한다(PROV-O 원문은 rdfs·owl 주석 속성도 선언하므로
    기본 어휘 넷은 뺀다) — 원문을 하나 더 등록하면 그 어휘가 그대로 검사 대상이 된다.
    """
    from rdflib.util import guess_format

    terms: set[URIRef] = set()
    for p in paths:
        g = Graph()
        g.parse(p, format=guess_format(p) or "turtle")
        for t in kb_lib.DEFINING_TYPES:
            terms |= {s for s in g.subjects(RDF.type, t) if isinstance(s, URIRef)}
    base = {str(RDF), str(RDFS), str(OWL), str(XSD)}
    return terms, {_namespace(t) for t in terms} - base
```
<!-- 인용 끝 -->
