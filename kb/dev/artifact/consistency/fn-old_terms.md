---
id: https://agentic-knowledge-base.dev/id/chunk/d145a64e-ff57-458c-b3ef-4853ef43366a
type: artifact
level: executable
title_ko: 함수 old_terms (tools/consistency.py)
title: function old_terms in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/38dd33c9-2317-4c0a-a596-5bb97eecca1b
---
**함수** — `old_terms(glossary)` 다. glossary 표의 셋째 열(옛 표기)에서 **tier 1** 용어를 뽑는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def old_terms(glossary: str) -> tuple[list, bool]:
    """glossary 표의 셋째 열(옛 표기)에서 **tier 1** 용어를 뽑는다 — '·'로 나뉜 항목 각각 → ([(옛, 표준)], tier 열 유무).

    tier 는 헤더에서 `tier` 열을 찾아 읽는다(값 1·2·3·—). 열이 없으면 전부 1 로 본다. 표준 용어이기도 한 옛 표기
    ("검증"·"프로파일")의 예외는 코드에 없다 — 그 자리는 tier 3 이 맡는다 (agrtls-practices-review-2026-09-12 B).
    """
    rows, tier_col = [], None
    for line in Path(glossary).read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0].startswith("표준 용어"):
            tier_col = next((i for i, c in enumerate(cells) if c.strip("`").lower() == "tier"), None)
            continue
        if len(cells) < 4 or all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append(cells)
    out = []
    for r in rows:
        tier = r[tier_col].strip("`") if tier_col is not None and tier_col < len(r) else "1"
        if tier != "1":
            continue
        for t in re.split(r"\s*·\s*", r[2]):
            t = t.strip()
            if t and t != "—" and len(t) >= 2:
                out.append((t, r[0]))
    return out, tier_col is not None
```
<!-- 인용 끝 -->
