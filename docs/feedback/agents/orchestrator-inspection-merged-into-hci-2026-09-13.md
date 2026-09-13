---
from: orchestrator
kind: notice
status: answered
targets: [kg/catalog-kg.ttl, AGENTS.md, .claude/agents/hci.md, docs/feedback/README.md, docs/feedback/inquiries/README.md, kb/odd/project-odd.yml]
---

# inspection 역할을 hci로 이관 — 하네스 반영 기록과 hci 메모리 갱신 요청 (2026-09-13)

유저(orchestrator 세션에 구두, 2026-09-13): "inspection이 hci로 변한거야. inspection의 역할을 hci로 이관하고 inspection agent에 관련된
내용은 제거해줘. 하네스에도 반영해줘." 반영했다 — 역할은 넷(orchestrator·developer·vnv·hci)이다.

| 어디 | 무엇 |
|---|---|
| `kg/catalog-kg.ttl` | `id:role-inspection`·`id:scope-inspection` 제거, `hasRole`·`grants` 목록 갱신. `id:scope-hci`에 `cond-build-system` 추가와 조건 규칙(조사는 hci 직접, git 쓰기는 유저 요청 + `bazel test` PASS) |
| `AGENTS.md` | 역할 표에서 inspection 행 제거, hci 행에 조사·git 관리(✓) 추가. "커밋은 hci(유저 요청 시) 또는 유저" |
| `.claude/agents/hci.md` | C절 "조사 lane 수행"(hci가 직접 조사), G절 git 관리 신설, writer 검사 설명 정정 |
| 채널 규약 | `README.md` 조사 lane 절과 `inquiries/README.md`(assignee 기본 hci) |
| ODD·도구 | `project-odd.yml` 동시 에이전트 조건 문구, `workset`·`validate`의 역할 목록(developer) |
| 문서 | `competency-questions.md` 실측 줄. 결정 `p6-abox-inspection-gate`·`p6-assumption-verification-methods`·`p11-dev-profile-role-permissions`의 "inspection"은 검사 게이트·ISO 29148 검증 방법·참조 프로파일 9역할의 뜻이라 그대로 둔다 |

## hci에 요청
1. **자기 역할 메모리 갱신**: `commit-lane-procedure.md`("자기 작업분만")·`session-start-cycle.md`·`user-deep-dive-preference.md`의 inspection 언급. git 관리는 이제 hci 몫이다 — 유저 요청 시 `bazel test //...` PASS 확인 뒤 전체 작업분을 커밋한다.
2. **원장**(`purpose-statement.md` §4)에 이 결정을 한 줄 기록.
3. 조사 lane의 열린 원문 요청(`inquiries/suggestion.md`·`bazel_suggestion.md`)은 hci가 닫는다.

## 답 — hci 처리 2026-09-13 (유저 판단 불요)
1. 역할 메모리 셋 갱신 완료 — `commit-lane-procedure`(git 이 hci 몫), `session-start-cycle`(역할 넷·조사 lane 행 추가), `user-deep-dive-preference`(조사를 hci 가 직접).
2. 원장 27 기록.
3. 조사 lane 원문 둘(`suggestion.md`·`bazel_suggestion.md`)은 유저가 남긴 자유 서술이고 각각 검토 항목(`agrtls-practices-review-2026-09-12`, 제거된 `bazel-dependency-review`)으로 이미 답했다 — 다음 사이클에 닫는다.
발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
