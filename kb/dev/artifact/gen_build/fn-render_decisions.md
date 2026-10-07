---
id: https://agentic-knowledge-base.dev/id/chunk/f27e5261-f973-4030-9f81-9dab47f4a21a
type: artifact
level: executable
title_ko: 함수 render_decisions (tools/gen_build.py)
title: function render_decisions in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0f0f082a-c9cd-454c-ab65-ca4f3bebc461, https://agentic-knowledge-base.dev/id/chunk/a8f6816d-512e-4fb2-8bce-765ddee8bf42, https://agentic-knowledge-base.dev/id/chunk/e284beaa-0477-4715-ba21-44028b13bf3f]
part_of: https://agentic-knowledge-base.dev/id/composite/bd43acdb-4493-4bcb-852c-56bb2a3c929e
---
**함수** — `render_decisions(items, iri_to_label)` 다. //kb/dev/decision — 결정 디렉토리 하나 = kb_decision 하나.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_decisions(items, iri_to_label):
    """//kb/dev/decision — 결정 디렉토리 하나 = kb_decision 하나. 본문 묶음은 세 부분 파일의 명시 목록이다.

    결정은 `<디렉토리>/{conclusion,rationale,alternatives}.md` 의 두 디렉토리 깊이다. `glob` 은 패키지 안 한 디렉토리 깊이만 대상으로 하므로
    (STYLEGUIDE §6 [권장]) 깊은 glob 대신 생성기가 이미 열거한 디렉토리에서 파일 목록을 낸다 — 목록의 원본은 트리이고
    이 파일은 뷰다. 세 부분 밖의 `.md` 는 묶음에 들지 않는다.
    """
    dirs = sorted(it["dir"] for it in items.values() if it["kind"] == "decision")
    parts_of = {it["dir"]: it["parts"] for it in items.values() if it["kind"] == "decision"}
    body = [HEADER, 'load("//defs:kb.bzl", "kb_bundle", "kb_decision")', "", 'package(default_visibility = ["//kb:decision_readers"])', "",
            'exports_files(["BUILD.bazel"])', "",
            'filegroup(\n    name = "decision",\n' + label_list("srcs", [f"{d}/{n}.md" for d in dirs for n in DECISION_READING_ORDER + (DECISION_OPTIONAL_PART,)
                                                                           if n in parts_of[d]]) + ")\n"]
    for lab, it in sorted(items.items()):
        if it["kind"] != "decision":
            continue
        p = it["parts"]
        links = {}
        for m in p.values():
            for k, v in links_of(m, iri_to_label, lab).items():
                links.setdefault(k, []).extend(v)
        roles = [n for n in DECISION_READING_ORDER + (DECISION_OPTIONAL_PART,) if n in p]  # 규약 청크는 있으면 넷째다
        body.append("kb_decision(\n" + f"    name = {q(it['dir'])},\n"
                    + "".join(f"    {n} = {q(it['dir'] + '/' + n + '.md')},\n" for n in roles)
                    + f"    iri = {q(it['comp_iri'])},\n"
                    # 순서는 선언이다 (유저 승인 2026-09-29: 결정도 예외 없음). 결정은 역할이 순서를 정하므로 생성기가 그 선언을
                    # 넣는다 — 205개 conclusion.md 의 frontmatter 를 손으로 고치는 것은 첨가이고, 순서의 원본은 추측이 아니라 이 인자다
                    + "    ordered = [" + ", ".join(q(p[n]["id"]) for n in roles) + "],\n"
                    + "    part_iris = [" + ", ".join(q(p[n]["id"]) for n in roles) + "],\n"
                    + "    part_levels = [" + ", ".join(q(p[n]["level"]) for n in roles) + "],\n"
                    + f"    status = {q(p['conclusion']['status'])},\n"
                    + "".join(label_list(k, sorted(set(v))) for k, v in sorted(links.items())) + ")\n")
    names = sorted(it["dir"] for it in items.values() if it["kind"] == "decision")
    body.append("# 이 패키지의 head 그래프 조각 묶음 — //kg:chunks_kg 가 병합한다\nkb_bundle(\n    name = \"kg\",\n" + label_list("items", [":" + n for n in names]) + ")\n")
    return "\n".join(body)
```
<!-- 인용 끝 -->
