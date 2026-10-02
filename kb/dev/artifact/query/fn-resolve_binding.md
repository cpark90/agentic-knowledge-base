---
id: https://agentic-knowledge-base.dev/id/chunk/26644059-7309-45ef-a32b-71465fa1d2fb
type: artifact
level: executable
title_ko: 함수 resolve_binding (tools/query.py)
title: function resolve_binding in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55]
part_of: https://agentic-knowledge-base.dev/id/composite/804dd9bd-ceaa-4ecc-9233-ef543578feb9
---
**함수** — `resolve_binding(g, spec)` 다. --bind ?var=value → (var, term).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve_binding(g: Graph, spec: str):
    """--bind ?var=value → (var, term). value 는 IRI · id:슬러그 · agt:용어 · 정수 · 라벨(ko/en 정확 일치). 모호하거나 없으면 ValueError."""
    if "=" not in spec:
        raise ValueError(f"--bind {spec!r}: ?var=value 형식이어야 한다")
    var, value = spec.split("=", 1)
    var = var.lstrip("?").strip()
    value = value.strip()
    if not var or not value:
        raise ValueError(f"--bind {spec!r}: 변수와 값이 비어 있으면 안 된다")
    if value.startswith("http://") or value.startswith("https://"):
        return var, URIRef(value)
    if value.startswith("id:"):
        return var, ID[value[3:]]
    if value.startswith("agt:"):
        return var, AGT[value[4:]]
    if re.fullmatch(r"-?\d+", value):
        return var, Literal(int(value))
    hits = sorted({s for s, lab in g.subject_objects(RDFS.label) if str(lab) == value}, key=str)
    if len(hits) == 1:
        return var, hits[0]
    if not hits:
        raise ValueError(f"--bind {spec!r}: 라벨 {value!r} 인 개체가 없다 (IRI·id:·agt: 표기도 된다)")
    raise ValueError(f"--bind {spec!r}: 라벨 {value!r} 인 개체가 {len(hits)}개다 — IRI 로 지정한다: " + ", ".join(kb_lib.compact_iri(str(h)) for h in hits))
```
<!-- 인용 끝 -->
