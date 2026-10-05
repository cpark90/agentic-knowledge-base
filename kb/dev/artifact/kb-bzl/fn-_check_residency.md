---
id: https://agentic-knowledge-base.dev/id/chunk/6eac2ae1-8d4b-41bd-9b7e-17100fd21d92
type: artifact
level: executable
title_ko: 함수 _check_residency (defs/kb.bzl)
title: function _check_residency in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/de15c0eb-b277-4159-9610-3cf83fed1763
---
**함수** — `_check_residency(label, plane, level)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _check_residency(label, plane, level):
    if plane not in PLANES:
        fail("%s: 알 수 없는 plane %r" % (label, plane))
    if level not in RESIDENCY[plane]:
        fail("%s: 수준 허용표 위반 — plane %s 는 level %s 에 살 수 없다 (6.4절)" % (label, plane, level))
```
<!-- 인용 끝 -->
