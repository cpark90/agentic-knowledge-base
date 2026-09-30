---
id: https://agentic-knowledge-base.dev/id/chunk/6c400590-b47a-4724-88dc-6d918284ffac
type: artifact
level: executable
title_ko: 함수 list_rule_counts (tools/consistency.py)
title: function list_rule_counts in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/02bb9c9f-7720-4f02-ae31-b3eee5ba6865
---
**함수** — `list_rule_counts(list_hits)` 다. ⑨ 의 위반을 규칙별로 센다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def list_rule_counts(list_hits):
    """⑨ 의 위반을 규칙별로 센다 — 규칙마다 다음 행동이 다르다(번호는 치환, 줄 수·항목 수는 분할)."""
    LIST_KINDS = (("손 번호", "손 번호"), ("항목 수", "개다"), ("중첩", "중첩"), ("항목 길이", "자다"), ("빈 항목", "빈 목록"))
    list_kinds = [(name, sum(1 for _, _, why in list_hits if key in why)) for name, key in LIST_KINDS]
    return [(k, v) for k, v in list_kinds if v]
```
<!-- 인용 끝 -->
