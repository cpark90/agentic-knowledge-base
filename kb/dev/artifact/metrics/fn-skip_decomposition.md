---
id: https://agentic-knowledge-base.dev/id/chunk/a0050c7a-8e88-4a2e-8172-5ecfcd868dff
type: artifact
level: executable
title_ko: 함수 skip_decomposition (tools/metrics.py)
title: function skip_decomposition in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99]
part_of: https://agentic-knowledge-base.dev/id/composite/8fa054a4-1f2a-4d86-b98d-3c68ca9a4619
---
**함수** — `skip_decomposition(g, plane, level, comp_of, skips)` 다. 건너뜀을 결정 복합체 몫(슬롯별)·V&V 정제 계층 몫·나머지(plane·수준 쌍별)로 가른다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def skip_decomposition(g, plane, level, comp_of, skips):
    """건너뜀을 결정 복합체 몫(슬롯별)·V&V 정제 계층 몫·나머지(plane·수준 쌍별)로 가른다 (유저 결정 2026-10-04).

    V&V 정제 계층 몫 (유저 답 Q30-b · Q41-a): V&V KB(`kb/vv/`) 안의 두 쌍은 정제 계층의 허용 구조다(p8-scenario-ladder-rungs).
    합격 기준(contract, logical) → 검증 목표(requirement, functional) `refines` 는 logical 정제 수준의 검증 대응 그 자체다(Q30-b).
    검증기(artifact, executable) → 합격 기준(contract, logical) `refines` 는 케이스 없이 기준을 정제하는 비표본 검증기의 꼴이다
    — 비표본 판정에는 표본 케이스가 없다(Q29-a 의 귀결, Q41-a). 둘 다 건너뜀에서 빼고 쌍마다 따로 센다(VV_LADDER_SKIPS).

    결정 복합체는 abstract·logical·concrete 를 한 복합체로 걸친다 (p7-decision-spans-three-levels). 복합체 단위로 보면
    결론(concrete)이 functional 요구를 `refines` 하는 것은 건너뜀이 아니다. 그래서 decision plane 부분을 가진 복합체의
    부분은 수준을 그 걸침(DECISION_SPAN ∪ 실제 부분 수준)으로 읽고, 양 끝 걸침 사이에 한 단계 차이가 있으면 뺀다.
    복합체 밖의 decision 청크는 그 하나가 결정이므로 같은 걸침(DECISION_SPAN ∪ 자기 수준)으로 읽는다.
    """
    span_of = defaultdict(set)
    for part_, comp_ in comp_of.items():
        if plane.get(part_) == "decision":
            span_of[comp_].add(level[part_])
    span_of = {c_: s_ | set(DECISION_SPAN) for c_, s_ in span_of.items()}
    def span(x):
        if plane.get(x) != "decision":
            return {level[x]}
        return span_of.get(comp_of.get(x)) or ({level[x]} | set(DECISION_SPAN))
    loc = {x: str(next(g.objects(x, AGT.assertionLocation), "")) for x in {c_ for pair in skips for c_ in pair}}
    def vv_ladder(s_, o_):
        """V&V KB 안의 허용 쌍이면 그 이름, 아니면 None — 이름은 VV_LADDER_SKIPS 의 키다."""
        if kb_lib.kb_of(loc[s_]) != kb_lib.KB_VV or kb_lib.kb_of(loc[o_]) != kb_lib.KB_VV:
            return None
        key = (plane.get(s_), level[s_], plane.get(o_), level[o_])
        return next((name for name, pair in VV_LADDER_SKIPS.items() if pair == key), None)
    composite_share, vv_share, residual = Counter(), Counter(), Counter()
    for s_, o_ in skips:
        rung = vv_ladder(s_, o_)
        if rung:
            vv_share[rung] += 1
        elif any(LEVELS.index(a_) - LEVELS.index(b_) == 1 for a_ in span(s_) for b_ in span(o_)):
            slots = {str(v_) for v_ in g.objects(s_, AGT.bodySlot)}
            composite_share["결론" if "결론" in slots else "그 밖의 부분"] += 1
        else:
            residual[(plane.get(s_), level[s_], plane.get(o_), level[o_])] += 1
    return composite_share, vv_share, residual
```
<!-- 인용 끝 -->
