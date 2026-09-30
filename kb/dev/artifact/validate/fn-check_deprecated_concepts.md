---
id: https://agentic-knowledge-base.dev/id/chunk/f5d521a5-98ba-4f17-ada0-7ddbb7162850
type: artifact
level: executable
title_ko: 함수 check_deprecated_concepts (tools/validate.py)
title: function check_deprecated_concepts in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/040c4845-cfe9-495a-91c7-f98702044ca6
---
**함수** — `check_deprecated_concepts(merged, ontology)` 다. 경고(FAIL 아님): agt:usesConcept 의 대상이 폐기된 용어다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_deprecated_concepts(merged: Graph, ontology: Graph) -> list[str]:
    """경고(FAIL 아님): agt:usesConcept 의 대상이 폐기된 용어다 — 용어 일관성 (dependency-graph-design §5).

    폐기는 삭제가 아니므로(p0-deprecate-not-delete) 링크 자체는 유효하다. 본문이 옛 용어를 쓰고
    있다는 신호이며, 재검증 시점에 대체 용어로 고칠 대상이다.
    """
    deprecated = deprecated_terms(ontology)
    return sorted(
        f"[usesConcept-deprecated] {_chunk_location(merged, s)} → {_agt_qname(merged, o)}"
        for s, o in merged.subject_objects(kb_lib.AGT.usesConcept)
        if o in deprecated
    )
```
<!-- 인용 끝 -->
