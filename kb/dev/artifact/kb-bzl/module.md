---
id: https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc
type: artifact
level: executable
title_ko: 파일 defs/kb.bzl
title: file defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T18:25:23Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/c5bb1922-eb82-4b96-a49c-a46e41c239e4, https://agentic-knowledge-base.dev/id/chunk/ee51de32-a48b-4ade-a147-4953bce27364, https://agentic-knowledge-base.dev/id/chunk/af618b63-841a-4c19-a935-62ec246c2218, https://agentic-knowledge-base.dev/id/chunk/525c2b08-d69e-41f1-bbcd-fbffa082a5eb]
---
**파일** — `defs/kb.bzl` 다. 718줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

**모듈 머리** — 모듈 docstring 과 `load` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
load("@bazel_skylib//rules:common_settings.bzl", "BuildSettingInfo")

"""단위 지식을 Bazel 타깃으로 — provider·규칙·가시성 (bazel-dependency-review B + 연결성, 2026-09-11).

원칙: 의존의 원본은 그래프(frontmatter·owl:imports)이고 BUILD는 생성물(tools/gen_build.py)이다.
Bazel이 맡는 것은 링크의 **구조** — 끝점의 존재(로드 시점), 방향(가시성·분석 시점 fail), 파급(rdeps).
링크의 **의미**(SHACL·통제 어휘·상태 전이)는 그래프 게이트(p6-validate-the-union 의 union)가 그대로 맡는다.
"""
```
<!-- 인용 끝 -->
