---
id: https://agentic-knowledge-base.dev/id/chunk/9c5d9700-a87b-4566-945f-2b4dc268cd55
type: artifact
level: executable
title_ko: 절 waiver-columns (tools/kb_lib.py)
title: section waiver-columns in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/ee34751d-8520-4de7-a22b-b2a1136b9dbf
composite: {id: https://agentic-knowledge-base.dev/id/composite/ee34751d-8520-4de7-a22b-b2a1136b9dbf, title_ko: 절 복합체 waiver-columns (tools/kb_lib.py), title: section composite waiver-columns in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/9c5d9700-a87b-4566-945f-2b4dc268cd55, https://agentic-knowledge-base.dev/id/chunk/e0b9b281-fec0-43a8-ab40-b41e13278f6a, https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f, https://agentic-knowledge-base.dev/id/chunk/4292d5fd-0111-4512-921f-82e93540b998, https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884], part_of: https://agentic-knowledge-base.dev/id/composite/ff9d354a-d261-44a5-b7cd-7dd050de0370}
---
**절** — `tools/kb_lib.py` 의 절 `waiver-columns` 다. 면제 선언 (docs/waivers.md, agrtls-practices-review-2026-09-12 C)

**정의** — `_cells` · `load_waivers` · `_target_matches` · `waived` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 면제 선언 (docs/waivers.md, agrtls-practices-review-2026-09-12 C) ──────────────────────
# "오탐은 침묵이 아니라 선언으로": 코드 속 면제 대신 표 하나. 도구는 면제 대상을 집계에서 빼되 목록에 남긴다.
WAIVER_COLUMNS = ("게이트 id", "대상", "축", "사유", "판정자", "날짜")
WAIVER_AXES = ("파일", "stem", "상태")
```
<!-- 인용 끝 -->
