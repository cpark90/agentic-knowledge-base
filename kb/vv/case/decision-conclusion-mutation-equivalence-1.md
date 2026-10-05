---
id: https://agentic-knowledge-base.dev/id/chunk/21c8bb87-da8e-5df6-8bca-0c230e6d1d86
type: schema
level: concrete
title_ko: base 결정 스냅숏과 고정물 디렉토리 base 의 head 스냅숏을 revalidate 스냅숏 꼴로 비교한다
title: Comparing the base decision snapshot with the head snapshot in fixture directory base in the revalidate snapshot form
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T23:16:12+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/2f69c738-6a24-4c0b-9a14-29a44b25d6ee]
verifies: [https://agentic-knowledge-base.dev/id/chunk/fd6617a6-5387-4059-9014-faf6ad5effcf]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/d9289be5-8c2a-5ec6-99ca-9701586f131f]
---
**케이스** — 결론과 산출물 두 파일의 스냅숏 쌍을 자극으로 쓴다. head 스냅숏은 `defs/tests/revalidate/base/` 다.

**자극** — 견본 고정물 `defs/tests/revalidate/base/` 와 `defs/tests/revalidate/base/` 의 `conclusion.md`·`child.md` 다. 임시 파일은 없다. git·`bazel query` 를 부르지 않는다.

**기대** — 두 스냅숏이 같아 종료 0이고 재판정 링크 개체가 0이다.

```yaml
expect:
  - exit: 0
    contains:
      - "재판정 링크 개체 0"
```

**실행 명령** — `python3 tools/revalidate.py --base-files defs/tests/revalidate/base/conclusion.md defs/tests/revalidate/base/child.md --head-files defs/tests/revalidate/base/conclusion.md defs/tests/revalidate/base/child.md`

**표본 근거** — `sampling:equivalence` · seed `1` · 시나리오 `decision-conclusion-mutation`. 값은 `head=base`이고 판정 부류는 `accept`(keep 안)다.
