---
id: https://agentic-knowledge-base.dev/id/chunk/8b1b0dcd-b04d-42f6-a3d6-849e3fe97268
type: artifact
level: executable
title_ko: 함수 _when_tokens (tools/kb_lib.py)
title: function _when_tokens in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/749019ce-0d81-4c5f-b549-f44c1b0d4e55
---
**함수** — `_when_tokens(expr)` 다. 식 → 토큰 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _when_tokens(expr: str) -> list:
    """식 → 토큰 목록. ("in", 이름) · ("op", 기호) · ("lit", True|False) · ("?", 원문) 넷이다."""
    out, i, n = [], 0, len(expr)
    while i < n:
        if expr[i].isspace():
            i += 1
            continue
        for pat, tag in ((_WHEN_IN, "in"), (_WHEN_OP, "op"), (_WHEN_LIT, "lit")):
            m = pat.match(expr, i)
            if m:
                out.append((tag, m.group(1) if tag == "in" else m.group(0) == "true" if tag == "lit" else m.group(0)))
                i = m.end()
                break
        else:
            m = _WHEN_OTHER.match(expr, i)
            out.append(("?", m.group(0)))
            i = m.end()
    return out
```
<!-- 인용 끝 -->
