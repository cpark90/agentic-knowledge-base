---
id: https://agentic-knowledge-base.dev/id/chunk/e7ab69be-0a39-47d8-b2cd-89083d854b3f
type: artifact
level: executable
title_ko: 함수 judge_log_graph (tools/kb_lib.py)
title: function judge_log_graph in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07748717-33f2-409f-8b8d-9c1a2fc37bc4, https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e, https://agentic-knowledge-base.dev/id/chunk/d536eb83-d269-4b4d-a6ed-281a4a2f54c2]
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
---
**함수** — `judge_log_graph(text)` 다. 판정 로그 파일의 글 → 그래프 (agt:JudgementLog 하나와 표의 행마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_log_graph(text: str) -> Graph:
    """판정 로그 파일의 글 → 그래프 (agt:JudgementLog 하나와 표의 행마다 agt:JudgementRow 하나, judge-threshold-ontology).

    판정 표는 `JUDGE_LOG_TABLE_HEADER` 의 열을 읽고(`judge_log_rows`), 미끼 검출 결과는 `JUDGE_LOG_DECOY` 로 시작하는 줄의 나머지다.
    `대상` 칸은 `agt:judgeTarget` 이다 — 쌍 꼴(`parse_pair_target`)이면 앵커와 대상 둘, IRI 하나면 그 하나다. 열이나 줄이
    없으면 그 트리플을 내지 않는다 — 없음의 판정은 shape(`JUDGE_LOG_SHAPES`)가 한다. 저장하지 않는 파생 그래프다.
    """
    from rdflib import BNode, Literal
    from rdflib.namespace import XSD
    m = re.search(r"^id:\s*(\S+)\s*$", text, re.MULTILINE)
    log = URIRef(m.group(1)) if m else BNode()
    g = Graph()
    g.add((log, RDF.type, AGT.JudgementLog))
    for cell in judge_log_rows(text):
        row = BNode()
        g.add((log, AGT.hasJudgementRow, row))
        g.add((row, RDF.type, AGT.JudgementRow))
        g.add((row, AGT.judgeId, Literal(cell["판정자 식별자"])))
        g.add((row, AGT.judgeAgreement, Literal(cell["일치"])))
        g.add((row, AGT.judgeRoute, Literal(cell["처리"])))
        pair = parse_pair_target(cell["대상"])
        for t in (pair[:2] if pair else ([cell["대상"]] if cell["대상"].startswith(str(ID)) else [])):
            g.add((row, AGT.judgeTarget, URIRef(t)))
        if JUDGE_CONFIDENCE.match(cell["확신도"]):
            g.add((row, AGT.judgeConfidence, Literal(cell["확신도"], datatype=XSD.decimal)))
    for line in chunk_body(text).split("\n"):
        if line.startswith(JUDGE_LOG_DECOY):
            g.add((log, AGT.decoyResult, Literal(line[len(JUDGE_LOG_DECOY):].strip())))
    return g
```
<!-- 인용 끝 -->
