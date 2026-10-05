---
id: https://agentic-knowledge-base.dev/id/chunk/57d4b0bb-fce0-462b-ba05-e71e7206bf74
type: artifact
level: executable
title_ko: 함수 fill_any (tools/case_gen.py)
title: function fill_any in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b32a6a71-a1e8-4f65-89b7-47ea42f67f32]
part_of: https://agentic-knowledge-base.dev/id/composite/7cb71e27-ad8a-449d-b46a-454149642b32
---
**함수** — `fill_any(obj, values)` 다. 템플릿 값 전체(문자열·목록·매핑)에 fill 을 건다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def fill_any(obj, values: dict):
    """템플릿 값 전체(문자열·목록·매핑)에 fill 을 건다."""
    if isinstance(obj, str):
        return fill(obj, values)
    if isinstance(obj, list):
        return [fill_any(x, values) for x in obj]
    if isinstance(obj, dict):
        return {fill(k, values) if isinstance(k, str) else k: fill_any(v, values) for k, v in obj.items()}
    return obj
```
<!-- 인용 끝 -->
