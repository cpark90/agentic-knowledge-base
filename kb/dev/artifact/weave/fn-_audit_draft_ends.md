---
id: https://agentic-knowledge-base.dev/id/chunk/dc36a14b-aeb6-4275-97fc-74eb0e0a9b25
type: artifact
level: executable
title_ko: 함수 _audit_draft_ends (tools/weave.py)
title: function _audit_draft_ends in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/48ebda88-1408-4667-9fbf-c8462a169843, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/ebcf6e73-cc0b-447d-ac23-00290abee9ca
---
**함수** — `_audit_draft_ends(m, g)` 다. `draft` 를 끝으로 둔 확정 링크의 수와 목록 — 결정 p4-chunk-state-machine 의 "draft 청크는 링크의 끝이 될 수 없다"를 재는 보고 지표다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_draft_ends(m: Model, g) -> list[str]:
    """`draft` 를 끝으로 둔 확정 링크의 수와 목록 — 결정 p4-chunk-state-machine 의 "draft 청크는 링크의 끝이 될 수 없다"를 재는 보고 지표다.

    링크는 head 그래프에서 frontmatter 링크 키(단일 정의 위치 chunk2kg.LINK_KEYS)가 낸 직접 트리플이고, 끝이 단위 지식이며 그 status 가 draft 인
    것을 센다. 끝이 복합체이면 status 가 없으므로 세지 않는다. 출발 단위 지식의 status 별로 나누어 세고, 출발이 deprecated 인 링크는 신규
    참조가 아니므로 목록에서 빼고 따로 한 줄로 센다. 판정은 게이트 `draft-end` 와 같은 함수 `kb_lib.draft_end_links` 다 (유저 답 Q108-a 3단계).
    """
    rows = [(st, m.location[s], key, m.location[o]) for st, s, key, o in kb_lib.draft_end_links(g, LINK_KEYS)]
    live_rows = sorted(r for r in rows if r[0] != "deprecated")
    by_status = Counter(r[0] for r in live_rows)
    dep_n = sum(1 for r in rows if r[0] == "deprecated")
    body = ["## draft 끝 링크 — `draft` 를 끝으로 둔 확정 링크 (p4-chunk-state-machine, 게이트 `draft-end` 와 같은 정의)", "",
            f"- 살아 있는 출발의 draft 끝 링크: **{len(live_rows)}** (목표 0) — 출발 상태별 "
            + (" · ".join(f"`{k}` {v}" for k, v in sorted(by_status.items())) or kb_lib.NONE_MARK),
            f"- 출발이 `deprecated` 인 draft 끝 링크: {dep_n} (신규 참조가 아니어서 목록에서 뺀다)",
            f"- 링크 키: {' · '.join(f'`{k}`' for k in LINK_KEYS)} (단일 정의 위치 `chunk2kg.LINK_KEYS`). 끝이 복합체인 링크는 상태가 없어 세지 않는다. "
            "같은 정의로 게이트 `draft-end` 가 살아 있는 출발의 건을 거부한다 (유저 답 Q108-a 3단계)", ""]
    if live_rows:
        body += ["| 출발 | 출발 상태 | 키 | 끝 |", "|---|---|---|---|"]
        body += [f"| `{src}` | {st} | `{key}` | `{dst}` |" for st, src, key, dst in live_rows] + [""]
    return body
```
<!-- 인용 끝 -->
