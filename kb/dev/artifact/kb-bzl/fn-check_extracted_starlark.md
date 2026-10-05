---
id: https://agentic-knowledge-base.dev/id/chunk/d4a3b639-e07c-4c13-834b-aa0f9d944d12
type: artifact
level: executable
title_ko: 함수 check_extracted_starlark (defs/kb.bzl)
title: function check_extracted_starlark in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/1aefa82b-e840-4a41-89c0-385789709974
---
**함수** — `check_extracted_starlark(registry_globs)` 다. `defs` 패키지의 등록부 사이드카 glob 결과와 `EXTRACTED_STARLARK` 가 같은 집합인지 로드 시점에 강제한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def check_extracted_starlark(registry_globs):
    """`defs` 패키지의 등록부 사이드카 glob 결과와 `EXTRACTED_STARLARK` 가 같은 집합인지 로드 시점에 강제한다 (유저 답 Q32-a).

    `check_extracted_sources` 의 Starlark 소스판이다. `glob` 은 패키지를 넘지 못하므로 호출은 `defs/BUILD.bazel` 이 하고
    그 결과는 접두 없는 `<이름>.chunks.yml` 이다. 갈리면 이 패키지를 보는 어떤 bazel 명령이든 바로 `fail` 한다 —
    목록에만 있는 이름은 드리프트 테스트가 없는 등록부를 가리키고, 등록부에만 있는 이름은 검사 밖의 생성물을 남긴다.
    """
    found = sorted([f[:-len(".chunks.yml")] for f in registry_globs])
    missing_from_list = [m for m in found if m not in EXTRACTED_STARLARK]
    missing_from_tree = [m for m in EXTRACTED_STARLARK if m not in found]
    if missing_from_list or missing_from_tree:
        fail("EXTRACTED_STARLARK(//defs:kb.bzl) 와 defs/*.chunks.yml 의 실재가 갈린다 — " +
             "등록부는 있는데 목록에 없음: %s · 목록에는 있는데 등록부가 없음: %s" % (missing_from_list, missing_from_tree))
```
<!-- 인용 끝 -->
