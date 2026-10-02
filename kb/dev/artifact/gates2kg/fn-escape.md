---
id: https://agentic-knowledge-base.dev/id/chunk/f15f1ad5-6a97-49e0-a1b6-d7cc84dd3b8e
type: artifact
level: executable
title_ko: 함수 escape (tools/gates2kg.py)
title: function escape in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T15:47:27Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ff1c5437-57a6-409e-86e7-767ffd3d41ff
---
**함수** — `escape(text)` 다. TTL 문자열 리터럴의 이스케이프 — 역슬래시와 따옴표만 나온다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def escape(text: str) -> str:
    """TTL 문자열 리터럴의 이스케이프 — 역슬래시와 따옴표만 나온다 (설명은 한 줄이다)."""
    return text.replace("\\", "\\\\").replace('"', '\\"')
```
<!-- 인용 끝 -->
