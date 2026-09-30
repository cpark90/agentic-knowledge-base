---
id: https://agentic-knowledge-base.dev/id/chunk/cf44d030-4ea7-4aeb-b13c-87a4aa84ab0d
type: artifact
level: executable
title_ko: 절 -odd-range (tools/kb_lib.py)
title: section -odd-range in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/5804ea44-62d7-4b14-9187-5a7bb71425e1
composite: {id: https://agentic-knowledge-base.dev/id/composite/5804ea44-62d7-4b14-9187-5a7bb71425e1, title_ko: 절 복합체 -odd-range (tools/kb_lib.py), title: section composite -odd-range in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/cf44d030-4ea7-4aeb-b13c-87a4aa84ab0d, https://agentic-knowledge-base.dev/id/chunk/29b60ef2-eb29-4888-b4c0-c2e627041d68], part_of: https://agentic-knowledge-base.dev/id/composite/ff9d354a-d261-44a5-b7cd-7dd050de0370}
---
**절** — `tools/kb_lib.py` 의 절 `-odd-range` 다. OpenODD 식의 상한 — odd2kg 가 agt:conditionValue 에 "<INCLUDE_…> <종류>: <식>" 으로 적는다 (tools/odd2kg.py NUM·RANGE)

**정의** — `odd_upper_bound` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── OpenODD 식의 상한 — odd2kg 가 agt:conditionValue 에 "<INCLUDE_…> <종류>: <식>" 으로 적는다 (tools/odd2kg.py NUM·RANGE) ──
# Range `[a .. b] unit` 의 b, UpperBound `<= n unit` 의 n, `< n unit` 은 n 미만이라 정수면 n-1. LowerBound·Equal(범주)·unknown 은 상한이 없다
_ODD_RANGE = re.compile(r"\[\s*(-?\d+(?:\.\d+)?)\s*\.\.\s*(-?\d+(?:\.\d+)?)\s*\]")
_ODD_UPPER = re.compile(r"(?<![\w<>=])(<=?)\s*(-?\d+(?:\.\d+)?)")
```
<!-- 인용 끝 -->
