---
id: https://agentic-knowledge-base.dev/id/chunk/fd21796e-0d7a-4cf4-b8bf-9b2f659a1853
type: artifact
level: executable
title_ko: 절 union-graph-paths (tools/kb_lib.py)
title: section union-graph-paths in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/cd5a8ce9-a52a-40c7-89b0-b41f163cfde2
---
**절** — `tools/kb_lib.py` 의 절 `union-graph-paths` 다. 그래프 union 과 라벨 인터페이스 (query · cq 뷰)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 그래프 union 과 라벨 인터페이스 (query · cq 뷰) ────────────────────────────────────────────────
# 활용 도구가 읽는 그래프 — metrics 와 같은 입력(head·참조·시드·카탈로그·복합체·게이트·ODD)에 온톨로지 모듈을 더한 union.
# 경로는 두 뿌리로 푼다 (task 0327 손질 5). **호출 저장소의 지식**(아래 `UNION_GRAPH_PATHS` · 호출 저장소의 온톨로지 확장)은
# 작업 디렉토리 기준이다 — runfiles(현재 디렉토리) → `<뿌리>/bazel-bin` → `<뿌리>` 순이고 뿌리는 `bazel run` 의
# `BUILD_WORKSPACE_DIRECTORY` 다. **이 모듈의 코어**(온톨로지 모듈 · 판정 프로파일 · shape)는 `core_root()` 기준이다 — runfiles
# 에서는 이 모듈의 저장소 디렉토리이고 소스에서 직접 돌리면 이 저장소다. 이 저장소가 루트면 두 뿌리가 같은 파일을 가리키므로
# 실경로로 중복을 뺀다.
UNION_GRAPH_PATHS = ("kg/chunks-kg.ttl", "kg/references-kg.ttl", "kg/base-kg.ttl", "kg/catalog-kg.ttl", "kg/composite-kg.ttl",
                     "kg/gates-kg.ttl", "kb/odd/project-odd.ttl")
UNION_GRAPH_GLOBS = ("kb/ontology/**/*-ontology.ttl",)
# IRI 축약 — 표 출력용. rdflib 의 qname 은 로컬부에 `/` 가 있는 단위 지식 IRI(id:chunk/<uuid>)를 만들지 못한다
COMPACT_PREFIXES = ((str(AGT), "agt:"), (str(ID), "id:"), ("http://www.w3.org/ns/prov#", "prov:"),
                    (str(RDFS), "rdfs:"), (str(OWL), "owl:"), (str(RDF), "rdf:"),
                    ("http://www.w3.org/2004/02/skos/core#", "skos:"), ("http://www.w3.org/2001/XMLSchema#", "xsd:"))
```
<!-- 인용 끝 -->
