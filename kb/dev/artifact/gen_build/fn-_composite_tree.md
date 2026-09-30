---
id: https://agentic-knowledge-base.dev/id/chunk/6b2fd7de-ac08-40ec-a4c0-7976d20b1f34
type: artifact
level: executable
title_ko: 함수 _composite_tree (tools/gen_build.py)
title: function _composite_tree in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/569c6e75-e264-4981-bf0b-bba156b541c8
---
**함수** — `_composite_tree(root, children)` 다. 뿌리에서 닿는 복합체 IRI 전부 (자신 포함) — 순환은 호출 전에 거부된다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _composite_tree(root, children):
    """뿌리에서 닿는 복합체 IRI 전부 (자신 포함) — 순환은 호출 전에 거부된다."""
    out, stack = [], [root]
    while stack:
        c = stack.pop()
        out.append(c)
        stack.extend(sorted(children.get(c, [])))
    return sorted(out)
```
<!-- 인용 끝 -->
