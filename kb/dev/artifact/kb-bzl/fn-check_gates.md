---
id: https://agentic-knowledge-base.dev/id/chunk/849657ba-c3cf-4977-8106-9d89338460ff
type: artifact
level: executable
title_ko: 함수 check_gates (defs/kb.bzl)
title: function check_gates in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/43c17d6f-f9ef-4fa2-aa31-cf3f8e6acc81
---
**함수** — `check_gates()` 다. `GATES`·`TOOL_TAGS` 리터럴의 자기 정합성을 로드 시점에 강제한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def check_gates():
    """`GATES`·`TOOL_TAGS` 리터럴의 자기 정합성을 로드 시점에 강제한다 (M1, check_extracted_sources 와 같은 자리).

    `BUILD` 파일은 `if` 문을 쓸 수 없어 판정을 함수로 옮겼다. 항목마다 네 키(`tier`·`tool`·`ko`·`desc`)가 있고
    `tier` 는 `GATE_TIERS` 안이며 두 목록은 서로소다. 갈리면 이 패키지를 보는 어떤 bazel 명령이든 바로 `fail`
    한다 — 등록부가 조용히 비거나 어긋나는 사고를 막는다.
    """
    for gid, spec in GATES.items():
        for key in ["tier", "tool", "ko", "desc"]:
            if key not in spec or not spec[key]:
                fail("GATES(//defs:kb.bzl) 의 %r 에 %s 가 없다 — 항목마다 실행 계층·판정 도구·한글 라벨·설명 한 줄을 적는다" % (gid, key))
        if spec["tier"] not in GATE_TIERS:
            fail("GATES(//defs:kb.bzl) 의 %r 의 실행 계층 %r 이 어휘 밖이다 — %s 중 하나다" % (gid, spec["tier"], GATE_TIERS))
    both = [t for t in TOOL_TAGS if t in GATES]
    if both:
        fail("GATES 와 TOOL_TAGS(//defs:kb.bzl) 가 겹친다 — %s. " % both +
             "한 태그는 게이트이거나 도구 태그이고 둘 다일 수 없다")
```
<!-- 인용 끝 -->
