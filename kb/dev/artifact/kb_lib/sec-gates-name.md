---
id: https://agentic-knowledge-base.dev/id/chunk/4eed8c76-8291-4781-b89d-aa92a749110d
type: artifact
level: executable
title_ko: 절 gates-name (tools/kb_lib.py)
title: section gates-name in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/cf732fdc-d595-4d0b-8344-6af01989d95c
composite: {id: https://agentic-knowledge-base.dev/id/composite/cf732fdc-d595-4d0b-8344-6af01989d95c, title_ko: 절 복합체 gates-name (tools/kb_lib.py), title: section composite gates-name in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/4eed8c76-8291-4781-b89d-aa92a749110d, https://agentic-knowledge-base.dev/id/chunk/04fe68bc-58a1-45bd-ac00-78d263cbba81, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952, https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e, https://agentic-knowledge-base.dev/id/chunk/90fe8a83-bd07-4bb1-bd2c-fcdad7d246b7, https://agentic-knowledge-base.dev/id/chunk/488bd7ba-cb14-4e6c-94f4-119987372f1f, https://agentic-knowledge-base.dev/id/chunk/e9c220ba-d7c1-4597-a620-d9ad84df3644, https://agentic-knowledge-base.dev/id/chunk/fd705af7-dd6d-489f-9d6f-620aecadba08], part_of: https://agentic-knowledge-base.dev/id/composite/e7e09bb4-4c00-411e-9e5d-857406143657}
---
**절** — `tools/kb_lib.py` 의 절 `gates-name` 다. 게이트 등록부의 파생 (`GATES` → 모듈 속성 `<이름>_GATE`) — 상수를 손으로 두지 않는다 (M1, 2026-10-02)

**정의** — `gates_bzl_path` · `load_gates` · `load_bzl_list` · `load_bzl_scalar` · `load_tool_tags` · `gate_constant_name` · `scan_gate_tags` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 게이트 등록부의 파생 (`GATES` → 모듈 속성 `<이름>_GATE`) — 상수를 손으로 두지 않는다 (M1, 2026-10-02) ───────
# 단일 정의처는 `defs/kb.bzl` 의 `GATES`·`TOOL_TAGS` 리터럴이다(`RESIDENCY`·`EXTRACTED_SOURCES` 와 같은 해법).
# Starlark 는 파일을 읽지 못하므로 분석 시점에 쓰이는 표가 그쪽에 살고 파이썬은 리터럴을 읽어 파생한다.
# 파생은 **적재 시점**이고 이름은 id 를 대문자 밑줄로 옮긴 것이다 — `chunk` → `CHUNK_GATE` · `judge-log` →
# `JUDGE_LOG_GATE`. 리터럴에서 id 를 지우면 그 이름을 쓰는 도구가 적재 시점에 `AttributeError` 로 죽는다
# (음성 시험 ②, 유저 지시 2026-10-01) — 조용히 빈 태그로 돌지 않는다. 리터럴을 못 읽으면 ValueError 다.
GATES_NAME = "GATES"            # 게이트 등록부 리터럴의 이름
TOOL_TAGS_NAME = "TOOL_TAGS"    # 게이트가 아닌 도구 태그 목록 리터럴의 이름
GATE_LAYER_NAME = "GATE_LAYER"  # 게이트가 속한 서비스 층(전부 하나) 리터럴의 이름
GATE_ID_PREFIX = "gate-"        # 개체 IRI 접두사 (docs/rules.md §개체 IRI 접두사) — id:gate-<게이트 id>
GATES_BZL_ENV = "KB_GATES_BZL"  # 리터럴 파일의 경로를 하네스가 직접 주는 자리 (runfiles 밖 실행)
# 게이트 태그의 표기 — 도구가 찍는 `FAIL [<id>]` 꼴과 메시지 머리의 `[<id>]` 꼴 둘이다. 게이트 `gate-registry`
# 가 이 두 정규식으로 코드 전수를 훑어 리터럴 밖의 태그를 잡는다.
GATE_TAG_KINDS = ("FAIL", "WARN", "CONFIG", "SKIP", "WAIVED", "PASS")
GATE_TAG_RE = re.compile(r"\b(?:%s)\s+\[([a-z][a-z0-9-]{1,30})\]" % "|".join(GATE_TAG_KINDS))
GATE_TAG_HEAD_RE = re.compile(r"^\[([a-z][a-z0-9-]{1,30})\]\s")  # 뒤에 공백 — 정규식의 문자 클래스(`[a-z]…`)와 가른다
















GATES = load_gates()
TOOL_TAGS = load_tool_tags()
for _gate_id in GATES:  # 파생 — 상수를 손으로 두지 않는다. 리터럴에 없는 이름은 적재 시점에 없다
    globals()[gate_constant_name(_gate_id)] = _gate_id
for _tool_tag in TOOL_TAGS:  # 도구 태그는 `<이름>_TAG` 로 갈린다 — 게이트가 아니라는 사실이 이름에 있다
    globals()[_tool_tag.replace("-", "_").upper() + "_TAG"] = _tool_tag
```
<!-- 인용 끝 -->
