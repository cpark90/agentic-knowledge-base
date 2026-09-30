---
id: https://agentic-knowledge-base.dev/id/chunk/a5547d6c-a232-4c09-83b0-81eb591e8bc6
type: artifact
level: executable
title_ko: 함수 decision_role_marker (tools/kb_lib.py)
title: function decision_role_marker in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/efdfa170-bf07-4ef8-9d31-b554c7e26f8c
---
**함수** — `decision_role_marker(path)` 다. 파일 경로가 요구하는 역할 표지 — 시나리오 패키지의 세 접미가 자극·요인·배제 자극, 결정 세 청크의 stem 이 결론·근거·대안, 그 밖(단일 파일 결정·단일 청크 시나리오)이 결론이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decision_role_marker(path) -> str:
    """파일 경로가 요구하는 역할 표지 — 시나리오 패키지의 세 접미가 자극·요인·배제 자극, 결정 세 청크의 stem 이 결론·근거·대안,
    그 밖(단일 파일 결정·단일 청크 시나리오)이 결론이다."""
    p = Path(path)
    if p.parent.name == SCENARIO_DIR:
        for suffix, mark in SCENARIO_ROLE_MARKERS.items():
            if p.stem.endswith("-" + suffix):
                return mark
    return DECISION_ROLE_MARKERS.get(p.stem, DECISION_SINGLE_FILE_MARKER)
```
<!-- 인용 끝 -->
