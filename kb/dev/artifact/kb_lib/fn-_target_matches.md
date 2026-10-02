---
id: https://agentic-knowledge-base.dev/id/chunk/4292d5fd-0111-4512-921f-82e93540b998
type: artifact
level: executable
title_ko: 함수 _target_matches (tools/kb_lib.py)
title: function _target_matches in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee34751d-8520-4de7-a22b-b2a1136b9dbf
---
**함수** — `_target_matches(declared, target, axis)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _target_matches(declared: str, target: str, axis: str) -> bool:
    if axis == "파일":
        t = Path(target).as_posix()
        return t == declared or t.endswith("/" + declared)  # 루트 상대 경로 또는 그 접미(절대 경로로 불렸을 때)
    return declared == target
```
<!-- 인용 끝 -->
