---
id: https://agentic-knowledge-base.dev/id/chunk/158f0994-6283-4b5d-ba92-7602f61dddb1
type: decision
level: concrete
title_ko: hci는 조사·구체화·제안 요청을 받아 조사를 직접 하고 git 쓰기는 유저 요청 시 hci 또는 유저만 한다
title: hci takes investigation, specification and proposal requests and investigates directly, and git writes are made only by hci on the user's request or by the user
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/83f4773c-a35b-4548-b264-c2ea792eff82
composite: {id: https://agentic-knowledge-base.dev/id/composite/83f4773c-a35b-4548-b264-c2ea792eff82, title_ko: hci의 조사와 git 관리, title: Investigation and git management by hci}
---
**결론** — hci는 유저 소통 외에 조사와 git 관리를 맡는다. 옛 inspection 역할의 몫이다(유저 결정 2026-09-13).

- **유저의 요청은 조사·구체화·제안이다.** 유저는 hci 세션에서 말한다. hci가 요청을 검토·구체화한다. 유저의 결정이 필요한 지점은 질문지로 묻는다(`p11-harness-two-channels`).
- **조사는 hci가 직접 한다.** 조회 범위는 저장소 전체다. 조사는 지식을 고치지 않는다. 조사 결과가 반영을 요구하면 `task`로 orchestrator에 넘긴다.
- **git 쓰기(add·commit·push)는 hci가 유저 요청 시 하거나 유저가 한다.** orchestrator·developer·vnv는 git에 쓰지 않는다.
- 커밋 전에 셀프체크의 게이트 전체 PASS를 확인한다(`p6-self-check-before-completion`).

카탈로그(`kg/catalog-kg.ttl`)에는 git 권한을 나타내는 술어가 없다. git 권한은 역할 표의 `git` 열에만 적힌다. 이 규약을 판정하는 게이트는 없다. 리뷰 규범이다.
