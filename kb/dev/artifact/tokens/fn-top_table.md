---
id: https://agentic-knowledge-base.dev/id/chunk/9dca3dba-bb72-415b-a4cb-bcf5058e807f
type: artifact
level: executable
title_ko: 함수 top_table (tools/tokens.py)
title: function top_table in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T10:12:42Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bb329900-d369-44b7-88d4-5e3996dc0aa5
---
**함수** — `top_table(rows)` 다. 토큰 수 상위 청크 — 분할의 첫 대상이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def top_table(rows: list[dict]) -> list[str]:
    """토큰 수 상위 청크 — 분할의 첫 대상이다."""
    out = ["| 토큰 | 줄 | plane | 청크 |", "|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (-r["tokens"], r["path"]))[:TOP_N]:
        out.append(f"| {r['tokens']} | {r['lines']} | {r['plane']} | `{r['path']}` |")
    return out + [""]
```
<!-- 인용 끝 -->
