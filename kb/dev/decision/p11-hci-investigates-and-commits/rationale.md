---
id: https://agentic-knowledge-base.dev/id/chunk/8400535f-68c3-4b66-a9d1-cf69a879c770
type: decision
level: logical
title_ko: 조사와 git 관리는 초기 구축부터 inspection의 몫이었고 2026-09-13 유저 결정으로 hci에 이관됐다
title: Investigation and git management belonged to inspection from the initial build and moved to hci by the user's decision of 2026-09-13
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/83f4773c-a35b-4548-b264-c2ea792eff82
---
**근거** — 노트 11.2절의 개발 프로파일 카탈로그는 inspection(dispatch·git 관리, 전 plane 읽기)과 inspection worker(조사 전용, 수정 금지)를 둔다(`p11-dev-profile-role-permissions`). 저장소 초기 구축(2026-09-01)의 역할 표는 inspection을 별도 세션으로 두고 "조사 전용 + git 관리(add/commit/push, 유저 요청 시)"를 맡겼다. 다른 역할의 `git` 열은 전부 ✗였다.

같은 날 hci가 유일한 유저 창구로 섰다. hci의 접수 대상은 조사 요청·구체화·제안이었고 깊은 조사는 조사 lane으로 inspection에 위임했다. 이 형식은 agrtls 하네스의 피드백 채널을 옮긴 것이다(2026-09-01 커밋 이력).

2026-09-13 유저 결정으로 inspection 역할이 hci로 이관됐다. 카탈로그의 역할·스코프, 역할 표, ODD의 동시 에이전트 조건이 같은 커밋에서 바뀌었다. 이관 뒤 조사와 git이 hci의 몫이고 위임할 조사 역할이 없으므로 조사는 hci가 직접 한다.

hci가 수행하지 않는다는 유저 교정(2026-09-11)은 지식·도구의 편집을 막는다. 조사(읽기)와 git 쓰기는 그 편집이 아니다.

미확정: 유저가 inspection을 hci로 이관한 이유는 기록에서 확인하지 못했다. git 쓰기를 유저 요청 시로 한정한 이유도 확인하지 못했다.
