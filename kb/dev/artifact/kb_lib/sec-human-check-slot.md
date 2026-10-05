---
id: https://agentic-knowledge-base.dev/id/chunk/bc02070e-9233-4ae6-8a48-37d3a1ee0362
type: artifact
level: executable
title_ko: 절 human-check-slot (tools/kb_lib.py)
title: section human-check-slot in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/45dfc4dd-c694-47a7-9a8c-6398612879db
composite: {id: https://agentic-knowledge-base.dev/id/composite/45dfc4dd-c694-47a7-9a8c-6398612879db, title_ko: 절 복합체 human-check-slot (tools/kb_lib.py), title: section composite human-check-slot in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/bc02070e-9233-4ae6-8a48-37d3a1ee0362, https://agentic-knowledge-base.dev/id/chunk/92ac1970-f252-48a0-b11a-fbaa774b2f4a, https://agentic-knowledge-base.dev/id/chunk/6553eed2-c1d9-41a4-b5c8-549f5d93193e, https://agentic-knowledge-base.dev/id/chunk/b743d72c-4fe1-4898-bd6f-aeed9063b344], part_of: https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893}
---
**절** — `tools/kb_lib.py` 의 절 `human-check-slot` 다. V&V 사다리 사슬 (게이트 `rung-before-descent` — 요구 r-023-rung-before-descent, 유저 결정 Q51-a · Q52-a)

**정의** — `human_check_criteria` · `vv_counterparts` · `rung_violations` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── V&V 사다리 사슬 (게이트 `rung-before-descent` — 요구 r-023-rung-before-descent, 유저 결정 Q51-a · Q52-a) ──────────
# 같은 높이의 V&V 검증 대응물(p8-scenario-ladder-rungs 가 높이마다 정한 대응물)이 있어야 다음 높이로 내려간다. 판정식은
# R1 사다리 사슬이다 — 높이마다 개발 하강 하나와 그 하강이 닿는 요구의 V&V 대응물을 짝짓는다.
#   functional→abstract  개발 하강(결정 결론 concrete → 요구 functional `refines`·`serves`)의 대상 요구를 derivesFrom 하는 목표가 있다
#   logical→concrete     logical·concrete 부분을 함께 가진 결정 복합체가 닿는 요구의 목표 가운데 합격 기준이 `refines` 하는 것이 있다
#   concrete→executable  executable 이 concrete 를 `refines` 하면 그 복합체가 닿는 요구의 목표 → 기준 가운데 검증기가 바인딩한 것이
#                        있다. 바인딩은 검증기 → 기준 `refines` 이거나 검증기 → 케이스 → 기준 `refines` 다. 사람 확인 기준만 가진
#                        요구는 면제다(Q26-a) — 사람 확인의 판정은 전방 추적 지표와 같은 `HUMAN_CHECK_SLOT` 이다
# 소비자는 게이트(validate check_rung_before_descent)와 지표(metrics vv_facts · forward_trace)다. 대응물의 집합을 한 곳에서 계산한다
HUMAN_CHECK_SLOT = "확인 절차"  # 사람 확인 합격 기준의 가운데 슬롯 (acceptance-criteria-body-shapes — 기계 판정이면 판정식)
RUNG_DESCENTS = ("functional→abstract", "logical→concrete", "concrete→executable")
```
<!-- 인용 끝 -->
