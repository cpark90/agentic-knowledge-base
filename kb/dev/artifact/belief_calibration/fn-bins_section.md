---
id: https://agentic-knowledge-base.dev/id/chunk/a9090c58-4abc-453a-a64f-e0b2991ca4c8
type: artifact
level: executable
title_ko: 함수 bins_section (tools/belief_calibration.py)
title: function bins_section in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/06ac1ac0-5466-4c53-9241-85ddecb10af6]
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `bins_section(title, results, note)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def bins_section(title: str, results: dict, note: str) -> list[str]:
    out = [f"## {title}", "", note, ""]
    for slug, letter in RULE_ORDER:
        r = results[slug]
        out += [f"### {letter} `{slug}`", ""]
        out += bin_rows(r) if r["n"] else ["값이 있는 항목이 없다.", ""]
    return out
```
<!-- 인용 끝 -->
