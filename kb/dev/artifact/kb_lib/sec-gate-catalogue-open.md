---
id: https://agentic-knowledge-base.dev/id/chunk/cae833c9-afb4-421a-adc6-c944075ba989
type: artifact
level: executable
title_ko: 절 gate-catalogue-open (tools/kb_lib.py)
title: section gate-catalogue-open in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/81809a6f-d845-4673-8a0f-b53283ae332c
composite: {id: https://agentic-knowledge-base.dev/id/composite/81809a6f-d845-4673-8a0f-b53283ae332c, title_ko: 절 복합체 gate-catalogue-open (tools/kb_lib.py), title: section composite gate-catalogue-open in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/cae833c9-afb4-421a-adc6-c944075ba989, https://agentic-knowledge-base.dev/id/chunk/7cd8593d-71b7-426d-836f-f3ce1157dc54, https://agentic-knowledge-base.dev/id/chunk/4b222206-08d6-4720-9b58-644cd8cdd017, https://agentic-knowledge-base.dev/id/chunk/a7114439-153f-4210-a8f9-965a33ad05f4], part_of: https://agentic-knowledge-base.dev/id/composite/e7e09bb4-4c00-411e-9e5d-857406143657}
---
**절** — `tools/kb_lib.py` 의 절 `gate-catalogue-open` 다. 게이트 총람 표 — 손 문서(`docs/tools.md`) 안의 생성 구간 (유저 답 Q150-a)

**정의** — `gate_catalogue_table` · `gate_catalogue_block` · `splice_gate_catalogue` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 게이트 총람 표 — 손 문서(`docs/tools.md`) 안의 생성 구간 (유저 답 Q150-a) ────────────────────────────
# 총람 표는 등록부 `GATES` 의 투영이고 손으로 쓴 셀이 없다. 표 앞뒤의 산문은 손 문서로 남고 두 표지 사이의 구간만
# 생성한다. 생성기는 `gates2kg --catalogue <문서>` 이고 검사는 `doccheck --gates`(`//:doccheck_test`)가 같은 함수로
# 다시 그려 바이트로 비교한다 — 생성기와 게이트가 한 렌더러를 공유한다(`check_gendoc` 과 같은 자리).
# 게이트의 배경·해소·측정은 등록부가 아니라 `decision` 키가 가리키는 결정에 있고 표는 그 결정에 링크한다.
GATE_CATALOGUE_OPEN = ("<!-- 생성 시작: 게이트 등록부 defs/kb.bzl 의 GATES 투영 — 손으로 고치지 않는다. "
                       "재생성 python3 tools/gates2kg.py --catalogue docs/tools.md, 검사 //:doccheck_test -->")
GATE_CATALOGUE_CLOSE = "<!-- 생성 끝 -->"
GATE_CATALOGUE_HEADER = ("id", "게이트", "무엇을 거부하는가", "실행 계층", "판정 도구", "결정")
DECISION_DIR = "kb/dev/decision"
```
<!-- 인용 끝 -->
