---
id: https://agentic-knowledge-base.dev/id/chunk/93603726-5c98-4055-96e5-fb41e9f77347
type: artifact
level: executable
title_ko: 함수 multiple_table (tools/tokens.py)
title: function multiple_table in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T10:12:42Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bb329900-d369-44b7-88d4-5e3996dc0aa5
---
**함수** — `multiple_table(rows)` 다. 42의 배수마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def multiple_table(rows: list[dict]) -> list[str]:
    """42의 배수마다 초과 청크 수와 비율 — 상한을 그 값으로 두면 몇 개를 쪼개야 하는가다."""
    n = len(rows)
    tokens = [r["tokens"] for r in rows]
    out = ["| 상한 | 배수 | 초과 청크 | 비율 |", "|---|---|---|---|"]  # 확정 상한은 42×26 과 42×68 이다
    for k in range(1, MULTIPLES + 1):
        limit = kb_lib.TOKEN_LIMIT_MULTIPLE * k
        over = sum(1 for t in tokens if t > limit)
        out.append(f"| {limit} | 42×{k} | {over} | {over}/{n} = {over / n:.1%} |")
    return out + [""]
```
<!-- 인용 끝 -->
