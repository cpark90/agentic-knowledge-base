---
id: https://agentic-knowledge-base.dev/id/chunk/bc4094f8-5d74-42ab-8efd-d981c7993732
type: artifact
level: executable
title_ko: 함수 _is_vv (defs/kb.bzl)
title: function _is_vv in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/de15c0eb-b277-4159-9610-3cf83fed1763
---
**함수** — `_is_vv(label)` 다. V&V KB 의 타깃인가 — 패키지 접두 kb/vv (pe-storage-layout).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _is_vv(label):
    """V&V KB 의 타깃인가 — 패키지 접두 kb/vv (pe-storage-layout). 그 밖(kb/dev·chunks)은 개발 KB 다."""
    return label.package == "kb/vv" or label.package.startswith("kb/vv/")
```
<!-- 인용 끝 -->
