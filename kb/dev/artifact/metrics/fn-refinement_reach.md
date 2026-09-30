---
id: https://agentic-knowledge-base.dev/id/chunk/b55968d0-8e31-4e98-a480-15a84b6ac07b
type: artifact
level: executable
title_ko: 함수 refinement_reach (tools/metrics.py)
title: function refinement_reach in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/fa4c4a17-7c5e-4ecc-b6f7-818675609be4
---
**함수** — `refinement_reach(g, live, plane, level)` 다. 요구에서 refines·serves 역방향으로 내려가 닿는 가장 낮은 수준의 분포를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def refinement_reach(g, live, plane, level):
    """요구에서 refines·serves 역방향으로 내려가 닿는 가장 낮은 수준의 분포를 돌려준다."""
    reqs = {c for c in live if plane[c] == "requirement"}
    # CQ19: 요구에서 refines 역방향으로 내려가 닿는 가장 낮은 level
    down = defaultdict(set)
    for s, o in g.subject_objects(AGT.refines):
        down[o].add(s)
    for s, o in g.subject_objects(AGT.serves):
        down[o].add(s)
    def deepest(r):
        seen, stack, best = set(), [r], -1
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x)
            if x in level and level[x] in LEVELS: best = max(best, LEVELS.index(level[x]))
            stack.extend(down.get(x, ()))
        return best
    reach = Counter(LEVELS[deepest(r)] if deepest(r) >= 0 else "none" for r in reqs)
    return reqs, reach
```
<!-- 인용 끝 -->
