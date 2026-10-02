---
id: https://agentic-knowledge-base.dev/id/chunk/642d5db6-db19-4189-acb3-253f39bd2671
type: artifact
level: executable
title_ko: 함수 _audit_comments (tools/weave.py)
title: function _audit_comments in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7ca2da27-a5fc-4b33-aa68-b855ee61d697, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_comments(m, g, live, pct, by_gen)` 다. 판정 주석의 라벨 분포와 해소 상태 (p7-commentary-form — 막는 것은 issue (blocking) + 해소 열림 뿐이다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_comments(m: Model, g, live: set, pct, by_gen) -> list[str]:
    """판정 주석의 라벨 분포와 해소 상태 (p7-commentary-form — 막는 것은 issue (blocking) + 해소 열림 뿐이다)."""
    body: list[str] = []
    # 4. 판정 주석 — 주석의 라벨 분포와 해소 상태 (p7-commentary-form: issue (blocking) + 해소 열림 만 게이트를 막는다)
    label_of = lambda c: str(next(g.objects(c, AGT.commentLabel), ""))        # noqa: E731
    deco_of = lambda c: str(next(g.objects(c, AGT.commentDecoration), ""))    # noqa: E731
    state_of = lambda c: str(next(g.objects(c, AGT.resolutionState), ""))     # noqa: E731
    comments = sorted((c for c in live if m.plane[c] == "annotation"), key=lambda c: m.location[c])
    open_ = [c for c in comments if state_of(c) == kb_lib.COMMENT_OPEN]
    blocking = [c for c in open_ if (label_of(c), deco_of(c)) == kb_lib.COMMENT_BLOCKING]
    body += ["## 판정 주석 — 주석의 라벨 분포와 해소 상태 (p7-commentary-form)", ""]
    if not comments:
        body += [f"살아 있는 주석 {kb_lib.NONE_MARK} — 판정 주석(`{kb_lib.KB_VV}/verdict/`)이 비어 있다. 게이트 "
                 f"`{kb_lib.BLOCKING_COMMENT_GATE}` 는 서 있고 막을 주석이 아직 없다.", ""]
    else:
        labels = Counter(label_of(c) or kb_lib.NONE_MARK for c in comments)
        states = Counter(state_of(c) or kb_lib.NONE_MARK for c in comments)
        body += [f"- 살아 있는 주석 **{len(comments)}** · 해소되지 않은 것(`해소: {kb_lib.COMMENT_OPEN}`) **{pct(len(open_), len(comments))}** · "
                 f"그중 게이트를 막는 `{kb_lib.COMMENT_BLOCKING[0]} ({kb_lib.COMMENT_BLOCKING[1]})` **{len(blocking)}** "
                 f"(목표 0 — 게이트 `{kb_lib.BLOCKING_COMMENT_GATE}`)", "",
                 "| 라벨 | 주석 수 | 그중 해소 열림 |", "|---|---|---|"]
        body += [f"| `{k}` | {v} | {sum(1 for c in open_ if (label_of(c) or kb_lib.NONE_MARK) == k)} |" for k, v in labels.most_common()]
        body += ["", "| 해소 상태 | 주석 수 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in states.most_common()] + [""]
        judged = {c for c in comments if by_gen(c) == kb_lib.JUDGE_GENERATOR}
        body += round_section(Counter(m.at(c)[:10] for c in comments if c not in judged), len(judged))
        if blocking:
            body += ["게이트를 막는 주석:", ""] + [f"- `{Path(m.location[c]).stem}` {m.ko(c)} → "
                     + (" · ".join(m.ko(t) for t in g.objects(c, AGT.targets)) or kb_lib.NONE_MARK) for c in blocking] + [""]
    return body
```
<!-- 인용 끝 -->
