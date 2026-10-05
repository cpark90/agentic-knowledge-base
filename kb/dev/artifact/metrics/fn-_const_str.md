---
id: https://agentic-knowledge-base.dev/id/chunk/5043c522-c415-4b84-99a0-cd5627e0b9d4
type: artifact
level: executable
title_ko: 함수 _const_str (tools/metrics.py)
title: function _const_str in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a599c470-8ce8-4e70-a475-1067401bb55c
---
**함수** — `_const_str(node)` 다. BUILD 의 문자열 식(상수와 `+` 이음)을 값으로 푼다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _const_str(node) -> str:
    """BUILD 의 문자열 식(상수와 `+` 이음)을 값으로 푼다. 다른 식은 빈 문자열이다."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return _const_str(node.left) + _const_str(node.right)
    return ""
```
<!-- 인용 끝 -->
