---
id: https://agentic-knowledge-base.dev/id/chunk/75af5f0a-9a09-4d47-8289-a31801125bfe
type: artifact
level: executable
title_ko: 함수 waived_tail (tools/consistency.py)
title: function waived_tail in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/e33ee826-0842-4cdd-8e68-16823604cffa
---
**함수** — `waived_tail(hits, gate, render)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def waived_tail(hits, gate, render):
    if not hits:
        return []
    return [f"- 면제 {len(hits)}건(waivers.md, `{gate}`) — 집계에서 뺐다:"] + ["  " + render(h) for h in hits[:50]]
```
<!-- 인용 끝 -->
