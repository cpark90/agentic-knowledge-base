---
id: https://agentic-knowledge-base.dev/id/chunk/df43fa6f-d424-49d0-aec2-0aea8545572a
type: artifact
level: executable
title_ko: 함수 pair_target (tools/kb_lib.py)
title: function pair_target in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6309baee-3513-4835-affe-e76a4382e7d5
---
**함수** — `pair_target(anchor, target, kind)` 다. 판정 로그 `대상` 열의 쌍 꼴 — `parse_pair_target` 이 되읽는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_target(anchor: str, target: str, kind: str) -> str:
    """판정 로그 `대상` 열의 쌍 꼴 — `parse_pair_target` 이 되읽는다."""
    return f"{anchor}{JUDGE_PAIR_SEP}{target}{JUDGE_PAIR_KIND_SEP}{kind}"
```
<!-- 인용 끝 -->
