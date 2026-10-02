---
id: https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e
type: artifact
level: executable
title_ko: 함수 pct (tools/kb_lib.py)
title: function pct in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
---
**함수** — `pct(n, d)` 다. G15 — 비율은 `n/d = p.p%` 꼴이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pct(n: int, d: int) -> str:
    """G15 — 비율은 `n/d = p.p%` 꼴이다. 분모 없는 백분율을 쓰지 않는다. 0 분모는 없음이다 (G14)."""
    return f"{n}/{d} = {100 * n / d:.{RATIO_DIGITS}f}%" if d else NONE_MARK
```
<!-- 인용 끝 -->
