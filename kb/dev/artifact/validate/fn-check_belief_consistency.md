---
id: https://agentic-knowledge-base.dev/id/chunk/6f429584-5f62-4039-9848-4d26e16a22ac
type: artifact
level: executable
title_ko: 함수 check_belief_consistency (tools/validate.py)
title: function check_belief_consistency in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2a4b8195-f60c-4855-abcc-199681ca3549, https://agentic-knowledge-base.dev/id/chunk/b526b631-d6a6-4bd8-9e43-b754fabfae9b]
part_of: https://agentic-knowledge-base.dev/id/composite/650f6771-cd62-485d-85c3-a08e4df10c41
---
**함수** — `check_belief_consistency(merged, chunk_files)` 다. 믿음 정도의 일관성 (게이트 belief-consistency) — 두 조건을 코드 단위 지식(파이썬 정의·SPARQL 질의)에서 본다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_belief_consistency(merged: Graph, chunk_files: list[str]) -> list[str]:
    """믿음 정도의 일관성 (게이트 belief-consistency) — 두 조건을 코드 단위 지식(파이썬 정의·SPARQL 질의)에서 본다.

    (i) 상태 전이 규칙은 믿음 정도를 읽지 않는다(Q90-a). 상태 전이 규칙은 상태 전이를 정한 결정(_TRANSITION_DECISIONS)을 자기
        또는 같은 디렉토리의 파일 단위 지식(module.md)의 refines 로 구현한다고 선언한 코드 가운데 상태의 어휘(_STATE_WORDS)를 쓰는
        단위다. 그 단위와 그것이 uses 로 부르는 정의들(전이 폐포)이 믿음 정도의 어휘(_BELIEF_WORDS)를 쓰면 FAIL 이다.
    (ii) 닫힌 계산 규칙이 없는 동안 병기 값은 선호의 동률 깨기에 쓰이지 않는다(Q137-a). 동률 깨기 코드는 선호의 부분순서를 정한
        결정(_TIE_BREAK_DECISIONS)을 refines 로 구현한다고 선언했거나 선호의 어휘(agt:preferredOver)를 쓰는 단위다. 닫힌 계산 규칙은
        설계 공간의 후보 링크 가운데 상태가 confirmed 이고 출발점이 믿음 정도 노드의 계산 규칙인 것이다(_CLOSED_RULES). 그것이
        그래프에 없으면, 동률 깨기 단위와 그 uses 폐포가 믿음 정도의 어휘를 쓸 때 FAIL 이다.
    단위의 판정은 이름 수준이다 — 주석과 docstring 은 보지 않고, 값의 흐름을 따라가지 않는다."""
    gate = kb_lib.BELIEF_CONSISTENCY_GATE
    units: dict[str, tuple[str, dict, set[str]]] = {}   # 단위 IRI → (경로, frontmatter, 이름들)
    module_refines: dict[str, set[str]] = {}            # 디렉토리 → 파일 단위 지식의 refines
    for path in chunk_files:
        if not path.endswith(".md"):
            continue
        try:
            meta, lang, code = _code_unit(path)
        except (OSError, ValueError):
            continue   # 읽을 수 없는 단위 지식은 chunk 게이트의 몫이다
        if meta.get("type") != "artifact":
            continue
        if Path(path).name == "module.md":
            module_refines[str(Path(path).parent)] = set(meta.get("refines") or [])
        if lang and isinstance(meta.get("id"), str):
            units[meta["id"]] = (path, meta, _code_words(lang, code))

    def declared(iri: str) -> set[str]:
        path, meta, _ = units[iri]
        return set(meta.get("refines") or []) | module_refines.get(str(Path(path).parent), set())

    def closure(iri: str) -> list[str]:
        seen, todo = [iri], [iri]
        while todo:
            for nxt in units[todo.pop()][1].get("uses") or []:
                if nxt in units and nxt not in seen:
                    seen.append(nxt)
                    todo.append(nxt)
        return seen

    def readers(iri: str) -> list[tuple[str, list[str]]]:
        return [(u, sorted(w for w in units[u][2] if _BELIEF_WORDS.search(w))) for u in closure(iri)
                if any(_BELIEF_WORDS.search(w) for w in units[u][2])]

    errors: list[str] = []
    closed = {str(r[0]) for r in merged.query(_CLOSED_RULES)} if len(merged) else set()
    for iri in sorted(units):
        path, _, words = units[iri]
        if declared(iri) & set(_TRANSITION_DECISIONS) and any(_STATE_WORDS.match(w) for w in words):
            for u, found in readers(iri):
                via = "" if u == iri else f" — uses 로 부르는 {units[u][0]} 에서"
                errors.append(f"[{gate}] {path}: 상태 전이 규칙이 믿음 정도를 읽는다{via} ({', '.join(found)}) — "
                              "상태 전이는 증거 기록만 읽는다 (조건 i, p9-evidence-ledger-with-belief, Q90-a)")
        tie_break = declared(iri) & set(_TIE_BREAK_DECISIONS) or any(_PREFERENCE_WORDS.match(w) for w in words)
        if tie_break and not closed:
            for u, found in readers(iri):
                via = "" if u == iri else f" — uses 로 부르는 {units[u][0]} 에서"
                errors.append(f"[{gate}] {path}: 닫힌 계산 규칙이 없는데 선호의 동률 깨기가 믿음 정도를 읽는다{via} ({', '.join(found)}) — "
                              "설계 공간 degree-of-belief-space 에서 규칙이 닫히기 전에는 병기 값만 둔다 (조건 ii, p9-preference-partial-order, Q137-a)")
    return errors
```
<!-- 인용 끝 -->
