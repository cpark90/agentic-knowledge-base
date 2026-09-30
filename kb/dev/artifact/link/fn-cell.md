---
id: https://agentic-knowledge-base.dev/id/chunk/ec5e9dfa-5521-4e0c-8ae8-6be045e70e81
type: artifact
level: executable
title_ko: 함수 cell (tools/link.py)
title: function cell in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d
---
**함수** — `cell(text)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")
```
<!-- 인용 끝 -->
