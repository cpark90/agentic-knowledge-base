# interpreter(hci) memory index

이 디렉토리는 2026-10-24 interpreter 2단계에서 옛 hci 역할 메모리 디렉토리에서 옮겨 왔다(Q-0061 Q143-a). 세션 시작 명령은 [세션 시작 사이클](session-start-cycle.md)을 본다.

- [user-deep-dive-preference](user-deep-dive-preference.md) — 유저는 깊은 조사도 hci가 직접; 반복 질문 패턴과 답이 있는 자리(tools·risks·`//kg:open`·`//kg:metrics`)
- [open-question-item-format](open-question-item-format.md) — 한 줄 질문은 답을 못 받는다(유저 2026-09-02); 질문 형식의 원본은 `harness/user/README.md`; 2026-10-24부터 백틱 slug·`agt:`·`id:` 옆에 한글 이름 정확 일치(`names` 검사, 결정은 composite `title_ko`)
- [대량 청크 생성 요령](bulk-generation-workflow.md) — 스크립트는 파일로, 참조는 라벨로 읽기, 대안은 원문대로
- [hci는 수행하지 않는다](approval-gate.md) — 2026-09-11 사건의 경위와 유저 교정 원문; 규칙의 자리는 `harness/agents/hci.md` 핵심 원칙 1·2
- [세션 시작 사이클](session-start-cycle.md) — 2026-10-24부터 역할 인자 `interpreter`·수신함 `to_interpreter/`·기동 `run-interpreter.sh`; 명령 순서 표(수치 없음), 되돌아오지 않은 것 보는 법
- [커밋 절차](commit-lane-procedure.md) — 유저 요청 시만, 남의 변경 판별, 전역 스코프 검사 셋 전후, 자기 작업분 검산
- [검토 규율](review-discipline.md) — 답을 다시 읽는다 · 참고와 도입을 가른다 · 유저 정의를 번역하지 않는다 · 편입 · 근사엔 한계 · 사슬 단위로 닫는다 · 삭제안의 범위는 걸린 줄을 읽고 적는다 (2026-10-06 개정)
- [반영 허가 신호](answered-tagging-gap.md) — Q24-b(2026-10-04): 유저가 "답 적었어"면 `답:`이 다 찼을 때만 hci가 `answered`를 대신 적는다; 알림 없이는 태깅 금지
- [수신 감시 정지](watcher-stoppage.md) — 원인 셋과 해결(0089→0090): 회수 끄기 환경·PID 중복 방지·턴마다 재무장; 시작 시 REAP=1 확인
- [frontier 해석 판정 금지](frontier-no-interpretive-closure.md) — Q65-b: 설계 공간의 확정·배제는 근거 문장이 직접 답할 때만; 대행 판정은 원문 대조 후 질문지로
- [동시 한도 대조](concurrency-check.md) — 분담 보고마다 역할별 1·전체 0~5 대조; ODD cmd는 카탈로그 합만 봄; fork·판정자 세션도 센다(0306→0307)
- [판정 기록의 Q66 예외](judge-record-exception.md) — Q170-c: 판정 기록은 한 번 50개 이하면 묻지 않음, 그 밖은 Q66대로
- [다른 프로젝트 부트스트랩](other-project-bootstrap.md) — 2026-11-01 smartbelley_vnv: 경계 읽기(원형 밖은 직접), 전사에서 옛 답 복구, 복제 골격(표준 라이브러리 channel_lint), 원형 질문지의 slug 이름은 composite.title_ko 정확 일치
