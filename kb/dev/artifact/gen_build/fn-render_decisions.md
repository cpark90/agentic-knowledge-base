---
id: https://agentic-knowledge-base.dev/id/chunk/f27e5261-f973-4030-9f81-9dab47f4a21a
type: artifact
level: executable
title_ko: 함수 render_decisions (tools/gen_build.py)
title: function render_decisions in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b9a75b3d-1c8f-4a7a-8f7f-dc10a84362fa
---
**함수** — `render_decisions(items, iri_to_label)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_decisions(items, iri_to_label):
    body = [HEADER, 'load("//defs:kb.bzl", "kb_bundle", "kb_decision")', "", 'package(default_visibility = ["//kb:decision_readers"])', "",
            'exports_files(["BUILD.bazel"])', "", 'filegroup(\n    name = "bodies",\n    srcs = glob(["**/*.md"]),\n)', ""]
    for lab, it in sorted(items.items()):
        if it["kind"] != "decision":
            continue
        p = it["parts"]
        links = {}
        for m in p.values():
            for k, v in links_of(m, iri_to_label, lab).items():
                links.setdefault(k, []).extend(v)
        body.append("kb_decision(\n" + f"    name = {q(it['dir'])},\n"
                    + "".join(f"    {n} = {q(it['dir'] + '/' + n + '.md')},\n" for n in ("conclusion", "rationale", "alternatives"))
                    + f"    iri = {q(it['comp_iri'])},\n"
                    # 순서는 선언이다 (유저 승인 2026-09-29: 결정도 예외 없음). 결정은 역할이 순서를 정하므로 생성기가 그 선언을
                    # 넣는다 — 205개 conclusion.md 의 frontmatter 를 손으로 고치는 것은 첨가이고, 순서의 원본은 추측이 아니라 이 인자다
                    + "    ordered = [" + ", ".join(q(p[n]["id"]) for n in DECISION_READING_ORDER) + "],\n"
                    + "    part_iris = [" + ", ".join(q(p[n]["id"]) for n in ("conclusion", "rationale", "alternatives")) + "],\n"
                    + "    part_levels = [" + ", ".join(q(p[n]["level"]) for n in ("conclusion", "rationale", "alternatives")) + "],\n"
                    + f"    status = {q(p['conclusion']['status'])},\n"
                    + "".join(label_list(k, sorted(set(v))) for k, v in sorted(links.items())) + ")\n")
    names = sorted(it["dir"] for it in items.values() if it["kind"] == "decision")
    body.append("# 이 패키지의 head 그래프 조각 묶음 — //kg:chunks_kg 가 병합한다\nkb_bundle(\n    name = \"kg\",\n" + label_list("items", [":" + n for n in names]) + ")\n")
    return "\n".join(body)
```
<!-- 인용 끝 -->
