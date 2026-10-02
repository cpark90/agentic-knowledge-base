---
id: https://agentic-knowledge-base.dev/id/chunk/7ab8e5ae-063f-4b69-99f7-9b984ccc4617
type: artifact
level: executable
title_ko: 장 gates-name (tools/kb_lib.py)
title: chapter gates-name in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/e7e09bb4-4c00-411e-9e5d-857406143657
composite: {id: https://agentic-knowledge-base.dev/id/composite/e7e09bb4-4c00-411e-9e5d-857406143657, title_ko: 장 복합체 gates-name (tools/kb_lib.py), title: chapter composite gates-name in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/7ab8e5ae-063f-4b69-99f7-9b984ccc4617, https://agentic-knowledge-base.dev/id/composite/cf732fdc-d595-4d0b-8344-6af01989d95c, https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294], part_of: https://agentic-knowledge-base.dev/id/composite/dca529bc-79c6-4569-af4c-122c0d736686}
---
**장** — `tools/kb_lib.py` 의 장 `gates-name` 다. 게이트 등록부와 저장소 경계

**정의** — 없음. 선언과 상수만 있는 구역이다.

**하위 구역** — `gates-name` · `kb-dev` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ══ 게이트 등록부와 저장소 경계 ════════════════════
# 단일 정의처가 `defs/kb.bzl` 의 리터럴이고 파이썬이 그것을 읽어 파생하는 것 둘 — 게이트 id 와 수준 허용표다.
# 둘 다 분석 시점 판정에 쓰이므로 표가 Starlark 쪽에 살고, 읽기 함수와 파생이 이 장에 있다 (M1 단일 정의처).
```
<!-- 인용 끝 -->
