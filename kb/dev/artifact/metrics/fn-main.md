---
id: https://agentic-knowledge-base.dev/id/chunk/0649925b-5b61-4525-aa1a-2838ae397422
type: artifact
level: executable
title_ko: 함수 main (tools/metrics.py)
title: function main in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/030c7af0-5dd1-4541-87a2-47f630beb3cd, https://agentic-knowledge-base.dev/id/chunk/05160394-59e0-426d-a8c1-2421857f4e21, https://agentic-knowledge-base.dev/id/chunk/1559adcb-99d9-41e1-b4d1-bef792a15377, https://agentic-knowledge-base.dev/id/chunk/1939bb14-28c6-4fc3-a367-bf91e805c37e, https://agentic-knowledge-base.dev/id/chunk/205ddaae-9763-4e5b-a48f-c8e0b4a8bc63, https://agentic-knowledge-base.dev/id/chunk/3591b8e8-245b-4398-94da-2db2b7e3339d, https://agentic-knowledge-base.dev/id/chunk/3da75bed-e0cb-4848-a438-30001f43fea2, https://agentic-knowledge-base.dev/id/chunk/3f9e7300-40c1-4755-9e4d-f22da6f54774, https://agentic-knowledge-base.dev/id/chunk/45edd053-bd47-4049-8f15-85cc5fb30edf, https://agentic-knowledge-base.dev/id/chunk/46cfcd54-cf4f-403a-8bf2-67c038422236, https://agentic-knowledge-base.dev/id/chunk/4cf4ea55-9afe-4a27-9b9b-fb3a38503594, https://agentic-knowledge-base.dev/id/chunk/61bc81fd-0938-43f0-b90d-4c697de5bd6e, https://agentic-knowledge-base.dev/id/chunk/62f85584-b202-466f-b9e1-9e55720699a8, https://agentic-knowledge-base.dev/id/chunk/8539f11f-8398-42c3-91a0-b7ae377c9927, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/98497cab-a974-4398-9ff8-276884ea85f2, https://agentic-knowledge-base.dev/id/chunk/a0050c7a-8e88-4a2e-8172-5ecfcd868dff, https://agentic-knowledge-base.dev/id/chunk/a0b3f8e3-4420-406f-9077-a1c20200be2f, https://agentic-knowledge-base.dev/id/chunk/ab27c783-b7b3-4ed2-8fa4-cb2b76c861b7, https://agentic-knowledge-base.dev/id/chunk/ac4042d4-658b-4464-af33-c3e2da6754d5, https://agentic-knowledge-base.dev/id/chunk/ad6647eb-8132-4478-a102-4fe23cf05e98, https://agentic-knowledge-base.dev/id/chunk/b55968d0-8e31-4e98-a480-15a84b6ac07b, https://agentic-knowledge-base.dev/id/chunk/bfe7f63e-7fc3-4a1b-bb7a-b40041fd189e, https://agentic-knowledge-base.dev/id/chunk/cae9f316-30b4-4aec-8a06-4a4df1f8e3f9, https://agentic-knowledge-base.dev/id/chunk/cca34039-f0b1-466a-bdb0-ed871d10347c, https://agentic-knowledge-base.dev/id/chunk/d03431bf-2330-4c3c-9fdc-99221b37916e, https://agentic-knowledge-base.dev/id/chunk/d68d1243-7e85-4ee5-90ac-241abc0db3c6, https://agentic-knowledge-base.dev/id/chunk/dcb5249e-42e9-471f-920a-3a3c0810a30d, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e, https://agentic-knowledge-base.dev/id/chunk/f35029fa-aa72-4c8d-92e7-fcc9e58f314d, https://agentic-knowledge-base.dev/id/chunk/f4d0d4bb-6623-435e-b230-93d98fb7ceac]
part_of: https://agentic-knowledge-base.dev/id/composite/a6e8151a-11f0-4db0-86cd-f33732a47457
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    a = parse_args()
    planes_, levels_, table_ = kb_lib.load_residency(a.residency)
    PLANES[:], LEVELS[:] = planes_, levels_
    RESIDENCY.update({p_: v_ for p_, v_ in table_.items() if set(v_) != set(levels_)})
    g = Graph()
    for f in a.files:
        if f.endswith(".ttl"):
            g.parse(f, format="turtle")
    # 설계 공간 그래프는 union 에 섞지 않는다 — 공간 청크·후보 링크 개체가 청크 수·링크 개체 수·링크 밀도에 들지 않게 한다 (Q60-a)
    gs = Graph()
    for f in a.spaces:
        gs.parse(f, format="turtle")
    pct = kb_lib.pct  # 비율 표기의 단일 정의처 (G15 — `n/d = p.p%`, 0 분모는 없음)
    chunks, plane, level, status, tokens, live = classify_chunks(g)
    linked, parts, orphans, link_count = orphan_and_links(g, chunks)
    reqs, reach, depth = refinement_reach(g, live, plane, level)
    declarer = composite_declarers(a.bodies)  # 복합체 → 선언 청크 (유저 결정 Q49-a)
    comp_of, siblings, authored, nonreq, ascribed = back_trace(g, live, plane, reqs, declarer)
    human, gen, hist, assumes = trust_and_size(g, chunks, live, plane, tokens)
    components, outside, skips, filled, residency_bad = axis_proxies(g, live, plane, level, authored, comp_of, siblings, declarer,
                                                                    kb_lib.space_linkage_edges(gs))
    skip_parts = skip_decomposition(g, plane, level, comp_of, skips)
    decisions, missing, missing_loc, candidate_decisions = decision_completeness(g, chunks, plane, status, comp_of, siblings,
                                                                                 kb_lib.open_space_candidates(gs))
    functional, human_reqs, fwd_base, fwd_reached = forward_trace(g, plane, level, reqs, depth)
    vv_all, vv_producers, vv_outsiders = vv_independence(g, chunks)
    mutations = mutation_fixtures(a.mutations)
    (link_ents, with_ev, origins, extracted_n, built_n, restored_total,
     sat, trig_on, TIM, tim_filled) = link_build(g)
    cov_line = fixed_sentence_coverage(a, live, plane, parts, siblings)
    (default_only, assumptions, grade_dist, grade_ab,
     observations, obs_recorded) = assumption_facts(g, live, plane)
    (vv, vv_by, verifies_links, no_criteria, verified_targets,
     dev_reqs, goals, covered_reqs, goals_with_criteria) = vv_facts(g, chunks, live, plane)
    role_rows, scope_bad, BUDGET = role_worksets(g, live, plane, tokens, pct)

    inputs = list(a.files) + list(a.spaces) + ([a.notes] if a.notes else []) + list(a.bodies) + list(a.mutations)
    head = render_head(g, chunks, live, siblings, inputs, [f for f in inputs if f not in a.spaces])
    o = render_distribution(pct, chunks, live, plane, level, orphans)
    o += render_axis_sections(pct, live, authored, components, filled, skips, skip_parts, residency_bad, cov_line,
                              link_ents, with_ev, origins, extracted_n, built_n, restored_total,
                              tim_filled, TIM, BUDGET, role_rows, scope_bad)
    o += render_component_diagnosis(g, plane, outside)
    o += render_refinement_section(g, pct, decisions, missing, missing_loc, functional, human_reqs, fwd_base, fwd_reached,
                                   candidate_decisions)
    o += render_stage_sections(g, pct, observations, obs_recorded, assumptions, assumes, grade_dist,
                               grade_ab, trig_on, sat, vv, vv_by, verifies_links, verified_targets,
                               no_criteria, covered_reqs, dev_reqs, goals_with_criteria, goals)
    o += render_vv_extra(g, pct, vv_all, vv_producers, vv_outsiders, mutations)
    o += render_tail_sections(g, pct, live, link_count, hist, reqs, reach, ascribed, nonreq, assumes,
                              default_only, gen, human)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, o, inputs), encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
