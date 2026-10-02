---
id: https://agentic-knowledge-base.dev/id/chunk/869af6ba-5152-4bae-8ae4-1081f5177303
type: artifact
level: executable
title_ko: 함수 render_chunks (tools/gen_build.py)
title: function render_chunks in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0f0f082a-c9cd-454c-ab65-ca4f3bebc461, https://agentic-knowledge-base.dev/id/chunk/a8f6816d-512e-4fb2-8bce-765ddee8bf42, https://agentic-knowledge-base.dev/id/chunk/b741d4e1-90f5-4f0b-9bb2-10c4efbcdf69, https://agentic-knowledge-base.dev/id/chunk/e284beaa-0477-4715-ba21-44028b13bf3f]
part_of: https://agentic-knowledge-base.dev/id/composite/b9a75b3d-1c8f-4a7a-8f7f-dc10a84362fa
---
**함수** — `render_chunks(pkg, items, iri_to_label, visibility, allow_empty)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_chunks(pkg, items, iri_to_label, visibility, allow_empty=False):
    glob_ = 'glob(\n        ["*.md"],\n        allow_empty = True,\n    )' if allow_empty else 'glob(["*.md"])'
    rules = ["kb_bundle", "kb_chunk"] + (["kb_composite"] if any(it["pkg"] == pkg and it["kind"] == "composite" for it in items.values()) else [])
    body = [HEADER, 'load("//defs:kb.bzl", ' + ", ".join(q(r) for r in sorted(rules)) + ")", "",
            f"package(default_visibility = [{q(visibility)}])", "",
            'exports_files(["BUILD.bazel"])', "", f'filegroup(\n    name = "bodies",\n    srcs = {glob_},\n)', ""]
    for lab, it in sorted(items.items()):
        if it["pkg"] != pkg:
            continue
        if it["kind"] == "composite":  # 복합체 = 타깃 하나, 부분 청크의 개별 타깃은 없다 (p4-all-knowledge-is-composite)
            body.append(render_composite(lab, it, iri_to_label))
            continue
        m = it["meta"]
        links = links_of(m, iri_to_label, lab)
        body.append("kb_chunk(\n" + f"    name = {q(lab.split(':')[1])},\n" + f"    src = {q(it['src'])},\n" + f"    iri = {q(m['id'])},\n"
                    + f"    plane = {q(m['type'])},\n" + f"    level = {q(m['level'])},\n" + f"    status = {q(m['status'])},\n"
                    + "".join(label_list(k, v) for k, v in sorted(links.items())) + ")\n")
    names = sorted(lab.split(":")[1] for lab, it in items.items() if it["pkg"] == pkg)
    body.append("# 이 패키지의 head 그래프 조각 묶음 — //kg:chunks_kg 가 병합한다\nkb_bundle(\n    name = \"kg\",\n"
                + (label_list("items", [":" + n for n in names]) or "    items = [],\n") + ")\n")
    return "\n".join(body)
```
<!-- 인용 끝 -->
