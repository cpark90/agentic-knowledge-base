---
id: https://agentic-knowledge-base.dev/id/chunk/b459c8d8-41ff-4f75-8df6-c9dfa12627cf
type: artifact
level: executable
title_ko: 함수 judgements (tools/link.py)
title: function judgements in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f1f06f16-947e-47c4-b831-f8359170bfed]
part_of: https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d
---
**함수** — `judgements(u)` 다. (f) 판정 — {(단위 쌍, 링크 종류): [극성…]}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judgements(u: Units) -> dict:
    """(f) 판정 — {(단위 쌍, 링크 종류): [극성…]}. run_evidence 가 후보 링크 개체에 붙인 agt:judgement 증거를 읽는다 (판정자마다 하나)."""
    g, out = u.g, defaultdict(list)
    for link in sorted(set(g.subjects(AGT.hasEvidence, None)), key=str):
        pols = [str(next(g.objects(e, AGT.polarity), "")) for e in sorted(g.objects(link, AGT.hasEvidence), key=str)
                if next(g.objects(e, AGT.evidenceKind), None) == AGT.judgement]
        if not pols:
            continue
        a, b = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None)
        kind = str(next(g.objects(link, AGT.linkKind), "")).split("/")[-1]
        ua, ub = u.unit_of.get(a), u.unit_of.get(b)
        if ua is not None and ub is not None and ua != ub:
            out[(frozenset((ua, ub)), kind)] += pols
    return out
```
<!-- 인용 끝 -->
