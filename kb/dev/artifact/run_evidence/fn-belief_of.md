---
id: https://agentic-knowledge-base.dev/id/chunk/1fd3a79a-b431-4470-8d04-5282bbc0eb31
type: artifact
level: executable
title_ko: 함수 belief_of (tools/run_evidence.py)
title: function belief_of in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a7e4d5c8-a3b3-466a-93eb-1bb3d94b2ed5
---
**함수** — `belief_of(entries)` 다. 증거 항목들 [(종류, 극성, 확신도)] → 계산 규칙 slug → (값, 입력 증거 수, 사후 분산 또는 None).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def belief_of(entries: list[tuple[str, str, float | None]]) -> dict[str, tuple[float, int, float | None]]:
    """증거 항목들 [(종류, 극성, 확신도)] → 계산 규칙 slug → (값, 입력 증거 수, 사후 분산 또는 None). 입력이 없는 규칙은 값을 내지 않는다.

    A kind-rank      서열 가중 w 를 극성대로 더한 S = Σ ±w 를 W = Σ w 로 나누어 (1 + S / W) / 2 로 접는다. 판정은 서열의 한 종류다.
    B beta-binomial  지지 s · 반박 r (판정의 극성도 그대로 센다)을 사전 Beta(1, 1) 에 더한 사후의 평균 (1 + s) / (2 + s + r) 과 분산.
    C judge-mean     판정 증거의 확신도('예'의 확률) 평균. 보정하지 않은 값이다."""
    out: dict[str, tuple[float, int, float | None]] = {}
    ranked = [(BELIEF_KIND_WEIGHT[k], p) for k, p, _ in entries if k in BELIEF_KIND_WEIGHT]
    total = sum(w for w, _ in ranked)
    if total > 0:
        signed = sum(w if p == "+" else -w for w, p in ranked)
        out["kind-rank"] = ((1 + signed / total) / 2, len(ranked), None)
    s = sum(1 for _, p, _ in entries if p == "+")
    r = sum(1 for _, p, _ in entries if p == "-")
    a, b = BELIEF_PRIOR[0] + s, BELIEF_PRIOR[1] + r
    out["beta-binomial"] = (a / (a + b), s + r, a * b / ((a + b) ** 2 * (a + b + 1)))
    conf = [c for k, _, c in entries if k == "agt:judgement" and c is not None]
    if conf:
        out["judge-mean"] = (sum(conf) / len(conf), len(conf), None)
    return out
```
<!-- 인용 끝 -->
