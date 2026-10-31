---
id: https://agentic-knowledge-base.dev/id/chunk/48ebda88-1408-4667-9fbf-c8462a169843
type: artifact
level: executable
title_ko: 함수 draft_end_links (tools/kb_lib.py)
title: function draft_end_links in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `draft_end_links(g, link_keys)` 다. `draft` 를 끝으로 둔 확정 링크 — (출발 status, 출발, 링크 키, 끝).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def draft_end_links(g: Graph, link_keys) -> list[tuple[str, URIRef, str, URIRef]]:
    """`draft` 를 끝으로 둔 확정 링크 — (출발 status, 출발, 링크 키, 끝). 결정 p4-chunk-state-machine 의 "draft 청크는 링크의 끝이 될 수 없다".

    링크는 frontmatter 링크 키(`link_keys` — 호출자가 단일 정의 위치 chunk2kg.LINK_KEYS 를 준다)가 낸 직접 트리플이고, 출발과 끝이 둘 다
    단위 지식(`agt:tokenCount` 를 가진 노드)이며 끝의 status 가 draft 인 것이다. 끝이 복합체이면 status 가 없어 세지 않는다. 출발이
    deprecated 인 링크도 낸다 — 거르는 일은 호출자가 한다. 소비자는 감사 보고의 지표(weave `_audit_draft_ends`)와 게이트
    `draft-end`(validate `check_draft_end`)이고 같은 정의를 쓴다 (유저 답 Q108-a 3단계).
    """
    chunks = set(g.subjects(AGT.tokenCount, None))
    status = {c: str(next(g.objects(c, AGT.status), "")) for c in chunks}
    return sorted(((status[s], s, key, o) for key in link_keys for s, o in g.subject_objects(AGT[key])
                   if s in chunks and o in chunks and status[o] == "draft"), key=lambda r: (str(r[1]), r[2], str(r[3])))
```
<!-- 인용 끝 -->
