---
id: https://agentic-knowledge-base.dev/id/chunk/221ff1dd-1b9e-4518-831b-2c8e960001ac
type: artifact
level: executable
title_ko: 함수 canonical_text (tools/canonicalize.py)
title: function canonical_text in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
part_of: https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389
---
**함수** — `canonical_text(path)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def canonical_text(path: Path) -> str:
    g = Graph()
    g.parse(str(path), format="turtle")
    cg = to_canonical_graph(g)

    # 사용된 네임스페이스만 @prefix 로 선언 — 리터럴 datatype 도 포함해야 한다
    used = []
    for triple in cg:
        for t in triple:
            if isinstance(t, URIRef):
                used.append(str(t))
            elif isinstance(t, Literal) and t.datatype:
                used.append(str(t.datatype))
    used_s = "".join(used)
    prefixes = {p: ns for p, ns in STANDARD_PREFIXES.items() if ns in used_s}

    out = [f"@prefix {p}: <{ns}> ." for p, ns in sorted(prefixes.items())]
    out.append("")

    by_subject: dict[str, list] = {}
    for s, p, o in cg:
        by_subject.setdefault(_term(s, prefixes), []).append((p, o))

    rdf_type = _term(RDF.type, prefixes)
    for skey in sorted(by_subject):
        pairs = by_subject[skey]
        rendered = sorted(
            ((_term(p, prefixes), _term(o, prefixes)) for p, o in pairs),
            key=lambda po: ((po[0] != rdf_type and po[0] != "a"), po[0], po[1]),
        )
        lines = [skey]
        for i, (pk, ok) in enumerate(rendered):
            pk_out = "a" if pk == rdf_type else pk
            sep = " ." if i == len(rendered) - 1 else " ;"
            lines.append(f"    {pk_out} {ok}{sep}")
        out.append("\n".join(lines))
        out.append("")

    return "\n".join(out).rstrip() + "\n"
```
<!-- 인용 끝 -->
