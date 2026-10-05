---
id: https://agentic-knowledge-base.dev/id/chunk/fd21796e-0d7a-4cf4-b8bf-9b2f659a1853
type: artifact
level: executable
title_ko: 절 union-graph-paths (tools/kb_lib.py)
title: section union-graph-paths in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd
composite: {id: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd, title_ko: 절 복합체 union-graph-paths (tools/kb_lib.py), title: section composite union-graph-paths in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/fd21796e-0d7a-4cf4-b8bf-9b2f659a1853, https://agentic-knowledge-base.dev/id/chunk/f05d76f0-e96f-4c89-a78e-86eeb1bf91d1, https://agentic-knowledge-base.dev/id/chunk/808534e8-8fca-4ace-ace9-9e4b7084233e, https://agentic-knowledge-base.dev/id/chunk/5b372e8e-c287-4ed0-b9d6-16c0366ee0c8, https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55, https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e], part_of: https://agentic-knowledge-base.dev/id/composite/cd5a8ce9-a52a-40c7-89b0-b41f163cfde2}
---
**절** — `tools/kb_lib.py` 의 절 `union-graph-paths` 다. 그래프 union 과 라벨 인터페이스 (query · cq 뷰)

**정의** — `resolve_path` · `resolve_glob` · `load_union` · `compact_iri` · `chunk_body` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 그래프 union 과 라벨 인터페이스 (query · cq 뷰) ────────────────────────────────────────────────
# 활용 도구가 읽는 그래프 — metrics 와 같은 입력(head·참조·시드·카탈로그·복합체·게이트·ODD)에 온톨로지 모듈을 더한 union.
# 경로는 워크스페이스 상대이고 `bazel run` 의 runfiles 에는 data 로 같은 경로에 놓인다. 온톨로지는 모듈 디렉토리 재귀 glob.
UNION_GRAPH_PATHS = ("kg/chunks-kg.ttl", "kg/references-kg.ttl", "kg/base-kg.ttl", "kg/catalog-kg.ttl", "kg/composite-kg.ttl",
                     "kg/gates-kg.ttl", "kb/odd/project-odd.ttl")
UNION_GRAPH_GLOBS = ("kb/ontology/**/*-ontology.ttl",)
# IRI 축약 — 표 출력용. rdflib 의 qname 은 로컬부에 `/` 가 있는 청크 IRI(id:chunk/<uuid>)를 만들지 못한다
COMPACT_PREFIXES = ((str(AGT), "agt:"), (str(ID), "id:"), ("http://www.w3.org/ns/prov#", "prov:"),
                    (str(RDFS), "rdfs:"), (str(OWL), "owl:"), (str(RDF), "rdf:"),
                    ("http://www.w3.org/2004/02/skos/core#", "skos:"), ("http://www.w3.org/2001/XMLSchema#", "xsd:"))
```
<!-- 인용 끝 -->
