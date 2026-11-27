---
id: https://agentic-knowledge-base.dev/id/chunk/69a84092-df60-4eb4-aed8-32d7724ec3f2
type: artifact
level: executable
title_ko: 함수 bin_of (tools/belief_calibration.py)
title: function bin_of in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7b6663a6-1c06-4819-aae0-798a36f11390
---
**함수** — `bin_of(p)` 다. 값 → 구간 번호.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def bin_of(p: Fraction) -> int:
    """값 → 구간 번호. [0, 1/3) · [1/3, 2/3) · [2/3, 1] — 경계값은 위 구간에 든다."""
    return 0 if p < BINS[1][0] else 1 if p < BINS[2][0] else 2
```
<!-- 인용 끝 -->
