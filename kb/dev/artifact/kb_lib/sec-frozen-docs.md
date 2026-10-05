---
id: https://agentic-knowledge-base.dev/id/chunk/67fe8f0c-7c7a-415f-b18f-71f20ba94969
type: artifact
level: executable
title_ko: 절 frozen-docs (tools/kb_lib.py)
title: section frozen-docs in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/513aca4d-e5f0-46c8-8d13-784c71691884
composite: {id: https://agentic-knowledge-base.dev/id/composite/513aca4d-e5f0-46c8-8d13-784c71691884, title_ko: 절 복합체 frozen-docs (tools/kb_lib.py), title: section composite frozen-docs in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/67fe8f0c-7c7a-415f-b18f-71f20ba94969, https://agentic-knowledge-base.dev/id/chunk/04fe68bc-58a1-45bd-ac00-78d263cbba81, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952, https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e, https://agentic-knowledge-base.dev/id/chunk/060d5b4a-ce00-45a6-893c-e9a0c787372f, https://agentic-knowledge-base.dev/id/chunk/90fe8a83-bd07-4bb1-bd2c-fcdad7d246b7, https://agentic-knowledge-base.dev/id/chunk/488bd7ba-cb14-4e6c-94f4-119987372f1f, https://agentic-knowledge-base.dev/id/chunk/e9c220ba-d7c1-4597-a620-d9ad84df3644, https://agentic-knowledge-base.dev/id/chunk/fd705af7-dd6d-489f-9d6f-620aecadba08], part_of: https://agentic-knowledge-base.dev/id/composite/e7e09bb4-4c00-411e-9e5d-857406143657}
---
**절** — `tools/kb_lib.py` 의 절 `frozen-docs` 다. 동결 문서 — 고치지 않는 원본 문서와 그 sha256 (유저 답 Q15-c, 결정 p0-service-is-a-three-layer-wiki "노트는 동결한다")

**정의** — `gates_bzl_path` · `load_gates` · `load_bzl_list` · `load_bzl_dict` · `load_bzl_scalar` · `load_tool_tags` · `gate_constant_name` · `scan_gate_tags` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 동결 문서 — 고치지 않는 원본 문서와 그 sha256 (유저 답 Q15-c, 결정 p0-service-is-a-three-layer-wiki "노트는 동결한다") ──
# 게이트 `frozen`(doccheck --frozen)이 파일의 sha256 을 이 값과 대조한다. 고치려면 이 상수도 같은 커밋에서 바꿔야 하므로
# 의도하지 않은 변경은 남지 않고 의도한 변경은 이 줄의 diff 로 드러난다. 정정은 유저 의도 대 노트의 어긋남이 확인된 자리에만 한다.
FROZEN_DOCS = {
    "docs/agent-knowledge-system-notes.md": "3e948a2cd19d49a2c4ebd70aa26ca8d12855c603e016aa5317bfc4cbf561f9c7",
}
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
