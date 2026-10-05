---
id: https://agentic-knowledge-base.dev/id/chunk/708eb95d-56a9-4df5-883c-65f3f6821507
type: artifact
level: executable
title_ko: 함수 _check_links (defs/kb.bzl)
title: function _check_links in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/de15c0eb-b277-4159-9610-3cf83fed1763
---
**함수** — `_check_links(ctx, plane, level)` 다. 링크 방향의 구조 판정 — 분석 시점 fail.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _check_links(ctx, plane, level):
    """링크 방향의 구조 판정 — 분석 시점 fail. 의미 판정은 그래프 게이트가 한다."""
    for dep in ctx.attr.refines + ctx.attr.serves:
        t = dep[ChunkInfo]
        if LEVELS.index(t.level) >= LEVELS.index(level):
            fail("%s: refines/serves 대상 %s 은 더 높은 수준이어야 한다 (정제 계층 6.2절): %s → %s" % (ctx.label, dep.label, level, t.level))
        if PLANES.index(t.plane) > PLANES.index(plane):
            fail("%s: plane 단방향 위반 (5.2절) — %s 가 하위 plane %s 를 refines 한다" % (ctx.label, plane, t.plane))
    for dep in ctx.attr.serves:
        if dep[ChunkInfo].plane != "requirement":
            fail("%s: serves 의 대상은 requirement 뿐이다 (6.8절): %s" % (ctx.label, dep.label))
    for dep in ctx.attr.supersedes:
        if dep[ChunkInfo].plane != plane:
            fail("%s: supersedes 는 같은 plane 안에서만 (7.4절): %s → %s" % (ctx.label, plane, dep[ChunkInfo].plane))
    for dep in ctx.attr.refines + ctx.attr.serves + ctx.attr.supersedes:
        if _is_vv(ctx.label) != _is_vv(dep.label):
            fail("%s: refines/serves/supersedes 는 KB 안에서만이다 — KB 를 가로지르는 링크는 verifies 뿐이다 (V&V → 개발, 7.5절): %s" % (ctx.label, dep.label))
    for dep in ctx.attr.verifies:
        if not _is_vv(ctx.label):
            fail("%s: verifies 의 주어는 V&V KB 청크뿐이다 (8.5절)" % ctx.label)
        if _is_vv(dep.label):
            fail("%s: verifies 의 대상은 개발 KB 청크다: %s" % (ctx.label, dep.label))
        if dep[ChunkInfo].level != level:
            fail("%s: verifies 는 같은 수준끼리 (8.3절 검증 대응물): %s ≠ %s" % (ctx.label, level, dep[ChunkInfo].level))
```
<!-- 인용 끝 -->
