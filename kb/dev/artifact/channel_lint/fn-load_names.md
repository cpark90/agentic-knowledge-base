---
id: https://agentic-knowledge-base.dev/id/chunk/d5916f30-3b18-49c6-8f72-8ef1cbcf9bec
type: artifact
level: executable
title_ko: 함수 load_names (tools/channel_lint.py)
title: function load_names in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04fe68bc-58a1-45bd-ac00-78d263cbba81, https://agentic-knowledge-base.dev/id/chunk/f25447a7-4301-4ae4-b0a6-d22f459cd775]
part_of: https://agentic-knowledge-base.dev/id/composite/30c94888-c0b3-4616-8c73-db2b38068fb2
---
**함수** — `load_names(decisions, ontology, graphs)` 다. 식별자 → (꼴, 현재 한글 이름들, 옛 한글 이름들).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_names(decisions: list[str], ontology: list[str], graphs: list[str]) -> dict[str, tuple[str, list[str], list[str]]]:
    """식별자 → (꼴, 현재 한글 이름들, 옛 한글 이름들). 꼴은 slug·agt·id 다.

    결정 slug 의 이름은 결정 기록(복합체)의 `composite.title_ko` 다 — slug 는 결정 기록의 디렉토리 이름이고 결론 하나의
    이름이 아니다. 복합체 선언이 없으면 결론의 `title_ko` 로 갈음한다. 옛 이름은 같은 자리의 `former_title_ko` 다.
    `agt:`·`id:` 는 온톨로지·그래프의 @ko 라벨(NAME_PREDICATES)이고 옛 이름은 `skos:hiddenLabel` @ko 다.
    `id:` 는 경로 없는 이름(`id:<name>`)만 받는다 — 단위 지식·복합체의 uuid IRI 는 백틱 식별자로 쓰이지 않는다.
    """
    names: dict[str, tuple[str, list[str], list[str]]] = {}
    if any(DECISION_RECORD.search(p) for p in decisions):  # parse_chunk 의 수준·상태 어휘 — 등록부와 같은 defs/kb.bzl 이다
        apply_plane_level_state(*load_plane_level_state(gates_bzl_path()))
    for path in decisions:
        m = DECISION_RECORD.search(path)
        if not m:
            continue
        meta, _ = parse_chunk(path)
        comp = meta.get("composite")
        src = comp if isinstance(comp, dict) and comp.get("title_ko") else meta
        names[m.group(1)] = ("slug", [src["title_ko"]], list(src.get(FORMER_TITLE_KEY) or []))
    g = Graph()
    for path in [*ontology, *graphs]:
        g += load_graph(path)
    for slot, preds in ((1, NAME_PREDICATES), (2, (FORMER_PREDICATE,))):
        for s, o in (so for pred in preds for so in g.subject_objects(pred)):
            if not isinstance(s, URIRef) or getattr(o, "language", None) != "ko":
                continue
            for kind, ns in (("agt", AGT), ("id", ID)):
                local = str(s)[len(str(ns)):] if str(s).startswith(str(ns)) else ""
                if local and "/" not in local:
                    ko = names.setdefault(f"{kind}:{local}", (kind, [], []))[slot]
                    if str(o) not in ko:
                        ko.append(str(o))
    return {k: v for k, v in names.items() if v[1]}  # 현재 이름이 없는 식별자(hiddenLabel 만 있는 것)는 풀리지 않는 토큰이다
```
<!-- 인용 끝 -->
