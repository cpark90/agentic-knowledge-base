---
id: https://agentic-knowledge-base.dev/id/chunk/c730fd69-c542-4d85-92ae-38125ac16f18
type: artifact
level: executable
title_ko: 모듈 머리 kind-type (tools/term_propose.py)
title: module head kind-type in tools/term_propose.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-term-propose}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-10T17:03:35Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/4754eb68-ad27-45ad-912c-0385087cd063, https://agentic-knowledge-base.dev/id/chunk/b136d285-c4ba-461b-99cf-bda07c2243d8]
part_of: https://agentic-knowledge-base.dev/id/composite/f141ce57-8f04-4bda-a9ff-756f81f57846
---
**모듈 머리** — `tools/term_propose.py` 의 모듈 머리 `kind-type` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
KIND_TYPE = {
    "class": "owl:Class",
    "object-property": "owl:ObjectProperty",
    "datatype-property": "owl:DatatypeProperty",
}
KIND_PARENT_PRED = {
    "class": "rdfs:subClassOf",
    "object-property": "rdfs:subPropertyOf",
    "datatype-property": "rdfs:subPropertyOf",
}
```
<!-- 인용 끝 -->
