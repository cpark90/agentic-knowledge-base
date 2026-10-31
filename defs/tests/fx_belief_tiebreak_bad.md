---
id: https://agentic-knowledge-base.dev/id/chunk/fx-belief-tiebreak-bad
type: artifact
level: executable
title_ko: 고정물 함수 — 닫힌 계산 규칙 없이 믿음 정도로 동률을 깨는 선호 정렬
title: fixture function — a preference order that breaks ties by degree of belief with no closed rule
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-choices}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-25T00:00:00Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/c6c78803-bdb6-4ca2-9b07-bba7878f3a01]
---
**함수** — 게이트 `belief-consistency` 조건 (ii)의 음성 고정물이다. 선호의 부분순서를 읽는 정렬이 순서 없는 두 후보를 믿음 정도의 값으로 가른다. 입력 그래프에 닫힌 계산 규칙이 없다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def ordered_candidates(g, space):
    """선호의 부분순서로 후보를 정렬하고, 순서 없는 두 후보는 믿음 정도로 가른다."""
    cands = list(g.objects(space, AGT.hasCandidate))
    above = {c: set(g.objects(c, AGT.preferredOver)) for c in cands}

    def belief(c):
        return max((float(v) for b in g.objects(c, AGT.hasDegreeOfBelief) for v in g.objects(b, AGT.beliefValue)), default=0.0)

    return sorted(cands, key=lambda c: (-len(above[c]), -belief(c)))
```
<!-- 인용 끝 -->
