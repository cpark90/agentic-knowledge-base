---
id: https://agentic-knowledge-base.dev/id/chunk/9bde304e-d5e3-48ae-ac25-19480f2cbc59
type: artifact
level: executable
title_ko: 함수 render_composition_section (tools/consistency.py)
title: function render_composition_section in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2b38088c-7807-429a-a6df-e08e9a052e3a]
part_of: https://agentic-knowledge-base.dev/id/composite/b4b758f5-4191-4b55-9a49-25639323a475
---
**함수** — `render_composition_section(comp, limit)` 다. 규칙마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_composition_section(comp, limit=30):
    """규칙마다 건수가 많은 단위 지식부터 사례(파일, 줄, 표현)를 항목마다 셋까지 낸다 — 몰린 항목을 먼저 고치게 한다."""
    lines = ["## ⑫ 문장 구성 — 결정 p0-sentence-composition 의 규칙 3, 4, 5, 6 을 정규식으로 센 대리 (보고; 판정은 리뷰가 한다)", ""]
    for key, name in COMPOSITION_RULES:
        hits = comp[key]
        per = defaultdict(int)
        for it, _, _ in hits:
            per[it["path"]] += 1
        hits = sorted(hits, key=lambda h: (-per[h[0]["path"]], h[0]["path"], h[1]))
        seen: dict[str, int] = defaultdict(int)
        shown = []
        for h in hits:  # 한 항목이 목록을 다 차지하지 않게 항목마다 사례를 셋까지 낸다
            seen[h[0]["path"]] += 1
            if seen[h[0]["path"]] <= 3:
                shown.append(h)
        lines += [f"### {name} — {len(hits)}건 / 단위 지식 {len(per)}개", ""]
        lines += listing(shown, limit, lambda h: f"- `{h[2].replace('`', chr(39))}`: `{h[0]['path']}:{h[1]}` (이 항목 {per[h[0]['path']]}건)")
        lines.append("")
    return lines
```
<!-- 인용 끝 -->
