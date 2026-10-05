---
id: https://agentic-knowledge-base.dev/id/chunk/95ee4941-b202-434b-88e2-2448ea147bdd
type: artifact
level: executable
title_ko: 절 gate-catalogue-heading (tools/doccheck.py)
title: section gate-catalogue-heading in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/fc4042df-b620-47ee-b006-cf1ceb777197
composite: {id: https://agentic-knowledge-base.dev/id/composite/fc4042df-b620-47ee-b006-cf1ceb777197, title_ko: 절 복합체 gate-catalogue-heading (tools/doccheck.py), title: section composite gate-catalogue-heading in tools/doccheck.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/95ee4941-b202-434b-88e2-2448ea147bdd, https://agentic-knowledge-base.dev/id/chunk/7985ad2f-b7d8-45b2-8d1f-a688617bb614, https://agentic-knowledge-base.dev/id/chunk/c32e7981-57d1-4c87-bd5a-a41189661360, https://agentic-knowledge-base.dev/id/chunk/58750c29-c6bb-4d83-b464-517f160f955d], part_of: https://agentic-knowledge-base.dev/id/composite/b5da82da-f5cc-4c80-9fbf-d65784ffee7d}
---
**절** — `tools/doccheck.py` 의 절 `gate-catalogue-heading` 다. 게이트 총람의 투영 — 손 표의 `id` 열 대 GATES 리터럴 (M1 단일 정의처, 2026-10-02)

**정의** — `gate_catalogue_section` · `gate_catalogue_ids` · `check_gate_catalogue` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 게이트 총람의 투영 — 손 표의 `id` 열 대 GATES 리터럴 (M1 단일 정의처, 2026-10-02) ────────────────────

GATE_CATALOGUE_HEADING = "## 게이트 총람"  # docs/tools.md 의 절 머리 — 이 절이 등록부의 투영이다
GATE_CATALOGUE_ID_COLUMN = "id"            # 그 절 표의 열 이름 — 셀의 백틱 토큰이 게이트 id 다
BACKTICK_TOKEN = re.compile(r"`([a-z0-9][a-z0-9_-]*)`")
```
<!-- 인용 끝 -->
