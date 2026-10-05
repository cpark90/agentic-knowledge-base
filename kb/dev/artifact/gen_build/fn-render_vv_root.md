---
id: https://agentic-knowledge-base.dev/id/chunk/50e03067-a51a-4276-beaa-b3062acbca52
type: artifact
level: executable
title_ko: 함수 render_vv_root (tools/gen_build.py)
title: function render_vv_root in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7da9bdbd-c81f-432f-a9a2-fe6561f504be, https://agentic-knowledge-base.dev/id/chunk/a8f6816d-512e-4fb2-8bce-765ddee8bf42]
part_of: https://agentic-knowledge-base.dev/id/composite/bd43acdb-4493-4bcb-852c-56bb2a3c929e
---
**함수** — `render_vv_root(items)` 다. //kb/vv — 하위 plane 패키지의 본문 묶음을 모으고, 청크가 하나라도 있으면 lint_test 를 켠다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_vv_root(items):
    """//kb/vv — 하위 plane 패키지의 본문 묶음을 모으고, 청크가 하나라도 있으면 lint_test 를 켠다 (빈 filegroup 은 $(rootpaths) 확장이 분석 에러다)."""
    subs = sorted(VV_PKGS)
    nonempty = any(it["pkg"].startswith(VV_ROOT + "/") for it in items.values())
    body = [HEADER]
    if nonempty:
        body.append('load("//defs:knowledge.bzl", "kb_chunk_lint_test")\n')
    body += ["# V&V KB — 시나리오 기반 확인의 지식 (노트 7.1절). 개발 KB 와 같은 코어의 두 번째 인스턴스 (p8-vv-plane-instances): 디렉토리 = plane.\n"
             "# 편집은 vnv 만(kg/catalog-kg.ttl agt:writesIn \"kb/vv\"), 개발 역할은 읽기만. verifies 링크만 KB 를 가로지른다 (V&V → 개발, 같은 level).",
             'package(default_visibility = ["//visibility:public"])', "", 'exports_files(["BUILD.bazel"])', "",
             f'filegroup(\n    name = {q(pkg_group(VV_ROOT))},\n    srcs = [\n' + "".join(f'        "//{VV_ROOT}/{s}",\n' for s in subs)
             + '    ] + glob(\n        ["*.md"],\n        allow_empty = True,\n    ),\n)\n']
    if nonempty:
        body.append('kb_chunk_lint_test(\n    name = "lint_test",\n    chunks = [' + q(":" + pkg_group(VV_ROOT)) + '],\n    waivers = "//docs:waivers",  # prose 면제 선언 (docs/waivers.md)\n)\n')
    else:
        body.append("# lint_test 는 첫 청크가 들어오면 생성기가 켠다 — 빈 filegroup 은 $(rootpaths) 확장이 분석 에러다\n")
    return "\n".join(body)
```
<!-- 인용 끝 -->
