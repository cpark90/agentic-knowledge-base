---
id: https://agentic-knowledge-base.dev/id/chunk/7d5d8898-16f3-47f6-a6e3-e5e8a50f08c8
type: artifact
level: executable
title_ko: 함수 belief_lines (tools/run_evidence.py)
title: function belief_lines in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/1fd3a79a-b431-4470-8d04-5282bbc0eb31]
part_of: https://agentic-knowledge-base.dev/id/composite/a7e4d5c8-a3b3-466a-93eb-1bb3d94b2ed5
---
**함수** — `belief_lines(inputs)` 다. 후보 링크 → 증거 항목들 을 받아 계산 규칙마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def belief_lines(inputs: dict[str, list[tuple[str, str, float | None]]]) -> tuple[list[str], Counter]:
    """후보 링크 → 증거 항목들 을 받아 계산 규칙마다 agt:DegreeOfBelief 노드 하나와 링크의 agt:hasDegreeOfBelief 를 낸다.
    노드 IRI 는 링크 IRI 의 `link/` 를 `belief/` 로 바꾸고 규칙 slug 를 붙인 것이다. 반환은 (TTL 줄들, 규칙 slug → 값을 실은 링크 수)."""
    lines: list[str] = []
    counts: Counter[str] = Counter()
    for link in sorted(inputs):
        for slug, (value, n, var) in sorted(belief_of(inputs[link]).items()):
            node = link.replace(f"{ID_BASE}link/", f"{ID_BASE}belief/", 1) + f"-{slug}"
            counts[slug] += 1
            tail = f" ;\n    agt:beliefVariance {var:.6f}" if var is not None else ""
            lines.append(f"\n<{link}>\n    agt:hasDegreeOfBelief <{node}> .")
            lines.append(f"\n<{node}>\n    a agt:DegreeOfBelief ;\n    agt:beliefValue {value:.4f} ;\n    agt:beliefRule <{BELIEF_RULES[slug]}> ;\n"
                         f"    agt:beliefEvidenceCount \"{n}\"^^xsd:nonNegativeInteger{tail} .")
    return lines, counts
```
<!-- 인용 끝 -->
