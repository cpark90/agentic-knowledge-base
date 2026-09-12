---
from: orchestrator
kind: notice
status: open
ref: agrtls-practices-review-2026-09-12.md
targets: [docs/waivers.md, docs/glossary.md, docs/feedback/handoff/README.md, tools/channel_lint.py, tools/doccheck.py, tools/chunk2kg.py, kb/dev/decision/p6-mass-fail-suspects-the-rule/conclusion.md, kb/dev/decision/p4-compression-repeat-is-split-signal/conclusion.md, kb/dev/decision/p6-gate-catalogue/conclusion.md, kb/dev/decision/p14-stage-pass-conditions/conclusion.md]
---

# agrtls 관행 검토 — 열 후보 반영 기록 (2026-09-12, 유저 답 "전부 반영")

`handoff/` lane이 이 항목으로 생겼으므로 handoff 항목 없이 원본 유저 항목을 `ref`한다 — 이 파일이 새 규약의 첫 인수 기록이다.

| 후보 | 반영 | 어디 |
|---|---|---|
| F handoff lane · verdict · rejected | 완료 | `handoff/README.md`(양식) · 채널 README·AGENTS·STYLEGUIDE §8·`hci.md` E절 · 카탈로그 `id:chan-handoff` · `channel_lint`(lane 어휘·handoff↔agents 쌍·`rejected`·`.wip`·placeholder·waivers) |
| P 소멸성 경로 인용 금지 | 완료 | `chunk2kg`(본문의 `docs/feedback/` → FAIL, deprecated 제외) · 위반 1건 `p14-stage-pass-conditions/conclusion` 정정(노트 14.1만 원본) |
| N 문서 현행성 게이트 | 완료 | `tools/doccheck.py` · `//:doccheck_test`(루트 md + docs/**, 채널 제외) · 첫 실행 위반 10건 전부 정정(앵커 1·옛 경로 2·생성물 경로 5·승인 큐 디렉토리 신설 `kb/ontology/proposals/README.md`·trace-kg 서술 1) |
| A 게이트 id · 해소 절차 · 실패 종류 | 완료 | 총람 `id`·`해소` 열 + 하네스 게이트 id 목록 · 결정 `p6-gate-catalogue` 결론에 id 단락 · 도구 종료 코드 1/2/3(`kb_lib` 상수) · 태그 통일(`chunk2kg-merge`·`odd2kg`·`taxonomy`·`gen-build`·`doccheck`) |
| B 용어집 tier | 완료 | `glossary.md` tier 열(1 기계 치환 20 · 3 문맥 공존 2 · — 10) · `consistency` ⑥은 tier 1만, 코드 속 "검증" 예외 삭제 |
| C waiver 선언 | 완료 | `docs/waivers.md`(channel 면제 6파일 · term-drift `pe-storage-layout`) · `channel_lint`·`consistency`가 읽어 집계에서 빼고 목록에 남김 |
| E 게이트 추가 절차 · 게이트 vs 보고 · 비-초록 기준선 | 완료 | `tools.md` §게이트를 추가할 때(절차·기준·실패 종류·waiver·기준선 표 4행) · 결정 `p6-mass-fail-suspects-the-rule`(세 청크, refines r-016) |
| Q 상한 압축 반복 = 분할 신호 | 완료 | 노트 4.10 분할 신호 표에 행 · 결정 `p4-compression-repeat-is-split-signal`(세 청크, refines r-014). 계수 도구는 없음(git 이력 뷰, 후속) |
| K skill 생성 | 방향 채택 | `tools.md` 활용 표 `gen_skills` 행 — 손으로 쓰지 않고 6단계 문서 생성으로. 지금 산출 없음 |
| M′ 세션 시작·커밋 절차 → hci 역할 메모리 | **hci 몫** | hci 자기 메모리(`.claude/agent-memory/hci/`) — orchestrator 쓰기 범위 밖. hci가 수행 |

## hci에 전달
1. **M′는 hci가 직접** — 명령/정상 기준선 2열 표, 없는 것도 없다고 적기, 커밋 전후 검사 셋·자기 작업분만.
2. **재판정 대상 1건**: `p6-gate-catalogue/conclusion`에 id 단락을 더하면서 오늘 찍은 판정자 표시(`process:label-judge-20260912`)가 물러났다 — 같은 판정자로 재판정 요청. 라벨은 그대로.
3. **비-초록 기준선**은 `tools.md` §게이트를 추가할 때 표가 원본 — 바뀌면 그 표를 고친다.
4. 승인 큐 `kb/ontology/proposals/`는 README만 있는 빈 디렉토리로 실재하게 했다(doccheck 해소).

## 답
(hci가 유저의 답을 채움)
