---
id: https://agentic-knowledge-base.dev/id/chunk/d1084eaf-333b-4dbd-ba82-e2d17786590c
type: artifact
level: executable
title_ko: 함수 render (tools/case_gen.py)
title: function render in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T12:40:09Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/57d4b0bb-fce0-462b-ba05-e71e7206bf74, https://agentic-knowledge-base.dev/id/chunk/769e8138-5647-40e0-8626-1ff77d838b92, https://agentic-knowledge-base.dev/id/chunk/b055ea3f-2020-43a8-8cc6-942e7df8e99f, https://agentic-knowledge-base.dev/id/chunk/b23dee78-99ba-49f8-bcde-88ea157cbe7a, https://agentic-knowledge-base.dev/id/chunk/b32a6a71-a1e8-4f65-89b7-47ea42f67f32, https://agentic-knowledge-base.dev/id/chunk/e222b91b-3e94-4d2c-a3f9-cf2851ce0d9f]
part_of: https://agentic-knowledge-base.dev/id/composite/d35350bd-7f95-4059-82b7-88108831c060
---
**함수** — `render(sc, a, case, name)` 다. 값 배정 하나 → 케이스 청크 텍스트.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render(sc: dict, a: dict, case: dict, name: str) -> str:
    """값 배정 하나 → 케이스 청크 텍스트. frontmatter 는 현행 케이스의 키 순서를 따른다."""
    keep, vals = sc["spec"]["keep"], a["values"]
    cls = "accept" if all(inside(keep[k], v) for k, v in vals.items()) else "reject"
    tmpl = case.get(cls)
    if tmpl is None:
        raise CaseGenError(f"{sc['path']}: `{name}` 은 `{cls}` 부류인데 `case.{cls}` 가 없다")
    key = json.dumps(vals, sort_keys=True, ensure_ascii=False)
    iri = CHUNK_NS + str(uuid.uuid5(uuid.NAMESPACE_URL, f"{sc['iri']}#case:{key}"))
    fm = ["---", f"id: {iri}", "type: schema", "level: concrete", f"title_ko: {fill(case['title_ko'], vals)}",
          f"title: {fill(case['title'], vals)}", "status: draft", f"sources: {sc['sources']}", f"assumes: {sc['assumes']}",
          f"generated: {{by: {ACTOR}, at: {sc['at']}}}", f"refines: [{case['criteria']}]"]
    if case.get("verifies"):
        fm.append(f"verifies: [{', '.join(case['verifies'])}]")
    derives = [sc["iri"]] + [x for x in dict.fromkeys(case.get("derivesFrom") or []) if x != sc["iri"]]  # 시나리오가 첫째다 — drift 가 첫 출처로 시나리오를 찾는다
    fm += [f"derivesFrom: [{', '.join(derives)}]", "---"]
    body = [f"**케이스** — {fill(case['summary'], vals).strip()}", "", f"**자극** — {fill(case['stimulus'], vals).strip()}", ""]
    files = fill_any(case.get("files") or {}, vals)
    if files:
        body += yaml_fence("files", files) + [""]
    body += [f"**기대** — {fill(tmpl['prose'], vals).strip()}", "", *yaml_fence("expect", fill_any(tmpl["expect"], vals)), ""]
    body += [f"**실행 명령** — `{fill(case['command'], vals).strip()}`", "", provenance(sc, a, cls)]
    return "\n".join(fm + body) + "\n"
```
<!-- 인용 끝 -->
