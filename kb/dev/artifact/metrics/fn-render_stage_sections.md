---
id: https://agentic-knowledge-base.dev/id/chunk/dcb5249e-42e9-471f-920a-3a3c0810a30d
type: artifact
level: executable
title_ko: 함수 render_stage_sections (tools/metrics.py)
title: function render_stage_sections in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/12b09ffc-10a1-4725-b174-8202306f3fc6
---
**함수** — `render_stage_sections(g, pct, observations, obs_recorded, assumptions, assumes, grade_dist, grade_ab, trig_on, sat, vv, vv_by, verifies_links, verified_targets, no_criteria, covered_reqs, dev_reqs, goals_with_criteria, goals)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_stage_sections(g, pct, observations, obs_recorded, assumptions, assumes, grade_dist, grade_ab, trig_on, sat, vv, vv_by, verifies_links, verified_targets, no_criteria, covered_reqs, dev_reqs, goals_with_criteria, goals):
    o = []
    o += ["", "## 4단계 대리 — 가정과 무효화 (14.1 정정본: 무효화 이력 · 판정식 등급 · 인위 파괴 실험)", "",
          f"- 의미 보존: 무효화 이력 — 관측(memory plane) **{len(observations)}**건, 그중 `assume_check --record` 의 판정 관측 {obs_recorded}건 (지금은 판정 관측 수 — 무효화 사건이 생기면 그 이력이 여기 쌓인다. provenance 는 관측이 `generatedBy`·`prov:wasDerivedFrom` 를 갖는 비율로 잰다 (목표 100.0%): {pct(sum(1 for c in observations if (c, AGT.generatedBy, None) in g and (c, PROV.wasDerivedFrom, None) in g), len(observations))})",
          f"- 구체화: 가정 개체 {len(assumptions)} · `assumes` 링크 {assumes} (가정 · 신뢰 등급 절과 같은 수) · 판정식 등급 분포(참조 조건 등급의 최저) " + (" · ".join(f"{k} {v}" for k, v in sorted(grade_dist.items())) or "없음") + f" — A·B 비율 **{pct(grade_ab, len(assumptions))}** (목표 100.0%), D **{grade_dist.get('D', 0)}**건 (목표 0)",
          f"- 연결: suspect 포화율 — 켜진 트리거({trig_on})가 suspect 로 유도하는 확정 링크 **{pct(sat['by_trigger'], sat['confirmed'])}** "
          f"(목표 포화 경고선 20% 미만 — 넘으면 트리거를 더 좁힌다). `agt:when` 을 가진 확정 링크 {sat['with_when']}건의 판정은 호스트 상태를 "
          "보므로 이 뷰 밖이고 `bazel run //tools:assume_check` 가 낸다. 선언의 원본은 `tools/kb_lib.py` 의 `SUSPECT_TRIGGERS` 이며 선언에 없는 종류는 돌지 않는다",
          "- 연결: 인위 파괴 실험은 `bazel run //tools:assume_check -- --break <cond>` — 계산된 직접 영향 집합과 실제 의존 집합(frontmatter 스캔)의 일치 여부를 그 보고가 낸다. 판정은 호스트 상태를 보므로 이 뷰 밖이다"]
    o += ["", "## 7단계 대리 — V&V (p8-vv-plane-instances · p8-pass-criteria · p8-scenario-ladder-rungs)", "",
          f"- 구체화: V&V KB(`kb/vv/`) 살아 있는 청크 **{len(vv)}** — 검증 목표(`requirement`) {vv_by['requirement']} · 시나리오(`decision`) {vv_by['decision']} · 합격 기준(`contract`) {vv_by['contract']} · 케이스(`schema`) {vv_by['schema']} · 검증기(`artifact`) {vv_by['artifact']} · 판정 주석(`annotation`) {vv_by['annotation']} · 실행 기록(`memory`) {vv_by['memory']}",
          f"- 연결: `verifies` 링크 **{len(verifies_links)}** (주어는 V&V 청크, 대상은 같은 수준의 개발 항목 — `defs/kb.bzl` 이 분석 시점에 강제) · 대상이 된 개발 항목 {len(verified_targets)}",
          f"- 의미 보존: 기준 없는 `verifies` **{len(no_criteria)}**건 (목표 0) — ( 주어가 합격 기준(`ContractChunk`)을 `refines` 해야 하며 verify 질의 `verifies-without-criteria` 가 거부한다)",
          f"- 연결: 검증 대응물이 있는 요구(검증 목표가 `derivesFrom` 으로 가리키는 개발 요구) **{pct(len(covered_reqs), len(dev_reqs))}** (목표 100.0% — 8.3절 functional 높이의 검증 대응물 필수) · 합격 기준이 달린 검증 목표 {pct(len(goals_with_criteria), len(goals))}"]
    return o
```
<!-- 인용 끝 -->
