---
id: https://agentic-knowledge-base.dev/id/chunk/c76e78d9-c530-49ad-85b7-9d8e6b3fc8bb
type: decision
level: logical
title_ko: 같은 목록이 여러 자리에 적히면 갈라지고 분석 시점에 쓰이는 표는 Starlark 쪽에 살아야 한다
title: A list written in several places diverges, and tables used at analysis time must live on the Starlark side
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/d36b748b-cc0d-46c5-9df7-7d05708e3cd1
---
**근거** — 원문(2026-09-01)의 이유는 둘이다. 상수는 접미사·네임스페이스 같은 규약 값이 파일마다 복제되지 않게 한 자리에 둔다(`tools/kb_lib.py` docstring은 노트 0.2절 접미사·0.3절 네임스페이스의 정의처라 적는다). 검사 함수는 검사 사이의 결합을 만들지 않으려고 독립시킨다.

2026-10-01 실측이 복제의 비용을 보였다. 게이트 id 목록이 넷으로 갈려 있었다 — `kb_lib`의 `*_GATE` 상수, 코드의 태그, `docs/tools.md` 총람의 `id` 열, 하네스 목록이다. 2026-10-02 `GATES` 리터럴 하나로 모으고 나머지를 파생으로 바꿨다(`defs/kb.bzl` 주석).

정의처가 `defs/kb.bzl`인 까닭은 Starlark가 파이썬 파일을 읽지 못하기 때문이다. 분석 시점 판정에 쓰이는 표는 Starlark 쪽에 살고 파이썬이 그 리터럴을 읽는다(`tools/kb_lib.py` 주석, `RESIDENCY`·`EXTRACTED_SOURCES`와 같은 해법). 본문 떼기와 계수기가 `chunk2kg`에 있는 까닭은 head 액션이 타깃마다 돌고 rdflib를 싣지 않기 때문이다(같은 주석).

실측(2026-10-03)에서 `check_prose`·`check_gendoc`은 게이트 위반과 보고 후보를 튜플로 함께 낸다. `list[str]` 꼴의 권장과 다르다. `tools/gen_build.py`는 rdflib 없이 돌아 `kb_lib`을 싣지 않으므로 경로 접두(`VV_ROOT` 등)를 자체 상수로 두고 정의처를 주석으로 가리킨다.

앞선 판의 미확정(규범 문서의 "단일 정의처는 `tools/kb_lib.py`" 문장이 `defs/kb.bzl` 리터럴과 `chunk2kg`의 몫을 포함하도록 고쳐지는가)은 닫혔다. 규범 문서는 이 결정의 규약 줄에서 생성되고 그 줄이 두 자리를 담는다(2026-10-04).
