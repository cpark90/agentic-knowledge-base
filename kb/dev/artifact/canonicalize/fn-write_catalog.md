---
id: https://agentic-knowledge-base.dev/id/chunk/8f13de9c-0e9b-48f7-9212-7bbc47a6f349
type: artifact
level: executable
title_ko: 함수 write_catalog (tools/canonicalize.py)
title: function write_catalog in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/639f6e6c-93f1-4f2e-97b5-e3ce99cc31fc, https://agentic-knowledge-base.dev/id/chunk/72c905c8-58fa-4d17-8305-7a26c700de4e, https://agentic-knowledge-base.dev/id/chunk/d8eae456-6327-477b-8cb2-b53024a57d90]
part_of: https://agentic-knowledge-base.dev/id/composite/48c79ecc-7011-4d44-bc3e-be0cc65036b7
---
**함수** — `write_catalog(out, root, modules, imports)` 다. 대응표·모듈 합본·최상위 파일 사본을 `out` 에 쓴다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def write_catalog(out: Path, root: str | None, modules: list[list[str]], imports: list[list[str]]) -> int:
    """대응표·모듈 합본·최상위 파일 사본을 `out` 에 쓴다. 최상위 owl:imports 와 모듈 imports 는 대응표 안이어야 한다."""
    if not root or not modules:
        print("FAIL [canon] --catalog: --root 와 --module 이 하나 이상 필요하다")
        return EXIT_CONFIG
    entries: dict[str, str] = {}
    sources: dict[str, list[str]] = {}
    for spec in modules:
        if len(spec) < 3:
            print(f"FAIL [canon] --module {' '.join(spec)}: <IRI> <이름> <원본 TTL...> 꼴이 아니다")
            return EXIT_CONFIG
        iri, name, files = spec[0], spec[1], spec[2:]
        if "/" in name or name == CATALOG_FILE or name == Path(root).name or name in entries.values() or iri in entries:
            print(f"FAIL [canon] --module {iri} {name}: 합본 이름이나 IRI 가 겹치거나 디렉토리 밖을 가리킨다")
            return EXIT_CONFIG
        entries[iri], sources[iri] = name, files
    extra: dict[str, list[str]] = {}
    for iri, imp in imports:
        extra.setdefault(iri, []).append(imp)
    try:
        rg = Graph()
        rg.parse(root, format="turtle")
        graphs = {iri: module_graph(iri, sources[iri], extra.get(iri, [])) for iri in entries}
    except Exception as e:  # OSError·rdflib 파서 — 판정 불가 입력
        print(f"FAIL [canon] --catalog: 읽거나 파싱할 수 없다 — {e}")
        return EXIT_CONFIG
    wanted = {str(o) for o in rg.objects(None, OWL.imports)} | {i for v in extra.values() for i in v}
    missing = sorted(wanted - set(entries))
    for iri in missing:
        print(f"FAIL [canon] {iri}: owl:imports 가 대응표에 없다 — 그 모듈을 --module 로 넘긴다")
    if missing:
        return EXIT_FAIL
    out.mkdir(parents=True, exist_ok=True)
    for iri, g in graphs.items():
        (out / entries[iri]).write_text(canonical_graph_text(g), encoding="utf-8")
    (out / CATALOG_FILE).write_text(catalog_xml(entries), encoding="utf-8")
    (out / Path(root).name).write_bytes(Path(root).read_bytes())
    return 0
```
<!-- 인용 끝 -->
