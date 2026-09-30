---
id: https://agentic-knowledge-base.dev/id/chunk/d68d1243-7e85-4ee5-90ac-241abc0db3c6
type: artifact
level: executable
title_ko: 함수 link_build (tools/metrics.py)
title: function link_build in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/d7f0885e-74e9-4b1e-bf89-f288680555a0
---
**함수** — `link_build(g)` 다. 링크 개체와 증거·후보·구축·복원·suspect 포화·TIM 채움을 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def link_build(g):
    """링크 개체와 증거·후보·구축·복원·suspect 포화·TIM 채움을 돌려준다."""
    # 3단계 대리 — 링크마다 근거 · 구축/복원 비율 · plane×plane 매트릭스 채움 (TIM 이 허용하는 칸)
    link_ents = list(g.subjects(RDF.type, AGT.Link))
    with_ev = [l for l in link_ents if (l, AGT.hasEvidence, None) in g]
    origins = kb_lib.link_origins(g)  # 후보·구축·복원의 단일 정의 — 상태와 증거 종류 기준 (p10-restored-link-marking · p10-extracted-references-are-candidates)
    extracted_n, built_n, restored_total = origins["extracted"], origins["built"], origins["restored"]
    # suspect 포화율 — 선언된 트리거(kb_lib.SUSPECT_TRIGGERS)만 돈다. `when` 판정은 호스트 상태를 보므로 이 뷰 밖이고
    # assume_check 가 낸다. 포화율을 보지 않으면 트리거를 좁힌 것이 맞는지 알 수 없다 (handoff link-model-robustness-cde-2026-09-19)
    sat = kb_lib.suspect_saturation(g)
    trig_on = " · ".join(f"`{k}`" for k, _rule, _basis in kb_lib.suspect_triggers_on()) or kb_lib.NONE_MARK
    TIM = kb_lib.TIM_CELLS  # 허용 칸의 정의처는 kb_lib — weave audit 이 같은 매트릭스를 낸다. 복합체 IRI 의 plane 보정도 kb_lib.link_cells
    seen_cells = kb_lib.link_cells(g)
    tim_filled = [c for c in TIM if c in seen_cells]
    return link_ents, with_ev, origins, extracted_n, built_n, restored_total, sat, trig_on, TIM, tim_filled
```
<!-- 인용 끝 -->
