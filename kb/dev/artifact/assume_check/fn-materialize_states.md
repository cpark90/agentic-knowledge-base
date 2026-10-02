---
id: https://agentic-knowledge-base.dev/id/chunk/ff4fd3d8-23db-4fee-89d7-f5c9052f5590
type: artifact
level: executable
title_ko: 함수 materialize_states (tools/assume_check.py)
title: function materialize_states in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8bfec137-25dc-4b30-8a96-8897afc667ad, https://agentic-knowledge-base.dev/id/chunk/9a2cd33a-ee49-4782-81c9-519aaf5a1621, https://agentic-knowledge-base.dev/id/chunk/9e7b4f02-5771-4b99-bd5c-6b89ee5cbe45, https://agentic-knowledge-base.dev/id/chunk/a171dc2a-1e86-477b-b9e7-4327ae6185f1, https://agentic-knowledge-base.dev/id/chunk/b573f0b1-8e42-4b97-bec6-397c246cd5b9, https://agentic-knowledge-base.dev/id/chunk/b76ee239-c1db-4b7d-b6f0-0f35e7ce919f]
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `materialize_states(g, cond_rows)` 다. 링크 상태를 평가한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def materialize_states(g: Graph, cond_rows: list[dict]) -> tuple:
    """링크 상태를 평가한다 → (states, when_false, when_unverified, by_trigger, sat, space_rows).

    상태는 저장값이 아니라 평가 결과다 (노트 9.11절) — 저장하지 않고 이 자리에서만 계산한다.
    """
    states = kb_lib.odd_states(cond_rows)
    when_false, when_unverified = kb_lib.suspect_by_when(g, states)
    by_trigger = kb_lib.suspect_by_trigger(g)
    sat = kb_lib.suspect_saturation(g, when_false)
    space_rows = []  # `-space` 의 양립 제약 — 링크의 when 과 같은 식 언어다 (space-ontology agt:compatibilityConstraint)
    for sp in sorted(g.subjects(AGT.spaceStatus, None), key=str):
        for c in sorted((str(x) for x in g.objects(sp, AGT.compatibilityConstraint)), key=str):
            verdict_c, left_c = kb_lib.when_eval(c, states)
            space_rows.append((local(sp), c, verdict_c, left_c))
    return states, when_false, when_unverified, by_trigger, sat, space_rows
```
<!-- 인용 끝 -->
