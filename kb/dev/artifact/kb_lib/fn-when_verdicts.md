---
id: https://agentic-knowledge-base.dev/id/chunk/badba8ff-e4ce-4780-8483-a93e7c6631a5
type: artifact
level: executable
title_ko: 함수 when_verdicts (tools/kb_lib.py)
title: function when_verdicts in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b76ee239-c1db-4b7d-b6f0-0f35e7ce919f]
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `when_verdicts(g, states)` 다. `agt:when` 을 가진 링크마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def when_verdicts(g: Graph, states: dict) -> list:
    """`agt:when` 을 가진 링크마다 (링크, 종류, 저장 상태, 판정, 유도 상태, 사유).

    유도 상태는 link-state-ontology 의 규칙 그대로다 — `when` 이 거짓이면 후보는 invalid(eliminated), 확정은
    suspect 다. 참이면 저장 상태 그대로이고 판정 불가면 유도하지 않는다 (9.11절, 10.6절).
    """
    rows = []
    for link in sorted(g.subjects(RDF.type, AGT.Link), key=str):
        expr = next(g.objects(link, AGT.when), None)
        if expr is None:
            continue
        kind = str(next(g.objects(link, AGT.linkKind), "")).split("/")[-1]
        state = str(next(g.objects(link, AGT.linkState), ""))
        verdict, left = when_eval(str(expr), states)
        if verdict == WHEN_FALSE:
            derived = LINK_STATE_INVALID if state == LINK_STATE_CANDIDATE else LINK_STATE_SUSPECT
            reason = f"`when` 거짓 — `{expr}`"
        elif verdict == WHEN_TRUE:
            derived, reason = state, f"`when` 참 — `{expr}`"
        else:
            derived, reason = "", f"`when` 판정 불가 — `{expr}`: " + " · ".join(left or ["사유 없음"])
        rows.append((link, kind, state, verdict, derived, reason))
    return rows
```
<!-- 인용 끝 -->
