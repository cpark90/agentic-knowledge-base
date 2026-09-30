---
id: https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884
type: artifact
level: executable
title_ko: 함수 waived (tools/kb_lib.py)
title: function waived in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/4292d5fd-0111-4512-921f-82e93540b998]
part_of: https://agentic-knowledge-base.dev/id/composite/ee34751d-8520-4de7-a22b-b2a1136b9dbf
---
**함수** — `waived(waivers, gate_id, target, axis)` 다. 게이트 `gate_id` 에서 `target` 이 `axis` 축으로 면제 선언됐는가.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def waived(waivers: list[dict], gate_id: str, target: str, axis: str) -> bool:
    """게이트 `gate_id` 에서 `target` 이 `axis` 축으로 면제 선언됐는가."""
    return any(w["gate"] == gate_id and w["axis"] == axis and any(_target_matches(d, target, axis) for d in w["targets"])
               for w in waivers)
```
<!-- 인용 끝 -->
