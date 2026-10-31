---
id: https://agentic-knowledge-base.dev/id/chunk/69ceb5b2-0e90-45f9-983b-c8a56c9fda09
type: artifact
level: executable
title_ko: 함수 pair_decoy_summary (tools/judge.py)
title: function pair_decoy_summary in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `pair_decoy_summary(tally)` 다. 쌍 모드 판정 로그의 미끼 검출 결과 줄의 값 — 음성 미끼에 no, 양성 미끼에 yes 가 검출이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_decoy_summary(tally: dict) -> str:
    """쌍 모드 판정 로그의 미끼 검출 결과 줄의 값 — 음성 미끼에 no, 양성 미끼에 yes 가 검출이다."""
    (nh, ns, nt), (ph, ps, pt) = tally["neg"], tally["pos"]
    if not (nt or pt):
        return f"{kb_lib.EMPTY_NOT_APPLICABLE} — 쌍 판정지에 미끼가 없다(`--decoys-neg 0 --decoys-pos 0`)"
    return (f"음성 미끼 {nt}건 중 응답 대조 {ns}건 · 검출(no) {nh}건 · 검출률 {kb_lib.pct(nh, ns)} · "
            f"양성 미끼 {pt}건 중 응답 대조 {ps}건 · 검출(yes) {ph}건 · 검출률 {kb_lib.pct(ph, ps)}")
```
<!-- 인용 끝 -->
