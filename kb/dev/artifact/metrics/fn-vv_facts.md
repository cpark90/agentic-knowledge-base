---
id: https://agentic-knowledge-base.dev/id/chunk/62f85584-b202-466f-b9e1-9e55720699a8
type: artifact
level: executable
title_ko: 함수 vv_facts (tools/metrics.py)
title: function vv_facts in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/6553eed2-c1d9-41a4-b5c8-549f5d93193e, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99]
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
    vv_by = Counter(plane[c] for c in vv)
    verifies_links = list(g.subject_objects(AGT.verifies))
    no_criteria = [s for s, _ in verifies_links if not any((c_, RDF.type, AGT.ContractChunk) in g for c_ in g.objects(s, AGT.refines))]
    verified_targets = {o for _, o in verifies_links}
    # 검증 대응물의 집합은 게이트 `rung-before-descent` 와 같은 함수 하나가 낸다 (kb_lib.vv_counterparts, 유저 결정 Q51-a)
    vc = kb_lib.vv_counterparts(g, plane, live)
    dev_reqs, goals, covered_reqs, goals_with_criteria = vc["dev_reqs"], vc["goals"], vc["covered_reqs"], vc["goals_with_criteria"]
    return vv, vv_by, verifies_links, no_criteria, verified_targets, dev_reqs, goals, covered_reqs, goals_with_criteria
```
<!-- 인용 끝 -->
