---
from: orchestrator
kind: notice
status: open
ref: handoff/connected-components-observations-2026-09-19.md
targets: [tools/metrics.py, kb/dev/decision/p14-stage-pass-conditions/, docs/roadmap.md, kb/dev/requirement/r-027-generated-documents-carry-provenance.md, kb/dev/requirement/r-028-generated-documents-share-one-form.md]
---

# 인수 기록 — `connected-components-observations-2026-09-19` (2026-09-27)

승인 항목 [`connected-components-observations-2026-09-19`](../connected-components-observations-2026-09-19.md)의 반영 계획을 2026-09-24~26에 수행했다. `bazel test //...` 23/23 PASS. 인수 기록을 `ref:`로 남기지 않아 handoff가 `open`으로 남았던 것을 채운다.

`tools/metrics.py`의 연결 성분·CQ20 후방 추적에서 `memory` plane을 제외했고 생성물 머리의 질의 줄에 "관측 제외"를 명시했다. 성분 6 → 4(그 뒤 vnv의 상향 링크로 → 2), CQ20 98.0 → 99.0%. 결정 `p14-stage-pass-conditions`에 근거 한 문장 — 관측은 실행의 부산물이고 append-only라 사후에 링크를 이을 길이 없으며 TIM에 `memory` 칸이 0개다; 관측을 세면 실행할수록 지표가 나빠지는데 그것은 고립이 아니라 기록의 축적이다. `docs/roadmap.md` 1단계 칸의 낡은 수치 둘을 생성물 인용으로 바꿨다. 계획 4번(권고)대로 `r-027`·`r-028`을 `documents-are-generated`에 `derivesFrom`(`restored`)으로 이었다. 남은 성분 1과 CQ20 잔여 7은 전부 판정 주석이다 — 제외 여부는 유저 항목으로 중계됐다.

hci가 handoff를 닫고 원장에 한 줄 적으면 된다. 재판정 대상 없음.
