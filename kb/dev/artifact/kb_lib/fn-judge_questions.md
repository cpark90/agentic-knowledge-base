---
id: https://agentic-knowledge-base.dev/id/chunk/00a89f1d-2167-43fb-9e95-4a70385078ae
type: artifact
level: executable
title_ko: 함수 judge_questions (tools/kb_lib.py)
title: function judge_questions in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
---
**함수** — `judge_questions(g)` 다. 등록된 판정 질문 — {지역명: {iri, label, label_en, text, form, scale, options}}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_questions(g: Graph) -> dict:
    """등록된 판정 질문 — {지역명: {iri, label, label_en, text, form, scale, options}}. `judge_load_profile`과 짝이다."""
    out = {}
    for q in g.subjects(RDF.type, AGT.JudgeQuestion):
        if not isinstance(q, URIRef):
            continue
        form = str(next(g.objects(q, AGT.questionForm), ""))
        out[str(q).rsplit("/", 1)[-1]] = {
            "iri": str(q), "form": form,
            "label": label_of(g, q) or str(q),
            "label_en": label_of(g, q, "en") or str(q).rsplit("/", 1)[-1],
            "text": str(next(g.objects(q, SKOS.definition), "")),
            "scale": sorted(str(s) for s in g.objects(q, AGT.scaleSituation)),
            "options": sorted(str(o) for o in g.objects(q, AGT.choiceOption)),
        }
    return out
```
<!-- 인용 끝 -->
