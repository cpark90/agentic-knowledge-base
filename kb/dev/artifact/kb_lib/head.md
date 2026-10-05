---
id: https://agentic-knowledge-base.dev/id/chunk/6da8f646-2923-45e6-9bf8-eace123f2901
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/kb_lib.py)
title: module head agt in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/dca529bc-79c6-4569-af4c-122c0d736686
---
**모듈 머리** — `tools/kb_lib.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# 이 체계 고유 어휘 (노트 0.3절, 0.7절)
AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
ID = Namespace("https://agentic-knowledge-base.dev/id/")
PROV = Namespace("http://www.w3.org/ns/prov#")  # 출처·귀속·특수화는 PROV-O 만 쓴다 (STYLEGUIDE §5)

# 외부 표준 어휘 — 정의를 변경하지 않고 그대로 쓴다 (0.3절)
WELL_KNOWN_PREFIXES = (
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#",   # rdf
    "http://www.w3.org/2000/01/rdf-schema#",          # rdfs
    "http://www.w3.org/2002/07/owl#",                 # owl
    "http://www.w3.org/2001/XMLSchema#",              # xsd
    "http://www.w3.org/2004/02/skos/core#",           # skos
    "http://www.w3.org/ns/shacl#",                    # sh
    "http://www.w3.org/ns/prov#",                     # prov
    "http://purl.org/dc/terms/",                      # dcterms
    "http://purl.org/co/",                            # co (Collections Ontology)
    "http://purl.obolibrary.org/obo/",                # bfo / iao / ro
)

# 산출물 접미사 (0.2절 + SHACL shape 파일용 -shapes 확장)
ALLOWED_TTL_SUFFIXES = (
    "-ontology",
    "-rules",
    "-shapes",
    "-space",
    "-kg",
    "-odd",
)

# 개체 IRI 접두사 (docs/rules.md §개체 IRI 접두사) — 카탈로그 정합성 검사(validate `catalog`)가 역할 ↔ 스코프 대응을
# id:role-<slug> ↔ id:scope-<slug> 로 푼다. 카탈로그에 역할→스코프 술어는 없고 슬러그가 대응의 원본이다 (STYLEGUIDE §5)
ROLE_ID_PREFIX = "role-"
SCOPE_ID_PREFIX = "scope-"
# ODD 동적 요소 — 역할별 agt:maxConcurrent 합의 상한 (AGENTS.md 역할 절, kb/odd/project-odd.yml concurrent_agents)
CONCURRENT_AGENTS_CONDITION = ID["cond-concurrent-agents"]
```
<!-- 인용 끝 -->
