---
id: https://agentic-knowledge-base.dev/id/chunk/4eed8c76-8291-4781-b89d-aa92a749110d
type: artifact
level: executable
title_ko: 절 gates-name (tools/kb_lib.py)
title: section gates-name in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e7e09bb4-4c00-411e-9e5d-857406143657
---
**절** — `tools/kb_lib.py` 의 절 `gates-name` 다. 게이트 등록부의 파생 (`GATES` → 모듈 속성 `<이름>_GATE`) — 상수를 손으로 두지 않는다 (M1, 2026-10-02)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 게이트 등록부의 파생 (`GATES` → 모듈 속성 `<이름>_GATE`) — 상수를 손으로 두지 않는다 (M1, 2026-10-02) ───────
# 단일 정의처는 `defs/kb.bzl` 의 `GATES`·`TOOL_TAGS` 리터럴이다(`RESIDENCY`·`EXTRACTED_SOURCES` 와 같은 해법).
# Starlark 는 파일을 읽지 못하므로 분석 시점에 쓰이는 표가 그쪽에 살고 파이썬은 리터럴을 읽어 파생한다.
# 파생은 **적재 시점**이고 이름은 id 를 대문자 밑줄로 옮긴 것이다 — `chunk` → `CHUNK_GATE` · `judge-log` →
# `JUDGE_LOG_GATE`. 리터럴에서 id 를 지우면 그 이름을 쓰는 도구가 적재 시점에 `AttributeError` 로 죽는다
# (음성 시험 ②, 유저 지시 2026-10-01) — 조용히 빈 태그로 돌지 않는다. 리터럴을 못 읽으면 ValueError 다.
GATES_NAME = "GATES"            # 게이트 등록부 리터럴의 이름
GATES_TAIL_NAME = "GATES_TAIL"  # 그 이어짐 리터럴의 이름 — 리터럴 하나가 추출 청크 하나라 인용 상한을 넘지 않게 id 순서로 잇는다
TOOL_TAGS_NAME = "TOOL_TAGS"    # 게이트가 아닌 도구 태그 목록 리터럴의 이름
GATE_LAYER_NAME = "GATE_LAYER"  # 게이트가 속한 서비스 층(전부 하나) 리터럴의 이름
GATE_ID_PREFIX = "gate-"        # 개체 IRI 접두사 (docs/rules.md §개체 IRI 접두사) — id:gate-<게이트 id>
VIEWS_NAME = "VIEWS"            # 생성 뷰 표(뷰 타깃 → 생성 도구) 리터럴의 이름 — 투영 그래프의 원본
VIEW_ID_PREFIX = "view-"        # 투영 개체 IRI 접두사 — id:view-<패키지·이름의 `/`·`:` 를 `-` 로> (agt:View)
SKILL_ID_PREFIX = "skill-"      # 투영 개체 IRI 접두사 — id:skill-<skill 이름> (agt:Skill, 원본 표는 SKILLS)
```
<!-- 인용 끝 -->
