---
id: https://agentic-knowledge-base.dev/id/chunk/18ab5773-e7d0-40b1-8790-f360d7a35f48
type: artifact
level: executable
title_ko: 함수 check_extracted_sources (defs/kb.bzl)
title: function check_extracted_sources in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/1aefa82b-e840-4a41-89c0-385789709974
---
**함수** — `check_extracted_sources(registry_globs)` 다. 등록부 사이드카 glob 결과와 `EXTRACTED_SOURCES` + `EXTRACTED_QUERY_DIRS` 가 같은 집합인지 로드 시점에 강제한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def check_extracted_sources(registry_globs):
    """등록부 사이드카 glob 결과와 `EXTRACTED_SOURCES` + `EXTRACTED_QUERY_DIRS` 가 같은 집합인지 로드 시점에 강제한다 (M1, 2026-10-01).

    `registry_globs` 는 호출자(`tools/BUILD.bazel`)가 준 `glob(["*.chunks.yml"])` 의 결과다 — `glob` 은 패키지를
    넘어가지 못하므로(최상위 `BUILD.bazel` 에서 `tools/*.chunks.yml` 을 globbing 할 수 없다) 호출은 `tools`
    패키지 안에서 하고, 그 결과는 접두 없는 `<이름>.chunks.yml` 이다. BUILD 파일은 `if` 문을 쓸 수 없어 이
    판정을 함수로 옮겼다(`_check_residency` 와 같은 자리). 갈리면 이 패키지를 보는 어떤 bazel 명령이든 바로
    `fail` 한다 — 조용히 비는 사고(음성 시험, 유저 지시 2026-10-01)를 막는다. `USES_TARGETS` 가
    `EXTRACTED_SOURCES` 의 부분집합인지도 같은 자리에서 본다 — 치역 경계와 방출 경계의 두 목록이 갈리면
    `uses` 의 대상이 실재하지 않는다.
    """
    found = sorted([f[:-len(".chunks.yml")] for f in registry_globs])
    both = [m for m in EXTRACTED_QUERY_DIRS if m in EXTRACTED_SOURCES]
    if both:
        fail("EXTRACTED_SOURCES 와 EXTRACTED_QUERY_DIRS(//defs:kb.bzl) 가 겹친다 — %s. " % both +
             "등록부 사이드카 하나는 소스 모듈 하나이거나 질의 디렉토리 하나다")
    listed = EXTRACTED_SOURCES + EXTRACTED_QUERY_DIRS
    missing_from_list = [m for m in found if m not in listed]
    missing_from_tree = [m for m in listed if m not in found]
    if missing_from_list or missing_from_tree:
        fail("EXTRACTED_SOURCES·EXTRACTED_QUERY_DIRS(//defs:kb.bzl) 와 tools/*.chunks.yml 의 실재가 갈린다 — " +
             "등록부는 있는데 목록에 없음: %s · 목록에는 있는데 등록부가 없음: %s" % (missing_from_list, missing_from_tree))
    outside = [m for m in USES_TARGETS if m not in EXTRACTED_SOURCES]
    if outside:
        fail("USES_TARGETS(//defs:kb.bzl) 가 EXTRACTED_SOURCES 밖을 치역으로 둔다 — %s. " % outside +
             "추출되지 않은 모듈에는 정의 청크가 없어 `uses` 의 대상이 실재하지 않는다 (dangling)")
```
<!-- 인용 끝 -->
