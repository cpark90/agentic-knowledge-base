---
id: https://agentic-knowledge-base.dev/id/chunk/1b092132-a9fd-4db3-8feb-374efcc07e19
type: artifact
level: executable
title_ko: 함수 load_doc (tools/gen_norms.py)
title: function load_doc in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/49271822-40b4-4cdd-9e5c-c787b7bd458a, https://agentic-knowledge-base.dev/id/chunk/6c4aaa8d-3d57-47ff-b67f-856e48d22fb0, https://agentic-knowledge-base.dev/id/chunk/e30fe78f-85fa-447c-8ec3-df25166cee41, https://agentic-knowledge-base.dev/id/chunk/eb4346c1-beed-427d-8e9d-767bc87f2e0b]
part_of: https://agentic-knowledge-base.dev/id/composite/4467fb1d-c722-4b87-a22b-5f679ceceee0
---
**함수** — `load_doc(root, stem)` 다. `kb/dev/norm/<stem>/` → {head: 메타, sections: [메타…], files: [경로…]} — 선언 순서대로.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_doc(root: Path, stem: str) -> dict:
    """`kb/dev/norm/<stem>/` → {head: 메타, sections: [메타…], files: [경로…]} — 선언 순서대로. 구조 위반은 GenNormsError."""
    d = root / NORM_ROOT / stem
    metas = []
    for f in sorted(d.glob("*.md")):
        meta, body = parse_chunk(str(f))
        meta["_path"], meta["_body"] = rel(root, f), body
        if meta["type"] != NORM_TYPE:
            raise GenNormsError(f"{meta['_path']}: {NORM_ROOT}/ 의 청크는 type: {NORM_TYPE} 이다 — 실제 {meta['type']!r}")
        metas.append(meta)
    where = f"{NORM_ROOT}/{stem}"
    decls = [m for m in metas if isinstance(m.get("composite"), dict) and m["composite"].get("id")]
    roots = [m for m in decls if not m["composite"].get(PART_OF_KEY)]
    if len(roots) != 1:
        raise GenNormsError(f"{where}: 머리 청크(composite: 선언, composite.{PART_OF_KEY} 없음)는 정확히 하나다 — 실제 {len(roots)}개 "
                            f"(문서 하나 = 복합체 하나)")
    head = roots[0]
    comp = head["composite"]
    bundles = {m["composite"]["id"]: m for m in decls if m is not head}  # 묶음 복합체 IRI → 선언한 첫 절 청크
    comps = {comp["id"]: head, **bundles}
    for b, m in sorted(bundles.items()):
        if m["composite"][PART_OF_KEY] not in comps:
            raise GenNormsError(f"{m['_path']}: 묶음 복합체 {b} 의 composite.{PART_OF_KEY} 가 문서 복합체 {comp['id']} 또는 그 아래 묶음이 "
                                f"아니다 — 실제 {m['composite'][PART_OF_KEY]!r} (p4-composite-as-part-of)")
    stray = [m["_path"] for m in metas if m.get("part_of") not in comps]
    if stray:
        raise GenNormsError(f"{where}: part_of 가 문서의 복합체 {comp['id']} 또는 그 아래 묶음이 아닌 청크 — {stray}")
    by_id = {m["id"]: m for m in metas}
    for c, decl in sorted(comps.items()):  # 복합체마다 선언된 순서 = 직접 부분(절 청크 · 묶음) 전부 (p4-composite-order-is-declared)
        order = decl["composite"].get(ORDERED_KEY)
        parts = sorted([m["id"] for m in metas if m.get("part_of") == c] +
                       [b for b, m in bundles.items() if m["composite"][PART_OF_KEY] == c])
        if not order or sorted(order) != parts:
            raise GenNormsError(f"{decl['_path']}: 복합체 {c} 의 composite.{ORDERED_KEY} 가 직접 부분(절 청크 · 묶음 복합체) 전부를 빠짐없이 "
                                f"한 번씩 담아야 한다 — 절의 순서는 선언이다 (p4-composite-order-is-declared). 선언 {order} · 부분 {parts}")
        if order[0] != decl["id"]:
            raise GenNormsError(f"{decl['_path']}: composite.{ORDERED_KEY} 의 첫 부분은 선언 청크 자신이다 — 문서는 도입문(머리 청크)이, "
                                f"묶음은 선언한 첫 절 청크가 첫머리다")
    errors = norm_bundle_errors(head, [(m, m["_path"]) for m in metas])
    if errors:
        raise GenNormsError("; ".join(errors))
    order = flatten(comp["id"], comps, set())
    sections = [by_id[i] for i in order[1:]]  # 깊이 우선으로 펼친 절 — 묶음은 제목을 내지 않고 순서만 준다
    if sections and is_continuation(sections[0]):
        raise GenNormsError(f"{sections[0]['_path']}: 문서의 첫 절은 이어짐 절 청크({NORM_CONTINUES_KEY}: true)일 수 없다 — "
                            f"이어짐은 앞 절의 묶음 뒤를 잇는다")
    prev = 1
    for s in sections:
        if is_continuation(s):  # 깊이는 앞 절을 잇는다
            continue
        depth = int(s[NORM_DEPTH_KEY])
        if depth > prev + 1:
            raise GenNormsError(f"{s['_path']}: depth {depth} 가 앞 절의 깊이 {prev} 를 한 단계 넘게 건너뛴다 — 문서의 첫 절은 depth 2 다 (G8)")
        prev = depth
    return {"head": head, "sections": sections, "files": [m["_path"] for m in metas]}
```
<!-- 인용 끝 -->
