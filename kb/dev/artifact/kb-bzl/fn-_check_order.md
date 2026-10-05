---
id: https://agentic-knowledge-base.dev/id/chunk/1bd8f244-2394-47da-84b8-ccc6b62491f3
type: artifact
level: executable
title_ko: 함수 _check_order (defs/kb.bzl)
title: function _check_order in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f39dff5d-eec4-44a9-a9eb-ac03d49b15bb
---
**함수** — `_check_order(label, ordered, part_iris)` 다. 선언된 순서가 부분 전부를 빠짐없이 한 번씩 담는가 — 분석 시점 fail.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _check_order(label, ordered, part_iris):
    """선언된 순서가 부분 전부를 빠짐없이 한 번씩 담는가 — 분석 시점 fail. 색인 1..n 의 정합성은 shape 가 본다."""
    if sorted(ordered) != sorted(part_iris):
        fail("%s: ordered 가 부분 집합과 다르다 — 순서 목록은 부분 전부를 빠짐없이 한 번씩 담는다 (p4-composite-order-is-declared): %s ≠ %s" %
             (label, ordered, part_iris))
```
<!-- 인용 끝 -->
