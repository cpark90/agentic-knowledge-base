---
id: https://agentic-knowledge-base.dev/id/chunk/5d00d456-902e-4ec0-b6c8-3a1d112a6dd8
type: artifact
level: executable
title_ko: 절 line-budget-gate (tools/kb_lib.py)
title: section line-budget-gate in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/6b96d312-0c81-452d-8431-76ec85445dda
composite: {id: https://agentic-knowledge-base.dev/id/composite/6b96d312-0c81-452d-8431-76ec85445dda, title_ko: 절 복합체 line-budget-gate (tools/kb_lib.py), title: section composite line-budget-gate in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/5d00d456-902e-4ec0-b6c8-3a1d112a6dd8, https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5], part_of: https://agentic-knowledge-base.dev/id/composite/9b61f2e4-e29d-4fe0-8a4f-f1be5708e79a}
---
**절** — `tools/kb_lib.py` 의 절 `line-budget-gate` 다. 본문 줄 수의 상한 — plane 별 프로파일 파라미터 (STYLEGUIDE §4, p7-code-extraction-direction "예산")

**정의** — `body_line_limit` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 본문 줄 수의 상한 — plane 별 프로파일 파라미터 (STYLEGUIDE §4, p7-code-extraction-direction "예산") ───────────
# 42줄은 컨텍스트 한계 약 200줄의 1/5 이고 **저작된 산문**의 예산이다 (4.1절, d-0002). `artifact` plane 의 본문은
# 저작이 아니라 소스의 인용이라 그 예산이 인위적 분할을 부른다 — 42줄에 맞추려면 함수를 쪼개야 하고 그것은 지식이
# 코드를 망가뜨리는 것이다. 그래서 상한을 plane 마다 두고 `artifact` 만 값을 달리한다.
# `artifact` = 200: 표본 tools/kb_lib.py 의 실측 최대 본문이 185줄(179줄 함수 `check_gendoc`)이고, 200 은 42줄의
# 근거가 된 컨텍스트 한계 그 자체다 — 청크 하나가 컨텍스트 한 창을 넘지 않는다가 이 상한의 뜻이다.
LINE_BUDGET_GATE = "line-budget"  # 게이트 id — FAIL [line-budget] (표와 shape 가 갈림, validate check_line_budget)
MAX_BODY_LINES = 42  # 기본 (4.1절)
BODY_LINE_LIMITS = {"artifact": 200}
```
<!-- 인용 끝 -->
