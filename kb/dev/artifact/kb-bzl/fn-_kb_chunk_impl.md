---
id: https://agentic-knowledge-base.dev/id/chunk/529ee1d7-f1a4-4eda-a71b-562040bdba47
type: artifact
level: executable
title_ko: 함수 _kb_chunk_impl (defs/kb.bzl)
title: function _kb_chunk_impl in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/327a7a64-22f6-4b2b-a0d2-542146d25d6f
---
**함수** — `_kb_chunk_impl(ctx)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _kb_chunk_impl(ctx):
    _check_residency(ctx.label, ctx.attr.plane, ctx.attr.level)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, ctx.attr.plane, ctx.attr.level)
    src = ctx.file.src
    head = _head_action(ctx, [src])
    return [
        DefaultInfo(files = depset([src])),
        ChunkInfo(iri = ctx.attr.iri, plane = ctx.attr.plane, level = ctx.attr.level, status = ctx.attr.status, srcs = depset([src]), parts = []),
        KgInfo(ttl = depset([head])),
        OutputGroupInfo(_validation = depset([_lint_action(ctx, [src])]), kg = depset([head])),
    ]
```
<!-- 인용 끝 -->
