---
id: https://agentic-knowledge-base.dev/id/chunk/46cfcd54-cf4f-403a-8bf2-67c038422236
type: artifact
level: executable
title_ko: 함수 forward_trace (tools/metrics.py)
title: function forward_trace in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/92ac1970-f252-48a0-b11a-fbaa774b2f4a]
part_of: https://agentic-knowledge-base.dev/id/composite/ea0b3b82-2b10-4fbf-91c7-d3d65d42b461
---
**함수** — `forward_trace(g, plane, level, reqs, depth)` 다. functional 요구 중 사람 확인 요구를 뺀 분모와 executable 까지 내려간 것을 돌려준다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def forward_trace(g, plane, level, reqs, depth):
    """functional 요구 중 사람 확인 요구를 뺀 분모와 executable 까지 내려간 것을 돌려준다 (유저 결정 2026-10-04 — 전방 추적).

    사람 확인 요구는 그래프에서 가른다. 검증 목표를 `refines` 하는 합격 기준의 가운데 슬롯이 **확인 절차** 이면 그 목표가
    사람 확인이고, 그 목표가 `derivesFrom` 으로 가리키는 개발 요구도 사람 확인이다 (acceptance-criteria-body-shapes).
    """
    human_criteria = kb_lib.human_check_criteria(g, plane)  # 게이트 `rung-before-descent` 의 면제와 같은 판정
    human_goals = {o for s, o in g.subject_objects(AGT.refines) if o in reqs and s in human_criteria}
    human = human_goals | {o for s, o in g.subject_objects(AGT.derivesFrom) if s in human_goals and o in reqs}
    functional = {r for r in reqs if level[r] == "functional"}
    base = functional - human
    reached = {r for r in base if depth[r] == LEVELS.index("executable")}
    return functional, functional & human, base, reached
```
<!-- 인용 끝 -->
