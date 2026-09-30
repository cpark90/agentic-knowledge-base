---
id: https://agentic-knowledge-base.dev/id/chunk/811c8a9a-7991-488b-927b-a703841a532b
type: artifact
level: executable
title_ko: 모듈 머리 exit-fail (tools/canonicalize.py)
title: module head exit-fail in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/a9cc1a02-29b3-4f53-8711-8d60a4bea3cf]
part_of: https://agentic-knowledge-base.dev/id/composite/cf91a784-b983-40fa-afff-ff9105164656
---
**모듈 머리** — `tools/canonicalize.py` 의 모듈 머리 `exit-fail` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)

STANDARD_PREFIXES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "sh": "http://www.w3.org/ns/shacl#",
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "co": "http://purl.org/co/",
    "obo": "http://purl.obolibrary.org/obo/",
    "agt": "https://agentic-knowledge-base.dev/agt/",
}


# 접두어 축약이 안전한 로컬 이름만 축약한다. 그 밖은 <IRI> 그대로.
_PN_LOCAL = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]*$")
```
<!-- 인용 끝 -->
