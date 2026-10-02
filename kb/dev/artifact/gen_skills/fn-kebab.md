---
id: https://agentic-knowledge-base.dev/id/chunk/f4e15fab-b378-46c2-b8ae-ca2982aa9dcd
type: artifact
level: executable
title_ko: 함수 kebab (tools/gen_skills.py)
title: function kebab in tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/210e1533-9390-4961-914e-3e556e96fe3d
---
**함수** — `kebab(tool)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def kebab(tool: str) -> str:
    return tool.replace("_", "-")
```
<!-- 인용 끝 -->
