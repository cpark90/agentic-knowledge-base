---
id: https://agentic-knowledge-base.dev/id/chunk/37d74334-40cf-4370-ba39-2a78da325338
type: artifact
level: executable
title_ko: 함수 record_header_old (tools/kb_lib.py)
title: function record_header_old in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
---
**함수** — `record_header_old(at)` 다. 기록 시각 `at`(frontmatter `generated.at` 의 값, 없으면 None) → 그 기록이 옛 표 머리(`*_OLD`)를 받는가.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def record_header_old(at) -> bool:
    """기록 시각 `at`(frontmatter `generated.at` 의 값, 없으면 None) → 그 기록이 옛 표 머리(`*_OLD`)를 받는가.

    시간대가 있는 시각이 `RECORD_HEADER_SINCE` 이전일 때만 참이다. 시각이 없거나, 읽지 못하거나, 시간대가 없으면 거짓이고
    그 기록은 새 머리를 요구한다 (Q161-a). 기록 머리를 시각으로 가르는 판단의 단일 정의 위치가 이 함수다 (Q164-a)."""
    if at is None:
        return False
    try:
        when = datetime.fromisoformat(str(at).replace("Z", "+00:00"))
    except ValueError:
        return False
    return when.tzinfo is not None and when < datetime.fromisoformat(RECORD_HEADER_SINCE)
```
<!-- 인용 끝 -->
