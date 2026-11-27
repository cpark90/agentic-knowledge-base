---
id: https://agentic-knowledge-base.dev/id/chunk/ddcf73be-8915-4f3c-a82b-2bd4efea17cd
type: artifact
level: executable
title_ko: 절 catalog-file (tools/canonicalize.py)
title: section catalog-file in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/48c79ecc-7011-4d44-bc3e-be0cc65036b7
composite: {id: https://agentic-knowledge-base.dev/id/composite/48c79ecc-7011-4d44-bc3e-be0cc65036b7, title_ko: 절 복합체 catalog-file (tools/canonicalize.py), title: section composite catalog-file in tools/canonicalize.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/ddcf73be-8915-4f3c-a82b-2bd4efea17cd, https://agentic-knowledge-base.dev/id/chunk/d8eae456-6327-477b-8cb2-b53024a57d90, https://agentic-knowledge-base.dev/id/chunk/72c905c8-58fa-4d17-8305-7a26c700de4e, https://agentic-knowledge-base.dev/id/chunk/8f13de9c-0e9b-48f7-9212-7bbc47a6f349], part_of: https://agentic-knowledge-base.dev/id/composite/cf91a784-b983-40fa-afff-ff9105164656}
---
**절** — `tools/canonicalize.py` 의 절 `catalog-file` 다. OWL 대응표 — 표준 OWL 도구가 owl:imports 를 로컬 파일로 풀게 하는 OASIS XML Catalog (Q176-a·Q177-c)

**정의** — `module_graph` · `catalog_xml` · `write_catalog` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── OWL 대응표 — 표준 OWL 도구가 owl:imports 를 로컬 파일로 풀게 하는 OASIS XML Catalog (Q176-a·Q177-c) ────────
# XML Catalog 는 IRI 하나를 파일 하나에 대응시키는데, 모듈은 디렉토리이고 파일이 여럿이며 owl:Ontology 선언이 없다.
# 그래서 모듈마다 원본 파일을 합친 합본에 `<모듈 IRI> a owl:Ontology` 머리를 더하고, 대응표와 최상위 파일 사본을
# 한 디렉토리에 둔다. 출력은 bazel-out 에만 있다(pe-generated-outputs-stay-in-bazel-out). IRI 의 원본은 모듈 BUILD 의
# `iri` 이고 규칙 `kb_owl_catalog`(defs/knowledge.bzl)가 OntologyModuleInfo 에서 읽어 인자로 넘긴다.

CATALOG_FILE = "catalog-v001.xml"  # Protégé·OWL API·ROBOT 가 온톨로지 옆에서 찾는 이름
CATALOG_NS = "urn:oasis:names:tc:entity:xmlns:xml:catalog"








if __name__ == "__main__":
    sys.exit(main())
```
<!-- 인용 끝 -->
