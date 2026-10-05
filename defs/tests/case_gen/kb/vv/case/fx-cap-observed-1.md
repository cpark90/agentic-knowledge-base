---
id: https://agentic-knowledge-base.dev/id/chunk/fd07a40e-2548-5a8a-9105-ad335cc5eee7
type: schema
level: concrete
title_ko: 크기 7·종류 nested·표시 on의 고정물 청크 검사
title: Checking a fixture chunk of size 7, kind nested and flag on
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T00:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c002]
verifies: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c003]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c001]
---
**케이스** — 크기 7의 `nested` 청크 하나를 검사한다.

**자극** — 임시 파일 하나다. 이름은 `fx.md`이고 경로는 검증기가 정한다.

```yaml
files:
  fx.md: "size 7\nkind nested\nflag on\n"
```

**기대** — 검사가 통과하고 게이트도 통과한다.

```yaml
expect:
  - exit: 0
  - exit: 0
```

**실행 명령** — `python3 tools/chunk_lint.py --chunks {{fx.md}}; bazel test //kg:gate_test`

**표본 근거** — `sampling:observed` · `origin:observed` · `odd:outside` · seed `11` · 시나리오 `fx-cap` · 실행 기록 `kb/vv/run/fx-run.md`. 값은 `tokens=7` · `kind=nested` · `flag=on`이고 판정 부류는 `accept`(keep 안)다.
