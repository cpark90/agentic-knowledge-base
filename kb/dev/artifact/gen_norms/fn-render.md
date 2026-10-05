---
id: https://agentic-knowledge-base.dev/id/chunk/0eed9071-0543-4627-8e10-d058808ca3cc
type: artifact
level: executable
title_ko: 함수 render (tools/gen_norms.py)
title: function render in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/082fbbdd-904c-4476-b773-8ebe8a85418e, https://agentic-knowledge-base.dev/id/chunk/0ce6acc5-e836-4236-a940-b32c38e5c86b, https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/49271822-40b4-4cdd-9e5c-c787b7bd458a, https://agentic-knowledge-base.dev/id/chunk/6dab97ca-f033-4314-aaff-01ed32eab6d5, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/a8f0dd40-2e94-4fef-91a8-971850c9f957, https://agentic-knowledge-base.dev/id/chunk/cca92813-a1e0-4006-9cf9-8775d4b68641, https://agentic-knowledge-base.dev/id/chunk/d0952dad-2a90-465f-bce8-0789223da6e8]
part_of: https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4
---
**함수** — `render(stem, out, doc, conventions)` 다. 문서 하나 — 머리 블록 + (G12) 목차 + 인용 구역(도입문 · 절마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render(stem: str, out: str, doc: dict, conventions: dict) -> str:
    """문서 하나 — 머리 블록 + (G12) 목차 + 인용 구역(도입문 · 절마다 제목 → 본문 → 항목) + (G4) 입력 파일 절."""
    head = doc["head"]
    numbering = head.get(NORM_NUMBERING_KEY)
    prefix, n = "", None
    if numbering:
        m = NORM_NUMBERING.match(str(numbering))
        prefix, n = m.group(1), int(m.group(2))
    inner: list[str] = []
    intro = rebase_links(head["_body"].strip(), head["_path"], out)
    if intro:
        inner += [intro, ""]
    inputs = set(doc["files"])
    n_items = 0
    for s in doc["sections"]:
        if not is_continuation(s):  # 이어짐 절 청크는 제목이 없고 번호를 소비하지 않는다
            depth = int(s[NORM_DEPTH_KEY])
            title = s[NORM_HEADING_KEY].strip()
            if depth == 2 and n is not None and s.get(NORM_NUMBERED_KEY, NORM_NUMBERED_DEFAULT) != "false":  # 번호 없는 절은 번호를 소비하지 않는다
                title = f"{prefix}{n}. {title}"
                n += 1
            inner += ["#" * depth + " " + title, ""]
        body = rebase_links(s["_body"].strip(), s["_path"], out)
        if body:
            inner += [body, ""]
        items = s.get("_norm_items") or []
        if items:
            inner += (render_table if form_of(s) == NORM_FORM_TABLE else render_list)(s, conventions, out) + [""]
        for it in items:
            for x in [it] + it["sub"]:
                inputs.add(conventions[x["ref"][0]]["path"])
            n_items += 1 + len(it["sub"])
    while inner and not inner[-1]:
        inner.pop()
    comp = head["composite"]
    header = kb_lib.gendoc_header(
        Path(out).name, comp["title_ko"], "tools/gen_norms.py",
        f"`{NORM_ROOT}/{stem}/` 의 절 청크를 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다",
        "python3 tools/gen_norms.py --root .", sorted(inputs), f"절 {len(doc['sections'])} · 규약 줄 {n_items}",
        kb_lib.gendoc_tree_notice(f"`{NORM_ROOT}/{stem}/` 의 절 청크와 결정의 `{CONVENTIONS_FILE}`", NOTICE_TARGET),
        input_kind="원본 파일", stamped=False)
    # 인용 구역을 줄 단위로 넘긴다 — 구역 안에도 제목 계층·목차 규칙이 적용되므로(G12) gendoc_assemble 이 본문의 실제 줄 수와
    # 제목을 세어 목차를 세운다. 원소 하나로 넘기면 120줄을 넘는 문서도 한 줄로 세어져 목차가 빠진다
    body = "\n".join(kb_lib.gendoc_quote("\n".join(inner))).split("\n") if inner else []
    return kb_lib.gendoc_assemble(header, body, sorted(inputs), input_kind="원본 파일", stamped=False)
```
<!-- 인용 끝 -->
