---
id: https://agentic-knowledge-base.dev/id/chunk/a0b3f8e3-4420-406f-9077-a1c20200be2f
type: artifact
level: executable
title_ko: 함수 render_distribution (tools/metrics.py)
title: function render_distribution in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/b2057520-5b84-4543-a292-bcedbb44ef9d
---
**함수** — `render_distribution(pct, chunks, live, plane, level, orphans)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_distribution(pct, chunks, live, plane, level, orphans):
    o = ["## plane × level (살아 있는 청크)", "", "| plane | " + " | ".join(LEVELS) + " | 합 |", "|---|" + "---|" * (len(LEVELS) + 1)]
    for p in PLANES:
        row = [sum(1 for c in live if plane[c] == p and level[c] == l) for l in LEVELS]
        o.append(f"| `{p}` | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    o += ["", "## 고아율 (4.13절 — 복합체 부분도 링크도 없는 청크)", "",
          f"- 전체: **{pct(len(orphans), len(chunks))}**",
          f"- 살아 있는 청크: **{pct(len(orphans & live), len(live))}** (목표 10% 미만) — 도입 1단계 통과 조건: **{'통과' if len(live) and len(orphans & live)/len(live) < 0.10 else '미통과'}**"]
    for p in PLANES:
        n = sum(1 for c in live if plane[c] == p)
        if n: o.append(f"  - `{p}`: {pct(sum(1 for c in orphans & live if plane[c] == p), n)}")
    return o
```
<!-- 인용 끝 -->
