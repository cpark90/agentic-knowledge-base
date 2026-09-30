---
id: https://agentic-knowledge-base.dev/id/chunk/829ed4f8-dab5-4026-a1d3-0bd17bb6c708
type: artifact
level: executable
title_ko: 함수 _own_lines (tools/extract.py)
title: function _own_lines in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `_own_lines(r)` 다. 구역의 제 몫 줄 범위 — 하위 구역과 정의의 본문을 뺀 나머지 (절 주석과 그 절의 상수).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _own_lines(r: Region) -> list[tuple[int, int]]:
    """구역의 제 몫 줄 범위 — 하위 구역과 정의의 본문을 뺀 나머지 (절 주석과 그 절의 상수)."""
    taken = [(c.start, c.end) for c in r.children] + [(n.lineno if not n.decorator_list else n.decorator_list[0].lineno, n.end_lineno)
                                                      for _, n in r.defs]
    spans, cur = [], r.start
    for a, b in sorted(taken):
        if a > cur:
            spans.append((cur, a - 1))
        cur = max(cur, b + 1)
    if cur <= r.end:
        spans.append((cur, r.end))
    return spans
```
<!-- 인용 끝 -->
