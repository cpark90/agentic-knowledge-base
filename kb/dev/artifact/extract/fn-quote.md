---
id: https://agentic-knowledge-base.dev/id/chunk/8961c276-af1a-4b25-82aa-8ea7a53a20d0
type: artifact
level: executable
title_ko: 함수 quote (tools/extract.py)
title: function quote in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0
---
**함수** — `quote(lines, lang)` 다. 인용 구역 — 소스를 그대로 옮긴 코드 펜스.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def quote(lines: list[str], lang: str = "python") -> list[str]:
    """인용 구역 — 소스를 그대로 옮긴 코드 펜스. 생성기는 원문을 고쳐 쓰지 않는다."""
    return [kb_lib.SOURCE_QUOTE_OPEN, f"```{lang}", *[l.rstrip() for l in lines], "```", kb_lib.SOURCE_QUOTE_CLOSE]
```
<!-- 인용 끝 -->
