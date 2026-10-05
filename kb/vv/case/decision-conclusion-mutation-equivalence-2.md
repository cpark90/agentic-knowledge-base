---
id: https://agentic-knowledge-base.dev/id/chunk/d14eff56-2983-5271-a6fa-6328bd0a91a9
type: schema
level: concrete
title_ko: base 결정 스냅숏과 고정물 디렉토리 head 의 head 스냅숏을 revalidate 스냅숏 꼴로 비교한다
title: Comparing the base decision snapshot with the head snapshot in fixture directory head in the revalidate snapshot form
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T23:16:12+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/2f69c738-6a24-4c0b-9a14-29a44b25d6ee]
verifies: [https://agentic-knowledge-base.dev/id/chunk/fd6617a6-5387-4059-9014-faf6ad5effcf]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/d9289be5-8c2a-5ec6-99ca-9701586f131f]
---
**케이스** — 결론과 산출물 두 파일의 스냅숏 쌍을 자극으로 쓴다. head 스냅숏은 `defs/tests/revalidate/head/` 다.

**자극** — 견본 고정물 `defs/tests/revalidate/base/` 와 `defs/tests/revalidate/head/` 의 `conclusion.md`·`child.md` 다. 임시 파일은 없다. git·`bazel query` 를 부르지 않는다.

**기대** — 결론 본문이 바뀌어 종료 1이고 바뀐 끝이 결정 결론인 링크 개체 하나가 도착 끝에서 `suspect` 로 유도된다.

```yaml
expect:
  - exit: 1
    contains:
      - "(바뀐 끝이 결정 결론인 것 1)"
      - "| 도착 | suspect |"
```

**실행 명령** — `python3 tools/revalidate.py --base-files defs/tests/revalidate/base/conclusion.md defs/tests/revalidate/base/child.md --head-files defs/tests/revalidate/head/conclusion.md defs/tests/revalidate/head/child.md`

**표본 근거** — `sampling:equivalence` · `sampling:factor` · seed `1` · 시나리오 `decision-conclusion-mutation` · 요인 `agt:reasoningActionMismatch`. 값은 `head=head`이고 판정 부류는 `reject`(keep 밖)다.
