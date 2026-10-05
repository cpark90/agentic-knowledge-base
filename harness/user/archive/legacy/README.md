# 옛 채널의 기록 (2026-10-03 이전)

2026-10-03에 채널이 `harness/`의 두 채널(질문지 · 수신함)로 바뀌었다. 그 전의 네 lane 채널
(`git:4c31fb2:docs/feedback/`)이 남긴 파일을 **옛 형식 그대로** 옮겨 둔 곳이다. 고치지 않는다.
게이트(`channel`·`doccheck`)의 대상이 아니다. 현행 프로토콜은 [`../../../README.md`](../../../README.md)다.

## 어디로 갔는가

| 옛 위치 | 지금 위치 | 무엇인가 |
|---|---|---|
| `docs/feedback/<주제>.md` | 이 디렉토리 | 유저 lane 항목 — 유저 ↔ hci. 다섯 절과 `## 답` |
| `docs/feedback/inquiries/` | `inquiries/` | 조사 lane — 유저의 조사 요청 원문과 hci의 답, 라벨 실험 응답(`label-exp-2026-09-30/`) |
| `docs/feedback/agents/` | `harness/channel/archive/legacy/agents/` | 에이전트 lane — orchestrator의 질문·보고·인수 기록(`ref: handoff/…`) |
| `docs/feedback/handoff/` | `harness/channel/archive/legacy/handoff/` | 인수인계 lane — hci → 담당 역할의 반영 계획 |
| `docs/feedback/README.md` · `TEMPLATE.md` | `old-protocol.md` · `old-template.md` | 옛 규약과 양식 |

## 읽는 법

- **파일 안의 상대 링크는 옛 배치 기준이다.** `handoff/<파일>`·`agents/<파일>`은 위 표의 지금 위치에서
  찾는다. `../<파일>`은 이 디렉토리의 파일이다.
- 옛 `status` 어휘는 다음과 같다. 유저 lane `open → approved | rejected`, 에이전트 lane
  `open → relayed → answered → closed`, 조사 lane `open → answered → closed`, 인수인계 lane `open → closed`.
  지금의 자리는 질문지의 `open → answered → closed`와 메시지의 `new → … → done`이다.
- 옮길 때 열려 있던 것은 넷이고 새 형식으로 이어졌다. 유저 판단 대기 `risk-grade-scale-stable`은
  질문지 `Q-0001`로, 판정지 `judge-rejudge-sheet`는 질문지 `Q-0002`로, 인수인계 `unification-program`과
  `judge-accuracy-rejudge`는 orchestrator 수신함의 `task` 메시지 `0001`·`0002`로 갔다. 나머지는 전부
  반영이 끝난 기록이다.
- 유저 결정의 원문 원장은 `purpose-statement.md` §8이다. 2026-10-03부터의 결정 원문은 닫힌 질문지
  (`harness/user/archive/`의 `Q-<번호>.md`)가 원장이다.
- 지식 그래프의 출처 개체는 이 파일들을 `git:<리비전>:<옛 경로>`로 가리킨다. 그 인용은 git 이력에서
  풀리므로 이 이동의 영향을 받지 않는다.
