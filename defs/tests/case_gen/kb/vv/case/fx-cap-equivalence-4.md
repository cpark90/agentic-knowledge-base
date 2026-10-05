---
id: https://agentic-knowledge-base.dev/id/chunk/d7c7749d-04b8-5e03-bf42-bf066422694e
type: schema
level: concrete
title_ko: 크기 1·종류 cyclic·표시 on의 고정물 청크 검사
title: Checking a fixture chunk of size 1, kind cyclic and flag on
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T00:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c002]
verifies: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c003]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c001]
---
**케이스** — 크기 1의 `cyclic` 청크 하나를 검사한다.

**자극** — 임시 파일 하나다. 이름은 `fx.md`이고 경로는 검증기가 정한다.

```yaml
files:
  fx.md: "size 1\nkind cyclic\nflag on\n"
```

**기대** — 검사가 `FAIL [chunk]`로 거부하고 게이트는 통과한다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [chunk]"
  - exit: 0
```

**실행 명령** — `python3 tools/chunk_lint.py --chunks {{fx.md}}; bazel test //kg:gate_test`

**표본 근거** — `sampling:equivalence` · `sampling:pairwise` · `sampling:factor` · `odd:outside` · seed `11` · 시나리오 `fx-cap` · 요인 `agt:fxCycle`. 값은 `tokens=1` · `kind=cyclic` · `flag=on`이고 판정 부류는 `reject`(keep 밖)다.
