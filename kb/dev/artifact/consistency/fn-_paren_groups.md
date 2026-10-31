---
id: https://agentic-knowledge-base.dev/id/chunk/cfb0a4b8-f534-4e19-875d-07dfe88eb9b4
type: artifact
level: executable
title_ko: 함수 _paren_groups (tools/consistency.py)
title: function _paren_groups in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
---
**함수** — `_paren_groups(text)` 다. 최상위 괄호 묶음 → [(여는 위치, 닫는 위치 + 1)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _paren_groups(text: str):
    """최상위 괄호 묶음 → [(여는 위치, 닫는 위치 + 1)]. 짝 없는 닫는 괄호("1)")는 무시한다."""
    out, depth, start = [], 0, 0
    for i, ch in enumerate(text):
        if ch in "(（":
            if depth == 0:
                start = i
            depth += 1
        elif ch in ")）" and depth:
            depth -= 1
            if depth == 0:
                out.append((start, i + 1))
    return out
```
<!-- 인용 끝 -->
