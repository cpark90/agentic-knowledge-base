---
id: https://agentic-knowledge-base.dev/id/chunk/9e7b4f02-5771-4b99-bd5c-6b89ee5cbe45
type: artifact
level: executable
title_ko: 함수 suspect_by_when (tools/kb_lib.py)
title: function suspect_by_when in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/badba8ff-e4ce-4780-8483-a93e7c6631a5]
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `suspect_by_when(g, states)` 다. `when` 이 확정 링크를 suspect 로 유도한 것 → 사유, 그리고 판정 불가 → 남긴 것.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def suspect_by_when(g: Graph, states: dict) -> tuple:
    """`when` 이 확정 링크를 suspect 로 유도한 것 → 사유, 그리고 판정 불가 → 남긴 것. 참인 링크는 어느 쪽에도 없다."""
    false_links: dict = {}
    unverified: dict = {}
    for link, _kind, _state, verdict, derived, reason in when_verdicts(g, states):
        if derived == LINK_STATE_SUSPECT:
            false_links[link] = reason
        elif verdict == WHEN_UNVERIFIED:
            unverified[link] = reason
    return false_links, unverified
```
<!-- 인용 끝 -->
