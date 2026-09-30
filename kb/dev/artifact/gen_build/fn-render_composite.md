---
id: https://agentic-knowledge-base.dev/id/chunk/b741d4e1-90f5-4f0b-9bb2-10c4efbcdf69
type: artifact
level: executable
title_ko: 함수 render_composite (tools/gen_build.py)
title: function render_composite in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b9a75b3d-1c8f-4a7a-8f7f-dc10a84362fa
---
**함수** — `render_composite(lab, it, iri_to_label)` 다. 복합체 묶음 하나 → kb_composite 호출.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_composite(lab, it, iri_to_label):
    """복합체 묶음 하나 → kb_composite 호출. 형식은 kb_decision 과 같다 — 부분의 링크를 타깃 하나로 올린다.

    `ordered` 는 선언 청크 frontmatter 의 `composite.ordered` 를 그대로 옮긴 뷰다 (p4-composite-order-is-declared).
    선언이 없으면 인자도 없다 — 생성기는 순서를 추측하지 않는다.
    """
    links = {}
    for m in it["metas"]:
        for k, v in links_of(m, iri_to_label, lab).items():
            links.setdefault(k, []).extend(v)
    return ("kb_composite(\n" + f"    name = {q(lab.split(':')[1])},\n"
            + label_list("srcs", it["srcs"])
            + f"    iri = {q(it['comp_iri'])},\n"
            + ("    ordered = [" + ", ".join(q(i) for i in it["ordered"]) + "],\n" if it["ordered"] else "")
            + "    part_iris = [" + ", ".join(q(i) for i in it["part_iris"]) + "],\n"
            + f"    plane = {q(it['plane'])},\n" + f"    level = {q(it['level'])},\n" + f"    status = {q(it['status'])},\n"
            + "".join(label_list(k, sorted(set(v))) for k, v in sorted(links.items())) + ")\n")
```
<!-- 인용 끝 -->
