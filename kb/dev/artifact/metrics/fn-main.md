---
id: https://agentic-knowledge-base.dev/id/chunk/0649925b-5b61-4525-aa1a-2838ae397422
type: artifact
level: executable
title_ko: 함수 main (tools/metrics.py)
title: function main in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
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
    chunks, plane, level, status, lines, live = classify_chunks(g)
    linked, parts, orphans, link_count = orphan_and_links(g, chunks)
    reqs, reach = refinement_reach(g, live, plane, level)
    comp_of, siblings, authored, nonreq, ascribed = back_trace(g, live, plane, reqs)
    human, gen, hist, assumes = trust_and_size(g, chunks, live, lines)
    components, skips, filled, residency_bad = axis_proxies(g, live, plane, level, authored, comp_of, siblings)
    (link_ents, with_ev, origins, extracted_n, built_n, restored_total,
     sat, trig_on, TIM, tim_filled) = link_build(g)
    cov_line = fixed_sentence_coverage(a, live, plane, parts, siblings)
    (default_only, assumptions, grade_dist, grade_ab,
     observations, obs_recorded) = assumption_facts(g, live, plane)
    (vv, vv_by, verifies_links, no_criteria, verified_targets,
     dev_reqs, goals, covered_reqs, goals_with_criteria) = vv_facts(g, chunks, live, plane)
    role_rows, scope_bad, BUDGET = role_worksets(g, live, plane, lines, pct)

    inputs = list(a.files) + ([a.notes] if a.notes else []) + list(a.bodies)
    head = render_head(g, chunks, live, siblings, inputs)
    o = render_distribution(pct, chunks, live, plane, level, orphans)
    o += render_axis_sections(pct, live, authored, components, filled, skips, residency_bad, cov_line,
                              link_ents, with_ev, origins, extracted_n, built_n, restored_total,
                              tim_filled, TIM, BUDGET, role_rows, scope_bad)
    o += render_stage_sections(g, pct, observations, obs_recorded, assumptions, assumes, grade_dist,
                               grade_ab, trig_on, sat, vv, vv_by, verifies_links, verified_targets,
                               no_criteria, covered_reqs, dev_reqs, goals_with_criteria, goals)
    o += render_tail_sections(g, pct, live, link_count, hist, reqs, reach, ascribed, nonreq, assumes,
                              default_only, gen, human)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, o, inputs), encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
