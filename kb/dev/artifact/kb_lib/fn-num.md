---
id: https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2
type: artifact
level: executable
title_ko: 함수 num (tools/kb_lib.py)
title: function num in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
---
**함수** — `num(x)` 다. G15 — 백분율이 아닌 수치의 자릿수.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def num(x: float) -> str:
    """G15 — 백분율이 아닌 수치의 자릿수. 모듈러리티 Q·Jaccard·링크 밀도·소요 초가 같은 자릿수를 쓴다."""
    return f"{x:.{VALUE_DIGITS}f}"
```
<!-- 인용 끝 -->
