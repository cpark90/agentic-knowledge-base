---
id: https://agentic-knowledge-base.dev/id/chunk/61bc81fd-0938-43f0-b90d-4c697de5bd6e
type: artifact
level: executable
title_ko: 함수 decision_completeness (tools/metrics.py)
title: function decision_completeness in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ea0b3b82-2b10-4fbf-91c7-d3d65d42b461
---
**함수** — `decision_completeness(g, chunks, plane, status, comp_of, siblings, open_candidates)` 다. 살아 있는 결정 중 대안 부분을 가진 것과 못 가진 것을 돌려준다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decision_completeness(g, chunks, plane, status, comp_of, siblings, open_candidates=frozenset()):
    """살아 있는 결정 중 대안 부분을 가진 것과 못 가진 것을 돌려준다 (유저 결정 2026-10-04 — 결정 완결률).

    결정의 단위는 **결론** 슬롯 청크를 부분으로 가진 복합체다. 복합체 밖의 결론 청크는 그 하나가 결정이다. 결론이 하나라도
    deprecated 가 아니면 살아 있다. 대안은 같은 복합체에 **대안** 슬롯 청크가 있는가로 본다. 복합체 밖의 결론 청크는
    형제가 없으므로 자기 본문의 슬롯을 본다.

    열린 공간의 후보 결정은 분모·분자에서 빼고 따로 센다 (유저 결정 Q60-a) — 결론이 `open_candidates`
    (`kb_lib.open_space_candidates`: status open 인 공간의 state open 후보)에 든 결정이다. 아직 고르지 않은 선택지이지 확정
    결정이 아니다. resolved 공간의 confirmed 후보는 확정 결정이므로 분모에 남는다.
    """
    def slots(c):
        return {str(v) for v in g.objects(c, AGT.bodySlot)}
    units = defaultdict(list)
    for c in chunks:
        if plane[c] == "decision" and "결론" in slots(c):
            units[comp_of.get(c, c)].append(c)
    alive = [u for u, cs in units.items() if any(status[c] != "deprecated" for c in cs)]
    candidate_units = [u for u in alive if any(c in open_candidates for c in units[u])]
    live_units = [u for u in alive if u not in set(candidate_units)]
    def has_alt(u):
        return any("대안" in slots(p) for p in (siblings.get(u) or (u,)))
    missing = sorted((u for u in live_units if not has_alt(u)), key=str)
    return live_units, missing, {u: sorted(units[u], key=str)[0] for u in missing}, candidate_units
```
<!-- 인용 끝 -->
