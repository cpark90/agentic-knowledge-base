---
id: https://agentic-knowledge-base.dev/id/chunk/cca92813-a1e0-4006-9cf9-8775d4b68641
type: artifact
level: executable
title_ko: 함수 render_table (tools/gen_norms.py)
title: function render_table in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:27:34Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/02b29145-5996-4360-8974-d74d70cd6de4, https://agentic-knowledge-base.dev/id/chunk/082fbbdd-904c-4476-b773-8ebe8a85418e, https://agentic-knowledge-base.dev/id/chunk/516aa2b9-e91a-4519-9bdd-e579b651a443]
part_of: https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4
---
**함수** — `render_table(s, conventions, out)` 다. 표 묶음 — 행은 항목 하나, 칸은 줄의 `a | b | …` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_table(s: dict, conventions: dict, out: str) -> list[str]:
    """표 묶음 — 행은 항목 하나, 칸은 줄의 `a | b | …` 다. 링크 열이 있으면 그 칸이 결정 링크(` · ` 로 이음)이고, 없으면 표 바로
    앞에 `원본:` 한 줄(행의 주 결정과 `+ slug2` 의 둘째 결정을 구분 없이 처음 나온 순서로 중복 없이)을 낸다."""
    cols = s[NORM_COLUMNS_KEY]
    linked = NORM_LINK_COLUMN_KEY in s
    rows, mains = [], []
    for it in s.get("_norm_items") or []:
        slug, k = it["ref"]
        cells = [rebase_links(c, conventions[slug]["path"], out) for c in table_cells(conventions[slug]["lines"][k - 1][1])]
        if linked:
            cells.append(" · ".join(decision_link(x, out) for x in [slug] + it["links"]))
        rows.append("| " + " | ".join(cells) + " |")
        for x in [slug] + it["links"]:  # 링크 열이 없으면 원본 줄이 행의 결정 링크를 내는 유일한 자리다 — 둘째 결정도 싣는다
            if x not in mains:
                mains.append(x)
    lines = [] if linked else ["원본: " + " · ".join(decision_link(x, out) for x in mains) + ".", ""]
    return lines + ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)] + rows
```
<!-- 인용 끝 -->
