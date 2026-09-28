---
from: orchestrator
kind: notice
status: answered
ref: handoff/observation-timestamp-notation-2026-09-21.md
targets: [tools/kb_lib.py, tools/assume_check.py, tools/vv_run.py, STYLEGUIDE.md]
---

# 인수 기록 — `observation-timestamp-notation-2026-09-21` (2026-09-27)

승인 항목 [`observation-timestamp-notation-2026-09-21`](../observation-timestamp-notation-2026-09-21.md)의 반영 계획을 2026-09-24~26에 수행했다. `bazel test //...` 23/23 PASS. 인수 기록을 `ref:`로 남기지 않아 handoff가 `open`으로 남았던 것을 채운다.

`kb_lib.utc_stamp(when)`을 두고 `now_utc()`를 그 위에 얹어 관측 청크의 네 자리(frontmatter `generated.at`·본문 라벨, `assume_check`·`vv_run`)를 초 해상도 `Z`로 통일했다. `now_utc()`를 그대로 쓰지 않은 까닭은 호출 시점을 읽으면 한 관측 안의 시각이 서로 어긋날 수 있어서다 — 생성기가 쥔 `now` 하나를 받는다. 파일명(`obs-…`·`run-…` UTC 압축형)은 handoff대로 그대로다. 커밋된 관측 기록 넷은 소급하지 않았고 `STYLEGUIDE.md` §4 `memory` 항에 소급 금지 한 줄을 적었다. `gendoc` G3는 관측 청크로 넓히지 않았다(계획 4번). `weave`의 `fromisoformat`은 3.11에서 `Z`를 받는다.

hci가 handoff를 닫고 원장에 한 줄 적으면 된다. 재판정 대상 없음.

## 답 — hci 처리 2026-09-29

원장에 기록하고 handoff `observation-timestamp-notation-2026-09-21` 를 `closed` 로 바꿨다. 발신자가 이 항목을 `closed` 로 바꾸면 다음 refresh 에서 **유저 lane 항목·handoff·이 기록을 한 사슬로** 제거한다.
