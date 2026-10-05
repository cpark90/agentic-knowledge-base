---
id: https://agentic-knowledge-base.dev/id/chunk/c00df5fa-5f8a-4f58-ad04-8357419cf445
type: artifact
level: executable
title_ko: 절 tool-tags (defs/kb.bzl)
title: section tool-tags in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/43c17d6f-f9ef-4fa2-aa31-cf3f8e6acc81
composite: {id: https://agentic-knowledge-base.dev/id/composite/43c17d6f-f9ef-4fa2-aa31-cf3f8e6acc81, title_ko: 절 복합체 tool-tags (defs/kb.bzl), title: section composite tool-tags in defs/kb.bzl, ordered: [https://agentic-knowledge-base.dev/id/chunk/c00df5fa-5f8a-4f58-ad04-8357419cf445, https://agentic-knowledge-base.dev/id/chunk/849657ba-c3cf-4977-8106-9d89338460ff], part_of: https://agentic-knowledge-base.dev/id/composite/b5154bf0-e67d-4227-8b66-c63012041201}
---
**절** — `defs/kb.bzl` 의 절 `tool-tags` 다. 도구 태그와 등록부의 자기 정합성 검사

**정의** — `check_gates` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 도구 태그와 등록부의 자기 정합성 검사 ─────────────────────────────────────────────────────────────
# 게이트가 아닌 **도구 태그** — 입력·설정 문제와 보고에만 쓰여 판정 효과가 없다(뷰·생성기의 CONFIG·WARN 자리).
# 같은 대괄호 표기를 쓰므로 게이트 `gate-registry` 가 태그 전수를 볼 때 이 목록이 둘째 경계다 (USES_TARGETS 와
# 같은 자리). `GATES` 와 서로소여야 한다 — `check_gates` 가 로드 시점에 강제한다.
TOOL_TAGS = [
    "consistency",
    "endorse",  # 쓰는 시점의 입력 거부(미래 시각의 --at) — 게이트는 시계에 의존할 수 없어 판정 효과가 없다
    "judge",
    "link",
    "open",
    "propose",
    "revalidate",
    "run-evidence",  # 실행 증거 생성기의 입력 거부(읽을 수 없는 청크·값 어휘) — 판정 효과가 없다
    "tokens",
    "validate",
    "weave",
]
```
<!-- 인용 끝 -->
