---
id: https://agentic-knowledge-base.dev/id/chunk/f58f73d7-95e7-4d7a-8bb5-687eaf43cb31
type: artifact
level: executable
title_ko: 함수 budget_lines (tools/tokens.py)
title: function budget_lines in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T10:12:42Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bb329900-d369-44b7-88d4-5e3996dc0aa5
---
**함수** — `budget_lines(rows)` 다. 예산 200줄의 토큰 환산 — 저작된 산문(요구·결정)의 줄당 토큰 중앙값 × 200 이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def budget_lines(rows: list[dict]) -> list[str]:
    """예산 200줄의 토큰 환산 — 저작된 산문(요구·결정)의 줄당 토큰 중앙값 × 200 이다."""
    sample = [r for r in rows if r["plane"] in BUDGET_PLANES and r["lines"]]
    per = statistics.median([r["tokens"] / r["lines"] for r in sample])
    budget = round(per * LINE_BUDGET_LINES)
    share = budget / VIEW_PLANES
    near = max(1, round(share / kb_lib.TOKEN_LIMIT_MULTIPLE))
    pooled = sum(r["tokens"] for r in sample) / sum(r["lines"] for r in sample)
    return [f"- 표본: {' · '.join(BUDGET_PLANES)} plane 의 청크 {len(sample)}개 — 저작된 산문이다",
            f"- 줄당 토큰 중앙값: {per:.2f}",
            f"- 표본 전체의 토큰 합 ÷ 줄 합: {pooled:.2f} — 중앙값과 갈리면 긴 청크가 끌어올린 값이다",
            f"- 예산 {LINE_BUDGET_LINES}줄의 토큰 환산: {budget}",
            f"- 조망 {VIEW_PLANES}개로 나눈 값: {share:.0f} — 가장 가까운 42의 배수는 "
            f"42×{near} = {kb_lib.TOKEN_LIMIT_MULTIPLE * near}", ""]
```
<!-- 인용 끝 -->
