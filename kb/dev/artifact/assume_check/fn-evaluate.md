---
id: https://agentic-knowledge-base.dev/id/chunk/304744ba-30b6-43f2-8aee-d9532aa66c13
type: artifact
level: executable
title_ko: 함수 evaluate (tools/assume_check.py)
title: function evaluate in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/3d72bcbf-9fce-4ada-9c3b-fff4759fa5fd, https://agentic-knowledge-base.dev/id/chunk/58418c78-77dc-491d-bce6-60d85217ee30, https://agentic-knowledge-base.dev/id/chunk/b573f0b1-8e42-4b97-bec6-397c246cd5b9]
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `evaluate(g, cond_rows)` 다. 가정마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def evaluate(g: Graph, cond_rows: list[dict]) -> list[dict]:
    """가정마다 상태·등급·유형·참조 조건 — 판정식은 참조 조건 판정의 연언이다."""
    by_iri = {r["iri"]: r for r in cond_rows}
    out = []
    for asm in sorted(g.subjects(RDF.type, AGT.Assumption), key=str):
        conds = sorted((str(c) for c in g.objects(asm, AGT.refersTo)), key=str)
        rows = [by_iri.get(c) for c in conds]
        states = [r["state"] if r else "unverified" for r in rows]  # ODD 문서에 없는 조건은 판정 불가
        status = "invalidated" if "out" in states else "valid" if states and all(s == "in" for s in states) else "unverified"
        cmds = [bool(r and r["cmd"]) for r in rows]
        kind = "실행 검사" if cmds and all(cmds) else "사람 확인" if not any(cmds) else "실행 검사·사람 확인"
        out.append({"iri": asm, "label": label_of(g, asm), "conds": conds, "states": states, "status": status, "kind": kind,
                    "grade": worst_grade([r["grade"] if r else "?" for r in rows]),
                    "expr": " ∧ ".join(f"in({local(c)})" for c in conds) or "(참조 조건 없음)"})
    return out
```
<!-- 인용 끝 -->
