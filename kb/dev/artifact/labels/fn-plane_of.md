---
id: https://agentic-knowledge-base.dev/id/chunk/f13654f3-9b08-41f4-a1f1-9688dccc4dd0
type: artifact
level: executable
title_ko: 함수 plane_of (tools/labels.py)
title: function plane_of in tools/labels.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-labels}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/fba87a37-4ad2-4ccb-b556-a27d4ef6b9d2
---
**함수** — `plane_of(group)` 다. 항목 디렉토리 → plane 디렉토리.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def plane_of(group: str) -> str:
    """항목 디렉토리 → plane 디렉토리. 결정 복합체처럼 디렉토리가 한 겹 더 있으면 그 부모가 plane 이다."""
    return str(Path(group).parent) if len(Path(group).parts) > 3 else group
```
<!-- 인용 끝 -->
