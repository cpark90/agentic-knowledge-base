---
id: https://agentic-knowledge-base.dev/id/chunk/b036d7e1-16f6-449e-a9cd-4ad07e213b53
type: artifact
level: executable
title_ko: 함수 plan (tools/gen_norms.py)
title: function plan in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T03:04:11Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/02b29145-5996-4360-8974-d74d70cd6de4, https://agentic-knowledge-base.dev/id/chunk/1b092132-a9fd-4db3-8feb-374efcc07e19, https://agentic-knowledge-base.dev/id/chunk/d0952dad-2a90-465f-bce8-0789223da6e8, https://agentic-knowledge-base.dev/id/chunk/e30fe78f-85fa-447c-8ec3-df25166cee41]
part_of: https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4
---
**함수** — `plan(root, docs, conventions)` 다. 문서 stem → 적재된 문서, (slug, k) → 쓰인 자리 (문서 stem, 절 청크 경로) 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def plan(root: Path, docs: dict[str, str], conventions: dict) -> tuple[dict, dict]:
    """문서 stem → 적재된 문서, (slug, k) → 쓰인 자리 (문서 stem, 절 청크 경로) 목록. 항목의 실재·강도를 여기서 판정하고 위반은 모아 GenNormsError 로 낸다."""
    errors: list[str] = []
    loaded, uses = {}, {}
    for stem in sorted(docs):
        doc = load_doc(root, stem)
        required = doc["head"].get(NORM_STRENGTH_KEY, STRENGTH_DEFAULT) == STRENGTH_DEFAULT
        for s in doc["sections"]:
            table = form_of(s) == NORM_FORM_TABLE
            cols = s.get(NORM_COLUMNS_KEY) or []
            width = len(cols) - (1 if NORM_LINK_COLUMN_KEY in s else 0)  # 줄이 채우는 칸 — 링크 열은 생성기가 채운다
            for it in s.get("_norm_items") or []:
                for x in [it] + it["sub"]:
                    slug, k = x["ref"]
                    c = conventions.get(slug)
                    if c is None:
                        errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 결정 {slug!r} 가 {DECISION_ROOT}/ 에 없다")
                        continue
                    if not c["live"] or not 1 <= k <= len(c["lines"]):
                        have = len(c["lines"]) if c["live"] else 0
                        errors.append(f"{s['_path']}: 항목 {slug}#{k} 가 없는 줄을 가리킨다 — {DECISION_ROOT}/{slug}/{CONVENTIONS_FILE} 의 "
                                      f"살아 있는 `규약:` 줄은 {have}개다 (p4-convention-slot)")
                        continue
                    uses.setdefault((slug, k), []).append((stem, s["_path"]))
                    if table:
                        strength, text = c["lines"][k - 1]
                        if strength is not None:
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 는 표 절의 행인데 줄에 강도 [{strength}] 가 있다 — 표의 줄은 "
                                          f"강도를 갖지 않는다. 줄을 `규약: a | b | …` 로 쓴다")
                        cells = table_cells(text)
                        if len(cells) != width:
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 칸 수 {len(cells)} 가 표의 열 수 {width}(링크 열 제외 "
                                          f"columns {cols}) 와 다르다 — 줄은 `a | b | …` 꼴이고 칸 안의 `|` 는 `\\|` 로 쓴다")
                        elif not all(cells):
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 에 빈 칸이 있다 — 빈 값은 `{kb_lib.NONE_MARK}` 으로 적는다 (G14)")
                    elif required and c["lines"][k - 1][0] is None:
                        errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 줄에 강도가 없다 — 문서 {stem} 은 강도를 요구한다"
                                      f"(머리 청크 strength: required). 줄을 `규약: [지킴] …` 또는 `규약: [권장] …` 으로 쓴다")
                    for extra in x["links"]:
                        if not conventions.get(extra, {}).get("linkable"):
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 링크 결정 {extra!r} 의 결론 청크가 없다 — "
                                          f"{DECISION_ROOT}/{extra}/{CONCLUSION_FILE}")
        loaded[stem] = doc
    for slug, c in sorted(conventions.items()):
        if not c["live"]:
            continue
        for k in range(1, len(c["lines"]) + 1):
            used = uses.get((slug, k), [])
            if not used:
                errors.append(f"{c['path']}: 줄 {slug}#{k} 를 어느 규범 문서도 싣지 않는다(고아 줄) — 줄은 적어도 한 문서에서 "
                              f"쓰인다. 절 청크의 items 에 `{slug}#{k}` 를 더한다 (p12-norm-documents-from-section-chunks)")
            for stem in sorted({d for d, _ in used}):
                paths = sorted(path for d, path in used if d == stem)
                if len(paths) > 1:
                    errors.append(f"{c['path']}: 줄 {slug}#{k} 가 문서 {stem} 안에서 {len(paths)}번 쓰였다(이중 소비) — {paths}. "
                                  f"한 문서 안에서는 한 줄을 한 번까지만 싣는다. 다른 문서가 같은 줄을 싣는 것은 허용한다")
    if errors:
        raise GenNormsError("\n".join(errors))
    return loaded, uses
```
<!-- 인용 끝 -->
