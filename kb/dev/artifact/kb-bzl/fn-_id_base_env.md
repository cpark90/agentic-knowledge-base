---
id: https://agentic-knowledge-base.dev/id/chunk/f779747e-220b-4ee0-b27f-1bf4f23584c5
type: artifact
level: executable
title_ko: 함수 _id_base_env (defs/kb.bzl)
title: function _id_base_env in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/de15c0eb-b277-4159-9610-3cf83fed1763
---
**함수** — `_id_base_env(ctx)` 다. 단위 지식 IRI 이름공간의 환경 변수 — 빌드 설정 `//defs:id_base` 의 값을 **루트 모듈의 타깃에만** 준다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
def _id_base_env(ctx):
    """단위 지식 IRI 이름공간의 환경 변수 — 빌드 설정 `//defs:id_base` 의 값을 **루트 모듈의 타깃에만** 준다 (task 0327 손질 9).

    값이 비면 도구가 자기 기본값(`chunk2kg.ID_BASE_DEFAULT`)을 쓴다. 이 모듈이 다른 저장소의 의존일 때 이 모듈 자신의
    타깃(`ctx.label.repo_name` 이 비지 않는다)은 설정을 받지 않는다 — 플래그는 빌드 전체에 하나라서, 그러지 않으면 코어의
    지식이 의존 저장소의 이름공간으로 다시 이름 붙는다. `ctx.attr._id_base` 가 그 설정을 가리킨다.
    """
    if ctx.label.repo_name:
        return {}
    return {"KB_ID_BASE": ctx.attr._id_base[BuildSettingInfo].value}
```
<!-- 인용 끝 -->
