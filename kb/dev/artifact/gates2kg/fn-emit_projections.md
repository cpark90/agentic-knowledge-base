---
id: https://agentic-knowledge-base.dev/id/chunk/7c84bccd-bce1-441d-ae3c-b5f960ab1dc8
type: artifact
level: executable
title_ko: 함수 emit_projections (tools/gates2kg.py)
title: function emit_projections in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b8f959c8-3cb6-443b-828c-c3952f8b8020, https://agentic-knowledge-base.dev/id/chunk/f15f1ad5-6a97-49e0-a1b6-d7cc84dd3b8e]
part_of: https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1
---
**함수** — `emit_projections(views, skills, modules, where)` 다. 뷰 표·skill 표 → 투영 TTL.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit_projections(views: dict[str, str], skills: tuple, modules: dict[str, str], where: str) -> str:
    """뷰 표·skill 표 → 투영 TTL. 원본 도구의 `module` 청크가 없으면 생성 시점에 거부한다."""
    errors = []
    blocks = []
    rows = [("View", kb_lib.VIEW_ID_PREFIX + view_slug(label), label, f"생성 뷰 {label}", tool,
             f"생성 뷰 {label} — 생성 도구 {tool} 의 출력이다")
            for label, tool in sorted(views.items())]
    for spec in skills:
        name = spec["tool"].replace("_", "-")
        rows.append(("Skill", kb_lib.SKILL_ID_PREFIX + name, name, f"skill {name}", spec["tool"], spec["when"]))
    for kind, slug, en, ko, tool, desc in rows:
        iri = modules.get(tool)
        if not iri:
            errors.append(f"{where}: {kind} {en!r} 의 원본 도구 {tool!r} 의 module 청크를 찾을 수 없다 — "
                          f"tools/{tool}.chunks.yml 의 `ids: module:` 가 prov:wasDerivedFrom 의 대상이다")
            continue
        props = [
            f"a agt:{kind}",
            f'rdfs:label "{escape(en)}"@en , "{escape(ko)}"@ko',
            f'skos:definition "{escape(desc)}"@ko',
            f"prov:wasDerivedFrom <{iri}>",
        ]
        blocks.append(" ;\n    ".join([f"id:{slug} {props[0]}"] + props[1:]) + " .")
    if errors:
        print("\n".join(f"FAIL [{TAG}] {e}" for e in errors), file=sys.stderr)
        raise SystemExit(EXIT_FAIL)
    return PROJECTION_HEADER + "\n" + "\n\n".join(blocks) + "\n"
```
<!-- 인용 끝 -->
