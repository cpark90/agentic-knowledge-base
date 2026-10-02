---
id: https://agentic-knowledge-base.dev/id/chunk/2d509ef2-a992-4376-8863-e6f4bd1edce1
type: artifact
level: executable
title_ko: 함수 group_composites (tools/gen_build.py)
title: function group_composites in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04bfcfb9-d96b-42ec-9555-a58bd09f1551, https://agentic-knowledge-base.dev/id/chunk/6b2fd7de-ac08-40ec-a4c0-7976d20b1f34, https://agentic-knowledge-base.dev/id/chunk/816a1348-352c-462d-bbb0-ad267befb0d9]
part_of: https://agentic-knowledge-base.dev/id/composite/569c6e75-e264-4981-bf0b-bba156b541c8
---
**함수** — `group_composites(items, iri_to_label)` 다. 같은 패키지에서 `composite.id` 로 묶인 청크들 → 복합체 항목 하나 (kb_composite).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def group_composites(items, iri_to_label):
    """같은 패키지에서 `composite.id` 로 묶인 청크들 → 복합체 항목 하나 (kb_composite). 중첩 복합체는 뿌리 하나로 모은다.

    묶음의 판별 기준은 **같은 패키지 + 같은 뿌리 복합체**다. 디렉토리가 기준인 결정(kb_decision)과 달리 일반 복합체는
    평평한 패키지 하나에 여러 개 설 수 있어 디렉토리로는 가를 수 없고, `composite.id` 는 이미 선언이 한 번뿐임을 chunk2kg 가
    강제하는 값이다. 패키지가 기준의 한 축인 것은 Bazel 타깃의 `srcs` 가 자기 패키지 안에만 있을 수 있기 때문이다 —
    묶음은 액션의 입력 집합이고 입력 집합은 패키지를 넘지 못한다.

    복합체는 청크뿐 아니라 **다른 복합체**를 부분으로 갖는다 (p4-composite-as-part-of). 선언 청크의 `composite.part_of` 가
    그 자리이고, 중첩된 복합체 전부가 **뿌리 복합체 타깃 하나**가 된다 — chunk2kg 가 part_of 대상을 같은 실행의 입력
    집합에서 찾으므로 뿌리부터 잎까지 한 액션이 받아야 한다. 부분 상한 9(4.5절)를 넘는 파일을 담는 유일한 형태다
    (p7-code-links-on-file-composite: 파일 → 절 → 함수).

    부분 청크의 개별 `kb_chunk` 타깃은 사라지고 뿌리 복합체 타깃 하나가 그 파일 전부를 갖는다 (결정과 같은 형식). 링크는
    묶음 안 청크들의 것을 그 타깃으로 올린다. 타깃 이름은 **뿌리 복합체**를 선언한 청크의 파일 이름이다.
    """
    decl, parent, members = {}, {}, {}
    for lab, it in items.items():
        if it["kind"] != "chunk":
            continue
        comp = it["meta"].get("composite") or {}
        if comp.get("id"):
            if comp["id"] in decl:  # chunk2kg 는 한 묶음 안의 중복만 본다 — 패키지를 가로지르는 중복은 여기서 거부한다
                raise GenBuildError(f"{it['pkg']}/{it['src']}: 복합체 {comp['id']} 가 {items[decl[comp['id']]]['pkg']}/"
                                    f"{items[decl[comp['id']]]['src']} 와 중복 선언됐다 — 선언은 복합체마다 한 번이다 (4.5절)")
            decl[comp["id"]] = lab
            if comp.get(PART_OF_KEY):
                parent[comp["id"]] = comp[PART_OF_KEY]
        if it["meta"].get("part_of"):
            members.setdefault(it["meta"]["part_of"], []).append(lab)
    for comp_iri, labs in sorted(members.items()):
        if comp_iri not in decl:
            raise GenBuildError(f"{items[sorted(labs)[0]]['pkg']}/{items[sorted(labs)[0]]['src']}: part_of 대상 복합체 {comp_iri} 를 "
                                f"선언한 청크(composite:)가 없다 — 선언은 부분 중 하나의 frontmatter 에 둔다 (4.5절)")
    children = {}
    for child, up in sorted(parent.items()):
        if up not in decl:
            raise GenBuildError(f"{items[decl[child]]['pkg']}/{items[decl[child]]['src']}: composite.{PART_OF_KEY} 대상 복합체 {up} 를 "
                                f"선언한 청크가 없다 — 중첩 복합체는 뿌리부터 잎까지 같은 패키지에 있어야 한다 (p4-composite-as-part-of)")
        children.setdefault(up, []).append(child)
    for comp_iri in sorted(decl):  # 사슬 순환 — 반대칭 공리(4.5절 비순환)의 생성 시점 대응
        seen_chain, cur = {comp_iri}, parent.get(comp_iri)
        while cur is not None:
            if cur in seen_chain:
                raise GenBuildError(f"{items[decl[comp_iri]]['pkg']}/{items[decl[comp_iri]]['src']}: composite.{PART_OF_KEY} 사슬이 "
                                    f"순환한다 — {comp_iri} 에서 시작해 {cur} 로 돌아온다 (4.5절 비순환)")
            seen_chain.add(cur)
            cur = parent.get(cur)
    for root in sorted(c for c in decl if c not in parent):
        tree = _composite_tree(root, children)
        dlab = decl[root]
        pkg = items[dlab]["pkg"]
        labs = sorted({decl[c] for c in tree} | {l for c in tree for l in members.get(c, [])})
        direct = {c: _check_bundle(c, decl[c], labs, items, pkg, members.get(c, []), children.get(c, []), decl) for c in tree}
        comp = {"kind": "composite", "pkg": pkg, "comp_iri": root,
                "ordered": (items[dlab]["meta"].get("composite") or {}).get(ORDERED_KEY) or [],
                "srcs": [items[l]["src"] for l in labs], "metas": [items[l]["meta"] for l in labs],
                "part_iris": direct[root], "status": items[dlab]["meta"]["status"],
                "plane": items[labs[0]]["meta"]["type"], "level": items[labs[0]]["meta"]["level"]}
        for l in labs:  # 부분의 개별 청크 타깃은 사라진다 — 뿌리 복합체 타깃 하나가 그 파일 전부를 갖는다
            iri_to_label[items[l]["meta"]["id"]] = dlab
            del items[l]
        for c in tree:
            iri_to_label[c] = dlab
        items[dlab] = comp  # 타깃 이름 = 뿌리 선언 청크의 파일 이름이라 라벨이 바뀌지 않는다
    return items, iri_to_label
```
<!-- 인용 끝 -->
