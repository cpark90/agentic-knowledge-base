---
id: https://agentic-knowledge-base.dev/id/chunk/d9289be5-8c2a-5ec6-99ca-9701586f131f
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 결론 본문 한 문장만 바꾼 결정 스냅숏 쌍의 재판정
title: Logical scenario stimulus — revalidating a decision snapshot pair that differs in one sentence of the conclusion body
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:16:12+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/92837b35-799b-52bf-993e-07d95d83e4ae
composite: {id: https://agentic-knowledge-base.dev/id/composite/92837b35-799b-52bf-993e-07d95d83e4ae, title_ko: 결론 본문 한 문장만 바꾼 결정 스냅숏 쌍의 재판정, title: Revalidating a decision snapshot pair that differs in one sentence of the conclusion body, ordered: [https://agentic-knowledge-base.dev/id/chunk/d9289be5-8c2a-5ec6-99ca-9701586f131f, https://agentic-knowledge-base.dev/id/chunk/32aefdda-b16d-5e90-b241-e94886de56d2, https://agentic-knowledge-base.dev/id/chunk/9b7251c8-6991-5c90-916f-b6faec9cdb72]}
---
**자극** — actor는 결정 결론을 편집하는 에이전트이고 action은 결론과 그것을 `refines` 하는 산출물로 된 스냅숏 둘을 `revalidate` 의 스냅숏 꼴로 비교하는 것이다. 표본 리비전 창은 합성 변이다(유저 답 Q38-c). 견본 고정물은 `defs/tests/revalidate/{base,head}/` 의 `conclusion.md`·`child.md` 이고 두 쌍은 결론 본문 한 문장만 다르다. head 결론 파일 이름은 `conclusion.md` 여야 결정 결론으로 인식된다. 순서는 base 스냅숏 고정 → head 스냅숏 선택 → 비교다. `keep()`은 산출물 본문과 `refines` 링크다. 변수는 head 스냅숏 `head` 하나이고 ODD 속성 `id:cond-repo-layout`(저장소 구조 — 한 청크는 한 파일이다)에 매인다. keep은 `base`(결론을 고치지 않음)다.

```yaml
keep:
  head: {odd: "id:cond-repo-layout", values: ["base"], reject: ["head"]}
cover:
  - {rule: equivalence, vars: [head]}
  - {rule: factor, var: head, factors: {"agt:reasoningActionMismatch": head}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/2f69c738-6a24-4c0b-9a14-29a44b25d6ee
  verifies: [https://agentic-knowledge-base.dev/id/chunk/fd6617a6-5387-4059-9014-faf6ad5effcf]
  title_ko: "base 결정 스냅숏과 고정물 디렉토리 ${head} 의 head 스냅숏을 revalidate 스냅숏 꼴로 비교한다"
  title: "Comparing the base decision snapshot with the head snapshot in fixture directory ${head} in the revalidate snapshot form"
  summary: "결론과 산출물 두 파일의 스냅숏 쌍을 자극으로 쓴다. head 스냅숏은 `defs/tests/revalidate/${head}/` 다."
  stimulus: "견본 고정물 `defs/tests/revalidate/base/` 와 `defs/tests/revalidate/${head}/` 의 `conclusion.md`·`child.md` 다. 임시 파일은 없다. git·`bazel query` 를 부르지 않는다."
  command: "python3 tools/revalidate.py --base-files defs/tests/revalidate/base/conclusion.md defs/tests/revalidate/base/child.md --head-files defs/tests/revalidate/${head}/conclusion.md defs/tests/revalidate/${head}/child.md"
  accept:
    prose: "두 스냅숏이 같아 종료 0이고 재판정 링크 개체가 0이다."
    expect:
      - {exit: 0, contains: ["재판정 링크 개체 0"]}
  reject:
    prose: "결론 본문이 바뀌어 종료 1이고 바뀐 끝이 결정 결론인 링크 개체 하나가 도착 끝에서 `suspect` 로 유도된다."
    expect:
      - {exit: 1, contains: ["(바뀐 끝이 결정 결론인 것 1)", "| 도착 | suspect |"]}
```
