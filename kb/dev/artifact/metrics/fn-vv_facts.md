---
id: https://agentic-knowledge-base.dev/id/chunk/62f85584-b202-466f-b9e1-9e55720699a8
type: artifact
level: executable
title_ko: 함수 vv_facts (tools/metrics.py)
title: function vv_facts in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/281c4f1d-6048-495f-872e-1aa02b250baa
---
**함수** — `vv_facts(g, chunks, live, plane)` 다. V&V KB 의 청크 분포와 verifies 링크·기준 없는 verifies·검증 대응물을 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def vv_facts(g, chunks, live, plane):
    """V&V KB 의 청크 분포와 verifies 링크·기준 없는 verifies·검증 대응물을 돌려준다."""
    # 7단계 대리 — V&V KB (p8-vv-plane-instances: 코어의 두 번째 인스턴스, kb/vv/). KB 는 청크 위치(assertionLocation)로 가른다 (kb_lib.kb_of)
    loc = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in chunks}
    vv = {c for c in live if kb_lib.kb_of(loc[c]) == kb_lib.KB_VV}
    dev = live - vv
    vv_by = Counter(plane[c] for c in vv)
    verifies_links = list(g.subject_objects(AGT.verifies))
    no_criteria = [s for s, _ in verifies_links if not any((c_, RDF.type, AGT.ContractChunk) in g for c_ in g.objects(s, AGT.refines))]
    verified_targets = {o for _, o in verifies_links}
    dev_reqs = {c for c in dev if plane[c] == "requirement"}
    goals = {c for c in vv if plane[c] == "requirement"}
    covered_reqs = {o for s, o in g.subject_objects(AGT.derivesFrom) if s in goals and o in dev_reqs}
    goals_with_criteria = {o for s, o in g.subject_objects(AGT.refines) if o in goals and plane.get(s) == "contract"}
    return vv, vv_by, verifies_links, no_criteria, verified_targets, dev_reqs, goals, covered_reqs, goals_with_criteria
```
<!-- 인용 끝 -->
