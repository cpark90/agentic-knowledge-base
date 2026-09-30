---
id: https://agentic-knowledge-base.dev/id/chunk/d75bedf5-7e0c-4441-b80e-9ead963a2b0e
type: artifact
level: executable
title_ko: 함수 plane_of (tools/impact.py)
title: function plane_of in tools/impact.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-impact}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/44b63663-ac34-40f1-92c6-a6281c93c7a6
---
**함수** — `plane_of(label)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def plane_of(label: str) -> str:
    pkg = label.split(":")[0]
    return {"//kb/dev/requirement": "requirement", "//kb/dev/decision": "decision", "//chunks/decision": "decision(deprecated)"}.get(pkg, pkg.split("/")[-1] or "?")
```
<!-- 인용 끝 -->
