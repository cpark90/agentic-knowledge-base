---
id: https://agentic-knowledge-base.dev/id/chunk/6da8f646-2923-45e6-9bf8-eace123f2901
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/kb_lib.py)
title: module head agt in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/7aee7ddf-f82b-4788-88ce-b27bd5290481
composite: {id: https://agentic-knowledge-base.dev/id/composite/7aee7ddf-f82b-4788-88ce-b27bd5290481, title_ko: 모듈 머리 복합체 agt (tools/kb_lib.py), title: section composite agt in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/6da8f646-2923-45e6-9bf8-eace123f2901, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99, https://agentic-knowledge-base.dev/id/chunk/f4d0d4bb-6623-435e-b230-93d98fb7ceac, https://agentic-knowledge-base.dev/id/chunk/f25447a7-4301-4ae4-b0a6-d22f459cd775, https://agentic-knowledge-base.dev/id/chunk/01fd5990-0c31-4b71-8dcd-ee095148db30, https://agentic-knowledge-base.dev/id/chunk/8d31b7a9-85c6-48b3-875b-1223f473d503, https://agentic-knowledge-base.dev/id/chunk/90abf3f7-3c52-496f-9cb4-a2af556264cb], part_of: https://agentic-knowledge-base.dev/id/composite/dca529bc-79c6-4569-af4c-122c0d736686}
---
**모듈 머리** — `tools/kb_lib.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — `kb_of` · `load_residency` · `load_graph` · `load_merged` · `defined_terms` · `is_well_known` (소스 순서).

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
CATALOG_GATE = "catalog"  # 게이트 id — FAIL [catalog]
WRITER_GATE = "writer"    # 게이트 id — FAIL [writer]
# 두 KB 의 경로 접두 (pe-storage-layout) — 역할의 agt:writesIn 값이자 청크 assertionLocation 의 KB 판정 기준 (p8-vv-roles, 2026-09-19).
# gen_build 는 rdflib 없이 돌므로 같은 접두를 자체 상수(VV_ROOT)로 갖는다 — chunk2kg 의 PLANE 상수와 같은 사유
KB_DEV = "kb/dev"
KB_VV = "kb/vv"
KB_ROOTS = (KB_DEV, KB_VV)




# 수준 허용표의 단일 정의처 — `defs/kb.bzl` 의 `LEVELS`·`RESIDENCY` 리터럴이다 (M1 단일 정의처, 2026-09-26).
# Starlark 는 파일을 읽지 못하므로 표는 Starlark 쪽에 있어야 하고, 파이썬은 그 리터럴을 읽어 파생한다.
# 파생처는 둘이다 — `tools/metrics.py` 의 거주 위반 지표와 `tools/validate.py` 의 게이트 `residency`
# (shape `residency-shapes.ttl` 이 이 표와 같은지 판정한다).
RESIDENCY_GATE = "residency"  # 게이트 id — FAIL [residency]
_BZL_RESIDENCY = re.compile(r"^\s*RESIDENCY\s*=\s*\{(.*?)^\}", re.M | re.S)



# 온톨로지 모듈이 "정의"로 간주되는 타입 (2.3절 경계 규칙, 2.5절 정의 완전성)
DEFINING_TYPES = (
    OWL.Class,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    OWL.NamedIndividual,
    RDFS.Class,
    RDF.Property,
)
```
<!-- 인용 끝 -->
