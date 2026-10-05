---
id: https://agentic-knowledge-base.dev/id/chunk/093f3277-7080-49e5-8c34-6f48eec1106d
type: artifact
level: executable
title_ko: 절 gate-layer (defs/kb.bzl)
title: section gate-layer in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b5154bf0-e67d-4227-8b66-c63012041201
---
**절** — `defs/kb.bzl` 의 절 `gate-layer` 다. 게이트 등록부 (`GATES`) — 게이트 id 의 **단일 정의처** (M1, 2026-10-02, RESIDENCY·EXTRACTED_SOURCES 와 같은 해법)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 게이트 등록부 (`GATES`) — 게이트 id 의 **단일 정의처** (M1, 2026-10-02, RESIDENCY·EXTRACTED_SOURCES 와 같은 해법) ─
# 결정 p0-service-is-a-three-layer-wiki: 게이트는 프로세스 층의 **항목**이다. 2026-10-01 실측에서 같은 목록이 넷으로
# 갈려 있었다 — `kb_lib` 의 `*_GATE` 상수 · 코드의 태그 · `docs/tools.md` 총람의 `id` 열 · 그 아래 하네스 목록.
# 여기 말고 어디에도 게이트 id 를 손으로 적지 않는다. 파생처는 넷이다 — `tools/kb_lib.py` 의 `load_gates`(리터럴
# 읽기 → 모듈 속성 `<이름>_GATE`) · `tools/gates2kg.py`(생성 그래프 `//kg:gates_kg` 의 `id:gate-<id>` 개체) ·
# `validate` 의 게이트 `gate-registry`(코드의 태그 집합 = 이 리터럴) · `doccheck` 의 총람 `id` 열 대조.
# 값에 주석(`#`)을 쓰지 않는다 — 파서가 주석을 지운 뒤 리터럴로 읽는다.
#
# 항목마다 넷을 적는다. `tier` 는 실행 계층(총람의 다섯), `tool` 은 판정 도구(`tools/<이름>.py` 의 모듈 이름 또는
# 파이썬 밖인 `starlark`·`bazel`), `ko` 는 한글 라벨, `desc` 는 무엇을 거부하는가 한 줄이다. 영문 라벨은 id 자신이다.
# 층은 항목마다 적지 않는다 — 게이트는 전부 프로세스 층이고 그 값이 `GATE_LAYER` 다.
GATE_LAYER = "process"
GATE_TIERS = ["shape", "verify", "analysis", "test", "human"]
GATE_TOOLS_OUTSIDE_PYTHON = ["starlark", "bazel"]
```
<!-- 인용 끝 -->
