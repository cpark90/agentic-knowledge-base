---
id: https://agentic-knowledge-base.dev/id/chunk/bc119f80-c2d4-4e13-bba3-e64e39bf8580
type: artifact
level: executable
title_ko: 함수 decision_units (tools/metrics.py)
title: function decision_units in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ea0b3b82-2b10-4fbf-91c7-d3d65d42b461
---
**함수** — `decision_units(g, chunks, plane, status, comp_of, open_candidates)` 다. 결정 단위와 열린 후보 결정 단위의 단일 정의 위치 — 결정 완결률과 CQ20 후방 추적이 같은 함수를 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decision_units(g, chunks, plane, status, comp_of, open_candidates=frozenset()):
    """결정 단위와 열린 후보 결정 단위의 단일 정의 위치 — 결정 완결률과 CQ20 후방 추적이 같은 함수를 쓴다 (유저 답 Q116-a).

    결정의 단위는 **결론** 슬롯 단위 지식을 부분으로 가진 복합체이고, 복합체 밖의 결론은 그 하나가 결정이다. 결론이 하나라도
    deprecated 가 아니면 살아 있다. 열린 후보 결정은 결론이 `open_candidates`(`kb_lib.open_space_candidates`: status open 인
    공간의 state open 후보)에 든 살아 있는 결정이다. 반환은 (단위 → 결론들, 살아 있는 단위, 열린 후보 단위)다.
    """
    units = defaultdict(list)
    for c in chunks:
        if plane[c] == "decision" and "결론" in {str(v) for v in g.objects(c, AGT.bodySlot)}:
            units[comp_of.get(c, c)].append(c)
    alive = [u for u, cs in units.items() if any(status[c] != "deprecated" for c in cs)]
    candidate_units = [u for u in alive if any(c in open_candidates for c in units[u])]
    return units, alive, candidate_units
```
<!-- 인용 끝 -->
