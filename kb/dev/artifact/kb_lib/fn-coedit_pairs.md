---
id: https://agentic-knowledge-base.dev/id/chunk/12124054-d49f-44e2-be10-6fbdb102b578
type: artifact
level: executable
title_ko: 함수 coedit_pairs (tools/kb_lib.py)
title: function coedit_pairs in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e, https://agentic-knowledge-base.dev/id/chunk/f5c8131e-c94d-4c0b-82fe-9e7ad9d36c69]
part_of: https://agentic-knowledge-base.dev/id/composite/66e7a8ca-2ebd-4dc8-8cc0-23fa46a065fb
---
**함수** — `coedit_pairs(paths, known)` 다. 동시 편집 관측 → (읽은 관측의 경로, 쌍 집합 {frozenset((IRI, IRI))}, 풀지 못한 항목 수).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def coedit_pairs(paths, known) -> tuple[str | None, set, int]:
    """동시 편집 관측 → (읽은 관측의 경로, 쌍 집합 {frozenset((IRI, IRI))}, 풀지 못한 항목 수).

    `paths` 가운데 파일명이 `COEDIT_PREFIX` 로 시작하는 것의 가장 늦은 것 하나만 읽는다 — 관측은 추가 전용이고 늦은 것이 앞선
    것을 대신한다. `known` 은 지금 트리의 단위 지식 IRI 들이고, 짧은 꼴과 국소 이름 전체를 IRI 로 푸는 데 쓴다.
    관측이 없으면 (None, 빈 집합, 0) 이다.
    """
    obs = sorted((p for p in paths if Path(p).name.startswith(COEDIT_PREFIX) and p.endswith(".md")), key=lambda p: Path(p).name)
    if not obs:
        return None, set(), 0
    table: dict[str, set] = {}
    for iri in known:
        for form in {coedit_short(iri), iri[len(str(ID)):] if iri.startswith(str(ID)) else iri}:
            table.setdefault(form, set()).add(iri)
    pairs, unresolved, inside = set(), 0, False
    for ln in chunk_body(Path(obs[-1]).read_text(encoding="utf-8")).splitlines():
        s = ln.strip()
        if not inside:
            inside = s == COEDIT_TABLE_HEADER
            continue
        if not s.startswith("|"):
            break
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 5 or set(cells[0]) <= {"-"}:
            continue
        items = []
        for form in _COEDIT_ITEM.findall(cells[4]):
            hit = table.get(form, set())
            if len(hit) == 1:
                items.append(next(iter(hit)))
            else:
                unresolved += 1
        items = sorted(set(items))
        pairs.update(frozenset((a, b)) for i, a in enumerate(items) for b in items[i + 1:])
    return obs[-1], pairs, unresolved
```
<!-- 인용 끝 -->
