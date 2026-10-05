---
id: https://agentic-knowledge-base.dev/id/chunk/c730fd69-c542-4d85-92ae-38125ac16f18
type: artifact
level: executable
title_ko: 모듈 머리 kind-type (tools/term_propose.py)
title: module head kind-type in tools/term_propose.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-term-propose}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/3eff15a8-c6b8-46a9-a707-b95a948c619d
composite: {id: https://agentic-knowledge-base.dev/id/composite/3eff15a8-c6b8-46a9-a707-b95a948c619d, title_ko: 모듈 머리 복합체 kind-type (tools/term_propose.py), title: section composite kind-type in tools/term_propose.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c730fd69-c542-4d85-92ae-38125ac16f18, https://agentic-knowledge-base.dev/id/chunk/0f329565-00ac-4268-a110-cf18eaef3332, https://agentic-knowledge-base.dev/id/chunk/2d62de0c-4e57-4e6c-ba4e-85fe1ebdc37f], part_of: https://agentic-knowledge-base.dev/id/composite/f141ce57-8f04-4bda-a9ff-756f81f57846}
---
**모듈 머리** — `tools/term_propose.py` 의 모듈 머리 `kind-type` 다. 모듈 머리

**정의** — `ontology_graph` · `chunk_types` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
KIND_TYPE = {
    "class": "owl:Class",
    "object-property": "owl:ObjectProperty",
    "datatype-property": "owl:DatatypeProperty",
    "individual": "owl:NamedIndividual",
}
KIND_PARENT_PRED = {
    "class": "rdfs:subClassOf",
    "object-property": "rdfs:subPropertyOf",
    "datatype-property": "rdfs:subPropertyOf",
}
# 근거가 될 수 있는 청크 종류 — 일반화의 입력은 관측과 판정 주석이다 (노트 14.1)
EVIDENCE_TYPES = ("memory", "annotation")
MIN_EVIDENCE = 2
ONTOLOGY_DIR = Path("kb") / "ontology"
EXCLUDED_SUBDIRS = ("proposals", "shapes")  # 큐 자신과 shape 는 어휘의 원본이 아니다
```
<!-- 인용 끝 -->
