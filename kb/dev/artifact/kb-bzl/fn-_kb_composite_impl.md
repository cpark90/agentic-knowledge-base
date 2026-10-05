---
id: https://agentic-knowledge-base.dev/id/chunk/9ea0fc86-c0a7-40b9-9890-52de62a048a9
type: artifact
level: executable
title_ko: 함수 _kb_composite_impl (defs/kb.bzl)
title: function _kb_composite_impl in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f39dff5d-eec4-44a9-a9eb-ac03d49b15bb
---
**함수** — `_kb_composite_impl(ctx)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _kb_composite_impl(ctx):
    n = len(ctx.attr.part_iris)
    if n < 2:
        fail("%s: 복합체는 부분 둘 이상의 묶음이다 — 부분 하나면 청크다 (4.5절): 부분 %d" % (ctx.label, n))
    if n > MAX_PARTS:
        fail("%s: 직접 부분은 최대 %d개(7±2)다 (4.5절): 부분 %d" % (ctx.label, MAX_PARTS, n))
    if len(ctx.files.srcs) < n:
        fail("%s: 부분이 묶음 밖에 있다 — 부분 청크는 이 액션의 입력 집합 안에 있어야 한다 (4.5절): 파일 %d · 부분 %d" %
             (ctx.label, len(ctx.files.srcs), n))
    _check_residency(ctx.label, ctx.attr.plane, ctx.attr.level)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, ctx.attr.plane, ctx.attr.level)
    if ctx.attr.ordered:
        _check_order(ctx.label, ctx.attr.ordered, ctx.attr.part_iris)
    if ctx.attr.conventions and ctx.attr.plane != "norm":
        fail("%s: conventions 는 규범 문서의 절(plane norm)의 복합체에만 준다 — 실제 plane %s (p12-norm-documents-from-section-chunks)" %
             (ctx.label, ctx.attr.plane))
    return _composite_outputs(ctx, ctx.attr.plane, ctx.attr.level, ctx.files.srcs, ctx.attr.part_iris, ctx.attr.ordered,
                              ctx.attr.conventions)
```
<!-- 인용 끝 -->
