---
id: https://agentic-knowledge-base.dev/id/chunk/552acfff-57db-463e-82cb-cdace15cb87d
type: artifact
level: executable
title_ko: 함수 render_artifact_root (tools/gen_build.py)
title: function render_artifact_root in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/b9a75b3d-1c8f-4a7a-8f7f-dc10a84362fa
---
**함수** — `render_artifact_root(root)` 다. //kb/dev/artifact — 소스 파일별 패키지의 bodies·kg 를 모은다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_artifact_root(root: Path):
    """//kb/dev/artifact — 소스 파일별 패키지의 bodies·kg 를 모은다. //kb/dev:bodies·//kg:chunks_kg 의 단일 끝점이다.

    파일을 하나 올릴 때마다 손으로 두 BUILD 를 고치지 않도록 여기가 집계처다 — 패키지 목록의 원본은 트리이고 이 파일은 뷰다.
    """
    pkgs = artifact_pkgs(root)
    body = [HEADER, 'load("//defs:kb.bzl", "kb_bundle")', "",
            "# 추출된 코드 청크 (p7-code-extraction-direction) — 소스 파일 하나 = 패키지 하나. 원본은 tools/*.py 이고\n"
            "# 청크는 tools/extract.py 의 생성물이다. 손으로 고치면 //:extract_drift_test 가 거부한다.",
            'package(default_visibility = ["//visibility:public"])', "", 'exports_files(["BUILD.bazel"])', "",
            'filegroup(\n    name = "bodies",\n    srcs = [\n'
            + "".join(f'        "//{ARTIFACT_ROOT}/{p}:bodies",\n' for p in pkgs)
            + '    ],\n)\n' if pkgs else 'filegroup(\n    name = "bodies",\n    srcs = [],\n)\n',
            "# 이 plane 의 head 그래프 조각 묶음 — //kg:chunks_kg 가 병합한다\nkb_bundle(\n    name = \"kg\",\n"
            + (label_list("items", [f"//{ARTIFACT_ROOT}/{p}:kg" for p in pkgs]) or "    items = [],\n") + ")\n"]
    return "\n".join(body)
```
<!-- 인용 끝 -->
