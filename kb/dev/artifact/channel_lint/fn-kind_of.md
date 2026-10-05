---
id: https://agentic-knowledge-base.dev/id/chunk/8857ba5c-fc60-4ee1-a15b-2a87ed72940f
type: artifact
level: executable
title_ko: 함수 kind_of (tools/channel_lint.py)
title: function kind_of in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6
---
**함수** — `kind_of(p)` 다. 경로 → (종류, 자리).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def kind_of(p: Path) -> tuple[str, str] | None:
    """경로 → (종류, 자리). 종류는 message·questionnaire, 자리는 수신함 이름·archive·user. 규약 밖 경로면 None."""
    parent, grand = p.parent.name, p.parent.parent.name
    if grand == "channel" and (parent in INBOXES or parent == ARCHIVE):
        return "message", parent
    if parent == "user":
        return "questionnaire", "user"
    if parent == ARCHIVE and grand == "user":
        return "questionnaire", ARCHIVE
    return None
```
<!-- 인용 끝 -->
