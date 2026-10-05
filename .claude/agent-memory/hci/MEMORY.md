# hci memory index

- [user-deep-dive-preference](user-deep-dive-preference.md) — 유저는 깊은 조사도 hci가 직접; 반복 질문 패턴과 답이 있는 문서 위치(roadmap·tools·risks·open-questions)
- [open-question-item-format](open-question-item-format.md) — 유저 판단 요청은 질문지(`harness/user/`)에 다섯 가지(질문·기정·현재·답이 가르는 것·선택지)와 권장; 한 줄 질문은 답 못 받는다
- [대량 청크 생성 요령](bulk-generation-workflow.md) — 스크립트는 파일로, 참조는 라벨로 읽기, 대안은 원문대로
- [hci는 수행하지 않는다](approval-gate.md) — 답은 질문지에 원문으로 → `task` 로 정제해 orchestrator 에 → 채널 밖 편집 금지 (2026-10-03 개정)
- [세션 시작 사이클](session-start-cycle.md) — 명령/정상 2열 표(2026-10-03 개정: 수신함·질문지), 되돌아오지 않은 것 보는 법, push 인증
- [커밋 절차](commit-lane-procedure.md) — 유저 요청 시만, 남의 변경 판별, 전역 스코프 검사 셋 전후, 자기 작업분 검산
- [검토 규율](review-discipline.md) — 답을 다시 읽는다 · 참고와 도입을 가른다 · 유저 정의를 번역하지 않는다 · 편입 · 근사엔 한계 · 사슬 단위로 닫는다 (2026-10-03 개정)
- [반영 허가 신호](answered-tagging-gap.md) — Q24-b(2026-10-04): 유저가 "답 적었어"면 `답:`이 다 찼을 때만 hci가 `answered`를 대신 적는다; 알림 없이는 태깅 금지
- [수신 감시 정지](watcher-stoppage.md) — 원인 셋과 해결(0089→0090): 회수 끄기 환경·PID 중복 방지·턴마다 재무장; 시작 시 REAP=1 확인
- [frontier 해석 판정 금지](frontier-no-interpretive-closure.md) — Q65-b: 설계 공간의 확정·배제는 근거 문장이 직접 답할 때만; 대행 판정은 원문 대조 후 질문지로
