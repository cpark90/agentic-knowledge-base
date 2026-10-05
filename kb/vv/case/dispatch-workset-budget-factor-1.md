---
id: https://agentic-knowledge-base.dev/id/chunk/5c6686a2-7697-55cc-85a9-631af3888d4c
type: schema
level: concrete
title_ko: 결정 p11-execution-mode-and-workset의 결론을 앵커로 준 vnv 작업 집합 뷰가 기본 예산에서 빌드되고 예산 10에서 FAIL [workset-budget]로 거부된다
title: The vnv workset anchored on the conclusion of the decision p11-execution-mode-and-workset builds within the default budget and is refused with FAIL [workset-budget] at budget 10
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T22:58:21+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/7db997bc-4f86-4b0c-aa3f-e941657a94a7]
verifies: [https://agentic-knowledge-base.dev/id/chunk/82e341ba-c47f-4677-8013-491082b24b6c]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/4e4de139-7e0c-512a-ba73-0263a7cf9a15]
---
**케이스** — 앵커를 준 뷰·앵커 없는 통제·예산을 좁힌 음성 자극(예산 10) 셋을 종료 코드로 판정한다.

**자극** — `//kg:workset`을 셋으로 빌드한다. 첫째는 앵커 + 기본 예산, 둘째는 앵커 없는 통제, 셋째는 같은 앵커 + 예산 10(음성 자극)이다.

**기대** — 첫째·둘째 빌드는 종료 0이다. 성공한 빌드 액션은 산출물 내용을 표준출력에 내지 않으므로 문구 대조는 실패하는 셋째에만 둔다. 셋째는 예산 10이 라벨 목록 길이보다 작아 `FAIL [workset-budget]`로 실패한다.

```yaml
expect:
  - exit: 0
  - exit: 0
  - exit: 1
    contains:
      - "FAIL [workset-budget]"
```

**실행 명령** — `bazel build //kg:workset --//kb:role=vnv --//kb:anchor=https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320; bazel build //kg:workset --//kb:role=vnv; bazel build //kg:workset --//kb:role=vnv --//kb:anchor=https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320 --//kb:budget=10`

**표본 근거** — `sampling:factor` · seed `1` · 시나리오 `dispatch-workset-budget` · 요인 `agt:worksetBudgetOverrun`. 값은 `budget=10`이고 판정 부류는 `reject`(keep 밖)다.
