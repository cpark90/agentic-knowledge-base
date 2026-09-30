---
id: https://agentic-knowledge-base.dev/id/chunk/ca2a23f5-0877-4142-9961-4660b6d48c41
type: artifact
level: executable
title_ko: 함수 analyse_terms (tools/consistency.py)
title: function analyse_terms in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/980ff6a4-1f10-4e39-bd06-73c6c65e5d37
---
**함수** — `analyse_terms(items, terms, waivers)` 다. ⑥ 용어 — tier 1 만.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_terms(items, terms, waivers):
    """⑥ 용어 — tier 1 만. 면제 파일(waivers.md, term-drift)의 히트는 집계에서 빼되 목록에 남긴다."""
    term_hits, term_waived = [], []
    for old, std in terms:
        for it in items:
            if old in it["body"] or old in it["title_ko"]:
                (term_waived if waived(waivers, GATE_TERM, it["path"], "파일") else term_hits).append((old, std, it))
    return term_hits, term_waived
```
<!-- 인용 끝 -->
