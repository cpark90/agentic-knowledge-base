---
id: https://agentic-knowledge-base.dev/id/chunk/f8e5269c-a64e-4801-8d2b-36a72554a5ae
type: decision
level: concrete
title_ko: 검사를 약화하는 변경은 유저 승인 사항이고 면제는 판정자와 함께 docs/waivers.md에 선언한다
title: A change that weakens a check requires user approval, and a waiver is declared with its judge in docs/waivers.md
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-agrtls-practices-review}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:15:16+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4d357229-2256-4521-a837-0444b804d2a0
composite: {id: https://agentic-knowledge-base.dev/id/composite/4d357229-2256-4521-a837-0444b804d2a0, title_ko: 검사 약화는 유저 승인 사항이다, title: Weakening a check needs user approval}
---
**결론** — 검사를 약화하는 변경은 유저 승인 사항이다(`STYLEGUIDE.md` §7, 2026-09-01). 약화는 shape·게이트 코드의 변경만이다(유저 답 Q7-b, 2026-10-03). 검사의 삭제와 코드 속 예외의 추가가 그것이다. 같은 규칙이 검사가 사는 자리마다 적용된다.

| 자리 | 약화의 예 | 규약의 위치 |
|---|---|---|
| 게이트 도구 `tools/*.py` | 검사 삭제, 코드 속 예외 | `STYLEGUIDE.md` §7 |
| SHACL shape | `maxCount` 완화, `sh:in` 확장. shape는 강화만 한다 | `STYLEGUIDE.md` §2 |
| 링크 규칙 `defs/kb.bzl` | 허용 대상의 확대, 수준 일치 검사의 예외 | `p8-agent-verification-target` |

- **면제는 약화가 아니다.** 면제는 orchestrator가 판정하고 선언으로 공개한다. 코드에 두지 않고 `docs/waivers.md`에 게이트 id·대상·축·사유·판정자·날짜로 선언하며 판정자 열이 비면 안 된다. 도구는 면제 대상을 집계에서 빼되 목록에 남긴다.
- **게이트가 틀렸다고 판단한 에이전트는 게이트를 고치지 않는다.** 질문으로 올린다(`AGENTS.md` 게이트 실패 대응). FAIL이면 산출물을 고친다는 황금률 1이 기본이다.
- 대량 FAIL에서 규칙의 범위를 좁히는 판정은 `p6-mass-fail-suspects-the-rule`의 절차를 따르고 총람 행에 기록한다.
