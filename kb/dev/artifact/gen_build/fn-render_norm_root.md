---
id: https://agentic-knowledge-base.dev/id/chunk/e54eb0d7-070d-49c3-80c1-2c299c1c0b7a
type: artifact
level: executable
title_ko: 함수 render_norm_root (tools/gen_build.py)
title: function render_norm_root in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0f0f082a-c9cd-454c-ab65-ca4f3bebc461, https://agentic-knowledge-base.dev/id/chunk/7da9bdbd-c81f-432f-a9a2-fe6561f504be, https://agentic-knowledge-base.dev/id/chunk/7e58cd2b-ecf9-4a21-a66b-9e28aa4474e9, https://agentic-knowledge-base.dev/id/chunk/a8f6816d-512e-4fb2-8bce-765ddee8bf42]
part_of: https://agentic-knowledge-base.dev/id/composite/6400a2c9-ed32-428b-bd76-5952553e5e04
---
**함수** — `render_norm_root(root)` 다. //kb/dev/norm — 문서별 패키지의 본문 묶음·kg 를 모은다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_norm_root(root: Path):
    """//kb/dev/norm — 문서별 패키지의 본문 묶음·kg 를 모은다. //kb/dev·//kg:chunks_kg 의 단일 끝점이다 (render_artifact_root 와 같은 형).

    문서 목록의 단일 정의처는 defs/kb.bzl 의 NORM_DOCS 이고 디렉토리 집합과의 일치는 생성기 gen_norms 가 본다 — 여기는 트리를 따른다.
    """
    pkgs = norm_pkgs(root)
    srcs = ('    srcs = [\n' + "".join(f'        "//{NORM_ROOT}/{p}",\n' for p in pkgs) + '    ],\n') if pkgs else "    srcs = [],\n"
    body = [HEADER, 'load("//defs:kb.bzl", "kb_bundle")', "",
            "# 규범 문서의 절 청크 (p12-norm-documents-from-section-chunks) — 문서 하나 = 패키지 하나 = 복합체 하나. 문서는\n"
            "# tools/gen_norms.py 가 이 청크와 결정의 conventions.md 에서 생성하고 //:norms_drift_test 가 바이트로 비교한다.",
            'package(default_visibility = ["//visibility:public"])', "", 'exports_files(["BUILD.bazel"])', "",
            f'filegroup(\n    name = {q(pkg_group(NORM_ROOT))},\n{srcs})\n',
            "# 이 plane 의 head 그래프 조각 묶음 — //kg:chunks_kg 가 병합한다\nkb_bundle(\n    name = \"kg\",\n"
            + (label_list("items", [f"//{NORM_ROOT}/{p}:kg" for p in pkgs]) or "    items = [],\n") + ")\n"]
    return "\n".join(body)
```
<!-- 인용 끝 -->
