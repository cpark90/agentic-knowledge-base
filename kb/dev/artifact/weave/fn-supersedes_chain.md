---
id: https://agentic-knowledge-base.dev/id/chunk/b620c1cf-7e83-4b6f-9176-454c6fe3091a
type: artifact
level: executable
title_ko: 함수 supersedes_chain (tools/weave.py)
title: function supersedes_chain in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ec24ef39-7e27-4fff-bba3-6fdb1829b342
---
**함수** — `supersedes_chain(m, parts)` 다. 대체 연쇄 — 부분들이 supersedes 하는 옛 결정과 그 옛 결정이 다시 supersedes 하는 것 (순환은 끊는다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def supersedes_chain(m: Model, parts) -> str:
    """대체 연쇄 — 부분들이 supersedes 하는 옛 결정과 그 옛 결정이 다시 supersedes 하는 것 (순환은 끊는다)."""
    firsts = sorted({t for p in parts for t in m.g.objects(p, AGT.supersedes)}, key=str)
    if not firsts:
        return "없음"
    chains = []
    for first in firsts:
        chain, cur, seen = [], first, set()
        while cur is not None and cur not in seen:
            seen.add(cur)
            chain.append(f"{m.ko(cur)} (`{kb_lib.compact_iri(str(cur))}`, {m.status.get(cur, '?')})")
            nxt = sorted(m.g.objects(cur, AGT.supersedes), key=str)
            cur = nxt[0] if nxt else None
        chains.append(" ← ".join(chain))
    return " · ".join(chains)
```
<!-- 인용 끝 -->
