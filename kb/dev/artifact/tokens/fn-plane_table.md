---
id: https://agentic-knowledge-base.dev/id/chunk/88215097-083d-4315-8983-eff5433360ad
type: artifact
level: executable
title_ko: 함수 plane_table (tools/tokens.py)
title: function plane_table in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T10:12:42Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2dcb7b2a-d62d-446a-abd6-5f776c990c7e]
part_of: https://agentic-knowledge-base.dev/id/composite/bb329900-d369-44b7-88d4-5e3996dc0aa5
---
**함수** — `plane_table(rows)` 다. plane 별 분포 — 청크 수·최소·1사분위·중앙·3사분위·최대·줄당 토큰 중앙값.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def plane_table(rows: list[dict]) -> list[str]:
    """plane 별 분포 — 청크 수·최소·1사분위·중앙·3사분위·최대·줄당 토큰 중앙값."""
    out = ["| plane | 청크 | 최소 | 1사분위 | 중앙 | 3사분위 | 최대 | 줄당 토큰 중앙 |", "|---|---|---|---|---|---|---|---|"]
    groups = {}
    for r in rows:
        groups.setdefault(r["plane"], []).append(r)
    for plane in sorted(groups) + ["전체"]:
        g = rows if plane == "전체" else groups[plane]
        lo, q1, med, q3, hi = quantiles([r["tokens"] for r in g])
        per = statistics.median([r["tokens"] / r["lines"] for r in g if r["lines"]])
        out.append(f"| {plane} | {len(g)} | {lo} | {q1} | {med} | {q3} | {hi} | {per:.1f} |")
    return out + [""]
```
<!-- 인용 끝 -->
