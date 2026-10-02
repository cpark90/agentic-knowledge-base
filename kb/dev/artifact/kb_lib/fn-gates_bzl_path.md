---
id: https://agentic-knowledge-base.dev/id/chunk/04fe68bc-58a1-45bd-ac00-78d263cbba81
type: artifact
level: executable
title_ko: 함수 gates_bzl_path (tools/kb_lib.py)
title: function gates_bzl_path in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/cf732fdc-d595-4d0b-8344-6af01989d95c
---
**함수** — `gates_bzl_path()` 다. `GATES` 리터럴이 사는 `defs/kb.bzl` 의 경로 — 환경 변수 · runfiles · 소스 트리 순으로 찾는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gates_bzl_path() -> Path:
    """`GATES` 리터럴이 사는 `defs/kb.bzl` 의 경로 — 환경 변수 · runfiles · 소스 트리 순으로 찾는다.

    runfiles 에서는 `//defs:kb.bzl` 이 `py_library //tools:kb_lib` 의 `data` 로 따라오므로 이 모듈의 위치에서
    워크스페이스 루트를 거슬러 찾는다. 못 찾으면 FileNotFoundError 다 — 판정 불가지 통과가 아니다.
    """
    env = os.environ.get(GATES_BZL_ENV)
    if env:
        return Path(env)
    here = Path(__file__)
    for base in (here.parent, here.resolve().parent):
        for up in range(1, 5):
            cand = base.parents[up - 1] / "defs" / "kb.bzl"
            if cand.is_file():
                return cand
    raise FileNotFoundError(
        "defs/kb.bzl 을 찾을 수 없다 — 게이트 등록부 GATES 의 단일 정의처다. "
        "py_test·py_binary 의 data 에 //defs:kb.bzl 을 더하거나 %s 로 경로를 준다" % GATES_BZL_ENV)
```
<!-- 인용 끝 -->
