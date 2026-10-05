---
id: https://agentic-knowledge-base.dev/id/chunk/1f886c5e-4c41-43ff-9555-867c1f4f13d4
type: artifact
level: executable
title_ko: 함수 space_rows (tools/open_questions.py)
title: function space_rows in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/104f7d3c-d114-46c9-aab7-b44761117813, https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55]
part_of: https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0
---
**함수** — `space_rows(g)` 다. 설계 공간 그래프 → 공간마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def space_rows(g: Graph) -> list[dict]:
    """설계 공간 그래프 → 공간마다 제목·status·변수·후보 state 별 수·본문 위치."""
    rows = []
    for s in set(g.subjects(RDF.type, AGT.Space)):
        counts = dict.fromkeys(kb_lib.SPACE_STATES, 0)
        for link in g.objects(s, AGT.hasCandidate):
            st = STATE_OF_LINK.get(str(next(g.objects(link, AGT.linkState), "")), "")
            if st:
                counts[st] += 1
        frm = next(g.objects(s, AGT.variableFrom), None)
        rows.append({
            "iri": str(s), "ko": kb_lib.label_of(g, s, "ko"),
            "status": str(next(g.objects(s, AGT.spaceStatus), "")),
            "loc": str(next(g.objects(s, AGT.assertionLocation), "")),
            "from_ko": kb_lib.label_of(g, frm, "ko") if frm is not None else "",
            "from_iri": kb_lib.compact_iri(str(frm)) if frm is not None else "",
            "kind": str(next(g.objects(s, AGT.variableKind), "")).split("/")[-1],
            "counts": counts, "slots": [],
        })
    rows.sort(key=lambda r: (r["status"] != "open", r["loc"]))
    return rows
```
<!-- 인용 끝 -->
