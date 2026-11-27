---
id: https://agentic-knowledge-base.dev/id/chunk/06ac1ac0-5466-4c53-9241-85ddecb10af6
type: artifact
level: executable
title_ko: 함수 bin_rows (tools/belief_calibration.py)
title: function bin_rows in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2, https://agentic-knowledge-base.dev/id/chunk/f1ef7fed-44fb-45ef-bc75-8f33101fc8cb]
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `bin_rows(r)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def bin_rows(r: dict) -> list[str]:
    out = ["| 구간 | n_k | 평균 예측 p̄_k | 관측 빈도 ō_k | 성공 수 | 이항 구간 0.95 [lo/n_k, hi/n_k] | 안에 드는가 |",
           "|---|---|---|---|---|---|---|"]
    for b in r["bins"]:
        if not b["n"]:
            out.append(f"| {b['name']} | 0 | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | 표본 없음 |")
            continue
        out.append(f"| {b['name']} | {b['n']} | {kb_lib.num(float(b['pbar']))} | {kb_lib.num(b['hits'] / b['n'])} | {b['hits']}/{b['n']} | "
                   f"[{kb_lib.num(b['lo'] / b['n'])}, {kb_lib.num(b['hi'] / b['n'])}] (성공 수 {b['lo']}~{b['hi']}) | {truth(b['inside'])} |")
    return out + [""]
```
<!-- 인용 끝 -->
