---
id: https://agentic-knowledge-base.dev/id/chunk/a8dde51e-2d80-4281-9dad-fcf5f948abdb
type: artifact
level: executable
title_ko: 함수 emit (tools/space2kg.py)
title: function emit in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/181f6c99-94f8-4b1c-8461-f34fc0d42c58, https://agentic-knowledge-base.dev/id/chunk/9875f781-35a4-413a-beae-89f20bb6ea33]
part_of: https://agentic-knowledge-base.dev/id/composite/2716ece9-44f6-48ff-b2ab-1ad0ea6fa6c0
---
**함수** — `emit(space, enc)` 다. 설계 공간 하나 → (IRI, 블록) 목록 — 공간 개체 · 후보 링크 개체 · 증거 항목.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit(space: dict, enc) -> list[tuple[str, str]]:
    """설계 공간 하나 → (IRI, 블록) 목록 — 공간 개체 · 후보 링크 개체 · 증거 항목."""
    esc, meta = chunk2kg.esc, space["meta"]
    frm, kind = space["var"]
    out, candidate_iris = [], []
    for c in space["candidates"]:
        h = chunk2kg.link_hash(frm, kind, c["to"])
        link = f"{chunk2kg.ID_BASE}link/{h}"
        classes, state = kb_lib.SPACE_STATE_LINK[c["state"]]
        evidences = []
        for i, (ekind, ref) in enumerate(c["support"]):
            evidences.append((f"{chunk2kg.ID_BASE}evidence/{h}-space{i}", ekind, ref, "+"))
        if c["elim"]:
            evidences.append((f"{chunk2kg.ID_BASE}evidence/{h}-eliminated", c["elim"][0], c["elim"][1], "-"))
        stmts = [f"a {classes}", f"agt:linkFrom <{frm}>", f"agt:linkTo <{c['to']}>", f"agt:linkKind agt:{kind}",
                 f'agt:linkState "{state}"']
        if c["when"]:
            stmts.append(f'agt:when "{esc(c["when"])}"')
        if evidences:
            stmts.append("agt:hasEvidence " + " , ".join(f"<{e}>" for e, _, _, _ in evidences))
        out.append((link, render(link, stmts)))
        for iri, ekind, ref, pol in evidences:
            ev = [f"a agt:Evidence", f"agt:evidenceKind agt:{ekind}",
                  (f"agt:evidenceRef <{ref}>" if ref.startswith("http") else f'agt:evidenceRef "{esc(ref)}"'),
                  f'agt:polarity "{pol}"']
            out.append((iri, render(iri, ev)))
        candidate_iris.append((c["to"], link))

    by_to = dict(candidate_iris)
    for a, b in space["preferences"]:
        out.append((by_to[a] + "|pref", render(by_to[a], [f"agt:preferredOver <{by_to[b]}>"])))

    stmts = [f"a {kb_lib.SPACE_TYPE}",
             f'rdfs:label "{esc(meta["title"])}"@en', f'rdfs:label "{esc(meta["title_ko"])}"@ko',
             f"agt:hasLevel agt:{meta['level']}", f"agt:tokenCount {kb_lib.token_count(space['body'], enc)}",
             f'agt:status "{meta["status"]}"', f'agt:contentHash "{meta["_content_hash"]}"',
             f'agt:generatedBy "{esc(meta["generated"]["by"])}"',
             f'prov:generatedAtTime "{meta["generated"]["at"]}"^^xsd:dateTime',
             f'agt:assertionLocation "{esc(space["path"])}"']
    for a in meta.get("assumes", []):
        stmts.append(f"agt:assumes <{a}>")
    for d in meta.get("sources", []):
        res = d.get("resource") if isinstance(d, dict) else d
        if not res:
            raise SpaceError(f"{space['path']}: sources 항목에 resource 가 없다 (OKF v0.2 §5.1)")
        stmts.append(f"prov:wasDerivedFrom <{res}>")
    stmts += [f'agt:spaceStatus "{space["status"]}"', f"agt:variableFrom <{frm}>", f"agt:variableKind agt:{kind}"]
    stmts += [f'agt:compatibilityConstraint "{esc(c)}"' for c in space["constraints"]]
    stmts += [f"agt:hasCandidate <{l}>" for _, l in candidate_iris]
    out.append((meta["id"], render(meta["id"], stmts)))
    return out
```
<!-- 인용 끝 -->
