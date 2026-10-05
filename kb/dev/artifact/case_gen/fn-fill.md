---
id: https://agentic-knowledge-base.dev/id/chunk/b32a6a71-a1e8-4f65-89b7-47ea42f67f32
type: artifact
level: executable
title_ko: 함수 fill (tools/case_gen.py)
title: function fill in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7cb71e27-ad8a-449d-b46a-454149642b32
---
**함수** — `fill(text, values)` 다. `${변수}` → 값.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def fill(text: str, values: dict) -> str:
    """`${변수}` → 값. 변수의 실재는 check_case_template 이 이미 보았다."""
    return TEMPLATE.sub(lambda m: str(values[m.group(1)]), text)
```
<!-- 인용 끝 -->
