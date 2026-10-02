---
id: https://agentic-knowledge-base.dev/id/chunk/193fbeed-19f3-4ecf-a72d-50c6c66a5e53
type: artifact
level: executable
title_ko: 함수 lane_of (tools/channel_lint.py)
title: function lane_of in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T11:29:42Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6
---
**함수** — `lane_of(p)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def lane_of(p: Path) -> str:
    return p.parent.name if p.parent.name in (AGENTS, INQUIRIES, HANDOFF) else USER
```
<!-- 인용 끝 -->
