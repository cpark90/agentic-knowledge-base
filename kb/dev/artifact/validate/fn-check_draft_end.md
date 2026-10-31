---
id: https://agentic-knowledge-base.dev/id/chunk/bcd2cb8b-0f77-4111-9cd6-194809eb4d2b
type: artifact
level: executable
title_ko: 함수 check_draft_end (tools/validate.py)
title: function check_draft_end in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/48ebda88-1408-4667-9fbf-c8462a169843, https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4]
part_of: https://agentic-knowledge-base.dev/id/composite/700062aa-fcac-4d30-8481-7021a666d072
---
**함수** — `check_draft_end(merged)` 다. `draft` 단위 지식을 끝으로 둔 확정 링크를 거부한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_draft_end(merged: Graph) -> list[str]:
    """`draft` 단위 지식을 끝으로 둔 확정 링크를 거부한다 (게이트 `draft-end`, 결정 p4-chunk-state-machine, 유저 답 Q108-a 3단계).

    출발이 deprecated 인 링크는 신규 참조가 아니므로 거부하지 않는다. 판정 함수는 감사 보고의 "draft 끝 링크" 지표(weave
    `_audit_draft_ends`)와 같은 `kb_lib.draft_end_links` 다 — 지표가 0건이 된 뒤에 같은 정의로 켠 게이트다.
    """
    gate = kb_lib.DRAFT_END_GATE
    return [f"[{gate}] {_chunk_location(merged, s)}: 링크 `{key}` 의 끝 {_chunk_location(merged, o)} 가 draft 다 — 끝을 검토해 "
            f"stable 로 올리거나 링크를 뺀다 (p4-chunk-state-machine)"
            for st, s, key, o in kb_lib.draft_end_links(merged, chunk2kg.LINK_KEYS) if st != "deprecated"]
```
<!-- 인용 끝 -->
