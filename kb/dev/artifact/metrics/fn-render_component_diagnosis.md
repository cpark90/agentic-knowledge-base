---
id: https://agentic-knowledge-base.dev/id/chunk/05160394-59e0-426d-a8c1-2421857f4e21
type: artifact
level: executable
title_ko: 함수 render_component_diagnosis (tools/metrics.py)
title: function render_component_diagnosis in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/104f7d3c-d114-46c9-aab7-b44761117813]
part_of: https://agentic-knowledge-base.dev/id/composite/a5749cfe-3647-4164-906e-1d7d739ba5ea
---
**함수** — `render_component_diagnosis(g, plane, outside)` 다. 주 성분 밖의 청크 목록 — 성분마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_component_diagnosis(g, plane, outside):
    """주 성분 밖의 청크 목록 — 성분마다 라벨·plane·경로다. 수만으로는 무엇이 떨어졌는지 알 수 없다."""
    o = ["", "## 주 성분 밖 청크 (연결 성분 진단)", ""]
    if not outside:
        o.append("- 없음 — 저작된 지식이 한 덩어리다 (연결 성분 1)")
        return o
    o += [f"- 주 성분 밖 성분 **{len(outside)}**개 · 청크 **{sum(len(m) for m in outside)}**건 — 링크·복합체·"
          "`prov:specializationOf` 가 주 성분에 닿지 않는 덩어리다. 성분 번호는 크기 내림차순(동수는 작은 IRI)이다", "",
          "| 성분 (청크 수) | 라벨 | plane | 경로 |", "|---|---|---|---|"]
    for i, members in enumerate(outside, 1):
        for c in sorted(members, key=str):
            loc = str(next(g.objects(c, AGT.assertionLocation), "")) or kb_lib.NONE_MARK
            lab = kb_lib.label_of(g, c).replace("|", "\\|")  # 표의 열 수를 지킨다 (G10)
            o.append(f"| {i} ({len(members)}) | {lab} | `{plane.get(c, kb_lib.NONE_MARK)}` | `{loc}` |")
    return o
```
<!-- 인용 끝 -->
