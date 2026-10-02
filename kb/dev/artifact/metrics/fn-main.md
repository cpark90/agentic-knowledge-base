---
id: https://agentic-knowledge-base.dev/id/chunk/0649925b-5b61-4525-aa1a-2838ae397422
type: artifact
level: executable
title_ko: 함수 main (tools/metrics.py)
title: function main in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/05160394-59e0-426d-a8c1-2421857f4e21, https://agentic-knowledge-base.dev/id/chunk/1559adcb-99d9-41e1-b4d1-bef792a15377, https://agentic-knowledge-base.dev/id/chunk/3da75bed-e0cb-4848-a438-30001f43fea2, https://agentic-knowledge-base.dev/id/chunk/45edd053-bd47-4049-8f15-85cc5fb30edf, https://agentic-knowledge-base.dev/id/chunk/4cf4ea55-9afe-4a27-9b9b-fb3a38503594, https://agentic-knowledge-base.dev/id/chunk/62f85584-b202-466f-b9e1-9e55720699a8, https://agentic-knowledge-base.dev/id/chunk/8539f11f-8398-42c3-91a0-b7ae377c9927, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/a0b3f8e3-4420-406f-9077-a1c20200be2f, https://agentic-knowledge-base.dev/id/chunk/ab27c783-b7b3-4ed2-8fa4-cb2b76c861b7, https://agentic-knowledge-base.dev/id/chunk/ac4042d4-658b-4464-af33-c3e2da6754d5, https://agentic-knowledge-base.dev/id/chunk/ad6647eb-8132-4478-a102-4fe23cf05e98, https://agentic-knowledge-base.dev/id/chunk/b55968d0-8e31-4e98-a480-15a84b6ac07b, https://agentic-knowledge-base.dev/id/chunk/bfe7f63e-7fc3-4a1b-bb7a-b40041fd189e, https://agentic-knowledge-base.dev/id/chunk/cca34039-f0b1-466a-bdb0-ed871d10347c, https://agentic-knowledge-base.dev/id/chunk/d03431bf-2330-4c3c-9fdc-99221b37916e, https://agentic-knowledge-base.dev/id/chunk/d68d1243-7e85-4ee5-90ac-241abc0db3c6, https://agentic-knowledge-base.dev/id/chunk/dcb5249e-42e9-471f-920a-3a3c0810a30d, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e, https://agentic-knowledge-base.dev/id/chunk/f35029fa-aa72-4c8d-92e7-fcc9e58f314d, https://agentic-knowledge-base.dev/id/chunk/f4d0d4bb-6623-435e-b230-93d98fb7ceac]
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
    pct = kb_lib.pct  # 비율 표기의 단일 정의처 (G15 — `n/d = p.p%`, 0 분모는 없음)
    chunks, plane, level, status, tokens, live = classify_chunks(g)
    linked, parts, orphans, link_count = orphan_and_links(g, chunks)
    reqs, reach = refinement_reach(g, live, plane, level)
    comp_of, siblings, authored, nonreq, ascribed = back_trace(g, live, plane, reqs)
    human, gen, hist, assumes = trust_and_size(g, chunks, live, plane, tokens)
    components, outside, skips, filled, residency_bad = axis_proxies(g, live, plane, level, authored, comp_of, siblings)
    (link_ents, with_ev, origins, extracted_n, built_n, restored_total,
     sat, trig_on, TIM, tim_filled) = link_build(g)
    cov_line = fixed_sentence_coverage(a, live, plane, parts, siblings)
    (default_only, assumptions, grade_dist, grade_ab,
     observations, obs_recorded) = assumption_facts(g, live, plane)
    (vv, vv_by, verifies_links, no_criteria, verified_targets,
     dev_reqs, goals, covered_reqs, goals_with_criteria) = vv_facts(g, chunks, live, plane)
    role_rows, scope_bad, BUDGET = role_worksets(g, live, plane, tokens, pct)

    inputs = list(a.files) + ([a.notes] if a.notes else []) + list(a.bodies)
    head = render_head(g, chunks, live, siblings, inputs)
    o = render_distribution(pct, chunks, live, plane, level, orphans)
    o += render_axis_sections(pct, live, authored, components, filled, skips, residency_bad, cov_line,
                              link_ents, with_ev, origins, extracted_n, built_n, restored_total,
                              tim_filled, TIM, BUDGET, role_rows, scope_bad)
    o += render_component_diagnosis(g, plane, outside)
    o += render_stage_sections(g, pct, observations, obs_recorded, assumptions, assumes, grade_dist,
                               grade_ab, trig_on, sat, vv, vv_by, verifies_links, verified_targets,
                               no_criteria, covered_reqs, dev_reqs, goals_with_criteria, goals)
    o += render_tail_sections(g, pct, live, link_count, hist, reqs, reach, ascribed, nonreq, assumes,
                              default_only, gen, human)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, o, inputs), encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
