---
id: https://agentic-knowledge-base.dev/id/chunk/f21b98bb-fdc6-42fa-9b87-cc35fc2f64c6
type: artifact
level: executable
title_ko: 함수 graph_beliefs (tools/belief_calibration.py)
title: function graph_beliefs in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/1edd84f8-3e8d-4183-996c-4666aefe4a4a
---
**함수** — `graph_beliefs(g)` 다. 그래프 → (링크 IRI, 규칙 slug) → 값.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def graph_beliefs(g: Graph) -> dict[tuple[str, str], Fraction]:
    """그래프 → (링크 IRI, 규칙 slug) → 값. 규칙 IRI 가 BELIEF_RULES 밖이면 읽지 않는다. 같은 칸에 값이 둘이면 ValueError 다."""
    slug_of = {v: k for k, v in BELIEF_RULES.items()}
    out: dict[tuple[str, str], Fraction] = {}
    for link, node in g.subject_objects(AGT.hasDegreeOfBelief):
        rule, value = g.value(node, AGT.beliefRule), g.value(node, AGT.beliefValue)
        slug = slug_of.get(str(rule))
        if slug is None or value is None:
            continue
        key = (str(link), slug)
        v = Fraction(str(value))
        if key in out and out[key] != v:
            raise ValueError(f"링크 {link} 의 규칙 {slug} 값이 둘이다 ({out[key]} · {v})")
        out[key] = v
    return out
```
<!-- 인용 끝 -->
