---
id: https://agentic-knowledge-base.dev/id/chunk/b7ffd04b-bbcb-41aa-a69d-0b651364d2db
type: artifact
level: executable
title_ko: 함수 _alt (tools/chunk2kg.py)
title: function _alt in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a
---
**함수** — `_alt(words)` 다. 정규식 대안 — 긴 낱말을 앞에 둔다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _alt(words) -> str:
    """정규식 대안 — 긴 낱말을 앞에 둔다 (`non-blocking` 이 `blocking` 에 가려지지 않게)."""
    return "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))
```
<!-- 인용 끝 -->
