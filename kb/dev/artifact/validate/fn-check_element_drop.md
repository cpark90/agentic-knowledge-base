---
id: https://agentic-knowledge-base.dev/id/chunk/6bf4337c-24c7-4689-8354-d179c822e031
type: artifact
level: executable
title_ko: 함수 check_element_drop (tools/validate.py)
title: function check_element_drop in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/621b8722-ef63-42b3-8470-9560e072a62a
---
**함수** — `check_element_drop(ontology, chunk_files)` 다. 소스 요소의 전수와 방출 전수의 차 (게이트 id `element-drop`, 현상 P19 의 관측 수단).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_element_drop(ontology: Graph | None, chunk_files: list[str]) -> list[str]:
    """소스 요소의 전수와 방출 전수의 차 (게이트 id `element-drop`, 현상 P19 의 관측 수단).

    참조 저장소 R3 이 남긴 형태 — 반영이 알려진 요소 집합에서 조립되므로 어휘가 없는 소스 요소는 슬롯을 얻지
    못해 조용히 빠진다. 그것을 잡으려면 소스를 전수로 세고 방출과 대조하는 수밖에 없다. 차가 나오면 대응은
    요소를 버리는 것이 아니라 어휘를 넓히는 것이다 (가정 id:asm-missing-vocabulary-is-signal).
    """
    errors = []
    consumed = set(chunk2kg.REQUIRED) | set(chunk2kg.LINK_KEYS) | set(kb_lib.CHUNK_OPTIONAL_KEYS)
    for path in sorted(chunk_files):
        for key in sorted(_frontmatter_keys(path) - consumed):
            errors.append(f"[{kb_lib.ELEMENT_DROP_GATE}] {path}: frontmatter 키 {key!r} 를 chunk2kg 가 소비하지 않는다 — "
                          f"방출되지 않는 키는 조용히 버려지는 소스 요소다. 키를 쓰려면 chunk2kg 가 읽고 "
                          f"kb_lib.CHUNK_OPTIONAL_KEYS 에 등재해야 한다 (8.21절 G1 현상 P19)")
    if ontology is None:
        return errors
    plane_classes = {URIRef(str(AGT) + q.split(":", 1)[1]) for q in chunk2kg.PLANE_CLASS.values()}
    declared = {s for s, o in ontology.subject_objects(RDFS.subClassOf) if o in plane_classes}
    emitted = {URIRef(str(AGT) + q.split(":", 1)[1]) for q in chunk2kg.PROFILE_SUBSTANCE.values()}
    for term in sorted(declared - emitted, key=str):
        errors.append(f"[{kb_lib.ELEMENT_DROP_GATE}] {_where({}, term)}: 실체 클래스 {ontology.qname(term)} 가 어휘에만 있다 — "
                      f"chunk2kg.PROFILE_SUBSTANCE 가 어느 plane 도 이 클래스로 타이핑하지 않아 데이터가 닿지 않는다 (CQ-28 고립 개념)")
    for term in sorted(emitted - declared, key=str):
        errors.append(f"[{kb_lib.ELEMENT_DROP_GATE}] chunk2kg.PROFILE_SUBSTANCE: 실체 클래스 {term} 가 생성기에만 있다 — "
                      f"프로파일이 plane 청크 클래스의 하위로 선언하지 않았다. 정의 없는 클래스는 어휘 밖이다 (2.3절 경계 규칙)")
    return errors
```
<!-- 인용 끝 -->
