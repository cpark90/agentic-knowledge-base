---
id: https://agentic-knowledge-base.dev/id/chunk/681baacc-3465-444d-a6cd-65f4e14d2444
type: artifact
level: executable
title_ko: 절 -link-attrs (defs/kb.bzl)
title: section -link-attrs in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/327a7a64-22f6-4b2b-a0d2-542146d25d6f
composite: {id: https://agentic-knowledge-base.dev/id/composite/327a7a64-22f6-4b2b-a0d2-542146d25d6f, title_ko: 절 복합체 -link-attrs (defs/kb.bzl), title: section composite -link-attrs in defs/kb.bzl, ordered: [https://agentic-knowledge-base.dev/id/chunk/681baacc-3465-444d-a6cd-65f4e14d2444, https://agentic-knowledge-base.dev/id/chunk/529ee1d7-f1a4-4eda-a71b-562040bdba47], part_of: https://agentic-knowledge-base.dev/id/composite/84e893d0-8cc4-4710-b3b9-3885ce121377}
---
**절** — `defs/kb.bzl` 의 절 `-link-attrs` 다. 청크 규칙 (`kb_chunk`) — 청크 하나 = 타깃 하나. 링크 속성의 provider 요구가 끝점을 지식 항목으로 묶는다

**정의** — `_kb_chunk_impl` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 청크 규칙 (`kb_chunk`) — 청크 하나 = 타깃 하나. 링크 속성의 provider 요구가 끝점을 지식 항목으로 묶는다 ───
_LINK_ATTRS = {
    "refines": attr.label_list(providers = [ChunkInfo], doc = "정제 — 더 높은 수준의 항목으로 (6.2절)"),
    "serves": attr.label_list(providers = [ChunkInfo], doc = "기여 — 결정이 봉사하는 요구 (6.8절, ⊑ refines)"),
    "supersedes": attr.label_list(providers = [ChunkInfo], doc = "대체 — 같은 plane 의 옛 항목 (7.4절)"),
    "verifies": attr.label_list(providers = [ChunkInfo], doc = "검증 — V&V 청크만 주어 (8.5절)"),
    "_lint": attr.label(default = "//tools:chunk_lint", executable = True, cfg = "exec"),
    "_waivers": attr.label(default = "//docs:waivers", allow_single_file = True, doc = "게이트 면제 선언 (docs/waivers.md)"),
    "_chunk2kg": attr.label(default = "//tools:chunk2kg", executable = True, cfg = "exec"),
    "_residency": attr.label(default = "//defs:kb.bzl", allow_single_file = True, doc = "PLANES·LEVELS·STATES 값 어휘의 원본 (M1 단일 정의처)"),
    "_vocab": attr.label(default = "@tiktoken_o200k_base//file", allow_single_file = True, doc = "토큰 계수기의 어휘 파일 — 크기 판정과 agt:tokenCount 의 계수기 (p1-chunk-unit-is-tokens)"),
}


kb_chunk = rule(
    implementation = _kb_chunk_impl,
    doc = "청크 하나 = 타깃 하나. frontmatter 에서 생성된다 (tools/gen_build.py) — 손으로 쓰지 않는다.",
    attrs = dict({
        "src": attr.label(allow_single_file = [".md"], mandatory = True),
        "iri": attr.string(mandatory = True),
        "plane": attr.string(mandatory = True, values = PLANES),
        "level": attr.string(mandatory = True, values = LEVELS),
        "status": attr.string(default = "stable", values = STATES),
    }, **_LINK_ATTRS),
)
```
<!-- 인용 끝 -->
