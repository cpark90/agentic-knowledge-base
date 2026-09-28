---
from: orchestrator
kind: notice
status: open
ref: handoff/composite-order-2026-09-29.md
targets: [kb/dev/decision/p4-composite-order-is-declared/, defs/kb.bzl, tools/gen_build.py, tools/chunk2kg.py, kb/ontology/shapes/composite-order-shapes.ttl, defs/tests/, docs/rules.md, docs/tools.md, STYLEGUIDE.md]
---

# 인수 기록 — `composite-order-2026-09-29` (2026-09-30)

승인 항목 [`composite-order-2026-09-29`](../composite-order-2026-09-29.md)의 반영 계획 다섯을 전부 수행했다. 유저 답은 선택지 2 — **결정 복합체도 예외 없이 `ordered` 선언**(orchestrator 권장과 다른 쪽). `bazel test //...` 33/33 PASS.

| 계획 | 수행 |
|---|---|
| 1 orchestrator — 결정 본문 | 예외 조항을 뺐다 — 결론 표의 `kb_decision` 행은 "역할 순서를 **생성기가 `ordered` 인자로 선언**한다", 근거는 "생성 BUILD의 인자는 저작물이 아니라 생성물이므로 첨가가 아니다", 대안에 넷째(결정만 예외 — 유저 기각) 추가. `status: stable`, 도장 orchestrator |
| 2 developer — 생성기 | `gen_build.render_decisions`가 `ordered = [결론, 근거, 대안]`을 넣는다(원본 상수 `DECISION_READING_ORDER`). 206개 `conclusion.md`는 손대지 않았다. `kb_decision.ordered`는 **필수**(결정에 예외가 없음을 구조로 강제), `kb_composite.ordered`는 선택(순서를 요구하지 않는 손 복합체 41건이 그 자리) |
| 3 developer — `chunk2kg` | 추측 갈래(`fixed_part_order`·`DECISION_PART_STEMS`) 삭제. 순서의 출처는 `--ordered` 인자 또는 frontmatter `composite.ordered`뿐이고 둘이 다르면 드리프트로 거부 |
| 4 developer — shape | `composite-order-shapes`에 결정 예외 분기는 처음부터 없었다(`sh:targetClass co:List` 하나). 지울 것 없음 |
| 5 고정물 | 18 `unordered_no_order_test`(선언 없는 묶음 → `co:List` 없음, 추측이 되살아나면 깨진다) + 기존 14(불일치 → FAIL). shape 자체를 겨눈 검증은 vnv 케이스 `composite-order-shape`(자극 셋 + 통제, 2026-09-30 오전) |

실측: 복합체 253 · `co:List` 212(결정 206 + 시나리오 5 + 검증기 1) · 순서 없는 복합체 41 · `co:item` 636. ADR 뷰의 출력 순서는 그대로다.

## hci에 전달

원장에 "복합체 순서 = 선언, 예외 없음(2026-09-29 승인; 결정은 생성기가 선언)" 한 줄. 재판정 대상 없음(결정 셋은 orchestrator 저작·도장).
