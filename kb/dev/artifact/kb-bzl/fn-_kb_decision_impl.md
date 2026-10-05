---
id: https://agentic-knowledge-base.dev/id/chunk/2293c3e9-50cc-4f0a-a8f4-3fa05b5eb583
type: artifact
level: executable
title_ko: 함수 _kb_decision_impl (defs/kb.bzl)
title: function _kb_decision_impl in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f39dff5d-eec4-44a9-a9eb-ac03d49b15bb
---
**함수** — `_kb_decision_impl(ctx)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _kb_decision_impl(ctx):
    levels = ctx.attr.part_levels
    n = 4 if ctx.file.conventions else 3  # 세 청크는 필수이고 규약 청크는 선택 넷째다 (p4-convention-slot, 유저 답 Q22-b)
    if len(levels) != n or len(ctx.attr.part_iris) != n:
        fail("%s: 결정은 결론·근거·대안 세 청크(+ 선택 규약 청크)의 복합체다 (7.4절, p4-convention-slot) — 부분 파일 %d · 수준 %d · IRI %d" %
             (ctx.label, n, len(levels), len(ctx.attr.part_iris)))
    for lv in levels:
        _check_residency(ctx.label, "decision", lv)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, "decision", levels[0])
    _check_order(ctx.label, ctx.attr.ordered, ctx.attr.part_iris)  # 결정도 예외가 없다 — 순서는 선언이고 인자가 필수다
    files = [ctx.file.conclusion, ctx.file.rationale, ctx.file.alternatives] + ([ctx.file.conventions] if ctx.file.conventions else [])
    return _composite_outputs(ctx, "decision", levels[0], files, ctx.attr.part_iris, ctx.attr.ordered)
```
<!-- 인용 끝 -->
